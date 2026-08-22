---
status: draft
last-reviewed: null
audience: [all-roles, human]
order: 6
depends-on: []
---

# Context Set: Production-Grade Software

Rules for execution sessions. What operable, observable, recoverable software
requires.

## Production-grade attributes

A production-grade change is assessed against:

- correctness
- usability
- performance
- accessibility
- security
- privacy
- reliability
- SLO compliance and error budget health
- operability
- observability
- recoverability
- maintainability
- cost and quota exposure
- dependency risk
- failure modes

Not every change requires deep treatment of every attribute. The agent must explicitly decide which attributes are relevant.

## Evidence requirements

A production-grade claim is supported by evidence such as:

- passing unit tests
- passing integration tests
- live smoke tests
- browser smoke tests
- contract checks
- static analysis
- lint/type checks
- manual verification checklist
- screenshots or traces where appropriate
- telemetry/monitoring plan
- rollback or mitigation plan

## Failure mode thinking

Every meaningful change answers:

1. What happens if this fails?
2. How would we know? Does this failure mode affect a Top K journey SLO, and would it burn error budget?
3. What would the user see?
4. Can the system recover?
5. Can Dave debug or roll back?
6. Is the failure acceptable?
