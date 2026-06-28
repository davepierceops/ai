---
context-set: ai-native-engineering
purpose: Roles, separation of concerns, and the AI-native team model.
include-when: Any multi-role or implementation chat.
depends-on: [base]
---

# Context Set: AI-Native Engineering

Status: draft

## Summary

AI-native engineering means treating LLMs and LLM agents as the primary implementation staff while preserving engineering discipline through explicit controls.

The goal is not to make the human read all code. The goal is to make the system produce enough artifacts to support responsible decisions.

## Core premise

> Agents are useful but structurally untrustworthy.

This does not mean agents are bad. It means their claims must be checked by evidence, independent review, reproducible commands, or live verification.

## Team model

The project may use these roles:

- PM/EM/Owner
- Orchestrator Agent
- Architect Agent
- Spec Reviewer Agent
- Test Designer Agent
- Coder Agent
- Reviewer Agent
- Skeptic/Risk Agent
- Release Manager Agent

The same underlying model may fill multiple roles across a project, but the role
boundaries must remain explicit, and two separations are mandatory rather than
optional:

- The agent that writes the tests for a unit of work does not implement that
  unit (Test Designer / Coder separation).
- Whoever produces an artifact does not approve it (the review boundary).
- The Architect Agent that drafts a spec does not act as the Spec Reviewer that
  certifies it (spec authorship / spec review separation).

## Separation of concerns

- The Orchestrator Agent decomposes an agreed spec into ordered change packages
  and drafts the Claude Code prompt for each one; it operates in chat, not inside
  a Claude Code session, and Dave approves the decomposition before any agentic
  work begins.
- The Coder Agent creates implementation.
- The Test Designer Agent defines how correctness will be evaluated.
- The Spec Reviewer Agent gates spec quality before Dave agrees a spec, and
  runs continuity scans to catch cross-document drift.
- The Reviewer Agent checks maintainability, correctness, and consistency.
- The Skeptic/Risk Agent looks for false confidence and hidden assumptions.
- The Release Manager Agent assesses whether evidence is sufficient to ship.

## Required discipline

Each nontrivial change should answer:

1. What was intended?
2. What changed?
3. How was it tested?
4. What does the test evidence actually prove?
5. What remains unverified?
6. What risks remain?
7. What should Dave inspect?
8. Is this ready to ship?

## Anti-patterns

Avoid:

- agent says it works
- tests are green, therefore ship
- mocks imply live behavior
- review summarizes only what changed, not what could be wrong
- undocumented assumptions
- hidden vendor/tool dependencies
- policy living only in Claude, Codex, ChatGPT, or another tool-specific surface
