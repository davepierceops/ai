# Directive — spec-review-cycle N1 fix (Trivium cycle-2 re-gate finding) — davepierceops/ai

Date: 2026-08-09
Route: fresh
Model: Opus 5
Track: A

Resolves: `reviews/spec-review-cycle-cycle-3.md` N1 (non-blocking). Dave accepted
the reviewer's specified fix.

Document in scope (pinned by commit SHA):
- skills/spec-review-cycle.md @ a7a915cddf3ca1fef774c17942f1e9406cc3715a
  (status: in-review, last-reviewed: null)

## Finding (N1)

The reversal made Route overridable while the document still grounds the *fresh*
default in its own Hard constraints — so it now both forbids and licenses
executing a cycle in the conversation that produced it, with no precedence
stated. An author could read "the stated field governs" as licensing
`Route: existing context` → execute in the cycle chat, carrying chat history —
the failure the Hard constraints exist to prevent.

## Change

In `skills/spec-review-cycle.md`, immediately after the clause ending
"…and the stated field governs" (~`:143-145`), add one clause establishing
precedence:

- Route selects the **execution** session (per `LEXICON.md`'s three layers).
  `existing context` therefore names an already-running *execution* session, and
  never releases the Hard constraints (`:29-32`) or step 5's prohibition
  (`:61-62`) on executing a cycle in the conversation that produced it — whatever
  Route is stated.

Intent: keep Route overridable (DEC-000150 intact — stating a field is not
freedom to choose any value without limit), while removing the reading in which a
stated field overrides a Hard constraint.

## Scope / do-not

- Edit **only** `skills/spec-review-cycle.md`. Neither mirror
  (`directive-dispatch.md`, `LEXICON.md`) carries this seam — do not touch them.
- Do not alter DEC-000150 or reopen the Route/Model reversal. This is a
  precedence clarification, not a change to overridability.
- Do not flip status.

## Executor obligations

- Verify `spec-review-cycle.md` is at `a7a915c` (or contains it in history with no
  intervening edits) before editing.
- Land via branch + PR (main is protected). Report branch/PR.
- Report what was done, not what this directive said.

## Done

The precedence clause is added; Route stays overridable; no mirror touched;
branch + PR opened. A **cycle-4** re-gate of `spec-review-cycle.md` follows before
the agreement flip.
