---
status: draft
last-reviewed: null
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
   the evidence. This artifact alone is usually worth the engagement fee: it
   converts a vague slowness into a named, sized list.
4. **Propose** — for the top stages, Improvement Proposals with expected
   deltas, effort estimates, and blast radius. Dave selects with the client's
   priorities in mind.
5. **Attack** — Implementer builds; Skeptic reviews; changes land as PRs
   through the client's own gates; re-measure after each landing, not in
   batches.
6. **Write up** — before/after distributions, the remaining ranked
   opportunities, and the recommendation. Written for the client's engineers
   to keep, in their vocabulary, citing their systems.

## The meta-lesson

Speed problems in pipelines are almost never one big thing; they are several
medium things hiding behind a missing stopwatch. The audit's job is to make
the stopwatch exist and let the distribution name the culprits.
