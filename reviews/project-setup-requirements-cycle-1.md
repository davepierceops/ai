# Review: policies/project-setup-requirements.md — cycle 1

Verdict: changes-required
Reviewed: policies/project-setup-requirements.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent (execution session, frontier tier)
Date: 2026-08-22
Scope: the whole file, 97 lines, against all ten rubric criteria at docs/global-context/review-rubric.md @ 2a722bb.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/verification-boundary-policy.md, policies/commit-and-change-control-policy.md, policies/release-readiness-policy.md, OPEN-ITEMS.md, reviews/expedited-log.md (existence), bin/install-hooks and bin/check-frontmatter (existence) — all @ 2a722bb.
Not inspected: the body of policies/document-metadata-policy.md (cycle 16b) — its existence and its role as the referent were confirmed, its content was not reviewed; bin/ implementations; roles/; skills/ other than spec-review-cycle.md; specs/, engagements/, writing/, vendors/.
Findings: 8 — 6 blocking, 2 non-blocking
Dave should inspect: PS-1 — this file and `policies/commit-and-change-control-policy.md` state the branch-protection requirement differently, and this one is the weaker of the two. Which file is the single home is a decision; the two-versus-four-item divergence is the risk.

## Criterion 10 first — disposition

**Retain-with-changes.**

The file lands in the `all-roles` bundle and contributes one thing no other
file in that bundle states: what must be true about a repository *before* the
methodology governs work in it. Its own Purpose makes the case that no other
mechanism can carry it — these preconditions live outside git, no hook can
enforce them, and git cannot record them. That is a real gap and this is the
only file that fills it.

What has to change is that three of its four requirements are written as
pointers to `policies/document-metadata-policy.md` rather than as statements,
one requirement contradicts a peer policy, and about a quarter of the file is
project bookkeeping addressed to nobody who reads the bundle.

The finding list below is the edit list.

## Criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — PS-4, PS-8 |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`; no `order:`, and position does not carry meaning here |
| 3 | No references to other files by path | fail — PS-4, 9 path references |
| 4 | Core states it → remove it here | pass — nothing here restates Core, the Decision Layer, LEXICON, or operating-model |
| 5 | Agent instruction, not authoring principle | fail — PS-3, PS-6 |
| 6 | Instructions, not rationale | fail — PS-6 |
| 7 | Session kind is explicit | fail — PS-7 |
| 8 | Tiers, not model names; route and model, not track | fail — PS-5 (vendor names); no model names, no retired terms ("not tracked" at :61 is the exempt sense) |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — `reviews/expedited-log.md` is a stated convention naming the file, which the criterion allows |
| 10 | The file earns its place or is retired | retain-with-changes, as above |

## PS-1 — blocking
Claim: Requirement 1 states the branch-protection requirement set as two items; `policies/commit-and-change-control-policy.md` states it as four, and this file's parenthetical leaves undecided a question that file has decided.
Location: policies/project-setup-requirements.md:29-48; policies/commit-and-change-control-policy.md:161-184
Evidence: Verified by reading both at 2a722bb. This file requires no force-push and no branch deletion. The other file requires those two plus "changes land via pull request" and "bypass disallowed, including for administrators," and says of the last one that it "carries the others." This file's :44-48 reads "*(Open: whether protection additionally requires a PR, required reviews, or required status checks … Left undecided pending the push/merge posture reaching a canonical home.)*" and points at the very file that settled it. Separately, :36-38 here and :176-178 there are near-verbatim.
Consequence: This is the adoption checklist — the document a repo is configured from. A repo set up from it protects against force-push and deletion, permits administrator bypass, and is compliant by this file's own text while the other policy's guarantee ("history on the default branch cannot be rewritten or destroyed whoever holds the credential") is false in it. Core rule 9: two sources disagree, and the weaker one is the operative one.
Fix: This file becomes the single home for the requirement set. Bring all four items here, delete :44-48 as decided, and reduce `policies/commit-and-change-control-policy.md`:161-184 to the statement that branch protection is the structural gate its push posture rests on. That file's :184 already says "Do not duplicate its checklist here," so the direction of the move is the one it asks for.
Related: PS-4

## PS-2 — blocking
Claim: Requirements 2, 3, and 4 do not state their requirement; each states that `policies/document-metadata-policy.md` requires something and defers to it for what.
Location: policies/project-setup-requirements.md:50-64 (req 2), :65-72 (req 3), :73-81 (req 4)
Evidence: Verified by reading. Req 2: "for the in-scope document set defined in `policies/document-metadata-policy.md`." Req 3: "`policies/document-metadata-policy.md` requires this explicitly." Req 4: "Per `policies/document-metadata-policy.md`: a document absent from the list does not qualify."
Consequence: Criterion 1 and criterion 3 fail together. A repo being set up from the bundle learns that a document set is in scope but not which documents; that a grandfather disposition list has rules but not what a conforming list contains. Three of four requirements are unactionable as written.
Fix: State each requirement. Req 2: the repo runs its own frontmatter check over its spec documents at commit time, because the methodology repo's hooks cannot reach a project repo — and name the in-scope set here, or state the rule that determines it. Req 3: an expedited-review log file exists, empty if there is nothing in it, because the first expedited agreement otherwise fails on a missing review artifact. Req 4: if any document enters migration already marked `agreed`, the repo records a one-time per-document list naming exactly which ones and declares where the list lives; a document absent from the list does not qualify; no list means the grandfather clause does not apply at all; recording "none" is complete.
Related: PS-4, PS-8

## PS-3 — blocking
Claim: "The constraint on this document" is an authoring principle addressed to whoever maintains the list, not an instruction to the agent reading it.
Location: policies/project-setup-requirements.md:19-25
Evidence: Verified by reading: "**This list stays short.** … If it grows toward twenty items, that is a signal the approach is wrong — not a reason for a longer list. Something that can be enforced by a hook, derived from git, or checked by a script belongs there instead of here."
Consequence: Criterion 5 names exactly this: a rule for the person writing instructions, sitting in the file the agent loads. The agent reading the bundle cannot act on it, and it is seven lines of loaded context.
Fix: Delete the section.

## PS-4 — blocking
Claim: Nine path-shaped references to other files.
Location: policies/project-setup-requirements.md:47, :53, :58, :59, :67, :69, :79, :85, :96
Evidence: Verified by running a path-shaped-token extraction over the body (frontmatter excluded): `policies/document-metadata-policy.md` ×3, `policies/commit-and-change-control-policy.md` ×1, `bin/install-hooks` ×1, `bin/check-frontmatter` ×1, `reviews/expedited-log.md` ×1, `OPEN-ITEMS.md` ×1, `docs/cycles/doc-review-2026-08-02-directive.md` ×1. All nine targets exist; none is a dead reference.
Consequence: The bundle reader can follow none of them, and per PS-2 three of the four requirements have no content without them.
Fix: The three `document-metadata-policy` references are resolved by PS-2 stating the requirements. :47 is resolved by PS-1 deleting the parenthetical. :85 and :96 are resolved by PS-6. :58-59 (`bin/install-hooks`, `bin/check-frontmatter`) are this repo's own tooling named inside a general requirement — keep the requirement general and note the tool names as this repo's instance, or drop them. `reviews/expedited-log.md` at :67 is a filename the requirement is *about* and stays.
Related: PS-1, PS-2, PS-6

## PS-5 — blocking
Claim: Vendor names appear twice, for a concept a peer policy already states vendor-neutrally.
Location: policies/project-setup-requirements.md:15 ("in GitHub's configuration"), :40 ("Branch protection lives in GitHub's configuration")
Evidence: Verified by running a case-insensitive grep for vendor and model names over the file. No model names found. `policies/commit-and-change-control-policy.md:180` states the same fact as "Branch protection lives in the forge's configuration, not in the repository" — the neutral form already exists in the tree.
Consequence: An adoption precondition document is the one place a vendor name is most costly: it reads as "this methodology requires GitHub."
Fix: "the forge's configuration," matching the existing neutral usage.

## PS-6 — blocking
Claim: The Discharge note and Status of this draft are project bookkeeping — an OPEN-ITEMS reconciliation and a drafting changelog — not instructions.
Location: policies/project-setup-requirements.md:83-91 (Discharge note), :93-97 (Status of this draft)
Evidence: Verified by reading. The Discharge note records which OPEN-ITEMS entry this document closes and when; `grep -n 'Per-project frontmatter' OPEN-ITEMS.md` → line 297, so the entry is real. Status of this draft records the drafting date, the directive that produced it, and "Nothing here is agreed."
Consequence: Criterion 5 and criterion 6 both fail. Fifteen lines — a sixth of the file — that instruct nobody, loaded into every `all-roles` bundle. The status claim also duplicates `status: draft` in the frontmatter, which is where it belongs.
Fix: Delete both sections. The discharge fact belongs in the OPEN-ITEMS entry, which is where a reader looking for it will be.

## PS-7 — non-blocking
Claim: The file does not state which session kind it is for.
Location: policies/project-setup-requirements.md:1-17
Evidence: Verified by reading; no session-kind statement. `policies/verification-boundary-policy.md:9-10`, a peer policy through Pass 1, opens with one, and `operating-model.md:9` does the same.
Consequence: The preconditions are confirmed by a human at adoption (:41-42), which makes this decision-session material almost throughout. An execution session loading it cannot tell that none of it is an instruction to act on.
Fix: State it: these are adoption preconditions confirmed before either session kind begins work in a repo, and confirming them is the human's.

## PS-8 — non-blocking
Claim: Requirement 3 quotes another document verbatim, in quotation marks, as its justification.
Location: policies/project-setup-requirements.md:69-72
Evidence: Verified by reading: "`policies/document-metadata-policy.md` requires this explicitly: without it, the first expedited agreement fails on a missing review artifact, \"which reads as a review problem rather than the setup omission it is.\""
Consequence: A quoted fragment of a file the bundle reader cannot open, attributed to it. The quotation marks make the sentence unusable on its own — it reads as reported speech about an absent source rather than as this file's statement.
Fix: State the reason in the file's own voice, unquoted, as part of the PS-2 rewrite of requirement 3.
Related: PS-2
