# Review: operating-model.md — cycle 4

Verdict: ready
Reviewed: operating-model.md @ cb3e75a
Baseline: 28d11fa (cycle 3 reviewed state)
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: the full file. Two passes: (a) O1–O7 checked against the cycle-6
decisions — O1: the lines restating Core 2, 3, 5, 7, and 9 are deleted,
verified by running grep for each flagged phrase, and the entries with no Core
counterpart (state assumptions; the mocked/contract/live/browser/production
distinction; weaken-verification; mocked-evidence; vendor-tooling) survive;
O2: zero path-shaped references, verified by running grep, and "README #5" is
gone; O3: the Trust model section is cut and the evidence-class vocabulary is
not restated; O4: "tracker issues (currently GitHub Issues)", the vendor named
once; O5: the two-question sentence is kept and the three rationale tails are
cut; O6: the session-scope line opens the file; O7: order: 3. All seven
resolved as decided. (b) all ten rubric criteria
(docs/global-context/review-rubric.md @ cb3e75a) re-applied to the current
text, and the five in-scope files cross-checked for a term stated in two
places — the meaningful-change definition, change flow, release-gate tiers,
change package, definition of done, and escalation triggers are stated nowhere
else in the five.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md,
LEXICON.md, engagements/working-with-dave.md @ cb3e75a.
Not inspected: duplication against policies/* and context-sets/* — notably
whether the release-gate tiers and the commit policy state the same tiers
twice — unchanged from cycle 3 and deferred to those files' cycles. The rubric
was applied, not reviewed. No bundler was run; bundle membership and load
order are inferred from frontmatter, not observed. The directive's excluded
items were not assessed; the README stale pointer the frontmatter check warns
on was observed and, per the directive, not reported.
Findings: none
Prior cycle: reviews/operating-model-cycle-3.md
