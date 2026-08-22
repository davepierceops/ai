# Review: docs/global-context/decision-layer.md — cycle 9

Verdict: ready
Reviewed: docs/global-context/decision-layer.md @ 8d49fa8
Baseline: cb3e75a (cycle 7 reviewed state, ready)
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: the full file — frontmatter, preamble, and all fifteen rules. Two
passes: (a) the cycle-8 revision decision touching this file checked against
the current text — the preamble is the three dictated sentences exactly, scope
only, carrying no definition; verified by running `git diff cb3e75a 8d49fa8`,
which shows the preamble line as this file's only change, and the clause it
lost ("that work happens in an execution session") arriving in Core's Decision
session entry. The fifteen rules are untouched and still number sequentially,
and no prose in the three in-scope files cites a rule number. (b) all ten
rubric criteria (docs/global-context/review-rubric.md @ 8d49fa8) re-applied to
the current text, and the three in-scope files cross-checked for a term stated
in two places. The duplication reported as reviews/LEXICON-cycle-10.md L9 —
this preamble against the lexicon's Sessions entry — is resolved, and resolved
without creating a new one: neither surviving statement of a session kind is
in this file. Criterion 7 is satisfied more plainly than at cycle 7, since the
preamble now says what the file is for and nothing else. Criterion 4 holds
against the shortened preamble: it states scope and load position, not a rule
Core states. Rule 13 speaks in tiers with no model name, and "track" does not
appear, verified by running grep.
Cross-checked: docs/global-context/core.md @ 8d49fa8 — the definition this
preamble dropped is stated there, once, and this file declares the dependency
in its own text ("Loads after Core and adds to it"), so a reader who has Core
has the term and a reader who does not is told what is missing; LEXICON.md @
8d49fa8; the cycle-8 revision directive (the dictated preamble wording).
Not inspected: the rubric was applied, not reviewed. Files outside the three in
scope. Bundle membership and load order are inferred from frontmatter, not
observed: I read `bin/bundle` and `bin/bundle-methodology`, and neither
consumes `order:` nor includes this path, so the claim that Core precedes this
file in every decision bundle rests on the `order:` values and this file's own
declaration, not on a generated bundle. The directive's excluded items —
including that all-decision-roles is not yet a reserved audience value — were
not assessed.
Findings: none
Prior cycle: reviews/decision-layer-cycle-7.md
