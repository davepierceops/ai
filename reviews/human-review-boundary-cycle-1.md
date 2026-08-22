# Review: boundaries/human-review-boundary.md — cycle 1

Verdict: changes-required
Disposition (criterion 10): **retain-with-changes**
Reviewed: `boundaries/human-review-boundary.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11b)
Date: 2026-08-21
Scope: the whole document, all ten rubric criteria, judged as a bundle member. Criterion 4 judged against `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md` at the same SHA. Criterion 10 judged by computing the reference closure with `bin/bundle` from all six context-set entry points, and by reading the other members of that closure that state the same rules.
Cross-checked: `operating-model.md`, `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `docs/global-context/review-rubric.md`, `context-sets/base.md`, `context-sets/spec-and-change-discipline.md`, `policies/commit-and-change-control-policy.md`, `policies/agent-review-policy.md`, `policies/document-metadata-policy.md`, `skills/spec-review-cycle.md`, `AGENTS.md`, `CLAUDE.md`
Not inspected: the eight escalation triggers were not tested against any real change or against `roles/reviewer-agent.md` / `roles/skeptic-risk-agent.md` — whether the Reviewer and Skeptic/Risk role documents actually deliver the review this file assumes was not checked, so B1's claim that the replacement controls exist is inherited from `operating-model.md`, not independently verified. `specs/`, `retros/`, `engagements/`, `.claude/**`, `vendors/claude-code/`, and `bin/` were not read. No adopting project repo was exercised. Prior review artifacts for other documents were read only where cited. Whether Dave wants the escalation list at all — the sole basis for the retain call — is his judgment and is not settled here.
Findings: 6 blocking, 2 non-blocking, 1 observation
Prior cycle: none — first artifact for this document
Dave should inspect: the criterion-10 call (B1 removes roughly half the file; what earns its place is the escalation list and the two-axes distinction, nothing else), and B5 — whether a file describing what *you* review belongs in an agent-facing bundle at all.

## Criterion pass

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — B4 |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`, both reserved values (`policies/document-metadata-policy.md:95-96`); no `order:` needed, position in a bundle does not matter |
| 3 | No references to other files by path | fail — B4 (1 reference) |
| 4 | Core states it → remove it here | fail — B1, B2, B3, N2 (6 restated rules across 4 sections) |
| 5 | Agent instruction, not authoring principle | fail — B5 |
| 6 | Instructions, not rationale | fail — B2, N1 |
| 7 | Session kind is explicit | fail — B6 |
| 8 | Tiers, not model names; route and model, not track | pass — 0 vendor names, 0 model names, 0 retired terms |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no filename |
| 10 | The file earns its place or is retired | **retain-with-changes** — see below |

## Criterion 10 — retain-with-changes

It lands in a bundle. **Verified by running** `python3 bin/bundle <entry> --format list` for all six context-set entry points (`base`, `testing-and-verification`, `spec-and-change-discipline`, `collab-workflow`, `ai-native-engineering`, `production-grade-software`): the file appears in all six closures. Unlike the other three boundary files, it is reached through *governing* documents and not only through backlog scratch — `context-sets/spec-and-change-discipline.md:165` and `policies/commit-and-change-control-policy.md:20,200` both cite it by path, and the second names it as the home of the control-surface axis it deliberately does not restate.

It contributes something no other file in that closure states: the **escalation-to-human-code-review trigger list** (eight conditions, lines 69-78) and the **two-axes distinction** (lines 62-67) — that the control surface and the release gate are independent, so a consequential change can ship without anyone reading its diff and a routine one can still be read. `operating-model.md:190` carries one bullet, *"human code inspection is warranted"*, with no criteria; `policies/commit-and-change-control-policy.md:15-21` asserts the two axes and then points here rather than stating the first one. Nothing else in the closure enumerates when a human should read code.

That is the whole of what earns the place. Everything above line 60 is restatement, rationale, or a description of Dave's behavior, and the finding list below is the edit list.

## B1 — blocking
Claim: §Required replacement controls restates `operating-model.md` §Control surfaces.
Location: `boundaries/human-review-boundary.md:46-58`
Evidence: **Verified by running** `sed -n '81,92p' operating-model.md`. Control surfaces reads: Specification / Test plan / Implementation evidence / Independent review / Verification boundaries / Operational readiness / Release judgment. This file's list reads: spec-first work / spec review / tests / independent agent review / skeptic/risk review / verification boundary documentation / release readiness review / reproducible evidence. Six of the eight map one-to-one — spec-first work/Specification, tests/Test plan, independent agent review/Independent review, verification boundary documentation/Verification boundaries, release readiness review/Release judgment, reproducible evidence/Implementation evidence. The remaining two are stated elsewhere in the same file: "spec review" is `operating-model.md:101` (change-flow step 1) and "skeptic/risk review" is `operating-model.md:108` (change-flow step 7).
Consequence: an agent reading the bundle gets the same control list twice in different words. Under Core rule 9 a reader who notices the two lists are not identical — eight items against seven, different nouns — has two sources that disagree and must surface it, which is friction generated by duplication rather than by a real disagreement. Under Core rule 13, a future edit to the control set has to find both copies or one silently goes stale.
Fix: delete lines 46-58 in full. The heading's work — *"when human code review is not used, the change must rely on"* — is already done by `operating-model.md:18` naming evidence as the primary control and §Control surfaces enumerating it.
Related: B2, B3, N2

## B2 — blocking
Claim: §Policy is a one-sentence rationale that also restates `operating-model.md:18`, and states no rule.
Location: `boundaries/human-review-boundary.md:20-21`
Evidence: **Verified by reading** both. This file: *"Because Dave is not defaulting to human code review, the system must produce stronger process evidence."* `operating-model.md:18`: *"Dave does not rely on routine line-by-line code review. The primary control is evidence: specifications, tests, reviews, verification boundaries, operational signals, and known gaps."* The sentence is a `Because X, Y` construction — an argument for the model, not an instruction to the agent reading it.
Consequence: a section headed **Policy** that contains no policy trains the reader that headings in this corpus do not mean what they say, and the section is the natural place a future editor will add a real rule, compounding the duplication B1 already records.
Fix: delete lines 20-21 including the heading.
Related: B1, N1

## B3 — blocking
Claim: §Summary opens by restating the standing claim that Dave does not default to human line-by-line code review, which is stated in six other governed files.
Location: `boundaries/human-review-boundary.md:9-12`
Evidence: **Verified by running** `grep -rn "line-by-line\|default quality gate" --include='*.md' operating-model.md context-sets/ boundaries/ policies/ AGENTS.md CLAUDE.md`. Hits: `operating-model.md:18`, `operating-model.md:53` (*"code review is not the default quality gate"*), `context-sets/base.md:15-17`, `policies/agent-review-policy.md:11`, `AGENTS.md:9`, `CLAUDE.md:23`, plus this file at `:11`. Seven copies of one claim; `operating-model.md`, `context-sets/base.md`, and this file all land in every bundle closure together.
Consequence: three copies of the same sentence arrive in one bundle. Beyond the token cost, Core rule 13 makes every one of the seven a maintenance obligation on any future change to the claim.
Fix: delete lines 11-12. Keep lines 14-17 — *"This is a boundary, not an absence of review... What this boundary removes is human diff-reading as the default, not review itself"* — which is not stated elsewhere, and reword its opening so it stands without the deleted sentence.
Related: B1, N2

## B4 — blocking
Claim: the file directs the reader to open another file by path.
Location: `boundaries/human-review-boundary.md:65`
Evidence: **Verified by running** a grep for backticked paths over the file — one hit, `` `policies/commit-and-change-control-policy.md` ``, in the parenthetical *"(see `policies/commit-and-change-control-policy.md`)"* attached to the claim that the release go/no-go is an evidence decision and not a code-reading decision.
Consequence: an agent reading this inside a generated bundle cannot follow the pointer; the sentence it supports — the load-bearing half of the two-axes distinction — arrives as an assertion with its support named but absent. This is a criterion 1 failure as much as a criterion 3 one.
Fix: delete the parenthetical. The sentence already states the claim; nothing is lost. Note that the reference is redundant in the other direction too — `policies/commit-and-change-control-policy.md:20` and `:200` already point *here*, so the pair is circular.

## B5 — blocking
Claim: §Human review includes and §Human review does not default to describe Dave's behavior, not the reading agent's, so neither is an agent instruction.
Location: `boundaries/human-review-boundary.md:23-44`
Evidence: **Verified by reading**. The sections open *"Dave may review:"* and list eleven artifacts, then four things human review does not default to. Every line is a statement about a human's habits. Rubric criterion 5 requires every rule to be an instruction to the agent reading it. The file carries `audience: [all-roles, human]`, so these 22 lines reach every agent bundle.
Consequence: an agent given a list of what Dave may read cannot act on it — there is no behavior it selects. The one operative consequence, that the agent should produce the artifacts on the list, is stated where it belongs, in `operating-model.md` §Change package and `context-sets/base.md` §Standard response shape.
Fix: delete lines 23-44. If the enumeration is wanted as a description of the operating model, its home is `operating-model.md` §Responsibilities → Dave, which already carries the short form at `:46-53`.
Related: B6

## B6 — blocking
Claim: the file does not state which session kind it is for, and its content is split across both.
Location: `boundaries/human-review-boundary.md:1-5` (frontmatter) and throughout
Evidence: **Verified by reading** the frontmatter — `status`, `last-reviewed`, `audience`, and nothing naming a session kind — against `docs/global-context/core.md:37-38`, which defines decision and execution sessions, and rubric criterion 7. §Human review includes/does not default to (B5) is decision-session material at most; §Escalation to human code review is written for whoever is deciding to escalate, which under `docs/global-context/decision-layer.md` is a decision session; nothing in the file is an instruction an execution session carries out against a working tree.
Consequence: the file is selected into execution-session bundles by `audience: [all-roles, human]` and delivers nothing an execution session acts on, spending context an executor needs for its directive. If the answer is decision-only, the audience value is wrong, not just the missing statement.
Fix: state the session kind in one line under the title. On the evidence above the honest answer is decision sessions, which also means `audience:` should narrow from `all-roles` — flag that as a change to `policies/document-metadata-policy.md` scope rather than making it here.
Related: B5

## N1 — non-blocking
Claim: §Core principle is an aphorism, not an instruction.
Location: `boundaries/human-review-boundary.md:80-82`
Evidence: **Verified by reading**: *"Human attention should be spent on judgment, not on pretending to be a compiler."* No rule is stated and no behavior is selected. `docs/research/methodology-scan-phase2-findings.md:174` records that the same principle is held a second time at `roles/chief-of-staff.md` §Handling execution-session reports (*"His attention is the scarce resource — spend it on judgment, not reading"*), which I confirmed by reading that file.
Consequence: minor — it costs three lines and is the kind of line that survives edits because it reads well, so it will still be here when the rules around it have changed.
Fix: delete lines 80-82. Non-blocking because it misleads no one.
Related: B2

## N2 — non-blocking
Claim: the Spec Reviewer gate over canonical documents is stated twice in this file and again in `operating-model.md`.
Location: `boundaries/human-review-boundary.md:29` and `:51-52`
Evidence: **Verified by reading** all three. Line 29: *"specs (PRD and TRD) — agreed by Dave after Spec Reviewer sign-off"*. Lines 51-52: *"spec review (Spec Reviewer Agent gate before Dave agrees any canonical document, specs and methodology documents alike)"*. `operating-model.md:101`: *"PRD/TRD written, reviewed by the Spec Reviewer Agent (hard gate), and agreed by Dave. The same gate covers any canonical document, methodology documents included."* Three statements of one gate, two of them in this file, and the two in this file differ in scope — line 29 says specs, lines 51-52 say any canonical document.
Consequence: the internal disagreement is the live one. A reader taking line 29 at face value concludes the gate covers PRD/TRD only, which `operating-model.md:101` contradicts. `reviews/document-metadata-policy-cycle-7.md:26` already carried a one-line instruction to delete the then-narrow form (*"before Dave agrees any spec"*) from §Required replacement controls; that instruction was executed there — lines 51-52 now read *"any canonical document"* — and the narrow form at line 29, in a different section, was not swept with it.
Fix: both lines fall out of the B1 and B5 deletions. If those are not taken, delete line 29's trailing clause at minimum.
Related: B1, B5

## O1 — observation
Claim: the file has no `order:` and its position relative to `operating-model.md` in a bundle is unspecified.
Location: `boundaries/human-review-boundary.md:1-5`
Evidence: **Verified by running** `grep -rhoE '^audience: .*' . --include='*.md' | sort | uniq -c` and reading the frontmatter of `docs/global-context/core.md` (`order: 0`), `docs/global-context/decision-layer.md` (`order: 1`), `LEXICON.md` (`order: 2`), `operating-model.md` (`order: 3`). The boundary files carry none.
Consequence: none demonstrable. Rubric criterion 2 requires `order:` only *"where its position in a bundle matters"*, and after the B1/B3/B5 cuts this file states nothing that depends on being read before or after another. Recorded as an observation, not a finding, because I cannot state what goes wrong.
