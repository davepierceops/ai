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

## DEC-000030 — Doc-only cycle excludes review-regime documents; they keep independent review
Date: 2026-08-06
Decision: Narrows DEC-000020. The doc-only cycle still overrides the expedited
path's ≤10-line body cap and single-in-scope-file rule for co-authored
documents, but it does not override the gate/enforcement-doc exclusion.
Documents that state a gate, a hard stop, or an enforcement rule governing how
work is reviewed, agreed, or released — the class defined in
`policies/document-metadata-policy.md`, "Expedited return to `agreed`",
condition 3 — reach `agreed` only through the full reviewer-gated cycle
(`skills/spec-review-cycle.md`), even when co-authored. The doc-only cycle's
verbal sign-off is not sufficient for that class.
Context: DEC-000020 overrode the gate-doc exclusion alongside the size and
single-file limits, which was too broad. The doc-only cycle trades away
independent review, and the one class where independence is load-bearing is the
set of documents that define the routes to `agreed`: a self-serving change there
would propagate to every future agreement with only its author having read it.
Prompted by the pending `document-metadata-policy.md` amendment, which under
this entry routes through the full cycle. This does not unwind the agreement of
`policies/decision-log-policy.md` under DEC-000020 — that document states a
working-practice obligation (consult the log), not a route to `agreed`, so it
falls outside the class this entry protects. Size and multi-file freedom are
retained for all other co-authored prose.
Supersedes: DEC-000020

## DEC-000040 — Doc-only cycle is single-document; multi-file override withdrawn
Date: 2026-08-06
Decision: Supersedes DEC-000030. The doc-only cycle overrides the expedited
path's ≤10-line body cap for co-authored documents — a co-authored document may
be any size — but does not override the single-in-scope-file rule: a doc-only
agreement covers exactly one in-scope document, as the expedited path does.
Several documents co-authored in one session are agreed as separate, sequential
agreements. The gate/enforcement-doc exclusion carried by DEC-000030 stands
unchanged: documents that state a gate, a hard stop, or an enforcement rule
governing how work is reviewed, agreed, or released reach `agreed` only through
the full reviewer-gated cycle, even when co-authored.
Context: DEC-000030 also overrode the single-file rule, letting one content
commit agree multiple documents under one shared content SHA. The cycle-11
re-gate of `document-metadata-policy.md` (finding B1) found the shared SHA
defeats the single-entry pointer resolution `### The record` relies on —
`bin/flip-agreed` / `bin/aimeta/expedited.py` match a `last-reviewed` pointer on
SHA alone, so document B's pointer is satisfied by document A's entry: a false
claim of review in the one case the SHA is deliberately shared. Rather than make
the checker path-aware (a `bin/` change), the single-file rule is restored; size
freedom is retained.
Supersedes: DEC-000030
