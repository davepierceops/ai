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

- `README.md`
- `operating-model.md`
- `specs/prd-template.md`
- `specs/trd-template.md`
- `context-sets/base.md`
- `context-sets/ai-native-engineering.md`
- `context-sets/production-grade-software.md`
- `context-sets/testing-and-verification.md`
- `context-sets/spec-and-change-discipline.md`
- `policies/testing-policy.md`
- `policies/verification-boundary-policy.md`
- `policies/agent-review-policy.md`
- `policies/release-readiness-policy.md`
- `policies/source-of-truth-policy.md`
- `policies/commit-and-change-control-policy.md`
- `roles/pm-em-owner.md`
- `roles/architect-agent.md`
- `roles/test-designer-agent.md`
- `roles/coder-agent.md`
- `roles/reviewer-agent.md`
- `roles/skeptic-risk-agent.md`
- `roles/release-manager-agent.md`
- `skills/boundary-audit.md`
- `skills/evidence-review.md`
- `skills/release-readiness-review.md`
- `skills/change-package-creation.md`
- `skills/test-plan-review.md`
- `boundaries/mocked-boundaries.md`
- `boundaries/live-integration-boundaries.md`
- `boundaries/human-review-boundary.md`
- `boundaries/vendor-tooling-boundary.md`

## Adapter files

- `CLAUDE.md`
- `AGENTS.md`
- `.claude/agents/README.md`
- `.claude/skills/README.md`

## v0.2 changes

- Revised `operating-model.md` for stronger trust model, standard change flow, definition of done, and escalation rules.
- Revised `context-sets/base.md` for sharper agent behavior, response shape, mock rule, and tooling rule.

## v0.3 changes

- Revised `context-sets/testing-and-verification.md` to define verification classes, confidence ledgers, test-plan requirements, and anti-patterns.
- Revised `policies/verification-boundary-policy.md` with boundary declaration schema, status labels, triggers, and release impact labels.
- Revised `roles/skeptic-risk-agent.md` into an operational review role with checklists, severity categories, and output template.

## v0.4 changes (methodology merge)

Merged the spec-first / test-driven methodology spine into this operating model.

- Added `specs/` with PRD and TRD templates. The TRD is the standing technical spec; the per-change architecture summary (Architect) sits between the TRD and Issues.
- Added `policies/source-of-truth-policy.md`: PRD → TRD → ACs → architecture summary → Issues; Issues are derived; conflicts are a hard stop.
- Added `policies/commit-and-change-control-policy.md`: two-tier release gate (routine flows to release on evidence; consequential requires explicit human go/no-go at the release decision) plus the red-gate and Test Designer/Coder separation.
- Added `context-sets/spec-and-change-discipline.md`: canonical sequence, red-gate, and operating habits (one question at a time, document consistency, loose-end tracking).
- Imposed Test Designer / Coder separation in `roles/test-designer-agent.md`, `roles/coder-agent.md`, and `context-sets/ai-native-engineering.md`.
- Gave the Architect role TRD authorship and the per-change architecture summary in `roles/architect-agent.md`.
- Revised `operating-model.md`: spec-first summary, source-of-truth section, spec-first change flow with role mapping, release gate, and red-then-green definition of done.
- Added composition front-matter (`include-when`, `depends-on`) to all context-sets and the bundles below.

## Context-set bundles

Paste only the sets a chat needs. `base` is always included.

- **Spec chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering`
- **Implementation chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering` + `testing-and-verification`
- **Release / risk chat:** `base` + `testing-and-verification` + `production-grade-software`
- **Everything:** all context-sets.
