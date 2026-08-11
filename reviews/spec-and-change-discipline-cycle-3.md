# Review: context-sets/spec-and-change-discipline.md — cycle 3

Verdict: ready-with-findings
Reviewed: `context-sets/spec-and-change-discipline.md` @ `ad240d4`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: confirmation pass over cycle 2's B1, N1, and N2, and a final read of the
whole Open spec delta section for anything the three cycles of edits left
inconsistent.
Cross-checked: `LEXICON.md` (Spec state), `skills/spec-review-cycle.md`
(Reconciliation), `roles/chief-of-staff.md` (Open spec deltas),
`operating-model.md`, `README.md`.
Not inspected: sections outside Core philosophy and Open spec delta, cleared at
cycle 1 and untouched since.
Findings: 1 observation
Prior cycle: `reviews/spec-and-change-discipline-cycle-2.md`

**Cycle 2 findings, re-checked — all resolved.** B1: `grep -n '\btracks\?\b'`
over the file at `ad240d4` returns only the parenthetical that warns against the
word; "the second tranche goes cross-project" replaces the missed sentence. N1:
both paragraphs rewrap at the file's width. N2: the reconciliation rule now reads
"once — once per delta, not once per edit", matching the skill.

## O1 — observation
Claim: The "frequent small reconciliations are the encouraged norm / the tranche
boundary is a deadline, not a target" point is stated in full both here and in
`skills/spec-review-cycle.md`.
Location: `context-sets/spec-and-change-discipline.md`, "A delta is bounded by
its tranche", against `skills/spec-review-cycle.md`, "A reconciliation may be
invoked early"
Evidence: Verified by reading both at `ad240d4`. Neither points at the other for
this point; each states it in its own words.
Consequence: A second copy of a rule drifts, which this repo treats as a defect
class in its own right. Against that: the two statements serve different readers —
this one is part of the rule set, the skill's is guidance to whoever is running a
cycle — and the wording differs deliberately rather than by accident. Left as an
observation rather than a finding because collapsing it would mean one of the two
documents losing a point its own reader needs.
Fix: If it drifts, the skill's copy becomes a pointer here. Not done now: three
cycles of edits is enough churn on this paragraph, and the duplication is
currently exact in substance.
