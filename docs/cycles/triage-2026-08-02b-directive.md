# Triage Directive — Exec Report on PR #3, 2026-08-02

Date: 2026-08-02
Source: chat triage of the execution report for
`docs/cycles/triage-2026-08-02-directive.md` (executed on branch
`triage-2026-08-02-exec`, merged to main as PR #3 by Dave).
Executor for W-1 through W-3: Claude Code, fresh session, local clone.
E1–E5 are dispositions recorded here; the reviewer re-gate is a separate
dispatch and is not authorized by this directive.

## Dispositions

### E1 — Finding 1 (lifecycle premise wrong for two of three files). RECORDED.
The prior directive asserted all three in-scope files were `agreed`; two were
`draft`. The executor's deviation — edit per actual status rather than stop —
is accepted. Consequence stands: no demotion and no flip is owed on
`context-sets/spec-and-change-discipline.md` or the pre-W-B text of
`policies/commit-and-change-control-policy.md`; only
`policies/document-metadata-policy.md` (now `in-review` via W-C's same-commit
demotion) requires a gated return to `agreed`.

### E2 — Finding 4 (condition 3's enumerated class). DECIDED, dispatched as W-1.
Decided by Dave, 2026-08-02:
- The trio is **in**: `policies/testing-policy.md`,
  `policies/verification-boundary-policy.md`, and
  `roles/skeptic-risk-agent.md`. Each states a hard stop removable inside the
  ten-line ceiling; a gate over work and a gate over documents carry the same
  small-diff-removes-a-gate hazard.
- Neither narrow-the-definition nor widen-the-list: the **criterion is
  primary** and the named list is a **non-exhaustive floor**. A document
  stating a gate, hard stop, or enforcement rule is ineligible for the
  expedited path whether or not it is named; the list is the minimum, not the
  boundary. When unsure, ineligible — mirroring the commit policy's "when in
  doubt, consequential."

### E3 — Finding 3 (flip-agreed SHA check). DISPATCHED as W-2.
Standing hard precondition on the next agreement flip. ACs already written in
`OPEN-ITEMS.md`; this directive dispatches the work, not a respecification.

### E4 — Finding 5 (stale references). SPLIT.
- `context-sets/collab-workflow.md:36` — dispatched as W-3. It is `draft` and
  carries the sentence B2 removed while pointing at
  `spec-and-change-discipline.md` for operating habits; the two now disagree.
  Plain-commit correction, per the N2-resolution precedent for aligning
  contradicting drafts.
- `policies/project-setup-requirements.md` §1 parenthetical — RECORDED, no
  action. That file is a W3 draft and gates separately; the stale note
  resolves in its own cycle.

### E5 — Finding 6 (evidence records not retrofitted). RECORDED: correct, leave.
`docs/packages/*-change-package.md` are records of what was measured then.
Retrofitting records to match later state is the defect, not the fix.

## Work items

### W-1 — `policies/document-metadata-policy.md`: condition 3 restatement
Restate the expedited path's condition 3 per E2:
- Criterion primary: any document stating a gate, hard stop, or enforcement
  rule is ineligible.
- Named list becomes an explicitly non-exhaustive floor ("at minimum"), and
  gains `policies/testing-policy.md`,
  `policies/verification-boundary-policy.md`, and
  `roles/skeptic-risk-agent.md`.
- Add the fail-safe clause: when unsure whether a document matches the
  criterion, it is ineligible.
The document is already `in-review` (W-C, same-commit demotion) — no further
status change in this work item, and **no flip**.
On landing, strike the `Settle condition 3` entry in `OPEN-ITEMS.md`
(decision: Dave, 2026-08-02, this directive; settlement rides the same
re-gate cycle the entry required).

### W-2 — `bin/flip-agreed` SHA-in-log check
Implement per the ACs in `OPEN-ITEMS.md` ("expedited path's log entry is
unenforced"):
- `flip-agreed --review` resolves the cited SHA against the target artifact's
  contents when that artifact is the expedited log, failing closed when the
  SHA is absent.
- Abbreviated SHAs normalized through `git rev-parse` before comparison.
- Non-log artifacts keep existence-only behaviour.
- `check-frontmatter` reports the same condition over the whole in-scope set.
Red-gate applies: tests derived from these ACs run and confirmed red before
implementation. Own commits, technically precise messages.
On green, annotate the `OPEN-ITEMS.md` entry resolved with the commit
reference. The precondition on the flip is then satisfied by this work — the
flip itself remains gated (W-4).

### W-3 — `context-sets/collab-workflow.md` alignment
Plain commit (document is `draft`): replace the line-36 claim with the
tiered posture as restated by W-A in `spec-and-change-discipline.md`
("Agents dispose of routine changes; Dave disposes of judgment calls"),
keeping the pointer to that document for operating habits. Check the rest of
the file for further instances of the superseded claim per the consistency
habit; fix any found in the same commit.

### W-4 — Report and stop
Report per work item: commits, evidence (`bin/tests/run`,
`check-frontmatter --all`, red-then-green for W-2), findings. **No flip** of
`policies/document-metadata-policy.md` — the gated return to `agreed`
requires the reviewer re-gate (fresh session, separate dispatch) and Dave's
explicit approval, in that order, with W-2 green as the precondition. Then
STOP.

## Out of scope — do not touch
- The gate review artifact: executor drafted these revisions and is recused
  per `roles/spec-reviewer-agent.md`.
- The agreement flip, under any circumstances.
- `docs/packages/*` records (E5) and
  `policies/project-setup-requirements.md` (E4).
- `specs/prd-template.md:22` — correct as-is; spec agreement is Dave's.

## Constraints
- Branch + PR; real git; verify every push in `git log`.
- One coherent commit per work item where practical.
- Anything ambiguous: stop and surface, do not improvise.
