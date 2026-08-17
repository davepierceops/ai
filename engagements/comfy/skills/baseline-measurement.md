---
status: agreed
last-reviewed: reviews/expedited-log.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293
audience: [cartographer, implementer, chief-of-staff-engagement, human]
---

# Skill: Baseline Measurement

The baseline-gate procedure. The engagement translation of the parent model's
red-gate: **the baseline is the failing test.** No optimization is implemented
until the stopwatch exists, the baseline is captured, and the expected delta
is stated in advance.

## Procedure

1. **Enumerate the stages** from the System Map: trigger delivery, queue,
   runner boot, checkout, auth, init, plan, apply, image build, image push,
   image pull, boot, data hydration, health-to-ready — whatever the actual
   pipeline's stages are.
2. **Instrument read-only first.** CI systems already timestamp nearly
   everything; extract stage timings from existing logs and APIs before
   proposing any pipeline change. Instrumentation that requires a change ships
   as a PR like anything else.
3. **Capture a distribution, not an anecdote.** Enough runs to state p50 and
   p95 per stage. One fast run proves nothing; tails are where the pain
   lives.
4. **Publish the baseline** — one document, beside the System Map in the
   engagement working repo (`system-discovery.md`): per-stage distributions,
   total, date range, run count, and known confounds. This is the
   engagement's most load-bearing artifact.
5. **Gate improvements on an expected-delta statement**: "this change attacks
   stage X, currently p50 A / p95 B; expected result: p50 → A′" — stated
   before implementation, recorded in the change package.
6. **Re-measure after the change** with the same stopwatch, same method.
   The delta claim in the change package cites both measurements
   (delta-verified, per `../roles/implementer.md`).

## Override

Dave may override the baseline-gate for a given change with an explicit
statement; logged per `../policies/override-log-policy.md`. The measurement
debt is named in the change package.

## Failure modes to avoid

- optimizing the stage that is easiest to see instead of the stage the
  distribution indicts
- changing the stopwatch and the pipeline in the same change
- reporting means; report p50/p95
- measuring spin-up but not teardown — teardown failures are silent spend
