# Review: context-sets/production-grade-software.md — cycle 1

Verdict: ready-with-findings
Reviewed: `context-sets/production-grade-software.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11a)
Date: 2026-08-21
Scope: the whole file — frontmatter and all five body sections — against all ten
criteria of `docs/global-context/review-rubric.md` @ `7310937`. This is the
file's first review artifact of any kind. Criterion 4 judged line-by-line
against `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, and `operating-model.md` @ `7310937`. Mechanical sweeps run
(verified by running `grep`): retired terms, vendor and model names, path-shaped
references — all three come back clean or near-clean on this file, which is not
true of any other file in this cycle. A tree-wide `grep` for "Top K" was run to
establish P4.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `operating-model.md`, `context-sets/base.md`,
`context-sets/testing-and-verification.md`, `specs/prd-template.md` (the "Top K"
definition line only), `bin/bundle-methodology`, `decisions/log.md`
Not inspected: the SLO and error-budget machinery this file leans on —
`boundaries/live-integration-boundaries.md`, `roles/skeptic-risk-agent.md`,
`roles/release-manager-agent.md`, `BACKLOG-v2.md`, and `OPEN-ITEMS.md:760` — were
located by `grep` for P4 but not read. P4's claim is about where "Top K" is
*defined*, not about whether those documents use it consistently; that
consistency was not checked. `specs/prd-template.md` was read at line 43 only.
No claim is made about whether the fifteen attributes at L25–39 are the right
fifteen — the review tests placement and duplication, not completeness of a
domain checklist.
Findings: 6 — 0 blocking, 3 non-blocking, 3 observations
Prior cycle: none
Dave should inspect: nothing.

## Criterion 10 — disposition

**retain-with-changes.**

This is the one file in the cycle-11a scope that clearly earns its place. Three
of its five sections state things no other file in the bundle states:

- **Production-grade attributes** (L21–41) — the fifteen-item checklist and,
  more importantly, the closing instruction: "Not every change requires deep
  treatment of every attribute. The agent must explicitly decide which
  attributes are relevant." That is an agent instruction with a decision
  procedure attached, and it appears nowhere in Core, the Decision Layer,
  `LEXICON.md`, or `operating-model.md`.
- **Evidence requirements** (L43–57) — the eleven-item menu of what can
  constitute evidence. `operating-model.md` §Control surfaces names seven
  categories of control and §Change package names twelve contents; neither
  enumerates evidence *kinds*. `context-sets/base.md` and
  `context-sets/testing-and-verification.md` classify evidence by verification
  boundary, which is a different axis.
- **Failure mode thinking** (L59–68) — six questions asked of every meaningful
  change. Unstated elsewhere. The one overlap is Q2's error-budget clause, which
  `context-sets/testing-and-verification.md:134-138` also raises, and even there
  the framing differs.

The two weak sections are the Summary (P1) and "Production-grade does not mean"
(P2). Neither is load-bearing and both are short.

The finding list below is the edit list. It is short, contains nothing blocking,
and the file is coherent after it.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — P4 |
| 2 | `audience:` is the selector | partial — P5 |
| 3 | No path references | **pass** — zero path-shaped references; the only file in this cycle's scope that is clean here |
| 4 | Core states it → remove it here | partial — P1, P2 |
| 5 | Agent instruction, not authoring principle | pass — L41 is the model of what criterion 5 asks for |
| 6 | Instructions, not rationale | partial — P2 |
| 7 | Session kind is explicit | fail — P3 |
| 8 | Tiers, not model names | **pass** — zero vendor or model names |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |

## Counts (instruction 4)

- **Rules restated from Core / Decision Layer / LEXICON / operating-model:** 2,
  both in weak sections. Summary L19 → `operating-model.md:205`; "Production-grade
  does not mean" L81 → `operating-model.md:174` and
  `context-sets/base.md:81`. This is the lowest count of the six files in scope
  by a wide margin — the next lowest is 8.
- **Path-shaped references:** 0.
- **Vendor and model names:** 0.
- **Retired terms:** 0.

## P1 — non-blocking
Claim: The Summary restates `operating-model.md` §Operating standard.
Location: `context-sets/production-grade-software.md:13-19`
Evidence: Verified by reading. This file L19: "The system is intentionally
specified, tested to stated boundaries, observable, recoverable, and
understandable enough to operate." `operating-model.md:205` @ `7310937`:
"Production-grade software is intentionally specified, verified to declared
boundaries, operationally supportable, observable, recoverable, and honest about
remaining uncertainty." Six of the seven attributes match; the wordings differ
in three places ("tested to stated" vs "verified to declared", "understandable
enough to operate" vs "operationally supportable", and this file drops "honest
about remaining uncertainty").
Consequence: The definition of the term the whole file is named for exists in
two files with three differences, one of which is substantive — dropping
"honest about remaining uncertainty" removes the clause that ties the definition
to the evidence model. An agent given both has two definitions and, under Core
rule 9, must surface rather than reconcile them.
Fix: Delete L13–19. `operating-model.md:205` states it, and states it better.
The file can open directly at §Production-grade attributes; its `purpose:`
frontmatter already carries the one-line framing the Summary was doing.

## P2 — non-blocking
Claim: "Production-grade does not mean" is framing rather than instruction, and
its one operative sentence is stated twice elsewhere.
Location: `context-sets/production-grade-software.md:70-81`
Evidence: Verified by reading. L72–78 is a six-item list of what the term does
not mean — perfect, over-tested, enterprise-heavy, no known gaps, every
dependency mocked and live-tested in every run, every line reviewed by a human.
No instruction is issued. L81 ("It does mean known gaps are visible and
intentionally accepted") restates `operating-model.md:174` ("known gaps are
explicit") and `context-sets/base.md:81`. L78 additionally restates
`operating-model.md:53` and `:18` (code review is not the default gate).
Consequence: Criterion 6. Twelve lines that argue against misreadings of a term
rather than instructing the agent. The cost is small and the risk is the usual
one: text that justifies rather than instructs survives edits to the rules it
was justifying.
Fix: Delete L70–81. If the anti-over-testing point is wanted as a rule, it is
already carried by
`context-sets/testing-and-verification.md:200` ("Boundary-sensitive does not
mean 'must be overtested.' It means 'do not overclaim.'"), which states it as an
instruction.

## P3 — non-blocking
Claim: Session kind is never stated.
Location: `context-sets/production-grade-software.md:1-11`
Evidence: Verified by reading. `audience: [all-roles, human]` names roles, not
session kinds, and no body sentence declares the kind. Compare
`docs/global-context/core.md:10`, `docs/global-context/decision-layer.md:10`,
and `operating-model.md:10`, all of which declare it in their first line.
Consequence: Criterion 7. The file is execution-session material throughout —
attributes to consider on a change, evidence to gather, failure modes to think
through — with one exception, L67 ("Can Dave debug or roll back?"), which is a
question an execution session asks about itself rather than a decision-session
rule. So the answer is unambiguous and simply unstated, which is the cheapest
class of criterion-7 failure to fix.
Fix: Add one line after the H1: "Rules for execution sessions." No other change
needed.

## P4 — observation
Claim: "Top K" is used as a defined term but is defined only in a per-project
spec template that no methodology bundle carries.
Location: `context-sets/production-grade-software.md:32,64`
Evidence: Verified by running. `grep -rn "Top K"` across the tree @ `7310937`
returns the term in `operating-model.md:155`,
`context-sets/testing-and-verification.md:135`, `roles/skeptic-risk-agent.md`,
`roles/release-manager-agent.md`, `roles/architect-agent.md`,
`boundaries/live-integration-boundaries.md`, `specs/trd-template.md:59`
("Inherit the Top K journeys from the PRD … Do not redefine them here"), and
`specs/prd-template.md:43`, which is the only definition: "Define the **Top K**
journeys — the K most important journeys out of all possible". `grep` over
`LEXICON.md` @ `7310937` returns no entry.
Consequence: Criterion 1. An agent reading a methodology bundle meets "Top K
journey SLO" in this file's failure-mode questions and in its attribute list,
and the sentence that defines it lives in a template the bundle does not
contain. The agent can infer roughly what is meant, which is worse than not
knowing — it will produce plausible answers about journeys it has no list of.
`specs/trd-template.md:59` compounds it by forbidding redefinition, so the term
is deliberately single-sourced to a document outside the methodology corpus.
Fix: Not this file's to fix alone — the term is used by eight documents. It
belongs in `LEXICON.md` as a term of the methodology, with the per-project *list*
staying in the PRD where `specs/trd-template.md:59` puts it. Raising it here
because this file is one of the eight; the edit is a `LEXICON.md` edit.

## P5 — observation
Claim: No `order:`, and three frontmatter fields that nothing reads.
Location: `context-sets/production-grade-software.md:1-9`
Evidence: Verified by reading and running. `audience: [all-roles, human]` — both
reserved, valid per `bin/aimeta/frontmatter.py:16`. No `order:`. `context-set:`,
`purpose:`, and `include-when:` are consumed by neither `bin/bundle` (reads
`depends-on:`) nor `bin/bundle-methodology` (reads `audience:`).
Consequence: `include-when: Changes affecting reliability, ops, security, or
release quality` is an instruction to whoever assembles context — criterion 5 —
and no assembler reads it. Since this file is being retained, the ordering gap
is live rather than moot: it declares `depends-on: [base]` and has no `order:`
to place it after `base`.
Fix: Add `order:`, after whatever value `context-sets/base.md` takes. Drop
`context-set:`, `purpose:`, and `include-when:` — noting that `purpose:` is
doing real work as the file's one-line framing under P1's deletion, so if it
goes, that framing moves into the body as a single sentence.
Related: P1

## P6 — observation
Claim: The section headers use "should consider" where the file's own best
sentence uses "must".
Location: `context-sets/production-grade-software.md:23,45,61`
Evidence: Verified by reading. L23 "A production-grade change should consider:";
L45 "A production-grade claim should be supported by evidence such as:"; L61
"Every meaningful change should consider:". Against L41: "The agent must
explicitly decide which attributes are relevant."
Consequence: Criterion 5 is satisfied in spirit — these are addressed to the
agent — but three of the file's four list-introducing sentences are advisory
while the one instruction that makes the attribute list actionable is
imperative. An agent optimising for compliance can satisfy all three "should
consider" lists by considering nothing and satisfy L41 by naming one attribute.
Consequence is modest and the fix is one word each.
Fix: L23 → "A production-grade change is assessed against:". L45 → "A
production-grade claim is supported by evidence such as:". L61 → "Every
meaningful change answers:". Leave L41 as it is; it is the sentence the section
turns on.
