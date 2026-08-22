# Review: docs/global-context/decision-layer.md — cycle 10

Verdict: ready
Reviewed: docs/global-context/decision-layer.md @ 2b9c856
Baseline: 8d49fa8 (cycle 9 reviewed state, ready)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter, preamble, and all sixteen rules. Three
passes. (a) The two edits since baseline checked against the decisions that
ordered them, verified by running `git diff 8d49fa8 2b9c856 --
docs/global-context/decision-layer.md`: the cycle-12 decision added the
loose-end-tracker carve-out to rule 9 ("A loose-end tracker is a record, not
derived state"), and the cycle-13 decision added rule 10 under "State and
record", immediately after the loose-end-tracker rule, carrying the dictated
sentence verbatim — "Before recommending or encoding anything an existing
decision may govern, read the decision log and cite the governing entry by ID."
Rules renumbered 10→11 through 15→16; the sequence 1–16 is unbroken, verified by
reading, and no prose in the nine in-scope files cites a Decision Layer rule by
number, verified by running grep. (b) All ten rubric criteria
(docs/global-context/review-rubric.md @ 2b9c856) re-applied to the current text.
Criterion 3 verified by running grep for backticked repo-relative paths — zero.
Criterion 8 verified by running grep — rule 14 speaks in tiers (frontier / solid
general-purpose / cheap) with no model name, and "track" does not appear as the
retired term. (c) All nine in-scope files cross-checked against each other for a
term or rule stated twice. Nothing in this file is stated by another of the
nine: rule 9's tracker sentence and
context-sets/spec-and-change-discipline.md's OPEN-ITEMS checkpoints are the
two halves the cycle-12 decision deliberately split, not two copies of one rule,
and rule 10's obligation appears in none of the other eight.
Cross-checked: LEXICON.md, operating-model.md,
context-sets/spec-and-change-discipline.md,
context-sets/testing-and-verification.md,
context-sets/production-grade-software.md,
boundaries/human-review-boundary.md, policies/verification-boundary-policy.md,
policies/source-of-truth-policy.md @ 2b9c856; the cycle-12 and cycle-13 revision
directives (the dictated wording and the placement instruction).
Not inspected: the rubric was applied, not reviewed. Files outside the nine in
scope — notably policies/decision-log-policy.md, which rule 10's "the decision
log" leans on: it exists and carries `audience: [all-roles, human]`, verified by
reading, but whether its statement of the log's shape agrees with rule 10 was
not checked, and instruction 3 scopes the duplication sweep to the nine. Bundle
membership and load order are inferred from frontmatter and from reading
`bin/bundle-methodology`, not observed; that script carries a hardcoded spine
that does not include this path and consumes no `order:`, so no generated bundle
was produced to read against criterion 1. Rule 9's "tracker" was swept against
LEXICON.md's Track retirement and is reported there, at
reviews/LEXICON-cycle-12.md L11, not here — no edit is owed in this file. The
directive's excluded items, including that all-decision-roles is not yet a
reserved audience value, were not assessed.
Findings: none
Prior cycle: reviews/decision-layer-cycle-9.md
