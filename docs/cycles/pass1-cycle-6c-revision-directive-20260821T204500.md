# Directive — Pass 1, Cycle 6c: retire the term "dispatch"

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

Documents in scope, all @ bf6b40ceb15ef969830c24040023642e1d5dbb94:
- docs/global-context/core.md
- docs/global-context/decision-layer.md

## Decision (Dave, 2026-08-21)

"Dispatch" is retired. It named nothing beyond "hand a directive to an execution session." Delete the Dispatch vocabulary entry from Core. Every remaining use of the word in the two files is rewritten in plain terms: "hand the directive to an execution session," "direct," or equivalent, whichever reads naturally in place. No entry is added in its place.

## Execution

1. Fetch origin/main; verify the tree contains bf6b40c with no later edits to the two files.
2. Delete the Dispatch entry. Rewrite every other occurrence of dispatch/dispatches/dispatched in both files. Confirm by grep that zero remain.
3. Re-read both files for anything the rewrite leaves awkward or inconsistent (Core 13). Touch no other file; the other fourteen governed files using the word are later cycles.
4. Commit on branch p1-cycle-6c-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Occurrences rewritten per file, before → after, abbreviated. Then branch and SHA.
