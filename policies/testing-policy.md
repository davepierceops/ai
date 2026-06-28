# Policy: Testing

Status: draft

## Purpose

This policy defines how tests should be designed, interpreted, and maintained in an AI-native engineering workflow.

## Policy

Tests must be treated as evidence with boundaries, not as unlimited proof of correctness.

A green test suite means:

> The tested scenarios passed under the conditions represented by the tests.

It does not automatically mean:

- the product is shippable
- external integrations work
- deployment configuration is valid
- browser-only behavior works
- production behavior has been verified

## Red-gate

Tests derived from acceptance criteria must be run and confirmed to fail before
any implementation begins. A test that passes before implementation is a broken
test, not a head start. Implementation proceeds only as far as needed to turn
the confirmed-failing tests green.

This rule applies to all tiers of change. See
`policies/commit-and-change-control-policy.md` and
`context-sets/spec-and-change-discipline.md`.

## Required test planning

For meaningful changes, the Test Designer Agent should produce or update a test plan before implementation.

The test plan should include:

- behaviors to verify
- test levels required
- mocked dependencies
- live dependencies
- browser/PWA concerns
- failure cases
- risks intentionally not tested
- acceptance criteria

## Test levels

Use the smallest useful test, but do not pretend small tests verify larger claims.

Preferred levels:

1. Unit tests for deterministic logic.
2. Component tests for UI behavior.
3. Integration tests for combined local components.
4. Contract tests for external assumptions.
5. Live smoke tests for real external services.
6. Browser/E2E smoke tests for browser-only behavior.
7. Production synthetic checks or monitoring for ongoing health, including
   verification against the SLO targets defined in the TRD for each Top K
   user journey. Error budget consumption should be observable from these
   checks.

## Mocking

Mocks are allowed and encouraged when they improve speed, determinism, or isolation.

Mocks must not hide verification gaps.

Any mock of a meaningful boundary should be associated with:

- what it verifies
- what it does not verify
- where the deferred verification happens
- whether the deferred verification is required before release

## Coverage

Line coverage is a weak signal.

Coverage may show that code executed. It does not show that the code was verified against production-relevant conditions.

Do not use coverage as a substitute for boundary analysis.

## Required evidence in change packages

A change package should include:

- test commands run
- test results
- skipped tests, if any
- mocked boundaries involved
- live/browser verification performed, if any
- known unverified behavior
- recommendation on whether testing evidence is sufficient

## Release standard

A change may ship with known testing gaps only if those gaps are explicit and accepted by Dave.
