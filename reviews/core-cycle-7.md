# Review: docs/global-context/core.md — cycle 7

Verdict: ready
Reviewed: docs/global-context/core.md @ cb3e75a
Baseline: 089083c (cycle 4 reviewed state)
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: the full file — frontmatter, all fourteen rules, and the Vocabulary
section. Two passes: (a) the cycle-6, 6b, and 6c decisions touching this file
checked against the current text — the Vocabulary section exists after "Acting"
carrying the entries moved from LEXICON (cycle-6 L1); the Sync block entry is
deleted (6b V1) and the Execution block and Directive entries carry the
dictated 6b V2/V3 wording, with V3's "stated like any other dispatch" rewritten
to "still stated in full each time" under 6c's plain-terms rule; the Dispatch
entry is deleted and zero occurrences of dispatch remain, verified by running
grep; (b) all ten rubric criteria (docs/global-context/review-rubric.md @
cb3e75a) re-applied to the current text, and the five in-scope files
cross-checked for a term stated in two places — nothing this file states is
stated elsewhere in the five; the one live sync-block/dispatch residue in the
scope is in LEXICON, reported there.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, engagements/working-with-dave.md @ cb3e75a (cross-file
term check); the cycle-6, 6b, and 6c directives (dictated wording and the rule
in force).
Not inspected: the rubric was applied, not reviewed. Files outside the five in
scope were not swept for the terms Core's Vocabulary now owns — their stale
usages are their own cycles. No bundler was run; every claim about bundle
membership or load order is inferred from frontmatter, not observed from a
generated bundle. The directive's excluded items were not assessed.
Findings: none
Prior cycle: reviews/core-cycle-4.md
