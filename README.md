# AI Operating Model

Status: draft
Tree version: v0.4 — see `MANIFEST.md` for the changelog. Per-document `Status`
lines carry a maturity word (`draft` / `in-review` / `stable`), not a version
number; the tree version is the single source for what's current.

This directory is the source of truth for how this project is built with AI agents.

The core model is:

> Dave acts as PM, EM, owner, and operator. LLMs and LLM agents act as the implementation team. *Human* code review is not the default control surface — code review is performed by agents (the Reviewer and Skeptic/Risk roles), and its output is evidence. The system must produce enough specification, verification, review, and operational evidence to support responsible release decisions.

## Document map

### Core

- `operating-model.md` describes the overall working model.
- `specs/` contains the canonical PRD and TRD templates (product and technical specs).
- `context-sets/` contains reusable portable context.
- `policies/` contains durable rules.
- `roles/` defines agent roles.
- `skills/` defines repeatable procedures.
- `boundaries/` defines known confidence and responsibility boundaries.

### Adapters

The portable documents in `/ai/` are authoritative.

Tool-specific files such as `CLAUDE.md`, `AGENTS.md`, `.claude/agents/`, and `.claude/skills/` are adapters. They may summarize or import these documents, but they should not become the only home for an operating principle.

## Key principles

1. Manage the proof, not the code.
2. Agent claims require evidence.
3. Green tests do not imply shippability beyond the verified boundary.
4. Every mocked boundary must declare what it verifies, what it does not verify, and where deferred verification happens.
5. The primary human control surface is the spec, the tests, and (increasingly) production observability — not *human* code review. Code review is still required in most flows, but it is agentic (the Reviewer and Skeptic/Risk roles), and its output is evidence feeding the recommendations humans decide on. Gating delivery on a human grokking unfamiliar code at machine speed doesn't scale; compressing the code-writing step is the primary value.
6. Production-grade means operable, observable, recoverable, and verified to stated boundaries.
7. Vendor-specific agent systems are implementation details, not the source of truth.
8. Specs are canonical (PRD → TRD → ACs → architecture summary → Issues); Issues are derived, and spec/Issue conflicts are a hard stop.
9. Work is spec-first and test-driven: specs are reviewed by the Spec Reviewer Agent (hard gate) and agreed by Dave before work begins; tests are confirmed failing before implementation; the agent that writes a unit's tests is not the agent that implements it; the Architect that drafts a spec is not the agent that reviews it.
10. The human gate is the **release decision** — an evidence-and-judgment call, not a code decision (see #5): for a release, a human reviews the test and agent-review artifacts and decides go/no-go. Routine releases flow on evidence; a defined consequential class requires the human go/no-go. Where the release event sits relative to commit and deploy is a per-project TRD concern.

## How to use this directory

Before starting a meaningful change, agents should read:

1. `operating-model.md`
2. the canonical specs under `specs/` (PRD, then TRD)
3. relevant files under `context-sets/`
4. relevant policy files
5. the role document for the role they are filling, including `roles/spec-reviewer-agent.md` for any chat involving spec authorship or review, and `roles/orchestrator-agent.md` for any chat involving decomposing a spec into work packages
6. any skill document for the procedure they are executing

Before release, agents should produce a change package that includes:

- specification or intent
- implementation summary
- test evidence
- verification boundary updates
- review evidence
- known gaps
- release recommendation
