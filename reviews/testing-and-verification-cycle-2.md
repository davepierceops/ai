# Review: context-sets/testing-and-verification.md — cycle 2

Verdict: changes-required
Reviewed: context-sets/testing-and-verification.md @ 2b9c856
Baseline: cceef9a (cycle 1 reviewed state, changes-required)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter and all ten surviving body sections. Three
passes. (a) All ten cycle-1 findings checked against the current text, verified
by running `git diff cceef9a 2b9c856 -- context-sets/testing-and-verification.md`
and by reading. All ten resolved, none overridden. T1 — the five class
definitions are deleted, §Verification classes now opens "What each class does
and does not support. The classes themselves are defined in the lexicon," the
useful-for / does-not-prove tables are intact, and both drift points survive in
LEXICON.md's Evidence classes (Live-verified keeps "or deploy-like service",
Production-verified keeps "logs"), which is the reconciliation T1's Fix required
under Core rule 13. T2 — the five-question form is kept and context-sets/base.md
is deleted, so only one copy of the mock checklist remained against the file
cycle 1 compared it to; a second copy against a *different* file is T11 below,
which is the same defect at a new pair, not a regression on T2. T3 — §What green
means is deleted; grep returns zero backticked repo-relative paths in the file.
T4 — the ledger example is rewritten domain-neutral ("External API client parses
a valid provider response", "The results view renders the returned records",
"Component test in a headless DOM"), and grep returns zero occurrences of
"jsdom", "TileLayer", or any vendor, product, or tool name; the matching
anti-pattern now reads "treating a headless DOM as browser rendering". T5 — the
three restated anti-patterns are deleted, five remain. T6 — :198-199 carries the
relation clause verbatim in substance: "This is the verification-specific
expansion of the Evidence, Boundary, and Gaps elements of the standard response
shape, not a second shape." T7 — Top K has a LEXICON.md entry. T8 — :11 reads
"Rules for execution sessions." T9 — `order: 5` added, the three unread
frontmatter fields dropped. T10 — LEXICON.md's Track entry gained a carve-out;
this file's :127 site is inside it, and what the carve-out still leaves open is
reported at reviews/LEXICON-cycle-12.md L11, not here. (b) All ten rubric
criteria (docs/global-context/review-rubric.md @ 2b9c856) re-applied to the
current text; criteria 1, 3, 4, 7, and 8 all move from fail or partial to pass on
this file's own text. (c) All nine in-scope files cross-checked against each
other for a term or rule stated twice. This is the pass cycle 1 could not run:
its Not-inspected line records that the SLO and error-budget material "was read
but not checked against" the boundary documents, and
policies/verification-boundary-policy.md — the file those boundary documents
were merged into — is in scope for the first time this cycle. Both findings
below come from that pass, and both are against that one file.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, context-sets/spec-and-change-discipline.md,
context-sets/production-grade-software.md, boundaries/human-review-boundary.md,
policies/verification-boundary-policy.md, policies/source-of-truth-policy.md
@ 2b9c856; the cycle-12 revision directive (the retain-with-changes disposition
and the Evidence-classes home); reviews/base-cycle-1.md B5 (the single-home
recommendation T1 turned on).
Not inspected: the rubric was applied, not reviewed. The confidence ledger
example's factual accuracy was not tested — cycle 1 made the same exclusion, and
the rewrite changed the domain, not the claims' truth. Whether the eight
evidence terms are used correctly in reviews/, retros/, and roles/ — that sweep
was not run in cycle 1 and was not run here. Files outside the nine, including
whether the useful-for / does-not-prove tables agree with roles/ documents that
consume them. The Top K uses at :125-126 and :190 were checked against
LEXICON.md's Service levels entry and agree; whether they agree with
specs/trd-template.md was not checked. No bundler was run;
`bin/bundle-methodology` was read and neither includes this path nor consumes
`order:`. The directive's excluded items were not assessed.
Findings: 2 — 1 blocking, 1 non-blocking
Prior cycle: reviews/testing-and-verification-cycle-1.md
Dave should inspect: T11 — the mock-boundary checklist is now stated in this
file and in policies/verification-boundary-policy.md at different lengths, with
the release-gap question binary in one and three-valued in the other. This is
T2's defect at a new pair, and the same call is owed: which file is the home.
The recommendation below differs from T2's, because the policy's copy carries an
item this file's does not.

## T11 — blocking
Claim: §Core principle's mock checklist is stated again in
policies/verification-boundary-policy.md §Policy statement, at six items instead
of five, and the two versions disagree on the release-gap question — binary
there, three-valued here.
Location: context-sets/testing-and-verification.md:22-31
Evidence: Verified by reading both @ 2b9c856, item for item. This file :25-31,
under "Every mock should make the boundary visible:" — 1. What production
behavior is being represented? 2. What does this test verify? 3. What does this
test not verify? 4. Where is the missing side verified? 5. If not verified, is
that gap blocking, deferred, or accepted?
policies/verification-boundary-policy.md:29-36, under "the agent must be able to
answer:" — 1. What production behavior is represented? 2. What did the evidence
verify? 3. What did the evidence not verify? 4. What verification is required
elsewhere? 5. Does the gap block release? 6. Who or what owns the follow-up?
Items 1 through 4 are the same obligation in near-identical words. Item 5 is not:
this file offers three outcomes, the policy offers two. Item 6 has no counterpart
here. The aphorism above each list differs too — this file's display quote "A
mock is a claim with a deferred proof" against the policy's ":22-23" sentence "A
mock is a claim about our side of the contract, with the other side verified
elsewhere or explicitly accepted as unverified", which the cycle-12 decision
added. Verified by running grep: both files carry `audience: [all-roles,
human]`, so both are selected into the same bundles. Verified by reading the
policy against itself: its own §Release impact labels at :115-120 is
four-valued — `blocking`, `deferred`, `accepted-risk`, `not-material` — so its
binary item 5 contradicts a list nine lines below it in the same file.
Consequence: This is precisely the defect T2 recorded and cycle 12 closed by
deleting context-sets/base.md's copy: an agent given both cannot tell whether
the mock disclosure requirement is five items or six, and the two versions
disagree on the shape of the answer to the release-gap question. T2's reasoning
about which copy is right applies unchanged — the three-valued form is the one
that matches this repo's own vocabulary, because LEXICON.md's Evidence classes
defines "Accepted risk" and "Deferred verification" as classes distinct from a
blocking gap. So the binary copy is the wrong one, and it is the copy in the
file that defines the release-impact labels. An agent that answers the policy's
item 5 with "no" has said nothing about whether the gap is deferred with a named
mechanism or accepted, which is the distinction the release requirement at
:179-188 of that same policy then demands.
Fix: One home, and on the merits it is the policy — it is the file that defines
the boundary declaration, owns the label vocabulary, and carries the ownership
question this file lacks. Move item 6 nowhere and adopt this file's item 5 there:
policies/verification-boundary-policy.md:33 becomes "If not verified, is that gap
blocking, deferred, or accepted?", which also removes its internal contradiction
with :115-120. Then delete this file's :25-31, keeping the display quote at :24,
which is the compressed form the section is built on and is stated nowhere else.
If the call goes the other way, the policy's item 6 has to come here and the
policy's §Policy statement question list goes.
Related: T12

## T12 — non-blocking
Claim: §Boundary-sensitive areas and policies/verification-boundary-policy.md
§Boundary types are two overlapping enumerations of the same suspects, one item
of which is stated near-identically in both; and the file's anti-pattern about
live tests restates that policy's CI expectation.
Location: context-sets/testing-and-verification.md:173-194 and :228
Evidence: Verified by reading both @ 2b9c856. This file lists sixteen areas to
treat as boundary-sensitive by default; the policy at :80-97 lists sixteen
"common boundary types". Nine pairs map: external APIs / mocked HTTP APIs; auth
and authorization / mocked authentication + mocked authorization; browser-only
behavior / mocked browser APIs; maps, tiles, geolocation, and rendering
libraries / mocked map/tile providers + mocked geolocation; service workers and
PWA offline behavior / mocked service workers; storage and persistence / mocked
storage; time, timers, and scheduling / mocked time; environment variables /
local environment variables replacing deployed secrets/config. One is not a pair
but the same entry twice: this file :190-191, "SLO targets and error budget
state — production signals that tests cannot capture; error budget exhaustion is
a release-relevant condition", against the policy :97, "SLO targets and error
budget state not yet connected to production monitoring". Separately, this
file's anti-pattern at :228 — "adding live tests to every unit run" — is the
policy's :153 rule stated as a prohibition: "Live/browser checks should normally
be separate from the default unit suite."
Consequence: Lower weight than T11 because the two lists are differently cut and
do not contradict — one names areas where claims are easy to overstate, the
other names mechanisms that stand in for production — so an agent given both
gets a longer list, not a conflicting one. The cost is that a reader looking for
"what should I treat as a boundary?" finds two answers of sixteen items each in
one bundle and has no way to tell whether the second is a refinement, a
superset, or a competing taxonomy; and any future addition has to be made twice,
which the duplicated SLO entry already shows going differently in each copy.
Fix: State the relation, or merge. The cheapest form that keeps both: this
file's list is areas, the policy's list is representation mechanisms, and one
clause in each saying so removes the ambiguity — the same move T6 made for the
response-shape overlap and which is already proven in this file at :198-199. If
a merge is preferred instead, the policy is the home for the mechanism list and
this file keeps the areas, with its duplicated SLO entry cut in favour of the
policy's. The :228 anti-pattern stands either way; it is a prohibition addressed
to an agent, where the policy's :153 is an expectation addressed to a suite, and
that distinction is worth the line.
Related: T11
