# Review: roles/skeptic-risk-agent.md — cycle 1

Verdict: changes-required
Reviewed: roles/skeptic-risk-agent.md @ ed926db174887c54a701b8fc4f0a35726bdc027a
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (227 lines — the longest of the six), against docs/global-context/review-rubric.md @ ed926db, all ten criteria.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ ed926db); roles/reviewer-agent.md and roles/release-manager-agent.md on responsibility overlap; skills/boundary-audit.md, skills/evidence-review.md and skills/release-readiness-review.md as bundle-mates; skills/spec-review-cycle.md review artifact schema; reviews/agent-review-policy-cycle-1.md findings A2 and A4; docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md.
Not inspected: skills/boundary-audit.md, skills/evidence-review.md and skills/release-readiness-review.md against their own rubric criteria — read only as evidence of where a rule already lives; policies/verification-boundary-policy.md as a document in its own right, beyond confirming cycle 17 moved the release-impact label definitions out of it and into LEXICON; whether `bin/bundle` in fact composes the bundle this review reasons about — audience selection is not implemented at ed926db, so every bundle-composition claim here is inferred from `audience:` frontmatter plus the settled selector rule, not observed from a generated bundle.
Findings: 9 — 3 blocking, 4 non-blocking, 2 observations
Dave should inspect: SK-1. The file defines four risk-severity categories and one of them is "Needs Dave decision", which LEXICON.md:71 rules out in as many words — "a gap awaiting Dave's judgment is blocking; 'requires Dave decision' is not a label." That is a direct contradiction between a role document and a foundation file, not a duplication, and the file carries three different gap vocabularies internally on top of it. Also SK-3: the file's own output template has this role emitting the ship recommendation, which operating-model assigns to the Release Manager at step 8.

## Criterion 10, first and explicitly

**retain-with-changes** — with roughly half the file coming out.

What earns its place, and nothing else in the bundle states: the core question
at :17 ("What confidence is being inferred that the evidence does not actually
support?"); the eight-item Assume list at :39-48 and, more valuably, the
four-item "Do not assume" counter-list at :50-56 — finding A4 identified this
pair as the better version that a weaker copy elsewhere was displacing, and it
survived that merge intact; the sentence at :74 that code may be reviewed but the
primary object of review is the evidence chain, which is the one place in the
repository that says what this role reviews *instead of* code; and the
false-confidence checklist at :93-109, thirteen named failure patterns that
appear nowhere else.

What does not: the two output shapes (SK-2), the boundary checklist that a
bundle-mate skill states as a procedure (SK-4), the risk-severity vocabulary
that contradicts LEXICON (SK-1), and the mandate sentence that restates
operating-model (SK-6). That is roughly 120 of 227 lines.

The residue is substantial and specific, so the file earns its place
comfortably. Retirement would not be available in any case: `audience:` values
are `roles/` file slugs (policies/document-metadata-policy.md:91-93), so
deleting the file deletes the `skeptic-risk-agent` selector.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass — nothing here assumes the reader can open another file |
| 2 | `audience:` is the selector | pass with an observation — `skeptic-risk-agent` is the file's own slug; `chief-of-staff` widens rather than narrows, SK-8 |
| 3 | No path references | pass — zero path-shaped references; one of two files in this cycle that is clean here |
| 4 | Core states it → remove it here | fail — SK-1 (a contradiction, not merely a duplicate), SK-6, SK-7 |
| 5 | Agent instruction, not authoring principle | pass — every rule is an instruction, in the third person; SK-9 |
| 6 | Instructions, not rationale | pass — the file states rules and stops |
| 7 | Session kind explicit | fail — the file names neither kind; see the note under SK-6 |
| 8 | Tiers, not model names | fail — one vendor name at :206, plus two technology names that presuppose a JavaScript stack; SK-5. No model name, no tier language, none of the four retired terms |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass — retain-with-changes, see above |

## Counts

- Rules restated from Core, decision-layer, LEXICON, or operating-model: **3** — the risk-severity vocabulary against LEXICON's release impact labels (SK-1, a contradiction rather than a restatement), the mandate sentence at :13 (SK-6), and one Non-goal at :222 (SK-7).
- Output-shape lists belonging elsewhere: **2** — "Required output" (:76-91, 12 items) and "Output template" (:167-213, 14 headings). Both fall under finding A2's settled rule and they disagree with each other; SK-2.
- Path-shaped references: **0.**
- Vendor and model names: **1 vendor** — "GitHub issue" (:206). Recorded separately, **2 technology names** that are not vendors but carry the same lock-in cost: "jsdom" (:44, :99) and "service worker/PWA" (:107); SK-5.
- Retired terms (dispatch, sync block, track, prompt): **0.**

## SK-1 — blocking
Claim: The Risk severity vocabulary contradicts LEXICON's release impact labels, and the file carries three different gap vocabularies internally.
Location: roles/skeptic-risk-agent.md:123-165, and :89, :121, :202
Evidence: Verified by reading both at ed926db. LEXICON.md:65-78, "Release impact labels — the labels a known gap is marked with at the release decision. Every material boundary gap carries one": `blocking`, `deferred`, `accepted-risk`, `not-material`. LEXICON.md:70-71, under `blocking`: "A gap awaiting Dave's judgment is blocking; 'requires Dave decision' is not a label." That sentence is the product of cycle 17's LEXICON disposition, which moved the label definitions out of policies/verification-boundary-policy.md and added the exclusion.

This file's four Risk severity headings: **Blocking** (:127), **Needs Dave decision** (:140), **Deferrable** (:152), **Not material** (:163). Against LEXICON: `blocking` matches; **Needs Dave decision** is the label LEXICON rules out by name; **Deferrable** is not `deferred`; `accepted-risk` has no heading at all. And the file does not agree with itself — :121, boundary checklist item 7, asks whether the missing evidence is "blocking, deferred, accepted, or not material" (closest to LEXICON, four labels, none of them "Needs Dave decision"); :89, Required output item 10, is "Accepted or deferrable risks"; :202, Output template, is "Deferrable / accepted risks". Four labellings in one file, three of them different from LEXICON.
Consequence: Criterion 4, in its sharpest form: not a rule restated but a rule contradicted. LEXICON.md carries `audience: [all-roles, human]`, order 2, so it is in this bundle ahead of this file — and Core rule 1 says a rule in a layer loaded after Core that conflicts does not waive the earlier rule, which resolves the conflict correctly only for a reader who notices there is one. The concrete failure: a gap that is genuinely awaiting Dave's judgment gets filed under "Needs Dave decision" here, and is therefore not marked `blocking`, and the Release Manager assembling the release package (operating-model.md:123, step 8) sees a category that is not one of the four labels the release decision is defined over. LEXICON's exclusion exists precisely to stop a blocking gap being downgraded to a question.
Fix: Delete :123-165 and use LEXICON's four labels. The examples under each heading are the part worth keeping — six under Blocking, five under Needs Dave decision, four under Deferrable — so redistribute them: the "Needs Dave decision" examples are, by LEXICON's own rule, `blocking` examples. Conform :89, :121 and :202 to the same four labels in the same change (:89 and :202 are deleted by SK-2 in any case). Do not resolve this by adding "Needs Dave decision" to LEXICON; LEXICON has already considered and rejected it.
Related: SK-2, SK-3

## SK-2 — blocking
Claim: The file states the shape of this role's report twice — as a 12-item list and as a 14-heading template — the two disagree, and both belong to the review artifact schema.
Location: roles/skeptic-risk-agent.md:76-91 and :167-213
Evidence: Verified by running. Extracting both sets of headings and comparing: the Required output list has 12 items; the Output template has 14. The template adds three the list does not name — **Supported claims**, **SLO / error budget status**, **Human-gate required** — drops one the list requires — **Security/privacy risks, if relevant** — and renames **Recommended next step** to **Recommendation**, changing its content from a next step to a ship call (see SK-3). reviews/agent-review-policy-cycle-1.md, A2, Fix, settled the rule: "the review artifact schema in `skills/spec-review-cycle.md` owns the *shape* of a review's output… role documents state only what their role must inspect, not what fields the report carries." Cycle 17 applied it to the merging policy and deferred the role documents to their own cycle. The schema's mapping table already absorbs these items: "Risks, verification gaps" → `Consequence` and `Not inspected`; "Evidence inspected; Scope reviewed" → `Scope`, `Cross-checked`; "What Dave should inspect" → `Dave should inspect`; the overall call → `Verdict`.
Consequence: Criterion 4 and A2's settled rule, with the divergence already realised inside one file rather than across two. An agent cannot satisfy both: filling the template omits security/privacy risks, which the list requires; filling the list omits the human-gate confirmation, which the template requires. Neither produces a conforming review artifact — the schema requires `Not inspected` as a header field and per-finding `Evidence` distinguishing verified-by-running from inferred-by-reading, and neither of these two carries either.
Fix: Delete both :76-91 and :167-213. What must survive is the content the schema does not carry and that is genuinely about what this role *inspects* rather than what it emits: the "Review inputs" list at :59-73 already states that, and stays. If any template item names an inspection this role must make and the Review inputs list does not — "Human-gate required" is the candidate — add it there as an inspection, not as an output field.
Related: SK-1, SK-3, SK-4

## SK-3 — blocking
Claim: The Output template has this role emitting the ship recommendation, using the four-item vocabulary roles/release-manager-agent.md states as its own, for a call operating-model assigns to the Release Manager.
Location: roles/skeptic-risk-agent.md:208-209
Evidence: Verified by running and by reading. :209: "- ship / ship with accepted risks / do not ship / needs Dave decision". roles/release-manager-agent.md:44-51, "Recommendation vocabulary — Use one of:", lists the same four in the same order; `diff` of the two four-item lists returns empty. skills/release-readiness-review.md:43-48 carries the same four again — that skill is in this bundle (`audience: [release-manager-agent, skeptic-risk-agent, human]`). operating-model.md:122-123: step 7 is "Skeptic/risk review — judgment on false confidence, mocked-boundary and live-integration gaps, config/deploy risk, and release overclaims, over the whole evidence chain. *(Skeptic/Risk)*"; step 8 is "**Release package** — assemble evidence and a ship recommendation. *(Release Manager)*".
Consequence: Criterion 4 and a responsibility assigned to two roles. operating-model separates the two steps deliberately, and this file's own Required output asks for a "Recommended next step" (:90) — which is the correct scope for step 7 — while its template asks for a ship call, which is step 8's. The concrete failure is a release package containing two ship recommendations from two roles with no rule for which governs, and the Skeptic making the call it exists to be independent of. "needs Dave decision" in this position also runs into SK-1: as a *ship call* it is coherent, since operating-model's two-tier gate requires Dave's go/no-go on consequential changes; as this file uses it at :140 it is a *gap label*, which LEXICON rules out. Both uses are in the file and nothing distinguishes them.
Fix: Delete :208-209 with the rest of the template (SK-2). The Skeptic's output is a next step and a set of labelled gaps; the ship call is the Release Manager's, and roles/release-manager-agent.md:44-51 is where the vocabulary lives. If the Skeptic must signal "this should not ship", it does so by marking a gap `blocking` per LEXICON.
Related: SK-1, SK-2

## SK-4 — non-blocking
Claim: The Boundary checklist is skills/boundary-audit.md's Procedure, a bundle-mate, restated as questions.
Location: roles/skeptic-risk-agent.md:111-121
Evidence: Verified by reading both at ed926db. skills/boundary-audit.md carries `audience: [reviewer-agent, skeptic-risk-agent, release-manager-agent, human]`, so it is in this bundle. Item for item:

| This file (:113-121) | skills/boundary-audit.md Procedure |
| --- | --- |
| 1. What production behavior is represented? | 1. List all affected production behaviors. |
| 2. What evidence exists? | 2. Identify which behaviors are tested locally. |
| 3. What verification class is this evidence? | 3. Identify which tests use mocks, fixtures, jsdom, fakes, or generated data. |
| 4. What claims are supported? | 4. For each boundary, state what is verified. |
| 5. What claims are unsupported? | 5. For each boundary, state what is not verified. |
| 6. What live/browser/production evidence is needed? | 6. Assign a deferred verification path. |
| 7. Is the missing evidence blocking, deferred, accepted, or not material? | 7. Mark unresolved gaps as accepted risk, deferred, or blocking. |

Seven items against seven, in the same order, on the same axis. Note the two disagree at item 7 on the label set — this file has four, the skill has three, and LEXICON has four (SK-1).
Consequence: Criterion 10. The skill is the procedural home — it also states inputs, a use-when list, and an output shape the checklist does not — and both are in the same bundle, so a Skeptic receives the same seven-step audit twice with a label mismatch at the last step.
Fix: Delete :111-121 and let skills/boundary-audit.md carry it. Conform that skill's step 7 to LEXICON's four labels as a dependency — it is not in this cycle's scope, so it is named here rather than raised as a finding against it.
Related: SK-1, SK-2

## SK-5 — non-blocking
Claim: One vendor name that diverges from a term cycle 17 fixed elsewhere, and two technology names that presuppose a JavaScript stack.
Location: roles/skeptic-risk-agent.md:206 ("GitHub issue"), :44 and :99 ("jsdom"), :107 ("service worker/PWA")
Evidence: Verified by running `grep -nEi '(github|gitlab|claude|anthropic|jira|linear|jsdom)' roles/skeptic-risk-agent.md`. :206: "(yes / no; if yes, confirm whether human-gate GitHub issue is open and linked)". Cycle 17 directed "'human-gate tracker issue' is the term" and applied it to roles/release-manager-agent.md, which now reads "tracker issue" at :20 and :40; this file was not in that cycle's scope. On the technology names: :44 "jsdom can hide browser failures", :99 "jsdom component test proves browser rendering", :107 "unit tests prove service worker/PWA behavior".
Consequence: Criterion 8 and Core rule 13 for :206 — the repository now names the same artifact two ways, and the divergence was introduced by fixing one file and not its neighbour. For the technology names, criterion 8 at the margin and criterion 1 more directly: this is a methodology document compiled into bundles for projects whose stack it does not know, and a Skeptic on a project with no JavaScript reads two of thirteen false-confidence patterns that cannot apply. context-sets/testing-and-verification.md:254 states the same rule stack-neutrally — "treating a headless DOM as browser rendering" — which is the available wording. The rules are correct where the stack matches, which is why this is non-blocking rather than blocking.
Fix: :206 becomes "tracker issue" — moot if SK-2 deletes the template, but the term must land wherever the human-gate inspection survives. :44 and :99 become "a headless DOM", per the wording already in context-sets/testing-and-verification.md. :107 becomes "unit tests prove background-worker or installed-app behavior", or is deleted if the general case is already covered by :99.
Related: SK-2

## SK-6 — non-blocking
Claim: The mandate sentence restates operating-model, and the file does not state which session kind it addresses.
Location: roles/skeptic-risk-agent.md:13; and the whole file for session kind
Evidence: Verified by reading. :13: "This role is mandatory for meaningful changes where Dave will not perform default human code review." operating-model.md:122, change flow step 7, places skeptic/risk review in the flow for meaningful changes; :18 states "Dave does not rely on routine line-by-line code review. The primary control is evidence"; :111-113 defines a meaningful change and states that each stage completes before the next begins. Separately, no sentence in this file names a decision session or an execution session.
Consequence: Criterion 4 for :13 — the sentence is operating-model's premise and step 7 combined, and operating-model is in this bundle. Criterion 7 for the omission: this role reviews an evidence chain, which is execution-session work against a working tree, but the same file's Review inputs list includes "release-readiness claims" and "operational notes", which reach a decision session too. The file should say which.
Fix: Delete :13. Add one line under the title naming the session kind.

## SK-7 — non-blocking
Claim: One Non-goal restates operating-model; the rest restate the file's own "Do not assume" list.
Location: roles/skeptic-risk-agent.md:215-223
Evidence: Verified by reading. :222 "duplicate the general Reviewer Agent role" ↔ operating-model.md:126-128, which states the Reviewer/Skeptic separation and what each asks. :219 "block work for theoretical perfection" ↔ :55 "theoretical concerns should stop progress"; :220 "demand exhaustive testing" ↔ :53 "every gap requires automation" and :54 "live tests belong in every fast test run"; :223 "treat every unverified behavior as equally important" ↔ :52 "all risks are blockers" and :57 "The job is to distinguish material risk from acceptable risk".
Consequence: Criterion 4 and criterion 6. Four of the five Non-goals are the "Do not assume" list restated as prohibitions twenty pages later in the same file; the fifth is operating-model's. The one item with no counterpart is :221, "rewrite the implementation by default".
Fix: Delete :215-223 except :221, which can move into Review inputs beside :74 — it is the same point that this role reviews the evidence chain rather than the code.
Related: SK-6

## SK-8 — observation
Claim: `audience:` includes `chief-of-staff`, which selects this role document into the Chief of Staff's bundle along with the other ten role documents.
Location: roles/skeptic-risk-agent.md:4
Evidence: Verified by running `grep -rn "audience:" --include='*.md' roles/`. All eleven files in `roles/` list `chief-of-staff` except roles/chief-of-staff.md, whose own audience is `[chief-of-staff, human]`. Inferred, not observed: audience selection is not implemented at ed926db. This file is the largest of the eleven at 227 lines, so it is also the largest single contributor to that bundle.
Consequence: Criterion 2, at the margin — the selector widens where its job is to narrow.
Fix: None proposed here. The pattern is identical across all eleven role documents; settle it once rather than per file.

## SK-9 — observation
Claim: Every rule is stated in the third person about the Skeptic/Risk Agent rather than as an instruction to the agent reading the bundle.
Location: roles/skeptic-risk-agent.md:11, :21, :61, :74, :217
Evidence: Verified by reading. The exceptions are the two best sections: "Assume:" / "Do not assume:" (:39, :50) and "Flag any statement equivalent to:" (:95) are written as direct instructions, and they are also the sections criterion 10 finds carry the file.
Consequence: Criterion 5, at the margin. The rules are instructions, so the criterion is not failed; the reader must identify itself as "the Skeptic/Risk Agent" before any of them binds.
Fix: Second person throughout, on the model of :39 and :95. The same pattern runs through all six roles in this cycle.
