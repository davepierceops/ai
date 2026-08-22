# Review: LEXICON.md — cycle 12

Verdict: ready-with-findings
Reviewed: LEXICON.md @ 2b9c856
Baseline: 8d49fa8 (cycle 11 reviewed state, ready-with-findings)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter, the touch rule, and all four sections (Spec
state, Evidence classes, Service levels, Retired terms). Three passes. (a) The
cycle-11 finding and the cycle-12 decisions checked against the current text,
verified by running `git diff 8d49fa8 2b9c856 -- LEXICON.md`: L10 is resolved —
Dispatch and Sync block now carry Retired-terms entries with the replacements
cycle 6b and 6c dictated. The three cycle-12 additions all landed: Evidence
classes carries all eight terms, and the two drift points cycle 1 of
context-sets/testing-and-verification.md reported are reconciled in the
surviving copy — Live-verified keeps "or deploy-like service" and
Production-verified keeps both "deployed" and "logs", verified by reading both
former copies at cceef9a. Service levels carries Top K, closing
reviews/production-grade-software-cycle-1.md P4 and
reviews/testing-and-verification-cycle-1.md T7. The Track entry gained a
carve-out, closing T10 in substance — see L11 for what the wording leaves open.
(b) All ten rubric criteria (docs/global-context/review-rubric.md @ 2b9c856)
re-applied to the current text. Criterion 3 verified by running grep for
backticked repo-relative paths — zero; the two backticked strings are
`spec/<tranche-slug>`, a branch name, and `agreed`, a status value. Criterion 8
verified by running grep — no model names; "model tier" is the phrasing. (c) All
nine in-scope files cross-checked against each other for a term or rule stated
twice. Two results: the eight Evidence classes are defined once here and
elsewhere only used, with the single exception of
policies/verification-boundary-policy.md's Required status labels, reported
against that file at reviews/verification-boundary-policy-cycle-1.md V2 rather
than here, since this is the home cycle 12 chose. The five Spec state terms
appear nowhere else — context-sets/spec-and-change-discipline.md's Open spec
delta section is now four operating rules with the definitions removed, per S6.
Cross-checked: docs/global-context/decision-layer.md, operating-model.md,
context-sets/spec-and-change-discipline.md,
context-sets/testing-and-verification.md,
context-sets/production-grade-software.md,
boundaries/human-review-boundary.md, policies/verification-boundary-policy.md,
policies/source-of-truth-policy.md @ 2b9c856; the cycle-12 revision directive
(the Evidence-classes home, the Top K decision, and the dictated Track
carve-out).
Not inspected: the rubric was applied, not reviewed. Whether files outside the
nine still agree with the definitions here — the touch rule and their own cycles
govern that; the live uses of "dispatch" outside this scope, which cycle 11
located and deferred, were not re-surveyed. Whether the eight evidence terms are
used correctly in reviews/, retros/, roles/, and decisions/ was not swept; L11's
site list covers only the nine in scope. No bundler was run;
`bin/bundle-methodology` was read and neither includes this path nor consumes
`order:`, so bundle position is inferred from frontmatter, not observed. The
directive's excluded items were not assessed.
Findings: 2 — 0 blocking, 1 non-blocking, 1 observation
Prior cycle: reviews/LEXICON-cycle-11.md
Dave should inspect: L11 — the Track carve-out you dictated covers SRE compounds
and a verb, and the corpus's live non-retired uses are mostly a *noun*
("tracker"), including the Decision Layer's own rule 9. Widening the carve-out
is a one-line edit but it is your wording, not the reviewer's.

## L11 — non-blocking
Claim: The Track carve-out names an SRE compound and a verb, but four of the
nine in-scope files use the retired word as a *noun* in a sense the carve-out
does not reach — including the Decision Layer rule the cycle-12 decision itself
wrote.
Location: LEXICON.md:100-106 ("Track", and the carve-out that follows it)
Evidence: Verified by running `grep -niE '\b(tracks?|tracking|tracker(s)?)\b'`
over the nine files @ 2b9c856. Five files hit, at nine sites. Covered by the
carve-out as written: context-sets/testing-and-verification.md:127 ("error
budget consumption — tracking how much of the allowed failure budget has been
spent") — an error-budget compound, named explicitly. Not covered:
docs/global-context/decision-layer.md:28 ("A loose-end **tracker** is a
record, not derived state"), added by the cycle-12 decision;
operating-model.md:35, :36, :119, :174 ("**tracker** issues", "Tracker issues",
"the **tracker** issue", "`human-gate` **tracker** issue reference"), which
cycle 4 of that file reviewed and passed;
context-sets/spec-and-change-discipline.md:82 and :92 ("Proactive loose-end
**tracking**", "Surface items from the **tracker**"), kept by the cycle-12
decision; policies/source-of-truth-policy.md:22 ("They **track** and organize
work"). None of the eight uncovered sites is an SRE compound. Seven of the eight
are the noun, which the clause "the ordinary verb" excludes on its face.
Verified by reading: the carve-out is worded "*Not covered by this retirement:*
**error budget tracking**, **SLO tracking**, and similar SRE compounds, along
with the ordinary verb 'keep a list of.'" The Prompt carve-out it was told to
match names the *covered usage* ("an approval **prompt** — a tool interrupting
to ask a human to authorise a step"); this one names the *replacement* wording
instead, so it never states which use of "track" survives.
Consequence: The touch rule (L14–15) makes conforming a file to this lexicon
mandatory at its next edit, and the retired-terms sweep is how that gets applied
— it is how cycle 6's S3 and T10 were found. Run mechanically against the
current entry, that sweep flags eight sites across four governed files,
including the Decision Layer's rule 9 and operating-model.md's canonical
source-of-truth order, both of which are through Pass 1 and neither of which is
wrong. The next executor to hold the touch rule and this entry either edits four
correct files or has to decide on its own that the entry does not mean what it
says, which is the judgment call a lexicon exists to remove.
Fix: Restate the carve-out in the Prompt entry's shape — name the surviving
usage rather than its replacement. One form that covers every site above: "*Not
covered by this retirement:* **track**, **tracking**, and **tracker** in the
ordinary sense of keeping or consulting a record — a loose-end tracker, a
tracker issue, error budget tracking, SLO tracking. Those are a different word
in a different domain, and they keep their ordinary meaning." No edit is owed in
the four site files; the retired sense — a third part of a directive alongside
route and model — appears in none of the nine.
Related: L12

## L12 — observation
Claim: The file states no session kind, and it is now one of two files in scope
that does not.
Location: LEXICON.md:1-16
Evidence: Verified by reading. The frontmatter carries `status`,
`last-reviewed`, `audience`, and `order`, and no body line names a session kind.
Compare docs/global-context/decision-layer.md:10 ("Rules for decision
sessions."), operating-model.md:10, context-sets/spec-and-change-discipline.md:11,
context-sets/testing-and-verification.md:11,
context-sets/production-grade-software.md:11,
boundaries/human-review-boundary.md:9, and
policies/verification-boundary-policy.md:9-10 — seven of the nine in-scope files
now open with the declaration, six of them as a cycle-11/cycle-12 fix. The two
that do not are this file and policies/source-of-truth-policy.md, reported there
at reviews/source-of-truth-policy-cycle-1.md SOT4. Cycle 11 applied all ten
criteria to this file and passed criterion 7 without comment; the two sections
added since (Evidence classes, Service levels) are vocabulary both kinds use,
so nothing about the content has changed the answer.
Consequence: None demonstrable. A lexicon is reference rather than rules, and
the one rule it does carry — the touch rule — binds any session that edits a
file. Recorded because the corpus convention is now uniform in the other
direction across seven of nine, and the honest declaration here is "both kinds",
which is one line.
Related: L11
