# Directive — Chief of Staff Supersession Package

Date: 2026-08-02
Source: chat review session finalizing `roles/chief-of-staff.md`. The revised
document text was produced and approved in that session and is committed
alongside this directive.
Executor: Claude Code, fresh session, local clone of `davepierceops/ai`.

Effects the Orchestrator → Chief of Staff replacement (Q3c) across the live
doc set, and advances `roles/chief-of-staff.md` through review to `agreed`.

## Preconditions (hard — stop and report if any fail)

1. `git pull` — working tree clean, `main` in sync with `origin/main`.
2. `policies/document-metadata-policy.md` is `agreed` at current main (the
   cycle-9 flip, PR #10, is landed).
3. All execution on a branch; land via PR. No direct-to-main.
4. `bin/check-frontmatter --all` passes before the PR is opened.
5. Any status flip runs through `bin/flip-agreed` (SHA-in-log precondition
   applies).

## Decisions this directive executes (agreed in chat; do not relitigate)

- D1. Orchestrator disposition: supersede-and-fold. `roles/chief-of-staff.md`
  carries the decomposition/handoff responsibility, redesigned.
- D2. Q1b: `cos` is NOT the agent-runner term — ruled out (role ≠ runner).
  "Agent-runner" remains the term; it is in live use and works. Question
  closed, no open item.
- D3. "Tranche" is the term for a scope of agreed spec proposed for
  implementation as one body of work. Proposed by cos, approved by Dave.
- D4. Durable decomposition artifact: `docs/packages/<tranche>-decomposition.md`,
  one per tranche. Applies FORWARD only — do not backfill decomposition docs
  for packages A–D.
- D5. Prompts are generated at execution time from the decomposition doc into
  `.prompts/<tranche>-<package>.md` — gitignored, regenerable, never
  committed.

## Work items, in order

### W1 — Verify revised `roles/chief-of-staff.md`

The revised body was committed to `roles/chief-of-staff.md` in the same
commit as this directive; status remains `draft`. Verify it is present at
current main (header reads "Supersedes the Orchestrator Agent (Q3c)"). No
edit in this step.

### W2 — Supersede the orchestrator role

`roles/orchestrator-agent.md`: frontmatter only — `status: superseded`, add
`superseded-by: roles/chief-of-staff.md`. Body frozen; verify diff-clean
outside frontmatter via `git diff`.

### W3 — Audience swaps (11 files)

Replace `orchestrator-agent` with `chief-of-staff` in the `audience`
frontmatter of:
`roles/architect-agent.md`, `roles/coder-agent.md`,
`roles/context-quality-reviewer.md`, `roles/pm-em-owner.md`,
`roles/release-manager-agent.md`, `roles/reviewer-agent.md`,
`roles/skeptic-risk-agent.md`, `roles/spec-reviewer-agent.md`,
`roles/test-designer-agent.md`, `skills/change-package-creation.md`,
`skills/spec-review-cycle.md`.
Frontmatter-only changes; verify no body edits.

### W4 — README repoint

`README.md` line ~61: role-loading guidance names
`roles/orchestrator-agent.md` for decomposition chats — repoint to
`roles/chief-of-staff.md`.

### W5 — Context-set update

`context-sets/ai-native-engineering.md`: rename the Orchestrator role entry
(~line 30) and description (~line 51) to Chief of Staff, and add the tranche
definition (D3) to the decomposition vocabulary so the term does not live
only in the role doc.

### W6 — OPEN-ITEMS updates

- Line ~97: live what's-needed entry points at a line to add in
  `roles/orchestrator-agent.md` — repoint to `roles/chief-of-staff.md`.
- Do NOT touch lines 104–128 (historical source attributions) or any struck
  entries.

### W7 — .gitignore

Add `.prompts/` with a rationale comment in the style of the existing
`.cycle-bundles/` entry (regenerable outputs; a committed copy drifts).

### W8 — Gate review: `roles/chief-of-staff.md` draft → agreed

Run the spec-review cycle on the revised doc per `skills/spec-review-cycle.md`:
in-review flip, review with findings, confirmation artifact in `reviews/`,
then `bin/flip-agreed` on Dave's explicit go. Advisory to carry into review:

- Portability: the read-sequence and `bin/state` reference `OPEN-ITEMS.md`,
  `BACKLOG-v2.md`, and `human-gate` issues. `BACKLOG-v2.md` is a
  repo-specific versioned filename. Reviewer to rule whether this doc is
  repo-bound by design or needs convention-name abstraction before agreement.

## Constraints

- Historical records are out of scope: `reviews/`, `docs/packages/`,
  `docs/cycles/`, MANIFEST changelog entries. Do not rewrite history.
- MANIFEST changelog gets one new entry for this package, per convention.
- If any W-item's target text does not match what this directive describes,
  STOP on that item and report — do not improvise around drift.
