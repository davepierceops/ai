# Skill: Evidence Review

Status: draft

## Purpose

Evaluate whether the evidence supports the claims made by an agent or change package.

## Use when

- reviewing implementation output
- reviewing test results
- preparing release
- deciding whether Dave needs to inspect more deeply

## Inputs

- spec or intent
- implementation summary
- test evidence
- review notes
- boundary ledger entries
- known gaps

## Procedure

1. List the claims being made.
2. Match each claim to evidence.
3. Identify unsupported claims.
4. Identify overbroad interpretations of test results.
5. Identify missing evidence for material risks.
6. Check whether SLO targets for affected Top K user journeys have production
   monitoring evidence; flag as unsupported if no mechanism exists.
7. Produce a recommendation.

## Output

Produce:

- supported claims
- unsupported or overbroad claims
- missing evidence
- SLO monitoring status for affected Top K user journeys
- risk level
- recommended next step
- what Dave should inspect
