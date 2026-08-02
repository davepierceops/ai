# Triage Directive — Doc-Review W5 Report, 2026-08-02

Date: 2026-08-02
Source: chat triage of the W5 report from
`docs/cycles/doc-review-2026-08-02-directive.md` (executed at `3600e90`,
report delivered at `ab1f829`).
Executor for D4: Claude Code, fresh session, local clone. D1–D3 are
dispositions recorded here; only D4 dispatches work.

## Dispositions

### D1 — Procedural deviation: drafts landed direct on main. RESOLVED: leave.
The five W3/W4 commits stay. They are `status: draft`, frontmatter-clean, and
reverting to redo via PR is ceremony producing history noise. The bypass that
permitted the direct push is addressed in D3.

### D2 — W1 bundle regeneration. RESOLVED: withdrawn, premise falsified.
Reference closure cannot reproduce a curated session bundle in this repo:
no entry-point at any depth yields a bundle-shaped set (1 / 5 / 28–35 / 54);
`context-sets/base.md` is a closure sink (mandatory root, zero out-edges);
MANIFEST had already recorded the same result and W1 reproduced it at a new
SHA. Q4 is closed. The bundle remains curated. Durable design question —
structural completeness-checking for a curated bundle (likely: committed
bundle manifest + verify script; judgment in the list, enforcement in the
check) — goes to BACKLOG (see D4 W-C).

### D3 — B4 credential bypass. PART RESOLVED / PART RECORDED.
Done 2026-08-02: `ai` branch protection now has bypass disallowed, including
administrators — the PR requirement binds every wielder of the credential.
Recorded: B4 is standing evidence on the Q7 backlog entry (role-scoped
credentials): an agent PAT that *cannot* bypass, with the admin credential as
break-glass, is the durable fix. Pending: apply the same no-bypass toggle to
wne-crm and catchable after the org's Team upgrade makes their protection
rules enforceable.

### D4 — B1+B2+B3 (+A4, A5). DISPATCHED: one spec-review cycle, below.

## D4 cycle specification

Run per `skills/spec-review-cycle.md`. Three files in scope; all are
`agreed`, so changes follow the full revision lifecycle (same-commit
demotion to `in-review`, review artifact, gated flip — flip-agreed
SHA-in-log check is a hard precondition per standing obligation).

### W-A — `context-sets/spec-and-change-discipline.md` (B1 + B2)
Rewrite the two sentences that contradict the decided posture, and every
other instance of the same claims per the document's own consistency habit:
- "Specifications are the source of truth, and a human verifies every
  consequential step before it lands" — replace the per-step-verification
  claim with the tiered posture: agents execute and merge the routine class
  autonomously; human judgment gates at release decisions and spec
  agreement ("gate only on actual human judgment"). The gate anchors at the
  release decision, not at landing — align with
  `policies/commit-and-change-control-policy.md`.
- "Claude drafts, Dave verifies. Agents propose; Dave disposes" — restate
  for the routine class: agents dispose of routine changes; Dave disposes of
  release decisions and spec agreement.
B1 and B2 are one change; fix all instances together.

### W-B — `policies/commit-and-change-control-policy.md` (B3, expansion)
Decided: expand this policy to match its title — no sibling policy. Add
governed statements of:
- Push mechanics: plain `git push` allowed for agents; force-push denied,
  both client-side (settings deny, respected in all permission modes) and
  server-side (branch protection).
- Branch protection as the structural gate: required on `main` in every
  adopting repo — no force-push, no deletion, changes via PR, bypass
  disallowed including administrators. Cross-reference
  `policies/project-setup-requirements.md` (draft) rather than duplicating
  its checklist.
- Agents may open and merge PRs for the routine class; the human gate fires
  at the release decision (existing §) and spec agreement, not at merge.

### W-C — `policies/document-metadata-policy.md` (A4 + A5)
- Extend in-scope globs to `vendors/**` (A4).
- Add `policies/project-setup-requirements.md` to the no-expedited-path
  enumeration, effective at that document's agreement (A5).

### W-D — BACKLOG-v2.md
- Annotate the role-scoped-credentials entry with B4 as evidence (one line).
- Add: bundle-manifest completeness check (committed bundle manifest +
  verify script) per D2 (one line).

### W-E — Report and stop
Cycle artifacts per the skill: findings, review artifact, proposed diffs.
The agreement flip is Dave's gate — present, do not flip without his
explicit per-cycle approval. Then STOP.

## Out of scope — do not touch
- A3 (orchestrator → chief-of-staff supersession): status flip, separate
  authorization.
- A1 (`.claude/settings.json` divergence): adapter file, converging via a
  parallel settings session; not a governed-doc change.
- Any edit to the W3 drafts themselves: they gate separately.

## Constraints
- Route all changes via branch + PR: `ai@main` now rejects direct push for
  everyone, by design. Real git; verify every push in `git log`.
- One coherent commit per work item where practical; technically precise
  messages.
- Anything ambiguous: stop and surface, do not improvise.
