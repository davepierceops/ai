# Cycle 11 Triage Directive — document-metadata-policy.md doc-only route

Date: 2026-08-06
Reviewed: `reviews/document-metadata-policy-cycle-11.md` — verdict `changes-required` (1 blocking, 3 non-blocking, 3 observations, all new)
Governing decisions: `DEC-000040` (this cycle — single-document doc-only, supersedes `DEC-000030`)

## Decisions

### B1 — modify (option b: drop shared-SHA multi-document)
Finding: `### The record`'s single-entry SHA resolution is falsified by the multi-document rule (`DEC-000030`/B3); a shared SHA lets document B's pointer resolve to document A's entry.
Resolution: Restore the single-in-scope-file rule for the doc-only cycle rather than make the checker path-aware. A doc-only agreement covers exactly one in-scope document (any size); multi-document sessions become sequential single-document agreements. `### The record`'s single-entry rule becomes true again untouched. Recorded as `DEC-000040`, superseding `DEC-000030` and carrying its gate-doc exclusion forward unchanged. The path-aware-checker option is not taken; no `bin/` change.

### N1 — accept
Resolution: `skills/spec-review-cycle.md` — the expedited path *and the doc-only cycle* produce the log lines. Draft, plain commit.

### N2 — accept (bar both routes)
Resolution: `skills/conversation-retro.md` — retro-surfaced revisions take the full cycle, not the expedited path *or* the doc-only cycle. Draft, plain commit. (Call made: the retro rule's intent is full scrutiny for retro-surfaced changes; both shortcuts are barred. If doc-only eligibility for co-authored retro revisions is ever wanted, that is a separate decision-log entry.)

### N3 — accept
Resolution: Folded into the B1 Sequence rewrite — the content commit touches only the one in-scope document; companion tracked paths (`decisions/log.md`, `OPEN-ITEMS.md`) land in their own commits, per the expedited path's "no other tracked path" rule.

### O1 — accept
Resolution: Name the source once — "the gate-document class defined by the expedited path's condition 3" — inside the doc-only condition 3.

### O2 — accept
Resolution: `OPEN-ITEMS.md` — one-line update noting the second bounded exception landed with the cycle-10 revision.

### O3 — accept (tracked, not fixed here)
Resolution: New `OPEN-ITEMS.md` entry recording the red `bundle base` test and its pinned cause (the AI-6 `base.md` citation makes reference closure pull in cited docs, staling AC-BN-10(a)). The fix is a `bin/` change, out of this gate's scope.

## Execution notes
- `document-metadata-policy.md` stays `in-review`; re-gate (cycle 12) precedes any flip.
- `skills/spec-review-cycle.md`, `skills/conversation-retro.md` are `draft` — plain commits, no flip.
- `decisions/log.md`, `OPEN-ITEMS.md` are out of the frontmatter in-scope set.
