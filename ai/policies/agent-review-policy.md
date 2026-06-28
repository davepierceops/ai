# Policy: Agent Review

Status: draft

## Purpose

This policy defines how agent-produced work is reviewed when Dave is not defaulting to human line-by-line code review.

## Core rule

Agent review must evaluate the evidence package, not merely summarize the implementation.

## Required review posture

Reviewers should assume:

- implementation may be plausible but wrong
- tests may pass while proving less than claimed
- mocks may hide important production failures
- the agent that wrote the code may have optimized for green tests
- hidden assumptions are likely

## Review roles

### Spec Reviewer Agent

Focuses on:

- spec completeness — all required sections present and substantively answered
- internal consistency — no section contradicts another within a document
- cross-document consistency — specs consistent with policies, boundaries, and
  role docs
- traceability — ACs trace to user journeys; TRD NFRs instantiate PRD NFRs;
  SLOs defined per Top K journey
- continuity scan findings — flags drift for Dave's resolution

### Reviewer Agent

The Reviewer Agent is a **hard gate**. A meaningful change does not proceed to
Skeptic/Risk review or release without a Reviewer Agent sign-off.

Focuses on:

- correctness
- maintainability
- consistency with project conventions
- test adequacy
- clarity
- unnecessary complexity

### Skeptic/Risk Agent

Focuses on:

- false confidence
- missing live verification
- security and privacy risk
- operational failure modes
- SLO breach risk and error budget state
- deployment/configuration gaps
- unclear ownership
- untested assumptions

### Release Manager Agent

Focuses on:

- readiness evidence
- known gaps
- rollback/mitigation
- whether the change should ship

## Required review output

An agent review should include:

1. Scope reviewed
2. Evidence inspected
3. Findings
4. Risks
5. Verification gaps
6. Required follow-ups
7. Recommendation

## Prohibited review patterns

Do not submit reviews that only say:

- looks good
- tests pass
- implementation matches spec
- no issues found

A useful review must state what was checked and what was not checked.

## Dave-facing summary

Because Dave is reviewing process and evidence, reviews should include a concise section:

> What Dave should inspect

This should identify the most decision-relevant artifacts, not every file changed.
