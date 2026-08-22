# Review: roles/coder-agent.md — cycle 1

Verdict: changes-required
Reviewed: roles/coder-agent.md @ ed926db174887c54a701b8fc4f0a35726bdc027a
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (48 lines), against docs/global-context/review-rubric.md @ ed926db, all ten criteria.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ ed926db); roles/test-designer-agent.md on the separation rule; skills/change-package-creation.md as a bundle-mate; reviews/agent-review-policy-cycle-1.md finding A2; the bundle-mate set computed from `audience:` frontmatter across the repository.
Not inspected: policies/commit-and-change-control-policy.md as a document in its own right — read only far enough to confirm the path at :39 resolves and that it is not in this bundle; skills/change-package-creation.md against its own criteria; whether `bin/bundle` in fact composes the bundle this review reasons about — audience selection is not yet implemented at ed926db, so every bundle-composition claim here is inferred from `audience:` frontmatter plus the settled selector rule, not observed from a generated bundle.
Findings: 7 — 2 blocking, 3 non-blocking, 2 observations
Dave should inspect: CO-1. This is the thinnest of the six once duplication is removed — three rules survive that nothing else states. It still cannot be retired, for a mechanical reason set out under criterion 10, but the gap between what the file is and what it would need to be to earn its own heading is worth a decision rather than an edit.

## Criterion 10, first and explicitly

**retain-with-changes.**

This file is the hardest of the six to justify on the criterion-10 test as
written, and the honest answer is that it survives on a mechanism rather than on
content. Set out plainly:

Of the twenty-two rules in the file, nineteen are stated by Core or by
operating-model, both of which are in every bundle this file lands in (CO-1,
CO-2, CO-5). Three are not: *keep changes small and coherent* (:14), *preserve
existing behavior unless asked to change it* (:15), and *do not remove
meaningful coverage without explanation* (:42). On the criterion as written —
"contributes something no other file in that bundle states" — three rules is a
pass, but a narrow one, and the criterion's own remedy ("removed, not fixed")
would be the reading if the residue were two rules instead of three.

It is not available as a reading. `audience:` values are `roles/` file slugs
(policies/document-metadata-policy.md:91-93). Deleting roles/coder-agent.md
deletes the `coder-agent` audience value, and `bin/bundle coder-agent` then
compiles a bundle in which nothing tells the receiving agent it is the Coder or
that the Coder's step in the change flow is step 5. Criterion 10's retirement
remedy assumes a file whose absence leaves the bundle intact; a role document
is the file that makes the bundle addressable. The remedy does not apply.

So: retain-with-changes, and the changes are substantial — the file should come
out of this at roughly a third of its length, stating the three rules that are
its own, the red-gate precondition in the one form that is a Coder instruction
rather than a restatement of the flow, and the session kind.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass with one exception — the file is self-contained apart from the reference at :39; CO-3 |
| 2 | `audience:` is the selector | pass with an observation — `coder-agent` is the file's own slug; `chief-of-staff` widens rather than narrows, CO-6 |
| 3 | No path references | fail — 1 reference at :39; CO-3 |
| 4 | Core states it → remove it here | fail — CO-1, CO-2, CO-5; the dominant defect, and close to the whole file |
| 5 | Agent instruction, not authoring principle | pass with an observation — every rule is an instruction, stated in the third person and softened to "should"; CO-7 |
| 6 | Instructions, not rationale | pass — the file states rules and stops; no trailing justifications |
| 7 | Session kind explicit | fail — CO-4 |
| 8 | Tiers, not model names | pass — no vendor name, no model name, no tier language, none of the four retired terms |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass, narrowly and on a mechanism — see above |

## Counts

- Rules restated from Core, decision-layer, LEXICON, or operating-model: **19**, itemised in CO-1's table. By section: Responsibilities 4 of 6, Required outputs 6 of 6, Constraints 6 of 7, Handoff 1 of 1.
- Output-shape lists belonging elsewhere: **1** — Required outputs (:22-28), which is operating-model's change package items 4 and 5 restated and diverged; CO-2.
- Path-shaped references: **1** — :39.
- Vendor and model names: **0.**
- Retired terms (dispatch, sync block, track, prompt): **0.**

## CO-1 — blocking
Claim: Nineteen of the file's twenty-two rules are already stated by Core or operating-model, both of which are in this file's bundle.
Location: roles/coder-agent.md:13-18, :22-28, :33-44, :48 — the whole body
Evidence: Verified by reading both foundation files at ed926db against every line of this file. The mapping:

| This file | Already stated in |
| --- | --- |
| :14 keep changes small and coherent | — **not duplicated** |
| :15 preserve existing behavior unless asked | — **not duplicated** |
| :16 run relevant checks | operating-model.md:120 step 5, "mechanical checks (lint, types, static analysis) pass as part of 'green'" |
| :17 update related docs when behavior changes | operating-model.md:77, Agents Must: "update relevant documentation when behavior changes" |
| :13 implement the requested change | operating-model.md:120 step 5, "Implement to green" |
| :18 report what changed and why | core.md rule 5, rule 10; operating-model.md:176-186 Standard response shape |
| :24-28 Required outputs | operating-model.md:160-174 change package items 4, 5; see CO-2 |
| :28 assumptions made | operating-model.md:75, Agents Must: "state assumptions" |
| :35-37 red-gate precondition | operating-model.md:119-120 steps 4 and 5; :126 "The red-gate at step 4 is mandatory" |
| :38-39 do not write the tests for the unit | operating-model.md:120 step 5, "(Coder — a different agent from the Test Designer for this unit)"; :90 "Whoever produces an artifact does not approve it" |
| :40 broaden scope silently | core.md rule 3, "Scope stays explicit" |
| :41 weaken tests to pass | operating-model.md:83, Agents Must not: "weaken verification to satisfy implementation" |
| :42 remove meaningful coverage without explanation | — **not duplicated** |
| :43 hide uncertainty | core.md rule 7, "Say what is unverified" |
| :44 claim live integration success from mocked tests | operating-model.md:84, Agents Must not: "claim live behavior from mocked evidence" |
| :48 Handoff | operating-model.md:121-123 change flow steps 6, 7, 8; see CO-5 |

Consequence: Criterion 4. core.md is `audience: [all-roles, human]`, order 0; operating-model.md is `audience: [all-roles, human]`, order 3. Both are in the Coder's bundle ahead of this file. The Coder therefore receives nineteen rules twice, and the second statement of each is weaker than the first in a way that matters: Core states its rules as rules ("Scope stays explicit"), this file states them as things "the Coder Agent should not" do. Core rule 1's framing — a layer loaded after Core adds rules, and a conflicting rule in a later layer does not waive the Core rule — resolves the conflict correctly but only for a reader who notices there is one.
Fix: Delete every row of the table above that has a right-hand entry. What survives is :14, :15, :42, plus the red-gate precondition in the reduced form CO-2's and this finding's fixes leave — see the note below. Do not preserve the deleted rules by rewording them; operating-model is in the bundle.

*Note on the red-gate.* :35-37 restates operating-model steps 4-5, but its second clause — "if this confirmation is absent, flag it rather than proceed" — is a Coder instruction that operating-model does not state; operating-model states the gate, not what the Coder does when it finds the gate unmet. Keep that clause, in one line, without restating the gate itself.

Related: CO-2, CO-5

## CO-2 — blocking
Claim: The Required outputs list is operating-model's change package restated in different words, and it has diverged — it omits three things cycle 17 added to the change package.
Location: roles/coder-agent.md:20-28
Evidence: Verified by reading both at ed926db. This file: implementation summary, files changed, tests run, failures encountered, unresolved issues, assumptions made — 6 items. operating-model.md:160-174, change package: item 4 "Implementation summary", item 5 "Test results — including the test commands run, any skipped tests, and a recommendation on whether the testing evidence is sufficient", item 9 "Known gaps". The three qualifiers on item 5 are the product of cycle 17's T8 disposition, which folded them in from the retired testing policy (docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md: "T8: fold the three additive items into operating-model.md's change package as sub-items of Test results"). None of the three appears in this file's "tests run".
Consequence: Criterion 4, and the divergence finding A2 identified on the review-output axis, here on the change-package axis. A Coder that satisfies this file's six-item list has not produced the change package: it has reported "tests run" without the commands, without the skipped tests, and without the sufficiency judgment — which is precisely the evidence the sufficiency sub-item exists to force. The role document is the file that looks like it is telling the Coder what to hand over, so it is the one that gets followed, and it is the one that was not updated when the change package was.
Fix: Delete :20-28. The change package's shape is operating-model's, it is in this bundle, and skills/change-package-creation.md (`audience: [coder-agent, release-manager-agent, chief-of-staff, human]`) is in this bundle too and carries the procedure. If "files changed" is judged worth keeping — it is the one item with no change-package counterpart — it belongs as a sub-item of operating-model's item 4, not as a competing list here.
Related: CO-1

## CO-3 — non-blocking
Claim: One path-shaped reference names a file the bundle does not carry.
Location: roles/coder-agent.md:39
Evidence: Verified by running `grep -nE '[A-Za-z0-9_/-]+\.(md|py|txt|json|yml|yaml)' roles/coder-agent.md`, which returns this line only: "(a separate Test Designer Agent owns those; see `policies/commit-and-change-control-policy.md`)". Checked against the bundle-mate set: that policy carries `audience: [all-roles, human]`, so it *is* in this bundle — the reference resolves, unlike the equivalents in roles/architect-agent.md.
Consequence: Criterion 3. The criterion is not conditioned on whether the target is in the bundle — "If the file needs something another file states, it states it. A path-shaped reference is a defect" — and the reference is doing no work here in any case: the sentence it closes states the rule in full before pointing.
Fix: Delete "; see `policies/commit-and-change-control-policy.md`". The clause before it already says what the reader needs, and CO-1 deletes the rest of the sentence as duplicated.
Related: CO-1

## CO-4 — non-blocking
Claim: The file does not state which session kind it addresses.
Location: roles/coder-agent.md — whole file
Evidence: Verified by reading. No sentence names a decision session or an execution session. Core defines both at core.md, Vocabulary: an execution session is "an LLM agent session carrying out a directive against a working tree"; a decision session "does not carry out the changes a directive specifies".
Consequence: Criterion 7. Unlike roles/architect-agent.md, where the answer is genuinely both, the Coder is unambiguously an execution session by Core's own definition — carrying out a directive against a working tree is what the role is. The file has the easiest possible answer to the criterion and does not give it.
Fix: One line under the title: this role runs in an execution session.

## CO-5 — non-blocking
Claim: The Handoff section restates operating-model's change-flow ordering.
Location: roles/coder-agent.md:46-48
Evidence: Verified by reading. This file: "The Coder Agent hands work to Reviewer and Skeptic/Risk review before release." operating-model.md:121-123, steps 6, 7, 8 in order: Quality review (Reviewer — hard gate), Skeptic/risk review, Release package. operating-model.md:112-113 also states "Each stage completes before the next begins; no skipping or working ahead", which is the "before release" clause.
Consequence: Criterion 4. This is the case the directive's Context names: "operating-model.md's change flow already assigns each of these roles its step; a role document that restates the flow is restating operating-model." The section is three lines and adds nothing to the two steps that follow the Coder's.
Fix: Delete :46-48.
Related: CO-1

## CO-6 — observation
Claim: `audience:` includes `chief-of-staff`, which selects this role document into the Chief of Staff's bundle along with the other ten role documents.
Location: roles/coder-agent.md:4
Evidence: Verified by running `grep -rn "audience:" --include='*.md' roles/`. All eleven files in `roles/` list `chief-of-staff` except roles/chief-of-staff.md, whose own audience is `[chief-of-staff, human]`. Under the settled selector rule (docs/batons/baton-20260822T153848.md, "What this session settled"), `bin/bundle chief-of-staff` compiles every role document into one bundle. Inferred, not observed: audience selection is not implemented at ed926db.
Consequence: Criterion 2, at the margin — the selector widens where its job is to narrow.
Fix: None proposed here. The pattern is identical across all eleven role documents, five of which are in cycle 19a; settle it once rather than per file.

## CO-7 — observation
Claim: Hard constraints are stated as things the role "should not" do, in the third person.
Location: roles/coder-agent.md:33 ("The Coder Agent should not:"), governing :35-44
Evidence: Verified by reading. The list under :33 includes the red-gate precondition and the test-authorship separation — both of which operating-model treats as mandatory rather than optional ("The red-gate at step 4 is mandatory", :126; "two separations are mandatory rather than optional", :87-89) — under a heading that says "should not".
Consequence: Criterion 5, at the margin. The rules are instructions, so the criterion is not failed, but the modal is wrong for two of them and the third person requires the reader to identify itself as "the Coder Agent" before any rule binds. The same pattern runs through all six roles in this cycle.
Fix: Second person, and "must not" for the constraints operating-model calls mandatory. Largely moot once CO-1 removes the duplicated constraints.
