# Directive — Pass 1, Cycle 2: re-gate core and decision-layer

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

## Documents in scope

- `docs/global-context/core.md` @ 04bfeaee26af68a0320619e571f665fbef052a84
- `docs/global-context/decision-layer.md` @ 04bfeaee26af68a0320619e571f665fbef052a84

Baseline: 5aa02c5ac3f530efc06d1c5e4311eb41e8914855 (cycle 1 reviewed state).
Prior cycle: `reviews/core-cycle-1.md`, `reviews/decision-layer-cycle-1.md`.
Decisions applied: `docs/cycles/global-context-cycle-1-revision-directive-20260821T184500.md`.
Rubric: `docs/global-context/review-rubric.md` @ 04bfeae.

## Instructions

1. Verify the tree contains 04bfeae with no later edits to the two documents.
2. For each cycle-1 finding, confirm the revision resolves it as the directive
   decided — including DL-6's modify and the two observations left open.
   A finding not resolved as decided is a finding.
3. Re-apply all ten rubric criteria to the revised text. New defects
   introduced by the revision are findings.
4. Known and out of scope: `all-decision-roles` is not yet a reserved audience
   value and `docs/global-context/` is outside the frontmatter scope. Both are
   Pass 2 work. Do not report either as a finding.
5. Write `reviews/core-cycle-2.md` and `reviews/decision-layer-cycle-2.md`
   using the schema in `skills/spec-review-cycle.md`, with a `Baseline:` line
   after `Reviewed:`. A clean pass is the header and nothing else. Verdict
   `ready` means ready for Dave's agreement.
6. Commit both on branch `gc-cycle-2-review`, push to `origin`, report branch
   and SHA read back from git. No pull request. No edits to either document.
   No `status` flip.

## Report shape

One line per document: path, verdict, finding counts. Then branch and SHA.
