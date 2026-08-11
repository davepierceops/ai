# Review: skills/spec-review-cycle.md — cycle 5

Verdict: changes-required
Reviewed: `skills/spec-review-cycle.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the revised Hard constraints, Procedure steps 4 and 6, the new
Reconciliation section, and the Output list. Checked against
`docs/cycles/friction-refactor-2026-08-09-directive.md` D1.1, D1.2, D2.2, D2.3.
Cross-checked: `skills/directive-dispatch.md` (Purpose; §4 Execution block;
Executor obligations), `policies/document-metadata-policy.md` (Revision
lifecycle; status transitions), `policies/commit-and-change-control-policy.md`
(Spec branches and the reconciliation pull request),
`context-sets/spec-and-change-discipline.md` (Open spec delta),
`policies/remote-write-verification-policy.md` (Relationship to existing rules).
Not inspected: the chat-side procedure (steps 1–3, 9–11) as practised —
unobservable from the repository, as in cycles 1 and 2; the Review artifact
schema and Cycle directive format sections, untouched this cycle except where
noted.
Findings: 2 blocking
Prior cycle: `reviews/spec-review-cycle-cycle-4.md`
Dave should inspect: B2 — where the agreement flip sits relative to the
reconciliation merge decides whether `agreed` on the default branch is
structurally true or merely usually true.

## B1 — blocking
Claim: "the accumulated diff goes through the reviewer gate **once, as a single
cycle**" reads as prohibiting a re-gate after findings, contradicting the
document's own step 10.
Location: `skills/spec-review-cycle.md`, Reconciliation, lead paragraph and
step 3
Evidence: Verified by reading against step 10 at the same SHA: "Hand the revised
documents back to the reviewer for the gate re-check. Findings from that
re-check open the next cycle at step 1." A reconciliation that produces blocking
findings therefore runs at least two cycles by the document's own procedure,
while its new section says "once, as a single cycle."
Consequence: The two sentences cannot both be followed. An executor resolving
the conflict in favour of the new section ships a reconciliation with blocking
findings open, on the grounds that a second cycle is forbidden — the exact
failure the re-gate exists to prevent, arrived at by obeying the document.
Fix: State what "once" quantifies. The *delta* is gated once — as against once
per edit — and a reconciliation that produces blocking findings re-gates
normally. One clause: "once, as a single cycle over the whole delta rather than
one per edit; findings re-gate per step 10 as in any cycle."

## B2 — blocking
Claim: The Reconciliation section leaves the agreement flip's position relative
to the pull-request merge unstated, and
`policies/commit-and-change-control-policy.md` asserts an ordering the section
does not establish.
Location: `skills/spec-review-cycle.md`, Reconciliation step 4, against
`policies/commit-and-change-control-policy.md`, "Spec branches and the
reconciliation pull request"
Evidence: Verified by reading both at `582fb6f`. This document: "On a clean
gate, Dave's agreement lands as it always does — a frontmatter-only status
transition — and the PR merges." The policy: "a document reading `agreed` on the
default branch has been through the gate, because the transition that sets it is
a status-transition commit made **after the reconciliation cycle closes**."
Neither says whether the flip commit lands on the spec branch or on the default
branch.
Consequence: Under the flip-then-merge reading, a spec branch carries
`status: agreed` while its content is still unmerged and still only proposed —
so `agreed` is true of a document on a branch that Dave might yet abandon, which
is the claim the whole design exists to make impossible. The policy's structural
argument is left resting on a convention nobody wrote down.
Fix: State it: the flip lands **after the merge, on the default branch**, citing
the reviewed spec-branch SHA. That keeps `agreed` a property of the default
branch at the moment it is set, and the cited SHA still resolves — it is an
ancestor of the default branch once merged.
