# Directive — Doc-Set Review (Permissions/Autonomy Canonicalization)

Date: 2026-08-02
Source: chat triage session; companion decisions file
`docs/cycles/doc-review-2026-08-02-questions.md` (same commit as this file).
Executor: Claude Code, fresh session, local clone of `davepierceops/ai`.

Read the companion questions file in full before starting. It contains the
decisions this directive executes; this file is sequencing and constraints.

## Preconditions (hard — stop and report if any fail)

1. `git pull` — working tree clean, `main` in sync with `origin/main`.
2. Streamlining changes are landed: `bin/` contains the reference-closure and
   flip scripts from Package A, and the frontmatter migration (Package B) is
   visible in git log. If not landed, STOP — this directive sequences after
   the streamlining merge.
3. Standing obligation from the streamlining session: the `flip-agreed`
   SHA-in-log check is a hard precondition on any agreement flip. No flips
   are directed here, but if any step tempts one: don't.

## Work items, in order

### W1 — Bundle regeneration with verification (Q4)

Run the reference-closure script against current `main` entry-points. Diff the
computed closure against the known-good 7-file list (`context-sets/base.md`,
`context-sets/spec-and-change-discipline.md`, `roles/spec-reviewer-agent.md`,
`skills/spec-review-cycle.md`, `boundaries/mocked-boundaries.md`,
`operating-model.md`, `policies/commit-and-change-control-policy.md`).

- Superset of the 7 → adopt; note which files the hand-picked list missed.
- Missing any of the 7 → STOP on this item; report whether it looks like a
  script defect or a genuinely unreferenced load-bearing file. Do not adopt.
- Exact match → adopt; note the hand-picked list is verified closed.

Regenerate `BUNDLE_chat` from the adopted closure, stamped with repo + SHA.

### W2 — Contradiction audit (Q6)

Read `policies/commit-and-change-control-policy.md`,
`context-sets/spec-and-change-discipline.md`, and `operating-model.md`
against the decisions in the questions file — in particular: git push moves
from ask to allow, branch protection becomes the structural gate, agents may
open and merge PRs, and the gating principle "gate only on actual human
judgment."

Report contradictions as findings in the standard gate format
(blocker/advisory). DO NOT edit any `agreed` document. Findings return to
Dave for triage; changes enter through a spec-review cycle. No second door.

### W3 — New draft documents

All land with `status: draft` frontmatter per the metadata policy. Register
each in `MANIFEST.md` per the retroactive-registration convention. Land via
the repo's current change-control path (direct to `main` if permitted; PR if
branch protection requires it).

1. `policies/project-setup-requirements.md` (working name) — the Q1c
   startup-assumptions doc merged with the per-project frontmatter
   enforcement item from `OPEN-ITEMS.md`. Short by design (~20 items = wrong
   approach). Include: branch protection on `main` (no force-push, no
   deletion), frontmatter enforcement, and anything else that must be true at
   adoption. Note the OPEN-ITEMS entry as discharged-when-agreed; do not
   remove it yet.
2. `vendors/claude-code/` — new directory per Q1b. Contents: an
   environment-config doc capturing the canonical `settings.json` posture
   (sandbox enabled, credentials deny for `~/.ssh` and `~/.aws/credentials`,
   network allowlist, strict `allowUnsandboxedCommands: false`, notification
   hook), and a README stating the vendor-directory convention. Minimal —
   flexible/expandable is the requirement, not the final taxonomy.
3. `roles/chief-of-staff.md` — replaces "orchestrator" per Q3. Behavior: on
   invocation, immediately assess state (manual read-sequence for now:
   OPEN-ITEMS → recent commits → pending gates) and propose next steps
   unprompted; minimize Dave's keystrokes; pre-stage work where possible.
   Note the `bin/state` script as planned-not-built. Do not decide the
   Q1b "agent-runner" term question here; flag it in the draft.
4. `skills/directive-dispatch.md` (working name) — the Q2 skill. Three
   requirements per dispatch (route fresh/existing, model per quality/cost —
   hard-coded table acceptable for v1, directive as committed .md with
   path@sha paste block). Propose a directive naming schema in the draft.
   Script (`bin/dispatch`) is deferred; the skill describes manual discipline.
5. Q5 MCP-verification discipline — placement is the executor's judgment call
   (candidate: `vendors/` -adjacent, since it is GitHub-MCP-specific).
   Content: fetch-back before reporting a commit landed; HEAD-read before
   retrying a timed-out write; git log as source of record.

### W4 — Backlog entries

Add three one-line entries to `BACKLOG-v2.md`: `bin/dispatch` (enforce
dispatch discipline), `bin/state` (render current state for chief-of-staff),
role-scoped credentials (fine-grained PATs per role).

### W5 — Report and stop

Report: W1 outcome and adopted bundle SHA; W2 findings list; W3 draft paths
and commit SHAs; W4 confirmation. Then STOP. No status flips, no merges of
findings-driven changes, no gate reviews — those are Dave's next decisions.

## Constraints

- Real git throughout; verify every push in `git log` before reporting it.
- Drafts are drafts: nothing created here claims `agreed`.
- One commit per coherent unit; technically precise commit messages.
- Anything ambiguous: stop and surface the question rather than improvise.
