# Decision Log — davepierceops/ai

Append-only record of methodology decisions, per
`policies/decision-log-policy.md`. Newest last. Entries are never edited or
deleted; a reversal is a new entry whose `Supersedes:` names the old ID.

## DEC-000010 — Doc-only cycle is a sanctioned route to `agreed`
Date: 2026-08-06
Decision: A co-authored methodology/governance document may reach `status:
agreed` through the doc-only cycle — authored or edited together in the artifact
pane, at least one consistency sweep, and Dave's verbal sign-off — recorded as an
entry in `reviews/expedited-log.md`, with `last-reviewed` citing the log and the
reviewed SHA.
Context: Entry conditions — the document is methodology/governance prose (any
format, not a program meant to run); it is co-authored in the artifact pane;
Dave asks for the cycle and agrees. The metadata policy previously sanctioned
only the full reviewer cycle and the expedited path, neither of which fits a
co-authored, multi-section, or new prose document.

## DEC-000020 — Doc-only cycle overrides metadata-policy route-to-`agreed` limits
Date: 2026-08-06
Decision: The doc-only cycle overrides the expedited-path eligibility conditions
in `policies/document-metadata-policy.md` (the ≤10-line body cap, the single
in-scope-file rule, and the gate/enforcement-doc exclusion) wherever they would
block a co-authored, signed-off document from reaching `agreed`. Dave is the
final arbiter of policy; this ruling governs over the metadata-policy text until
that text is amended to describe the doc-only route.
Context: `policies/decision-log-policy.md` is a new multi-section policy, so it
fails the expedited eligibility conditions, yet it was co-authored and signed
off under the doc-only cycle. `bin/flip-agreed` enforces only a frontmatter-only
transition and that the cited SHA resolves to a log entry — not the eligibility
conditions — so this agreement lands cleanly. Amending the metadata-policy prose
is queued as follow-up.
