# Review: policies/agent-review-policy.md — cycle 1

Verdict: changes-required
Reviewed: policies/agent-review-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (106 lines), against docs/global-context/review-rubric.md @ 2a722bb, all ten criteria.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ 2a722bb); roles/reviewer-agent.md, roles/spec-reviewer-agent.md, roles/skeptic-risk-agent.md, roles/release-manager-agent.md; skills/spec-review-cycle.md; policies/decision-log-policy.md, policies/testing-policy.md, policies/document-metadata-policy.md.
Not inspected: the four role documents against their own rubric criteria — they are in a later cycle, and this review reads them only as evidence of where a rule already lives; roles/context-quality-reviewer.md and roles/orchestrator-agent.md; whether any bundle currently selects this policy and a role document together.
Findings: 5 — 2 blocking, 2 non-blocking, 1 observation
Dave should inspect: A1 and A5 together. A1 proposes merging this file away; A5 is the cost — skills/spec-review-cycle.md names this policy by path in the table that disambiguates "Recommendation", and that table has to be re-pointed in the same change. The merge is cheap; leaving the table pointing at a deleted file is the failure mode.

## Criterion 10, first and explicitly

**merge-into `roles/reviewer-agent.md`.**

Every rule in this file is already stated in a role document, in
`operating-model.md`, or in Core. Two sentences are word-for-word identical to
`roles/reviewer-agent.md` (A1). The residue that is not duplicated is two items
— the Prohibited review patterns list and the Dave-facing summary requirement —
and neither needs a policy of its own: the first is a review-quality rule and
lands in `roles/reviewer-agent.md`; the second is already a field in the review
artifact schema. The file does not contribute something no other file in its
bundle states, which is the criterion-10 test, so it is merged rather than
fixed.

Named target for the residue: `roles/reviewer-agent.md`. Secondary landing for
the Dave-facing summary: the `Dave should inspect` field already defined in
`skills/spec-review-cycle.md`.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass — nothing here assumes the reader can open another file |
| 2 | `audience:` is the selector | fail — `[all-roles, human]` selects this into every role's bundle, including roles that perform no review; A3 |
| 3 | No path references | pass — the only file in this cycle's scope with zero path-shaped references |
| 4 | Core states it → remove it here | fail — A1, A2, A4; the dominant defect |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | pass — the file is unusually clean here; it states rules and stops |
| 7 | Session kind explicit | fail — A5 (observation); review happens in both kinds and the file says neither |
| 8 | Tiers, not model names | pass — no vendor name, no model name, no use of the retired *track*, *dispatch*, *sync block*, or *prompt* |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | fail — merge, see above |

## A1 — blocking
Claim: Every section of this policy restates content already held by a role document or by operating-model.md, including two sentences that are byte-identical to roles/reviewer-agent.md.
Location: policies/agent-review-policy.md:13-106 (the whole body below Purpose)
Evidence: Verified by running. `diff <(sed -n '43,44p' policies/agent-review-policy.md) <(sed -n '11,12p' roles/reviewer-agent.md)` returns empty — the two-sentence hard-gate statement is identical. The remaining mapping, verified by reading both texts at 2a722bb:

| This file | Already stated in |
| --- | --- |
| 15 Core rule — evaluate the evidence package | core.md:21 rule 5, core.md:26 rule 10; operating-model.md:29 "Manage the proof, not the code" |
| 19-25 Required review posture | roles/skeptic-risk-agent.md:38-47 "Required posture" — a superset, same three lead assumptions |
| 31-39 Spec Reviewer focuses on | roles/spec-reviewer-agent.md (role scope and continuity scan) |
| 43-44 Reviewer Agent is a hard gate | roles/reviewer-agent.md:11-12 — **identical** |
| 46-53 Reviewer Agent focuses on | roles/reviewer-agent.md:17-24 Responsibilities |
| 57-66 Skeptic/Risk focuses on | roles/skeptic-risk-agent.md:21-34 Responsibilities |
| 70-75 Release Manager focuses on | roles/release-manager-agent.md:13-21 Responsibilities |
| 79-87 Required review output | roles/reviewer-agent.md:26-33; roles/release-manager-agent.md:25-35; operating-model.md:178-186 — see A2 |
| 91-98 Prohibited review patterns | roles/reviewer-agent.md:39 (partial); core.md:26 rule 10 (partial) — the only substantially non-duplicated rule |
| 102-106 Dave-facing summary | skills/spec-review-cycle.md review artifact schema, `Dave should inspect` field |

Consequence: Criterion 4 and criterion 10. The file is a second, shorter, and already-diverging copy of four role documents. Divergence has begun: the posture list here has five assumptions where the skeptic role has eight, and the output list here has seven items where the reviewer role has six. An agent whose bundle carries both a role document and this policy receives two specifications of its own job and no rule for which wins. Because `audience: [all-roles]` puts this file in every bundle (A3), that collision is the normal case rather than an edge one.
Fix: Merge into `roles/reviewer-agent.md`: carry across the Prohibited review patterns list (91-98) and the sentence "A useful review must state what was checked and what was not checked", which sharpens the role document's existing weaker "should say what was inspected". Carry the Dave-facing summary requirement (102-106) nowhere — it is already the `Dave should inspect` field in the artifact schema. Delete the rest as duplicated. Then retire the file, and update the dependency in A5.
Related: A2, A5

## A2 — blocking
Claim: Four documents state a "required review output" list, and the four lists disagree.
Location: policies/agent-review-policy.md:79-87
Evidence: Verified by reading all four at 2a722bb. This file (79-87): Scope reviewed, Evidence inspected, Findings, Risks, Verification gaps, Required follow-ups, Recommendation — 7 items. roles/reviewer-agent.md:26-33: scope reviewed, evidence inspected, findings, required changes, optional improvements, recommendation — 6 items, and it splits findings into required/optional where this file does not. roles/release-manager-agent.md:25-35: 10 numbered items on a different axis entirely. operating-model.md:178-186 Standard response shape: Role, Intent, Evidence, Boundary, Gaps, Recommendation, Dave decision points — 7 items, different ones. skills/spec-review-cycle.md already anticipates the collision, mapping "Required changes" → `blocking` entries and "Advisory items" → `non-blocking`, and warns explicitly that "Recommendation" means two different things across this policy and the artifact schema.
Consequence: A reviewer cannot satisfy all four. Omitting "Risks" and "Verification gaps" conforms to the reviewer role document and violates this policy; including "optional improvements" conforms to the role document and is unnamed here. The artifact schema's mapping table exists precisely to repair this, which is evidence the duplication is already costing something rather than a hypothetical.
Fix: One home. Proposed: the review artifact schema in `skills/spec-review-cycle.md` owns the *shape* of a review's output, since it already claims that mapping and `last-reviewed:` makes it load-bearing; role documents state only what their role must inspect, not what fields the report carries. Delete 79-87 here as part of the merge.
Related: A1

## A3 — non-blocking
Claim: `audience: [all-roles, human]` selects a review-only policy into the bundle of every role, including roles that perform no review.
Location: policies/agent-review-policy.md:4
Evidence: Verified by reading the frontmatter against document-metadata-policy.md:95-98, which defines `audience:` values as `roles/` slugs plus the reserved `all-roles` and `human`, and against the eleven files in `roles/`. Coder, Test Designer, Architect, and PM/EM/Owner perform no step this file governs.
Consequence: Criterion 2. The selector is doing the opposite of its job: it widens rather than narrows, so the file lands in bundles where it is inert context, and — per A1 — lands *alongside* the role document it duplicates, which is where the two-specifications collision actually bites.
Fix: Subsumed by the merge. If the file were retained instead, `audience:` would narrow to `[reviewer-agent, spec-reviewer-agent, skeptic-risk-agent, release-manager-agent, chief-of-staff, human]`.
Related: A1

## A4 — non-blocking
Claim: The Required review posture list is a subset of roles/skeptic-risk-agent.md's Required posture, with three of five assumptions in near-identical wording.
Location: policies/agent-review-policy.md:19-25
Evidence: Verified by reading. Here: "implementation may be plausible but wrong" / "tests may pass while proving less than claimed" / "mocks may hide important production failures". roles/skeptic-risk-agent.md:40-42: "an implementation can be plausible but wrong" / "tests can be green while proving less than claimed" / "mocks can hide production failures". The role document adds five further assumptions and a "Do not assume" counter-list this file lacks.
Consequence: Criterion 4. The weaker copy is the one selected into every bundle (A3), so the common case is that an agent receives the five-item version and never the eight-item version with its calibrating counter-list — the subset actively displaces the better rule.
Fix: Delete 19-25 as part of the merge. The posture's home is roles/skeptic-risk-agent.md.
Related: A1

## A5 — observation
Claim: skills/spec-review-cycle.md references this policy by path in a table that resolves a naming ambiguity, so merging this file requires editing that table in the same change; and this file does not state which session kind it addresses.
Location: policies/agent-review-policy.md — whole file; the external reference is skills/spec-review-cycle.md, "What this schema governs" table and the note beneath it.
Evidence: Verified by reading skills/spec-review-cycle.md @ 2a722bb: "`roles/spec-reviewer-agent.md` and `policies/agent-review-policy.md` govern the **review** — what must be inspected and what must be reported", followed by "Note the entry field is `Fix`, not `Recommendation`. `policies/agent-review-policy.md` uses 'Recommendation' for the overall ship call, and one word meaning two things across two canonical documents is the ambiguity this table exists to remove."
Consequence: Core rule 13 — a changed fact changes everywhere it appears. Merging this file without re-pointing that table leaves the schema citing a deleted path to explain a distinction whose other half has moved, which converts a resolved ambiguity back into an open one. Separately, criterion 7: review happens in both session kinds and the file names neither, so a reader cannot tell whether these rules bind a decision session reviewing a document or an execution session reviewing a diff.
Fix: Re-point the schema's table and note at `roles/reviewer-agent.md` in the same change package as the merge. skills/spec-review-cycle.md is not in this cycle's scope, so the edit is named here as a dependency rather than as a finding against that file. Session kind is moot once the file merges; the receiving role document states its own.
Related: A1
