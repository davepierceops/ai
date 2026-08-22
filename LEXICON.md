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
record. The default branch therefore never carries unreviewed spec text, and
`agreed` there never lies.

**Claimed** — of a spec document: appearing in an open delta's diff. A claimed
document may not be claimed by a second open delta. Concurrency comes from
claiming disjoint territory, never from merging convergent edits.

## Evidence classes

The classes an evidence claim is labelled with. Every verification claim carries
one.

**Mock-verified** — against controlled or simulated inputs.

**Contract-verified** — against a documented or encoded interface contract.

**Live-verified** — against a real external system or deploy-like service.

**Browser-verified** — in a real browser environment.

**Production-verified** — through deployed telemetry, monitoring, synthetic
checks, logs, or real production signals.

**Unverified** — known but not yet checked.

**Deferred verification** — intentionally postponed, with a named future
mechanism.

**Accepted risk** — an explicit decision to proceed despite a known gap.

## Service levels

**Top K** — the K most important user journeys of a product. The list is defined
once, in the PRD; the TRD sets SLO targets against it and does not redefine it.
Where a document requires SLO status or error budget accounting "for Top K
journeys," it means that list.

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

**Dispatch** — retired 2026-08-21. Write "hand the directive to an execution
session," or "direct."

**Sync block** — retired 2026-08-21. Nothing precedes the execution block; the
executor fetches as its first act.

**Track** — retired 2026-08-21. A directive states route and model tier; there
is no third part.

*Not covered by this retirement:* **error budget tracking**, **SLO tracking**,
and similar SRE compounds, along with the ordinary verb "keep a list of." Those
are a different word in a different domain, and they keep their ordinary
meaning.
