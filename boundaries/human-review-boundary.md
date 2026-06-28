# Boundary: Human Review

Status: draft

## Summary

This project intentionally does not use *human* line-by-line code review as the
default quality control.

This is a boundary, not an absence of review. Code review still happens — it is
performed by agents (the Reviewer and Skeptic/Risk roles), and its output is
evidence that feeds the recommendations humans decide on. What this boundary
removes is *human* diff-reading as the default, not review itself.

## Policy

Because Dave is not defaulting to human code review, the system must produce stronger process evidence.

## Human review includes

Dave may review:

- product intent
- acceptance criteria
- specs (PRD and TRD) — agreed by Dave after Spec Reviewer sign-off
- change packages
- test plans
- verification boundaries
- review summaries
- release recommendations
- known gaps
- operational evidence
- selected diffs when risk justifies it

## Human review does not default to

- reading every changed line
- checking every implementation detail
- manually reproducing every test
- acting as the only reviewer

## Required replacement controls

When human code review is not used, the change must rely on:

- spec-first work
- spec review (Spec Reviewer Agent gate before Dave agrees any spec)
- tests
- independent agent review
- skeptic/risk review
- verification boundary documentation
- release readiness review
- reproducible evidence

## Escalation to human code review (exception path)

This is the exception path to the control-surface boundary above: the rare case
where a human *chooses to read code directly*. It is a separate axis from the
release gate — the release go/no-go is an evidence-and-judgment decision, not a
code-reading decision (see `policies/commit-and-change-control-policy.md`). A
change can be in the consequential class (needs a human release go/no-go) without
anyone reading its diff, and vice versa.

A human may choose to inspect code directly when:

- the change is security-sensitive
- the system handles private data
- release risk is high
- agents disagree
- evidence is weak
- behavior is surprising
- the change affects core architecture
- production impact would be hard to reverse

## Core principle

Human attention should be spent on judgment, not on pretending to be a compiler.
