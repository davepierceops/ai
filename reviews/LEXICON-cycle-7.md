# Review: LEXICON.md — cycle 7

Verdict: changes required
Reviewed: `LEXICON.md` @ `4ccfaeb`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-10
Scope: the Dispatch, Blocks, Handoff, and Retired-terms sections, over the C1,
C2, and C4 edits. Checked: (1) the `Directive` definition's three-part
enumeration against `skills/directive-dispatch.md`'s "The three requirements"
and `skills/spec-review-cycle.md`'s Cycle directive format, for agreement on
which three and on the all-three-stated invariant; (2) the `Track` tombstone
against the behavior it claims survives, by reading
`skills/directive-dispatch.md` Executor obligations; (3) the `Sync block`
definition against §3 Execution block, now that the Track A scoping is gone;
(4) the new `Baton` entry against the `Handoff` entry it sits under, adversarially,
for whether the two can both be true; (5) the `Prompt` tombstone's routing
against an independent inventory of typed-at-or-consumed-by-a-session artifacts,
swept from this file and all nine skills; (6) every pointer this file's edited
regions make, resolved at HEAD.
Cross-checked: `skills/directive-dispatch.md` (Purpose; Use when; The three
requirements; §3 Execution block; Executor obligations),
`skills/spec-review-cycle.md` (Cycle directive format; Hard constraints; Inputs),
`context-sets/spec-and-change-discipline.md` (concurrency parenthetical),
`context-sets/collab-workflow.md` (Session handoff),
`roles/coder-agent.md` and `docs/packages/package-c-change-package.md` (the two
handoff uses the entry keeps), `vendors/claude-code/environment-config.md` (the
approval-prompt sense the tombstone exempts); `bin/check-frontmatter --all` by
execution (clean, 47 files in scope, 10 globs).
Not inspected: the three layers, Sessions, and Spec state — untouched since
cycle 6 and not reached by any edit here.

## B1 — the `Baton` entry contradicts the `Handoff` entry it sits under

Severity: blocking
Claim: `Baton`'s `*Not:*` line read "*Not:* a handoff. A handoff is the transfer;
a baton is what travels." The `Handoff` entry defines a handoff as "transfer of
unfinished responsibility between sessions or roles, **and the set of things that
must travel with it** for the receiver to continue" — so "what travels" is part
of what `handoff` denotes, not its complement.
Location: `LEXICON.md`, Handoff, `Baton`
Evidence: Verified by reading both entries at `4ccfaeb`. The `Handoff` entry's
own `*Not:*` paragraph does distinguish "the transfer and the artifact", which is
where the contradicting formulation came from — but that paragraph is about not
calling a *directive* a handoff, and the definition line above it is the one that
governs what the word covers.
Consequence: A reader resolving `baton` against `handoff` finds each entry
denying a clause of the other. The distinction C2 actually needs is
baton-versus-directive, which the boundary sentence already carries; the
handoff denial adds nothing and costs the entry its consistency.
Fix: Replace the `*Not:*` line with a directive/dispatch denial, and state the
baton as one artifact class *within* a decision-to-decision handoff.
Status: FIXED at `9adf89d`.

## N1 — the two tombstones are not symmetric

Severity: non-blocking
Claim: `Prompt` sits in full under `## Retired terms`; `Track` sits in full under
`## Dispatch`, with a one-line pointer from `## Retired terms`.
Location: `LEXICON.md`, Dispatch and Retired terms
Evidence: Verified by reading. The asymmetry is deliberate and recorded at
`docs/cycles/friction-refactor-2026-08-09-decisions.md` D22: a tombstone earns
its keep by sitting where the reader looks the term up, and someone holding an
August directive that reads `Track: A` opens the file at Dispatch.
Consequence: A reader scanning `## Retired terms` for the complete set of dead
terms gets one entry and one pointer rather than two entries. The pointer
resolves, so nothing is lost, but the section does not read as a register.
Fix: None taken. If a third term is ever retired the question reopens, and the
answer then is probably a register section with every tombstone in it and
in-place pointers, rather than the reverse.

Findings: 1 blocking (fixed), 1 non-blocking (no fix taken)
Prior cycle: `reviews/LEXICON-cycle-6.md`
