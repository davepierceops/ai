# Directive — Pass 1, Cycle 3 revision: core

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

Document in scope: docs/global-context/core.md @ 04bfeaee26af68a0320619e571f665fbef052a84
Review triaged: reviews/core-cycle-2.md on branch gc-cycle-2-review @ 719d013c9ccb9b81a7c61080ddf47bd4dc237726
Rubric: docs/global-context/review-rubric.md @ 04bfeae

## Decisions

### CORE-9 — accept
Rule 14: the convention applies to a filename you generate when no stated convention names the file; where a convention names it, follow the convention. Remove the enumeration "session artifacts, retros, directives, captured output" and the "canonical document" exception — the convention clause covers both. Keep the ISO 8601 basic example and the "never random strings, hashes, or UUIDs" clause.

### CORE-10 — accept
Rule 6: replace "A claim without a class is not a claim." with "State the class; an unlabelled assertion is treated as *unknown*." Keep the final sentence.

## Execution

1. Verify the tree contains 04bfeae with no later edits to core.md. Fetch and read the review artifact from origin/gc-cycle-2-review.
2. Apply both decisions. Re-read the file end to end for any text the edits leave inconsistent (rule 13).
3. Commit core.md on branch gc-cycle-3-revision (same branch as this directive), push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

One line: rule 14 and rule 6 before → after. Then branch and SHA. Then anything not applied as written.
