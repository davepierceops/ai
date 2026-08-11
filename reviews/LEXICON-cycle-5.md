# Review: LEXICON.md — cycle 5

Verdict: ready-with-findings
Reviewed: `LEXICON.md` @ `7d4d03a`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: re-check of the Spec state section against the cycle-1 fixes made to
`context-sets/spec-and-change-discipline.md` and `skills/spec-review-cycle.md` —
specifically whether any definition here now trails the rule it points at.
Cross-checked: `context-sets/spec-and-change-discipline.md` (Open spec delta),
`skills/spec-review-cycle.md` (Reconciliation),
`roles/chief-of-staff.md` (Open spec deltas).
Not inspected: the Dispatch, Blocks, Handoff, and Prompt sections — reviewed at
cycle 4 and untouched since.
Findings: 1 non-blocking
Prior cycle: `reviews/LEXICON-cycle-4.md`

**Cycle 4's N1 stands as recorded** — a non-blocking observation about the
redefined `Track A / Track B`, with no fix taken and the alternative logged at
`docs/cycles/friction-refactor-2026-08-09-decisions.md` D1.

## N1 — non-blocking
Claim: The `Reconciliation` entry carries "once, as a single cycle", the phrasing
that produced a blocking finding at `skills/spec-review-cycle.md` and was
corrected there.
Location: `LEXICON.md`, Spec state, `Reconciliation`
Evidence: Verified by reading both at `7d4d03a`. The skill now distinguishes
once-per-delta from once-per-cycle; this entry does not, and it is the definition
of the term.
Consequence: A lexicon entry that is less precise than the rule it defines
inverts the relationship — the lexicon is where a reader goes to settle exactly
this kind of question. Non-blocking because the entry points at both governing
documents and the correct reading is one hop away.
Fix: "gate **once** — once per delta, not once per edit".
Related: `reviews/spec-and-change-discipline-cycle-2.md` N2
