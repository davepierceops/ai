# Review: operating-model.md — cycle 3

Verdict: changes-required
Disposition (criterion 10): retain-with-changes — the change flow, release-gate
tiers, change package, definition of done, and escalation triggers are stated
nowhere in core or the decision layer and earn the file its place; the
responsibilities roster and trust model shrink to what core does not state, and
the delegations to other files are inlined or cut.
Reviewed: `operating-model.md` @ `26f8f10`
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: full text against all ten rubric criteria (`docs/global-context/review-rubric.md`
@ 26f8f10), criterion 10 answered first per the cycle-5 directive; criterion 4
judged against the current text of core.md and decision-layer.md @ 26f8f10.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`README.md` @ 26f8f10 (duplication — see `reviews/README-cycle-3.md` R1).
Not inspected: duplication against `policies/*` and `context-sets/*` (notably
whether the release-gate section and `policies/commit-and-change-control-policy.md`
state the same tiers twice, and how much of "Trust model" survives in
`context-sets/base.md`) — criterion 10's "no other file in that bundle states
it" was verified against core, decision-layer, and README only.
Findings: 3 blocking, 3 non-blocking, 1 observation
Prior cycle: `reviews/operating-model-cycle-2.md`
Dave should inspect: the residue split in O1 — which sentences of the
responsibilities and trust-model sections are domain content worth keeping
versus core restated.

## O1 — blocking
Claim: Rules restated from core (criterion 4), with rule numbers.
Location: "Trust model", "Source of truth", "Responsibilities"
Evidence: side-by-side reading @ 26f8f10 — "Claims require supporting evidence"
(Trust model) and "provide evidence for claims" (Agents, Must) → Core 5; "stay
within scope" (Must) and "expand scope without approval" (Must not) → Core 3;
"hide uncertainty" (Must not) and "identify unverified areas" (Must) → Core 7;
"surface the conflict, name both sides, and wait for Dave. Do not resolve by
guessing or by preferring the more recent artifact" → Core 9; Dave's ownership
of prioritization, agreement, and release decisions → Core 2.
Consequence: the same rules maintained in two canonical places; they already
diverge in wording, and Core 13 makes every future edit a two-file edit.
Fix: delete each restated line; keep the entries with no core counterpart
("state assumptions", the mocked/contract/live/browser/production distinction,
"weaken verification to satisfy implementation", "claim live behavior from
mocked evidence", "store durable policy only in vendor-specific tooling").

## O2 — blocking
Claim: 8 path-shaped references plus one by-name document reference (criterion 3).
Location: grep-verified — `context-sets/spec-and-change-discipline.md` (17, 116),
`context-sets/base.md` (33, 112), `policies/source-of-truth-policy.md` (46),
`skills/spec-review-cycle.md` (116), `policies/commit-and-change-control-policy.md`
(139), `/ai/` (216); plus "README #5" (138)
Evidence: verified by running grep over the file @ 26f8f10.
Consequence: dangling in a bundle; "README #5" additionally points at a
document this cycle recommends retiring.
Fix: inline what is load-bearing (see O3), cut the provenance citations; delete
the README cross-reference.

## O3 — blocking
Claim: The trust model delegates its own content to another file (criterion 1):
"See `context-sets/base.md` for the evidence vocabulary and mock rule."
Location: "Trust model" (line 33); same pattern at line 112 ("see
`context-sets/base.md`") for the meaningful-change definition
Evidence: verified by reading.
Consequence: a bundle reader whose selection excludes base.md has an operating
model whose central section is one sentence and a pointer; the rubric requires
the file to state what it needs.
Fix: either state the evidence vocabulary here (if base.md retires from that
role) or cut the trust-model section entirely and let base.md carry it — one
home, chosen deliberately; note Core 6 already states the claim-class
vocabulary, so the residue may be small.

## O4 — non-blocking
Claim: Vendor names, counted (criterion 8): GitHub ×3 ("GitHub Issues" in
Source of truth ×2, "`human-gate` GitHub issue reference" in Change package),
OpenFeature ×1 (Release gate, hedged with "e.g."). No model names; no tier
language needed — the file makes no model selection.
Location: "Source of truth", "Release gate", "Change package"
Evidence: verified by reading.
Consequence: the Issues layer of the canonical order is bound to a vendor; the
file elsewhere insists vendor systems are implementation details (its own
principle 7 in README's numbering).
Fix: "tracker issues" with the vendor named once as the current instance, or
accept as a deliberate binding and leave it; OpenFeature is already hedged.

## O5 — non-blocking
Claim: Trailing justifications carried as content (criterion 6).
Location: "The red-gate at step 4 is mandatory: a test that passes before
implementation is a broken test, not a head start"; "Gating… quality review
asks 'is this good?'; skeptic/risk asks 'where is this lying to us?'"; "the
same provider-independence logic as the vendor-tooling boundary"; "this is the
main cost the mechanism introduces"
Evidence: verified by reading.
Consequence: modest — these are short and some carry instructional content
(the two-question framing arguably earns its place); the pure rationale tails
do not.
Fix: keep the two-question sentence if judged instructional; cut the rest.

## O6 — non-blocking
Claim: Session kind is not explicit (criterion 7): an all-roles file mixing
decision-session material (release-gate tiers, flag ownership and debt, Dave's
responsibilities) with execution-facing flow (red-gate, test/coder separation).
Location: whole file; sharpest in "Release gate"
Evidence: inferred by reading against the decision-layer preamble's session
definitions.
Consequence: execution bundles carry release-gate mechanics their reader cannot
act on.
Fix: state the file's session scope in one line, or split the release-gate
detail toward the decision-facing policy that governs it.

## O7 — observation
Claim: No `order:` in frontmatter, though this is the framing document and
should precede roles and skills in any bundle that carries it (criterion 2).
Location: frontmatter
Evidence: verified by reading.
Fix: add `order:` after core and the lexicon.
