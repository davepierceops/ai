# Expedited Review Log

One line per expedited or doc-only agreement, per the "Expedited return to
`agreed`" and "Doc-only cycle" sections of
`policies/document-metadata-policy.md`. Documents agreed either way
carry `last-reviewed: reviews/expedited-log.md @ <sha>`; the SHA selects the
entry.

Append-only. Entries are not edited or removed when the document they describe
is later revised, superseded, or deleted — this is a record of agreements, not
a description of current state. Newest last.

This file is a dated record: each entry states a fact about one agreement on
one date. It carries no totals, rates, or rollups, and nothing derived from it
belongs in canonical policy text.

Format — one Markdown list item per entry:

`- <YYYY-MM-DD> — <document path> @ <sha> — <what changed, one clause>`

Where the document is new — which the doc-only cycle admits and the expedited
path does not — nothing changed, so the last clause states what the document
is instead.

The SHA is authoritative. The date and the one-clause summary are reader
convenience — both are derivable from the commit it names, and on any conflict
`git show` wins. They are written out anyway because a log of bare paths and
hashes is a log nobody reads, and this file is a dated record, which is where
derived facts are allowed to live.

## Entries

- 2026-08-06 — policies/decision-log-policy.md @ 01fb1030e06dffa555ff6482eeda9a90f9e2b461 — founding decision-log policy, agreed via doc-only cycle (DEC-000020)
- 2026-08-07 — policies/document-metadata-policy.md @ 1f5b7153dc3140f500ceb5575f459f1098b23de0 — LEXICON.md added to in-scope set; owner override of doc-only condition 3, no review cycle (DEC-000060)
- 2026-08-07 — roles/chief-of-staff.md @ 81df6ddf0829fd23d4c7fe3a3516c8e0c4c9d245 — execution-report handling, sharpened pre-staging, decomp spec-SHA pin, directive-register compression; agreed via doc-only cycle (DEC-000070)
- 2026-08-11 — LEXICON.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — policies/remote-write-verification-policy.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — roles/chief-of-staff.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — skills/command-blocks.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — skills/directive-dispatch.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — skills/spec-review-cycle.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
