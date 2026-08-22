# Review: docs/global-context/core.md — cycle 9

Verdict: ready
Reviewed: docs/global-context/core.md @ 8d49fa8
Baseline: cb3e75a (cycle 7 reviewed state, ready)
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: the full file — frontmatter, all fourteen rules, and the Vocabulary
section. Two passes: (a) the cycle-8 revision decisions touching this file
checked against the current text — the two Sessions entries are in Vocabulary,
placed first and ahead of the three-layers statement; the decision-layer
preamble's extra detail is folded into the Decision session entry as the
trailing clause "that work happens in an execution session"; the two
qualifying paragraphs that governed those entries in their old home — the
production-system sentence and "The boundary is role in the flow, not
capability" — moved with them. Verified by running `git diff cb3e75a 8d49fa8`:
this file gained those seven lines and nothing else. (b) all ten rubric
criteria (docs/global-context/review-rubric.md @ 8d49fa8) re-applied to the
current text, and the three in-scope files cross-checked for a term stated in
two places. The one pair the move could have created is closed: the session
definitions are stated here and the Sessions section is deleted from the
all-roles lexicon, verified by running grep. "Prompt" is addressed both here
(Vocabulary: when an artifact has a name, use it) and in the lexicon's Retired
terms (which name to use instead); the two are complementary rather than a
restatement, so criterion 4 is not engaged. In its new position the "boundary
is role in the flow" paragraph earns a keep it did not need before: it is now
adjacent to "Work moves through three layers: decision — chat", and it is what
stops a reader inferring from that medium that a decision session may not hold
a clone or commit. Zero path-shaped references and zero occurrences of
dispatch, sync block, or track, verified by running grep.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md @ 8d49fa8;
the cycle-8 revision directive (the dictated L8/L9 decisions) and the cycle-6b
and 6c directives (the rule in force on sync blocks and dispatch).
Not inspected: the rubric was applied, not reviewed. Files outside the three in
scope — their uses of the vocabulary this file owns are their own cycles.
Bundle membership and load order are inferred from frontmatter, not observed:
I read `bin/bundle` and `bin/bundle-methodology`, and neither consumes `order:`
nor includes this path, so no bundler assembles these three files today and no
generated bundle was produced to read against criterion 1. The directive's
excluded items were not assessed.
Findings: none
Prior cycle: reviews/core-cycle-7.md
