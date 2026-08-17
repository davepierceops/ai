---
status: agreed
last-reviewed: reviews/expedited-log.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293
audience: [all-roles, human, client]
---

# Skill: Speed Audit

The end-to-end engagement play for "make X faster," sized to a one-week
engagement. Composes the other skills; the roles execute their parts.

## The play

1. **Discover** (`system-discovery.md`) — Cartographer maps the pipeline;
   unknowns go to Dave; Dave decides what to ask the client.
2. **Baseline** (`baseline-measurement.md`) — capture per-stage
   distributions. Change nothing yet. This is typically days one and two, and
   resisting the urge to fix things during it is the discipline.
3. **Rank** — order stages by cost at p50 and p95. Present the ranking with
   the evidence. This artifact converts a vague slowness into a named, sized
   list — often the most valuable single deliverable.
4. **Propose** — for the top stages, the CoS drafts Improvement Proposals
   (see below), pre-staged per the parent's pre-staging rule. Dave selects
   with the client's priorities in mind.
5. **Attack** — Implementer builds; Skeptic reviews; changes land as PRs
   through the client's own gates; re-measure after each landing, not in
   batches.
6. **Write up** — before/after distributions, the remaining ranked
   opportunities, and the recommendation. Written for the client's engineers
   to keep, in their vocabulary, citing their systems.

## The Improvement Proposal

One screen, drafted by the CoS from the Cartographer's map and the baseline —
the Cartographer does not propose; the Implementer does not self-authorize:

- target stage, with baseline cite (p50/p95)
- the change
- expected delta, stated in advance
- effort estimate and blast radius, with rollback path
- draft acceptance criteria

**Agreed** means Dave says yes, in chat; the proposal records it and the
change package cites it. The acceptance criteria are agreed in the same
breath.

## The meta-lesson

Speed problems in pipelines are almost never one big thing; they are several
medium things hiding behind a missing stopwatch. The audit's job is to make
the stopwatch exist and let the distribution name the culprits.
