# Skill: Boundary Audit

Status: draft

## Purpose

Identify where the system's tests, mocks, tools, or assumptions stop proving production behavior.

## Use when

- adding or changing a mock
- adding or changing an external integration
- changing auth/config/deployment behavior
- reviewing a green test suite before release
- investigating a surprise production/manual failure
- verifying that SLO targets defined in the TRD have a production monitoring
  mechanism in place

## Inputs

- change summary
- test plan
- relevant tests/mocks
- external dependencies
- release context

## Procedure

1. List all affected production behaviors.
2. Identify which behaviors are tested locally.
3. Identify which tests use mocks, fixtures, jsdom, fakes, or generated data.
4. For each boundary, state what is verified.
5. For each boundary, state what is not verified.
6. Assign a deferred verification path.
7. Mark unresolved gaps as accepted risk, deferred, or blocking.

## Output

Produce a boundary audit with:

- boundary name
- production surface
- verification class
- verified claims
- unverified claims
- deferred verification path
- release impact
- SLO status: whether each affected Top K journey has a production monitoring
  mechanism in place and current error budget state, if known
