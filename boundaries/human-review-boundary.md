---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Boundary: Human Review

Rules for decision sessions.

## Summary

This is a boundary, not an absence of review. Code review still happens — it is
performed by agents (the Reviewer and Skeptic/Risk roles), and its output is
evidence that feeds the recommendations humans decide on. What this boundary
removes is *human* diff-reading as the default, not review itself.

## Escalation to human code review (exception path)

This is the exception path to the control-surface boundary: the rare case where
a human *chooses to read code directly*. It is a separate axis from the release
gate — the release go/no-go is an evidence-and-judgment decision, not a
code-reading decision. A change can be in the consequential class (needs a human
release go/no-go) without anyone reading its diff, and vice versa.

A human may choose to inspect code directly when:

- the change is security-sensitive
- the system handles private data
- release risk is high
- agents disagree
- evidence is weak
- behavior is surprising
- the change affects core architecture
- production impact would be hard to reverse
