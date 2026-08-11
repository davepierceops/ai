# Review: roles/chief-of-staff.md — cycle 4

Verdict: ready
Reviewed: `roles/chief-of-staff.md` @ `4ccfaeb`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-10
Scope: the C3 edits — the "Prompt generation — at execution time, not before"
subsection removed and replaced by a one-sentence dispatch rule, and the
decomposition paragraph's "it contains no prompts" conformed. Checked: (1) that
nothing in the removed subsection is load-bearing elsewhere, by grepping the
tree for each obligation it stated — the `.prompts/<tranche>-<package>.md` path,
"state the path", "Dave owns the final used", and the four-item coverage list;
(2) the replacement against `skills/directive-dispatch.md`, for whether "a
package is dispatched per" resolves to an actual procedure; (3) the
decomposition-doc paragraph read whole after the edit, since the removed
subsection was what "it contains no prompts" pointed forward to; (4) the
Open-spec-deltas subsection above it, which the removal now abuts, for a
dangling reference; (5) the `Handling execution-session reports` section, which
names the report an execution session returns and is the one place this role
consumes a named inbound artifact — checked against the `Prompt` tombstone's
routing in `LEXICON.md`.
Cross-checked: `skills/directive-dispatch.md` (Purpose; The three requirements;
Executor obligations), `LEXICON.md` (Retired terms; Dispatch),
`context-sets/ai-native-engineering.md` (Separation of concerns),
`.gitignore` (the removed `.prompts/` stanza), `OPEN-ITEMS.md` (the struck
chat-originated-prompts entry), `roles/orchestrator-agent.md` (superseded and
frozen; deliberately not conformed).
Not inspected: Activation behavior, the read-sequence, the computed-state
constraint, and Pre-staging — untouched since cycle 3.
Findings: none

One note. `roles/orchestrator-agent.md` carries four "prompt" uses in the sense
C4 retires, and is `status: superseded` with `superseded-by:
roles/chief-of-staff.md`. It was left alone: a frozen document is a record of
what a superseded role said, and conforming it would make it a worse record
without making anything truer. Recorded here because it is the largest
unconformed cluster left in `roles/`, and a later sweep should find the reason
rather than re-derive it.

Prior cycle: `reviews/chief-of-staff-cycle-3.md`
