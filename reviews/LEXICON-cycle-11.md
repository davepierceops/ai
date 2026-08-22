# Review: LEXICON.md — cycle 11

Verdict: ready-with-findings
Reviewed: LEXICON.md @ 8d49fa8
Baseline: cb3e75a (cycle 10 reviewed state, changes-required)
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: the full file. Two passes: (a) L8 and L9 checked against the current
text — L8: the Prompt entry's shell bullet is now "**What runs in a shell** —
a *command block*." with the dispatch/sync-block clause cut, and zero
occurrences of either word remain in the three in-scope files, verified by
running grep; L9: the Sessions section is deleted, both entries are in Core's
Vocabulary placed first, the two qualifying paragraphs moved with them, and
the decision-layer preamble's clause is folded into Core's Decision session
entry — verified by running `git diff cb3e75a 8d49fa8`. Both resolved as the
cycle-8 directive decided. The remaining sections are Spec state and Retired
terms; the directive's expected list also named "Tranche", which is a term
inside Spec state and was never a section of this file, so that is a wording
slip in the expectation, not a missing section. (b) all ten rubric criteria
(docs/global-context/review-rubric.md @ 8d49fa8) re-applied to the current
text, and the three in-scope files cross-checked for a term stated in two
places. No term is defined twice: the five spec-state terms appear nowhere
else, and the Retired terms bullets point at Core's terms rather than
redefining them. "Prompt" is addressed here and in Core's Vocabulary, but
Core states the rule (use the artifact's name) and this file supplies which
name, so the pair is complementary and criterion 4 is not engaged; the
approval-prompt carve-out qualifies this file's own retirement, not Core's
rule, so Core's precedence sentence is not in play. Zero path-shaped
references, verified by running grep. The finding below is from pass (b).
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md
@ 8d49fa8; the cycle-8 revision directive (the dictated L8/L9 decisions) and
the cycle-6b and 6c directives (the decisions that retired sync block and
dispatch).
Not inspected: the rubric was applied, not reviewed. Whether files outside the
three in scope still agree with the definitions here — the touch rule and
their own cycles govern that; the live uses of "dispatch" outside this scope
were located but not assessed. Bundle membership and load order are inferred
from frontmatter, not observed: I read `bin/bundle` and `bin/bundle-methodology`,
and neither consumes `order:` nor includes this path, so no bundler assembles
these three files today and no generated bundle was produced to read against
criterion 1. The directive's excluded items were not assessed.
Findings: 1 non-blocking
Prior cycle: reviews/LEXICON-cycle-10.md
Dave should inspect: whether Retired terms is the home for the dispatch and
sync-block retirements, given cycle 6c's "No entry is added in its place"; and
whether the touch rule's "this lexicon" is still the reach he wants now that
the session and artifact vocabulary lives in Core.

## L10 — non-blocking
Claim: Retired terms records the retirement of "prompt" only — "sync block"
and "dispatch", retired by the cycle-6b and 6c decisions, are named nowhere a
reader of this file can see, and cycle 8 removed this file's last mention of
both.
Location: LEXICON.md:41-61 ("Retired terms")
Evidence: verified by running grep over the three in-scope files @ 8d49fa8 —
zero occurrences of either word; `git diff cb3e75a 8d49fa8` shows the only
occurrence, the Prompt entry's shell bullet, cut by L8 as decided, and that
clause used both words as live terms rather than recording their retirement,
so this file has never carried the retirement. The decisions themselves live
in the cycle-6b directive (Core's Sync block entry deleted) and the cycle-6c
directive ("'Dispatch' is retired... No entry is added in its place"), neither
of which is a governed document a bundle reader receives. Verified by running
`git grep`: the word is still live outside this scope in OPEN-ITEMS.md,
context-sets/spec-and-change-discipline.md, context-sets/ai-native-engineering.md,
decisions/log.md, and BACKLOG-v2.md, and skills/directive-dispatch.md carries
it in its filename — the set cycle 6c called "the other fourteen governed
files using the word" and deferred to later cycles.
Consequence: the touch rule is this repo's mechanism for propagating
vocabulary — "any file edited for another reason is conformed to this lexicon
as part of that edit" — and after cycle 8 this lexicon retires exactly one
word. An agent editing one of those deferred files, holding only a bundle, has
no instruction that "dispatch" or "sync block" is retired and no statement of
what to write instead, so the touch rule passes the file unchanged and each
deferred file needs its own directive dictating the replacement. That is the
cost cycles 6b, 6c, and 8 have now paid three times for these two words.
Fix: add both to Retired terms with the replacements already dictated — cycle
6c fixed "hand the directive to an execution session", "direct", or whichever
reads naturally in place, and cycle 6b abolished the sync block outright, so
that entry states no replacement. This is Dave's call, not the reviewer's:
cycle 6c's "No entry is added in its place" governed the Vocabulary entry in
Core, and whether it also forecloses a Retired-terms entry here — an entry
that says do not use this word, rather than one that defines it — has not been
decided. No edit until it is.
