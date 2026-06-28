# Boundary: Mocked Boundaries

Status: draft

## Summary

A mocked boundary is any place where a test or agent-controlled environment replaces production behavior with simulated behavior.

## Policy

Mocks are acceptable, but they must not create hidden confidence.

A mock should be treated as:

> A claim about our side of the contract, with the other side verified elsewhere or explicitly accepted as unverified.

## Common mocked boundaries

- HTTP APIs
- browser APIs
- time
- geolocation
- storage
- authentication
- authorization
- map/tile providers
- service workers
- network status
- generated test data
- third-party response fixtures
- SLO monitoring and error budget tracking (targets defined but no production
  signal in place)

## Required declaration

For each material mocked boundary, declare it using the boundary declaration
schema in `policies/verification-boundary-policy.md`. At minimum, document:
production surface, mock mechanism, what is verified, what is not, deferred
verification path, and release impact.

## Example

```yaml
boundary: external.geocoding
production_surface: "fetch() to live geocoding provider"
mocked_by: "MSW handler in unit/component tests"
verified_by_mock:
  - "request construction"
  - "response parsing"
  - "empty result handling"
not_verified_by_mock:
  - "valid API key"
  - "provider availability"
  - "live schema compatibility"
  - "quota and billing state"
deferred_to:
  - "live smoke test"
  - "pre-release checklist"
release_status: "blocking until live verification or Dave accepts risk"
```
