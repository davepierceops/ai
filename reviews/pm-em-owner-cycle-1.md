# Review: roles/pm-em-owner.md — cycle 1

Verdict: changes-required
Reviewed: `roles/pm-em-owner.md` @ `ed926db`
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (51 lines) against `docs/global-context/review-rubric.md` @ `ed926db`, all ten criteria, criterion 10 answered first. Criterion 4 judged against the current text of `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`, all @ `ed926db`.
Cross-checked: `operating-model.md` §Responsibilities (`### Dave`), §Change flow step 9, §Release gate, §Standard response shape, §Change package, §Definition of done, §Escalation; `docs/global-context/core.md` rule 2; `LEXICON.md` §Release impact labels, §Service levels; `docs/global-context/decision-layer.md`; `policies/document-metadata-policy.md` (`audience:` values and the reserved set); `roles/chief-of-staff.md`, `roles/spec-reviewer-agent.md`, `roles/context-quality-reviewer.md`, `roles/orchestrator-agent.md` (the other four files in this cycle); `skills/spec-review-cycle.md` §Review artifact schema, for the `Sign-off` term at `:20`.
Not inspected: `policies/commit-and-change-control-policy.md` — it defines the consequential class and the `human-gate` label this file's `:45` names, and is a later cycle; whether any bundle currently compiles for the `pm-em-owner` audience — no generator run was performed; `REVIEW-v0.4.md:151`, which lists this file as "carried", since that document is outside this cycle's scope; whether the eight items in `:34-45` are the right inputs as a matter of product judgment, as against duplicated — that is Dave's call, not a gate question.
Findings: 6 — 2 blocking, 3 non-blocking, 1 observation
Dave should inspect: P2. It is the finding that decides the disposition, and it is a question about you rather than about the text: a role document is the part of a bundle that tells an agent what it is for, and no agent fills PM/EM/Owner — you do. If the answer is that this file is a human-readable statement of your own responsibilities rather than agent context, the merge below is right and `roles/` is the wrong directory for it either way.

## Criterion 10, first and explicitly

**merge-into `operating-model.md`**, §Responsibilities → `### Dave`.

`operating-model.md` already carries a `### Dave` subsection stating four of the
things this file states, and this file's version is the fuller one — nine owned
items against four, plus a Non-responsibilities list the operating model states
only as a summary sentence. The two are the same content at two levels of
detail, in two files, both in every bundle. The right resolution is not to keep
the thinner copy and delete the fuller one; it is to move the fuller text into
the file that already claims the section, and delete this one.

The mapping:

| This file | Already stated in |
| --- | --- |
| `:13-23` Dave owns — product direction, user value, prioritization, acceptance criteria, risk tolerance, release decisions, operational learning | `operating-model.md` `### Dave` ("product intent, acceptance criteria, risk tolerance, operational learning"); `core.md:15` rule 2 ("Agreement, release, prioritization, and publication are his") |
| `:20` agreeing the PRD and TRD (after Spec Reviewer sign-off) | `operating-model.md` §Change flow step 1; `core.md:15` rule 2 |
| `:22` release decisions | `operating-model.md` §Release gate; `core.md:15` rule 2 |
| `:27-32` Non-responsibilities | `operating-model.md` §Summary ("Dave does not rely on routine line-by-line code review") and `### Dave` ("code review is not the default quality gate") |
| `:34-45` Inputs Dave should receive | `operating-model.md` §Standard response shape (7 items), §Change package items 7 and 11, §Escalation — see P4 |
| `:47-51` Dave-facing question | `operating-model.md` §Core operating rule and §Definition of done ("Dave has enough information to assess risk") |

Residue that must survive the merge, because it is stated nowhere else: the four
extra owned items at `:14-15`, `:19`, `:23` (product direction, user value,
prioritization, decisions about whether evidence is sufficient); the four
Non-responsibilities as an explicit list rather than a summary sentence,
particularly `:32` "replacing missing evidence with intuition"; and the
Dave-facing question at `:50-51`.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — P2; the file is not written to an agent, and the bundle its `audience:` names has no agent to receive it |
| 2 | `audience:` is the selector | fail — P3; `pm-em-owner` names a bundle for a human the reserved `human` value already names |
| 3 | No references to other files by path | pass — verified by running; the only backtick token in the file is `human-gate` at `:45`, a label, not a path |
| 4 | Core states it → remove it here | fail — P1, P4, P5 |
| 5 | Agent instruction, not authoring principle | fail — P2; 37 of 51 lines describe a human's responsibilities rather than instructing the agent reading them |
| 6 | Instructions, not rationale | pass — the file states lists and stops; `:47-51` is framing rather than rationale, and it is the one part worth keeping (P1) |
| 7 | Session kind is explicit | fail — P6; neither kind is named |
| 8 | Tiers, not model names; route and model, not track | pass — verified by running; `grep -ncE 'dispatch\|sync block\|\bprompt\|\btrack' roles/pm-em-owner.md` returns 0, and no vendor or model name appears |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | fail — merge, see above |

## P1 — blocking
Claim: Every section restates `operating-model.md` `### Dave`, Core rule 2, or another operating-model section, and the two documents have already diverged on what Dave owns.
Location: `roles/pm-em-owner.md:11-51` (the whole body)
Evidence: Verified by running. `sed -n '/^### Dave$/,/^### Agents$/p' operating-model.md` returns: "Owns: product intent / acceptance criteria / risk tolerance / operational learning. May inspect code when needed, but code review is not the default quality gate." This file at `:13-23` states nine owned items, of which three are the same as the operating model's ("acceptance criteria", "risk tolerance", "operational learning"), one is a rewording ("product direction" against "product intent"), and five are additions. `grep -n "Dave decides" docs/global-context/core.md` returns `:15` "**Dave decides. You propose.** Agreement, release, prioritization, and publication are his" — which covers `:19`, `:20`, and `:22`. The full mapping is the table above.
Consequence: Criterion 4 and criterion 10. Both documents carry `audience:` values that put them in the same bundles — `operating-model.md` is `[all-roles, human]` — so every agent receives two lists of what Dave owns, one with four items and one with nine, and no rule for which governs. The divergence is not hypothetical: "product intent" and "product direction" are different words for what may or may not be the same thing, and an agent deciding whether a question is Dave's has to guess. Core rule 9 applies — two sources disagree, surface it — and this review is that surfacing.
Fix: Move the residue named above into `operating-model.md` `### Dave`: extend the Owns list to the nine items, replace the trailing sentence with the four-item Non-responsibilities list, and add the Dave-facing question at the end of the subsection. Then delete `roles/pm-em-owner.md`. `:34-45` moves separately — see P4.
Related: P2, P4, P5

## P2 — blocking
Claim: The file is a description of a human's responsibilities, not an instruction to the agent reading it, and the bundle its `audience:` names has no agent to receive it.
Location: `roles/pm-em-owner.md:9`, `:11-32`, `:47-51`
Evidence: Verified by reading. `:9` — "Dave fills the PM, EM, owner, and operator roles." Every rule in `:13-32` has Dave as its subject: "Dave owns…", "Dave does not default to…". The one section addressed to an agent is `:34-45`, whose lead is "Agents should give Dave:". `docs/global-context/review-rubric.md` criterion 5: "**Agent instruction, not authoring principle.** Every rule is an instruction to the agent reading it." Criterion 1: "The file is written to be read inside a generated bundle, by an agent that has never seen the repository." `operating-model.md` §Responsibilities `### Dave` states the same content and is correctly placed — that file governs the model, not a role.
Consequence: Criterion 5 and criterion 1. A role document is the part of a bundle that tells an agent what it is for, and this one tells an agent what *Dave* is for. The `pm-em-owner` audience value implies a compiled bundle for an agent filling PM/EM/Owner; no such agent exists, since `:9` says Dave fills it. So either the bundle is never generated — and the file lands in no bundle, failing criterion 10 outright — or it is generated for Dave, in which case the reserved `human` value already selects it and the role slug is redundant (P3). The section that *is* agent-facing, `:34-45`, is not a role document at all: it is a standing instruction to every agent, which is why the operating model already carries its content (P4).
Fix: Subsumed by the merge. `:11-32` and `:47-51` become `operating-model.md` `### Dave`, where a human-facing description belongs; `:34-45` merges per P4. The `roles/` directory is left holding only documents that instruct an agent.
Related: P1, P3, P4

## P3 — non-blocking
Claim: `audience: [pm-em-owner, chief-of-staff, human]` names a bundle for a human that the reserved `human` value already names.
Location: `roles/pm-em-owner.md:4`
Evidence: Verified by reading `policies/document-metadata-policy.md:91-93`: "`audience:` list of roles that consume this document. Values are `roles/` file slugs plus two reserved values: `all-roles` and `human`. Any other value fails enforcement." `pm-em-owner` is a valid value under that rule — it is a `roles/` file slug — so this passes enforcement and fails criterion 2 on a different ground: the rubric says `audience:` is *the selector*, and this one selects a bundle whose only possible reader is Dave, who is already selected by `human`.
Consequence: Criterion 2. `bin/bundle --list` emits every audience value in use, so `pm-em-owner` appears as a compilable audience alongside real agent roles, and anyone reading that list sees an agent role that is not one. The cost is small and entirely in the selector surface; the file's content problems (P1, P2) are the reason for the disposition, not this.
Fix: Subsumed by the merge — deleting the file removes the value. If Dave retains the file instead, `audience:` narrows to `[chief-of-staff, human]`, since the Chief of Staff is the one role that acts on what Dave owns and Dave is reached by `human`.
Related: P2

## P4 — non-blocking
Claim: `Inputs Dave should receive` restates `operating-model.md` §Standard response shape and two change-package items, with a different item list.
Location: `roles/pm-em-owner.md:34-45`
Evidence: Verified by reading both at `ed926db`. This file states eight items: concise decision summaries, options and tradeoffs, known risks, evidence packages, verification boundary status, SLO status and error budget consumption for affected Top K user journeys, pending `human-gate` items requiring go/no-go, clear recommendations. `operating-model.md` §Standard response shape states seven, on a different axis: Role, Intent, Evidence, Boundary, Gaps, Recommendation, Dave decision points. `operating-model.md` §Change package item 7 is "SLO status and error budget consumption for affected Top K user journeys" — word-for-word identical to `:43` — and item 11 is "`human-gate` tracker issue reference, if the change is consequential", which `:45` restates. `decision-layer.md:22` rule 6 covers "options and tradeoffs": "**Ask the judgment calls.** When a decision is his, state the options and tradeoffs and ask."
Consequence: Criterion 4. `:43` is an exact duplicate of a change-package item, so a change to the Top K wording in one place leaves the other asserting the old form — Core rule 13. The rest is a third list of what an agent owes Dave, alongside the response shape and the change package, and the three disagree: an agent satisfying this file's eight items has not stated `Boundary` or `Gaps`, which the response shape requires; one satisfying the response shape has not stated SLO status, which this file requires.
Fix: Delete `:34-45`. `:43` and `:45` are already change-package items and transfer nowhere. The remaining six items map onto the response shape's Recommendation, Dave decision points, Evidence, Boundary, and Gaps; where the mapping is imperfect, extend the response shape in `operating-model.md` rather than keeping a competing list.
Related: P1, P5

## P5 — non-blocking
Claim: `:20` restates the change-flow gate and uses the term the artifact schema replaced.
Location: `roles/pm-em-owner.md:20`
Evidence: Verified by reading. `:20` — "agreeing the PRD and TRD (after Spec Reviewer sign-off)". `operating-model.md` §Change flow step 1: "PRD/TRD written, reviewed by the Spec Reviewer Agent (hard gate), and agreed by Dave. The same gate covers any canonical document, methodology documents included." `skills/spec-review-cycle.md` §Header: "`Verdict` is deliberately **not** the word `agreed`… `ready` means ready for Dave's agreement," and its §What this schema governs table maps "Sign-off; Recommendation (the overall ship call)" onto `Verdict`, meaning `Sign-off` is the superseded term.
Consequence: Criterion 4, and a narrowing. The operating model's step 1 says the gate covers *any* canonical document; this line says PRD and TRD, which is the reach `roles/spec-reviewer-agent.md:41` explicitly corrects ("The gate's reach is **any canonical document, not `specs/` only**"). So the shorter copy states the narrower, wrong reach. `Sign-off` is the milder half — one word out of step with the schema.
Fix: Delete `:20`. Core rule 2 and the change flow both already state that agreement is Dave's, over any canonical document, and neither needs this line.
Related: P1

## P6 — observation
Claim: The file names no session kind.
Location: `roles/pm-em-owner.md` — whole file
Evidence: Verified by running. `grep -niE 'decision session|execution session|in chat' roles/pm-em-owner.md` returns nothing. `core.md` §Vocabulary defines both kinds and makes the distinction load-bearing for what a session may write.
Consequence: Criterion 7, but with a caveat that makes it an observation rather than a finding: the criterion asks whether the file "is for decision sessions, execution sessions, or both, and says nothing only the other kind needs." This file is for neither, because it is not for a session (P2) — so the criterion technically fails while the underlying defect is the one P2 states, not this. Recorded so the criterion table's `fail` is not read as a second, separable problem.
Fix: None separable from the merge. `operating-model.md:10` already states its own answer for both kinds and covers the merged content.
Related: P2
