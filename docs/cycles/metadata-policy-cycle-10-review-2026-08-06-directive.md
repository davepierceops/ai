# Cycle 10 Review Directive — document-metadata-policy.md

Date: 2026-08-06
Type: gate-review kickoff (fresh Spec Reviewer session)
Model: Opus

## Document under review

- `policies/document-metadata-policy.md` @ `fca43091fff78275b1d65b60aa9c80d0c9e9089f`
  (`status: in-review` on `main`)

Scope: the new `## Doc-only agreement` section, reviewed against the **whole**
document — this is a revision to a gate document, not a standalone addition.

## Reviewer

Execute as the **Spec Reviewer Agent** (`roles/spec-reviewer-agent.md`). This
session must not be the one that drafted the section, and it does not agree the
document — Dave does. Read `roles/spec-reviewer-agent.md` and the review artifact
schema in `skills/spec-review-cycle.md` before reviewing.

## Checks (the gate-review subset that applies to a policy document)

- **Completeness.** The route is fully specified — eligibility, sequence,
  recording — with no gap an agent would fill by guessing.
- **Internal consistency.** It contradicts no other section, and its
  cross-references resolve and stay accurate: `"The record"` and the sequence it
  defers to (both under "Expedited return to `agreed`"), and the `condition 3`
  gate-doc class it points at.
- **Traceability.** It faithfully implements the decisions it derives from —
  `decisions/log.md` `DEC-000010` (the route exists) and `DEC-000030` (gate docs
  excluded, kept on the full cycle even when co-authored). Flag any drift.
- **Route coherence.** A third path to `agreed` alongside the full cycle and the
  expedited path contradicts neither, nor what `bin/flip-agreed` enforces.
- **No overstated confidence, no ambiguity** that turns an enforcement rule into
  a judgment call.
- Flag anything needing **Dave's judgment** before agreement.

## Output

Write `reviews/document-metadata-policy-cycle-10.md` per the schema
(verdict-first; `Verdict` = `ready | ready-with-findings | changes-required`,
never `agreed`). Commit on a branch, open a PR. Do **not** change the policy's
`status` — the flip to `agreed` is Dave's, after a clean verdict.
