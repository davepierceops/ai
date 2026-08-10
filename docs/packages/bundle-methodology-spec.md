# Package TP-2 — `bin/bundle-methodology`: Spec and Acceptance Criteria

Source directive: `docs/cycles/tp2-bundle-methodology-2026-08-09-directive.md`.

This document is tracker/spec-class for a tooling package. `docs/**` is out of
the frontmatter in-scope set per `policies/document-metadata-policy.md`, so this
file carries no lifecycle frontmatter.

## 1. Intent

One command regenerates the `methodology-context-bundle` — the chat-upload
artifact defined by `decisions/log.md` `DEC-000140` — correct-by-construction,
retiring the hand-run interim procedure recorded there. Two prior hand-assembly
failures are the reason this exists: a stale commit cut pre-merge, and a shell
`!` history-expansion corrupting every separator (both in
`docs/global-retro-inbox.md`).

Spec basis (do not invent behavior beyond these):

- `decisions/log.md` @ `dec4b6b5fb2f26880a25cac1e144bdd581338720`, `DEC-000140` —
  filename format, file-set rule, header pins, per-file blob short-SHA,
  `<!-- FILE n/N -->` separators, and the runnable interim Python procedure
  recorded as the reference behavior.
- The current uploaded bundle (not committed to this repo — it is a
  chat-project upload) is the golden output *format*: title +
  do-not-edit line; `Source:`; `Generated:`; the file-set rule statement;
  numbered file list with per-file `(blob <short-sha>)`; and
  `<!-- FILE n/N: <path> @ <short-sha> -->` separators.

Where the two could be read as disagreeing on a byte, `DEC-000140`'s runnable
procedure governs, because the directive names it — not the prose summary next
to it — "the reference behavior" (§4).

## 2. CLI

```
bundle-methodology --out DIR
```

- `--out DIR` (required) — the directory the bundle is written into, created
  with `mkdir -p` semantics if absent. Repo-relative or absolute; resolved
  against the invoking cwd like the rest of this tool family.

No hardcoded personal path (the interim procedure wrote to `~/code/`; per
§2.1's "no hardcoded project paths" principle for this tool family, the
destination is always caller-supplied here too — a deliberate, narrow
deviation from the ad hoc script, not a bundle-format change).

## 3. Design fork — new script, not a `bin/bundle` mode

`bin/bundle` (`docs/packages/package-a-spec.md` §3.7) is a `depends-on`
closure walker; its `--format concat` emits body-only output with
`===== path @ sha =====` separators, no header, and `sha` is the **last commit
that touched the path** (`repo.last_commit_sha`), not a blob hash.
`bundle-methodology` needs:

- a **fixed file set** (spine + audience-filtered `skills/*.md`), not a
  reference-graph walk — there is no `depends-on` traversal here at all;
- a **header** (title, do-not-edit line, `Source:`, `Generated:`, file-set rule
  statement, numbered list) that `bin/bundle` has no concept of;
- **blob SHAs** (`git rev-parse --short HEAD:<path>`, each file's own content
  hash), not commit SHAs;
- **`<!-- FILE n/N: ... -->`** separators, not `===== ... =====`.

Every one of the four differs from `bin/bundle`'s contract. Folding this in as
a `bin/bundle --format methodology` mode would mean two incompatible SHA
semantics and two separator grammars living behind one flag, and risks
`bin/bundle`'s own contract (package A, `§3.7`, out of this package's blast
radius per the directive's do-not list). Decision: **(a) a new script**,
`bin/bundle-methodology`, sharing only the `aimeta` plumbing (`repo`, `cli`)
that both already depend on. `bin/bundle` is untouched.

## 4. File-set rule (computed, never hardcoded)

Fixed spine, in this order:

```
context-sets/base.md
context-sets/spec-and-change-discipline.md
context-sets/collab-workflow.md
operating-model.md
roles/chief-of-staff.md
policies/commit-and-change-control-policy.md
```

Plus every `skills/*.md`, sorted lexicographically by path, whose `audience`
frontmatter field (parsed with `aimeta.frontmatter.parse_text`, not a
hand-rolled regex — the dialect already handles both inline `[a, b]` and block
`- item` forms per `package-a-spec.md` AC-FM-4) contains `all-roles` or
`chief-of-staff`. A skill with neither is excluded. A new skill, or an
audience edit on an existing one, changes the computed set on the next run with
no code change — this is the property `DEC-000140` calls out by name and AC-BM-3
requires.

## 5. Content and SHA sourcing

Both the per-file blob SHA and the embedded file body are read from the git
blob at `HEAD` (`aimeta.repo.blob_at_rev(root, "HEAD", relpath)` /
`file_at_rev`), **not** from the working-tree file. The interim procedure in
`DEC-000140` hashes the `HEAD` blob but reads body text from the worktree file
— harmless when the tree is synced and clean (the tool's documented
precondition, AC-BM-6), but a needless way for a labeled SHA and an embedded
body to diverge on a dirty tree. Sourcing both from the same git read closes
that gap without changing a single output byte in the documented use case, so
it is a robustness choice, not a format change (the directive's "do not
change the bundle format" is about output bytes, not the read path).

A spine or skills-glob path that does not resolve to a blob at `HEAD` is a
hard failure (AC-BM-9) — a silently-omitted spine file would produce a
plausible-looking but wrong bundle, which is worse than refusing.

## 6. Acceptance criteria

- **AC-BM-1** Writes exactly one file,
  `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md` (timestamp at generation
  time, local time, minute resolution), to `--out DIR`.
- **AC-BM-2** The header, in order: `# methodology-context-bundle`; a blank
  line; `**Derived artifact — do not edit.** Regenerate from davepierceops/ai;
  the repo is canonical.`; a blank line; `- Source: davepierceops/ai @
  <full HEAD SHA>`; `- Generated: <stamp>`; `- File set: fixed decision-layer
  spine + every skills/*.md whose audience includes all-roles or
  chief-of-staff (rule; Dave 2026-08-07).`; a blank line; the numbered file
  list (§6, AC-BM-4); two blank lines before the first `<!-- FILE -->` block.
  Byte-exact per §7's rendering.
- **AC-BM-3** File set = the fixed six-file spine (§4) **plus** every
  `skills/*.md` whose `audience` frontmatter contains `all-roles` or
  `chief-of-staff`, computed from the rule every run — never a hardcoded list.
  A new skill file, or an audience change on an existing one, is picked up
  with no code change (test: add/edit a skill in a fixture repo between two
  runs; assert the file list changes accordingly).
- **AC-BM-4** Numbered file list, one entry per line, 1-indexed, spine first in
  the order given in §4 followed by matching skills in lexicographic path
  order: `  <n>. <path> (blob <short-sha>)`. The SHA is that file's own blob
  at `HEAD` (`git rev-parse --short HEAD:<path>`), never the repo HEAD SHA.
- **AC-BM-5** Each file body is preceded by a three-line separator block:
  a bar line (`<!-- ` + 60 `=` + ` -->`), `<!-- FILE n/N: <path> @ <short-sha>
  -->` (same blob SHA as its list entry), then the bar line again — matching
  `DEC-000140`'s runnable procedure exactly (§7).
- **AC-BM-6** Every SHA in the output — the header `Source:` SHA and every
  per-file blob SHA — is computed by calling git against `HEAD` at run time;
  none is a literal or hardcoded value anywhere in the implementation (test:
  create a second commit that changes a spine file's content in the fixture
  repo; assert the corresponding blob SHA in the output changes and no other
  SHA does). Documented operational precondition, not a runtime-enforced
  check (the tool has no way to know which branch name means "main" in an
  arbitrary invoking repo): run on a synced `main` with a clean tree, per
  `DEC-000140`. §5 makes correctness independent of tree cleanliness anyway —
  the precondition is about the *meaning* of the bundle (which commit it
  claims to describe), not about a failure mode this tool must detect.
- **AC-BM-7** Deterministic given `HEAD` and the fixture tree: two runs against
  the same `HEAD` produce byte-identical output once each run's `Generated:`
  line is normalized out.
- **AC-BM-8** Writes only the one bundle file named in AC-BM-1. No other file
  in the repository or the output directory is created, modified, or deleted;
  the repository's git status is unchanged by a run (test: `git status
  --porcelain` before and after, on the fixture repo, are equal).
- **AC-BM-9** A spine path, or a `skills/*.md` path that the file-set rule
  selected, that does not resolve to a blob at `HEAD` (deleted, or the working
  copy is ahead of `HEAD` with an uncommitted rename/add) is a hard failure:
  exit 3, naming the missing path on stderr. No partial bundle is written.

## 7. Concrete rendering (fixture: two files, spine-plus-one-skill shape)

Given `HEAD` = `abc123fullsha`, `context-sets/base.md` at blob `e1e2e3f`
containing `file a\ncontent\n`, and `skills/x.md` at blob `a1b2c3d` containing
`file b content, no trailing newline` (no trailing newline in the source), and
`--stamp`-equivalent generation time `2026-08-09-1200`, the byte-exact output is:

```
# methodology-context-bundle

**Derived artifact — do not edit.** Regenerate from davepierceops/ai; the repo is canonical.

- Source: davepierceops/ai @ abc123fullsha
- Generated: 2026-08-09-1200
- File set: fixed decision-layer spine + every skills/*.md whose audience includes all-roles or chief-of-staff (rule; Dave 2026-08-07).

  1. context-sets/base.md (blob e1e2e3f)
  2. skills/x.md (blob a1b2c3d)


<!-- ============================================================ -->
<!-- FILE 1/2: context-sets/base.md @ e1e2e3f -->
<!-- ============================================================ -->

file a
content


<!-- ============================================================ -->
<!-- FILE 2/2: skills/x.md @ a1b2c3d -->
<!-- ============================================================ -->

file b content, no trailing newline

```

(File body trailing newlines are always normalized to exactly one blank line
after the body, regardless of how many — zero or more — the source file ends
with; `DEC-000140`'s procedure does this by `rstrip("\n")`-ing the body before
re-joining.) This block was generated by literally running `DEC-000140`'s
procedure logic against these two inputs — not hand-typed — so it is safe to
diff test fixtures against.

## 8. Red-gate / golden-oracle strategy

Strong form per the directive: golden-comparison against a fixture tree, not a
hand-maintained expected-string constant that could silently drift from
`DEC-000140`. The test suite builds a small throwaway git repo (same
`bin/tests/helpers.py` fixture pattern as the rest of this tool family — real
git, no mocking) containing the six spine paths plus a handful of
`skills/*.md` fixtures with varied `audience` values (some matching, some not,
one using the `- item` block-list form), then:

1. Runs `DEC-000140`'s interim procedure (transcribed verbatim into a test
   helper, parameterized only on the file-set list and the output path — same
   algorithm, not a re-derivation) against that fixture repo to produce the
   oracle bundle.
2. Runs `bin/bundle-methodology --out <dir>` against the same fixture repo.
3. Asserts byte equality after stripping each output's `Generated:` line.

This ties the test directly to the recorded reference behavior instead of a
second hand-written expectation that could itself be wrong. Confirm red
(behavioral: the script does not exist yet, or its output does not match the
oracle — not a missing-module import error) before implementation.

## 9. Scope / do-not

- Touch only: `bin/bundle-methodology`, its tests (`bin/tests/test_bundle_methodology.py`
  or similar), and this spec doc.
- Do not change the bundle format (§§2, 6, 7 are it). If the golden format and
  `DEC-000140` disagree on a byte this spec doesn't already resolve, STOP and
  surface rather than guessing.
- Do not touch `bin/bundle`, any other `bin/` tool, or any methodology
  document.

## 10. Done

`bin/bundle-methodology` generates a bundle byte-matching §7's rendering
(and, generally, `DEC-000140`'s procedure output) modulo the `Generated:`
line; this spec doc is written; tests are confirmed red-then-green; the
existing `bin/tests/run` suite still passes at whatever baseline it was at
before this package (3 pre-existing, unrelated failures on `main` as of
2026-08-09 — `AC-BN-10`/`AC-SC-1` scope-policy drift — are not this package's
to fix per §9); branch + PR opened for Dave's review.

## Status of this draft

Written 2026-08-09 executing
`docs/cycles/tp2-bundle-methodology-2026-08-09-directive.md`. Not yet reviewed.
