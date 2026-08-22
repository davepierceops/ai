# Review: context-sets/spec-and-change-discipline.md — cycle 7

Verdict: ready-with-findings
Reviewed: context-sets/spec-and-change-discipline.md @ 2b9c856
Baseline: cceef9a (cycle 6 reviewed state, changes-required)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter and all four surviving body sections. Three
passes. (a) All twelve cycle-6 findings checked against the current text,
verified by running `git diff cceef9a 2b9c856 --
context-sets/spec-and-change-discipline.md` and by reading. Resolved: S1 — the
canonical sequence is deleted in full and the surviving hand-off at :51-53 now
reads "steps 1 through 5" and "quality review, skeptic/risk review, release
package, and release gate — steps 6 through 9", which aligns stage for stage
with operating-model.md's nine-stage flow and puts quality review inside the
continuing range, as the cycle-12 decision required; S2 — "Definition of done
(spec discipline view)" is deleted; S3 — "at handoff" replaces "at dispatch" at
:25-26, "A directive issued mid-delta derives from the spec branch" replaces the
mid-delta-dispatches heading at :67, and grep returns zero occurrences of
"dispatch" in any form; S4 — all five restated operating habits are deleted, two
bullets remain; S5 — settled by the cycle-12 decision rather than by this file:
OPEN-ITEMS.md stays, docs/global-context/decision-layer.md rule 9 gained the
carve-out sentence, and this file keeps its four checkpoints, which are not a
restatement of that carve-out; S6 — the five LEXICON.md definitions are gone and
§Open spec delta is four operating rules, with LEXICON.md's Reconciliation entry
having absorbed the two clauses S6 named; S7 — the four rationale passages are
cut, including the decomposition argument the cycle-12 commit records cutting,
and both P3 provenance parentheticals; S8 — the mechanism-cost bullet is
deleted; S10 — :11 declares both session kinds, which is S10's second branch and
is the honest call now that the Core-philosophy and habit material spanning both
kinds survives; S11 — `order: 4` added, `context-set:`, `purpose:`, and
`include-when:` dropped; S12 — the track parenthetical is deleted. Partially
resolved: S9 — twelve of the thirteen path-shaped references are gone; one
survives, reported below as S13. (b) All ten rubric criteria
(docs/global-context/review-rubric.md @ 2b9c856) re-applied to the current text.
Criterion 8 verified by running grep: zero model names, and "GitHub Issue" — the
one vendor name cycle 6 counted — is gone with the deleted §Core philosophy
line. (c) All nine in-scope files cross-checked against each other for a term or
rule stated twice; S14 is that pass's result.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, context-sets/testing-and-verification.md,
context-sets/production-grade-software.md, boundaries/human-review-boundary.md,
policies/verification-boundary-policy.md, policies/source-of-truth-policy.md
@ 2b9c856; the cycle-12 revision directive (the retain-with-changes
disposition, the OPEN-ITEMS settlement, and the step-range instruction);
`bin/bundle-methodology` (the hardcoded spine).
Not inspected: the rubric was applied, not reviewed. Whether S7's two provenance
parentheticals actually landed in retros/ or decisions/log.md as its Fix
suggested — those files are outside the nine and the move was a suggestion, not
a directive decision, so their absence here is recorded as resolved and their
arrival elsewhere is unverified. OPEN-ITEMS.md's contents were not read; S13
concerns the reference form, not what the tracker holds. The nine "track*"
occurrences across the nine files were swept and are reported against LEXICON.md
at reviews/LEXICON-cycle-12.md L11 — two of them are in this file, at :82 and
:92, and no edit is owed here. Files outside the nine, including
policies/commit-and-change-control-policy.md, whose two-tier statement bears on
S14 and which instruction 3 scopes out. No bundler was run;
`bin/bundle-methodology` was read and places this file *first* in its hardcoded
spine, ahead of operating-model.md — which is what makes S14's ordering claim
concrete, and is read from the script rather than observed in a generated
bundle. The directive's excluded items were not assessed.
Findings: 2 — 0 blocking, 2 non-blocking
Prior cycle: reviews/spec-and-change-discipline-cycle-6.md
Dave should inspect: S14 — §Core philosophy is a second copy of
operating-model.md's spec-first paragraph and its two-tier release gate, and in
the decision-layer bundle this file arrives *before* operating-model.md, so the
copy a reader meets first is the one in the file that does not own the rule.

## S13 — non-blocking
Claim: One of cycle 6's thirteen path-shaped references survives — the file's
last one, and the one S9's fix did not reach.
Location: context-sets/spec-and-change-discipline.md:82
Evidence: Verified by running grep for backticked repo-relative paths over the
current text: one hit, "- **Proactive loose-end tracking.** The loose-end
tracker `OPEN-ITEMS.md` is updated at defined checkpoints, rather than relying on
Dave to remember:". Verified by reading the governing decisions: cycle 6's S9
listed OPEN-ITEMS.md at :174 and :183 among the thirteen and its Fix directed
that the references not covered by a deletion "become prose without the
backticked path". The cycle-12 decision on this bullet settled *whether the
instruction stays* — "Context sets keep their OPEN-ITEMS instruction where it is
not a restatement of that tracker's own header" — and said nothing about the
reference form; its separate standing rule, "Any Fix that would add a
path-shaped reference: not applied", governs additions, not survivals. So S9 is
neither resolved at this site nor overridden.
Consequence: Criterion 3, and criterion 1 behind it. The rest of the file was
brought to zero path-shaped references, so a mechanical sweep of the corpus
still returns this file. The concrete cost is in an adopting project: the bundle
instructs the agent to update a tracker at a fixed repository path, and in a
project that has no OPEN-ITEMS.md the instruction names a file that does not
exist, with no statement of what the artifact is that would let the agent
recognise or create the right one. The four checkpoints — the part of the bullet
that earns its place — do not depend on the path.
Fix: Drop the backticks and the extension: "The loose-end tracker is updated at
defined checkpoints, rather than relying on Dave to remember". The tracker is
named by convention in docs/global-context/decision-layer.md:28 ("A loose-end
tracker is a record, not derived state"), which arrives in the same decision
bundle, so nothing is lost. :92's "Surface items from the tracker" already uses
the reference-free form.

## S14 — non-blocking
Claim: §Core philosophy restates operating-model.md's spec-first paragraph and
its two-tier release gate, in a file the decision-layer bundle loads first.
Location: context-sets/spec-and-change-discipline.md:16-36
Evidence: Verified by reading both @ 2b9c856, sentence by sentence. Three pairs.
(i) This file :18-21 — "Development is **spec-first** and **test-driven**.
Nothing is built that is not specified: the spec and its acceptance criteria
exist, and are correct, at the moment work is handed to an executor. Tests are
written before implementation." operating-model.md:20 — "Work is **spec-first**
and **test-driven**: nothing is built that is not specified with written
acceptance criteria, and tests are written and confirmed failing before
implementation." (ii) This file :23-24 — "**Spec-first is a truth requirement,
not an approval sequence.** The rule is that the spec is true **at handoff** and
true **at rest**". operating-model.md:20, second sentence — "Spec-first is a
requirement that the spec be *true* at handoff and at rest — not that every
sentence was agreed before it was written; agreement lands at reconciliation."
(iii) This file :32-36 — "Those decisions are spec agreement and the release
decision for the consequential class. Everything between them is the routine
class: agents execute it, review it, and merge it autonomously once the evidence
exists. The gate anchors at the release decision, not at landing."
operating-model.md:134-146 §Release gate — "The human gate is the **release
decision**, not a code decision and not the commit… **Routine changes** flow to
release on evidence… **Consequential changes** require the human's explicit
go/no-go at the release decision." Cycle 6's Counts block recorded both
restatements ("Core philosophy 2") but no cycle-6 finding carried a Fix for
them: S1 addressed the canonical sequence, S2 the definition of done, S4 the
operating habits. So this is unresolved rather than re-opened. Verified by
running: `bin/bundle-methodology`:25-30 carries a hardcoded spine whose first
entry is this file and whose second is operating-model.md.
Consequence: The copies agree, so no agent is given contradictory instruction
and nothing stops — which is why this is non-blocking. The costs are two. First,
about twenty of this file's hundred and four lines duplicate the spine document,
in a bundle both files land in. Second, and the reason it is worth an edit
rather than a shrug: the spine loads this file first, so the reader meets the
spec-first rule and the two-tier gate here, in the file whose criterion-10 case
rests on three other sections entirely — the behavioral red-gate, the open-delta
operating rules, and the derived-fields checklist. A future change to the tiers
has to find this copy, and Core rule 13 makes that obligation real.
Fix: Delete :18-21 and :32-36; operating-model.md states both, and states the
gate more fully. Keep :23-27 — the truth-requirement framing with the amnesiac-
executor sentence — only if it is cut to the half operating-model.md does not
carry: the sentence "What generates the truth requirement is the amnesiac
executor: a session holds nothing but the documents it is given, so those
documents must be right at handoff" is stated nowhere else and is what makes the
rule usable. The display quote at :29-30 is likewise unique and stands. That
leaves §Core philosophy at roughly five lines, all of it additive.
Related: S13
