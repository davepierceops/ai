# Cycle 2 Directive — policies/document-metadata-policy.md

Date: 2026-07-21
Documents in scope:
- `policies/document-metadata-policy.md` @ `d5e7b2c` (main)
- Agreement change package: branch `metadata-policy-agreement` @ `0230e11`
  (`MANIFEST.md`, `specs/prd-template.md`, `specs/trd-template.md`)

Review artifact: `reviews/document-metadata-policy-cycle-2.md`
Prior cycle directive: `docs/cycles/cycle-1-directive.md` (committed
retroactively per B4 below)

## Decisions

### B1 — accept
Finding: Root-level governing documents fall in neither scope set.
Resolution: Add `operating-model.md` and `README.md` to the in-scope set
as explicit paths alongside the six directory globs. Extend the
out-of-scope enumeration to name `BACKLOG-v2.md` and `MERGE-NOTES-v0.4.md`
explicitly as trackers/history, alongside the existing exclusions.

### B2 — accept
Finding: The grandfather clause has no applicability criterion.
Resolution: The applicability criterion is a per-document disposition
list, recorded in this directive (below). Amend the grandfather clause to
reference the committed cycle directive as the canonical record of which
documents enter migration as `agreed`. The disposition list supersedes
the unchecked sign-off boxes in `REVIEW-v0.4.md` as the record of what
was agreed at v0.4; `REVIEW-v0.4.md` itself is historical and is not
edited.

#### Migration disposition list

Enter migration as `agreed` (grandfathered, `last-reviewed: null`) —
reviewed and resolved in the v0.4 spine review:

- `operating-model.md`
- `README.md`
- `specs/prd-template.md`
- `specs/trd-template.md`
- `policies/agent-review-policy.md`
- `policies/commit-and-change-control-policy.md`
- `policies/release-readiness-policy.md`
- `policies/source-of-truth-policy.md`
- `policies/testing-policy.md`
- `policies/verification-boundary-policy.md`
- `context-sets/ai-native-engineering.md`
- `context-sets/base.md`
- `context-sets/production-grade-software.md`
- `context-sets/spec-and-change-discipline.md`
- `context-sets/testing-and-verification.md`
- `roles/architect-agent.md`
- `roles/coder-agent.md`
- `roles/pm-em-owner.md`
- `roles/release-manager-agent.md`
- `roles/reviewer-agent.md`
- `roles/skeptic-risk-agent.md`
- `roles/test-designer-agent.md`
- `boundaries/human-review-boundary.md`
- `boundaries/live-integration-boundaries.md`
- `boundaries/mocked-boundaries.md`
- `boundaries/vendor-tooling-boundary.md`
- `skills/boundary-audit.md`
- `skills/change-package-creation.md`
- `skills/evidence-review.md`
- `skills/release-readiness-review.md`
- `skills/test-plan-review.md`

Enter migration as `draft` — created after the v0.4 review, never gated:

- `roles/context-quality-reviewer.md`
- `roles/orchestrator-agent.md`
- `roles/spec-reviewer-agent.md`
- `skills/spec-review-cycle.md`
- `context-sets/collab-workflow.md`

These five are the next gate-review candidates; note that
`skills/spec-review-cycle.md` and `roles/spec-reviewer-agent.md` are the
machinery running this cycle and should be gated early so the
context-loading rule covers them.

In flight — not grandfathered:

- `policies/document-metadata-policy.md` (`in-review`; becomes `agreed`
  at merge of the agreement package via the normal transition)

Out of scope per the policy's Scope section as amended by B1:

- `CLAUDE.md`, `AGENTS.md`, `.claude/**` (adapters)
- `MANIFEST.md`, `OPEN-ITEMS.md`, `COLLAB-STATE.md`, `TREE.txt`,
  `BACKLOG-v2.md` (trackers)
- `MERGE-NOTES-v0.4.md`, `REVIEW-NOTES-v0.2.md`, `REVIEW-NOTES-v0.3.md`,
  `REVIEW-v0.4.md`, `reviews/**`, `docs/cycles/**` (history / review
  artifacts / decision records)

### B3 — accept (folding in A6)
Finding: The revision-lifecycle rule makes supersession of an agreed
document impossible; the agreement flip commit's auditability is
unstated.
Resolution: Add a clause to the Revision lifecycle section: transitions
to `superseded` / `deprecated`, and the agreement flip itself, are
**status transitions**, not revisions, and are exempt from the
edit-flips-in-review rule; content edits alone trigger it. State the
companion constraint: a status-transition commit contains nothing but
the frontmatter transition, so the reviewed-SHA-to-HEAD diff remains
trivially auditable.

### B4 — accept
Finding: Cycle-1 triage decisions have no committed decision record.
Resolution: Commit `docs/cycles/cycle-1-directive.md` (retroactive
reconstruction of the cycle-1 triage, reviewed state `f96a313`, marked
as recorded after the fact) and this directive at
`docs/cycles/cycle-2-directive.md`. Both are the small MCP writes the
skill sanctions; performed from the cycle chat.

### A1 — accept
Finding: The templates the agreement package edits remain non-compliant
with the policy it enacts.
Resolution: On branch `metadata-policy-agreement`, replace the plain
`Status: draft` line in `specs/prd-template.md` and
`specs/trd-template.md` (the template files' own headers, not the
skeletons) with compliant frontmatter: `status: draft`,
`last-reviewed: null`, `audience: [all-roles, human]`. Their `agreed`
status arrives via the normal gate, not the grandfather clause — the
current template revisions have not been re-gated since the v0.4-agreed
content changed on this branch.

### A5 — accept
Finding: Nothing tracks standing up this repo's own enforcement hook.
Resolution: Add one item to `OPEN-ITEMS.md`: build the methodology
repo's frontmatter-enforcement hook over the in-scope set as amended by
B1. May be folded into the existing migration item if that reads
cleaner.

## Deferred / out of scope

- A2 (project-repo `audience` slug validation) — folded into the
  per-project enforcement open item in `OPEN-ITEMS.md`.
- A3 (`last-reviewed` hard-codes `reviews/`) — deferred to project
  setup guidance; relax wording when that guidance is written.
- A4 (`reviews/` unregistered in MANIFEST/TREE) — deferred to the next
  checkpoint: regenerate `TREE.txt` and decide registration of
  `reviews/` and `docs/cycles/` contents then.

## Execution notes

- Policy edits (B1, B2, B3) apply to `policies/document-metadata-policy.md`
  on `main`, based on `d5e7b2c`. Commits reference cycle 2.
- The A1 template edits apply on branch `metadata-policy-agreement`,
  based on `0230e11`.
- The migration itself is **not** executed under this directive — it
  remains the separate open item. The disposition list above is the
  record the migration will follow.
- The policy remains `in-review`; the flip to `agreed` lands at merge of
  the agreement package with `last-reviewed` pointing at the final
  review artifact and SHA, per the staged sequence.
- Re-gate for cycle 3 after edits land.
