# Package A — Frontmatter & Cycle Tooling: Spec, Architecture, and ACs

Source directive: `docs/cycles/streamlining-directive.md` (F1 + F4, plus F2's
transform script, which rides in Package A).

This document is tracker/spec-class for a tooling package. `docs/**` is out of
the frontmatter in-scope set per `policies/document-metadata-policy.md`, so this
file carries no lifecycle frontmatter.

## 1. Intent

Replace hand-executed methodology ceremony with scripts that are cheap to run
and self-verifying:

- **F1** — frontmatter status flips stop being hand-edits. A script performs the
  agreed-flip and proves its own commit touched nothing but frontmatter; a
  pre-commit hook performs the `agreed → in-review` flip automatically when an
  agreed document's *content* is edited, so the lifecycle rule in
  `policies/document-metadata-policy.md` is enforced by construction rather than
  by memory.
- **F4** — cycle opening stops being manual SHA bookkeeping. `cycle-open` reads
  reviewed SHAs from git, writes the directive skeleton, and emits the exact
  reviewed revisions as an upload bundle. `bundle` computes the reference
  closure from entry-point context-sets, replacing hand-maintained bundle lists.
- **F2 (transform only)** — a mechanical, status-preserving legacy-header →
  YAML-frontmatter transform, split into a `--plan` step (mechanical detection +
  human judgment fields) and an `--apply` step. Package B consumes it; Package A
  only builds and tests it.

Non-goals for Package A: running the migration (Package B), editing any `agreed`
document, editing `MANIFEST.md`, `bin/gate-open`, and installing the shim into
`wne-crm`. All are sequenced later by the directive.

## 2. Architecture

### 2.1 Placement and portability

Per the directive's architecture decision, scripts live canonically in
`/ai/bin/` and are never copied into project repos. Consequences that constrain
the design:

- **No hardcoded project paths.** Every path is derived at runtime.
- **Repo root comes from the invoking repo** (`git rev-parse --show-toplevel`
  against the process cwd), never from the location of the script.
- **In-scope globs are read from the metadata policy**, not baked into code.
  The policy lives in the methodology home; the globs are evaluated against the
  invoking repo. Globs matching nothing are inert, which is what makes the same
  glob set correct for a project repo (where only `specs/**` typically matches).
- **Methodology home discovery** order, used by both the shim and the Python
  code: `$AI_METHODOLOGY_HOME` → the invoking repo itself if it contains
  `bin/check-frontmatter` (the self-hosted methodology repo) → a sibling
  directory named `ai` (`<parent-of-repo-root>/ai`). If none resolves, fail
  loudly with the fix in the message. Never guess further.

### 2.2 Language and dependencies

Python 3 (>= 3.9), standard library only. No PyYAML: the frontmatter dialect is
a documented subset (§3.1) parsed by our own code, which also lets us produce
precise, policy-shaped error codes. Tests use `unittest`, also stdlib.

Rationale over shell: the hook must parse and rewrite YAML-ish blocks, mutate
the git index safely, and be unit-testable. macOS ships bash 3.2; that is a bad
substrate for this. Rationale over Node: no package manifest or install step in
this repo, and none wanted for a hook.

### 2.3 File layout

```
bin/
  aimeta/
    __init__.py
    frontmatter.py        # parse / render / validate the frontmatter dialect
    scope.py              # in-scope globs read from the metadata policy
    repo.py               # git helpers, repo root, methodology home, role slugs
  check-frontmatter       # validator + hook engine (--staged)
  flip-agreed             # self-verifying frontmatter-only status commit
  cycle-open              # directive skeleton + reviewed-revision bundle
  bundle                  # reference-closure over entry-point context-sets
  migrate-frontmatter     # F2 transform: --plan then --apply
  install-hooks           # writes the pre-commit shim into a target repo
  tests/
    helpers.py            # temp-git-repo fixture helpers
    test_*.py
```

Executables are extensionless, `chmod 0755`, shebang `#!/usr/bin/env python3`,
and add their own directory to `sys.path` so `import aimeta` resolves without
installation.

### 2.4 Exit-code convention (all CLIs)

| code | meaning |
| --- | --- |
| 0 | success (including "nothing to do") |
| 1 | policy/validation failure — the thing being checked is wrong |
| 2 | usage error (bad arguments) |
| 3 | precondition failure — refused to act (dirty index, file exists, unresolved TODOs) |
| 4 | self-verification failure — the tool's own output was not what it promised |

Human-readable diagnostics go to stderr, one finding per line, prefixed with a
severity word and a bracketed code: `ERROR path: [code] message`.

## 3. Component contracts and acceptance criteria

Each AC is a behavioral statement. The Test Designer writes one or more tests
per AC and labels them with the AC id.

### 3.1 `aimeta.frontmatter`

The dialect: a document has frontmatter iff its first line is exactly `---`.
The block ends at the next line that is exactly `---`. Inside the block, per
line: blank, a `#` comment, `key: value`, or a `- item` continuation of the
preceding key. Values: empty or `null` → `None`; `[a, b]` → list of strings;
quoted (`"` or `'`, matching) → the unquoted string; anything else → the
verbatim trimmed string.

API:

```python
STATUSES = {"draft", "in-review", "agreed", "superseded", "deprecated"}
EXCLUDED_FIELDS = {"version", "last-modified", "author", "changelog"}
RESERVED_AUDIENCE = {"all-roles", "human"}
FIELD_ORDER = ["status", "last-reviewed", "audience", "superseded-by"]
LAST_REVIEWED_RE = r"^reviews/\S+\.md @ [0-9a-f]{7,40}$"

class Document:
    fields: dict          # insertion-ordered; None for null
    body: str             # everything after the closing fence line
    has_frontmatter: bool
    errors: list[Finding] # structural parse findings only

class Finding:
    code: str
    message: str

def parse_text(text: str) -> Document
def render(doc: Document) -> str
def with_fields(doc: Document, updates: dict) -> Document   # returns a new Document
def validate(doc: Document, *, path: str, role_slugs: set[str],
             grandfathered: bool = False) -> list[Finding]
```

- **AC-FM-1** `parse_text` on a document with frontmatter returns
  `has_frontmatter == True`, the parsed `fields`, and a `body` that is exactly
  the original text after the closing `---` line (the newline ending the fence
  line is consumed; nothing else is stripped).
- **AC-FM-2** `parse_text` on a document with no leading `---` returns
  `has_frontmatter == False`, empty `fields`, and `body` equal to the entire
  input.
- **AC-FM-3** A document whose first line is `---` with no closing `---`
  produces a finding with code `unclosed-frontmatter`, and does not raise.
- **AC-FM-4** Values parse per the dialect: `null` and empty → `None`;
  `[a, b]` → `["a", "b"]`; block `- a` / `- b` lines → `["a", "b"]`; a quoted
  scalar loses exactly its outer matching quotes; `reviews/x.md @ abc1234`
  parses as that verbatim string.
- **AC-FM-5** A repeated key produces a finding with code `duplicate-key`. A
  non-blank, non-comment line inside the block that is neither `key: value` nor
  a `- item` continuation produces `malformed-frontmatter`.
- **AC-FM-6** `render(parse_text(t)).body-part` preserves the body byte for
  byte: for any document `t`, `parse_text(render(parse_text(t))).body ==
  parse_text(t).body`.
- **AC-FM-7** `render` emits known fields in `FIELD_ORDER` first, then any
  unknown fields in their original relative order. `None` renders as `null`; a
  list renders inline as `[a, b]`. Unknown fields (e.g. the context-set
  composition fields `context-set`, `purpose`, `include-when`, `depends-on`)
  survive a parse/render round trip.
- **AC-FM-8** `with_fields` returns a new `Document` with the updates applied
  and the original left unmutated; a key mapped to `None` is set to null (it is
  not deleted).

`validate` findings (each is a distinct code, all lower-case kebab):

- **AC-FM-9** `missing-frontmatter` when `has_frontmatter` is false.
- **AC-FM-10** `missing-status` when `status` is absent or null;
  `invalid-status` when its value is outside `STATUSES`.
- **AC-FM-11** `missing-last-reviewed` when the key is absent entirely (null is
  permitted, absence is not); `invalid-last-reviewed` when a non-null value
  does not match `LAST_REVIEWED_RE`.
- **AC-FM-12** `agreed-without-review` when `status: agreed` and
  `last-reviewed` is null — **unless** `grandfathered=True`, in which case the
  finding is not emitted.
- **AC-FM-13** `missing-audience` when absent or null; `empty-audience` when an
  empty list; `invalid-audience` (one finding per offending value, naming the
  value) when a value is neither in `RESERVED_AUDIENCE` nor in `role_slugs`. A
  bare string audience is treated as a one-element list, not an error.
- **AC-FM-14** `superseded-without-pointer` when `status: superseded` and
  `superseded-by` is null or absent; `superseded-by-without-status` when
  `superseded-by` is non-null and `status` is not `superseded`. Per the
  policy's null semantics, `superseded-by: null` on a non-superseded doc is
  permitted and is not a finding.
- **AC-FM-15** `excluded-field` (one per field, naming it) for any key in
  `EXCLUDED_FIELDS`.
- **AC-FM-16** A fully valid agreed document (`status: agreed`,
  `last-reviewed: reviews/x.md @ <sha>`, `audience: [all-roles]`,
  `superseded-by: null`) yields zero findings.

### 3.2 `aimeta.scope`

```python
def parse_in_scope_globs(policy_text: str) -> list[str]
def load_globs(methodology_home: pathlib.Path) -> list[str]
def matches(relpath: str, globs: list[str]) -> bool
class ScopeError(Exception)
```

- **AC-SC-1** `parse_in_scope_globs` extracts the backticked entries of the
  bullet list that follows the line containing `In scope (frontmatter
  required)` and stops at the line containing `Out of scope`. For the current
  `policies/document-metadata-policy.md` this yields exactly:
  `policies/**`, `roles/**`, `context-sets/**`, `boundaries/**`, `skills/**`,
  `specs/**`, `operating-model.md`, `README.md` — in document order.
- **AC-SC-2** If the in-scope section is absent, or contains no backticked
  entries, `parse_in_scope_globs` raises `ScopeError`. It never falls back to a
  built-in list — failing closed is required, because a silent fallback would
  let a policy edit stop being enforced without anyone noticing.
- **AC-SC-3** `matches` treats `dir/**` as "any path under `dir/`, at any
  depth" and any other glob as an `fnmatch` against the whole relative path.
- **AC-SC-4** Only `.md` files are ever in scope: `matches("policies/x.txt",
  globs)` is false even though `policies/**` matches its prefix. (Stated
  assumption: frontmatter is a markdown convention; the policy says
  "documents".)
- **AC-SC-5** `matches` is false for paths outside every glob (e.g.
  `MANIFEST.md`, `OPEN-ITEMS.md`, `docs/cycles/x.md`, `reviews/x.md`,
  `CLAUDE.md`, `.claude/skills/README.md`).

### 3.3 `aimeta.repo`

```python
class GitError(Exception)
def git(*args, cwd) -> str                  # stdout, stripped; raises GitError on nonzero
def repo_root(start=None) -> pathlib.Path
def methodology_home(root) -> pathlib.Path  # §2.1 order; raises GitError-like LookupError
def last_commit_sha(root, relpath) -> str | None
def file_at_rev(root, rev, relpath) -> str | None    # None if absent at that rev
def staged_entries(root) -> list[tuple[str, str]]    # (status letter, relpath)
def role_slugs(root, home) -> set[str]
def disposition_paths(root) -> set[str]
DISPOSITION_PATH = "reviews/frontmatter-disposition.md"
```

- **AC-RP-1** `repo_root` returns the top level of the repo containing the cwd,
  and raises when run outside a repo.
- **AC-RP-2** `methodology_home` honours `$AI_METHODOLOGY_HOME` first; falls
  back to the invoking repo when it contains an executable
  `bin/check-frontmatter`; then to a sibling directory named `ai`; and raises
  `LookupError` naming both fixes when none resolves. A set-but-invalid
  `$AI_METHODOLOGY_HOME` (no `bin/check-frontmatter`) falls through to the next
  candidate rather than failing.
- **AC-RP-3** `last_commit_sha` returns the full SHA of the most recent commit
  touching the path, and `None` for an untracked path.
- **AC-RP-4** `file_at_rev` returns file content at a revision and `None` when
  the path does not exist there (it does not raise). `rev` may be `:` -prefixed
  index notation (`file_at_rev(root, ":", path)` reads the staged blob).
- **AC-RP-5** `staged_entries` returns `(letter, path)` for the staged set
  using `git diff --cached --name-status -z` against HEAD (and against the
  empty tree when HEAD does not exist), with rename entries reported as `R`
  carrying the new path.
- **AC-RP-6** `role_slugs` is the set of `roles/*.md` basenames without
  extension, taken from the invoking repo when it has a `roles/` directory and
  otherwise from the methodology home.
- **AC-RP-7** `disposition_paths` parses every backticked `*.md` path out of
  `reviews/frontmatter-disposition.md` and returns them; when that file does
  not exist it returns the empty set (per the policy's "if no disposition list
  exists, the clause does not apply").

### 3.4 `bin/check-frontmatter`

```
check-frontmatter [PATH...]        # validate working tree; no mutation
check-frontmatter --staged         # hook mode: auto-flip, then validate the index
check-frontmatter --all            # validate every in-scope file in the repo
options: --no-flip (validate only, in --staged mode)
```

Default with no arguments and no flags: `--all`.

- **AC-CF-1** In default mode, in-scope files with valid frontmatter produce no
  output and exit 0; a file with findings prints one `ERROR <path>: [code]
  <message>` line per finding and exits 1.
- **AC-CF-2** Out-of-scope paths are ignored entirely, even when named
  explicitly on the command line (they are reported as skipped, exit 0).
- **AC-CF-3** In default mode nothing is written: file mtimes and contents are
  unchanged even when findings exist.
- **AC-CF-4** In `--staged` mode, for a staged in-scope file whose staged
  frontmatter says `status: agreed` and whose staged **body** differs from its
  body at HEAD, the tool rewrites the staged blob to `status: in-review` with
  `last-reviewed: null`, leaves every other field untouched, and re-stages it —
  so the resulting commit contains the flip. It prints
  `FLIPPED <path>: agreed -> in-review (content edit)` and exits 0 if there are
  no validation findings.
- **AC-CF-5** A staged change that touches **only** frontmatter (body at HEAD
  byte-identical to staged body) is never flipped — this is the policy's
  status-transition exemption, and it is what keeps `flip-agreed` from fighting
  the hook.
- **AC-CF-6** A staged file whose staged status is not `agreed` is never
  flipped, whatever HEAD says.
- **AC-CF-7** A newly added file (absent at HEAD) is never flipped; it is still
  validated, so adding a file claiming `agreed` with `last-reviewed: null` and
  no grandfather entry fails with `agreed-without-review`.
- **AC-CF-8** Staged deletions are skipped entirely (no read, no finding).
- **AC-CF-9** The flip mutates the **index** (`git hash-object -w` +
  `git update-index --cacheinfo`), and additionally rewrites the worktree file
  only when the worktree content equals the pre-flip staged content. With a
  partially-staged file (worktree differs from index) the worktree is left
  untouched and the index still carries the flip; the tool prints a `NOTE`
  naming that the worktree copy still claims `agreed`.
- **AC-CF-10** `--staged --no-flip` performs validation against the index and
  never mutates index or worktree.
- **AC-CF-11** Validation findings in `--staged` mode exit 1 (blocking the
  commit) and the message names `git commit --no-verify` as the deliberate
  override.
- **AC-CF-12** The grandfather clause is applied: a file listed in
  `reviews/frontmatter-disposition.md` may carry `status: agreed` with
  `last-reviewed: null` without a finding; the same file, unlisted, fails.
- **AC-CF-13** The in-scope set is derived from the metadata policy at runtime:
  with the policy's in-scope list edited to drop `skills/**`, a bad
  `skills/x.md` stops being reported. (Proves AC-SC-1 is wired through, not
  re-implemented.)

### 3.5 `bin/flip-agreed`

```
flip-agreed PATH --review "reviews/<file>.md @ <sha>"
             [--status agreed|superseded|deprecated] [--superseded-by PATH]
             [--message MSG] [--no-commit]
```

`--status` defaults to `agreed`. The three permitted statuses are exactly the
policy's "status transitions", which are exempt from the edit-flips-in-review
rule; the tool refuses any other status so it cannot be used to launder a
content edit.

- **AC-FA-1** Happy path: on an in-scope file with `status: in-review`, the tool
  sets `status: agreed` and `last-reviewed: <value>`, leaves all other fields
  and the body untouched, stages, and creates exactly one commit containing
  exactly that one file.
- **AC-FA-2** Self-verification: before committing, the tool asserts the staged
  body equals the HEAD body; if a content difference is present it restores the
  file, unstages, prints `[frontmatter-only-violation]`, and exits 4 without
  committing.
- **AC-FA-3** It refuses (exit 3) when the index already holds other staged
  changes, so the commit cannot pick up unrelated work.
- **AC-FA-4** It refuses (exit 3) when the target file has unstaged body edits
  in the worktree.
- **AC-FA-5** `--review` is required for `--status agreed` (exit 2 otherwise);
  the value must match `LAST_REVIEWED_RE` (exit 1), the review artifact must
  exist in the worktree (exit 1), and the SHA must resolve to a commit via
  `git rev-parse --verify <sha>^{commit}` (exit 1).
- **AC-FA-6** `--status superseded` requires `--superseded-by` (exit 2), and
  writes that field. `--status deprecated` clears nothing else and is accepted
  without `--review`.
- **AC-FA-7** The resulting frontmatter is validated before commit; any finding
  aborts with exit 1 and no commit (e.g. a doc whose `audience` was already
  invalid is not silently promoted to agreed).
- **AC-FA-8** Refuses out-of-scope paths, missing files, and files without
  frontmatter (exit 1), naming which.
- **AC-FA-9** `--no-commit` performs every check and leaves the change staged
  without committing; exit 0.
- **AC-FA-10** Default commit message is
  `docs(<relpath>): status -> <status>`, with the review pointer on a body
  line; `--message` overrides the subject.
- **AC-FA-11** Post-commit re-verification: the tool re-reads the committed
  file, re-validates it, and confirms `HEAD` touches exactly one path; a
  mismatch exits 4 (the commit is left in place and the failure is reported —
  the tool does not rewrite history).

### 3.6 `bin/cycle-open`

```
cycle-open (--cycle N | --name SLUG) [--title T] [--out DIR]
           [--bundle ENTRY]... [--date YYYY-MM-DD] [--allow-dirty] [PATH...]
```

- **AC-CO-1** Writes `docs/cycles/cycle-<N>-directive.md` for `--cycle N`, or
  `docs/cycles/<SLUG>-directive.md` for `--name SLUG`; exactly one of the two
  is required (exit 2).
- **AC-CO-2** Refuses to overwrite an existing directive (exit 3).
- **AC-CO-3** The skeleton matches the format in `skills/spec-review-cycle.md`:
  an `# Cycle <n> Directive — <title>` heading, a `Date:` line, a
  `Documents in scope:` list of `- <path> @ <full sha>` entries, a
  `## Decisions` section containing one commented placeholder decision entry
  with the `Finding: / Resolution: / Dictated wording:` fields, a
  `## Deferred / out of scope` section, and an `## Execution notes` section.
- **AC-CO-4** Each in-scope SHA is the full SHA of the last commit touching
  that path, read from git — never invented, never abbreviated.
- **AC-CO-5** Refuses (exit 3) when any named document has uncommitted
  modifications, because its recorded SHA would not describe the uploaded
  content; `--allow-dirty` downgrades this to a `WARN` line.
- **AC-CO-6** Refuses (exit 1) an untracked or non-existent path, naming it.
- **AC-CO-7** Emits the reviewed-revision bundle: for each document, the
  content at its recorded SHA (`git show <sha>:<path>`, i.e. the reviewed
  revision, not the worktree) written to `<out>/<path with / replaced by __>`,
  plus `<out>/BUNDLE.txt` listing `<path> @ <sha>` per line and the directive
  path. Default `--out` is `.cycle-bundles/<directive-stem>/`.
- **AC-CO-8** When the bundle output directory is not ignored by git, it prints
  a `WARN` naming the risk (uploads becoming tracked files) but still writes.
- **AC-CO-9** `--bundle ENTRY` expands via the same closure as `bin/bundle` and
  unions the result with explicit `PATH` arguments, de-duplicated, order
  stable.
- **AC-CO-10** `--date` fixes the `Date:` line (determinism for tests);
  otherwise today's local date in `YYYY-MM-DD`.
- **AC-CO-11** The tool writes only the directive and the bundle directory. It
  does not stage, commit, or modify any document.

### 3.7 `bin/bundle`

```
bundle [--format list|json|concat] [--max-depth N] [--why] [--strict] ENTRY...
```

An `ENTRY` is a context-set name (`base` → `context-sets/base.md`) or a
repo-relative path.

- **AC-BN-1** Closure edges are (a) `depends-on:` frontmatter entries resolved
  to `context-sets/<name>.md`, and (b) backticked repo-relative `*.md` paths in
  the document body that exist as files in the repo. Both are followed
  transitively.
- **AC-BN-2** Output is deterministic: breadth-first by depth from the entry
  points, ties broken lexicographically, entry points first, no duplicates.
- **AC-BN-3** Reference cycles terminate (a mutual `depends-on` pair yields two
  entries, not a hang).
- **AC-BN-4** `--max-depth N` truncates the walk at depth N; depth 0 yields only
  the entry points.
- **AC-BN-5** A `depends-on` target that does not resolve to a file prints
  `WARN [dangling-reference]` to stderr and is omitted from the closure; with
  `--strict`, exit 1.
- **AC-BN-6** Backticked strings that are not repo files (e.g.
  `` `status: agreed` ``, `` `somewhere/absent.md` ``) are silently ignored,
  not reported as dangling — only declared `depends-on` edges are strict.
- **AC-BN-7** `--format list` (default) prints one repo-relative path per line
  on stdout, nothing else. `--format json` prints an array of objects with
  `path`, `depth`, and `via` (the referring path, null for entries).
  `--format concat` prints each document's content preceded by a
  `===== <path> @ <sha> =====` separator line.
- **AC-BN-8** `--why` annotates list output with `  <- <referrer> (depth N)`.
- **AC-BN-9** An entry that does not resolve to a file exits 2 naming it.
- **AC-BN-10** Concrete regression anchors against this repo, rather than a
  full expected set (which would churn with every doc edit):
  (a) `bundle base` yields exactly `context-sets/base.md` — `base.md` declares
  `depends-on: []` and contains no backticked `*.md` references, so a closure
  that returns more than itself is over-collecting;
  (b) `bundle operating-model.md` reaches
  `policies/source-of-truth-policy.md`, proving transitive body references are
  actually followed. *(Revised — the original wording named `base` as the entry
  point for the transitive assertion, which is unsatisfiable for any correct
  implementation. Defect D1, found by the Test Designer at the red-gate.)*

### 3.8 `bin/migrate-frontmatter` (F2 transform)

```
migrate-frontmatter --plan [--out FILE]
migrate-frontmatter --apply PLAN [--dry-run]
```

Plan entry format (one block per document; `--out` defaults to stdout):

```markdown
## `context-sets/base.md`
- action: migrate
- has-frontmatter: yes
- legacy-status-line: 10 `Status: stable`
- status: TODO            # legacy 'stable' has no mapping in the policy
- last-reviewed: null
- audience: TODO
- grandfather: TODO
```

- **AC-MG-1** `--plan` emits one block per in-scope `.md` file, in sorted path
  order, with the path as a backticked H2.
- **AC-MG-2** Legacy status detection finds a body line matching
  `^Status:\s*(\S+)` within the first 20 lines after the H1 and records its
  1-based line number and verbatim text.
- **AC-MG-3** Status mapping is preserving where the policy defines the value:
  `draft` → `draft`, `in-review` → `in-review`. `stable` (and any other legacy
  value, and no legacy line at all) → `TODO`, with a comment naming why. The
  script never guesses `agreed`.
- **AC-MG-4** `audience` is always `TODO` — it is the judgment field, and the
  transform is mechanical by design.
- **AC-MG-5** A document that already has complete, valid lifecycle frontmatter
  is emitted with `action: skip` and no TODOs.
- **AC-MG-6** `--plan` writes no changes to any document.
- **AC-MG-7** `--apply` refuses (exit 3) if any `TODO` remains in the plan,
  listing every path that still needs a decision.
- **AC-MG-8** `--apply` is all-or-nothing: it computes every new document in
  memory, validates all of them, and writes nothing at all if any would be
  invalid (exit 1, naming the failures).
- **AC-MG-9** For a document with no frontmatter, `--apply` inserts a
  frontmatter block at the very top and deletes the legacy `Status:` line; the
  remaining body is byte-identical apart from that deletion and the collapse of
  a doubled blank line left behind by it.
- **AC-MG-10** For a document that already has frontmatter (e.g. the
  context-sets' composition fields), `--apply` merges the lifecycle fields into
  the existing block, preserving the existing keys and their values, and still
  removes the legacy body `Status:` line.
- **AC-MG-11** `--apply --dry-run` prints a unified diff per document and
  writes nothing.
- **AC-MG-12** `--apply` never stages or commits; the resulting worktree is
  left for review (Package B's batch gate).
- **AC-MG-13** Round-trip: after a successful `--apply`, `check-frontmatter
  --all` reports zero findings for the migrated set.

### 3.9 `bin/install-hooks` and the shim

```
install-hooks [--repo DIR] [--force] [--print]
```

- **AC-IH-1** Writes an executable `pre-commit` into the target repo's hooks
  directory, honouring `core.hooksPath` when configured and otherwise using
  `$(git rev-parse --git-common-dir)/hooks`.
- **AC-IH-2** The written shim contains the managed marker
  `# >>> ai-methodology frontmatter hook (managed) >>>`, resolves the
  methodology home in the §2.1 order, and `exec`s
  `<home>/bin/check-frontmatter --staged`.
- **AC-IH-3** Idempotent: re-running over a previously managed hook replaces it
  and exits 0 without a backup.
- **AC-IH-4** Refuses (exit 3) when an unmanaged `pre-commit` already exists;
  `--force` backs it up to `pre-commit.bak` before writing.
- **AC-IH-5** `--print` writes the shim to stdout and touches nothing.
- **AC-IH-6** The shim contains no absolute paths to any specific repo.
- **AC-IH-7** End-to-end (behavioral, real git): in a temp repo with the hook
  installed and `AI_METHODOLOGY_HOME` pointed at this repo, committing a
  content edit to an `agreed` in-scope document produces a commit whose version
  of that file says `status: in-review` and `last-reviewed: null`; committing a
  frontmatter-only change to the same document does not alter its status; and
  committing a document with an invalid `audience` value fails with a non-zero
  git exit.

## 4. Cross-cutting acceptance criteria

- **AC-X-1** No file under `bin/` contains an absolute path referencing any
  specific repository or user home directory (grep-level assertion).
- **AC-X-2** No script imports a third-party module; every import resolves in a
  bare Python 3 stdlib environment.
- **AC-X-3** Every CLI supports `--help` and exits 0 for it.
- **AC-X-4** Every CLI run outside a git repository fails with a clear message
  and exit 2 or 3, never a traceback.
- **AC-X-5** No tool writes to any path outside the invoking repo (excluding
  the temp files git itself creates).

## 5. Verification boundary

- Tests are **mock-free where it matters**: git behaviour is exercised against
  real temporary repositories created with `git init`, real commits, and the
  real index. There is no mocked git layer.
- **Mock-verified**: nothing.
- **Contract-verified**: the frontmatter dialect, the metadata policy's field
  rules, and the in-scope glob extraction — verified against the policy text
  itself as the contract.
- **Live-verified**: hook installation and firing, index mutation, and commit
  shaping, in throwaway repos and finally in this repo itself.
- **Not verified by this package**: behaviour inside a project repo other than
  this one (the `wne-crm` shim install is deferred by the directive); any
  Windows or non-POSIX shell path; git versions other than the one on this
  machine.

## 6. Spec clarifications (resolved at the red-gate)

The Test Designer, working only from §1–§5, reported eight ambiguities. Each is
resolved here so the implementation is not guessing. D1 is folded into AC-BN-10
above; the rest are binding additions.

- **D2 — output streams.** *All* human-readable diagnostics go to **stderr**:
  `ERROR`, `WARN`, `NOTE`, and `FLIPPED` alike. **stdout is reserved for
  machine-consumable output** — `bundle`'s closure, `migrate-frontmatter
  --plan`'s plan, `install-hooks --print`'s shim. This is what keeps
  `bundle base | xargs cat` honest.
- **D3 — the `--apply` plan grammar.** A plan block is an H2 whose text is the
  backticked repo-relative path, followed by `- key: value` lines. On input:
  `action`, `status`, `last-reviewed`, `audience`, and `grandfather` are
  **required**; `has-frontmatter` and `legacy-status-line` are informational
  output only and are ignored on input (the transform re-derives them from the
  document, which is also the staleness guard if the doc moved under the plan);
  unknown keys are ignored. A trailing ` # comment` is stripped from a value
  before parsing. The literal `TODO` in any required value refuses the run per
  AC-MG-7. Blocks whose `action` is `skip` are not transformed.
- **D4 — directive heading under `--name`.** With `--cycle N` the heading is
  `# Cycle <N> Directive — <title>`; with `--name SLUG` it is
  `# <title> Directive`. `--title` sets `<title>`; its default is the slug with
  hyphens replaced by spaces for `--name`, and the repository directory name
  for `--cycle`.
- **D5 — "commented placeholder".** An HTML comment (`<!-- ... -->`) wrapping
  one example decision entry carrying the `Finding:` / `Resolution:` /
  `Dictated wording:` labels. It is a comment so that an unedited skeleton
  cannot be mistaken for a real decision.
- **D6 — `flip-agreed` recovery on self-verification failure (AC-FA-2).** The
  tool restores the target file to its pre-invocation worktree content and
  resets that path's index entry to its pre-invocation state. It touches no
  other path's index entry — and cannot need to, since AC-FA-3 already refuses
  to run with unrelated staged changes.
- **D7 — `repo_root` outside a repo** raises `GitError` (the natural
  consequence of `git rev-parse` failing), not a bare `OSError`.
- **D8 — binding signatures.** `frontmatter.validate(doc, *, path=None,
  role_slugs=None, grandfathered=False)`; `repo.role_slugs(root, home=None)`;
  `repo.git(*args, cwd=None, check=True)` — `cwd` must survive as a named
  parameter.

**Known un-testable branch.** AC-FA-11's exit-4 path fires only when
`flip-agreed`'s own commit disagrees with what it staged. That cannot be induced
from outside the process, so it has no black-box test. It is recorded as
**unverified** in the change package; the implementation must keep that branch
to a single comparison so it is verifiable by reading.

## 7. Known risks (to be carried into the change package)

1. **Between Package A and Package B the hook blocks commits touching legacy
   docs** that have no frontmatter at all. That is intended pressure, but it is
   a real operational cost; `git commit --no-verify` is the documented
   override, and the error message names it.
2. **The hook mutates the index.** A bug here corrupts a commit rather than
   merely failing it. This is the highest-risk surface in the package and the
   reason for AC-CF-9's partial-staging rule and for `flip-agreed`'s
   post-commit re-verification.
3. **Policy-text parsing is prose-coupled.** Reformatting the metadata policy's
   Scope section can break `scope.py`. Mitigated by failing closed (AC-SC-2)
   rather than falling back to a stale built-in list.
