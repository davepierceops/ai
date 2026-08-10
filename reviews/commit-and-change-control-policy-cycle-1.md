# Review: policies/commit-and-change-control-policy.md — cycle 1

Verdict: changes-required
Reviewed: `policies/commit-and-change-control-policy.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the new "Spec branches and the reconciliation pull request" subsection
only — the rest of the document is untouched by this directive and was read for
contradiction, not re-gated. Checked against
`docs/cycles/friction-refactor-2026-08-09-directive.md` D2.1, D2.2.
Cross-checked: `skills/spec-review-cycle.md` (Reconciliation),
`context-sets/spec-and-change-discipline.md` (Open spec delta),
`policies/document-metadata-policy.md` (Revision lifecycle; status transitions),
`boundaries/human-review-boundary.md`.
Not inspected: Tiers 1 and 2, the red-gate and Test/Coder clauses, pending-gate
visibility, push mechanics, and branch protection — unchanged this cycle;
branch protection itself, which lives in forge configuration and cannot be
verified from the repository, as this document already states.
Findings: 1 blocking

## B1 — blocking
Claim: The subsection rests a structural guarantee on an ordering that no
document establishes — that the agreement flip happens after the reconciliation
cycle closes, on the default branch.
Location: `policies/commit-and-change-control-policy.md`, "Spec branches and the
reconciliation pull request", second paragraph
Evidence: Verified by reading against `skills/spec-review-cycle.md` at the same
SHA. This document: "a document reading `agreed` on the default branch has been
through the gate, because the transition that sets it is a status-transition
commit made after the reconciliation cycle closes." The owning skill's
Reconciliation step 4 says only "Dave's agreement lands as it always does — a
frontmatter-only status transition — and the PR merges", which is compatible with
the flip landing on the spec branch before the merge.
Consequence: If the flip lands on the spec branch, a document reads `agreed` on a
branch that has not merged and might not — so the sentence in this policy is
false, and the guarantee a reader relies on ("`agreed` on the default branch has
been through the gate") is a convention rather than a structure. A policy stating
a structural guarantee it does not have is worse than one stating none.
Fix: The fix lands in the owning document — `skills/spec-review-cycle.md` states
that the flip is post-merge, on the default branch. This subsection is correct
once it does, and needs no edit of its own beyond the pointer it already carries.
Related: `reviews/spec-review-cycle-cycle-5.md` B2 (same defect, at its owner)
