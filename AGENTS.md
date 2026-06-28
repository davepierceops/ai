# Agent Instructions

This file provides generic instructions for AI coding agents.

The authoritative operating model lives in `/ai/`.

## Core model

Dave is PM, EM, owner, and operator. LLM agents perform implementation, review, and release-preparation work. Dave does not default to human line-by-line code review.

## Agent requirements

For meaningful changes:

1. Read `ai/README.md`, `ai/operating-model.md`, and the canonical specs under `ai/specs/`.
2. Identify the role you are filling. Role documents live under `ai/roles/`,
   including the Spec Reviewer Agent (`ai/roles/spec-reviewer-agent.md`) for
   spec authorship and review contexts.
3. Work spec-first: specs and ACs before tests; confirm tests fail before implementing; keep test authorship and implementation in separate agents.
4. Follow relevant policies under `ai/policies/`, including the source-of-truth and commit/change-control policies.
5. Use relevant skills under `ai/skills/`.
6. Update boundary docs when mocks, integrations, or verification assumptions change.
7. Produce evidence for claims.
8. Get the human's go/no-go at the release decision for consequential changes;
   open a `human-gate` GitHub issue and state it explicitly in the current
   response. Routine changes flow to release on evidence.
9. Do not treat green tests as broader proof than the tested boundary supports.
10. For document authorship or review contexts, follow
    `ai/context-sets/collab-workflow.md`.

## Required change summary

At handoff, include:

- what changed
- why it changed
- tests run
- what the tests prove
- what remains unverified
- known risks
- recommended next step

## Core rule

Agent claims require evidence.
