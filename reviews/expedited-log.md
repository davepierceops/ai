# Expedited Review Log

One line per expedited agreement, per the "Expedited return to `agreed`"
section of `policies/document-metadata-policy.md`. Documents agreed this way
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

The SHA is authoritative. The date and the one-clause summary are reader
convenience — both are derivable from the commit it names, and on any conflict
`git show` wins. They are written out anyway because a log of bare paths and
hashes is a log nobody reads, and this file is a dated record, which is where
derived facts are allowed to live.

## Entries

- 2026-08-06 — policies/decision-log-policy.md @ 01fb1030e06dffa555ff6482eeda9a90f9e2b461 — founding decision-log policy, agreed via doc-only cycle (DEC-000020)
