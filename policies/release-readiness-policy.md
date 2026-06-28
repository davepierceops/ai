# Policy: Release Readiness

Status: draft

## Purpose

This policy defines what evidence is required before shipping a meaningful change.

## Core rule

A release decision must be based on explicit evidence, known gaps, and accepted risk.

## Release package

Before release, the Release Manager Agent should produce a release package containing:

1. Change summary
2. User-visible behavior
3. Test evidence
4. Verification boundary status
5. SLO status and error budget consumption for any affected Top K user journeys
6. Live/browser verification status, if relevant
7. Operational risks
8. Rollback or mitigation path
9. Known gaps
10. Recommendation

For consequential changes, a `human-gate` GitHub issue must also be open and
linked in the release package before Dave's go/no-go is sought. See
`policies/commit-and-change-control-policy.md`.

## Required checks

The required checks depend on risk, but common checks include:

- unit tests
- component tests
- integration tests
- lint/type checks
- contract checks
- live smoke tests
- browser smoke tests
- PWA/service worker checks
- accessibility spot checks
- monitoring or synthetic check updates

## Known gaps

Known gaps must be stated explicitly.

Each gap should have one of these statuses:

- must fix before release
- acceptable for release
- deferred with follow-up
- requires Dave decision

## Ship/no-ship recommendation

The Release Manager Agent should give one of:

- ship
- ship with accepted risks
- do not ship
- needs Dave decision

The recommendation must be supported by evidence.

## Dave's role

Dave makes the release decision.

Dave may accept risk, but risk should not be hidden or implied.
