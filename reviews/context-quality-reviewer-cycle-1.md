# Review: roles/context-quality-reviewer.md — cycle 1

Verdict: changes-required
Reviewed: `roles/context-quality-reviewer.md` @ `ed926db`
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (111 lines) against `docs/global-context/review-rubric.md` @ `ed926db`, all ten criteria, criterion 10 answered first. Criterion 4 judged against the current text of `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`, all @ `ed926db`. The output-shape section is judged against the settled rule in `reviews/agent-review-policy-cycle-1.md` finding A2.
Cross-checked: `docs/global-context/review-rubric.md` (all ten criteria, mapped against this file's four dimensions); `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `operating-model.md` (all @ `ed926db`); `skills/spec-review-cycle.md` §Review artifact schema; `reviews/agent-review-policy-cycle-1.md` finding A2; `roles/spec-reviewer-agent.md` §Continuity scan (Depth 3), `roles/chief-of-staff.md`, `roles/pm-em-owner.md`, `roles/orchestrator-agent.md`; `policies/document-metadata-policy.md` (`audience:` values); the working tree, for the existence of every path this file's Scope section names.
Not inspected: `roles/skeptic-risk-agent.md` against its own rubric criteria — cycle 19b, read here only for the boundary this file draws against it at `:100-101`; whether this role has ever been invoked and what it produced — no artifact in `reviews/` names it as reviewer, and I did not search chat or other records; `docs/global-context/review-rubric.md` against its own criteria — it is the instrument of this pass and is treated as foundation, not as a document under review; `MANIFEST.md`, which names this file at `:134`, since it is outside this cycle's scope.
Findings: 6 — 3 blocking, 2 non-blocking, 1 observation
Dave should inspect: X1 and X4 together. X1 proposes merging this file away; X4 is the residue and the price — dimension 2, escalation-vs-decision wording, is a genuine lens the ten-criterion rubric does not have, so the merge means adding an eleventh criterion to `docs/global-context/review-rubric.md` mid-pass. That is a change to the instrument every other file in Pass 1 is being judged against, and it is your call whether it lands now, lands in Pass 2, or does not land at all — in which case the lens is lost and this file should be retained instead.

## Criterion 10, first and explicitly

**merge-into `docs/global-context/review-rubric.md`.**

Three of this file's four evaluation dimensions are rubric criteria under
different names, and the fourth — Scope, at `:69-78` — names a directory tree
that does not exist. What is left after the duplicated dimensions and the dead
scope come out is one lens and one output format; the output format belongs to
the artifact schema per A2, and the lens is the residue that justifies the
merge rather than a bare retirement.

The mapping, dimension by dimension:

| This file | Already stated in |
| --- | --- |
| `:27-34` 1. Story coherence — "would produce different behavior depending on which documents were loaded" | `review-rubric.md` criterion 1 ("written to be read inside a generated bundle, by an agent that has never seen the repository") and criterion 10 ("contributes something no other file in that bundle states") |
| `:47-55` 3. Unhelpful duplication — "copies could drift and produce inconsistent agent behavior" | `review-rubric.md` criterion 4 ("Core states it → remove it here"); `core.md:44` rule 13 |
| `:57-67` 4. Token efficiency — "preamble an agent would not use", "examples that do not add information not already in the rule", "hedging that dilutes precision" | `review-rubric.md` criterion 6 ("Instructions, not rationale. Rules are stated; arguments for them are cut") |
| `:36-45` 2. Escalation vs. decision wording | **nowhere** — the residue; see X4 |
| `:80-93` Required output format | `skills/spec-review-cycle.md` §Review artifact schema — A2 |
| `:95-102` Relationship to other roles | the roles' own documents; `core.md:15` rule 2 |
| `:104-111` Non-goals | restates this file's own body; `core.md:15` rule 2 |

Named target: `docs/global-context/review-rubric.md`, carrying dimension 2 as an
eleventh criterion. Secondary landing for nothing else — the remaining content
is duplicated, dead, or owned by the artifact schema.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — X2; the Scope section instructs the agent to review a tree it cannot open and which does not exist |
| 2 | `audience:` is the selector | pass — `[context-quality-reviewer, chief-of-staff, human]`; the role's own slug, the role that assigns it, and the reserved value |
| 3 | No references to other files by path | fail — X2; eleven, of which nine name a nonexistent tree |
| 4 | Core states it → remove it here | fail — X4, X5 |
| 5 | Agent instruction, not authoring principle | pass — the dimensions are questions the agent asks of a document, which is an agent instruction |
| 6 | Instructions, not rationale | fail — X6; `:20-23` and `:48-52` |
| 7 | Session kind is explicit | fail — X6; "session role" at `:9` is not either of Core's two kinds |
| 8 | Tiers, not model names; route and model, not track | pass — verified by running; `grep -onE 'dispatch\|sync block\|\bprompts?\b\|\btracks?\b' roles/context-quality-reviewer.md` returns nothing, and the only vendor-shaped token is `CLAUDE.md` at `:78`, a filename in the dead Scope list (X2) |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | fail — merge, see above |

## X1 — blocking
Claim: The file's four evaluation dimensions are three rubric criteria plus one lens, so it does not contribute what no other file states.
Location: `roles/context-quality-reviewer.md:25-67`
Evidence: Verified by reading `docs/global-context/review-rubric.md` and this file side by side at `ed926db`; the full mapping is the table above. The closest pairs, quoted: dimension 4's "sections that restate what is already clear from context / preamble that an agent would not use / examples that do not add information not already in the rule" against criterion 6's "Rules are stated; arguments for them are cut. 'Never X' restatements of a stated rule and trailing justifications are cut." Dimension 3's "Is the same information repeated in multiple documents in ways that create maintenance risk or divergence?" against criterion 4's "The file does not restate a rule that Core or the Decision Layer already states."
Consequence: Criterion 10. This file was written before the rubric and describes the job the rubric now does; Pass 1 is that job being executed, and it is being executed against the rubric, not against this document. Keeping both means two instruments for one audit with no rule for which governs — and they are not equivalent instruments, since the rubric's ten criteria include six things this file has no dimension for (`audience:` as selector, path references, agent-instruction-not-authoring-principle, session kind, tiers-not-model-names, filename convention). An agent handed this role reviews a document against four dimensions and passes it, while the same document fails the rubric on criteria 2, 3, 7, 8, and 9.
Fix: Merge. Carry dimension 2 (`:36-45`) into `docs/global-context/review-rubric.md` as an eleventh criterion — see X4 for the proposed wording — and delete this file. Nothing else transfers.
Related: X2, X3, X4

## X2 — blocking
Claim: The Scope section names a directory tree that does not exist in the repository.
Location: `roles/context-quality-reviewer.md:69-78`
Evidence: Verified by running. A loop testing each path this section names, executed against the working tree at `ed926db`: `ai` → MISSING. `context-sets`, `policies`, `roles`, `skills`, `boundaries`, `specs` → all EXIST at the repository root, without the `ai/` prefix. `CLAUDE.md` and `AGENTS.md` → EXIST at the root. So seven of the nine paths named are wrong by one path component, and the root the section is scoped to — "The full `ai/` repository" at `:71` — resolves to nothing. `:13` and `:20` repeat the same dead root in prose.
Consequence: Criterion 1 and criterion 3. An agent given this role and told to review "the full `ai/` repository" has no such thing in its bundle and no such thing in the tree; it either reviews nothing or silently substitutes its own guess about what was meant. `:78` compounds it: `CLAUDE.md` and `AGENTS.md` are adapters, which the baton records as deliberately stale and deferred to Pass 2 — so the one part of the scope list that does resolve points the reviewer at the two files it should not be reviewing yet. The section is not repairable by dropping the prefix, either: a bundle-compiled agent has no directory tree at all, so scope in this world is an `audience:` value, not a path list.
Fix: Subsumed by the merge — the rubric states its own scope ("Criteria every non-code file in this repository is examined against") without a path list, and needs nothing from here. If Dave retains this file instead of merging it, `:69-78` is replaced by "Every non-code file in this repository," and `:13` and `:20` drop the `ai/` prefix.
Related: X1

## X3 — blocking
Claim: `Required output format` states a review report's field list and summary shape, which the artifact schema owns.
Location: `roles/context-quality-reviewer.md:80-93`
Evidence: Verified by reading both at `ed926db`. This file states five per-finding fields — **Dimension**, **Location**, **Finding**, **Severity** (blocking/advisory), **Proposal** — plus a closing summary of counts by dimension and an "overall assessment: ready / needs revision / significant issues." `skills/spec-review-cycle.md` §Findings states five different per-finding fields — `Claim`, `Location`, `Evidence`, `Consequence`, `Fix` — and §Header states the verdict vocabulary as `ready | ready-with-findings | changes-required`. `reviews/agent-review-policy-cycle-1.md` A2 settled that the schema owns output shape and role documents do not.
Consequence: Criterion 4 and the A2 rule. The two verdict vocabularies are three words each and overlap on exactly one: `ready`. "needs revision" and "significant issues" are this file's invention and map onto nothing in the schema, so an artifact written to `:93` cannot be read by anything that consumes `Verdict`. More seriously, the per-finding list has no `Evidence` field, so a finding produced under this role cannot state whether it was verified by running or inferred by reading — the distinction the schema calls "not optional" and Core rule 6 requires of every claim.
Fix: Delete `:80-93`. It transfers nowhere: the schema already has every field this list was reaching for, under better names.
Related: X1

## X4 — non-blocking
Claim: Dimension 2, escalation-vs-decision wording, is the file's only content with no home elsewhere, and the rubric has no criterion covering it.
Location: `roles/context-quality-reviewer.md:36-45`
Evidence: Verified by reading all ten rubric criteria at `ed926db` against this dimension's four sub-items. The dimension asks: "Does any wording create a gap where an agent would make an autonomous decision rather than escalating to Dave?" — covering "underspecified conditions that invite interpretation", "missing explicit escalation triggers", "language that implies agent authority the methodology does not intend to grant", "ambiguous role boundaries where two roles could plausibly claim ownership". No rubric criterion asks this. Criterion 5 is adjacent — "Every rule is an instruction to the agent reading it" — but it tests the *form* of a rule, not whether the rule leaves an agent free to decide something that is Dave's. `core.md:15` rule 2 and `operating-model.md` §Escalation state the substantive requirement (escalate; Dave decides), but neither is a review lens for finding where a document fails it.
Consequence: Criterion 10 in the constructive direction — this is the reason the disposition is merge rather than retire. Losing this lens loses the one check aimed at the failure mode the whole repository exists to prevent: a document worded so an agent proceeds where it should have stopped. The fourth sub-item also happens to be the lens that catches this cycle's own S9 and O1 findings — two roles plausibly claiming one responsibility — which the ten criteria surface only indirectly, through criterion 10.
Fix: Add to `docs/global-context/review-rubric.md` as criterion 11: "**Escalation is not left to inference.** No wording lets the agent decide what is Dave's. Underspecified conditions, missing escalation triggers, language implying authority the methodology does not grant, and boundaries two roles could both claim are defects." Then delete `:36-45` with the rest of the file. This edits a foundation document mid-pass; see the header's `Dave should inspect`.
Related: X1

## X5 — non-blocking
Claim: `Relationship to other roles` and `Non-goals` restate this file's own body and Core rule 2.
Location: `roles/context-quality-reviewer.md:95-111`
Evidence: Verified by reading. `:102` — "**Dave**: receives all findings; makes all resolution decisions" — against `core.md:15` rule 2: "**Dave decides. You propose.**" `:107` ("rewrite documents (it flags; Dave decides)") restates `:44-45` and `:88`, each of which already says the proposal is optional and Dave decides — three statements of one rule in 111 lines. `:108` ("evaluate implementation or tests") restates `:13-16`. `:111` ("persist beyond this review session") restates `:9-11`.
Consequence: Criterion 4 and criterion 6. Four of the five items across these two sections are "never X" restatements of rules stated above them, which criterion 6 names as the thing to cut. The one item that is not — `:109-110`, "assess whether the methodology is correct as a matter of engineering judgment — only whether it is coherent and safe as LLM context" — is a real boundary and is the only sentence in either section worth carrying anywhere.
Fix: Delete `:95-111` with the merge. If the file is retained instead, keep `:109-110` and delete the rest.
Related: X1

## X6 — observation
Claim: The file names no session kind in Core's vocabulary, and its Purpose section argues rather than instructs.
Location: `roles/context-quality-reviewer.md:9-11`, `:18-23`, `:48-52`
Evidence: Verified by running. `grep -niE 'decision session|execution session|in chat' roles/context-quality-reviewer.md` returns nothing. `:9-11` says "This is a **session role** — purpose-built for a specific review task. It is not a standing role in the operating model. Load this role when directed by Dave; discard it when the session ends" — which describes the role's lifetime, not which of Core's two kinds it runs in. `:20-23` — "Quality failures in these documents produce agent errors that are hard to trace: wrong decisions, silent gaps, and divergent behavior. This role exists to find those failures before they manifest in agentic sessions" — is the argument for the role, not an instruction to it. `:48-52` similarly argues when duplication is and is not acceptable before stating the flag.
Consequence: Criterion 7 and criterion 6. The session-kind gap is not idle here: the role produces findings over the whole corpus and explicitly does not rewrite (`:107`), which reads as an execution session returning an artifact — but "Load this role when directed by Dave; discard it when the session ends" reads as a decision session Dave is talking to. Whether the output is a committed artifact or a chat report is left to the agent. Recorded as an observation rather than a finding because the merge disposition makes it moot: the rubric states no session kind because it is an instrument, not a role.
Fix: None if the merge lands. If the file is retained, add "The Context Quality Reviewer runs as an execution session and returns a review artifact," and cut `:20-23` and `:48-50` to their rules.
Related: X1
