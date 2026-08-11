# Review: context-sets/spec-and-change-discipline.md — cycle 2

Verdict: changes-required
Reviewed: `context-sets/spec-and-change-discipline.md` @ `7d4d03a`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: re-gate of cycle 1's B1 and B2, plus a regression check over the whole
Open spec delta section, which both fixes edited.
Cross-checked: `LEXICON.md` (Spec state; Track A / Track B),
`roles/chief-of-staff.md` (Open spec deltas),
`skills/spec-review-cycle.md` (Reconciliation).
Not inspected: the sections outside Open spec delta and Core philosophy, cleared
in cycle 1 and untouched since.
Findings: 1 blocking, 2 non-blocking
Prior cycle: `reviews/spec-and-change-discipline-cycle-1.md`
Dave should inspect: B1 — the cycle-1 fix renamed the term in the sentence the
finding quoted and left it standing three sentences later.

**Cycle 1 findings, re-checked.** B2 (the editing licence named nobody) is
**resolved**: the rule now names Dave and carries an explicit paragraph refusing
the agent reading. B1 (the `track` collision) is **partly resolved** — see B1
below.

## B1 — blocking
Claim: The cycle-1 rename missed the last sentence of the paragraph it edited,
which still reads "tracks go cross-project."
Location: `context-sets/spec-and-change-discipline.md`, Open spec delta, final
sentence of the concurrency paragraph
Evidence: **Verified by running.**
`grep -n '\btracks\?\b' context-sets/spec-and-change-discipline.md` at `7d4d03a`
returns the fixed opening ("at most two tranches execute concurrently"), the new
parenthetical warning against the word, and — three sentences later — "Where a
project has no disjoint territory to claim, tracks go cross-project, or the work
goes serial."
Consequence: The paragraph now warns against a word it then uses, in the same
breath, for the sense it warned against. That is worse than the original defect:
a reader who trusts the parenthetical reads the final sentence as being about
Track A and Track B. It is also the precise failure this document's own
"Document consistency" habit names — a value updated in one place and stale in
another.
Fix: "the second tranche goes cross-project."

## N1 — non-blocking
Claim: Two paragraphs edited in cycle 1 have broken line wrapping — a four-word
line mid-paragraph where the file otherwise wraps at ~80 columns.
Location: `context-sets/spec-and-change-discipline.md`, concurrency paragraph
Evidence: Verified by reading the raw file at `7d4d03a`: "second delta. The" and
"edits is exactly the" each terminate a line early.
Consequence: Cosmetic in rendering, but the diff of any future edit to these
paragraphs will be noisier than the change it carries, which is a real cost in a
repo where the diff is a control surface.
Fix: Rewrap both paragraphs.

## N2 — non-blocking
Claim: Cycle 1's fix to `skills/spec-review-cycle.md` clarified what "once, as a
single cycle" quantifies; this document restates the phrase without the
clarification.
Location: `context-sets/spec-and-change-discipline.md`, "Reconciliation closes
the delta"
Evidence: Verified by reading both at `7d4d03a`. The skill now says the delta is
gated once "as against once per edit — not that a reconciliation may run only one
cycle." This document, which is the canonical statement of the delta rules, says
only "once, as a single cycle".
Consequence: The ambiguity that produced a blocking finding in the skill survives
at the site a reader is more likely to hit first — this document is a context set
loaded by `include-when`, and the skill is opened deliberately.
Fix: "once — once per delta, not once per edit". Same correction at `LEXICON.md`.
Related: `reviews/LEXICON-cycle-5.md` N1
