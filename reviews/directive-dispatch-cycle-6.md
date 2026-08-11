# Review: skills/directive-dispatch.md — cycle 6

Verdict: changes required
Reviewed: `skills/directive-dispatch.md` @ `4ccfaeb`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-10
Scope: the C1 edits — the frontmatter description, *Use when*, "The three
requirements", the deletion of §3 Track, the renumbered §3 Execution block, the
new executor obligation, and the revision note. Checked, adversarially, for what
the deleted section carried that nothing else states: §3 was read at `4ccfaeb^`
line by line and each behavioral claim in it traced to a surviving home or to
nothing. Also checked: (1) the three-requirement count against `LEXICON.md`
`Directive` and `skills/spec-review-cycle.md`'s Cycle directive format; (2) the
sync-block bullet with the Track B carve-out removed, against `LEXICON.md`'s
`Sync block`; (3) section renumbering against every `§n` reference in the tree;
(4) the revision note against the D8 convention that notes are appended, not
retrofitted; (5) the frontmatter `description` field, which is loaded as skill
metadata and stated the retired field.
Cross-checked: `LEXICON.md` (Dispatch; Blocks; Handoff),
`skills/spec-review-cycle.md` (Procedure steps 6–7; Cycle directive format),
`policies/remote-write-verification-policy.md` (Rules 1–4; Scope),
`skills/command-blocks.md` (conformance criteria, for the sync block),
`context-sets/spec-and-change-discipline.md`; `git show 4ccfaeb^:skills/directive-dispatch.md`
for the deleted text; `grep -rn "§[0-9]"` over the tree for dangling section
pointers; `bin/tests/run` by execution.
Not inspected: the model table, the naming schema, and *Writing the directive
file* — untouched, cleared at cycle 4, and not reached by C1.

## B1 — deleting §3 removed the only statement that the executor pushes

Severity: blocking
Claim: §3's Track A paragraph read "The executor has a working tree and a
reachable remote: it commits the directive, **pushes**, and reports the pushed
SHA." That was the sole place in this document requiring the push. Executor
obligations said "write it … commit it, and read the SHA back"; the Purpose
paragraph said "write it to `docs/cycles/`, commit it, read the SHA back, and
report". Neither said push.
Location: `skills/directive-dispatch.md`, Executor obligations; Purpose
Evidence: Verified by running. `git show 4ccfaeb^:skills/directive-dispatch.md |
grep -n "push"` returns four lines, `:81` and `:86-88`, every one inside §3 —
`:81` is Track A's requirement and the rest are Track B's account of why a local
SHA is not citable. At `4ccfaeb` the same grep returns three lines, `:127`,
`:130`, and `:187`: two in the new unreachable-remote obligation and one in the
revision note recording it. All three are the *exception*; the rule they except
is stated nowhere. `LEXICON.md`'s `Directive file` entry says "written and committed
by the executor as its first act" and is likewise silent on the push.
Consequence: The new obligation reads "an executor that cannot push stops", and
an executor looking for where it was told to push finds nothing. Worse, the
degradation the obligation exists to prevent — commit locally, report the SHA,
say nothing — becomes *conformant*, because a local commit satisfies every
surviving step. C1 intended to make that failure harder, and as landed it made
it legal.
Fix: Add the push to the land-first obligation and to the Purpose enumeration,
and say what it buys: the reported SHA is a pushed SHA, which is what makes it
resolvable outside this clone.
Status: FIXED at `9adf89d`.

## B2 — a false historical claim inside a living rule

Severity: blocking
Claim: The new obligation ended "This is not a directive field and never was one
to state." Track was a stated directive field from `DEC-000110` through
`DEC-000150` and appears as a `Track:` header line in nine directives under
`docs/cycles/`.
Location: `skills/directive-dispatch.md`, Executor obligations
Evidence: Verified by running. `grep -rn "^Track: " docs/cycles/ | wc -l` → 9.
`decisions/log.md` `DEC-000150` reads "**track is required per directive**,
because it genuinely varies".
Consequence: A reader who has seen a `Track:` line and then reads "never was one
to state" concludes the document is wrong about its own history, which is
corrosive to every other empirical claim in it. The point the clause wanted to
make — that the condition is not knowable by the party writing the directive —
is the actual argument and survives the correction.
Fix: State the reason it is not a field now, not a claim about the past.
Status: FIXED at `9adf89d`.

## O1 — everything else §3 carried has a home

Severity: observation
Claim: Beyond the push, §3's surviving content is fully rehoused.
Location: `skills/directive-dispatch.md`, Executor obligations; `LEXICON.md`
Evidence: Verified by reading `4ccfaeb^`'s §3 clause by clause. "No reachable
remote: forge down, no credential, offline" → the obligation's parenthetical.
"An unpushed commit resolves in that clone and nowhere else" → the obligation,
verbatim in substance. "Stops and surfaces it rather than silently degrading to
a local commit" → the obligation, promoted from a Track B aside to a first-class
executor rule. "A SHA exists the moment `git commit` runs" → dropped, and
deliberately: it was true only as a defence of reporting an unpushed SHA, which
is now forbidden. "Track B is operator-invoked; the agent never infers it" →
dropped, having nothing left to invoke. Recorded so a later reader can see the
deletion was audited rather than assumed.

Findings: 2 blocking (both fixed), 1 observation
Prior cycle: `reviews/directive-dispatch-cycle-5.md`
