# Directive — Pass 1, Cycle 9: re-gate core, decision-layer, LEXICON

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ 8d49fa8cfaf81300c9c54d68031652cf970654c1:
- docs/global-context/core.md — baseline cb3e75a (cycle 7, ready)
- docs/global-context/decision-layer.md — baseline cb3e75a (cycle 7, ready)
- LEXICON.md — baseline cb3e75a (cycle 10, changes-required)

Prior cycles: reviews/core-cycle-7.md, reviews/decision-layer-cycle-7.md, reviews/LEXICON-cycle-10.md.
Decisions applied: docs/cycles/pass1-cycle-8-revision-directive-20260821T211500.md.
Rubric: docs/global-context/review-rubric.md @ 8d49fa8.

## Instructions

1. Fetch origin/main; verify the tree contains 8d49fa8 with no later edits to the three files.
2. Confirm L8 and L9 are resolved as the cycle 8 directive decided, including the two qualifying paragraphs that moved to Core with the session definitions and the folded clause from the decision-layer preamble.
3. Re-apply all ten rubric criteria to the current text of each file; new defects are findings. Check the three files against each other for any term stated in two places.
4. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning. Do not report any of these.
5. Write reviews/core-cycle-9.md, reviews/decision-layer-cycle-9.md, reviews/LEXICON-cycle-11.md per the schema in skills/spec-review-cycle.md, with a Baseline: line after Reviewed:. A clean pass is the header and nothing else.
6. Commit on branch p1-cycle-9-review, push to origin, report the SHA read back from git. No pull request. No edits to any document. No status flip.

## Report shape

One line per file: path, verdict, finding counts. Then branch and SHA.
