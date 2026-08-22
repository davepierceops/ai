---
status: in-review
last-reviewed: null
audience: [all-roles, human]
order: 2
---

# Lexicon

Terms with a fixed meaning across this methodology.

Governed like any canonical document: changes enter through a review cycle.

**The touch rule:** any file edited for another reason is conformed to this
lexicon as part of that edit.

## Spec state

**Tranche** — one concurrent workstream of build work.

**Spec branch** — the branch a tranche's spec edits land on, named
`spec/<tranche-slug>`. Git is the machinery; there is no status value for this
and no register recording it. The branch existing, with commits on it, is the
state.

**Open spec delta** — the interval during which a tranche's spec branch carries
edits that the default branch does not. During it Dave edits spec documents
freely, with no reviewer gate and no per-edit ceremony. A delta is bounded by
its tranche and never spans two.

**Reconciliation** — closing a delta: the spec is brought to full agreement with
what was actually built, and the whole accumulated diff goes through the
reviewer gate **once** — once per delta, not once per edit — arriving on the
default branch as a pull request. Agreement attaches here, to the version of
record.

**Claimed** — of a spec document: appearing in an open delta's diff. A claimed
document may not be claimed by a second open delta. Concurrency comes from
claiming disjoint territory, never from merging convergent edits.

## Retired terms

**Prompt** — not a term of this methodology. What is meant is one of:

- **What a decision session hands an execution session** — a *directive*; its
  committed form is a *directive file*, its transport is an *execution block*,
  and one direction inside it is an *instruction*.
- **What a decision session hands its successor decision session** — a *baton*.
- **What a directive points the executor at** — a *companion document*.
- **What runs in a shell** — a *command block*.
- **What a session loads as standing context** — a *context set*, a *role
  document*, a *skill document*, a *policy*, a *boundary document*.
- **What a session derives work from** — the *decomposition doc*, a *change
  package*, the *acceptance criteria*, the *spec* (PRD/TRD).
- **Inbound material a session acts on** — the specific name of that material:
  *reviewer findings*, a *review artifact*, an *execution report*, an *upload*,
  a *retro*.

*Not covered by this retirement:* an approval **prompt** — a tool interrupting
to ask a human to authorise a step. That is a different word in a different
domain, and it keeps its ordinary meaning.
