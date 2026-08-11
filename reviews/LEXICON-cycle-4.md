# Review: LEXICON.md — cycle 4

Verdict: ready-with-findings
Reviewed: `LEXICON.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the redefined `Track A / Track B`, `Execution block`, and `Directive
file`; the revised `Sync block`; and the new `Spec state` section. Checked that
each definition matches the document that owns the rule, and that no other entry
was left describing the retired delivery path.
Cross-checked: `skills/directive-dispatch.md` (Purpose; §3 Track; §4 Execution
block), `skills/spec-review-cycle.md` (Reconciliation),
`context-sets/spec-and-change-discipline.md` (Open spec delta),
`policies/commit-and-change-control-policy.md` (Spec branches),
`decisions/log.md` `DEC-000090`, `DEC-000150`.
Not inspected: the three-layers, Sessions, Handoff, and Prompt sections,
untouched this cycle; the adoption-scope and touch-rule preamble, likewise.
Findings: 1 non-blocking
Prior cycle: `reviews/LEXICON-cycle-3.md`
Dave should inspect: whether the `Spec state` section should exist at all —
D2.1 asked for "no lexicon machinery beyond pointing at git", and the reading
taken is recorded at `docs/cycles/friction-refactor-2026-08-09-decisions.md` D5.

## N1 — non-blocking
Claim: `Track A / Track B` keeps its name while changing what it denotes, and the
only guard against the old reading is a `Not:` line.
Location: `LEXICON.md`, Dispatch, `Track A / Track B`
Evidence: Verified by running `git show 582fb6f^:LEXICON.md` against the current
text. Old: "the two paths a directive takes to become **citable** … Track B
produces it in an artifact, and Dave commits it from a local clone." New: "the
executor's repository environment, and so the two paths a directive takes to
become citable." The commit-not-push half is continuous; the delivery half is
gone.
Consequence: Documents outside the governed set still carry the old sense —
`docs/global-retro-inbox.md`, `retros/retro-20260807-194436.md`,
`docs/research/methodology-scan-phase2-findings.md` — and a reader arriving from
one of those reads a live term with a changed meaning and no signal. The `Not:`
line answers this for anyone who reaches the lexicon; it does not reach anyone
who does not.
Fix: The touch rule already governs this — those files are records of what
happened and are not conformed (`LEXICON.md`, "The touch rule"; the same reason
`reviews/` is not retrofitted). Recorded rather than fixed. The alternative,
retiring the label and coining a new one, was considered and rejected at
`docs/cycles/friction-refactor-2026-08-09-decisions.md` D1, chiefly because
`DEC-000150` requires `bin/cycle-open` to emit a field called Track.
