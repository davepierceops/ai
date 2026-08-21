# Review: LEXICON.md — cycle 9

Verdict: changes-required
Disposition (criterion 10): retain-with-changes — the only all-roles home for the
dispatch, block, and spec-state vocabulary; strip what the Decision Layer now
states, the history, and the citations.
Reviewed: `LEXICON.md` @ `26f8f10`
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: full text against all ten rubric criteria (`docs/global-context/review-rubric.md`
@ 26f8f10), criterion 10 answered first per the cycle-5 directive; criterion 4
judged against the current text of core.md and decision-layer.md @ 26f8f10.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`skills/spec-review-cycle.md` (directive defaults), the other three cycle-5 documents.
Not inspected: the policies, context sets, roles, and skills LEXICON cites —
whether those files agree with the definitions here was not re-verified this
cycle; duplication against files other than core and decision-layer.
Findings: 3 blocking, 3 non-blocking, 1 observation
Prior cycle: `reviews/LEXICON-cycle-8.md`
Dave should inspect: L1 — the vocabulary now lives twice, and the two homes have
disjoint reach (decision-layer never reaches execution sessions; LEXICON is
all-roles). Which file is the single home is a structural decision, not an edit.

## L1 — blocking
Claim: The layers, blocks, dispatch, and handoff vocabulary is restated from the
Decision Layer, which now states it as rules.
Location: sections "The three layers", "Blocks", "Dispatch", "Handoff"
Evidence: side-by-side reading of both texts @ 26f8f10 — three layers → DL-12;
paste block → DL-12; command block → DL-12; execution block → DL-12; directive
(route, model, execution block, all three stated) → DL-12; handoff → DL-12;
baton (decision-to-successor-decision only) → DL-12; the prompt prohibition
("do not say 'prompt'") → DL-12; decision-session definition → Decision Layer
preamble; directive-file self-containment ("nothing from the conversation") →
DL-13; the Instruction entry's "cannot be executed as written stops the
session" → Core 11.
Consequence: two canonical statements of the same terms drift independently —
they already differ in detail (LEXICON's directive entry names a model, DL-14
speaks in tiers) — and criterion 4 makes every duplicate a defect. But the naive
fix (delete from LEXICON) strips the block and directive vocabulary from
execution bundles, because the Decision Layer states "Execution sessions never
receive this file." The duplication and the reach problem must be resolved
together.
Fix: pick a single home for the shared vocabulary and make the other defer.
Either the terms live here (all-roles) and DL-12 shrinks to decision-only
register rules, or the execution-facing subset moves to an execution-layer file.
Decision Layer is verdict-ready, so this is Dave's call; no edit until it is made.

## L2 — blocking
Claim: The Directive entry names a model — "model *Opus 5*" — where the rubric
and DL-14 require tiers.
Location: section "Dispatch", Directive entry
Evidence: verified by reading; DL-14 @ 26f8f10 defines frontier / solid
general-purpose / cheap and states "Model by workload, not by name."
Consequence: the lexicon contradicts the layer that governs model selection, and
the named default goes stale with every model generation.
Fix: state the default in tier language ("model frontier") or drop the default
clause and leave defaults to the class's own document.
Related: L5

## L3 — blocking
Claim: 14 path-shaped references in the body (frontmatter excluded).
Location: throughout; grep-verified list — `roles/chief-of-staff.md` (39),
`skills/spec-review-cycle.md` (41, 70, 135), `policies/commit-and-change-control-policy.md`
(57), `skills/directive-dispatch.md` (79, 115), `context-sets/spec-and-change-discipline.md`
(81, 135), `skills/command-blocks.md` (109), `context-sets/collab-workflow.md` (151),
`roles/coder-agent.md` (152), `docs/packages/package-c-change-package.md` (153),
`vendors/claude-code/environment-config.md` (189)
Evidence: verified by running grep over the file @ 26f8f10.
Consequence: a bundle reader cannot follow any of them; each is a dangling
citation that implies the definition is incomplete without another file.
Fix: where the citation carries a needed rule, state the rule; where it is
provenance, cut it.

## L4 — non-blocking
Claim: Authoring history and rationale are carried as content (criterion 6).
Location: intro paragraphs 3–5 ("Adoption scope", "The touch rule" preamble,
"These definitions were chosen… `handoff`, which carried six senses"); "Keeping
them separate is the whole point of this section"; "This matches every existing
use in the repo…"; the baton entry's "named because that particular transfer had
no name and kept borrowing one"; the reconciliation entry's "which is why
`agreed` on the default branch never lies".
Evidence: verified by reading.
Consequence: an agent in a bundle gets drift archaeology instead of definitions;
the file is materially longer than its rule content.
Fix: cut the history; keep the touch rule itself (it is an instruction), cut its
justification sentence.

## L5 — non-blocking
Claim: Vendor and model names, counted (criterion 8): Claude Code ×4 (lines 35,
40 twice, 41), Opus 5 ×1 (line 69), plus the `vendors/claude-code/…` path (189).
Location: "The three layers", "Dispatch", "Retired terms"
Evidence: verified by reading.
Consequence: layer definitions bind to a vendor; "currently Claude Code" is
hedged but the parenthetical corpus citations are not.
Fix: define layer 2 as "an LLM agent session" (already done) and drop the vendor
naming; Opus 5 is L2.
Related: L2

## L6 — non-blocking
Claim: The Spec state section ("Spec branch", "Open spec delta",
"Reconciliation", "Claimed") is decision-session material in an all-roles file
(criterion 7).
Location: section "Spec state"
Evidence: inferred by reading — the terms govern gating and agreement, which
the Decision Layer preamble assigns to decision sessions.
Consequence: every execution bundle carries vocabulary its reader never uses.
Fix: if the vocabulary split of L1 is resolved by audience, move these terms to
the decision-facing home.

## L7 — observation
Claim: No `order:` in frontmatter, though a lexicon's position in a bundle
matters — it should precede the files that use its terms (criterion 2).
Location: frontmatter
Evidence: verified by reading.
Consequence: bundle position is left to the compiler's default.
Fix: add `order:` near the front, after core.
