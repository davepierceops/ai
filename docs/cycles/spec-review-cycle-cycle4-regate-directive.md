# Cycle-4 Re-gate Directive — spec-review-cycle (N1 fix) — davepierceops/ai

Date: 2026-08-09
Route: fresh
Model: Opus 5
Track: A

Purpose: reviewer gate re-check confirming N1 is resolved and the precedence
clause introduced no new seam, before the agreement flip. Produces
`reviews/spec-review-cycle-cycle-4.md`.

Document in scope (pinned by commit SHA):
- skills/spec-review-cycle.md @ 2fe299cade4325e80a3d51d3e2513c970f921b20
  (status: in-review, last-reviewed: null)

Change under review: `docs/cycles/spec-review-cycle-n1-fix-2026-08-09-directive.md`
@ `db9634a`, executed on branch `spec-review-cycle-n1-fix-exec`, merged via PR #60.
Prior artifact: `reviews/spec-review-cycle-cycle-3.md` (ready-with-findings, N1).

## Reviewer task

Confirm — not a full re-review:

1. **N1 resolved.** The added clause (after "…the stated field governs", ~`:143`)
   establishes that Route selects the *execution* session; `existing context`
   names an already-running execution session and never releases the Hard
   constraints or step 5's prohibition. The forbid/license seam is gone.
2. **Route stays overridable** — DEC-000150 intact; the clause limits what the
   value *means*, not the ability to state it.
3. **No new seam.** Re-read the surrounding paragraph and the Hard constraints /
   step 5 for any contradiction the clause may have introduced.
4. **Scope held.** No mirror edited; frontmatter unchanged (`in-review`, `null`).

## Output

- `reviews/spec-review-cycle-cycle-4.md`, per the schema in this document.
  Verdict-first; clean pass = header only. Do not overwrite cycle-3.
- `changes-required` → stop the flip; findings open the next cycle.
- Land via branch + PR (main is protected). Report branch/PR.

## Notes

- The other two docs (`directive-dispatch.md`, `LEXICON.md`) are unaffected —
  already cycle-3 `ready`, not in scope here, flipped alongside this one.
- On a `ready` verdict, the agreement flip is Dave's — all three, `bin/flip-agreed`
  pointing each `last-reviewed` at its artifact (dd + LEXICON → cycle-3;
  spec-review-cycle → cycle-4).
