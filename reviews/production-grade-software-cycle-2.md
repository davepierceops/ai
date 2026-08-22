# Review: context-sets/production-grade-software.md — cycle 2

Verdict: ready
Reviewed: context-sets/production-grade-software.md @ 2b9c856
Baseline: cceef9a (cycle 1 reviewed state, ready-with-findings)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter and all three surviving body sections. Three
passes. (a) All six cycle-1 findings checked against the current text, verified
by running `git diff cceef9a 2b9c856 -- context-sets/production-grade-software.md`
and by reading: P1 — the Summary that restated operating-model.md's Operating
standard is deleted, replaced by the single framing sentence P5's fix released
from the dropped `purpose:` field; P2 — "Production-grade does not mean" is
deleted in full; P3 — "Rules for execution sessions." is the line after the H1;
P4 — "Top K" now has a LEXICON.md entry under Service levels, and the
per-project list stays in the PRD as specs/trd-template.md requires; P5 —
`order: 6` added, `context-set:`, `purpose:`, and `include-when:` dropped; P6 —
all three list-introducing sentences are imperative ("is assessed against", "is
supported by evidence such as", "answers"), and L34 is unchanged. All six
resolved as decided; none was overridden. (b) All ten rubric criteria
(docs/global-context/review-rubric.md @ 2b9c856) re-applied to the current text.
Criterion 3 verified by running grep for backticked repo-relative paths — zero,
unchanged from cycle 1. Criterion 8 verified by running grep for vendor, product,
tool, and model names — zero. Retired terms verified by running grep — zero.
(c) All nine in-scope files cross-checked against each other for a term or rule
stated twice. This file states nothing another of the nine states: the
fifteen-attribute list with its explicit-relevance instruction, the eleven
evidence *kinds*, and the six failure-mode questions have no counterpart, and
the three sites where this file and
context-sets/testing-and-verification.md both touch SLO and error-budget
material sit in three different list types — an attribute, a boundary-sensitive
area, and a report field — rather than being one rule stated twice.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, context-sets/spec-and-change-discipline.md,
context-sets/testing-and-verification.md, boundaries/human-review-boundary.md,
policies/verification-boundary-policy.md, policies/source-of-truth-policy.md
@ 2b9c856; the cycle-12 revision directive (the retain-with-changes
disposition).
Not inspected: the rubric was applied, not reviewed. Whether the fifteen
attributes are the right fifteen, or the eleven evidence kinds the right eleven
— cycle 1 declined that claim and this cycle does not reopen it; the review
tests placement and duplication, not completeness of a domain checklist. Files
outside the nine in scope, including whether the SLO and error-budget machinery
in roles/ agrees with this file's use of it. `depends-on: []` survives as an
empty field consumed by `bin/bundle`; it creates no edge and no consequence was
identified, so no entry is opened. No bundler was run; `bin/bundle-methodology`
was read and neither includes this path nor consumes `order:`, so bundle
position is inferred from frontmatter, not observed. The directive's excluded
items were not assessed.
Findings: none
Prior cycle: reviews/production-grade-software-cycle-1.md
