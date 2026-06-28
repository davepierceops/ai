# Review Notes: v0.3

## Scope

Reviewed and revised:

- `context-sets/testing-and-verification.md`
- `policies/verification-boundary-policy.md`
- `roles/skeptic-risk-agent.md`

## Intent

These three files should operationalize the original mocked-boundary insight:

> A mock is a claim with a deferred proof.

The goal was to make this idea usable by agents during implementation, review, and release-readiness work.

## Changes made

### `context-sets/testing-and-verification.md`

Strengthened:

- distinction between test results and verification claims
- verification classes
- confidence ledger concept
- test-plan requirements
- boundary-sensitive areas
- meaning of green tests
- minimal acceptable practice
- anti-patterns

### `policies/verification-boundary-policy.md`

Strengthened:

- formal definition of verification boundary
- boundary declaration schema
- release impact labels
- required triggers for updates
- CI/live-test expectations
- reviewer obligations
- release requirements

### `roles/skeptic-risk-agent.md`

Strengthened:

- role mandate
- evidence-chain review posture
- false-confidence checklist
- boundary checklist
- risk severity categories
- output template
- non-goals

## Editorial judgment

v0.3 makes the testing/verification spine much stronger.

The operating model now has a clear enforcement path:

1. `base.md` states agent claims require evidence.
2. `testing-and-verification.md` defines how to classify evidence.
3. `verification-boundary-policy.md` requires boundaries to be documented.
4. `skeptic-risk-agent.md` challenges overbroad confidence before release.

## Next likely review targets

Recommended next pass:

1. `policies/agent-review-policy.md`
2. `policies/release-readiness-policy.md`
3. `skills/evidence-review.md`
4. `skills/release-readiness-review.md`

Those should align the review and release machinery with the stronger v0.3 verification language.
