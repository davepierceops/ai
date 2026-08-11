# Review: README.md — cycle 1

Verdict: ready-with-findings
Reviewed: `README.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: key principle 9 only — the single line this directive changed. Read for
contradiction against the rest of the file; nothing else was edited.
Cross-checked: `context-sets/spec-and-change-discipline.md` (Core philosophy;
canonical sequence step 1), `operating-model.md` (Summary; Change flow step 1),
`roles/spec-reviewer-agent.md` (Gate review),
`skills/spec-review-cycle.md` (Reconciliation).
Not inspected: principles 1–8 and 10, the reading list, and the change-package
list — untouched this cycle.
Findings: 1 observation

## O1 — observation
Claim: Principle 9 now runs to roughly sixty words and carries four clauses, in a
list whose other entries are one claim each.
Location: `README.md`, key principle 9
Evidence: Verified by reading the list at `582fb6f`. Principles 1–4 and 6–7 are
single sentences of ten to thirty words; 9 was already the longest before this
edit and grew by a clause.
Consequence: Readability only. The clause added is load-bearing — without it the
principle says spec is agreed "before work begins", which
`context-sets/spec-and-change-discipline.md` now contradicts, and a README that
contradicts a context set is the drift this repo exists to stop. So the length is
the cost of correctness rather than a defect to fix by cutting.
Fix: If the list is ever tightened, principle 9 splits into two — the agreement
rule and the separation rules are independent claims sharing a bullet. Not
attempted here: restructuring the principle list is outside this directive's
blast radius.
