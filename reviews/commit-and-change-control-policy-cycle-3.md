# Review: policies/commit-and-change-control-policy.md — cycle 3

Verdict: changes-required
Reviewed: policies/commit-and-change-control-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent (execution session, frontier tier)
Date: 2026-08-22
Scope: the whole file, 226 lines, against all ten rubric criteria at docs/global-context/review-rubric.md @ 2a722bb.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/verification-boundary-policy.md, policies/project-setup-requirements.md, policies/release-readiness-policy.md, roles/release-manager-agent.md, context-sets/spec-and-change-discipline.md — all @ 2a722bb.
Not inspected: bin/ implementations; the four policies not in this cycle's scope (agent-review, decision-log, document-metadata, testing); roles/ other than release-manager-agent.md; skills/ other than spec-review-cycle.md; specs/, engagements/, writing/, vendors/; prior review artifacts other than the cycle-2 pointer below.
Findings: 13 — 9 blocking, 3 non-blocking, 1 observation
Prior cycle: reviews/commit-and-change-control-policy-cycle-2.md
Dave should inspect: CC-1 (two consequential-class lists disagree and one calls itself exhaustive — which one is canonical is a decision, not an edit) and CC-2 (branch protection stated twice with different content; the single home is a decision).

## Criterion 10 first — disposition

**Retain-with-changes.**

The file lands in the `all-roles` bundle and, after the cuts below, contributes
one thing no other file in that bundle states: the mechanics by which a change
reaches the default branch — push and force-push posture, the two-layer deny,
branch protection as the structural gate, agents opening and merging pull
requests, and the spec-branch/reconciliation-PR path. That is commit control,
and this is its only home.

What does not survive is the second half of the title. The two-tier release
gate, the consequential class, the deploy/release distinction, the flag
mechanics, the red-gate, and Test/Coder separation are all stated in
`operating-model.md` (through Pass 1) or in
`context-sets/spec-and-change-discipline.md`, and this file restates them at
length. Criterion 4 removes them. That is roughly half the file.

The exception is the consequential-class **list** itself, which is longer and
more specific here than in operating-model and calls itself exhaustive. One of
the two must go; see CC-1.

The finding list below is the edit list.

## Criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — CC-6, CC-7, CC-8 |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`; no `order:`, and position does not carry meaning here |
| 3 | No references to other files by path | fail — CC-8, 9 path references plus one by name |
| 4 | Core states it → remove it here | fail — CC-3, CC-4, CC-5, CC-12 |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | fail — CC-11 |
| 7 | Session kind is explicit | fail — CC-10 |
| 8 | Tiers, not model names; route and model, not track | fail — CC-9 (vendor names); no model names, no retired "track" |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |
| 10 | The file earns its place or is retired | retain-with-changes, as above |

## CC-1 — blocking
Claim: The consequential class is stated twice, in this file and in `operating-model.md`, and the two lists differ; this one declares itself exhaustive, which makes the divergence a contradiction rather than a summary.
Location: policies/commit-and-change-control-policy.md:50-78 (11 bullets, "The following list is exhaustive"); operating-model.md:"Release gate" (7 items, inline prose)
Evidence: Verified by reading both files at 2a722bb. This file lists: auth/authz; schema or data migration; security or privacy controls; irreversible or hard-to-reverse operation; first exposure of a new surface; breaking change to a public interface; pricing/billing/entitlements; user data visibility or sharing; a verification boundary; core architecture; any code path for a Top K journey at or below 20% error budget. operating-model lists: auth, schema/migrations, security or privacy, irreversible operations, public-facing surfaces, a verification boundary, core architecture. Four items — breaking public-interface change, pricing/billing/entitlements, user data visibility, and the 20%-error-budget trigger — appear only here.
Consequence: An agent that receives operating-model but reads the shorter list will classify a pricing change or an error-budget-depleted code path as routine and release it without a human go/no-go. That is exactly the Tier 2 failure this policy exists to prevent. Core rule 9 requires surfacing the disagreement rather than resolving it by picking one.
Fix: One list, one home. Recommend the exhaustive list stays here and operating-model names the tier without enumerating it. Requires an edit to operating-model, which is through Pass 1 — so this is Dave's call, not an executor's.
Related: CC-3

## CC-2 — blocking
Claim: The branch-protection requirement set is stated twice — here and in `policies/project-setup-requirements.md` — with different content, in a section that instructs the reader not to duplicate it.
Location: policies/commit-and-change-control-policy.md:161-184 and :176-178; policies/project-setup-requirements.md:29-48 and :36-38
Evidence: Verified by reading both at 2a722bb. This file requires four things: no force-push, no branch deletion, changes land via pull request, bypass disallowed including for administrators. project-setup-requirements requires two — no force-push, no branch deletion — and its parenthetical at :44-48 leaves "whether protection additionally requires a PR, required reviews, or required status checks" explicitly undecided, pointing at this file. This file has decided it. Separately, :176-178 and project-setup-requirements:36-38 are near-verbatim ("This is what makes 'agents may push and merge' safe to state / safe to say: history on the default branch cannot be rewritten or destroyed, whoever holds the credential"). Line :184 says "Do not duplicate its checklist here" while :163-168 does.
Consequence: A repo adopting the methodology from the setup document configures two of the four protections and believes it is compliant. Bypass-disallowed is the one this file says "carries the others," and it is the one the setup checklist omits.
Fix: Move the full four-item set into `policies/project-setup-requirements.md` as requirement 1, delete :163-168 and :176-178 here, and keep only the sentence that branch protection is the structural gate this policy's push posture rests on. Delete project-setup-requirements:44-48 as decided.
Related: CC-8

## CC-3 — blocking
Claim: The two-tier release gate, the deploy/release distinction, the feature-flag exposure rule, and both tier descriptions restate `operating-model.md`'s "Release gate" section.
Location: policies/commit-and-change-control-policy.md:15-38 (Purpose, second half), :40-48 (Tier 1), :50-56 and :76-81 (Tier 2 framing)
Evidence: Verified by reading operating-model.md "Release gate" at 2a722bb, which states the two-tier structure, that routine changes flow on evidence without an explicit go/no-go, that consequential changes require the human's explicit go/no-go at the release decision, that deploy and release may be separate events with the mapping recorded in the project's TRD, and that the gate attaches to the exposure event with a dark flag being routine.
Consequence: Two statements of one rule in the same bundle. When one is edited the other drifts, and criterion 4 exists because the drift is invisible to the reader who has only the bundle.
Fix: Delete :15-38, :40-48, and :76-81. Keep :50-74 (the enumerated class, per CC-1) and :80-81 (the architecture-summary corollary), reframed as the class definition rather than as a tier description.
Related: CC-1

## CC-4 — blocking
Claim: The Red-gate section restates a rule stated in `operating-model.md` and elaborated in `context-sets/spec-and-change-discipline.md`, and cites the latter rather than deferring to it.
Location: policies/commit-and-change-control-policy.md:83-89
Evidence: Verified by reading operating-model.md change flow step 4 ("Test plan, confirmed red — ACs translated into test code, run, and confirmed to fail before any implementation") and its closing "The red-gate at step 4 is mandatory," and context-sets/spec-and-change-discipline.md:24-35, which states the behavioral-red requirement this section's weaker version omits.
Consequence: The reader gets the weakest of three statements of the rule — this one does not say the red must be behavioral rather than a missing-module error, which is the part that actually catches the failure.
Fix: Delete the section.

## CC-5 — blocking
Claim: The Test/Coder separation section restates operating-model and spec-and-change-discipline, and its "See" clause points at a deleted file.
Location: policies/commit-and-change-control-policy.md:91-96
Evidence: Verified by reading operating-model.md change flow step 5 ("Coder — a different agent from the Test Designer for this unit") and "Whoever produces an artifact does not approve it"; and context-sets/spec-and-change-discipline.md:30-35, which states why the separation matters. `test -e context-sets/ai-native-engineering.md` returns false; `git log --diff-filter=D` shows it deleted in 40b5ffe.
Consequence: A restated rule plus a dead pointer. The reader who follows the pointer for the reasoning finds nothing.
Fix: Delete the section.
Related: CC-6

## CC-6 — blocking
Claim: Reference to a deleted file, `context-sets/ai-native-engineering.md`.
Location: policies/commit-and-change-control-policy.md:95
Evidence: Verified by running `git log --oneline --diff-filter=D -1 -- context-sets/ai-native-engineering.md` → deleted in 40b5ffe ("Pass 1 cycle 12 revision: context-sets and boundaries"). Confirms the line the baton at docs/batons/baton-20260822T153848.md names.
Consequence: A pointer to nothing. In a bundle the reader cannot even discover it is dead.
Fix: Removed by CC-5's deletion of the section. No separate edit needed.
Related: CC-5

## CC-7 — blocking
Claim: Reference to a retired file, by name rather than path: "See README principle #5."
Location: policies/commit-and-change-control-policy.md:19-20
Evidence: Verified by running `git log --oneline --diff-filter=D -1 -- README.md` → deleted in e922926 ("Pass 1 cycle 6 revision: vocabulary to Core, README retired"). The baton records README as retired, to be rewritten human-only in Pass 2. Not on the baton's stale-reference list — this is an additional one.
Consequence: A pointer to a numbered principle in a file that no longer exists and, when rewritten in Pass 2, will be human-only and will not carry numbered principles. The reader has no way to recover the claim.
Fix: Removed by CC-3's deletion of :15-38. If any of that paragraph is kept, state the control-surface claim outright or drop it — `boundaries/human-review-boundary.md` is its home and it is through Pass 1.

## CC-8 — blocking
Claim: Nine path-shaped references to other files, plus one reference by filename.
Location: policies/commit-and-change-control-policy.md:20, :89, :95, :182, :191, :200, :205, :209, :217 (paths); :19 (README, by name)
Evidence: Verified by running a path-shaped-token extraction over the body (frontmatter excluded), then de-duplicating: `boundaries/human-review-boundary.md` ×2, `context-sets/spec-and-change-discipline.md` ×2, `context-sets/ai-native-engineering.md` ×1, `policies/project-setup-requirements.md` ×1, `roles/spec-reviewer-agent.md` ×1, `skills/spec-review-cycle.md` ×1, `policies/document-metadata-policy.md` ×1.
Consequence: Criterion 1 and criterion 3 both fail on the same lines: the file is written for a reader who can open the repository, and the bundle reader cannot. Two of the nine are already dead (CC-6) and the reader cannot tell which.
Fix: Six of the nine disappear with the CC-3/CC-4/CC-5 deletions. For the remaining three — :182 (setup checklist), :209 (the reconciliation gate), :217 (the status-transition commit) — state what is needed rather than pointing: that branch protection is an adoption precondition confirmed by a human; that the reconciliation pull request carries the reviewer gate over the whole accumulated diff; that the `agreed` transition is a frontmatter-only commit made after the reconciliation cycle closes. :191 (`roles/spec-reviewer-agent.md`) becomes "the reviewer gate that precedes Dave's agreement."

## CC-9 — blocking
Claim: Vendor names appear three times.
Location: policies/commit-and-change-control-policy.md:102 ("`human-gate` GitHub issue"), :122 ("GitHub unreachable"), :127 ("MCP GitHub was unavailable")
Evidence: Verified by running a case-insensitive grep for vendor and model names over the file. No model names and no use of the retired term "track" were found. "skip prompting" at :152 is the approval-prompt sense LEXICON exempts from the "prompt" retirement.
Consequence: The methodology is vendor-neutral by design — `vendors/README.md` states the swap test, and this file's own :180 already uses "the forge's configuration" for the same idea. Naming GitHub in the canonical text binds the policy to one host.
Fix: "`human-gate` tracker issue" (the term operating-model already uses), "the tracker unreachable," and delete the :125-127 anecdote entirely per CC-11.

## CC-10 — non-blocking
Claim: The file does not state which session kind it is for.
Location: policies/commit-and-change-control-policy.md:1-13
Evidence: Verified by reading the file; no session-kind statement. `policies/verification-boundary-policy.md:9-10` — a peer policy, through Pass 1 — opens with "This policy governs both session kinds: decision sessions and execution sessions," and `operating-model.md:9` does the same.
Consequence: An execution session cannot tell whether the pending-gate-visibility rules ("In chat, state one line") are addressed to it. They are not — that is a decision-session obligation — and nothing in the file says so.
Fix: Open with the session-kind line. The commit mechanics govern both kinds; the pending-gate visibility section governs decision sessions and should say so in its first line.

## CC-11 — non-blocking
Claim: Rationale and argument appear where the rule alone is what the agent needs.
Location: policies/commit-and-change-control-policy.md:34-38, :107-108, :112-115, :125-127, :143-145, :147-148, :158-159, :169-174, :197-200, :219-220
Evidence: Verified by reading. Examples: ":125-127 This is not hypothetical: the directive that introduced this rule was itself delivered as a file because MCP GitHub was unavailable that session" — session history, not an instruction. ":169-174 Protection that administrators may bypass binds only the credentials that were never the risk … the protection reads as a control while enforcing nothing against the actor most able to break it" — an argument for a rule already stated as a bullet. ":143-145 An approval here would be ceremony on an event this policy does not gate, and ceremony on a frequent event is how a gate stops being read" — likewise.
Consequence: The file is 226 lines carrying perhaps 60 lines of rule. In a bundle every line is loaded context, and the rule is harder to find inside the argument for it.
Fix: Cut each cited span. Keep the bullets and the one-line statements they justify.

## CC-12 — non-blocking
Claim: The "When in doubt" section restates a sentence stated 170 lines earlier in the same file, and also stated in operating-model.
Location: policies/commit-and-change-control-policy.md:222-226, restating :54 ("When unsure, treat as consequential and ask")
Evidence: Verified by reading. operating-model.md "Release gate" states the same: "When unsure which tier applies, treat the change as consequential and ask."
Consequence: A third copy of one sentence, and criterion 6 names trailing restatements as the thing to cut.
Fix: Delete :222-226. :54 keeps the rule.

## CC-13 — observation
Claim: The `human-gate` issue requirement is stated in three files.
Location: policies/commit-and-change-control-policy.md:98-137; policies/release-readiness-policy.md:32-34; roles/release-manager-agent.md:20 and :38-40
Evidence: Verified by reading all three at 2a722bb. operating-model.md's change package item 11 makes a fourth partial statement ("`human-gate` tracker issue reference, if the change is consequential").
Consequence: Four statements of one requirement, using two different names for the artifact (GitHub issue / tracker issue).
Fix: This file is the single home — it states the mechanics, the derivation from the change package, the degraded-tooling case, and the cross-repo label. The other three should reference the requirement by name without restating it. Recorded here; the edits to the other files belong to their own cycles.
