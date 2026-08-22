# Review: LEXICON.md — cycle 10

Verdict: changes-required
Reviewed: LEXICON.md @ cb3e75a
Baseline: 28d11fa (cycle 9 reviewed state)
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: the full file. Two passes: (a) L1–L7 checked against the cycle-6
decisions — L1: the Layers, Blocks, Dispatch, and Handoff sections are gone,
their entries live in Core's Vocabulary, and no deferring pointer remains;
L2: no model name remains; L3: zero path-shaped references, verified by
running grep (the production-system sentence keeps its rule and drops the
policy path); L4: the adoption-scope, history, and rationale paragraphs are
cut and the touch rule survives as an instruction; L5: zero vendor names,
"an LLM agent session" is the term; L6: the spec-state terms are retained;
L7: order: 2. All seven resolved as decided. (b) all ten rubric criteria
(docs/global-context/review-rubric.md @ cb3e75a) re-applied to the current
text, and the five in-scope files cross-checked for a term stated in two
places. Both findings below are from pass (b).
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md,
operating-model.md, engagements/working-with-dave.md @ cb3e75a; the cycle-6b
and 6c directives (the rule in force on sync blocks and dispatch).
Not inspected: duplication against files outside the five in scope; whether
the files that use lexicon terms still agree with the definitions here — the
touch rule and their own cycles govern that. No bundler was run; bundle
membership and load order are inferred from frontmatter, not observed.
Findings: 2 blocking
Prior cycle: reviews/LEXICON-cycle-9.md
Dave should inspect: L9 — which file is the single home for the
decision-session definition; the same class of call as cycle 6's L1.

## L8 — blocking
Claim: The Prompt entry's shell bullet reads "the one that opens a dispatch is
a *sync block*" — using the retired term "dispatch" and stating a sync block,
which the rule in force abolishes.
Location: LEXICON.md:68-69 ("Retired terms", Prompt entry)
Evidence: verified by running grep over the five in-scope files @ cb3e75a —
this is the only occurrence of either term in the scope. Core's Vocabulary @
cb3e75a states the directive form with no sync block (cycle-6b V1 deleted the
entry; cycle-6c retired "dispatch"), and both of those directives confined
their rewrites to core.md and decision-layer.md, deferring every other file.
Consequence: an all-roles bundle presents "sync block" as a live term and
instructs the reader that one opens the handing of every directive — a
procedure the directive format no longer contains; an agent following it would
expect or emit a block that must not exist.
Fix: cut the clause — the bullet becomes "**What runs in a shell** — a
*command block*." No replacement entry.

## L9 — blocking
Claim: The decision-session definition is stated in two places — this file's
Sessions entry and the Decision Layer's preamble (criterion 4; the cycle-7
cross-file check).
Location: LEXICON.md:19-22 ("Sessions"); docs/global-context/decision-layer.md:10
Evidence: verified by reading side by side @ cb3e75a — both state "triages,
decides, and produces the artifacts that direct and record work" and "does not
[itself] carry out the changes a directive specifies". They already differ in
detail: LEXICON adds the artifact list ("directives, session records, tracker
updates"); decision-layer adds "that work happens in an execution session".
Cycle 9's L1 evidence named this pair, but the cycle-6 L1 decision moved only
the Layers, Blocks, Dispatch, and Handoff entries and never dispositioned the
preamble, so the pair stands undecided rather than resolved.
Consequence: the cycle-6 structural decision — vocabulary has one home, split
by reach — is violated by the surviving pair, and the two homes have disjoint
reach: decision-layer never enters execution bundles, LEXICON is all-roles, so
the two statements drift independently and different session kinds can hold
different definitions of the same term.
Fix: one home. Either the decision-layer preamble shrinks to scope-only
("Rules for decision sessions. Loads after Core and adds to it. Execution
sessions never receive this file."), deferring the definition to the all-roles
home already ordered ahead of it in every decision bundle — the fix that
preserves the cycle-6 split by reach — or the Sessions entries leave LEXICON.
Which home is Dave's call; no edit until it is made.
