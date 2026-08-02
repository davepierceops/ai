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
  `policies/document-metadata-policy.md` is enforced **on a direct
  `git commit` of a UTF-8 regular file, when the in-scope set resolves and no
  merge is in progress** — rather than by memory. *(Originally "enforced by
  construction". The first re-gate disproved that: a pre-commit hook does not
  run for merge, rebase, cherry-pick, or revert. The second re-gate disproved
  the first correction too — `MERGE_HEAD`, a staged symlink, an undecodable
  HEAD, and a glob set matching nothing are all escapes **on a direct
  `git commit`**, which is what the narrowed claim asserted. This is the third
  wording, and it is qualified to exactly what was verified. Each escape is
  named in §8.4.)*
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
    cli.py                # exit codes, diagnostic format, context loading
    closure.py            # the reference closure shared by bundle & cycle-open
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
  shaping, in throwaway repos shaped like this one. *(Originally claimed
  "and finally in this repo itself". That was false and is struck: Package A's
  own non-goals forbid installing the hook here, and §7.1 is the reason it must
  not be installed until Package B lands. The tests run in throwaway repos
  shaped like this one — not in it.)*
- **Also live-verified after the fix round** (this list was stale in the first
  correction and is restated from measurement): pathspec commits, `git commit
  -a`, and conflicted merges; non-UTF-8 documents *as blocked*; and minimal-
  environment shim behaviour — a `PATH` carrying git but not `python3` produces
  the shim's own `ERROR` and exit 3, and `LC_ALL=C` with em-dash documents
  works.
- **Not verified by this package**: behaviour inside a project repo other than
  this one (the `wne-crm` shim install is deferred by the directive); **merge,
  rebase, cherry-pick, and revert**, which bypass pre-commit entirely;
  `git commit --amend`, which has no test though it was verified by hand;
  **processing** a non-UTF-8 document (only blocking it is verified); **CRLF
  documents**; **any git version other than 2.54.0** — AC-CF-16's mirror depends
  on undocumented git lock ordering, so this is a real re-verification
  obligation before the hook is installed anywhere; Linux, Windows, or a
  case-sensitive filesystem; true concurrent git processes.

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

1. **Between Package A and Package B the hook blocks commits touching almost
   every in-scope document.** Measured against this repo at review time:
   **34 of 38 in-scope documents fail, with 46 findings** — not only the 5
   `missing-frontmatter` cases but `missing-status`, `missing-audience`, and
   `missing-last-reviewed` across the six context-sets, plus one
   `invalid-status` (`context-sets/spec-and-change-discipline.md` carries
   `status: draft v0.1`). The measured breakdown is **28 `missing-frontmatter`,
   5 `missing-status`, 6 `missing-audience`, 6 `missing-last-reviewed`, 1
   `invalid-status`**. *(Originally worded "legacy docs that have no frontmatter
   at all", which understated the gap roughly sevenfold; the first correction
   then transposed the 28 and the 5.)*
   Consequently **the hook is not installed in this repo by Package A**; it is
   installed when Package B's migration lands. `git commit --no-verify` is the
   documented override, but note it disables the *entire* hook for that commit,
   suspending the flip as well as the legacy check — so the interim would train
   exactly the habit the hook exists to remove.
2. **The hook mutates the index.** A bug here corrupts a commit rather than
   merely failing it. This is the highest-risk surface in the package, and the
   review gates proved the point: the original implementation transcoded
   non-UTF-8 documents in the index and left the index mutated when it crashed
   mid-flip (§8, B1), and left the real index stale on a pathspec commit in a
   way that inverted the enforcement over two commits (§8, B2). AC-CF-9's
   partial-staging rule and `flip-agreed`'s post-commit check — the mitigations
   this risk originally named — covered neither. The mitigations that actually
   address it are AC-CF-14 through AC-CF-18.
3. **Policy-text parsing is prose-coupled.** Reformatting the metadata policy's
   Scope section can break `scope.py`. Mitigated by failing closed (AC-SC-2)
   rather than falling back to a stale built-in list — but note the gate found
   a route around that protection: a glob that *parses* but matches nothing
   enforces nothing, silently (§8, AC-CF-19).

## 8. Gate findings and revised acceptance criteria

The Reviewer gate returned **FAIL** and the Skeptic/Risk gate returned **do not
ship as-is**. Between them they found three data-integrity defects that a fully
green 232-test suite did not catch, because the suite exercised one git verb
(`git commit -m`), one repo shape, one encoding (UTF-8/LF), and one environment.
Every finding below sits just outside that aperture.

The ACs in this section are **additions and amendments** to §3 and §4. They are
written the same way — behavioural statements the Test Designer turns into
tests, red before any fix is written. There are **18 new AC ids** below; other
ids appearing in this section (`AC-CF-5`, `AC-CO-9`, `AC-FA-11`, `AC-MG-13`,
`AC-SC-2`, `AC-X-5`) are cross-references to existing criteria, not additions.

**A note on exit codes for this round.** Several of these defects currently
*also* exit 1, because that is Python's uncaught-exception code. For this
package, **exit 1 is not evidence of a controlled failure** — the ACs below are
written against observable state (blob bytes, index contents, absence of a
traceback, the specific finding code), not against the exit code alone, and
tests must be too.

### 8.1 Blocking defects

**B1 — the hook transcodes non-UTF-8 documents in the index, then crashes
mid-mutation.** `repo.file_at_rev` decoded with `errors="replace"` and the flip
re-encoded as UTF-8, so every non-UTF-8 byte became U+FFFD in the blob written
to the index. The index write completed *before* the failing worktree read, so
the corruption survived the crash, and `git commit --no-verify` — the override
the tool's own message recommends — committed it.

- **AC-CF-14** A staged in-scope document that is not valid UTF-8 is reported
  `[undecodable]` and blocks the commit (exit 1). Its index blob and its
  worktree file are **byte-identical before and after** the run. No transcoding,
  ever: the flip path reads and writes bytes, and any decode for parsing is
  strict.
- **AC-CF-15** **Validate before mutating.** Findings are computed on the
  would-be-flipped content *before* anything is written; when findings exist,
  neither the index nor the worktree is modified. This also resolves the
  separate finding that a *blocked* commit was leaving the developer's working
  tree edited, and that `--no-verify` afterwards then committed the tool's
  rewrite rather than what the developer staged.
- **AC-X-6** No CLI ever emits a Python traceback. Every uncaught exception
  becomes a diagnostic line with one of the documented exit codes — including
  `UnicodeDecodeError` from `check-frontmatter --all`, `check-frontmatter
  PATH`, and `migrate-frontmatter --plan`, all of which currently traceback.
- **AC-X-7** Every file read and write specifies UTF-8 explicitly rather than
  relying on the platform default. *(On Linux under `LC_ALL=C` — realistic for a
  hook spawned by a GUI client — the default resolves to ASCII, and every
  document containing an em-dash would raise. This repo is full of em-dashes.)*

**B2 — `git commit -- <path>` leaves a stale real index, and the enforcement
inverts.** Git runs pre-commit against a *temporary* index for pathspec commits.
The hook flipped that index correctly, so the commit was right — but the real
index kept the pre-flip blob, leaving a staged change the user never made. A
second, ordinary `git commit` then sailed through: staged body equalled HEAD
body, so AC-CF-5's status-transition exemption applied and nothing flipped.
Final state: `status: agreed` with a stale `last-reviewed` on an edited body —
precisely the lie the policy exists to prevent, reached via two hook-approved
commits.

- **AC-CF-16** When the hook runs against a temporary index (`$GIT_INDEX_FILE`
  set to something other than the repository's own `index`), the flip is
  mirrored into the real index **when, and only when, the real index's entry
  for that path is still the pre-flip blob** — never clobbering unrelated
  staged state. After any `git commit` variant, the real index must not hold a
  stale pre-flip blob for a flipped path, and `git status` must not report a
  modification the user did not make.

**B3 — a conflicted merge nulls the review pointer on documents agreed on the
merged branch.** `check_staged` diffs against HEAD (the first parent), so every
in-scope document that changed on the merged branch looks like a content edit —
including documents legitimately reviewed and agreed *there*. The merge commit
recorded `status: in-review`, `last-reviewed: null`, destroying the durable
record of which review agreed the document, on a commit the user believes is
just a merge, at exit 0.

- **AC-CF-17** When `MERGE_HEAD` exists, no flip occurs. The tool validates and
  prints a `NOTE` naming why. A merge's difference against its first parent is
  not an authored edit, and treating it as one loses review history.

### 8.2 Correctness defects

- **AC-FA-12** *(F2)* `flip-agreed` commits **without** `--no-verify`, so hooks
  run and can alter content — but its post-commit check never compared the
  committed body to the parent's. With a content-modifying pre-commit hook it
  committed an injected body line and exited 0, while its docstring promised "a
  commit that provably touches nothing but frontmatter". The post-commit check
  gains one comparison: the committed body must equal the body at `HEAD~1`
  (or the file must be new at HEAD). This keeps the anti-laundering property of
  running hooks while closing the window. *(AC-FA-11 as originally written
  specified exactly re-validate-plus-single-path, and that is exactly what was
  built — the spec was the defect, not the code.)*
- **AC-FA-13** *(N5)* If `git commit` fails for any reason — a rejecting
  site-wide hook, a signing failure, a missing identity — `flip-agreed`
  restores the worktree file and that path's index entry to their pre-invocation
  state, reports the failure, and exits 3. It must not leave the developer with
  a mutation they did not ask for and no message saying so. *(§6 flagged
  AC-FA-11's exit-4 branch as the unverified risk. That was the wrong thing to
  flag: the exit-4 branch is benign and effectively unreachable, while this
  path is reachable and destructive. The risk ordering was inverted.)*
- **AC-CF-18** *(N1)* A staged rename (`R`) whose new path is in scope compares
  the staged body against the **old** path at HEAD, so renaming an agreed
  document and editing it in the same commit still flips. Previously the tool
  looked for the new path at HEAD, found nothing, treated it as an addition, and
  never flipped — a one-command, hook-blessed bypass.
- **AC-MG-14** *(F3)* `--apply` records every document marked `grandfather: yes`
  in `reviews/frontmatter-disposition.md`, creating the file if absent, as part
  of the same all-or-nothing write. **The entries are backticked repo-relative
  paths** — that is the only form `repo.disposition_paths` parses (AC-RP-7), and
  the round trip into AC-CF-12 is the whole point, so a format that reads back
  empty is a silent failure rather than a formatting preference. Without this, a grandfathered document
  passes `--apply` and then immediately fails `check-frontmatter --all` with
  `agreed-without-review`, violating AC-MG-13 — and landing on Package B, the
  consumer.
- **AC-CO-12** *(F4; wording corrected at the second re-gate)* `--out` is
  interpreted **relative to the repo root**, not to the current working
  directory, and **any absolute path is refused with exit 2** — including one
  that happens to fall inside the repo — as is any path escaping the root via
  `..`. *(The escape itself was fixed, but the implementation resolved `--out`
  against the CWD and accepted absolute paths inside the repo, so spec and code
  disagreed: from `nested/deep`, `--out bundlehere` landed in
  `nested/deep/bundlehere`. One rule, stated once, is worth more than a
  convenience here — the bundle's location is referenced by the directive.)*
  *(`pathlib`'s `/` operator discards the left operand when the right is
  absolute, so `--out /tmp/x` wrote outside the repo at exit 0, violating
  AC-X-5. `migrate-frontmatter` already does this correctly via
  `cli.relpath_of`.)*
- **AC-FM-17** *(F5)* `render` preserves comment lines and blank lines inside
  the frontmatter block. **Binding rule, since AC-FM-7 reorders keys and the two
  would otherwise collide: a comment or blank line binds to the key that
  follows it and moves with that key; a trailing comment with no following key
  is emitted at the end of the block.** The
  dialect (§3.1) admits `#` comments and `parse_text` accepts them, but nothing
  round-tripped them — so an unattended index mutation silently deleted content
  the author wrote, including, in the worked example, a comment explaining why
  the document's `audience` must not change.
- **AC-FM-18** *(F8)* A `- item` continuation line following a scalar-valued key
  yields `malformed-frontmatter` rather than silently discarding the scalar.

### 8.3 Honesty and operability

- **AC-CF-19** *(N3)* `check-frontmatter --all` prints a `NOTE` stating how many
  files matched the in-scope set, and emits a `WARN` for any configured glob
  that matches no path in the repo. **Exit stays 0** — per §2.4 a `WARN` is not
  a policy failure, and a project repo legitimately has no `policies/` or
  `roles/` directory. The goal is that "enforcing nothing" stops being visually
  identical to "fully compliant", not that it becomes an error. Today a repo where enforcement matches
  *nothing* is indistinguishable from a fully compliant one: both print nothing
  and exit 0. AC-SC-2's fail-closed design covers a missing, unreadable, or
  restructured policy — it does not cover a policy that parses fine and matches
  nothing, which is reachable by a typo, a renamed directory, or a stale
  `$AI_METHODOLOGY_HOME` pointing at an older clone.
- **AC-IH-8** *(N4)* `install-hooks --uninstall` removes a managed hook,
  restoring `pre-commit.bak` if one exists, and refuses to remove an unmanaged
  hook. Without it, rollback is manual, and deleting or moving the `/ai` clone
  bricks commits in every repo still carrying the shim.
- **AC-IH-9** *(N4)* When `python3` is not on `PATH`, the shim fails with the
  same `ERROR:`-prefixed diagnostic form it already uses for the
  home-not-found path, naming `python3` and how to fix it, and exits with a
  code from §2.4's set. Hooks spawned by GUI clients do not inherit a login
  shell, and the current behaviour degrades to raw shell noise
  (`dirname: command not found`, `env: python3: No such file or directory`,
  exit 127). *(Sharpened after the Test Designer noted that the raw `env:`
  message already names `python3` on a literal reading, so the original wording
  was satisfied by the defect itself.)*
- **AC-CF-20** *(D5)* A path argument that differs only in case from the file on
  disk is resolved to its real case before scope matching. On a
  case-insensitive filesystem, `check-frontmatter Policies/x.md` currently exits
  0 silently — a false all-clear.
- **AC-CF-21** *(D4)* A staged symlink at an in-scope path is reported with the
  code `[symlink]` and skipped rather than being read as a document, and the
  link itself is never replaced. The blob of a symlink is its target path, so
  it was reported `[missing-frontmatter]` and blocked forever with a misleading
  code. *(The related hazard — `write_text` following the link and writing
  outside the repo — is theoretical rather than reachable: a symlink's blob is a
  bare path, which can never parse as an `agreed` document, so the flip path
  cannot be entered. The misleading-report defect is the real one.)*

### 8.5 Second re-gate — the mirror must fail loudly

The Skeptic/Risk re-gate confirmed B1, B2, and B3 closed on every normally
reachable path, and then found that the B2 *fix* re-opens B2 when it fails.

- **AC-CF-22** *(S1, blocking)* If mirroring the flip into the installable
  index fails for any reason, the tool reports `ERROR [real-index-unreachable]`
  **naming the consequence** — that the flip is not in the real index and a
  later commit could restore the pre-flip status — and **exits 1, blocking the
  commit**. It must never downgrade to a `NOTE` at exit 0. *Reproduced: with a
  stale `.git/index.lock.lock`, `git commit -m x -- policies/p.md` succeeded at
  exit 0 leaving the real index at `agreed`, and a second ordinary commit then
  landed `status: agreed` with a stale `last-reviewed` on an edited body —
  defect B2 verbatim, through two hook-approved commits.* The mechanism depends
  on undocumented git ordering (git pre-populates `.git/index.lock` before the
  hook and installs it after); that dependency is acceptable **only** if its
  failure is loud, because a silent failure is indistinguishable from success.
- **AC-CF-23** *(S6, blocking)* `--staged` emits a `WARN` when the resolved
  in-scope glob set matches **no path in the repo**, so a typo'd glob, a renamed
  directory, or a stale `$AI_METHODOLOGY_HOME` cannot silently disable the hook.
  AC-CF-19 put this diagnostic in `--all` — the mode a human runs deliberately —
  and not in `--staged`, the mode that runs unattended. That is backwards. The
  warning stays quiet in the normal case (files matched) and fires only when
  enforcement has become a no-op.
- **AC-CF-24** *(S2)* The mirror is skipped, and **no `[real-index-untouched]`
  NOTE is emitted**, when the installable index is the same file the flip was
  already written to (the `git commit -a` case, where the guard compares the
  flipped blob against itself and always declines). The NOTE must appear only
  when the real index genuinely holds a different blob. A false diagnostic is a
  defect in a tool whose entire product is honesty.

### 8.6 Second re-gate — the mirror's failure path, and the `index.lock` verdict

The Reviewer re-gate returned **PASS with two conditions** and, by instrumenting
git rather than reasoning about it, settled the `index.lock` question that had
been the package's largest open risk.

**The mechanism is safe, and safer than the implementation argued.** During a
partial commit, `.git/index.lock` is already fully populated before the hook
runs, and `lsof` shows **no open file descriptor on it**. Git wrote the lock,
closed it, and installs it afterwards by `rename()` alone. The failure anyone
would fear here — git holding an fd across the hook and writing through it
after our replacement, orphaning our inode — cannot occur. `git update-index`
against a malformed lock *refuses* (`index file smaller than expected`) rather
than writing garbage, so the write side degrades safely too. The blast radius is
bounded to the post-commit index, never history, and an index is reconstructible
with `git reset` / `git add`.

**Decision: keep the mirror; do not refuse pathspec commits.** Refusing imposes
a certain cost on an everyday workflow and would train `git commit --no-verify`,
which §7.1 names as the habit this package exists to remove. Trading a
guaranteed behavioural regression for an unreachable hypothetical is the wrong
side of that trade. *(This reverses the orchestrator's earlier recommendation to
refuse, which was made before the no-open-fd evidence existed.)*

**Condition 1 (blocking).** `repo.index_entry` at `bin/check-frontmatter:92`
sits **outside** the `try/except repo.GitError` that guards the mirror — and it
is precisely the call that fails in the degradation scenario. Observed: the temp
index flipped, the worktree left at `agreed`, the commit aborted at exit 3 with
a raw git error rather than a coded finding. That is a mutation surviving a
failure, the class AC-CF-15 exists to eliminate, and it also means that with two
planned flips a failure on the second leaves the first applied. AC-CF-22 covers
the required behaviour; the guard must cover the read as well as the write, and
the `installable_index_path` docstring's "degrades safely" claim must be
corrected to match what the code actually does.

**Version-pinned assumption.** The mechanism depends on git's partial-commit
lock protocol, verified on **git 2.54.0 only**. This is a standing
re-verification obligation before the hook is installed anywhere, and a named
follow-up exists for the durable alternative: a `post-commit` companion that
repairs the real index after the fact and needs no undocumented behaviour.

### 8.7 Recorded but not fixed in Package A

Each of these was verified by a gate, is non-blocking, and is disclosed rather
than absorbed. They are the follow-up list.

- **Trivia inside a block list re-binds to the following key.** A comment inside
  an `audience:` block list moves to sit between `audience` and
  `superseded-by`, where it reads as a comment about the wrong field. Content is
  preserved; meaning is misattributed. AC-FM-17's binding rule has no answer for
  trivia *inside* a value, and its own worked example is this comment.
- **Undecodable HEAD is a demonstrated bypass, not merely an untested area.** A
  document that is not valid UTF-8 at HEAD can have its body rewritten while
  keeping `status: agreed` and a stale `last-reviewed`, at exit 0. §5 excludes
  non-UTF-8 documents from the boundary, so declining to flip is defensible —
  but this is *demonstrated*, and it is closeable (both blobs are in hand as
  bytes; compare them bytewise instead of declining). Note the chain: B1's fix
  recommends `--no-verify`, which is how such a document reaches HEAD.
- **`check-frontmatter --all` still follows symlinks** and reports the
  misleading `[missing-frontmatter]` that AC-CF-21 removed from `--staged`.
- **`cli.relpath_of` resolves symlinks before scope matching**, so a named
  in-scope path that is a symlink is matched by its target: `check-frontmatter
  policies/aliased.md` exits 0 silently on a document `--all` reports with two
  findings. Pre-existing at `ea21174`, and it defeats AC-CF-20's purpose from
  the other direction.
- **`migrate-frontmatter` writes the disposition file after the documents**, so
  a failure there leaves documents migrated to `agreed` with no disposition
  entry — the exact AC-MG-13 violation AC-MG-14 exists to prevent.
- **`bundle --format concat` prints a separator and no body** for an undecodable
  document, so a bundle can silently lose a document with only a stderr WARN.
- **`| head` exits 120**, outside §2.4's set. Python's interpreter-level final
  flush, not the tool's return; affects interactive use only, never the hook.
  §2.4's table should say so, since it presents itself as the contract.

### 8.4 Accepted, deferred, or Dave's call

- **`aimeta/cli.py` and `aimeta/closure.py`** — **accepted** by the Reviewer and
  by me, and §2.3 is amended above to list them. AC-CO-9 requires `cycle-open`
  and `bundle` to share *one* closure implementation; a shared module is the
  only honest way to satisfy it.
- **Bypass via merge, rebase, cherry-pick, and revert** — inherent to
  pre-commit hooks and out of reach. Not fixed; the §1 claim is narrowed
  instead. A `post-rewrite`/`post-merge` companion is a possible future package.
- **CRLF documents** *(D2)* — `check-frontmatter PATH` passes them (universal
  newlines) while `--staged` reports `missing-frontmatter` on line 1 being
  `---\r`. Deferred as a named follow-up; no document in this repo uses CRLF.
- **Sibling-`ai/` as the primary documented install** *(N4)* — the spec presents
  `$AI_METHODOLOGY_HOME` first, but the env var is exactly what a GUI client
  will not have. This is a product decision about who commits from what tool,
  and it belongs with the deferred `wne-crm` shim install rather than here.
- **Installing the hook in this repo** — **not done by Package A**, per the
  revised §7.1.
