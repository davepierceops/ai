# Skill: Test Plan Review

Status: draft

## Purpose

Evaluate whether a test plan is sufficient for the intended change and risk.

## Use when

- writing tests before implementation
- reviewing a spec-first/TDD plan
- adding external dependencies
- adding browser/PWA behavior
- adding or changing mocks

## Inputs

- spec
- acceptance criteria
- proposed test plan
- affected boundaries
- known risks

## Procedure

1. Map acceptance criteria to tests.
2. Identify untested criteria.
3. Identify mocks and fixtures.
4. Identify live/browser verification needs.
5. Check that the plan includes a red-gate step — tests must be run and
   confirmed failing before the Coder begins; flag if absent.
6. Check whether SLO verification needs are addressed for affected Top K user
   journeys; flag if no production monitoring check is planned.
7. Check negative/failure cases.
8. Identify over-testing or unnecessary complexity.
9. Recommend changes.

## Output

A test-plan review with:

- adequate areas
- gaps
- red-gate coverage (present / absent)
- SLO verification coverage for affected Top K journeys
- unnecessary tests
- boundary concerns
- required live/browser checks
- recommendation
