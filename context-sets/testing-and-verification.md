---
status: draft
last-reviewed: null
audience: [all-roles, human]
order: 5
depends-on: []
---

# Context Set: Testing and Verification

Rules for execution sessions.

## Summary

Testing is not the same as verification.

A test executes a controlled scenario. Verification is the confidence claim drawn from that evidence. This project requires agents to state the boundary of each verification claim.

The central risk is not undertesting. The central risk is **overclaiming what a test proves**.

## Core principle

> A mock is a claim with a deferred proof.

Every mock should make the boundary visible:

1. What production behavior is being represented?
2. What does this test verify?
3. What does this test not verify?
4. Where is the missing side verified?
5. If not verified, is that gap blocking, deferred, or accepted?
6. Who or what owns the follow-up?

## Verification classes

What each class does and does not support. The classes themselves are defined in
the lexicon.

### Mock-verified

Useful for:

- application logic
- parsing
- error handling
- UI state
- edge cases
- retry behavior
- fast local feedback

Does not prove:

- third-party auth
- live availability
- live schema stability
- browser-only behavior
- deployment config
- quota/billing state
- CORS/domain rules

### Contract-verified

Useful for:

- fixture shape
- schema expectations
- required fields
- API assumptions
- compatibility checks

Does not prove:

- live credentials
- provider availability
- provider account state
- quota or billing
- CORS/domain restrictions
- browser rendering

### Live-verified

Useful for:

- credentials
- provider availability
- auth shape
- live response shape
- real status codes
- quota/billing/config failures

Does not prove:

- all edge cases
- future availability
- complete UX correctness
- browser rendering unless run in browser

### Browser-verified

Useful for:

- rendering
- layout
- map/tile loading
- service worker behavior
- PWA behavior
- browser-only APIs
- real network behavior from the page

Does not prove:

- all devices
- all browsers
- all network conditions
- production health over time

### Production-verified

Useful for:

- ongoing dependency health
- real-world failure modes
- regressions after deploy
- availability
- live user impact
- SLO target compliance — confirming the system is meeting the targets defined
  in the TRD for each Top K user journey
- error budget consumption — tracking how much of the allowed failure budget has
  been spent; a verification claim made against an exhausted or critical error
  budget is materially weaker than one with headroom

A production-verified claim should state:
- which SLO was checked and its current status (healthy / degraded / exhausted)
- current error budget remaining, if known
- whether error budget state was a factor in the release decision

Does not replace pre-deploy checks for known high-risk paths.

## Confidence ledger

For meaningful changes, agents should be able to produce a confidence ledger.

Example:

```text
Claim: External API client parses a valid provider response.
Evidence: Mock-verified unit test with fixture.
Boundary: Does not verify live provider auth, quota, domain restrictions, or current schema.
Deferred verification: live smoke test against the provider.

Claim: The results view renders the returned records.
Evidence: Component test in a headless DOM.
Boundary: Does not verify browser network requests or visible rendering.
Deferred verification: browser smoke test with network observation.
```

The ledger does not need to be heavyweight. It needs to prevent false confidence.

## Test plan requirements

A test plan for meaningful changes should include:

1. Acceptance criteria.
2. Test levels used.
3. Mocked dependencies.
4. Fixture sources.
5. Contract assumptions.
6. Live verification needs.
7. Browser/PWA verification needs.
8. Production monitoring or synthetic checks, if relevant.
9. Known unverified behavior.
10. Release impact of gaps.

## Boundary-sensitive areas

This list names areas where a claim is easy to overstate. The verification
boundary policy's boundary types name the representation mechanisms that stand
in for production; the two lists are complementary cuts, not competing
taxonomies.

Treat these areas as boundary-sensitive by default:

- external APIs
- auth and authorization
- environment variables
- browser-only behavior
- maps, tiles, geolocation, and rendering libraries
- service workers and PWA offline behavior
- payment, email, notification, or messaging services
- storage and persistence
- time, timers, and scheduling
- rate limits, quotas, and billing
- hosted databases
- analytics and telemetry providers
- domain and CORS restrictions
- SLO targets and error budget state — production signals that tests cannot
  capture; error budget exhaustion is a release-relevant condition
- security and privacy controls

Boundary-sensitive does not mean "must be overtested." It means "do not overclaim."

## Required output when tests are written or reviewed

This is the verification-specific expansion of the Evidence, Boundary, and Gaps
elements of the standard response shape, not a second shape. When writing or
reviewing tests, agents should state:

- what is verified
- what is not verified
- what is mocked
- what assumptions the fixture encodes
- whether live/browser/production verification is needed
- how the verification boundary is recorded
- whether any gap blocks release

## Minimal acceptable practice

For a small project or early-stage feature, the minimum acceptable practice is:

1. Keep fast mocked/unit tests.
2. Declare mocked boundaries.
3. Add at least one live or browser smoke test for material external/user-visible integrations.
4. Keep a pre-release checklist for verification not yet automated.
5. Record accepted risks explicitly.

## Anti-patterns

Avoid:

- treating a headless DOM as browser rendering
- treating agent review as evidence without stating what was reviewed
- using fixtures without knowing what assumptions they encode
- adding live tests to every unit run
- refusing mocks because live behavior matters
