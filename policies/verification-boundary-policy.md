---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Verification Boundaries

This policy governs both session kinds: decision sessions and execution
sessions.

## Purpose

This policy makes verification boundaries visible and intentional.

A verification boundary is the point where evidence stops. It is the line between what has been checked and what is merely assumed, mocked, deferred, or accepted as risk.

## Core rule

Every meaningful mock, stub, fake, fixture, simulated service, generated response, assumed external behavior, browser substitute, or deployment assumption must have a declared verification boundary.

A mock is a claim about our side of the contract, with the other side verified
elsewhere or explicitly accepted as unverified.

## Policy statement

Agents must not let tests imply broader confidence than they actually support.

A mocked boundary carries the answers to the mock-boundary checklist stated in
the testing and verification context set, including who or what owns the
follow-up.

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
- cadence — how often the verification is re-run
- failure response — what happens when the verification fails
- owner or trigger for follow-up

Example:

```yaml
boundary: external-api.record-lookup
production_surface: "request to the live provider's record-lookup endpoint"
representation: "HTTP mock handler with a canned response fixture"
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
  - "live record-lookup smoke test"
  - "pre-release checklist"
release_impact: "blocking before first production release unless Dave explicitly accepts risk"
```

## Boundary types

This list names the representation mechanisms that stand in for production; the
boundary-sensitive areas in the testing and verification context set name where
a claim is easy to overstate. The two lists are complementary cuts, not
competing taxonomies.

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
- a headless DOM replacing a real browser
- local development config replacing production config
- local environment variables replacing deployed secrets/config

## Release impact labels

Every verification claim carries one of the evidence classes defined in the
lexicon. Every material boundary gap additionally carries one of the
release-impact labels — `blocking`, `deferred`, `accepted-risk`,
`not-material` — which are defined in the lexicon.

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

- the project TRD's standing verification boundary section, for durable
  cross-cutting boundaries
- a feature-specific verification ledger
- inline test comments for small/local boundaries
- a change package
- a release-readiness review
- a pre-release checklist

Durable or repeated boundaries are declared in the project TRD's standing
verification boundary section, or in a dedicated project verification ledger
where the project keeps one.

## CI and automation expectations

Fast unit tests should remain fast and deterministic.

Live/browser checks should normally be separate from the default unit suite. They may run:

- manually before release
- in a dedicated CI job
- on a schedule
- after deploy as synthetic monitoring

Choose among these by the risk of the boundary, not by a fixed schedule. A
boundary material to user-visible behavior or release risk is verified before
release; one that can drift after deployment is verified by production
monitoring.

## Reviewer obligations

Apply the obligation for the role you are filling:

- **Spec Reviewer** — check that declared durable boundaries are consistent with
  the TRD's standing verification boundary section, and flag drift as a
  continuity finding.
- **Reviewer** — check whether boundaries are named and documented.
- **Skeptic/Risk** — challenge overbroad confidence claims.
- **Release Manager** — ensure material boundary gaps are resolved, deferred, or
  accepted before release.

## Release requirement

Before release, all material verification boundaries must be in one of these
states, which are the discharge conditions for the release-impact labels above:

1. verified by an appropriate mechanism
2. explicitly deferred with a named path
3. explicitly accepted as a known risk by Dave
4. explicitly marked not material to the release

Implicit unknowns are not acceptable.
