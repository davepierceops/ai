# Cycle 11 Review Directive — document-metadata-policy.md (re-gate)

Date: 2026-08-06
Type: gate re-review (fresh Spec Reviewer session)
Model: Opus

## Document under review

- `policies/document-metadata-policy.md` @ `321ff5af104854d37443fd30bb7581d9e7740ab0`
  (`status: in-review` on `main`)

This is the re-gate of the cycle-10 revision. Review the `## Doc-only cycle`
section and its collateral edits against the **whole** document.

## Prior cycle

- `reviews/document-metadata-policy-cycle-10.md` — verdict `changes-required`
- `docs/cycles/metadata-policy-cycle-10-triage-2026-08-06-directive.md` — the dispositions this revision executed

## Collateral edits in the same change (confirm consistency with the amended policy)

- `roles/spec-reviewer-agent.md` — both bounded exceptions named and bounded (B4)
- `reviews/expedited-log.md` — header and entry format generalized to expedited-or-doc-only (N1)

## Reviewer

Execute as the **Spec Reviewer Agent** (`roles/spec-reviewer-agent.md`). Not the
instance that drafted or executed the section; does not agree the document. Read
the role doc and the review artifact schema in `skills/spec-review-cycle.md`
before reviewing.

## Checks

1. **Resolution.** Each cycle-10 finding (B1–B4, N1–N5, O1) is resolved per the
   triage directive's disposition — including that N3 was a *modify*: no `DEC-`
   IDs in the portable body, cited at the change level instead, and the route
   renamed to "doc-only cycle." A disposition the executor departed from is a
   finding.
2. **New issues.** Scan the revised section and the collateral edits for anything
   the revision introduced — internal consistency, cross-reference accuracy and
   resolution, traceability, overstated confidence, and any ambiguity that turns
   an enforcement rule into a judgment call.
3. **Whole-document coherence.** The three routes to `agreed` (full cycle,
   expedited, doc-only) are mutually consistent, and the `roles/` and
   `reviews/expedited-log.md` edits match the policy.
4. Flag anything needing **Dave's judgment** before agreement.

## Output

Write `reviews/document-metadata-policy-cycle-11.md` per the schema (verdict-first;
`Verdict` = `ready | ready-with-findings | changes-required`, never `agreed`).
Commit on a branch, open a PR. **Do not** change the policy's `status` — the flip
to `agreed` is Dave's, after a clean verdict.
