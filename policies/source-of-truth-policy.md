---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Source of Truth

This policy governs both session kinds: decision sessions and execution
sessions.

## Purpose

This policy fixes what is canonical and what is derived, so that disagreements
between artifacts are resolved by authority rather than by guessing.

## Canonical order

1. **PRD** — product intent. Canonical for *what* and *why*.
2. **TRD** — technical design. Canonical for *how*.
3. **Acceptance criteria** — derived from the PRD, owned by Dave.
4. **Architecture summary** (per change) — derived from the TRD, produced by the
   Architect Agent. This is the artifact a tracker issue is cut from.
5. **Tracker issues** (currently GitHub Issues) — **derived PM artifacts**. They
   track and organize work. A tracker issue is a *view onto the specs*, not an
   independent source of truth.

The portable operating-model documents (context sets, policies, roles, skills,
boundaries) are canonical for *how the project is run*. Vendor-specific AI
tooling — agent frameworks, skills, hooks, memory files, IDE integrations, and
the instruction files they read — is an adapter, never the sole home of a
durable rule.

## Adapter discipline

No durable operating principle lives only inside a vendor-specific tool. When
creating a vendor-specific artifact:

1. Identify the portable source document.
2. Keep the adapter short where possible.
3. Do not add new durable policy only in the adapter.
4. Update the portable source first.
5. Note intentional deviations.

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
stale. The agent making the change flags which derived artifacts now need
updating.

## Proactive drift detection

The Spec Reviewer Agent is the designated mechanism for proactively catching
drift between canonical and derived artifacts before it reaches a hard stop.
Continuity scans run on every spec revision and at wider scope on demand.
Surface suspected drift when you meet it; do not wait for a scan.
