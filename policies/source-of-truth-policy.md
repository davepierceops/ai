# Policy: Source of Truth

Status: draft

## Purpose

This policy fixes what is canonical and what is derived, so that disagreements
between artifacts are resolved by authority rather than by guessing.

## Canonical order

1. **PRD** (`specs/prd-template.md`) — product intent. Canonical for *what* and
   *why*.
2. **TRD** (`specs/trd-template.md`) — technical design. Canonical for *how*.
3. **Acceptance criteria** — derived from the PRD, owned by Dave.
4. **Architecture summary** (per change) — derived from the TRD, produced by the
   Architect Agent. This is the artifact a GitHub Issue is cut from.
5. **GitHub Issues** — **derived PM artifacts**. They track and organize work.
   An Issue is a *view onto the specs*, not an independent source of truth.

The `/ai/` operating-model documents (context-sets, policies, roles, skills,
boundaries) are canonical for *how the project is run*. Vendor-specific files
(`CLAUDE.md`, `AGENTS.md`, `.claude/`) are adapters, never the sole home of a
durable rule (see `boundaries/vendor-tooling-boundary.md`).

## Conflicts are a hard stop

If a derived artifact disagrees with a canonical one — an Issue that contradicts
the spec, an architecture summary that contradicts the TRD, an adapter that
contradicts a policy — this is **not** resolved by guessing or by preferring the
more recent artifact.

It is a hard stop. The agent must:

1. Stop work on the conflicted item.
2. Surface the conflict to Dave explicitly in the current response: name both
   artifacts, quote or describe the contradicting content, and state clearly
   that this is a hard stop requiring resolution before work continues.
3. Wait for Dave to resolve it.

Do not silently reconcile. Do not pick the version that is easier to implement.

## Keeping derived artifacts honest

When a canonical document changes, derived artifacts downstream of it may go
stale. The agent making the change is responsible for flagging which derived
artifacts now need updating, per the document-consistency principle in
`context-sets/spec-and-change-discipline.md`.

## Proactive drift detection

The Spec Reviewer Agent is the designated mechanism for proactively catching
drift between canonical and derived artifacts before it reaches a hard stop.
Continuity scans run automatically on every spec revision (Depth 1) and on
demand at greater scope (Depth 2, Depth 3). See `roles/spec-reviewer-agent.md`.
