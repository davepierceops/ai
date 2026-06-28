# Manifest

Tree version: v0.4
Status: draft

This file is the assembly record and the single source for "what's current."
Individual documents carry a maturity word on their `Status` line
(`draft` / `in-review` / `stable` / `placeholder`), not a version number — the
tree version above is the only version. Project artifacts produced *by* this
model (a project's own PRD/TRD) version independently and are not covered by
this convention.

Generated initial document set.

## Source-of-truth files

- `ai/README.md`
- `ai/operating-model.md`
- `ai/specs/prd-template.md`
- `ai/specs/trd-template.md`
- `ai/context-sets/base.md`
- `ai/context-sets/ai-native-engineering.md`
- `ai/context-sets/production-grade-software.md`
- `ai/context-sets/testing-and-verification.md`
- `ai/context-sets/spec-and-change-discipline.md`
- `ai/policies/testing-policy.md`
- `ai/policies/verification-boundary-policy.md`
- `ai/policies/agent-review-policy.md`
- `ai/policies/release-readiness-policy.md`
- `ai/policies/source-of-truth-policy.md`
- `ai/policies/commit-and-change-control-policy.md`
- `ai/roles/pm-em-owner.md`
- `ai/roles/architect-agent.md`
- `ai/roles/test-designer-agent.md`
- `ai/roles/coder-agent.md`
- `ai/roles/reviewer-agent.md`
- `ai/roles/skeptic-risk-agent.md`
- `ai/roles/release-manager-agent.md`
- `ai/skills/boundary-audit.md`
- `ai/skills/evidence-review.md`
- `ai/skills/release-readiness-review.md`
- `ai/skills/change-package-creation.md`
- `ai/skills/test-plan-review.md`
- `ai/boundaries/mocked-boundaries.md`
- `ai/boundaries/live-integration-boundaries.md`
- `ai/boundaries/human-review-boundary.md`
- `ai/boundaries/vendor-tooling-boundary.md`

## Adapter files

- `CLAUDE.md`
- `AGENTS.md`
- `.claude/agents/README.md`
- `.claude/skills/README.md`

## v0.2 changes

- Revised `ai/operating-model.md` for stronger trust model, standard change flow, definition of done, and escalation rules.
- Revised `ai/context-sets/base.md` for sharper agent behavior, response shape, mock rule, and tooling rule.

## v0.3 changes

- Revised `ai/context-sets/testing-and-verification.md` to define verification classes, confidence ledgers, test-plan requirements, and anti-patterns.
- Revised `ai/policies/verification-boundary-policy.md` with boundary declaration schema, status labels, triggers, and release impact labels.
- Revised `ai/roles/skeptic-risk-agent.md` into an operational review role with checklists, severity categories, and output template.

## v0.4 changes (methodology merge)

Merged the spec-first / test-driven methodology spine into this operating model.

- Added `ai/specs/` with PRD and TRD templates. The TRD is the standing technical spec; the per-change architecture summary (Architect) sits between the TRD and Issues.
- Added `ai/policies/source-of-truth-policy.md`: PRD → TRD → ACs → architecture summary → Issues; Issues are derived; conflicts are a hard stop.
- Added `ai/policies/commit-and-change-control-policy.md`: two-tier release gate (routine flows to release on evidence; consequential requires explicit human go/no-go at the release decision) plus the red-gate and Test Designer/Coder separation.
- Added `ai/context-sets/spec-and-change-discipline.md`: canonical sequence, red-gate, and operating habits (one question at a time, document consistency, loose-end tracking).
- Imposed Test Designer / Coder separation in `roles/test-designer-agent.md`, `roles/coder-agent.md`, and `context-sets/ai-native-engineering.md`.
- Gave the Architect role TRD authorship and the per-change architecture summary in `roles/architect-agent.md`.
- Revised `ai/operating-model.md`: spec-first summary, source-of-truth section, spec-first change flow with role mapping, release gate, and red-then-green definition of done.
- Added composition front-matter (`include-when`, `depends-on`) to all context-sets and the bundles below.

## Context-set bundles

Paste only the sets a chat needs. `base` is always included.

- **Spec chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering`
- **Implementation chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering` + `testing-and-verification`
- **Release / risk chat:** `base` + `testing-and-verification` + `production-grade-software`
- **Everything:** all context-sets.
