---
status: draft
last-reviewed: null
audience: [all-roles, human]
order: 3
---

# Operating Model

This file governs both session kinds: decision sessions and execution sessions.

## Summary

This project is built by an AI-native software team.

Dave acts as PM, EM, owner, and operator. Agents perform implementation, testing, review, analysis, and documentation work.

Dave does not rely on routine line-by-line code review. The primary control is evidence: specifications, tests, reviews, verification boundaries, operational signals, and known gaps.

Work is **spec-first** and **test-driven**: nothing is built that is not specified with written acceptance criteria, and tests are written and confirmed failing before implementation. Spec-first is a requirement that the spec be *true* at handoff and at rest — not that every sentence was agreed before it was written; agreement lands at reconciliation.

## Working thesis

> Build production-grade software with AI agents by managing evidence, not implementation details. Release decisions should be based on documented intent, verification, review, and risk.

## Core operating rule

> Manage the proof, not the code.

Code matters, but trust comes from evidence that the change behaves as intended within known verification boundaries.

## Source of truth

Specifications are canonical. Everything downstream of them — acceptance
criteria, architecture summaries, tracker issues (currently GitHub Issues) — is
a derived artifact: a view onto the specs, never an independent source of truth.

If a derived artifact conflicts with a canonical one (an issue against the spec,
an architecture summary against the TRD), it is a **hard stop**.

## Responsibilities

### Chief of Staff

Assesses current state and proposes the next step: proposes tranches of agreed
spec for Dave's approval, and decomposes an approved tranche into ordered change
packages before any agentic work on it begins. It operates as a decision
session, not an execution session.

### Dave

Owns:

- product direction
- user value
- prioritization
- acceptance criteria
- risk tolerance
- release decisions
- operational learning
- decisions about whether evidence is sufficient

Does not default to:

- reading every implementation line
- acting as the primary code reviewer
- manually verifying every low-level design choice
- replacing missing evidence with intuition

The primary question for Dave is:

> Is the evidence sufficient to accept the risk?

### Agents

May:

- design solutions
- write specifications
- implement code
- create tests
- review changes
- identify risks
- update documentation

Must:

- state assumptions
- distinguish mocked, contract, live, browser, and production verification
- update relevant documentation when behavior changes
- escalate unclear product, risk, or release decisions

Must not:

- equate passing tests with shippability
- weaken verification to satisfy implementation
- claim live behavior from mocked evidence
- store durable policy only in vendor-specific tooling

The same underlying model may fill multiple roles, but two separations are
mandatory rather than optional:

- Whoever produces an artifact does not approve it.
- Whoever drafts a document does not act as the Spec Reviewer that gates it.

## Control surfaces

Primary controls are:

1. Specification
2. Test plan
3. Implementation evidence
4. Independent review
5. Verification boundaries
6. Operational readiness
7. Release judgment

## Change flow

For meaningful changes, work moves through these stages and roles. A meaningful
change is any change that warrants a change package — any change affecting
behavior, interfaces, tests, dependencies, boundaries, or documentation of
substance. Trivial changes — typo fixes, comment edits, mechanical formatting —
are not meaningful in this sense, and use a lighter shape. Each stage completes
before the next begins; no skipping or working ahead.

1. **Specs agreed** — PRD/TRD written, reviewed by the Spec Reviewer Agent (hard gate), and agreed by Dave. The same gate covers any canonical document, methodology documents included. *(PM/EM/Owner + Architect + Spec Reviewer)*
   While a tranche is executing, spec edits may land ungated on its spec branch and are gated together at reconciliation; the default branch never carries unreviewed spec text.
2. **Acceptance criteria** — explicit, written ACs for the unit of work. *(PM/EM/Owner)*
3. **Architecture summary** — per-change design derived from the TRD; the tracker issue is cut from this. *(Architect)*
4. **Test plan, confirmed red** — ACs translated into test code, run, and confirmed to fail before any implementation. *(Test Designer)*
5. **Implement to green** — minimum code to turn the failing tests green; mechanical checks (lint, types, static analysis) pass as part of "green." *(Coder — a different agent from the Test Designer for this unit)*
6. **Quality review** — judgment on maintainability, correctness, consistency, and test adequacy, over the diff and the mechanical results. *(Reviewer — hard gate)*
7. **Skeptic/risk review** — judgment on false confidence, mocked-boundary and live-integration gaps, config/deploy risk, and release overclaims, over the whole evidence chain. *(Skeptic/Risk)*
8. **Release package** — assemble evidence and a ship recommendation. *(Release Manager)*
9. **Release gate** — routine changes flow to release on evidence; the consequential class requires the human's explicit go/no-go at the release decision (see below). *(Dave)*

The red-gate at step 4 is mandatory. Quality review (6) and skeptic/risk review
(7) are deliberately separate — quality review asks "is this good?"; skeptic/risk
asks "where is this lying to us?" — and a change can pass one and fail the other.
Mechanical checks (lint/types/static analysis) are deterministic evidence folded
into "green," not a review step. Use a lighter process for routine changes, but
do not omit necessary evidence and do not skip the red-gate.

## Release gate

The human gate is the **release decision**, not a code decision and not the
commit (see "Source of truth"). A **two-tier** release gate governs exposing
changes to users:

- **Routine changes** flow to release on evidence, without an explicit human
  go/no-go.
- **Consequential changes** require the human's explicit go/no-go at the release
  decision. The consequential class is the list the commit and change control
  policy states. When unsure which tier applies, treat the change as
  consequential and ask.

*Deploy* (code on prod) and *release* (functionality exposed to users) may be
separate events; where the release decision sits relative to commit and deploy
is recorded in the project's TRD, not here.

When deploy and release are separated, the usual mechanism is **feature flags**
(or canaries). Depend on a **vendor-neutral flag interface** (e.g. OpenFeature)
so the flag backend stays a swappable per-project TRD choice rather than a
lock-in. The release gate attaches to the **exposure event**: flipping a flag
that exposes a consequential change *is* the gated release; adding a dark (off)
flag is routine. Every flag has an owner and a removal trigger, and stale flags
are tracked as debt and cleaned up.

## Change package

A meaningful change should produce a change package containing:

1. Intent / problem statement
2. Acceptance criteria
3. Test plan
4. Implementation summary
5. Test results — including the test commands run, any skipped tests, and a
   recommendation on whether the testing evidence is sufficient
6. Verification boundary updates
7. SLO status and error budget consumption for affected Top K user journeys
8. Review findings
9. Known gaps
10. Operational notes
11. `human-gate` tracker issue reference, if the change is consequential
12. Release recommendation

## Standard response shape

For substantial implementation, review, or release work, the reply states:

1. **Role**: what role you are filling.
2. **Intent**: what the change or review is trying to accomplish.
3. **Evidence**: what was checked.
4. **Boundary**: what the evidence does and does not prove.
5. **Gaps**: what remains unknown or deferred.
6. **Recommendation**: what should happen next.
7. **Dave decision points**: what requires human judgment.

This is the shape of the reply. It is not the change package, which is the
artifact the reply reports on.

## Definition of done

A change is not done merely because code was written or tests are green.

A change is done when:

- intended behavior is implemented
- the pre-written tests were confirmed failing, then turned green
- mechanical checks (lint, types, static analysis) pass
- relevant verification has run
- evidence is summarized
- verification boundaries are documented
- known gaps are explicit
- quality review and skeptic/risk review passes have occurred
- release readiness is clear
- the change cleared the appropriate gate at the release decision
- Dave has enough information to assess risk

## Escalation

Escalate when:

- requirements are ambiguous
- risk tolerance is unclear
- evidence is insufficient
- a product tradeoff exists
- security, privacy, or operational concerns arise
- reviewers disagree materially
- human code inspection is warranted
- the role for the current session has not been specified

When in doubt whether to escalate, escalate.

Do not escalate routine implementation decisions that can be resolved through existing guidance.

## Operating standard

Production-grade software is intentionally specified, verified to declared boundaries, operationally supportable, observable, recoverable, and honest about remaining uncertainty.
