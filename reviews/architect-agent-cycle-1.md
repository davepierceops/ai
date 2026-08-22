# Review: roles/architect-agent.md — cycle 1

Verdict: changes-required
Reviewed: roles/architect-agent.md @ ed926db174887c54a701b8fc4f0a35726bdc027a
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (74 lines), against docs/global-context/review-rubric.md @ ed926db, all ten criteria.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ ed926db); the other five roles in this cycle; reviews/agent-review-policy-cycle-1.md finding A2; docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md; skills/spec-review-cycle.md review artifact schema; the bundle-mate set computed from `audience:` frontmatter across the repository.
Not inspected: specs/trd-template.md and context-sets/ai-native-engineering.md as documents in their own right — read only far enough to confirm the paths at :25, :45 and :46 resolve; roles/spec-reviewer-agent.md against its own criteria (cycle 19a); whether `bin/bundle` in fact composes the bundle this review reasons about — audience selection is not yet implemented (`bin/bundle` still takes ENTRY paths), so every bundle-composition claim here is inferred from `audience:` frontmatter plus the settled selector rule, not observed from a generated bundle.
Findings: 8 — 2 blocking, 3 non-blocking, 3 observations
Dave should inspect: AR-2. The per-change architecture summary is defined in two places that now disagree on one word — operating-model says the *tracker* issue is cut from it, this file says a *GitHub Issue* is. Cycle 17 moved the rest of the repository off vendor names; this file was not in that cycle's scope and was left behind.

## Criterion 10, first and explicitly

**retain-with-changes.**

The file contributes two things no other file in its bundle states: that the
Architect owns every TRD section including the SLO-per-Top-K-journey definitions
and the instantiation of the PRD's NFR dimensions, and the contents of the
per-change architecture summary. Neither is in operating-model, Core,
decision-layer, or LEXICON, and no bundle-mate carries them.

It cannot be retired on the residue argument even if that residue were thinner:
`audience:` values are `roles/` file slugs
(policies/document-metadata-policy.md:91-93), so deleting the file deletes the
selector, and `bin/bundle architect-agent` would then compile a bundle with no
statement of what the receiving agent is for. Retirement is available to a
policy or a context set; it is not available to a role document that is the sole
definition of its own audience value. The disposition is therefore
retain-with-changes, and the findings below are the edit list.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — four path-shaped references ask the reader to open files the bundle does not carry; AR-3 |
| 2 | `audience:` is the selector | pass with an observation — `architect-agent` is the file's own slug; `chief-of-staff` widens rather than narrows, AR-8 |
| 3 | No path references | fail — 4 references; AR-3 |
| 4 | Core states it → remove it here | fail — AR-1, AR-2, AR-5 |
| 5 | Agent instruction, not authoring principle | pass with an observation — every rule is an instruction, but stated in the third person about the role; AR-6 |
| 6 | Instructions, not rationale | pass — the file states rules and stops |
| 7 | Session kind explicit | fail — AR-4; the file names neither kind |
| 8 | Tiers, not model names | fail — one vendor name, "GitHub Issue" at :38; AR-2. No model name, no tier language, none of the four retired terms |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass — retain-with-changes, see above |

## Counts

- Rules restated from Core, decision-layer, LEXICON, or operating-model: **3** — the separation requirement (AR-1), the architecture-summary-to-issue sequence (AR-2), the consequential-class claim (AR-5).
- Output-shape lists belonging elsewhere: **0.** The Required outputs list (:50-56) is the architecture summary's contents. It is not a review output, so finding A2's settled rule does not reach it, and operating-model's change package has no architecture-summary item, so it is not the change package's either. This list is this file's own and stays.
- Path-shaped references: **4** — :25, :29, :45, :46.
- Vendor and model names: **1** — "GitHub Issue" (:38).
- Retired terms (dispatch, sync block, track, prompt): **0.**

## AR-1 — blocking
Claim: The Separation requirement section restates a rule operating-model.md already states, and adds nothing to it but two path references.
Location: roles/architect-agent.md:41-46
Evidence: Verified by reading both at ed926db. This file: "The Architect Agent that drafts a TRD (or a TRD revision) is not the agent instance that acts as Spec Reviewer for that document. Authorship and review must be separated." operating-model.md:91-92, under Responsibilities, in the list of the two mandatory separations: "The Architect that drafts a spec does not act as the Spec Reviewer that certifies it." operating-model states it as one of exactly two separations the model treats as mandatory rather than optional; this file states the same rule with "TRD" substituted for "spec" and no further content.
Consequence: Criterion 4. operating-model.md is in this bundle — `audience: [all-roles, human]`, order 3 — so the Architect's bundle carries the rule twice. The two are not identical: operating-model's version covers any spec, this file's covers a TRD or TRD revision, which reads as narrower. An agent reading both has no rule for which governs a PRD the Architect drafted, and the narrower copy is the one under the heading that looks authoritative for this role.
Fix: Delete :41-46 entirely. The rule's home is operating-model.md's mandatory-separations list, which is in every bundle this file lands in. If the TRD-revision case is judged to need saying, it is a widening of operating-model's sentence and belongs there, not here.
Related: AR-3

## AR-2 — blocking
Claim: The per-change architecture summary bullet restates operating-model's change-flow step 3, and states it with a vendor name that operating-model no longer uses.
Location: roles/architect-agent.md:37-39
Evidence: Verified by reading both at ed926db, and by grep. This file: "**The per-change architecture summary** — scoped to one unit of work, derived from the TRD. This is the artifact a GitHub Issue is cut from, and it sits between the TRD and the Issues in the canonical sequence." operating-model.md:118, change flow step 3: "**Architecture summary** — per-change design derived from the TRD; the tracker issue is cut from this. *(Architect)*". Same three facts — scope, derivation, what is cut from it — and the same role attribution. `grep -nEi '(github|gitlab|jira|linear)' roles/*.md` over the six files in this cycle returns two hits: this line and roles/skeptic-risk-agent.md:206. Cycle 17 directed "Vendor names become 'the forge', 'the tracker', or are deleted; 'human-gate tracker issue' is the term" (docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md, Rules for every edit), and applied it to roles/release-manager-agent.md, which now reads "tracker issue" at :20 and :40. This file was not in that cycle's scope.
Consequence: Criterion 4 and criterion 8. Core rule 13 — a changed fact changes everywhere it appears — was satisfied for the two roles cycle 17 touched and not for this one, so the repository now states the same fact two ways. A bundle carrying both operating-model and this file tells the Architect the tracker issue is cut from the summary and that a GitHub Issue is, which is a vendor lock-in claim in a document whose own Review focus list names vendor lock-in as a thing to watch for (:67).
Fix: Delete the second sentence of :37-39 ("This is the artifact a GitHub Issue is cut from, and it sits between the TRD and the Issues in the canonical sequence"). operating-model's step 3 states it. Keep "scoped to one unit of work, derived from the TRD" only if :50-59 does not already carry it; :50 opens "For meaningful changes, produce a per-change architecture summary with:", which does.
Related: AR-1, AR-5

## AR-3 — non-blocking
Claim: Four path-shaped references ask the reader to open files the bundle does not carry.
Location: roles/architect-agent.md:25 (`specs/trd-template.md`), :29 (`policies/commit-and-change-control-policy.md`), :45 (`roles/spec-reviewer-agent.md`), :46 (`context-sets/ai-native-engineering.md`)
Evidence: Verified by running `grep -nE '[A-Za-z0-9_/-]+\.(md|py|txt|json|yml|yaml)' roles/architect-agent.md`, which returns exactly these four. Checked against the bundle-mate set computed from `audience:` frontmatter: `specs/trd-template.md` carries `audience: [all-roles, human]` and is in the bundle; the other three are not. `roles/spec-reviewer-agent.md` carries `audience: [spec-reviewer-agent, chief-of-staff, human]`, `context-sets/ai-native-engineering.md` and `policies/commit-and-change-control-policy.md` were checked the same way.
Consequence: Criterion 3 and criterion 1. Three of the four name files the receiving agent cannot open, and two of those (:45, :46) are the entire content of the sentence they close — after AR-1 deletes that section they go with it. :29's reference is load-bearing in a different way: it is the only thing telling the Architect where the consequential class is defined, and the agent cannot follow it. See AR-5.
Fix: :45 and :46 go with AR-1. :25 becomes "the standing TRD" without the path — the bundle carries the template, and the Architect does not need its path to write it. :29 per AR-5.
Related: AR-1, AR-5

## AR-4 — non-blocking
Claim: The file does not state which session kind it addresses.
Location: roles/architect-agent.md — whole file
Evidence: Verified by reading. No sentence names a decision session or an execution session. Compare the shape cycle 17 required of every retained policy: "Each retained policy opens with one line naming the session kind it governs" (docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md, Rules for every edit). Role documents were not in that cycle's scope and none of the six in this one carries the line.
Consequence: Criterion 7. The ambiguity is real for this role rather than formal: drafting the standing TRD is decision-session work — it is canonical text that Dave agrees — while producing a per-change architecture summary against an already-agreed TRD is execution work. The file describes both at :21-39 and distinguishes neither, so an execution session receiving this bundle cannot tell whether it is authorised to draft the standing TRD.
Fix: One line under the title naming both kinds and splitting them: the standing TRD is drafted in a decision session; the per-change architecture summary is produced in an execution session.

## AR-5 — non-blocking
Claim: The file states that a change to the standing TRD is a consequential change, which creates a second, partial home for a class that one policy owns.
Location: roles/architect-agent.md:27-29
Evidence: Verified by reading at ed926db. operating-model.md:141-143, Release gate: "The consequential class is the list the commit and change control policy states." That sentence is the product of cycle 17's CC-1 disposition, which made the policy's list canonical and replaced operating-model's inline enumeration with a pointer to it. This file adds a member to that class — a standing-TRD change — under its own heading, and defers to the policy by path in the same breath.
Consequence: Criterion 4. Either the standing-TRD change is on the policy's list, in which case this sentence restates it, or it is not, in which case this file has silently extended a class that operating-model says one policy defines. The reader cannot tell which, and cannot check, because the path at :29 does not resolve inside the bundle.
Fix: Check the commit-and-change-control policy's list. If a standing-TRD change is on it, delete :27-29. If it is not, the sentence is a proposed addition to that list and belongs in that policy — raise it there and delete it here either way. Do not resolve it by keeping both.
Related: AR-2, AR-3

## AR-6 — observation
Claim: Every rule is stated in the third person about the Architect Agent rather than as an instruction to the agent reading the bundle, and one section heading names a review this role does not perform.
Location: roles/architect-agent.md:9, :23, :43, :63, :74 (third person); :61-70 ("Review focus")
Evidence: Verified by reading. "The Architect Agent should pay special attention to" (:63), "The Architect Agent should not optimize for cleverness" (:74). On the heading: operating-model's change flow assigns review to step 6 (Reviewer) and step 7 (Skeptic/Risk); the Architect's step is 3. The six items under "Review focus" — coupling, hidden dependencies, vendor lock-in, deployment assumptions, operational complexity, maintainability — are design attention, not a review gate.
Consequence: Criterion 5, at the margin. The rules are instructions, so the criterion is not failed; but an agent that receives the bundle is told what "the Architect Agent" should do and must infer that it is the Architect Agent, and "Review focus" invites it to believe it holds a gate that operating-model assigns elsewhere. roles/test-designer-agent.md:35 carries the same mislabelled heading.
Fix: Second person throughout, and rename "Review focus" to "Design attention" or fold its six items into Responsibilities.
Related: the same heading in roles/test-designer-agent.md (TD-8)

## AR-7 — observation
Claim: "avoid unnecessary complexity" and the Non-goals section state the same rule twice.
Location: roles/architect-agent.md:19 and :72-74
Evidence: Verified by reading. :19, last item of Responsibilities: "avoid unnecessary complexity". :74: "The Architect Agent should not optimize for cleverness. Prefer boring, understandable designs."
Consequence: Criterion 6, at the margin — the second is the first restated as a Non-goal, which is the "Never X restatement of a stated rule" the criterion names. Small: it costs three lines.
Fix: Delete :72-74 and let :19 carry it, or delete :19 and let the Non-goal carry it. "Prefer boring, understandable designs" is the more useful wording of the two.

## AR-8 — observation
Claim: `audience:` includes `chief-of-staff`, which selects this role document into the Chief of Staff's bundle along with the other ten role documents.
Location: roles/architect-agent.md:4
Evidence: Verified by running `grep -rn "audience:" --include='*.md' roles/`. All eleven files in `roles/` list `chief-of-staff` except roles/chief-of-staff.md itself, whose own audience is `[chief-of-staff, human]`. Under the settled selector rule — bundles select by `audience:` frontmatter plus `order:` (docs/batons/baton-20260822T153848.md, "What this session settled") — `bin/bundle chief-of-staff` therefore compiles every role document into one bundle. Inferred rather than observed: `bin/bundle` at ed926db is still the path-following closure tool and takes ENTRY paths, so this could not be confirmed by running it.
Consequence: Criterion 2, at the margin. The selector widens where its job is to narrow — the same shape as finding A3 against policies/agent-review-policy.md, in a milder form, since a role document at least is not inert in the CoS bundle. Whether the Chief of Staff needs the full instruction text of ten roles it does not fill, or only the fact that they exist, is a design question this cycle cannot settle: the pattern is identical across all eleven role documents, five of which are in cycle 19a.
Fix: None proposed here. Settle it once, across all eleven, rather than per file.
