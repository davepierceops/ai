# Cycle 12 Review Directive — document-metadata-policy.md (re-gate)

Date: 2026-08-06
Type: gate re-review (fresh Spec Reviewer session)
Model: Opus

## Document under review

- `policies/document-metadata-policy.md` @ `67b586a1be1bd01cca6dfc82c68ca30ab04df9ad`
  (`status: in-review` on `main`)

Re-gate of the cycle-11 revision. Review the `## Doc-only cycle` section and its
collateral edits against the whole document.

## Prior cycle

- `reviews/document-metadata-policy-cycle-11.md` — verdict `changes-required`
- `docs/cycles/metadata-policy-cycle-11-triage-2026-08-06-directive.md` — the dispositions this revision executed

## What changed since cycle 11 (confirm each is resolved)

- **B1 (option b):** the multi-document rule was removed, not patched — a doc-only
  agreement now covers exactly one in-scope document, so `### The record`'s
  single-entry SHA resolution holds by construction. Recorded as `DEC-000040`,
  superseding `DEC-000030` and carrying its gate-doc exclusion forward.
- **N1** `skills/spec-review-cycle.md`, **N2** `skills/conversation-retro.md` (both
  routes now named; retro-surfaced revisions barred from both), **N3** companion
  tracked paths in their own commits, **O1** condition-3 source named once,
  **O2**/**O3** `OPEN-ITEMS.md`.

## Checks

1. **Resolution.** Each cycle-11 finding (B1, N1–N3, O1–O3) is resolved per the
   triage directive. A disposition departed from is a finding.
2. **New issues.** Scan the revised section and collateral for anything the
   removal introduced — dangling references to the deleted multi-document rule,
   internal consistency, cross-reference accuracy, traceability to `DEC-000040`,
   overstated confidence, ambiguity.
3. **Decision-log integrity.** `DEC-000040` supersedes `DEC-000030` and preserves
   its gate-doc exclusion; confirm nothing still in force was dropped in the
   supersession.
4. **Whole-document coherence.** The three routes to `agreed` remain mutually
   consistent.
5. Flag anything needing **Dave's judgment**.

## Output

Write `reviews/document-metadata-policy-cycle-12.md` per the schema (verdict-first;
`Verdict` = `ready | ready-with-findings | changes-required`, never `agreed`).
Commit on a branch, open a PR. **Do not** change the policy's `status`.
