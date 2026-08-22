# Review: roles/reviewer-agent.md — cycle 1

Verdict: changes-required
Reviewed: roles/reviewer-agent.md @ ed926db174887c54a701b8fc4f0a35726bdc027a
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (53 lines), against docs/global-context/review-rubric.md @ ed926db, all ten criteria. The two sections cycle 17 merged in from policies/agent-review-policy.md — Prohibited review patterns (:40-47) and the what-was-checked sentence (:38) — are inspected as part of the file, on the same footing as the rest.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ ed926db); roles/skeptic-risk-agent.md and roles/spec-reviewer-agent.md on the two Non-goals; skills/spec-review-cycle.md review artifact schema; skills/evidence-review.md, skills/boundary-audit.md and skills/test-plan-review.md as bundle-mates; reviews/agent-review-policy-cycle-1.md findings A1, A2, A5; docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md.
Not inspected: roles/spec-reviewer-agent.md against its own rubric criteria (cycle 19a) — read only to confirm it is not a bundle-mate of this file and to check the Non-goal at :53; skills/spec-review-cycle.md against its own criteria — read only for the artifact schema and the table A5 names; whether `bin/bundle` in fact composes the bundle this review reasons about — audience selection is not implemented at ed926db, so every bundle-composition claim here is inferred from `audience:` frontmatter plus the settled selector rule, not observed from a generated bundle.
Findings: 7 — 1 blocking, 4 non-blocking, 2 observations
Dave should inspect: RV-1 and its dependency together. Deleting the Required outputs list is what finding A2 settled and what cycle 17 deferred to this cycle — but the word "recommendation" in that list is the referent of the note in skills/spec-review-cycle.md that disambiguates `Fix` from `Recommendation`. A5 re-pointed that note at this file three commits ago; deleting the list it points at makes the note cite a file that no longer contains the thing it cites. The two edits go in one change or the ambiguity A5 closed reopens.

## Criterion 10, first and explicitly

**retain-with-changes.**

The file contributes two things no bundle-mate states. The first is the
Reviewer/Spec-Reviewer boundary at :53 — "It reviews implementation quality and
consistency, not spec documents." roles/spec-reviewer-agent.md carries
`audience: [spec-reviewer-agent, chief-of-staff, human]` and is therefore *not*
in this bundle, so this sentence is the only thing in the Reviewer's bundle that
prevents an agent holding it from reviewing a PRD. The second is the Prohibited
review patterns list (:40-47), which cycle 17 carried in from
policies/agent-review-policy.md precisely because it was the one substantially
non-duplicated rule in that file (reviews/agent-review-policy-cycle-1.md, A1).
Both survive.

The residue is thinner than the file's length suggests — the hard-gate
statement, the Required outputs list, and the first Non-goal all come out — but
it is real, and retirement is not available in any case: `audience:` values are
`roles/` file slugs (policies/document-metadata-policy.md:91-93), so deleting
the file deletes the `reviewer-agent` selector and leaves `bin/bundle
reviewer-agent` compiling a bundle that never says what the receiving agent is
for. This file is also, after cycle 17, the merge target of a retired policy;
retiring it now would strand that merge.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass — nothing here assumes the reader can open another file |
| 2 | `audience:` is the selector | pass with an observation — `reviewer-agent` is the file's own slug; `chief-of-staff` widens rather than narrows, RV-6 |
| 3 | No path references | pass — zero path-shaped references; one of two files in this cycle that is clean here |
| 4 | Core states it → remove it here | fail — RV-1, RV-3, RV-5 |
| 5 | Agent instruction, not authoring principle | pass — every rule is an instruction, in the third person; RV-7 |
| 6 | Instructions, not rationale | fail — RV-2; the file states the same obligation twice, in two strengths |
| 7 | Session kind explicit | fail — RV-4, and this is the half of finding A5 that A5 explicitly deferred to this file |
| 8 | Tiers, not model names | pass — no vendor name, no model name, no tier language, none of the four retired terms |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass — retain-with-changes, see above |

## Counts

- Rules restated from Core, decision-layer, LEXICON, or operating-model: **2** — the hard-gate statement and the flow ordering it carries (RV-3), and the Reviewer/Skeptic distinction (RV-5). Plus one rule restated from within the file itself (RV-2).
- Output-shape lists belonging elsewhere: **1** — Required outputs (:23-32), which the review artifact schema in skills/spec-review-cycle.md owns under A2's settled rule; RV-1.
- Path-shaped references: **0.**
- Vendor and model names: **0.**
- Retired terms (dispatch, sync block, track, prompt): **0.**

## RV-1 — blocking
Claim: The Required outputs list states the shape of a review's output, which finding A2 settled belongs to the review artifact schema, and its deletion breaks a citation in that schema unless the two are changed together.
Location: roles/reviewer-agent.md:23-32
Evidence: Verified by reading at ed926db. The list: scope reviewed, evidence inspected, findings, required changes, optional improvements, recommendation — six items. reviews/agent-review-policy-cycle-1.md, A2, Fix: "the review artifact schema in `skills/spec-review-cycle.md` owns the *shape* of a review's output… role documents state only what their role must inspect, not what fields the report carries." Cycle 17 applied A2 to the merging policy and deferred this file: "A2: the review artifact schema in skills/spec-review-cycle.md owns the output shape; delete the list here; role documents are trimmed in their own cycle" (docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md, agent-review-policy disposition). This is that cycle. The schema's own mapping table already absorbs all six items: "Evidence inspected; Scope reviewed" → `Scope`, `Cross-checked`; "Required changes" → entries marked `blocking`; "Advisory items" → `non-blocking`; "Sign-off; Recommendation (the overall ship call)" → `Verdict`.

The dependency, verified by reading skills/spec-review-cycle.md at ed926db: the note beneath that table reads "Note the entry field is `Fix`, not `Recommendation`. `roles/reviewer-agent.md` uses 'Recommendation' for the overall ship call, and one word meaning two things across two canonical documents is the ambiguity this table exists to remove." That sentence cites *this file* — the citation is the product of cycle 17's A5 disposition, which re-pointed it here from the deleted policy — and the only occurrence of "recommendation" in this file is :32, inside the list this finding deletes.
Consequence: Criterion 4 and A2's settled rule. Two documents specify what a Reviewer hands over, and they are not reconcilable item for item: the role document names "optional improvements" and the schema has no such field, while the schema requires `Not inspected`, `Consequence` per finding, and evidence classed as verified-by-running versus inferred-by-reading, none of which this list mentions. A Reviewer that satisfies the six items has not written a conforming artifact. Then the second-order cost: delete the list without touching the schema and the note explains a distinction by citing a file that no longer makes it, which converts a resolved ambiguity back into an open one — Core rule 13, and exactly the failure A5 was raised to prevent.
Fix: Delete :23-32. In the same change, edit the note in skills/spec-review-cycle.md so it no longer rests on this file's wording — either drop the second sentence and keep "Note the entry field is `Fix`, not `Recommendation`", or restate the ambiguity without a citation. skills/spec-review-cycle.md is not in this cycle's scope, so that edit is named here as a dependency rather than as a finding against it, on A5's precedent.
Related: RV-2

## RV-2 — non-blocking
Claim: The file states the what-was-inspected obligation twice, in two strengths, and the two disagree.
Location: roles/reviewer-agent.md:9 (second sentence) and :38
Evidence: Verified by reading at ed926db. :9: "If only a subset was reviewed, state what was and was not inspected." :38: "A useful review must state what was checked and what was not checked." The second is the sentence cycle 17 carried in from policies/agent-review-policy.md — its A1 Fix named it explicitly, on the grounds that it "sharpens the role document's existing weaker" statement. It was added; the weaker statement was not removed.
Consequence: Criterion 6 and criterion 4 within one file. :9 makes the obligation conditional on having reviewed a subset; :38 makes it unconditional. A Reviewer that reviewed everything satisfies :9 by saying nothing and violates :38. The schema settles it in the same direction as :38 — `Not inspected` is a required header field, "required precisely because omitting it is how an unbounded claim gets made by accident" — so the conditional version is the one that is wrong, and it is the one in the file's opening paragraph where it is read first.
Fix: Delete the second sentence of :9. :38 states it unconditionally and correctly. Fold :38 up into the opening paragraph if the "Review posture" heading is not carrying its weight after :36 goes (see RV-5).
Related: RV-1

## RV-3 — non-blocking
Claim: The hard-gate statement restates operating-model's change flow, including the flow ordering.
Location: roles/reviewer-agent.md:11-12
Evidence: Verified by reading both at ed926db. This file: "The Reviewer Agent is a **hard gate**. A meaningful change does not proceed to Skeptic/Risk review or release without a Reviewer Agent sign-off." operating-model.md:121, change flow step 6: "**Quality review** — judgment on maintainability, correctness, consistency, and test adequacy, over the diff and the mechanical results. *(Reviewer — hard gate)*", followed by step 7 (Skeptic/Risk) and step 8 (Release package); and :112-113, "Each stage completes before the next begins; no skipping or working ahead." operating-model.md carries `audience: [all-roles, human]`, order 3, so it is in this bundle ahead of this file.
Consequence: Criterion 4. This is the case the directive's Context names: operating-model's change flow already assigns this role its step, and a role document that restates the flow is restating operating-model. The two agree today; the cost is that they must be kept agreeing.
Fix: Delete :11-12. operating-model states both the hard gate and the ordering, in this bundle.
Related: RV-5

## RV-4 — non-blocking
Claim: The file does not state which session kind it addresses, and this is the obligation finding A5 assigned to it.
Location: roles/reviewer-agent.md — whole file
Evidence: Verified by reading. No sentence names a decision session or an execution session. reviews/agent-review-policy-cycle-1.md, A5: "criterion 7: review happens in both session kinds and the file names neither… Session kind is moot once the file merges; the receiving role document states its own." This file is the receiving role document, and it does not.
Consequence: Criterion 7. The ambiguity is live rather than formal. This file's own :9 describes reviewing "the diff" — execution-session work against a working tree — while operating-model.md:115 puts any canonical document, methodology documents included, through the Spec Reviewer gate, and the Prohibited review patterns list at :40-47 reads naturally as governing both. A Reviewer receiving this bundle in a decision session cannot tell whether these rules bind it.
Fix: One line under the title naming the kind. On the evidence of :9 and :19-21 — diff, tests, boundary updates — the answer is an execution session; if the intent is both, say both and say what differs.

## RV-5 — non-blocking
Claim: The first Non-goal restates a distinction operating-model already draws; the second does not and must stay.
Location: roles/reviewer-agent.md:49-53
Evidence: Verified by reading at ed926db. :51: "The Reviewer Agent is not the same as the Skeptic/Risk Agent. It should review general quality, not only false confidence and operational risk." operating-model.md:126-128: "Quality review (6) and skeptic/risk review (7) are deliberately separate — quality review asks 'is this good?'; skeptic/risk asks 'where is this lying to us?' — and a change can pass one and fail the other." operating-model is in this bundle. By contrast :53 — "The Reviewer Agent is not the same as the Spec Reviewer Agent. It reviews implementation quality and consistency, not spec documents" — has no counterpart in the foundation, and roles/spec-reviewer-agent.md is not a bundle-mate (`audience: [spec-reviewer-agent, chief-of-staff, human]`), verified by running `grep -rn "audience:" --include='*.md' roles/`.
Consequence: Criterion 4 for :51 only. operating-model's version is the better of the two — it says what each review asks, which this one does not — so the duplicate is also the weaker copy.
Fix: Delete :51. Keep :53; it is load-bearing and unique to this bundle. Also delete :36 ("The Reviewer Agent should be constructive but skeptical") — it states a disposition, not an instruction, and the Prohibited review patterns list at :40-47 is what actually enforces it.
Related: RV-3

## RV-6 — observation
Claim: `audience:` includes `chief-of-staff`, which selects this role document into the Chief of Staff's bundle along with the other ten role documents.
Location: roles/reviewer-agent.md:4
Evidence: Verified by running `grep -rn "audience:" --include='*.md' roles/`. All eleven files in `roles/` list `chief-of-staff` except roles/chief-of-staff.md, whose own audience is `[chief-of-staff, human]`. Inferred, not observed: audience selection is not implemented at ed926db.
Consequence: Criterion 2, at the margin — the selector widens where its job is to narrow.
Fix: None proposed here. The pattern is identical across all eleven role documents; settle it once rather than per file.

## RV-7 — observation
Claim: Every rule is stated in the third person about the Reviewer Agent rather than as an instruction to the agent reading the bundle.
Location: roles/reviewer-agent.md:9, :11, :36, :51, :53
Evidence: Verified by reading. The exception is the Prohibited review patterns list at :42, "Do not submit reviews that only say" — the one section cycle 17 carried in from elsewhere is also the one written as a direct instruction.
Consequence: Criterion 5, at the margin. The rules are instructions, so the criterion is not failed; the reader must identify itself as "the Reviewer Agent" before any of them binds.
Fix: Second person throughout, on the model of :42. The same pattern runs through all six roles in this cycle.
