# Boundary: Vendor Tooling

Status: draft

## Summary

This project may use vendor-specific AI tooling such as Claude Code, Codex, ChatGPT, agent frameworks, skills, hooks, memory files, or IDE integrations.

These tools are execution backends, not the source of truth.

## Policy

No durable operating principle should live only inside a vendor-specific tool.

The portable `/ai/` documents are authoritative. Vendor-specific files are adapters.

## Examples

- `CLAUDE.md` may summarize or import portable context.
- `.claude/agents/` may adapt role documents for Claude subagents.
- `.claude/skills/` may adapt skill documents for Claude skills.
- `AGENTS.md` may provide generic agent instructions.
- Codex prompts or tasks may reference `/ai/` docs.

## Risks

Vendor-specific tooling can create:

- lock-in
- hidden policy drift
- stale duplicated instructions
- inconsistent agent behavior across tools
- difficult migration to other models
- unclear source of truth

## Required discipline

When creating vendor-specific artifacts:

1. Identify the portable source document.
2. Keep the adapter short where possible.
3. Do not add new durable policy only in the adapter.
4. Update the portable source first.
5. Note intentional deviations.

## Core principle

Context Sets are the constitution. Vendor artifacts are deployment targets.
