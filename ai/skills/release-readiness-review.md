# Skill: Release Readiness Review

Status: draft

## Purpose

Determine whether a change is ready to ship.

## Use when

- preparing to merge
- preparing to deploy
- evaluating a completed change package

## Inputs

- change package
- test results
- review evidence
- verification boundary status
- SLO status and error budget consumption for affected Top K user journeys
- operational notes

## Procedure

1. Summarize user-visible change.
2. Summarize test evidence.
3. Summarize verification boundary status.
4. State SLO status and error budget consumption for affected Top K user journeys.
5. Identify live/browser/production checks required.
6. Identify known gaps.
7. Identify rollback or mitigation path.
8. Confirm `human-gate` GitHub issue is open and linked if the change is
   consequential; flag if absent.
9. Give a recommendation.

## Output

Use one of:

- ship
- ship with accepted risks
- do not ship
- needs Dave decision

Include the evidence behind the recommendation.
