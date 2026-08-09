# Cycle 2 Directive — Trivium gate (D3 reversal: unpin Route/Model)

Date: 2026-08-08
Route: fresh
Model: Opus 5
Track: A
Documents in scope:
- skills/spec-review-cycle.md @ 435ebc4
- skills/directive-dispatch.md @ cd7a7fd
- LEXICON.md @ fc9f49b

## Decisions

### R1 — modify (reverses the Route/Model half of D3)

Finding: D3 (Trivium cycle-1) declared Route (*fresh*) and Model (*Opus 5*)
**fixed-by-class** for reviewer-gated cycle directives, unstated per directive.
Dave reverses this half: cycle directives state **all four** (route, model,
track, execution block) like every other dispatch. Opus 5 and fresh are the
class **defaults** — overridable, and stated per directive. The Track-required
half of D3 stands.

Resolution:

- **skills/spec-review-cycle.md**
  - *Format block (`:107` region):* add `Route: <fresh | existing context>` and
    `Model: <model — default Opus 5>` as stated fields, alongside the existing
    `Date:` / `Track:` lines, so the generated cycle directive carries all four.
  - *Required-fields line (`:130`):* add route and model to the required set.
  - *"Route and model are fixed by class" prose (`:133`+):* rewrite. They are no
    longer fixed-by-class. State that Opus 5 and fresh are the **defaults** for
    reviewer-gated cycle directives, stated per directive and overridable, keeping
    the pointers to `directive-dispatch` §1/§2. Remove the "not restated per
    directive" claim.
- **skills/directive-dispatch.md** (`:21`–`27` bounded-exception): rewrite.
  Remove the carve-out making route/model fixed-by-class. A reviewer-gated cycle
  directive states all four requirements like any dispatch; note Opus 5/fresh as
  the usual selection for the class, not an exemption. Reconcile downstream refs:
  §1 Route, §2 Model, and the "Status of this draft" line (~`:325`) that cites
  "the cycle-directive bounded exception."
- **LEXICON.md** (`Directive` def, ~`:64`–`66`): update the mirror so the
  definition no longer states the fixed-by-class exception; align with "all four
  stated, Opus 5/fresh default."

Dictated wording: none — executor drafts to the intent above; Dave reviews the diff.

### R2 — record the reversal (audit)

Finding: D3's Route/Model-fixing is being reversed after landing agreed.
Resolution: append **DEC-000142** to `decisions/log.md` — D3 (Trivium cycle-1)
fixed Route=fresh / Model=Opus 5 as fixed-by-class for reviewer-gated cycle
directives; this reverses that half (Route/Model stated per directive, Opus 5/
fresh default). The Track-required half stands. Owner override (Dave).

## Deferred / out of scope

- **TP-1 (`bin/cycle-open`)** — re-scoped: the skeleton must emit **Route, Model,
  Track** (not Track alone), and AC-CO-3 must enumerate all three. Re-dispatched
  after this cycle agrees. **PR #54 (Track-only) is superseded — held, do not
  merge.**
- **B1 contradiction** — stays closed. With all four stated, nothing is omitted,
  so `directive-dispatch`'s "an unstated part is a defect" is satisfied by
  statement rather than by exemption. This is the alternative valid fix to the
  same finding, not a reopening.

## Execution notes

- Scope is the Route/Model reversal only — do not touch the Track-required
  decision or any other D-series item.
- Reviewer re-gates the corrected docs before Dave agrees.
- This directive already states Route/Model in its header, modelling the target
  rule.
