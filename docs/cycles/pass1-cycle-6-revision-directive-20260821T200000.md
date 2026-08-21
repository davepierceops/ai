# Directive — Pass 1, Cycle 6 revision: docroot identity files + vocabulary move

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

Documents in scope, all @ 28d11fa8a99e2a926b7c33e9a77898812e4934da:
- docs/global-context/core.md
- docs/global-context/decision-layer.md
- LEXICON.md
- README.md
- operating-model.md
- engagements/working-with-dave.md

Reviews triaged: reviews/LEXICON-cycle-9.md, reviews/README-cycle-3.md, reviews/operating-model-cycle-3.md, reviews/working-with-dave-cycle-1.md @ 28d11fa.
Rubric: docs/global-context/review-rubric.md @ 28d11fa. Every edit leaves every file in scope conformant to all ten criteria.

## Structural decisions (Dave, 2026-08-21)

- Vocabulary has one home, split by reach. Domain-neutral terms — paste block, command block, execution block, directive, handoff, baton, the three layers — move into Core as a new section "Vocabulary". Fiducial-specific terms stay in LEXICON.
- README is retired. The public front page is rewritten in Pass 2 once bin/bundle exists.
- The Comfy engagement is over. Engagement files are generic and carry role audiences; no client-shaped selector exists. engagements/comfy/ is untouched by this directive.

## Decisions

### L1 — accept (Dave)
Move the Layers, Blocks, Dispatch, and Handoff entries from LEXICON into Core as a section "Vocabulary" placed after "Acting". Merge with decision-layer rule 12's text where the two state the same term; where they differ, Core takes LEXICON's definition and decision-layer's brevity. Delete decision-layer rule 12 entirely; renumber. LEXICON keeps every term not moved and loses the moved entries completely — no deferring pointer.

### L2 — accept
Any model default states a tier: "model frontier".

### L3 — accept
Every path-shaped reference in LEXICON: state the rule if needed, otherwise cut. Zero remain.

### L4 — accept
Cut authoring history and rationale. Keep the touch rule as an instruction.

### L5 — accept
Drop vendor names; "an LLM agent session" is the term.

### L6 — accept
Spec-state terms stay in LEXICON (fiducial-specific, all-roles).

### L7 — accept
LEXICON: order: 2.

### R1–R6 — accept
Delete README.md. Before deleting, confirm LICENSE exists at the repo root (it does at 28d11fa; stop if not). Any sentence existing only in README and carrying an instruction an agent needs is moved to operating-model.md; expect none.

### O1 — accept
Delete each line restating Core 2, 3, 5, 7, 9. Keep entries with no Core counterpart.

### O2 — accept
Inline what is load-bearing; cut provenance citations. Zero path references remain.

### O3 — accept (Dave: one home)
Cut the trust-model section. Core 5–7 carry the claim rules. The evidence-class vocabulary (mock/contract/live/browser/production-verified, unverified, deferred, accepted risk) is not restated here; its home is decided in the context-sets cycle.

### O4 — accept
"tracker issues"; name the vendor once as the current instance, or not at all.

### O5 — accept
Keep the two-question sentence; cut the rest.

### O6 — accept
One line stating session scope: this file governs both session kinds.

### O7 — accept
operating-model: order: 3.

### W1 — accept (Dave: role audiences)
Add frontmatter: status: draft, last-reviewed: null, audience: [assistant, cartographer, skeptic, human], order: 10.

### W2 — accept
Strip every rule restated from Core or decision-layer. Keep the residue: the infra verification ladder (plan/apply/serving/delta-verified), the zero-write-access client guardrail, and the working-with-Dave engagement rules that are not restatements. Remove Comfy-specific facts (client name, dates, people); where a fact is needed as an example, generalize it.

### W3 — accept
Delete the preamble.

### W4 — accept
One line: this file is for execution sessions within an engagement.

### W5 — accept
Leave as is.

### W6 — accept
Covered by W1 and W2.

## Execution

1. Fetch origin/main; verify the tree contains 28d11fa with no later edits to the six files.
2. Apply every decision. Then re-read all six files end to end: any rule number, term, or count that the edits leave stale is fixed (Core rule 13). Core and decision-layer rule numbering after the move is the renumbered sequence; no prose elsewhere cites them.
3. Run bin/check-frontmatter --all. Stop and report on failure.
4. Commit on branch p1-cycle-6-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Per file: one line, rule or section count before → after (README: deleted). Then branch and SHA. Then any decision not applied as written, with reason.
