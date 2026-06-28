# Skill: Change Package Creation

Status: draft

## Purpose

Create a reviewable evidence package for a meaningful change.

## Use when

- a feature is implemented
- a bug is fixed
- a dependency/integration changes
- a release candidate is prepared

## Inputs

- request or issue
- acceptance criteria
- implementation summary
- test results
- review results
- boundary audit
- operational notes

## Procedure

1. State intent.
2. State acceptance criteria.
3. Summarize implementation.
4. Summarize tests and results.
5. Summarize verification boundaries.
6. State SLO status and error budget consumption for any affected Top K user
   journeys.
7. Summarize review findings.
8. State known gaps.
9. State whether a `human-gate` GitHub issue is required and, if so, confirm
   it is open and linked.
10. State release recommendation.

## Output

A change package suitable for Dave to review without reading implementation code line by line.
