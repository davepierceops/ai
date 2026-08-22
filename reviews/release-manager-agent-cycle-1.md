# Review: roles/release-manager-agent.md — cycle 1

Verdict: changes-required
Reviewed: roles/release-manager-agent.md @ ed926db174887c54a701b8fc4f0a35726bdc027a
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (55 lines), against docs/global-context/review-rubric.md @ ed926db, all ten criteria. The two edits cycle 17 landed here — the release-package list retained over the policy's, and "GitHub issue" replaced by "tracker issue" — are inspected as part of the file, on the same footing as the rest.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ ed926db); roles/skeptic-risk-agent.md on the recommendation vocabulary; skills/release-readiness-review.md, skills/change-package-creation.md, skills/evidence-review.md and skills/boundary-audit.md as bundle-mates; reviews/agent-review-policy-cycle-1.md finding A2; docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md, dispositions for policies/release-readiness-policy.md (RR-2, RR-6).
Not inspected: skills/release-readiness-review.md and skills/change-package-creation.md against their own rubric criteria — read only as evidence of where a rule already lives; policies/release-readiness-policy.md and policies/commit-and-change-control-policy.md as documents in their own right, beyond confirming the paths at :41-42 resolve and that cycle 17 emptied the former of the release-package list; whether `bin/bundle` in fact composes the bundle this review reasons about — audience selection is not implemented at ed926db, so every bundle-composition claim here is inferred from `audience:` frontmatter plus the settled selector rule, not observed from a generated bundle.
Findings: 7 — 2 blocking, 3 non-blocking, 2 observations
Dave should inspect: RM-1. Cycle 17 settled that the release-package list lives in this role document rather than in policies/release-readiness-policy.md. It is also, unchanged, the Procedure of skills/release-readiness-review.md, which is in the same bundle — and the Recommendation vocabulary here is byte-identical to that skill's Output, verified by diff. The cycle-17 decision resolved role-versus-policy; this is role-versus-skill and needs the same call. Also RM-2: the sentence "assembled from the change package, not written fresh" is true for eight of the ten items and false for two.

## Criterion 10, first and explicitly

**retain-with-changes.**

Two things here are stated by no other file at all: the Responsibilities list's
framing of this role as *collection* rather than judgment (:13-15, "collect
change summary / collect test evidence / collect review evidence"), which is
what distinguishes step 8 from steps 6 and 7; and the Non-goal at :55, "should
not rubber-stamp work because tests pass". Two more are stated only by
operating-model, which makes them duplicates rather than contributions: the
human-gate confirmation and the ship recommendation.

The file's two largest sections are not among the survivors. The release-package
list (:25-36) and the Recommendation vocabulary (:44-51) are both stated by
skills/release-readiness-review.md, a bundle-mate — the first item for item, the
second byte for byte (RM-1). That leaves this file thin, but cycle 17 explicitly
chose this document as the release-package list's home over
policies/release-readiness-policy.md, and this review does not reopen a decision
Dave made three commits ago on evidence that has not changed. The finding names
the skill as the file to change and treats that edit as a dependency.

Retirement is not available in any case: `audience:` values are `roles/` file
slugs (policies/document-metadata-policy.md:91-93), so deleting the file deletes
the `release-manager-agent` selector.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass with one exception — self-contained apart from the references at :41-42; RM-4 |
| 2 | `audience:` is the selector | pass with an observation — `release-manager-agent` is the file's own slug; `chief-of-staff` widens rather than narrows, RM-6 |
| 3 | No path references | fail — 2 references at :41-42; RM-4 |
| 4 | Core states it → remove it here | fail — RM-2, RM-3 |
| 5 | Agent instruction, not authoring principle | pass — every rule is an instruction, in the third person; RM-7 |
| 6 | Instructions, not rationale | pass — the file states rules and stops |
| 7 | Session kind explicit | fail — RM-5 |
| 8 | Tiers, not model names | pass — "tracker issue" at :20 and :40 is correct, not a retired term; see the note under Counts. No vendor name, no model name, no tier language |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass — retain-with-changes, see above |

## Counts

- Rules restated from Core, decision-layer, LEXICON, or operating-model: **2** — the human-gate confirmation, stated twice within this file and once in operating-model (RM-3), and the change-package sourcing claim (RM-2). The release-package list itself is *not* counted here: it is not the change package restated, it is a re-cut of it, which is what RM-2 is about.
- Output-shape lists belonging elsewhere: **1**, with a qualification — Required outputs (:25-36) is the release package's shape, and cycle 17 settled that its home is this file. Finding A2's settled rule does not reach it: A2 governs the shape of a *review's* output and assigns it to the review artifact schema, and a release package is not a review artifact. The collision is with a bundle-mate skill, not with the schema, and is reported on criterion 10; RM-1.
- Path-shaped references: **2** — :41, :42.
- Vendor and model names: **0.** "tracker issue" at :20 and :40 is the term cycle 17 required, and LEXICON.md:118-121 carves *tracker* out of the retirement of *track* explicitly — "**track**, **tracking**, and **tracker** in the ordinary sense of keeping or consulting a record… keep their ordinary meaning." Recorded here so a later mechanical sweep does not "fix" a correct term.
- Retired terms (dispatch, sync block, track, prompt): **0.**

## RM-1 — blocking
Claim: The release-package list and the Recommendation vocabulary are both stated by skills/release-readiness-review.md, which is in this bundle — the first item for item, the second byte for byte.
Location: roles/release-manager-agent.md:25-36 and :44-51
Evidence: Verified by running and by reading. skills/release-readiness-review.md carries `audience: [release-manager-agent, skeptic-risk-agent, human]`, so it is in this bundle. On the vocabulary: extracting the four-item list from each file and running `diff` returns empty — "ship / ship with accepted risks / do not ship / needs Dave decision", same four, same order, and both are introduced by the same phrase, "Use one of:". On the list, item for item:

| This file (:27-36) | skills/release-readiness-review.md Procedure |
| --- | --- |
| 1. Change summary | 1. Summarize user-visible change |
| 2. User-visible behavior | 1. (same step) |
| 3. Test evidence | 2. Summarize test evidence |
| 4. Verification boundary status | 3. Summarize verification boundary status |
| 5. SLO status and error budget consumption for affected Top K user journeys | 4. State SLO status and error budget consumption for affected Top K user journeys |
| 6. Live/browser verification status, if relevant | 5. Identify live/browser/production checks required |
| 7. Operational risks | — |
| 8. Rollback or mitigation path | 7. Identify rollback or mitigation path |
| 9. Known gaps | 6. Identify known gaps |
| 10. Ship/no-ship recommendation and Dave decision points | 9. Give a recommendation |
| (:40-42, prose) | 8. Confirm `human-gate` GitHub issue is open and linked if consequential |

Nine of ten items have a counterpart; only "Operational risks" does not.
Consequence: Criterion 10. Two of this file's four substantive sections are stated by another file in the same bundle, and they have already begun to diverge in the way finding A2 documented: the skill's step 8 still reads "human-gate GitHub issue", where cycle 17 moved this file to "tracker issue" — so the same artifact is named two ways inside one bundle, which is Core rule 13. A Release Manager holding both has two specifications of the package it assembles and no rule for which governs.
Fix: Keep both sections here — cycle 17 chose this file as the list's home over policies/release-readiness-policy.md (RR-2: "delete the release-package list here; roles/release-manager-agent.md keeps it"), and that decision is not reopened by this cycle. The edit is to skills/release-readiness-review.md: its Procedure becomes the *method* of assembling the package rather than a second enumeration of the package's contents, and its Output section drops the four-item vocabulary this file states. That skill is not in this cycle's scope, so the edit is named here as a dependency rather than as a finding against it, on finding A5's precedent. Conform its step 8 to "tracker issue" in the same change. Note that roles/skeptic-risk-agent.md:209 carries the same four-item vocabulary a third time; that is finding SK-3 in this cycle, and its fix is deletion there.
Related: RM-2, RM-3; roles/skeptic-risk-agent.md SK-3

## RM-2 — blocking
Claim: "This package is assembled from the change package, not written fresh" is false for two of the ten items, and the package silently drops four change-package items.
Location: roles/release-manager-agent.md:38, governing :25-36
Evidence: Verified by reading both at ed926db. operating-model.md:160-174 lists the change package's twelve items. Mapped against this file's ten:

| Release package (this file) | Change package (operating-model.md:160-174) |
| --- | --- |
| 1. Change summary | 4. Implementation summary (+ 1. Intent / problem statement) |
| 2. User-visible behavior | — **no source** |
| 3. Test evidence | 5. Test results |
| 4. Verification boundary status | 6. Verification boundary updates |
| 5. SLO status and error budget consumption | 7. — same wording |
| 6. Live/browser verification status | subsumed in 5 and 6 |
| 7. Operational risks | 10. Operational notes |
| 8. Rollback or mitigation path | — **no source** |
| 9. Known gaps | 9. — same wording |
| 10. Ship/no-ship recommendation and Dave decision points | 12. Release recommendation |
| — | 2. Acceptance criteria — **dropped** |
| — | 3. Test plan — **dropped** |
| — | 8. Review findings — **dropped** |
| — | 11. `human-gate` tracker issue reference — **dropped from the list**; recovered in prose at :40-42 |

The sentence at :38 is the product of cycle 17's RR-2 disposition, which added it when the list was retained here ("roles/release-manager-agent.md keeps it and gains the one sentence that the package is assembled from the change package, not written fresh").
Consequence: Criterion 4, and a false claim rather than a duplicated one. Items 2 and 8 cannot be assembled from the change package because the change package does not contain them — a Release Manager following :38 literally will look for a user-visible-behavior statement and a rollback path in the change package, not find them, and either fabricate them or omit them. Both are material at a release decision; the rollback path in particular is what operating-model's own release gate depends on. In the other direction, "Review findings" is a change-package item with no release-package slot, so the reviews at steps 6 and 7 can reach the release decision only through "Known gaps".
Fix: Two options, and this is a decision rather than a mechanical edit. Either add "user-visible behavior" and "rollback or mitigation path" to operating-model's change package, which makes :38 true as written and is the better answer since both belong in a change package regardless; or narrow :38 to say the package is assembled from the change package where the change package states it, and name the two items the Release Manager must source elsewhere. Either way, add "Review findings" to the release package or say explicitly that it reaches the release decision through Known gaps. operating-model.md is through Pass 1 and not in this cycle's scope, so the first option is named as a dependency.
Related: RM-1

## RM-3 — non-blocking
Claim: The human-gate confirmation is stated twice in this file and once in operating-model.
Location: roles/release-manager-agent.md:20 and :40-42
Evidence: Verified by reading. :20, Responsibilities: "confirm `human-gate` tracker issue is open and linked for consequential changes". :40-42, prose beneath the Required outputs list: "For consequential changes, confirm the `human-gate` tracker issue is open and linked before presenting to Dave." operating-model.md:173, change package item 11: "`human-gate` tracker issue reference, if the change is consequential"; and :141-143, Release gate, which states the two-tier rule and that the consequential class is the commit and change control policy's list.
Consequence: Criterion 4 and criterion 6 — the same obligation three times, twice within fifty-five lines. The two statements here agree, so nothing is currently wrong; the cost is that three copies must be kept agreeing, and skills/release-readiness-review.md:37-38 is a fourth that has already drifted on the vendor name (RM-1).
Fix: Delete :40-42. :20 states it, and the "before presenting to Dave" timing is implied by the role's position at step 8. If the timing is judged load-bearing, keep it as a clause on :20.
Related: RM-1

## RM-4 — non-blocking
Claim: Two path-shaped references.
Location: roles/release-manager-agent.md:41-42
Evidence: Verified by running `grep -nE '[A-Za-z0-9_/-]+\.(md|py|txt|json|yml|yaml)' roles/release-manager-agent.md`, which returns these two: "See `policies/release-readiness-policy.md` and `policies/commit-and-change-control-policy.md`." Both carry `audience: [all-roles, human]` and are in this bundle, so the references resolve — but criterion 3 is not conditioned on that.
Consequence: Criterion 3. The references also point at a moving target: cycle 17 reduced policies/release-readiness-policy.md to a session-kind line, a definition, and a statement that the gate is the commit-and-change-control policy's two tiers, so the first of the two paths now names a file that no longer contains the release-package content a reader following it would expect.
Fix: Delete the sentence with RM-3. If any of it survives, the paths do not.
Related: RM-3

## RM-5 — non-blocking
Claim: The file does not state which session kind it addresses.
Location: roles/release-manager-agent.md — whole file
Evidence: Verified by reading. No sentence names a decision session or an execution session. Compare the shape cycle 17 required of every retained policy: "Each retained policy opens with one line naming the session kind it governs."
Consequence: Criterion 7, and the ambiguity is live for this role more than for any other of the six. Assembling evidence from a working tree is execution work; presenting a package to Dave for a go/no-go, and confirming a tracker issue is open before doing so, sits against Core's definition of a decision session as the kind that "produces the artifacts that direct and record work". The file describes both and distinguishes neither.
Fix: One line under the title. If the answer is both, say which acts belong to which kind — assembly in an execution session, presentation at the release decision in a decision session.

## RM-6 — observation
Claim: `audience:` includes `chief-of-staff`, which selects this role document into the Chief of Staff's bundle along with the other ten role documents.
Location: roles/release-manager-agent.md:4
Evidence: Verified by running `grep -rn "audience:" --include='*.md' roles/`. All eleven files in `roles/` list `chief-of-staff` except roles/chief-of-staff.md, whose own audience is `[chief-of-staff, human]`. Inferred, not observed: audience selection is not implemented at ed926db.
Consequence: Criterion 2, at the margin — the selector widens where its job is to narrow.
Fix: None proposed here. The pattern is identical across all eleven role documents; settle it once rather than per file.

## RM-7 — observation
Claim: Every rule is stated in the third person about the Release Manager Agent rather than as an instruction to the agent reading the bundle.
Location: roles/release-manager-agent.md:9, :55
Evidence: Verified by reading. :9: "The Release Manager Agent assembles release evidence and gives a ship/no-ship recommendation." :55: "The Release Manager Agent should not rubber-stamp work because tests pass." The Responsibilities list at :13-21 is the exception — bare imperatives, correctly framed.
Consequence: Criterion 5, at the margin. The rules are instructions, so the criterion is not failed; the reader must identify itself as "the Release Manager Agent" before any of them binds.
Fix: Second person, on the model of :13-21. The same pattern runs through all six roles in this cycle.
