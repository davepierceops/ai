# Manifest

This file is the assembly record and the single source for "what's current."

Document versioning and metadata are governed by
`policies/document-metadata-policy.md`: the version of a document at
reference time is the SHA of the last commit touching it; there is no
repo-wide version number and no per-document version numbers. In-scope
documents carry YAML frontmatter (`status`, `last-reviewed`, `audience`).
Instantiated project PRDs/TRDs live in project repos and adopt the same
schema, with enforcement stood up as part of project setup.

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
- `context-sets/collab-workflow.md`
- `policies/testing-policy.md`
- `policies/verification-boundary-policy.md`
- `policies/agent-review-policy.md`
- `policies/release-readiness-policy.md`
- `policies/source-of-truth-policy.md`
- `policies/commit-and-change-control-policy.md`
- `policies/document-metadata-policy.md`
- `roles/pm-em-owner.md`
- `roles/architect-agent.md`
- `roles/test-designer-agent.md`
- `roles/coder-agent.md`
- `roles/reviewer-agent.md`
- `roles/skeptic-risk-agent.md`
- `roles/release-manager-agent.md`
- `roles/orchestrator-agent.md`
- `roles/context-quality-reviewer.md`
- `roles/spec-reviewer-agent.md`
- `skills/boundary-audit.md`
- `skills/evidence-review.md`
- `skills/release-readiness-review.md`
- `skills/change-package-creation.md`
- `skills/test-plan-review.md`
- `skills/spec-review-cycle.md`
- `skills/conversation-retro.md`
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

## v0.5 changes

- Added `skills/spec-review-cycle.md`: reviewer-gated spec review cycles run
  chat-for-triage, Claude Code-for-execution. Cycle directives (with reviewed
  commit SHAs) are the handoff artifact; full documents never round-trip
  through chat.
- Linked the skill from `operating-model.md` change-flow step 1 and from
  `context-sets/collab-workflow.md` (mode distinction).
- Retroactive registration of files predating this commit and missing from
  this manifest: `roles/orchestrator-agent.md`, `roles/context-quality-reviewer.md`,
  `roles/spec-reviewer-agent.md`, `context-sets/collab-workflow.md`.
- Regenerated `TREE.txt` (was stale: pre-flattening paths, missing newer files).

## Post-v0.5 changes (SHA-versioned per document-metadata-policy)

- Added `policies/document-metadata-policy.md`: YAML frontmatter schema,
  git-SHA versioning, revision lifecycle, and agent build-gating rules.
  Removed the repo-wide `Tree version` declaration from this file — the
  version headings above are historical record, not a live convention.
- Added `skills/conversation-retro.md` (draft): per-conversation
  retrospective skill. Retros are per-project tracker-class artifacts
  (`retros/` in project repos, no lifecycle frontmatter); methodology
  changes they surface enter via spec-review cycles only.

## Context-set bundles

Paste only the sets a chat needs. `base` is always included.

- **Spec chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering`
- **Implementation chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering` + `testing-and-verification`
- **Release / risk chat:** `base` + `testing-and-verification` + `production-grade-software`
- **Everything:** all context-sets.
