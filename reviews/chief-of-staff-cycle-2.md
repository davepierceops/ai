# Review: roles/chief-of-staff.md — cycle 2

Verdict: changes-required
Reviewed: `roles/chief-of-staff.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the revised read-sequence item 3, the new paragraph opening "Handling
execution-session reports", and the new "Open spec deltas" subsection. Checked
against `docs/cycles/friction-refactor-2026-08-09-directive.md` D1.1, D2.3–D2.5.
Cross-checked: `LEXICON.md` (Track A / Track B; Spec state),
`context-sets/spec-and-change-discipline.md` (Open spec delta),
`skills/directive-dispatch.md` (§3 Track; §4 Execution block),
`decisions/log.md` `DEC-000070` (what a decomp doc pins).
Not inspected: Activation behavior, Pre-staging, Prompt generation, and
Constraints — untouched this cycle; the computed-state constraint's interaction
with the new read-sequence item was checked for contradiction but the item was
not executed against a live tree.
Findings: 1 blocking, 1 non-blocking
Prior cycle: `reviews/chief-of-staff-cycle-1.md`

## B1 — blocking
Claim: "Propose at most two concurrent **tracks**" uses `track` in a sense
`LEXICON.md` does not carry and that collides with the sense it does.
Location: `roles/chief-of-staff.md`, Open spec deltas, third bullet
Evidence: Verified by running `grep -n "Track" LEXICON.md` at `582fb6f`:
`Track A / Track B` is defined as the executor's repository environment, and this
document's own "Mid-delta directives cite the spec branch" bullet points at
`skills/directive-dispatch.md`, where a dispatch must state one. Same word, two
senses, both live in one file.
Consequence: CoS is the role that drafts dispatches, so it holds both senses
simultaneously and has no way to tell which a sentence means. The concurrency
rule — the one thing standing between two deltas and the refused merge case —
becomes unreadable at exactly the moment it binds.
Fix: "Propose at most two tranches executing concurrently." A delta is bounded by
a tranche, so the unit is already named and no meaning is lost.
Related: `reviews/spec-and-change-discipline-cycle-1.md` B1

## N1 — non-blocking
Claim: The read-sequence adds "`spec/*` branches ahead of the default branch with
no reconciliation pull request open" without saying how to compute it.
Location: `roles/chief-of-staff.md`, The read-sequence, item 3
Evidence: Inferred by reading. Items 1 and 2 name their sources concretely
(`OPEN-ITEMS.md`, `git log`); item 3's other clauses name queryable things (open
`human-gate` issues, `docs/cycles/` against `reviews/`, `status: in-review`).
This clause names a state without naming the query.
Consequence: The check is skippable by ambiguity rather than by decision — the
weakest failure mode for a step whose whole purpose is that nothing sits silently
in a queue. `OPEN-ITEMS.md` already tracks the enforcement gap for the related
claim rule; this is the read-side of the same gap.
Fix: Name the query inline, or leave it to the `bin/` script the open item
proposes. Not blocking: the state is genuinely computable and a CoS instance can
derive the command.
