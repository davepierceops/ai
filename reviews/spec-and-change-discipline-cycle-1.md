# Review: context-sets/spec-and-change-discipline.md — cycle 1

Verdict: changes-required
Reviewed: `context-sets/spec-and-change-discipline.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the whole document, with attention to the rewritten Core philosophy, the
revised canonical-sequence step 1, the new Open spec delta section, and the new
first operating habit. Checked against
`docs/cycles/friction-refactor-2026-08-09-directive.md` D2.1–D2.7 and against
`LEXICON.md` at the same SHA.
Cross-checked: `LEXICON.md` (Spec state; Dispatch), `skills/spec-review-cycle.md`
(Reconciliation), `roles/chief-of-staff.md` (Open spec deltas),
`policies/commit-and-change-control-policy.md` (Spec branches),
`operating-model.md`, `README.md`, `context-sets/ai-native-engineering.md`.
Not inspected: the red-gate and derived-field material below "Definition of done",
untouched this cycle and outside the two changes; whether any of the delta design
survives contact with a real tranche — it has never been run, and this review
cannot supply that evidence.
Findings: 2 blocking, 1 observation
Dave should inspect: B1 — the directive's own word for a concurrent workstream
collides with `Track`, and resolving it meant not using Dave's word.

## B1 — blocking
Claim: "At most two tracks run at once" reuses `track`, which `LEXICON.md` fixes
to mean the executor's repository environment (A or B), for a second and
unrelated sense: a concurrent workstream.
Location: `context-sets/spec-and-change-discipline.md`, Open spec delta,
"Concurrency is achieved by disjoint territory"
Evidence: Verified by running `grep -n "Track" LEXICON.md` at `582fb6f` —
`Track A / Track B` is a defined term two sections above the new `Spec state`
section in the same file, and `skills/directive-dispatch.md` §3 requires every
dispatch to state one. The collision is inherited from the directive's D2.5,
which uses "tracks" for workstreams, but a directive is not the lexicon.
Consequence: An agent reading "at most two tracks run at once" against the
lexicon parses a constraint on Track A and Track B — of which there are exactly
two, always — and extracts no constraint at all. This is the failure the lexicon
was created to stop; `handoff` carrying six senses is the precedent it cites.
Fix: Say "at most two tranches execute concurrently" and drop the word `track`
from the concurrency rule. The unit is already named — a delta is bounded by a
tranche, so two concurrent deltas *are* two concurrent tranches — and the
substance of D2.5 is unchanged.
Related: `reviews/chief-of-staff-cycle-2.md` B1

## B2 — blocking
Claim: The delta's editing licence is stated in the passive voice and names
nobody, so it reads as licensing any agent to edit spec documents without a
gate.
Location: `context-sets/spec-and-change-discipline.md`, Open spec delta, "The
branch is the state"
Evidence: Verified by reading the text at `582fb6f`: "spec documents are edited
freely on a dedicated branch … with no reviewer gate and no per-edit ceremony."
The directive's D2.1 says "**Dave** may edit spec documents freely." The subject
was dropped in transcription.
Consequence: This document is loaded into any chat that produces specs
(`include-when`), alongside `roles/coder-agent.md` and the rest. As written it
tells an implementation agent that spec edits need no gate while a tranche is
executing — which inverts `roles/spec-reviewer-agent.md`'s hard gate and
`context-sets/collab-workflow.md`'s rule that agreement of a canonical document
returns to Dave. The one class of edit the methodology most carefully gates
becomes, by omission, the least gated.
Fix: Name the actor. "Dave edits spec documents freely on a dedicated branch";
agents propose spec edits as they always have.

## O1 — observation
Claim: "Definition of done (spec discipline view)" is unchanged and does not
mention reconciliation.
Location: `context-sets/spec-and-change-discipline.md`, Definition of done
Evidence: Inferred by reading. The section defines done for a *change*;
reconciliation is bounded by a *tranche*.
Consequence: None found. A change can be done while its tranche's delta is open,
which is the intended behaviour — reconciliation gates the next decomposition,
not this change's release. Recorded so a later reader does not read the silence
as an oversight.
Fix: None required. If a tranche-level definition of done is ever written,
reconciliation belongs in it.
