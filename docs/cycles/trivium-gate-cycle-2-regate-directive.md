# Re-gate Directive — Trivium cycle-2 (D3 reversal) — davepierceops/ai

Date: 2026-08-09
Route: fresh
Model: Opus 5
Track: A

Purpose: reviewer gate re-check of the cycle-2 changes (Route/Model reversal +
DEC-000150) before Dave's agreement flip. Produces **cycle-3** review artifacts
per doc — these docs are already at cycle-2 (the original cycle-1 re-gate).

Documents in scope (pinned by **commit** SHA — resolvable in main history):
- skills/spec-review-cycle.md @ a7a915cddf3ca1fef774c17942f1e9406cc3715a
- skills/directive-dispatch.md @ a7a915cddf3ca1fef774c17942f1e9406cc3715a
- LEXICON.md @ a7a915cddf3ca1fef774c17942f1e9406cc3715a

All three are currently `status: in-review`, `last-reviewed: null`.

Change under review: `docs/cycles/trivium-gate-cycle-2-directive.md` @ `6c87ea9`,
executed on branch `trivium-gate-cycle-2-exec`, merged to main (PR #56).
Prior review artifacts (per doc): `reviews/<stem>-cycle-2.md` — Verdict: ready,
the state the original agreement rested on.

## Reviewer task

For each in-scope document, gate re-check the reversal — not a full re-review:

1. **R1 landed and correct.** Route/Model are now stated per cycle directive,
   with Opus 5/fresh as overridable **defaults**; the fixed-by-class carve-out is
   gone from all three mirrors (spec-review-cycle format block + prose;
   directive-dispatch *Use when* + *The four requirements*; LEXICON `Directive`
   def). Grep the whole tree — **no dangling reference to the removed carve-out
   survives** anywhere.
2. **Track-required half preserved.** Nothing in the reversal weakened or dropped
   "track is required per directive."
3. **B1 stays closed by the all-four-stated route.** With route/model/track/exec
   all stated, directive-dispatch's "an unstated part is a defect" is satisfied by
   statement, not by exemption.
4. **Mirror consistency.** The three docs agree with one another and with
   DEC-000150; no doc still asserts the old fixed-by-class rule.
5. **R2 audit.** `decisions/log.md` DEC-000150 supersedes DEC-000110, restates the
   Track half inline (whole-entry supersession), and its ID conforms to
   `decision-log-policy`. (The log is not a lifecycle doc — check as part of the
   change, not for frontmatter.)
6. **Regression.** Re-read each edited section for internal contradiction the
   edits may have introduced.

## Output

- One review artifact per doc at `reviews/<stem>-cycle-3.md`, per the schema in
  `skills/spec-review-cycle.md`. Verdict-first. **Do not overwrite the cycle-2
  artifacts.**
- Clean pass → header only, no prose. Any `changes-required` → stop the flip;
  those findings open the next cycle.
- Land the artifacts via branch + PR (main is protected). Report the branch/PR.

## Notes

- Route fresh / model Opus 5 / Track A are stated here per the very rule this
  reversal installs — the directive models the new convention.
- On ready verdicts, the agreement flip is Dave's: `bin/flip-agreed` points each
  doc's `last-reviewed` at its cycle-3 artifact.
