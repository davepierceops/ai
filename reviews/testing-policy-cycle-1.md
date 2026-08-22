# Review: policies/testing-policy.md — cycle 1

Verdict: changes-required
Reviewed: policies/testing-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (107 lines), against docs/global-context/review-rubric.md @ 2a722bb, all ten criteria; and against context-sets/testing-and-verification.md @ 2a722bb for the single-home check the directive requires.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ 2a722bb); context-sets/testing-and-verification.md; policies/verification-boundary-policy.md frontmatter and section headings only; policies/agent-review-policy.md, policies/decision-log-policy.md, policies/document-metadata-policy.md.
Not inspected: policies/commit-and-change-control-policy.md and context-sets/spec-and-change-discipline.md beyond confirming they exist and that the red-gate is stated in operating-model.md — both are in other cycles; policies/verification-boundary-policy.md body; roles/test-designer-agent.md; any actual test suite or bin/ tooling.
Findings: 7 — 3 blocking, 3 non-blocking, 1 observation
Dave should inspect: T2. Two live documents give different required contents for the same artifact — the test plan — and they have already drifted to eight items against ten. Whichever list survives is a real change to what a Test Designer must produce, not a formatting choice.

## Criterion 10, first and explicitly

**merge-into `context-sets/testing-and-verification.md`.**

Of nine sections, six are restatements: the green-suite disclaimer (Core rule 6
and operating-model), the red-gate (operating-model change flow step 4), the
test plan list (testing-and-verification, and divergent — T2), the mocking
checklist (testing-and-verification, the baton's named single home — T1), the
change-package evidence list (operating-model's change package), and the
release standard (Core rule 2 and operating-model's release gate). The residue
is three rules: "a test that passes before implementation is a broken test, not
a head start", the seven-level test-level ladder, and the coverage-is-a-weak-
signal rule. Three rules do not earn a policy, and all three are about how to
choose and read test evidence — which is what
`context-sets/testing-and-verification.md` already is. The baton has already
placed the mock checklist there; the rest of this file follows the same rule to
the same home.

Named target: `context-sets/testing-and-verification.md`.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — T4; lines 36-38 send the reader to two files for the scope of a rule stated here |
| 2 | `audience:` is the selector | fail (minor) — `[all-roles, human]` and no `order:`, where the merge target carries `order: 5` and the file sits in a sequence that matters |
| 3 | No path references | fail — T4 |
| 4 | Core states it → remove it here | fail — T1, T2, T5, T6, T7, T8; the dominant defect |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | pass — terse throughout; the file's one clear strength |
| 7 | Session kind explicit | fail — not stated; the merge target states "Rules for execution sessions" in its first line |
| 8 | Tiers, not model names | pass — no vendor name, no model name, no use of the retired *track*, *dispatch*, *sync block*, or *prompt* |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | fail — merge, see above |

## T1 — blocking
Claim: The Mocking section duplicates the mock-boundary checklist whose single home the baton has already assigned to context-sets/testing-and-verification.md.
Location: policies/testing-policy.md:72-83
Evidence: Verified by reading both at 2a722bb. Here (78-83): "Any mock of a meaningful boundary should be associated with: what it verifies / what it does not verify / where the deferred verification happens / whether the deferred verification is required before release" — 4 items. context-sets/testing-and-verification.md:24-32: "A mock is a claim with a deferred proof. Every mock should make the boundary visible:" followed by 6 numbered questions, which include all four of these plus "What production behavior is being represented?" and "Who or what owns the follow-up?". The baton states the disposition directly under What this session settled: "Single homes: … mock checklist in testing-and-verification".
Consequence: Criterion 4, against a single-home decision already taken. The four-item copy is strictly weaker: it never asks what production behaviour the mock stands in for, and never assigns the follow-up an owner. An agent bundled with this policy and not the context set declares a boundary with no owner and satisfies the policy exactly, which is the false-confidence failure both documents exist to prevent.
Fix: Delete 72-83. The checklist's home is context-sets/testing-and-verification.md:24-32, unchanged.
Related: T2, T3

## T2 — blocking
Claim: Two live documents state the required contents of a test plan, and the two lists disagree.
Location: policies/testing-policy.md:40-53
Evidence: Verified by reading both at 2a722bb. Here (44-53), 8 unnumbered items: behaviors to verify, test levels required, mocked dependencies, live dependencies, browser/PWA concerns, failure cases, risks intentionally not tested, acceptance criteria. context-sets/testing-and-verification.md:159-172, 10 numbered items: acceptance criteria, test levels used, mocked dependencies, fixture sources, contract assumptions, live verification needs, browser/PWA verification needs, production monitoring or synthetic checks, known unverified behavior, release impact of gaps. Overlap is six; this file uniquely requires "failure cases"; the context set uniquely requires fixture sources, contract assumptions, production monitoring, and release impact of gaps.
Consequence: A Test Designer cannot satisfy both by satisfying one. A plan built to this policy omits fixture sources and contract assumptions — the two inputs that make a mocked claim auditable — and omits release impact of gaps, which is what the release decision consumes. A plan built to the context set omits failure cases. Both are conformant and both are incomplete, and neither document acknowledges the other exists.
Fix: One home: `context-sets/testing-and-verification.md:159-172`. Add "failure cases" to that list as item 11 — it is the one genuinely missing element, not a duplicate under another name. Delete 40-53 here.
Related: T1, T3

## T3 — blocking
Claim: After the duplicated sections are removed, three rules remain, which does not sustain a standalone policy.
Location: policies/testing-policy.md — whole file
Evidence: Verified by reading the file against Core, operating-model, LEXICON, and context-sets/testing-and-verification.md at 2a722bb; the section-by-section mapping is T1, T2, T5, T6, T7, T8. Residue: line 32-34 "A test that passes before implementation is a broken test, not a head start. Implementation proceeds only as far as needed to turn the confirmed-failing tests green"; lines 59-70, the seven-level ladder; lines 85-91, coverage.
Consequence: Criterion 10. The file does not contribute something no other file in its bundle states. Retaining it retains six duplications to preserve three rules, and — as T1 and T2 show — the duplicated copies are already the weaker and diverging ones, so the cost is not merely redundancy but a second, worse specification competing with the first.
Fix: Merge the three residual rules into `context-sets/testing-and-verification.md` and retire this file. Placement: the broken-test sentence joins the red-gate wherever it is stated in the merge target or, failing that, immediately under its Summary; the seven-level ladder becomes a subsection preceding Verification classes, subject to T7; the coverage rule joins Anti-patterns.
Related: T1, T2, T5, T6, T7, T8

## T4 — non-blocking
Claim: The red-gate's scope is deferred to two other files by path.
Location: policies/testing-policy.md:36-38
Evidence: Verified by reading. "This rule applies to all tiers of change. See `policies/commit-and-change-control-policy.md` and `context-sets/spec-and-change-discipline.md`." Both files exist (verified by `ls`), so this is not a dead reference; it is a live one, which is what criterion 3 forbids.
Consequence: Criteria 1 and 3. An agent reading this inside a bundle is told the rule's reach is defined elsewhere and cannot open elsewhere. "Applies to all tiers of change" already states the reach completely; the two paths add nothing the reader can use and remove the reader's confidence that the preceding sentence is the whole rule.
Fix: Delete "See ..." across 36-38, keeping "This rule applies to all tiers of change."

## T5 — non-blocking
Claim: The green-suite disclaimer restates Core rule 6, operating-model's agent prohibition, and the merge target's Summary.
Location: policies/testing-policy.md:15-27
Evidence: Verified by reading at 2a722bb. core.md:22 rule 6: "A passing check proves the check, not the claim." operating-model.md:82, Agents must not: "equate passing tests with shippability". context-sets/testing-and-verification.md:19: "The central risk is not undertesting. The central risk is **overclaiming what a test proves**." The five "does not automatically mean" items at 23-27 map onto the Does-not-prove lists under Mock-verified and Contract-verified at testing-and-verification.md:51-59 and 71-78.
Consequence: Criterion 4. Four statements of one idea across three documents. The specific harm is that the five-item list here reads as exhaustive where the merge target's per-class lists are longer and class-specific, so an agent that checks its claim against this list and stops has done less work than the context set requires while believing it complied.
Fix: Delete 15-27.
Related: T3

## T6 — non-blocking
Claim: The red-gate rule restates operating-model.md's change flow step 4 and its mandatory-gate sentence.
Location: policies/testing-policy.md:29-34
Evidence: Verified by reading at 2a722bb. operating-model.md:119 step 4: "**Test plan, confirmed red** — ACs translated into test code, run, and confirmed to fail before any implementation. *(Test Designer)*"; operating-model.md:126: "The red-gate at step 4 is mandatory"; operating-model.md:131: "do not skip the red-gate"; operating-model.md:20: "tests are written and confirmed failing before implementation"; core rule is echoed again at operating-model.md:198.
Consequence: Criterion 4. The rule is stated five times in operating-model alone and a sixth time here. The one sentence not already stated anywhere is "A test that passes before implementation is a broken test, not a head start" — which is the sentence most worth keeping and the one currently buried in the restatement.
Fix: Delete 29-31 and 36-38; carry 32-34 to the merge target per T3.
Related: T3, T4

## T7 — non-blocking
Claim: Test levels 4 through 7 restate LEXICON's evidence classes under different names, creating a second vocabulary for the same distinctions.
Location: policies/testing-policy.md:59-70
Evidence: Verified by reading at 2a722bb. Here: "4. Contract tests for external assumptions. 5. Live smoke tests for real external services. 6. Browser/E2E smoke tests for browser-only behavior. 7. Production synthetic checks or monitoring". LEXICON.md:42-63 defines Contract-verified, Live-verified, Browser-verified, Production-verified as the evidence classes every verification claim is labelled with, and context-sets/testing-and-verification.md:36-37 states "The classes themselves are defined in the lexicon." Levels 1-3 (unit, component, integration) have no LEXICON counterpart and are genuinely additive.
Consequence: Criterion 4, and a vocabulary hazard beyond it. An agent now has two ordered vocabularies — *levels* and *classes* — that partially coincide, and the file gives no rule for which term to use in a claim. Core rule 6 requires every claim to carry its class; a claim labelled "level 5" is not labelled with a class, and this file makes that mislabelling look conformant.
Fix: Keep levels 1-3 as the additive part. For 4-7, state the level and name the evidence class it produces, rather than defining the distinction a second time — or drop 4-7 and let the classes carry it. Do not restate the class definitions in the merge target, which already points at LEXICON for them.
Related: T3

## T8 — observation
Claim: The change-package evidence list overlaps operating-model.md's change package, and the file states no session kind.
Location: policies/testing-policy.md:93-103; session kind absent throughout
Evidence: Verified by reading. Here, 7 items; operating-model.md:161-174, 12 numbered items, of which 3 (Test plan), 5 (Test results), 6 (Verification boundary updates) and 9 (Known gaps) cover most of this list. Not a clean duplication — "test commands run", "skipped tests, if any", and "recommendation on whether testing evidence is sufficient" are not in operating-model's list. Session kind: context-sets/testing-and-verification.md:11 states "Rules for execution sessions"; this file states nothing.
Consequence: Criteria 4 and 7. Weaker than T1/T2 because the divergence is additive rather than contradictory — a change package built to operating-model's list is incomplete by this file's lights but not wrong by it. The reader still has no rule for whether operating-model's twelve items are the whole package or a floor.
Fix: Fold the three additive items into operating-model.md's change package as sub-items of Test results, or into the merge target's Required output section; delete 93-103. Session kind is settled by the merge — the target already declares it.
Related: T3
