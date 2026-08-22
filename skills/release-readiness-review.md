---
status: draft
last-reviewed: null
audience: [release-manager-agent, skeptic-risk-agent, human]
---

# Skill: Release Readiness Review

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

The Release Manager's role document states what the release package contains.
This is how it is assembled.

1. Take each item the release package requires and find its source in the
   change package. Where the change package states it, carry it across
   unchanged; do not rewrite it.
2. For the two items the change package does not carry — user-visible behavior,
   and the rollback or mitigation path — derive them from the change and state
   where each came from.
3. Where a required item has no source at all, say so rather than filling the
   slot; a missing item is a known gap.
4. Confirm the `human-gate` tracker issue is open and linked if the change is
   consequential; flag if absent.

## Output

The assembled package, plus the evidence behind the recommendation.
