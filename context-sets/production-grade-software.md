---
context-set: production-grade-software
purpose: What operable, observable, recoverable software requires.
include-when: Changes affecting reliability, ops, security, or release quality.
depends-on: [base]
---

# Context Set: Production-Grade Software

Status: draft

## Summary

Production-grade software is not merely feature-complete. It is software that can be operated responsibly.

For this project, production-grade means:

> The system is intentionally specified, tested to stated boundaries, observable, recoverable, and understandable enough to operate.

## Production-grade attributes

A production-grade change should consider:

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

A production-grade claim should be supported by evidence such as:

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

Every meaningful change should consider:

1. What happens if this fails?
2. How would we know? Does this failure mode affect a Top K journey SLO, and would it burn error budget?
3. What would the user see?
4. Can the system recover?
5. Can Dave debug or roll back?
6. Is the failure acceptable?

## Production-grade does not mean

Production-grade does not mean:

- perfect
- over-tested
- enterprise-heavy
- no known gaps
- every dependency mocked and live-tested in every run
- every line reviewed by a human

It does mean known gaps are visible and intentionally accepted.
