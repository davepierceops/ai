# Directive: bundle --write mode

Date: 2026-08-11
Route: fresh
Model: Sonnet 5
Track: A
Execution block: this file is the baton. First act: commit it verbatim to
docs/cycles/bundle-write-2026-08-11-directive.md on a new branch
`bundle-write`, push the branch, then execute the rest.

## Intent

bin/bundle prints to stdout only. The output-file naming convention exists
solely inside bin/bundle-methodology (`methodology-context-bundle-<stamp>.md`,
stamp `%Y-%m-%d-%H%M`). The generalization dropped it, so the operator must
hand-assemble redirection and filenames — the drift-defect class this repo
exists to prevent.

## Change

Add to bin/bundle:

- `--write` (boolean): render the concat form fully in memory, then write it
  to a file the script names itself. Error if `--format` is explicitly set to
  anything other than concat. Error if more than one ENTRY is given.
- `--out DIR` (default `~/Downloads`, tilde expanded): where `--write` puts
  the file. Only meaningful with `--write`; error otherwise.
- Filename: `<entry>-context-bundle-<YYYY-MM-DD-HHMM>.md`, stamp generated
  exactly as bin/bundle-methodology does.
- In-memory-first rule as in bundle-methodology (AC-BM-9): a failure mid-render
  leaves no partial file and creates no directory.
- On success print exactly one line: `wrote <absolute path>`. Nothing else to
  stdout in --write mode.

## Discipline

1. Spec first: record --write behavior in docs/packages/package-a-spec.md
   §3.7 (or a sibling subsection) before any test or implementation.
2. Tests in bin/tests, written and confirmed red before implementation.
   Cover: default out dir, --out override, stamp format, single-entry
   enforcement, --format conflict error, no-partial-file on render failure.
3. Implement to green. Existing bundle behavior without --write is unchanged;
   full existing test suite stays green.

## Constraints

- Do not modify bin/bundle-methodology.
- Do not open a PR (gh API is unreachable from your sandbox) — push the
  branch, then STOP and report: branch name, test results red-then-green,
  files changed.
- If bin/bundle at HEAD differs materially from the description in Intent,
  STOP and surface before editing.
