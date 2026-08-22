# Review: roles/spec-reviewer-agent.md — cycle 3

Verdict: changes-required
Reviewed: `roles/spec-reviewer-agent.md` @ `ed926db`
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (142 lines) against `docs/global-context/review-rubric.md` @ `ed926db`, all ten criteria, criterion 10 answered first. Criterion 4 judged against the current text of `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`, all @ `ed926db`. The output-shape sections are judged against the settled rule in `reviews/agent-review-policy-cycle-1.md` finding A2.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `operating-model.md` (all @ `ed926db`); `skills/spec-review-cycle.md` §Review artifact schema and §What this schema governs; `reviews/agent-review-policy-cycle-1.md` finding A2; `policies/document-metadata-policy.md` (expedited path, doc-only cycle, `audience:` values); `roles/context-quality-reviewer.md`, `roles/chief-of-staff.md`, `roles/pm-em-owner.md`, `roles/orchestrator-agent.md` (the other four files in this cycle); `docs/batons/baton-20260822T153848.md` ("What this session settled").
Not inspected: `roles/architect-agent.md`, `roles/reviewer-agent.md`, and `roles/skeptic-risk-agent.md` against their own rubric criteria — they are cycle 19b, and are read here only as evidence of where a responsibility already lives; whether the Depth 1/2/3 scan depths are the right depths, as against internally consistent — no continuity scan has been run at Depth 2 or 3 and there is no record to check them against; `context-sets/spec-and-change-discipline.md` and `skills/spec-review-cycle.md` against their own criteria — later cycles; whether any bundle currently compiles for the `spec-reviewer-agent` audience and what else lands in it.
Findings: 9 — 3 blocking, 5 non-blocking, 1 observation
Prior cycle: `reviews/spec-reviewer-agent-cycle-2.md`
Dave should inspect: S4. Deleting the expedited-path and doc-only-cycle summary at `:41-53` is the right call under criterion 4, but it is the one deletion in this list that removes information the reviewer actually needs at the moment of deciding whether a document is in its gate's reach. The fix below routes that need through `audience:` on the metadata policy rather than through a copy here, and that routing is a bundle-composition decision, not a wording one.

## Criterion 10, first and explicitly

**retain-with-changes.**

This file is the only place that states the Spec Reviewer's two activation
modes, the hard-gate rule with its drafter/reviewer separation, the gate-review
inspection list (`:62-73`), and the three continuity-scan depths. `operating-
model.md` names the role at three points in the change flow and never says what
it inspects. It lands in the `spec-reviewer-agent` bundle and contributes what
no other file in that bundle states, so it is fixed rather than removed.

The two things it should stop carrying are both output shapes — `:75-84` and
`:116-123` — and A2 settled that question: the review artifact schema in
`skills/spec-review-cycle.md` owns the shape of a review's output; a role
document states what the role inspects and decides, not what fields its report
carries. This file states two report shapes, and neither matches the schema.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — S7; sixteen path-shaped references, and `:42-43` reasons from "the review record" in `reviews/`, a directory no bundle contains |
| 2 | `audience:` is the selector | pass — `[spec-reviewer-agent, chief-of-staff, human]`; the role's own slug, the role that assigns it, and the reserved value |
| 3 | No references to other files by path | fail — S7; sixteen |
| 4 | Core states it → remove it here | fail — S3, S4, S5, S6 |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | fail — S8; `:36-39`, `:42-43`, and the script-supervisor analogy at `:90-95` |
| 7 | Session kind is explicit | fail — S8; neither kind is named anywhere in the file |
| 8 | Tiers, not model names; route and model, not track | pass — verified by running; `grep -onE 'dispatch\|sync block\|\bprompts?\b\|\btracks?\b\|Claude\|Opus' roles/spec-reviewer-agent.md` returns nothing |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | pass — retain-with-changes, see above |

## S1 — blocking
Claim: `Required outputs (gate review)` states the review report's field list, which the artifact schema owns, and the five fields it states disagree with the schema's.
Location: `roles/spec-reviewer-agent.md:75-84`
Evidence: Verified by reading both at `ed926db`. This file states five fields: **Scope**, **Findings** (with location, description, severity blocking/advisory), **Required changes**, **Advisory items**, **Sign-off**. `skills/spec-review-cycle.md` §Header states ten: `Verdict`, `Reviewed`, `Reviewer`, `Date`, `Scope`, `Cross-checked`, `Not inspected`, `Findings`, `Prior cycle`, `Dave should inspect`. The schema's own §What this schema governs table already maps this file's vocabulary onto its own — "Sign-off; Recommendation (the overall ship call)" → `Verdict`; "Required changes" → entries marked `blocking`; "Advisory items" → entries marked `non-blocking` — which is direct evidence that the two lists were already known to collide. `reviews/agent-review-policy-cycle-1.md` A2 settled it: "the review artifact schema in `skills/spec-review-cycle.md` owns the *shape* of a review's output … role documents state only what their role must inspect, not what fields the report carries."
Consequence: Criterion 4 and the A2 rule. The lists are not merely different lengths; they conflict on a load-bearing word. `Sign-off` here is "explicit statement that the document is ready for Dave's agreement," and the schema deliberately refuses that framing: "`Verdict` is deliberately **not** the word `agreed`… `ready` means ready for Dave's agreement." More concretely, this file's list omits `Not inspected`, and the schema calls that field "required precisely because omitting it is how an unbounded claim gets made by accident." A reviewer following this document produces an artifact with no `Not inspected` line, satisfying its role document and violating the schema — which is exactly the failure this review's own header is shaped to avoid.
Fix: Delete `:75-84` including the heading. If anything is carried across, it is one sentence into the schema, not into this file. The gate-review inspection list at `:62-73` stays — that is what the role inspects, which is this document's job.
Related: S2

## S2 — blocking
Claim: `Continuity scan output` states a second, different report shape for the same role.
Location: `roles/spec-reviewer-agent.md:116-123`
Evidence: Verified by reading. `:119-121` states three per-finding fields — **Location**, **Contradiction**, **Severity** (blocking/advisory). The schema's §Findings states five — `Claim`, `Location`, `Evidence`, `Consequence`, `Fix` — of which four are required and `Evidence` "distinguishing *verified by running* from *inferred by reading* is not optional." `:123` adds "No fixes proposed," which contradicts this same file at `:92-95`: "if a fix is obvious, the Spec Reviewer may propose one alongside the flag — clearly labeled as a proposal."
Consequence: Criterion 4 and the A2 rule, plus an internal contradiction the file makes against itself twenty-eight lines apart. A continuity-scan finding written to `:119-121` carries no `Evidence` field, so it cannot distinguish a contradiction the reviewer confirmed by running from one it inferred by reading — which is the distinction the schema exists to force and Core rule 6 requires. And `:123`'s flat "No fixes proposed" tells the agent the opposite of `:92-95`, with no rule for which wins. The role ends up with two report formats, neither of which is the schema's, and they disagree with each other about whether a fix may be proposed.
Fix: Delete `:116-123` including the heading. Keep the severity vocabulary only if it is carried into the schema; the schema already has `blocking | non-blocking | observation` and does not need a fourth pair of words. The substantive rule at `:87-95` — that a scan flags rather than rewrites, and that a proposal is optional and labeled — stays, because that is what the role decides, not what its report looks like.
Related: S1

## S3 — blocking
Claim: The hard-gate paragraph restates the two mandatory separations from `operating-model.md`.
Location: `roles/spec-reviewer-agent.md:28-30`
Evidence: Verified by running. `grep -n "does not approve it\|does not act as the Spec Reviewer" operating-model.md` returns `:90` "- Whoever produces an artifact does not approve it." and `:91-92` "- The Architect that drafts a spec does not act as the Spec Reviewer that certifies it." This file at `:30`: "The Spec Reviewer may not be the same agent instance that drafted the document under review." At `:127`: "**Architect Agent**: drafts TRD; Spec Reviewer gates it. Not the same instance." — a third statement of the same rule, inside this file.
Consequence: Criterion 4. `operating-model.md` carries `audience: [all-roles, human]`, so it is in every bundle this file is in; the rule is stated three times in one bundle, twice within one file. The copies have already diverged on scope: `operating-model.md` binds the *Architect* who drafts a spec, this file at `:30` binds any *agent instance* that drafted *the document under review*, which is broader and is the version that actually matters for methodology documents. The broader rule is the right one and is not the one in the foundation document.
Fix: Delete `:30` and `:127`. Then widen `operating-model.md:91-92` to the general form this file was carrying — "Whoever drafts a document does not act as the Spec Reviewer that gates it" — as a dependent edit named here, since `operating-model.md` is not in this cycle's scope.
Related: S5

## S4 — non-blocking
Claim: Thirteen lines summarize the expedited path and the doc-only cycle from `policies/document-metadata-policy.md`, restating five stated conditions each.
Location: `roles/spec-reviewer-agent.md:41-53`
Evidence: Verified by reading both at `ed926db`. This file: "The **expedited path** substitutes Dave's own read of a diff for this gate, bounded to a single-commit, single-in-scope-file revision of no more than ten body lines, over a document that states no gate and is not under `specs/`." Followed by an equally detailed doc-only-cycle summary and "Both carry five stated conditions." `policies/document-metadata-policy.md` states both paths with their conditions; this file says so itself at `:43-44` ("There are two bounded exceptions, both in `policies/document-metadata-policy.md`").
Consequence: Criterion 4, and Core rule 13 is the live risk. Two documents now state the same numeric bound — "no more than ten body lines" — and a change to that bound in the policy leaves this copy asserting the old number to the one role whose job is catching exactly that class of drift. The metadata policy carries `audience: [all-roles, human]`, so both texts land in this role's bundle together; the summary buys nothing the bundle does not already have.
Fix: Replace `:41-53` with two sentences: "The gate's reach is any canonical document, not `specs/` only. Two bounded exceptions substitute a different check for this gate; the document-metadata policy states them and their conditions, and this role does not restate them." That keeps the reach rule — which is this file's — and drops the copy. This depends on the metadata policy remaining in the `spec-reviewer-agent` bundle; it does, at `audience: [all-roles, human]`.
Related: S7

## S5 — non-blocking
Claim: The file states four other roles' scope twice, and the second statement restates Core rule 2.
Location: `roles/spec-reviewer-agent.md:12-15`, `:125-133`
Evidence: Verified by reading. `:12-15` — "This role is distinct from the Reviewer Agent (which reviews implementation) and the Skeptic/Risk Agent (which evaluates change package risk)." `:125-133` restates the same two distinctions at greater length plus the Architect (S3) and Dave. `:132-133` — "**Dave**: receives gate review sign-off and continuity scan findings; makes all agreement and resolution decisions" — against `core.md:15` rule 2: "**Dave decides. You propose.** Agreement, release, prioritization, and publication are his."
Consequence: Criterion 4 and criterion 6. The Reviewer/Skeptic distinction is stated twice inside one file, 110 lines apart, in different words — "evaluates change package risk" at `:13` and "evaluates change package risk. Spec Reviewer evaluates spec completeness and consistency. Complementary, not overlapping" at `:130-131`. Neither copy is an instruction to the agent reading it; both describe what other agents do, which the other roles' own documents state and which no bundle compiled for this role needs in order to act.
Fix: Delete `:125-133` entirely. Keep `:12-15`, which is the one-sentence orientation a reader needs, and drop `:127` from it per S3.
Related: S3, S6

## S6 — non-blocking
Claim: The Non-goals list restates rules the body already states and Core rule 2.
Location: `roles/spec-reviewer-agent.md:135-142`
Evidence: Verified by reading. Item 1 ("propose fixes during a continuity scan without flagging first; proposals are optional and advisory, Dave decides") restates `:92-95`. Item 2 ("review implementation, tests, or change packages") restates `:12-15` and S5's `:125-133`. Item 3 ("make agreement decisions (Dave decides)") restates `core.md:15` rule 2 and `:132-133`. Item 4 ("author or co-author specs") is the only item not stated elsewhere in this file, and it is the negative half of S3's separation rule.
Consequence: Criterion 4 and criterion 6 — the section is four "never X" restatements of rules stated above it, which criterion 6 names as the thing to cut. Item 1 is worse than redundant: it is the contradiction from S2 restated a third time, since `:123` says no fixes are proposed and this says they may be, optionally.
Fix: Delete `:135-142`. Fold item 4's content into `:9-10` as a clause — "and does not author or co-author the documents it gates" — which is where the role's boundary belongs.
Related: S2, S3, S5

## S7 — non-blocking
Claim: Sixteen path-shaped references, and one argument that reasons from a directory no bundle contains.
Location: `roles/spec-reviewer-agent.md:24`, `:25` (×4), `:35` (×2), `:41`, `:42`, `:43`, `:44`, `:47`, `:50`, `:105`, `:106`
Evidence: Verified by running; a count of backtick-delimited path tokens returns 16. Every one resolves at `ed926db`. `:42-43` reads "This matches `skills/spec-review-cycle.md` and the review record: every gate review in `reviews/` is over a non-`specs/` document."
Consequence: Criterion 3, and criterion 1 for `:42-43` specifically. That sentence's warrant is a census of a directory the agent cannot open — a bundle contains no `reviews/` — so the reader is asked to accept a claim about evidence that is not in front of it. The directory-name references at `:24-25` and `:105-106` are a milder case: they name where canonical documents live, which in a bundle-compiled world is an audience question, not a path question.
Fix: `:42-43` — delete the warrant and keep the rule: "The gate's reach is any canonical document, not `specs/` only." (S4 already rewrites this passage.) `:24-25` — replace the directory list with "any canonical document, PRD and TRD and the methodology documents equally." `:105-106` — replace with "Depth 1 plus boundary and policy documents." Delete the citations at `:35`.
Related: S4

## S8 — non-blocking
Claim: The file names neither session kind, and three passages argue rather than instruct.
Location: `roles/spec-reviewer-agent.md` — whole file for session kind; `:36-39`, `:42-43`, `:90-95`
Evidence: Verified by running. `grep -niE 'decision session|execution session|in chat' roles/spec-reviewer-agent.md` returns nothing. `core.md` defines both kinds and makes the distinction load-bearing: a decision session "does not carry out the changes a directive specifies." `:36-39` — "Nothing is exempted by this: every revision still passes the gate, and it is the same gate — what changes is that a delta's revisions are reviewed together, as the diff that is actually being proposed for agreement, rather than one at a time on their way to it" — argues for the rule stated at `:32-35`. `:90-95` is an analogy: "The analogy is a film script supervisor: the job is to catch when the coffee cup is full in one shot and empty in the next — not to rewrite the scene."
Consequence: Criterion 7 and criterion 6. The session-kind gap has a concrete edge: `skills/spec-review-cycle.md` puts triage in a decision session and the reviewer's own work in an execution session, and this file's `:73` instruction — "flag any item that requires Dave's judgment before the document can be agreed" — reads differently depending on which the agent is in. An agent that reads this as a decision-session role may address Dave directly; one that reads it as an execution-session role writes the flag into an artifact. The file does not say, and both are defensible from the text.
Fix: Add one sentence under the title: "The Spec Reviewer runs as an execution session and returns a review artifact; the triage of its findings happens in a decision session." Delete `:36-39` and `:42-43` (S4 and S7 already touch the latter). Reduce `:90-95` to its rule: "If a fix is obvious, the Spec Reviewer may propose one alongside the flag, clearly labeled as a proposal. Dave decides whether to accept, modify, or reject it." Drop the analogy.
Related: S4, S7

## S9 — observation
Claim: Depth 3 of the continuity scan claims the whole-methodology contradiction check that `roles/context-quality-reviewer.md` dimensions 1 and 3 also claim, with no rule for which role holds it.
Location: `roles/spec-reviewer-agent.md:110-114`
Evidence: Verified by reading both at `ed926db`. This file `:110-114`: "**Depth 3 — Full sweep** (on demand, milestone moments): Scope: Everything — spine, boundaries, policies, role docs, skills, context sets. Checks: Does anything in the whole methodology contradict anything else?" `roles/context-quality-reviewer.md:27-34` dimension 1, Story coherence: "Is there a consistent, logical narrative across the repository? … Flag: any place where the story breaks, requires inference to hold together, or would produce different behavior depending on which documents were loaded." And `:47-52` dimension 3, Unhelpful duplication: "Is the same information repeated in multiple documents in ways that create maintenance risk or divergence?" `roles/context-quality-reviewer.md:97-99` acknowledges the neighbouring role but draws the line at spec completeness, not at cross-document contradiction: "**Spec Reviewer Agent**: evaluates spec documents for completeness and traceability. This role evaluates all context documents for coherence and agent-safety."
Consequence: Two roles are assigned the same responsibility — find contradictions across the whole methodology corpus — and the boundary each draws is drawn against a description of the other that does not match the other's text. Dave asking for a corpus-wide contradiction sweep has two roles to invoke and no basis for choosing. This is an observation against this file rather than a finding because the resolution is not here: `reviews/context-quality-reviewer-cycle-1.md` recommends merging that role away, which removes the overlap without editing this file at all.
Fix: None against this file, if the context-quality-reviewer merge lands. If Dave retains that role instead, `:110-114` needs a clause ceding the corpus-wide sweep to it, or that role's dimensions 1 and 3 need to cede to Depth 3 — one or the other, not both.
