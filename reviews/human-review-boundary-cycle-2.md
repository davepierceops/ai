# Review: boundaries/human-review-boundary.md — cycle 2

Verdict: ready-with-findings
Reviewed: boundaries/human-review-boundary.md @ 2b9c856
Baseline: cceef9a (cycle 1 reviewed state, changes-required)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter and both surviving sections. Three passes.
(a) All nine cycle-1 findings checked against the current text, verified by
running `git diff cceef9a 2b9c856 -- boundaries/human-review-boundary.md` and by
reading. All nine resolved as decided; none was overridden. B1 — §Required
replacement controls is deleted in full, so the eight-item control list no
longer competes with operating-model.md §Control surfaces. B2 — §Policy and its
heading are deleted. B3 — the line restating the standing no-line-by-line claim
is deleted, and §Summary now opens on the sentence B3's Fix directed be kept and
reworded: "This is a boundary, not an absence of review." B4 — the parenthetical
path reference is deleted; grep over the current text returns zero backticked
repo-relative paths. B5 — §Human review includes and §Human review does not
default to are deleted, twenty-two lines of description of a human's habits. B6
— :9 reads "Rules for decision sessions."; the audience narrowing B6's Fix
flagged was explicitly deferred to a metadata-policy scope change, and the
directive's instruction 4 scopes it out of this cycle, so it is not reported. N1
— §Core principle is deleted. N2 — both statements of the Spec Reviewer gate
fall out with the B1 and B5 deletions, as its Fix anticipated. O1 — an
observation with no demonstrable consequence; no `order:` was added and none is
owed, since after the cuts nothing here depends on being read before or after
another file. The file went from roughly eighty lines to thirty-seven, and what
survives is exactly the two things cycle 1's criterion-10 disposition said earn
the place. (b) All ten rubric criteria (docs/global-context/review-rubric.md @
2b9c856) re-applied to the current text: criteria 1, 3, 4, and 7 move from fail
to pass, and criterion 6 passes — the surviving §Summary states scope rather
than arguing for it. (c) All nine in-scope files cross-checked against each
other for a term or rule stated twice; O3 is that pass's one result, and the
eight escalation triggers at :29-36 appear in none of the other eight files.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, context-sets/spec-and-change-discipline.md,
context-sets/testing-and-verification.md,
context-sets/production-grade-software.md,
policies/verification-boundary-policy.md, policies/source-of-truth-policy.md
@ 2b9c856; the cycle-12 revision directive (the retain-with-changes
disposition).
Not inspected: the rubric was applied, not reviewed. Cycle 1's exclusion stands
unchanged — the eight escalation triggers were not tested against any real
change, and whether roles/reviewer-agent.md and roles/skeptic-risk-agent.md
actually deliver the agent review §Summary asserts still happens was not
verified; that claim remains inherited from operating-model.md rather than
independently checked. policies/commit-and-change-control-policy.md, which
cycle 1 found points *here* for the control-surface axis, is outside the nine
and was not re-read, so whether the pair is still coherent after this file lost
half its text is unassessed — it is the obvious next place to look. Files
outside the nine were not read. No adopting project repo was exercised. Whether
Dave wants the escalation list at all — the sole basis for the retain call — is
his judgment and is not settled here. No bundler was run.
Findings: 2 — 0 blocking, 0 non-blocking, 2 observations
Prior cycle: reviews/human-review-boundary-cycle-1.md

## O2 — observation
Claim: The surviving escalation section is framed as a statement about what a
human may do, not as an instruction to the agent reading it.
Location: boundaries/human-review-boundary.md:27-36
Evidence: Verified by reading. The section's operative line is "A human may
choose to inspect code directly when:", followed by eight conditions. Rubric
criterion 5 requires every rule to be an instruction to the agent reading it.
Cycle 1 marked criterion 5 "fail — B5" and B5's Location was :23-44 — the two
sections describing Dave's reading habits — so this section was outside B5's
scope and was passed; B5's Fix explicitly preserved it, and cycle 1's
criterion-10 disposition rests on it. So this is not a regression and no prior
decision is unresolved. The framing objection B5 raised nevertheless applies to
it in weaker form: the subject of the sentence is a human, not the reader.
Consequence: None demonstrable, which is why this is an observation. The
conditions are operable — operating-model.md:220 instructs the agent to escalate
when "human code inspection is warranted" and states no criteria, so this list is
what the agent applies to decide whether that trigger is met, and it functions
whichever way the sentence is turned. Recorded because the fix is one clause and
because criterion 5 is the criterion this file failed hardest at cycle 1.
Fix: If wanted: "Escalate for human code inspection when:" — which names the
agent's action, matches operating-model.md's escalation vocabulary, and leaves
the eight conditions untouched.
Related: O3

## O3 — observation
Claim: The first half of the two-axes distinction is also stated by
operating-model.md §Release gate.
Location: boundaries/human-review-boundary.md:20-24
Evidence: Verified by reading both @ 2b9c856. This file: "It is a separate axis
from the release gate — the release go/no-go is an evidence-and-judgment
decision, not a code-reading decision. A change can be in the consequential
class (needs a human release go/no-go) without anyone reading its diff, and vice
versa." operating-model.md:135-136: "The human gate is the **release decision**,
not a code decision and not the commit (see "Source of truth")." The shared
proposition is that the release gate is not a code-reading decision. Cycle 1
established the two-axes distinction as this file's criterion-10 justification
by comparing it to policies/commit-and-change-control-policy.md:15-21; it did
not compare it to operating-model.md §Release gate, and that section is in scope
this cycle.
Consequence: None demonstrable. The overlap is one clause, the two statements
agree, and the sentence that follows it here — the bidirectional independence
claim, that a consequential change can ship with no diff read and a routine one
can still be read — is stated in neither operating-model.md nor any other of the
nine, and is the half that does the work. Recorded so that a future edit to
either sentence knows the other exists, per Core rule 13, and so the
criterion-10 case for this file is on the record as resting on the independence
claim rather than on the shared clause.
Fix: None owed. If the clause is cut for economy, the independence sentence
stands on its own and must be kept.
Related: O2
