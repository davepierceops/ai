# Review: roles/test-designer-agent.md — cycle 1

Verdict: changes-required
Reviewed: roles/test-designer-agent.md @ ed926db174887c54a701b8fc4f0a35726bdc027a
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (54 lines), against docs/global-context/review-rubric.md @ ed926db, all ten criteria.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ ed926db); roles/coder-agent.md on the separation rule; context-sets/testing-and-verification.md and skills/test-plan-review.md as bundle-mates; reviews/agent-review-policy-cycle-1.md finding A2; the bundle-mate set computed from `audience:` frontmatter across the repository.
Not inspected: context-sets/testing-and-verification.md and skills/test-plan-review.md against their own rubric criteria — read only as evidence of where a rule already lives; policies/commit-and-change-control-policy.md as a document in its own right; whether `bin/bundle` in fact composes the bundle this review reasons about — audience selection is not implemented at ed926db, so every bundle-composition claim here is inferred from `audience:` frontmatter plus the settled selector rule, not observed from a generated bundle.
Findings: 8 — 2 blocking, 4 non-blocking, 2 observations
Dave should inspect: TD-1. Two files in the same bundle define the test plan and the lists disagree — the role document's seven items against the context set's eleven, with items unique to each. This is finding A2's defect on the test-plan axis rather than the review-output axis, and A2's settled remedy (one home) applies, but which home is the judgment call: the context set is where cycle 17 landed the testing content, the role document is where a Test Designer looks.

## Criterion 10, first and explicitly

**retain-with-changes.**

The file contributes three things no bundle-mate states: that the red-gate is
the Test Designer's to run and confirm rather than merely a stage that must have
happened (:20-21), that a test passing before implementation is a broken test
rather than a head start (:21), and the negative framing of the role's
scope — do not build large suites for their own sake (:54). The first is the
sharpest: operating-model.md:119 states the red-gate as a change-flow stage and
:126 states it is mandatory, but neither says who runs it, and
skills/test-plan-review.md:35-36 has the *reviewer* of a plan check that a
red-gate step is present. This file is the only place that assigns the running
of it.

Everything else in the file is stated by operating-model, by
context-sets/testing-and-verification.md, or by skills/test-plan-review.md, all
three of which are in this bundle. The residue is small but real and specific,
so the file earns its place; and as with the other five roles, retirement is not
available in any case, because `audience:` values are `roles/` file slugs
(policies/document-metadata-policy.md:91-93) and deleting the file deletes the
selector that addresses the bundle.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass with one exception — self-contained apart from the reference at :50; TD-5 |
| 2 | `audience:` is the selector | pass with an observation — `test-designer-agent` is the file's own slug; `chief-of-staff` widens rather than narrows, TD-7 |
| 3 | No path references | fail — 1 reference at :50; TD-5 |
| 4 | Core states it → remove it here | fail — TD-1, TD-2, TD-3, TD-4 |
| 5 | Agent instruction, not authoring principle | pass — every rule is an instruction, in the third person; see the note under TD-8 |
| 6 | Instructions, not rationale | fail — TD-2; the separation section closes with an argument for itself |
| 7 | Session kind explicit | fail — TD-6 |
| 8 | Tiers, not model names | pass — no vendor name, no model name, no tier language, none of the four retired terms. "browser/PWA requirements" (:31) names a technology but not a vendor; recorded, not flagged |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass — retain-with-changes, see above |

## Counts

- Rules restated from Core, decision-layer, LEXICON, or operating-model: **4** — the separation rule (TD-2), and three of the four Review focus items (TD-4). By section: Responsibilities 0 against the foundation but 5 of 8 against bundle-mates (TD-3); Required outputs 0 against the foundation, whole list against a bundle-mate (TD-1); Separation 1; Review focus 3.
- Output-shape lists belonging elsewhere: **1** — Required outputs (:23-33), the test plan, which context-sets/testing-and-verification.md:186-196 also defines; TD-1. Finding A2's settled rule does not reach it — a test plan is not a review's output — so the collision is resolved on criterion 10 rather than by A2.
- Path-shaped references: **1** — :50.
- Vendor and model names: **0.**
- Retired terms (dispatch, sync block, track, prompt): **0.**

## TD-1 — blocking
Claim: Two files in this bundle define what a test plan contains, and the two lists disagree in both directions.
Location: roles/test-designer-agent.md:23-33
Evidence: Verified by reading both at ed926db and by counting: `sed -n '182,196p' context-sets/testing-and-verification.md | grep -c '^[0-9]'` returns 11; `sed -n '25,33p' roles/test-designer-agent.md | grep -c '^-'` returns 7.

| This file (7) | context-sets/testing-and-verification.md:186-196 (11) |
| --- | --- |
| behaviors under test | — **only here** |
| test levels | 2. Test levels used |
| mocks and fixtures | 3. Mocked dependencies; 4. Fixture sources |
| live verification requirements | 6. Live verification needs |
| browser/PWA requirements | 7. Browser/PWA verification needs |
| negative cases | 11. Failure cases |
| known out-of-scope cases | — **only here** |
| — | 1. Acceptance criteria — **only there** |
| — | 5. Contract assumptions — **only there** |
| — | 8. Production monitoring or synthetic checks — **only there** |
| — | 9. Known unverified behavior — **only there** |
| — | 10. Release impact of gaps — **only there** |

Both files are in the Test Designer's bundle: context-sets/testing-and-verification.md carries `audience: [all-roles, human]`. Item 11, "Failure cases", is the product of cycle 17's T2 disposition, which added it to the context set's list (docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md: "T2: add 'failure cases' as item 11 of the test-plan list in the merge target") — this file's equivalent, "negative cases", was already here and was not conformed.
Consequence: Criterion 4 and criterion 10. This is the defect A2 named, on a different axis: a Test Designer cannot satisfy both lists by satisfying either. Producing this file's seven items yields a plan with no acceptance-criteria mapping, no contract assumptions, and no release impact of gaps — the three items that carry the most weight at the release decision, and the three the context set has and this file does not. Producing the context set's eleven yields a plan with no statement of behaviors under test and no out-of-scope list. The role document is the file a Test Designer reads to learn its job, so the seven-item version is the one that gets followed, and it is the weaker of the two.
Fix: One home, per A2's settled rule applied by analogy: context-sets/testing-and-verification.md owns the shape of a test plan, this file states what the Test Designer must determine and decide. Delete :23-33. Carry the two items unique to this file — "behaviors under test" and "known out-of-scope cases" — into the context set's list in the same change; naming that edit as a dependency, since context-sets/testing-and-verification.md is through Pass 1 and is not in this cycle's scope. Do not resolve this by conforming the two lists to each other: two conformed lists diverge again, which is the history this finding records.
Related: TD-3

## TD-2 — blocking
Claim: The Test Designer / Coder separation rule is stated in three places in this bundle, and this file's statement of it closes with rationale.
Location: roles/test-designer-agent.md:44-50
Evidence: Verified by reading all three at ed926db. This file: "For a given unit of work, the Test Designer Agent and the Coder Agent must be different agents. The agent that writes the tests does not implement the unit, and the agent that implements it did not write its tests. This preserves tests as an independent specification rather than a description of code that already exists." roles/coder-agent.md:38-39, under Constraints: the Coder shall not "write the tests for the unit it is implementing (a separate Test Designer Agent owns those…)". operating-model.md:120, change flow step 5: "*(Coder — a different agent from the Test Designer for this unit)*", and :87-90, the two separations "mandatory rather than optional": "Whoever produces an artifact does not approve it."
Consequence: Criterion 4 and criterion 6. operating-model is in both roles' bundles, so the rule reaches both agents from the foundation without either role document stating it. The third sentence — "This preserves tests as an independent specification rather than a description of code that already exists" — is the argument for the rule, which criterion 6 cuts. The duplication is not currently costing a divergence: all three statements agree. It is the standing cost that three copies must be kept agreeing, which is what Core rule 13 exists to make explicit and what the two-list defect in TD-1 shows happening when they are not.
Fix: Delete :44-50. operating-model.md:120 states it in the flow and :87-90 states it as one of the two mandatory separations; both are in this bundle. If the rule is judged to need restating at the point of use, restate it in one clause inside Responsibilities and delete the rationale sentence — but the same argument then applies to roles/coder-agent.md:38-39, and one of the two should carry it, not both.
Related: roles/coder-agent.md CO-1, CO-3

## TD-3 — non-blocking
Claim: Five of the eight Responsibilities are the Procedure of skills/test-plan-review.md, a bundle-mate.
Location: roles/test-designer-agent.md:13-19
Evidence: Verified by reading both at ed926db. skills/test-plan-review.md carries `audience: [test-designer-agent, reviewer-agent, human]`, so it is in this bundle. The mapping: :13 "derive test cases from acceptance criteria" ↔ skill step 1 "Map acceptance criteria to tests"; :15 "identify mocked dependencies" ↔ step 3 "Identify mocks and fixtures"; :16 "identify live/browser verification needs" ↔ step 4, same words; :17 "identify SLO verification needs for affected Top K user journeys" ↔ step 6, same scope; :18 "specify failure cases" ↔ step 7 "Check negative/failure cases". Not duplicated: :14 "choose appropriate test levels", :19 "define what evidence will be required", :20-21 the red-gate.
Consequence: Criterion 10, at the margin rather than fatally — the skill states these as checks on a plan and this file states them as things to do, which is a real difference of stance even where the words match. But the skill also carries step 5, which checks the red-gate is present, and step 9, which recommends changes, so an agent holding both has the same five obligations described twice with no rule for which framing governs.
Fix: Optional. If the list is trimmed, keep :14, :19, :20-21 — the three the skill does not state — and let the skill carry the rest. If it is kept whole, say in one line that the skill is the review of a plan and these are the plan's construction, so the reader knows the two are not competing.
Related: TD-1

## TD-4 — non-blocking
Claim: The Review focus section restates rules from operating-model and Core, and states the release-impact distinction in words LEXICON has retired in favour of labels.
Location: roles/test-designer-agent.md:35-42
Evidence: Verified by reading at ed926db. :39 "what tests prove" and :40 "what tests do not prove" ↔ operating-model.md:76, Agents Must: "distinguish mocked, contract, live, browser, and production verification", and core.md rule 7 "Say what is unverified" and rule 6's evidence-class labelling; also context-sets/testing-and-verification.md:226-238, "Required output when tests are written or reviewed", which states "what is verified / what is not verified" as the first two of seven items. :41-42 "which gaps must be closed before release / which gaps can be deferred" ↔ LEXICON.md:65-78, Release impact labels, which defines four — `blocking`, `deferred`, `accepted-risk`, `not-material` — and states at :71 that a gap awaiting Dave's judgment is blocking.
Consequence: Criterion 4. The first two items are stated twice in the bundle already. The second two are worse than duplication: they are a two-way split of a four-label vocabulary that LEXICON.md — order 2, in every bundle — defines. A Test Designer following :41-42 sorts gaps into "must be closed" and "can be deferred" and has no bucket for `accepted-risk` or `not-material`, so a gap that is neither blocking nor deferrable gets forced into one of the two.
Fix: Delete :35-42. If the role needs a statement here at all, it is one line: mark each gap the test plan leaves open with its release impact label. LEXICON defines the labels and is in the bundle.

## TD-5 — non-blocking
Claim: One path-shaped reference.
Location: roles/test-designer-agent.md:50
Evidence: Verified by running `grep -nE '[A-Za-z0-9_/-]+\.(md|py|txt|json|yml|yaml)' roles/test-designer-agent.md`, which returns this line only: "See `policies/commit-and-change-control-policy.md`." That policy carries `audience: [all-roles, human]` and is in this bundle, so the reference resolves — but criterion 3 is not conditioned on that.
Consequence: Criterion 3. Moot once TD-2 deletes the section that contains it.
Fix: Goes with TD-2.
Related: TD-2

## TD-6 — non-blocking
Claim: The file does not state which session kind it addresses.
Location: roles/test-designer-agent.md — whole file
Evidence: Verified by reading. No sentence names a decision session or an execution session.
Consequence: Criterion 7. The answer is unambiguous — writing test code and running it against a working tree is Core's definition of an execution session — and the file's own red-gate responsibility (:20-21) only makes sense in one, so the criterion is failed on an omission with no ambiguity behind it.
Fix: One line under the title: this role runs in an execution session.

## TD-7 — observation
Claim: `audience:` includes `chief-of-staff`, which selects this role document into the Chief of Staff's bundle along with the other ten role documents.
Location: roles/test-designer-agent.md:4
Evidence: Verified by running `grep -rn "audience:" --include='*.md' roles/`. All eleven files in `roles/` list `chief-of-staff` except roles/chief-of-staff.md, whose own audience is `[chief-of-staff, human]`. Inferred, not observed: audience selection is not implemented at ed926db.
Consequence: Criterion 2, at the margin — the selector widens where its job is to narrow.
Fix: None proposed here. The pattern is identical across all eleven role documents; settle it once rather than per file.

## TD-8 — observation
Claim: The "Review focus" heading names a review this role does not perform.
Location: roles/test-designer-agent.md:35
Evidence: Verified by reading operating-model.md:115-124. The change flow assigns review to step 6 (Reviewer) and step 7 (Skeptic/Risk); the Test Designer's step is 4. The four items under the heading are judgments the Test Designer makes about its own plan, not a review gate. roles/architect-agent.md:61 carries the same heading for the same reason.
Consequence: Criterion 5, at the margin. An agent that receives this bundle and holds no other role could read the heading as authorising it to perform the review at step 6.
Fix: Moot if TD-4 deletes the section. If any of it is kept, the heading is "What the plan must distinguish".
Related: roles/architect-agent.md AR-6
