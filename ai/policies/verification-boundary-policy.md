# Policy: Verification Boundaries

Status: draft

## Purpose

This policy makes verification boundaries visible and intentional.

A verification boundary is the point where evidence stops. It is the line between what has been checked and what is merely assumed, mocked, deferred, or accepted as risk.

## Core rule

Every meaningful mock, stub, fake, fixture, simulated service, generated response, assumed external behavior, browser substitute, or deployment assumption must have a declared verification boundary.

## Policy statement

Agents must not let tests imply broader confidence than they actually support.

When a test uses a mock, fixture, jsdom, fake timer, fake API, generated data, local-only config, or simulated environment, the agent must be able to answer:

1. What production behavior is represented?
2. What did the evidence verify?
3. What did the evidence not verify?
4. What verification is required elsewhere?
5. Does the gap block release?
6. Who or what owns the follow-up?

## Boundary declaration

A boundary declaration should include:

- boundary name
- production surface
- representation mechanism
- verification class
- verified claims
- unverified claims
- deferred verification path
- release impact
- owner or trigger for follow-up

Example:

```yaml
boundary: stadia.geocoding
production_surface: "fetch() call to live geocoding provider"
representation: "MSW handler with canned response fixture"
verification_class: "mock-verified"
verified_claims:
  - "request URL is constructed as expected"
  - "query parameters are encoded"
  - "successful response is parsed"
  - "empty response is handled"
unverified_claims:
  - "API key is configured"
  - "provider accepts request"
  - "domain/CORS rules allow production browser usage"
  - "quota and billing state are valid"
  - "live response shape still matches fixture"
deferred_verification:
  - "live geocoding smoke test"
  - "pre-release checklist"
release_impact: "blocking before first production release unless Dave explicitly accepts risk"
```

## Boundary types

Common boundary types include:

- mocked HTTP APIs
- mocked browser APIs
- mocked storage
- mocked authentication
- mocked authorization
- mocked time
- mocked geolocation
- mocked service workers
- mocked network state
- mocked map/tile providers
- local fixtures representing third-party data
- generated data standing in for production data
- jsdom replacing a real browser
- local development config replacing production config
- local environment variables replacing deployed secrets/config
- SLO targets and error budget state not yet connected to production monitoring

## Required status labels

Use these labels:

- `mock-verified`
- `contract-verified`
- `live-verified`
- `browser-verified`
- `production-verified`
- `unverified`
- `deferred`
- `accepted-risk`
- `blocking`

## Release impact labels

Each material boundary gap should be labeled as one of:

- `blocking`: must be resolved before release
- `deferred`: intentionally postponed with a named mechanism
- `accepted-risk`: Dave or the release process has explicitly accepted the gap
- `not-material`: known but not relevant to the release decision

## Required triggers

Update or create a boundary declaration when:

- adding a new mock
- changing a fixture for external data
- adding or changing an external integration
- adding browser/PWA/service-worker behavior
- changing authentication or authorization behavior
- changing production environment/config assumptions
- changing monitoring or synthetic checks
- discovering that a test passed despite unverified production behavior
- shipping with a known unverified dependency

## Documentation location

Boundary information may live in:

- `ai/boundaries/` for durable cross-cutting boundaries
- a feature-specific verification ledger
- inline test comments for small/local boundaries
- a change package
- a release-readiness review
- a pre-release checklist

For durable or repeated boundaries, prefer `ai/boundaries/` or a dedicated project verification ledger.

## CI and automation expectations

Fast unit tests should remain fast and deterministic.

Live/browser checks should normally be separate from the default unit suite. They may run:

- manually before release
- in a dedicated CI job
- on a schedule
- after deploy as synthetic monitoring

The important rule is not “run live tests constantly.” The important rule is “know which claims require live/browser/production evidence.”

## Reviewer obligations

The Spec Reviewer Agent should check that durable boundaries declared in
`ai/boundaries/` are consistent with the TRD's standing verification boundary
section, and flag drift as a continuity finding.

The Reviewer Agent should check whether boundaries are named and documented.

The Skeptic/Risk Agent should challenge overbroad confidence claims.

The Release Manager Agent should ensure material boundary gaps are resolved, deferred, or accepted before release.

## Release requirement

Before release, all material verification boundaries must be in one of these states:

1. verified by an appropriate mechanism
2. explicitly deferred with a named path
3. explicitly accepted as a known risk by Dave
4. explicitly marked not material to the release

Implicit unknowns are not acceptable.

## Non-goals

This policy does not require live tests for every dependency in every run.

It requires that confidence boundaries be visible, intentional, and tied to release judgment.
