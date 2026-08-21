# Review: README.md — cycle 3

Verdict: changes-required
Disposition (criterion 10): retire — it lands in bundles carrying
`operating-model.md` and contributes almost nothing that file does not state;
its remaining job (repository front door for humans) is one the bundle model
assigns to a human-only file, which is new authorship, not this text. Surviving
content: the CC BY 4.0 license line moves to a repo-level home (a LICENSE file
or the human-facing replacement); the frontmatter-enforcement paragraph already
lives in `policies/document-metadata-policy.md`, which it cites; nothing else is
unique.
Reviewed: `README.md` @ `26f8f10`
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: full text against all ten rubric criteria (`docs/global-context/review-rubric.md`
@ 26f8f10), criterion 10 answered first per the cycle-5 directive; criterion 4
judged against the current text of core.md and decision-layer.md @ 26f8f10.
Cross-checked: `operating-model.md` @ 26f8f10 (duplication, R1),
`docs/global-context/core.md`, `docs/global-context/decision-layer.md`.
Not inspected: whether any key principle survives *only* here versus also in a
policy or context set beyond operating-model.md — R1's duplication mapping was
against operating-model.md and the foundation only; the licensing implications
of moving the CC BY 4.0 line.
Findings: 3 blocking, 3 non-blocking
Prior cycle: `reviews/README-cycle-2.md`
Dave should inspect: R1 — retiring the repo's root README is his call, as is
where the license notice lands.

## R1 — blocking
Claim: The file duplicates `operating-model.md` nearly wholesale and contributes
no rule of its own to a bundle (criterion 10).
Location: whole file
Evidence: side-by-side reading @ 26f8f10 — the title itself collides ("AI
Operating Model" vs. operating-model.md's "Operating Model"); the block-quoted
core model (Dave as PM/EM/owner/operator, agents as implementation team,
evidence over human review) appears in both; key principles map onto
operating-model sections: #1 → "Core operating rule", #2 → "Trust model", #3 →
"Must not: equate passing tests with shippability", #4 → "distinguish mocked,
contract, live, browser, and production verification", #5 → the responsibilities
and control-surfaces sections, #6 → "Operating standard", #7 → "Relationship to
tools", #8 → "Source of truth", #9 → "Change flow" steps 1–5, #10 → "Release
gate"; the change-package list (lines 64–72) is a subset of operating-model's
twelve-item list.
Consequence: two files state the operating model; every future edit must land
twice or the two drift — Core 13's obligation made permanent by duplication.
Fix: retire per the disposition above. Any sentence found to exist only here
moves into operating-model.md before removal.

## R2 — blocking
Claim: 21 path-shaped references (criterion 3), the most of any cycle-5 document.
Location: grep-verified — `CLAUDE.md` (12, 38), `AGENTS.md` (13, 38),
`.claude/**` (13), `.claude/agents/` (38), `.claude/skills/` (38),
`policies/document-metadata-policy.md` (14), `operating-model.md` (26, 57),
`specs/` (27, 58), `context-sets/` (28, 59), `policies/` (29), `roles/` (30),
`skills/` (31), `boundaries/` (32), `/ai/` (36),
`roles/spec-reviewer-agent.md` (61), `roles/chief-of-staff.md` (61)
Evidence: verified by running grep over the file @ 26f8f10.
Consequence: the document map and reading list are nothing but paths — the file
is structurally a table of contents, which is the artifact the bundle compiler
replaces.
Fix: none in place; resolved by R1's retirement.

## R3 — blocking
Claim: The file assumes the reader can open the repository (criterion 1).
Location: "This directory is the source of truth…" (line 16), "Document map",
"How to use this directory" ("Before starting a meaningful change, agents
should read: …")
Evidence: verified by reading.
Consequence: inside a bundle, every instruction in the "How to use" section is
unexecutable — the reader has no directory, and the compiler already made the
selection the section tells the agent to make by hand.
Fix: none in place; resolved by R1's retirement.

## R4 — non-blocking
Claim: Rules restated from core (criterion 4): key principle 2 ("Agent claims
require evidence") → Core 5; principle 8's spec/Issue conflict hard stop →
Core 9; principle 10's human release gate as Dave's call → Core 2.
Location: "Key principles" 2, 8, 10
Evidence: side-by-side reading @ 26f8f10.
Consequence: subsumed by R1; listed for the criterion-4 record.
Fix: resolved by R1's retirement.

## R5 — non-blocking
Claim: Vendor names, counted (criterion 8): `CLAUDE.md` ×2, `AGENTS.md` ×2,
`.claude/…` paths ×3 (lines 12–13, 38). No model names.
Location: intro paragraph, "Adapters"
Evidence: verified by running grep.
Consequence: the adapters paragraph is itself sound (it names vendor files in
order to demote them), but it belongs with the metadata policy that already
governs the exclusion, not in an all-roles bundle.
Fix: resolved by R1; the adapters rule survives in operating-model.md's
"Relationship to tools" and `policies/document-metadata-policy.md`.

## R6 — non-blocking
Claim: Principle 5 carries its argument (criterion 6): "Gating delivery on a
human grokking unfamiliar code at machine speed doesn't scale; compressing the
code-writing step is the primary value."
Location: "Key principles" 5
Evidence: verified by reading.
Consequence: rationale an agent cannot act on, restating a rule stated twice
already in the same file (intro block quote and principle 5's first sentence).
Fix: resolved by R1's retirement.
