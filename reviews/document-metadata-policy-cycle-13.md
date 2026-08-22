# Review: policies/document-metadata-policy.md — cycle 13

Verdict: changes-required
Reviewed: policies/document-metadata-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (372 lines), against docs/global-context/review-rubric.md @ 2a722bb, all ten criteria. This is the first full-rubric pass over the file; cycles 1-12 pre-date the rubric and were scoped to individual sections.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ 2a722bb); docs/batons/baton-20260822T153848.md; skills/spec-review-cycle.md (review artifact schema and filename convention); roles/spec-reviewer-agent.md (the two bounded exceptions); policies/decision-log-policy.md, policies/agent-review-policy.md, policies/testing-policy.md; the presence of every path this file enumerates.
Not inspected: bin/flip-agreed, bin/check-frontmatter, and bin/aimeta/expedited.py — behaviour is asserted from the file's own text and the baton, not verified by running the tools; reviews/expedited-log.md contents; whether the repo's existing agreements conform to the routes described here, which cycle 12 examined and this pass did not re-open; the cycle 1-12 findings and their dispositions, other than confirming cycle 12 closed clean; the gate-document class list checked for presence only, not for whether each named document does in fact state a gate.
Findings: 8 — 2 blocking, 4 non-blocking, 2 observations
Prior cycle: reviews/document-metadata-policy-cycle-12.md
Dave should inspect: D2. The length finding proposes cutting roughly a quarter of the file, and much of what it proposes cutting is argument you dictated across earlier cycles to stop specific conditions being negotiated away. Cutting it is a judgment about whether the argument still has to travel with the rule, and that judgment is yours, not the reviewer's.

## Criterion 10, first and explicitly

**retain-with-changes.**

This file is the single home for the frontmatter schema, the five `status`
values, the `last-reviewed` pointer format, the revision lifecycle, and the two
bounded routes to `agreed`. Nothing else in the repository states any of it, and
enforcement reads its in-scope set directly from the Scope section. It earns its
place decisively. The findings below are an edit list, not a case for retirement.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — D4; and D2, in that a file this long is skimmed rather than read inside a bundle |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`; correct, since every role's documents are governed by this schema. No `order:`, and position does not matter |
| 3 | No path references | fail — D4. The Scope globs (25-34), the gate-document class list (173-198), `reviews/expedited-log.md`, and `decisions/log.md` are **exempt**: they are the normative data the policy operates on, not deferrals of content to another file. A reader acts on them from the bundle alone |
| 4 | Core states it → remove it here | pass — no rule here is stated by Core, the decision layer, LEXICON, or operating-model. The `agreed` = Dave's decision gloss (74-75) narrows Core rule 2 to a field's semantics rather than restating it |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | fail — D2, the dominant defect |
| 7 | Session kind explicit | fail — D6 |
| 8 | Tiers, not model names | fail — D5 (vendor names). No model name, no tier claim; no use of the retired *dispatch*, *sync block*, or *prompt*, and every *track* hit is the carved-out ordinary sense |
| 9 | Filenames `<descriptor>-<timestamp>` | pass — the file prescribes `reviews/expedited-log.md`, a stated convention naming the file, which criterion 9 permits; it prescribes no generated filename |
| 10 | Earns its place | pass — see above |

## D1 — blocking
Claim: The in-scope glob list does not cover `docs/global-context/**`, so four governed files carrying frontmatter sit outside enforcement and cannot be agreed.
Location: policies/document-metadata-policy.md:23-34 (in-scope list), 52 ("Enforcement (hooks) checks exactly the in-scope set")
Evidence: Verified by running. `ls docs/global-context/` returns core.md, decision-layer.md, inventory.md, review-rubric.md; `head -1` on each returns `---`, so all four carry frontmatter and expect to be governed. None matches any of the ten glob entries at 25-34. The baton records the consequence and the disposition under "Agreement is blocked on scope": "`bin/flip-agreed` refuses `docs/global-context/**` (outside the metadata policy's glob list). Dave chose: leave everything `draft` through Pass 1; fix the scope once, in the document-metadata-policy cycle, together with reserving `all-decision-roles`. Sequencing rule: the reserved value lands before the glob extends."
Consequence: Core and the decision layer — the two files every bundle is built around — are permanently unagreeable. They will finish Pass 1 as `draft`, and a `draft` methodology document is by this file's own rule at 365-369 "not loaded as governing context unless the human explicitly directs it". The policy therefore excludes from governed context the files that state the governing rules.
Fix: Out of scope for this review by directive. The edit belongs to the revision cycle, and the baton holds both the disposition and the sequencing rule — the reserved `all-decision-roles` audience value lands before the glob extends. This finding is the pointer to it and deliberately designs nothing.

## D2 — blocking
Claim: At 372 lines the file is the longest governed document in the repository, and roughly a quarter of it is justification rather than instruction.
Location: policies/document-metadata-policy.md — whole file; the justification passages are 80-81, 145-154, 156-170, 200-205, 212-224, 226-229, 241-256, 258-261, 273-276, 280-287, 289-291, 320-326, 348-351
Evidence: Verified by running. `wc -l` across policies/, roles/, context-sets/, boundaries/, skills/, LEXICON.md, operating-model.md, and docs/global-context/ ranks this file first at 372, ahead of skills/spec-review-cycle.md (331), context-sets/testing-and-verification.md (234), and operating-model.md (228). Summing the thirteen passages above gives 96 lines, 25% of the file. Sampling them: 212-224 is thirteen lines arguing that condition 5 is load-bearing; 241-256 is sixteen lines explaining that a mechanical check was weakened and what carries the weight instead; 145-154 is ten lines on why the ten-line threshold is arbitrary.

Note on the criterion: the rubric has no standalone length criterion. Length is judged here under criterion 6 (instructions, not rationale) and criterion 1 (written to be read inside a bundle). The directive asks for particular care on this file, and the baton supplies the standard — documents that do not fit in working attention get skimmed.
Consequence: Criterion 6 directly, and criterion 1 by consequence. The rules an agent must apply — the five status values, the pointer format, the edit-flips-to-in-review rule, the five conditions on each route — are interleaved with argument at roughly one line in four, so the reader who skims extracts the arguments as readily as the rules and cannot tell from shape alone which is which. The specific hazard is the conditions: condition 3 on the expedited path is a fifteen-line passage (156-170) whose operative sentence is its first, and a skimmed reading takes the enumerated list at 172-198 for the rule when the file says twice that the criterion governs and the list is a floor.
Fix: Cut the thirteen passages to the rule they justify, keeping the operative sentence of each. Four are load-bearing enough to keep in compressed form and are flagged as such rather than cut blind: 156-170's "when it is unclear, it is ineligible"; 200-205's "the list is normative where it names a document, and cannot bound the class"; 212-224's "any finding escalates, however small"; 241-256's "the SHA cited in `last-reviewed` must appear in an entry in the log". Each survives as one sentence. That removes on the order of 80 lines without losing a rule. Dave's call per the header — see "Dave should inspect".
Related: D7

## D3 — non-blocking
Claim: The file uses *route* for a path to `agreed`, where Core and LEXICON use *route* for the fresh-or-existing choice a directive states.
Location: policies/document-metadata-policy.md:289, 291, 304, 317, 326
Evidence: Verified by running. `grep -inE '\broute\b'` in this file returns those five lines, all meaning the doc-only path to agreement — "The route reaches only documents in the frontmatter in-scope set", "Dave asks for this route", "this route neither reaches that gate nor overrides it". The same grep over core.md and LEXICON.md returns core.md:49, "one line stating route (fresh or existing session) and model tier", and LEXICON.md:100, "A directive states route and model tier; there is no third part" — the definition given when *track* was retired.
Consequence: One word carries two fixed meanings across canonical documents. This is the ambiguity LEXICON exists to remove, and the collision is with the term LEXICON most recently pinned down: an agent reading "Dave asks for this route" in a bundle that also carries Core's directive vocabulary has to infer from context which sense applies. It also blocks the obvious sentence "the directive states its route", which would now be ambiguous inside this file.
Fix: Use *path* throughout, which the file already uses for the same idea eleven times ("the expedited path", "this path does not reach that gate"). Rename "the doc-only cycle" route language at 289, 291, 304, 317, 326 to *path*. LEXICON is not edited: *route* keeps its single meaning, and this file stops competing for it.

## D4 — non-blocking
Claim: Nine passages defer content to another file by path rather than stating it.
Location: policies/document-metadata-policy.md:159-161, 207-208, 218, 228, 311, 317-318, 320, 351
Evidence: Verified by running the path grep over the file and classifying each hit. The nine above are pointers — "Spec agreement is gated by the Spec Reviewer Agent (`roles/spec-reviewer-agent.md`)" (207-208, and again at 317-318); "it becomes a full cycle per `skills/spec-review-cycle.md`" (218); "`skills/conversation-retro.md` routes anything a retrospective surfaces through a full cycle" (228), a claim about another file's content; "It extends the within-document consistency check `context-sets/spec-and-change-discipline.md` already requires" (311); "`bin/flip-agreed` verifies the pointer's format" (320); "the per-document application of the canonical-vs-derived principle in `policies/source-of-truth-policy.md`" (351); and 159-161, which cites `operating-model.md` and `boundaries/human-review-boundary.md` as worked examples inside an argument. Distinguished from the exempt path lists recorded against criterion 3 above.
Consequence: Criteria 3 and 1. The reader cannot open any of them. Most are recoverable — 207-208 states the rule and the path is decoration — but two are not: 228 asserts a rule that lives entirely in another file, so a bundle without that file leaves the reader knowing a rule exists and not what it says; and 320 describes what enforcement does and does not check, which is the paragraph that tells the reader the five conditions are unenforced judgments. That is exactly the content criterion 3 requires to be stated rather than pointed at.
Fix: For 228 and 320, state the rule and drop the path: "a document may exclude its own revisions from this path, and the retro skill does" becomes the rule itself; the enforcement paragraph states what is checked without naming the script. For 207-208, 218, 311, 317-318, 351, delete the parenthetical path and keep the sentence. For 159-161, the paths go with the passage under D2.
Related: D2

## D5 — non-blocking
Claim: The out-of-scope list names a vendor's product files.
Location: policies/document-metadata-policy.md:42
Evidence: Verified by reading. "Adapters: `CLAUDE.md`, `AGENTS.md`, `.claude/**`. These are thin deployment targets, and leading YAML may collide with tool consumption." `CLAUDE.md` and `.claude/**` are Claude-specific; `AGENTS.md` is not vendor-bound.
Consequence: Criterion 8. A vendor name in a canonical policy is the coupling operating-model.md:85 prohibits when it bars agents from storing durable policy only in vendor-specific tooling, and it dates the file to one tool. The exposure is bounded — the names appear in an exclusion, so a repo with no Claude adapter simply has nothing to exclude — but a second adapter for a second vendor requires editing this policy, which is the wrong file to have to touch.
Fix: State the exclusion by class rather than by name: "Adapters — the per-tool entry files that point a vendor's harness at this methodology, and their configuration directories. These are thin deployment targets, and leading YAML may collide with tool consumption." The class covers `AGENTS.md` and any future adapter without naming a vendor. The baton assigns the adapter files themselves to Pass 2; this is the reference to them in an in-scope document, which Pass 2 does not reach.

## D6 — non-blocking
Claim: The file does not state which session kind it addresses, and it addresses both differently.
Location: policies/document-metadata-policy.md — whole file; contrast the Agent behavior section, 353-372
Evidence: Verified by reading. No line names a session kind. The content splits cleanly on it: the Sequence sections (263-276, 328-339), the revision lifecycle (109-127), and the expedited and doc-only conditions describe commits an execution session makes; conditions 2, 4 and 5 of the expedited path and conditions 2 and 4 of the doc-only path are Dave's acts in a decision session; the Agent behavior rules at 353-372 bind any session that loads a document. context-sets/testing-and-verification.md:11 shows the convention — a single line, "Rules for execution sessions."
Consequence: Criterion 7. An execution session cannot tell which of the five conditions it is expected to satisfy and which are Dave's, so it either blocks on conditions it cannot meet or asserts compliance with conditions it cannot observe. The file says at 220-224 that conditions 3 and 5 are judgments enforcement cannot check, but never says whose judgment, which is the same gap stated from the other side.
Fix: Add one line under the title: "This file governs both session kinds; the conditions marked as Dave's are decision-session acts." Then mark the conditions — conditions 2, 4 and 5 of the expedited path, conditions 2 and 4 of the doc-only path — as his, which the text already implies at 209-210 and 304-306 without saying so structurally.

## D7 — observation
Claim: The gate-document class list names `README.md`, which no longer exists.
Location: policies/document-metadata-policy.md:198
Evidence: Verified by running. `ls README.md` → absent; the baton records "README retired; rewritten human-only in Pass 2 once `bin/bundle` exists." This is a **separate occurrence** from the one the directive excludes: step 6 puts "the README unmatched-glob warning" out of scope, which is the in-scope glob at line 33 and the `bin/check-frontmatter` WARN it produces. Line 198 is in the normative gate-document class list, produces no warning, and is not that item.
Consequence: Low. The list is explicitly a floor rather than a boundary (200-205), so a dead entry costs nothing operationally — nothing resolves through it and no check reads it. It is a Core rule 13 loose end: a changed fact that did not change everywhere it appears. It becomes live again in Pass 2, when a rewritten README either belongs in this class or does not, and the stale entry would then pre-answer that question by accident.
Fix: Remove line 198 when the glob entry at line 33 is settled, so both README references are resolved in one edit rather than leaving the second behind. No action needed before then.

## D8 — observation
Claim: The file's own frontmatter carries `superseded-by: null` on a document that is not superseded.
Location: policies/document-metadata-policy.md:5
Evidence: Verified by reading. Frontmatter reads `status: agreed` with `superseded-by: null`. The file's own rule at 102-107 makes `superseded-by:` "required if and only if `status: superseded`" and then permits the null form: "A key present with value `null` (e.g., `superseded-by: null` on a draft) is permitted and treated as the field being absent."
Consequence: None mechanically — the file is conformant, and its own null-semantics rule is what makes it conformant, using very nearly this line as the worked example. The cost is exemplary: this is the schema document, and it is the only one of the four policies in this cycle carrying the field, so a reader inferring the convention from the canonical file's own frontmatter infers that the key is expected on non-superseded documents when 102-104 says it is required only on superseded ones.
Fix: Delete line 5. The rule that permits it stays; the schema document stops modelling the permitted-but-unnecessary form.
