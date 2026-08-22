# Review: roles/chief-of-staff.md — cycle 5

Verdict: changes-required
Reviewed: `roles/chief-of-staff.md` @ `ed926db`
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (156 lines) against `docs/global-context/review-rubric.md` @ `ed926db`, all ten criteria, criterion 10 answered first. Criterion 4 judged against the current text of `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`, all @ `ed926db`.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `operating-model.md` (all @ `ed926db`); `roles/orchestrator-agent.md`, `roles/spec-reviewer-agent.md`, `roles/context-quality-reviewer.md`, `roles/pm-em-owner.md` (the other four files in this cycle); `skills/spec-review-cycle.md` (review artifact schema); `policies/document-metadata-policy.md` (frontmatter fields, revision lifecycle); `docs/batons/baton-20260822T153848.md` ("What this session settled"); `reviews/agent-review-policy-cycle-1.md` finding A2; the working tree for the existence of every path this file cites.
Not inspected: `skills/directive-dispatch.md` against its own rubric criteria — it is a later cycle, and is read here only to establish that this file cites it and what that citation carries; whether any bundle currently compiles for the `chief-of-staff` audience and what else lands in it; the six roles in cycle 19b; `MANIFEST.md`, `OPEN-ITEMS.md`, and `BACKLOG-v2.md` as documents — checked only for the existence of the entries this file names; whether the decomposition procedure at `:84-117` is operationally correct, as against internally consistent and non-duplicative — no tranche has been decomposed under it.
Findings: 11 — 4 blocking, 6 non-blocking, 1 observation
Prior cycle: `reviews/chief-of-staff-cycle-4.md`
Dave should inspect: C1 and C11 together. C1 says the mid-delta rule at `:134` names a mechanism Core abolished, so the rule has no working half — the fix has to say what replaces the sync block, and that is a judgment about how a mid-delta directive pins a spec branch, not a word swap. C11 is the cost of touching this file at all: it is the only one of the five at `status: agreed`, so any edit from this list flips it to `in-review` and puts it back through the gate.

## Criterion 10, first and explicitly

**retain-with-changes.**

This file is the only place that states the Chief of Staff's activation
behavior (`:15-19`), the read-sequence (`:21-34`), and the tranche →
decomposition-doc procedure (`:84-117`). `operating-model.md` names the role in
three sentences and stops; nothing else in the tree carries the procedure. It
lands in the `chief-of-staff` bundle and contributes what no other file in that
bundle states, which is the criterion-10 test, so it is fixed rather than
removed.

What it should stop carrying is large. Six sections restate a rule already held
by Core, the Decision Layer, or LEXICON, and one of them — the mid-delta sync
block at `:134` — restates a mechanism that no longer exists. The findings below
are the edit list.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — C10 (sixteen path-shaped references, three to things absent from the tree) and C4 (the `(Q3a)` heading tag names a decision-artifact question ID no bundle reader can resolve) |
| 2 | `audience:` is the selector | pass — `[chief-of-staff, human]`; the role's own slug plus the reserved value |
| 3 | No references to other files by path | fail — C10; sixteen |
| 4 | Core states it → remove it here | fail — C1, C4, C5, C6, C7, C8, C9; the dominant defect |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | fail — C5 (`:52`), C6 (`:81-82`), and the staleness paragraph `:110-117`, which argues a position and then declines to take one |
| 7 | Session kind is explicit | fail — C11; the file never uses Core's vocabulary, saying only "in chat" at `:90` |
| 8 | Tiers, not model names; route and model, not track | fail — C2 (six prose uses of the retired *dispatch*, one of the retired *sync block*), C3 (four vendor tokens) |
| 9 | Filenames `<descriptor>-<timestamp>` | pass — `:100` prescribes `docs/packages/<tranche>-decomposition.md`, which is a stated convention naming the file; Core rule 14 permits exactly that |
| 10 | Earns its place | pass — retain-with-changes, see above |

## C1 — blocking
Claim: The mid-delta directive rule at `:134` requires a sync block, a mechanism Core abolished, so the rule cannot be followed as written.
Location: `roles/chief-of-staff.md:132-134`
Evidence: Verified by running. `grep -n "sync block" roles/chief-of-staff.md` returns `:134` — "and its sync block names that ref". `grep -n "Sync block" LEXICON.md` returns the tombstone: "**Sync block** — retired 2026-08-21. Nothing precedes the execution block; the executor fetches as its first act." `docs/global-context/core.md` defines **Directive** as "one line stating route (fresh or existing session) and model tier, then the execution block as a paste block" — two parts, no third, and nothing before the execution block. `docs/batons/baton-20260822T153848.md` records the same settlement under "What this session settled".
Consequence: The rule has a live half and a dead half. The live half — a mid-delta directive pins the spec branch and its SHA rather than the default branch — is correct and stated nowhere else. The dead half names the artifact that was supposed to carry the ref. An agent following this file drafts a directive with a sync block in it, which Core's directive definition has no slot for, and the executor receives a two-part structure with a third part attached. Worse, if the agent instead drops the sync block as retired, the rule loses its mechanism entirely and the spec-branch ref is pinned nowhere.
Fix: Replace `:132-134` with: "**Mid-delta directives cite the spec branch.** A directive drafted while a delta is open pins the spec branch and its SHA, not the default branch. Because the executor fetches as its first act, the branch and SHA are stated as instructions inside the execution block." Drop the `skills/directive-dispatch.md` citation with it (C10).
Related: C2, C10

## C2 — blocking
Claim: Six prose uses of the retired term *dispatch*, plus one retired *sync block*, in a document at `status: agreed`.
Location: `roles/chief-of-staff.md:51`, `:65`, `:67`, `:107`, `:142`, `:144`; `:134`
Evidence: Verified by running. `grep -oniE 'dispatch(ed|ing)?' roles/chief-of-staff.md` returns nine hits at `:51`, `:65`, `:67` (×2), `:107`, `:134`, `:142`, `:144` (×2). Three of the nine are inside the path `skills/directive-dispatch.md` (`:67`, `:134`, `:144`) and are a criterion-3 defect rather than a criterion-4 one (C10); the remaining six are prose. `LEXICON.md` Retired terms: "**Dispatch** — retired 2026-08-21. Write 'hand the directive to an execution session,' or 'direct.'" The baton's known-stale list records "14 governed files still use 'dispatch'; conformed on touch per LEXICON," and LEXICON states the touch rule: "any file edited for another reason is conformed to this lexicon as part of that edit."
Consequence: Criterion 8, and the touch rule makes it mandatory once any other finding here is applied. The concrete cost is at `:51`, where the sentence dictates what the agent should *say* to Dave — "here is the dispatch; tell me what to change" — so a retired term is scripted into the role's own output, not merely used to describe it. `:142` is worse than a word: it is a section heading, so the file's table of contents advertises a retired mechanism.
Fix: `:51` → "here is the directive; tell me what to change". `:65` → "A directive is handed to an execution session as a paste block and landed by the executor". `:67` → "not before it is handed over". `:107` → "Those are written when the directive is handed over". `:142` heading → "### Handing a package to an execution session". `:144` → "A package is handed to an execution session as a directive, and the decomposition doc — not the spec — is the source the directive derives from." `:134` is C1.
Related: C1, C3, C10

## C3 — blocking
Claim: Four vendor tokens name a specific harness where Core's three-layer vocabulary names the layer.
Location: `roles/chief-of-staff.md:61`, `:62`, `:71`, `:90`
Evidence: Verified by running. `grep -on 'Claude Code\|\bCC\b' roles/chief-of-staff.md` returns `:61` "Claude Code", `:62` "CC", `:71` "CC", `:90` "Claude Code". `docs/global-context/core.md` states the layers: "**decision** — chat; **execution** — an LLM agent session; **shell** — commands run in a shell," and defines *execution session* as "an LLM agent session carrying out a directive against a working tree." The baton settles that "Harnesses are adapters downstream of bundles."
Consequence: Criterion 8, and criterion 1 compounds it. A bundle is compiled for whatever agent reads it; naming one vendor's harness makes three of this file's rules read as inapplicable to an agent running anywhere else, and `:61` — "Dave does not read Claude Code output" — states a fact about one product where the intended rule is about the execution layer generally. The section heading at `:59` already uses the right word ("execution-session reports"), so the body contradicts its own heading.
Fix: `:61` → "Dave does not read execution-session output. He pastes it here; the Chief of Staff is the reader." `:62` → "Write directives so the returned report is **triageable by the Chief of Staff**". `:71` → "On a pasted execution report:". `:90` → "In a decision session (execution belongs to an execution session):" — which also resolves C11 for that line.
Related: C11

## C4 — blocking
Claim: The section at `:36-40` restates decision-layer rule 9 with a diverging body, under a heading tagged with an unresolvable question ID.
Location: `roles/chief-of-staff.md:36-40`
Evidence: Verified by running. `grep -n "State is computed" docs/global-context/decision-layer.md roles/chief-of-staff.md` returns both: `decision-layer.md:28` "**State is computed, never maintained.** Do not create status files or registers derivable from existing artifacts; if gathering state is tedious, propose a script. A loose-end tracker is a record, not derived state." and `chief-of-staff.md:38` "**State is computed, never maintained.**" — the lead sentence is identical. The bodies are not: this file says "Do not create **or update** state registers, status files, or any hand-maintained copy of state derivable from existing **sources**"; the Decision Layer says "existing **artifacts**" and adds the loose-end-tracker carve-out, which this file omits.
Consequence: Criterion 4, and the divergence is the live cost rather than the redundancy. `OPEN-ITEMS.md` is a loose-end tracker, and this file's copy — with no carve-out and an added "or update" — forbids the Chief of Staff from updating it, while the Decision Layer explicitly permits it. Both files land in this role's bundle, so the agent receives a prohibition and its exception with no rule for which wins. Separately, the heading's `(Q3a)` tag cites a decision-artifact question ID that appears nowhere in the bundle: criterion 1.
Fix: Delete `:36-40` entirely, heading included. The Decision Layer states the rule and states it better.
Related: C5, C6, C7

## C5 — non-blocking
Claim: The Pre-staging section restates decision-layer rules 5 and 7 and then argues for them.
Location: `roles/chief-of-staff.md:42-57`
Evidence: Verified by reading both at `ed926db`. `decision-layer.md:21` rule 5: "**Pre-stage the predictable.** When the next artifact is obvious, draft it and present it ready for correction." `decision-layer.md:23` rule 7: "**He says what; you deliver how.** The first response to a request is the artifact — a block, a draft, a path — not a plan for it." This file at `:44-46`: "Where the next step is predictable, prepare it: draft the directive, assemble the file set, stage the command. Present work ready to approve, not ready to start." At `:49-53`: "**Do not ask permission to produce a predictable artifact.** 'Shall I draft the directive? y/n' fails: it makes progress wait on another chat cycle for an obvious step." `:52` — "A wrong draft costs a correction, not a cycle" — is an argument for the rule, not the rule.
Consequence: Criterion 4 and criterion 6. Two of the three surviving sentences are the same instruction the bundle already carries one file earlier; the third — `:46-47` "Pre-staging is drafting, not landing — it flips no status, agrees no document, releases nothing" — is the only part not already stated, and it is buried under fourteen lines that are.
Fix: Reduce `:42-57` to its residue: keep `:46-47` ("Pre-staging is drafting, not landing — it flips no status, agrees no document, releases nothing") and `:55-57` (the bar on deciding consequential calls). Delete `:44-45`, `:49-53`, and the trailing justification at `:52`.
Related: C4, C6

## C6 — non-blocking
Claim: The report-handling procedure at `:71-82` restates decision-layer rules 1, 2, and 13, and the directive-SHA paragraph at `:65-69` restates Core's `Directive file` definition.
Location: `roles/chief-of-staff.md:63-82`
Evidence: Verified by reading both at `ed926db`. Item 1 "Triage, do not relay" and item 2 "Lead with a pithy bullet list" against `decision-layer.md:15` rule 2: "**Lead with the point.** … When he pastes output, triage it: one line per item that needs his judgment, up front; hold or discard the rest." Item 3 "One question at a time; never stack" against `decision-layer.md:14` rule 1: "**One question at a time.** Ask the one that matters most, wait, then the next." `:62-63` "Write CC directives so the returned report is **triageable by CoS**" against `decision-layer.md:35` rule 13: "Write it so the returned report is triageable by the next decision session." `:65-69` against `core.md` Vocabulary: "**Directive file** — the markdown file holding a directive's instructions, written and committed by the executor as its first act, and thereafter cited by path and the SHA of the commit that landed it."
Consequence: Criterion 4 and criterion 6. `:81-82` — "Do not info-dump the report and let Dave find what matters. His attention is the scarce resource — spend it on judgment, not reading" — is a "never X" restatement of item 1 followed by its own justification, which criterion 6 names explicitly as the thing to cut. The residue that is *not* duplicated is `:67-69` — that a report omitting the path/SHA pair is incomplete and the Chief of Staff must ask for it; that obligation is on the reader of the report and appears nowhere else.
Fix: Keep `:67-69` (capture the path/SHA pair first; a report omitting it is incomplete, ask for it) and item 3's "Do not leave an item until every question it raises is answered," which is stricter than rule 1 and not stated elsewhere. Delete `:62-63`, `:65-66`, items 1 and 2 at `:73-77`, and `:81-82`.
Related: C4, C5

## C7 — non-blocking
Claim: Two of the five Constraints restate Core rules 2 and 7.
Location: `roles/chief-of-staff.md:149`, `:154`
Evidence: Verified by running. `grep -n "Dave decides\|Proposes; does not decide" docs/global-context/core.md roles/chief-of-staff.md` returns `core.md:15` "2. **Dave decides. You propose.** Agreement, release, prioritization, and publication are his." and `chief-of-staff.md:149` "- Proposes; does not decide. Agreement, release, and prioritization are Dave's." `:154` "Renders state honestly. Reports 'could not determine X' rather than guessing" against `core.md:23` rule 7: "**Say what is unverified.** Never report assumed as verified. 'Could not determine' beats a guess."
Consequence: Criterion 4. `:149` also drops *publication* from Core's four-item list, so the shorter copy silently narrows the rule for the one role most likely to publish something.
Fix: Delete `:149` and `:154`. The remaining three constraints (`:150-153`, `:155-156`) are role-specific and stay.
Related: C4

## C8 — non-blocking
Claim: The file defines *tranche*, and its definition is not LEXICON's.
Location: `roles/chief-of-staff.md:86-88`
Evidence: Verified by running. `grep -n -A1 "^\*\*Tranche\*\*" LEXICON.md` gives "**Tranche** — one concurrent workstream of build work." This file at `:86-88`: "A **tranche** is a scope of agreed spec proposed for implementation as one body of work: proposed by CoS, approved by Dave."
Consequence: Criterion 4, and Core rule 9 — two sources disagree. The definitions are not synonyms: LEXICON's turns on *concurrency* (which is what makes the claimed/disjoint-territory rule at `:135-140` work), and this one turns on *agreed spec scope* and omits concurrency entirely. The rule at `:137-140` that a second tranche must claim disjoint territory depends on the concurrency sense, and this file supplies the other one three sentences before stating it.
Fix: Delete the definition at `:86-88` and keep only what is role-specific: "One decomposition doc per tranche; change packages are entries within it." The proposal-and-approval half is already at `:151` and in `operating-model.md` §Responsibilities.
Related: C9

## C9 — non-blocking
Claim: The Open spec deltas preamble restates LEXICON's `Open spec delta`, `Reconciliation`, and `Claimed`.
Location: `roles/chief-of-staff.md:121-123`, `:137-139`
Evidence: Verified by reading both at `ed926db`. `:121-123` "While a tranche executes, its spec edits land ungated on `spec/<tranche-slug>` and are gated together at reconciliation" against `LEXICON.md` **Open spec delta** ("the interval during which a tranche's spec branch carries edits that the default branch does not… no reviewer gate and no per-edit ceremony") and **Reconciliation** ("the whole accumulated diff goes through the reviewer gate **once**"). `:137-139` "A document already appearing in one open delta's diff is claimed and may not be claimed by a second" against **Claimed** — "of a spec document: appearing in an open delta's diff. A claimed document may not be claimed by a second open delta."  `:138` is a near-verbatim copy.
Consequence: Criterion 4. The three role-binding consequences at `:126-140` are genuinely this file's and are worth keeping; the definitional preamble under them is the bundle's third statement of the same mechanism.
Fix: Delete `:121-123` and reduce `:137-139` to the instruction: "Check the claim before proposing the second tranche." Keep the three bulleted consequences and `:139-140` (the refusal to merge two deltas' edits), which is stated nowhere else.
Related: C8

## C10 — non-blocking
Claim: Sixteen path-shaped references, three of which name things absent from the tree or about to be.
Location: `roles/chief-of-staff.md:10`, `:23` (×2), `:26`, `:30`, `:31`, `:32`, `:34`, `:67`, `:100`, `:112`, `:121`, `:123`, `:134`, `:144`
Evidence: Verified by running. A count of backtick-delimited path tokens returns 16. Existence checked with a loop over each: `bin/state` (`:23`) does not exist — the file says so itself ("Until `bin/state` exists"), but the reference is still a path a bundle reader cannot resolve. `roles/orchestrator-agent.md` (`:10`) exists now and retires this pass — see `reviews/orchestrator-agent-cycle-1.md`, which recommends deletion. The remaining fourteen resolve at `ed926db`.
Consequence: Criterion 3, and Core rule 13 for `:9-10` specifically: deleting `roles/orchestrator-agent.md` without editing that line leaves this file — the one at `status: agreed` — citing a deleted path to explain its own provenance. `:26-34`, the read-sequence, is the defensible cluster: those are paths the agent is instructed to *open and read*, which is a different act from citing a file for a rule. The rest are citations.
Fix: For the read-sequence (`:26-34`), keep the paths and drop the parenthetical rule citations (`policies/commit-and-change-control-policy.md` at `:30`, `context-sets/spec-and-change-discipline.md` at `:34`) — the sequence needs the targets, not the warrants. For `:9-10`, replace the supersession sentence with "Short form: **`cos`**." and nothing more; the supersession is a fact about a file that will not exist. Delete the citations at `:67`, `:112`, `:123`, `:134`, `:144`. Keep `:100` (the decomposition doc's own destination) and `:23`'s `bin/state` conditional.
Related: C1, C2

## C11 — observation
Claim: The file never states its session kind in Core's vocabulary, and it is the only one of the five at `status: agreed`, so applying any finding above flips it to `in-review`.
Location: `roles/chief-of-staff.md:1-5`; `:90`
Evidence: Verified by running. `grep -niE 'decision session|execution session|in chat' roles/chief-of-staff.md` returns only `:90` "In chat (execution belongs to Claude Code)" — the section heading at `:59` says "execution-session reports", but the file never says what kind of session *it* is. `operating-model.md` §Responsibilities does: "It operates as a decision session, not an execution session." Frontmatter at `:2-3` reads `status: agreed`, `last-reviewed: reviews/expedited-log.md @ c9e87ad…`; the other four files in this cycle are `draft` or `superseded`. `policies/document-metadata-policy.md` §Revision lifecycle: "When an `agreed` document is edited, the same commit flips `status: in-review` and resets `last-reviewed: null`. … No exceptions for trivial edits **on the way out**."
Consequence: Criterion 7. An agent receiving this bundle cannot tell from this file whether it may commit, and `:90`'s parenthetical is the only signal — expressed in vendor terms (C3). Separately, the metadata policy makes this a scoping fact for whoever executes the edit list: the commit that applies C1–C10 must also carry the frontmatter transition, and this document then needs a re-gate before it returns to `agreed`. That is not a defect in the file; it is the price of the edit list, and it is recorded here so the executor does not discover it after committing.
Fix: Add one sentence under the title: "The Chief of Staff operates as a decision session." Then, in the same commit that applies C1–C10, set `status: in-review` and `last-reviewed: null`.
Related: C3
