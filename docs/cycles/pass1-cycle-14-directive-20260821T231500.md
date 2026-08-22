# Directive — Pass 1, Cycle 14: re-gate after the context-sets/boundaries revision

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ 2b9c856736b238edf64863eb5bf08f445e721235:
- docs/global-context/decision-layer.md — baseline 8d49fa8 (cycle 9, ready); edited by cycles 12 and 13
- LEXICON.md — baseline 8d49fa8 (cycle 11, ready-with-findings); edited by cycles 10 and 12
- operating-model.md — baseline cb3e75a (cycle 4, ready); edited by cycle 12
- context-sets/production-grade-software.md — baseline cceef9a (cycle 1, ready-with-findings)
- context-sets/spec-and-change-discipline.md — baseline cceef9a (cycle 6, changes-required)
- context-sets/testing-and-verification.md — baseline cceef9a (cycle 1, changes-required)
- boundaries/human-review-boundary.md — baseline cceef9a (cycle 1, changes-required)
- policies/verification-boundary-policy.md — merge target; first Pass 1 review
- policies/source-of-truth-policy.md — merge target; first Pass 1 review

Decisions applied: docs/cycles/pass1-cycle-12-revision-directive-20260821T223000.md and pass1-cycle-13-revision-directive-20260821T230000.md. Read both; the cycle-12 report's "findings not applied as written" list is in the branch p1-cycle-12-revision's merge commit message body if present, otherwise accept the directive's dispositions as the governing record.
Rubric: docs/global-context/review-rubric.md @ 2b9c856.

## Instructions

1. Fetch origin/main; verify the tree contains 2b9c856 with no later edits to the nine files.
2. For the seven previously reviewed files, confirm every prior finding is resolved as decided, or was overridden by a directive decision. Unresolved and not overridden is a finding.
3. Apply all ten rubric criteria to the current text of all nine. For the two policies, this is their first Pass 1 review: answer criterion 10 explicitly, and list every path-shaped reference and vendor name — the cycle-12 executor left those in place deliberately, and they are findings now. Check all nine against each other for any term or rule stated twice.
4. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning; references to deleted files in files outside this scope. Do not report any of these.
5. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md with n one more than the highest existing for that stem. Baseline: line after Reviewed:. A clean pass is the header and nothing else.
6. Commit on branch p1-cycle-14-review, push to origin, report the SHA read back from git. No pull request. No edits to any document. No status flip.

## Report shape

One line per file: path, verdict, finding counts. Then branch and SHA. Then, for each policy, the criterion-10 disposition in one line.
