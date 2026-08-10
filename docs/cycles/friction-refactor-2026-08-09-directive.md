# Directive: Friction Refactor — 2026-08-09

Route: fresh
Model: Opus 5
Track: A (git push available; no MCP in the loop)
Execution block: this directive travels as a paste block. Your first act — before
any other work — is Step 0 below, which lands this file in git. This directive is
itself the first use of the transport model it introduces.

## What this is

An overnight, autonomous execution. Two methodology changes, decided today by
Dave in a decision-layer session, are to be implemented across the
`davepierceops/ai` repository, then run through self-review cycles until clean —
without returning to Dave. Every judgment call you would normally escalate, you
instead decide and log. Dave reviews the whole branch in the morning.

**The agreement gate is preserved by structure, not by asking:** everything
happens on a branch, nothing merges to main, no document flips to `agreed`.
Your job is to produce a branch worth agreeing to.

## Step 0 — Land this directive

1. `git fetch origin` and branch from `origin/main` HEAD:
   `methodology/friction-2026-08-09`.
2. Write this directive, verbatim and in full, to
   `docs/cycles/friction-refactor-2026-08-09-directive.md`.
3. Commit it to the branch and push the branch. Record the commit SHA — this is
   the "landed as SHA" your final report cites.

## Binding decisions (do not re-litigate)

These were decided by Dave today. They are inputs, not proposals. Where a
document contradicts them, the document changes.

### Change 1 — Directive transport

- **D1.1** Directives travel from chat to executor as paste blocks. The
  executor's first act is writing the directive to `docs/cycles/` and
  committing it. The SHA is reported back post-hoc ("executed X, landed as
  SHA"), not established pre-dispatch. This applies to **all** directive
  classes, cycle directives included — Dave explicitly confirmed post-hoc SHAs
  are sufficient for the decision record.
- **D1.2** Chat-side MCP writes leave the dispatch critical path. The
  verification apparatus that existed to compensate for the MCP transport
  (content checks, size-field inspection after full-file writes, read-back
  verification of chat-side pushes) shrinks accordingly: it governs only the
  MCP writes that remain, and the documents must stop presenting it as part of
  dispatch.
- **D1.3** Track B in its current form — the no-repository-tooling delivery
  path via `~/Downloads`, pre-flight globs, relocate/commit/echo blocks —
  loses its reason to exist for directive delivery, since the paste transport
  needs no repository tooling on the chat side at all. Retire it from the
  dispatch skill. Preserve the *diagnostic* insight Dave chose to keep: the
  two-consecutive-failure pattern as a contention/tooling-degradation detector
  (DEC-000080's keep-reason) must survive somewhere sensible, even though the
  track it used to open is gone. Where it lands is your call — log it.
- **D1.4** The rationale, if a document needs it stated: a directive does two
  jobs, transport (value expires at execution) and record (value is later).
  Only the record needs git, and the executor — not chat — is the party for
  whom git is cheap. The integrity question shifts from provenance to
  paste-arrival-intactness, which the existing parse-atomic paste rules
  already govern.

### Change 2 — Spec branches (open spec delta)

- **D2.1** During a tranche's execution, Dave may edit spec documents freely,
  with no reviewer gate and no per-edit ceremony, on a dedicated spec branch:
  `spec/<tranche-slug>`. Commits land as he goes. This is called an **open
  spec delta**; the branch is the state — no new status value, no lexicon
  machinery beyond pointing at git.
- **D2.2** **Reconciliation** closes the delta: the spec is brought to 100%
  agreement with what was actually built, and the accumulated diff goes
  through the reviewer gate **once, as a single cycle**, arriving as a PR.
  Main never carries unreviewed spec text, so `agreed` on main never lies.
- **D2.3** A delta is bounded by the tranche and never spans tranches.
  Reconciliation blocks the next tranche's decomposition — decomposing from
  unreviewed spec is prohibited. Dave may invoke reconciliation early,
  mid-tranche, at will; frequent small reconciliations are the encouraged
  norm, the tranche boundary is merely the deadline.
- **D2.4** Mid-delta dispatches derive from the **spec branch**, not main:
  truth-at-handoff. The dispatch pins a branch SHA; provenance survives.
- **D2.5** Concurrency: Dave runs at most two tracks, always on different
  tranches, chosen for disjoint spec territory. A spec document is *claimed*
  by appearing in an open delta's diff; a document claimed by one open delta
  may not be claimed by another. Parallelism is achieved by claiming disjoint
  territory, never by merging convergent edits — the merge case is refused,
  not tooled. Where disjoint territory doesn't exist in a project, tracks go
  cross-project or work goes serial.
- **D2.6** The reframe this encodes: agreement attaches to the version of
  record at reconciliation, not to a version pre-approved before building.
  During a delta the spec is descriptive of decisions Dave is making with hot
  context; the amnesiac-executor constraint requires truth-at-handoff, not
  agreement-in-advance. The recreate-from-spec goal needs the spec true at
  rest, between deltas — not at every instant during one.
- **D2.7** The design test both changes must satisfy, worth encoding where
  operating habits live: **what does this cost Dave in the loop?** Operator
  attention is the system's scarcest, non-parallelizable resource; evidence
  integrity may not be purchased by spending it as if it were free.

## Work

1. **Read first.** Read every document you will touch in full, plus
   `LEXICON.md`, `decisions/log.md` (cite governing entries where they exist),
   and `OPEN-ITEMS.md`, before editing anything.
2. **Sweep for blast radius.** The known-affected set is
   `skills/directive-dispatch.md`, `skills/spec-review-cycle.md`,
   `policies/remote-write-verification-policy.md`, `LEXICON.md`,
   `context-sets/spec-and-change-discipline.md`, `operating-model.md`,
   `policies/commit-and-change-control-policy.md`,
   `roles/chief-of-staff.md`, `skills/command-blocks.md`. Do not trust this
   list: grep the repo for `Track B`, `sync block`, `MCP`, `dispatch`,
   `pre-flight`, `agreed`, `red-gate`, `spec-first`, and related terms, and
   find every passage the two changes touch. A value updated in one place but
   stale in another is a defect.
3. **Edit for the decisions.** Revise every affected document so the binding
   decisions above are what the documents say. Preserve each document's
   register and length discipline — directive-dispatch was deliberately
   compressed; do not bloat it back. Where spec-first language
   ("nothing is built until specified") now conflicts with D2.6, rewrite it to
   state the true rule: the spec is true at dispatch and at rest, and
   agreement lands at reconciliation.
4. **Status honesty.** Any currently-`agreed` document whose content you
   revise moves to `status: in-review` on the branch. Do not flip anything to
   `agreed` — that is Dave's verb, and it happens after his morning review,
   not tonight.
5. **History, not rewrite.** Update each document's status-of-this-draft /
   revision notes per its own convention, citing this directive by path.
   Do not retrofit existing `reviews/` artifacts — they are the record of what
   happened.

## Self-review cycles

6. After the edit pass, act as the Spec Reviewer role over the full changed
   set. Write a review artifact per the schema in
   `skills/spec-review-cycle.md`, one per document, to `reviews/` **on the
   branch**, using the standard filename convention with cycle numbers
   continuing each document's existing sequence. Mark them clearly as
   self-review: `Reviewer: self-review (autonomous, this directive)`.
7. Fix every `blocking` finding. Re-review. Repeat until a clean pass or
   **5 cycles**, whichever first. If cycle 5 ends with blocking findings
   open, stop and list them in the report — do not force a clean verdict.
8. You are reviewing your own work; treat that honestly in the artifacts.
   Independence is degraded by design tonight; Dave's morning review is the
   independent gate.

## Decision log

9. Every judgment call you make that would normally go to Dave — a wording
   choice with policy weight, where the two-failure detector lands, how a
   conflict between documents resolves, anything you'd otherwise ask —
   gets an entry in `docs/cycles/friction-refactor-2026-08-09-decisions.md`
   on the branch: numbered, one per decision, each stating the question, the
   options, what you chose, and why. This file is what makes overnight
   autonomy reviewable. When in doubt whether something is log-worthy, log it.

## Hard constraints

- Never merge to main; never push to main; never force-push.
- Never flip any document to `agreed`.
- Do not modify `decisions/log.md` — propose entries in the decision-log file
  instead, formatted for Dave to promote.
- Do not attempt PR creation via `gh` (known TLS failure in this sandbox) —
  push the branch; the PR opens from the morning session.
- Stay inside the blast radius of the two changes plus required consistency
  edits. This is not a general cleanup pass.
- An instruction here that cannot be executed as written → stop that item,
  log it, continue with the rest. Do not improvise silently and do not let
  one blocked item halt the whole run.

## Final report

Report what was done, not what this directive said — triageable by CoS:

- branch name and HEAD SHA; the Step 0 landed-as SHA
- documents changed, one line each
- review cycles run, final verdict per document, any blocking findings left
- the decision log: count, plus the three decisions most needing Dave's eye
- anything stopped or blocked, and why
