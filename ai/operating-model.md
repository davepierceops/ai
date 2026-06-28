# Operating Model

Status: draft

## Summary

This project is built by an AI-native software team.

Dave acts as PM, EM, owner, and operator. Agents perform implementation, testing, review, analysis, and documentation work.

Dave does not rely on routine line-by-line code review. The primary control is evidence: specifications, tests, reviews, verification boundaries, operational signals, and known gaps.

Work is **spec-first** and **test-driven**: nothing is built until it is specified with written acceptance criteria, and tests are written and confirmed failing before implementation. See `context-sets/spec-and-change-discipline.md`.

## Working thesis

> Build production-grade software with AI agents by managing evidence, not implementation details. Release decisions should be based on documented intent, verification, review, and risk.

## Core operating rule

> Manage the proof, not the code.

Code matters, but trust comes from evidence that the change behaves as intended within known verification boundaries.

## Trust model

Agent output is useful but not self-validating.

Claims require supporting evidence.

Examples:

- Feature behavior requires acceptance evidence.
- Integration behavior requires live or deploy-like evidence.
- Test coverage claims must state what is and is not verified.
- Release recommendations must include known gaps.
- Mock-based verification must declare its boundaries.

## Source of truth

Specifications are canonical. The order is: **PRD** (product) → **TRD**
(technical) → acceptance criteria → per-change architecture summary → **GitHub
Issues**. Issues are derived PM artifacts — a view onto the specs, never an
independent source of truth.

If a derived artifact conflicts with a canonical one (an Issue against the spec,
an architecture summary against the TRD), it is a **hard stop**: surface the
conflict, name both sides, and wait for Dave. Do not resolve by guessing or by
preferring the more recent artifact. See `policies/source-of-truth-policy.md`.

## Responsibilities

### Dave

Owns:

- product intent
- prioritization
- acceptance criteria
- risk tolerance
- agreeing the PRD and TRD (after Spec Reviewer sign-off)
- release decisions
- operational learning

May inspect code when needed, but code review is not the default quality gate.

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
- stay within scope
- provide evidence for claims
- distinguish mocked, contract, live, browser, and production verification
- identify unverified areas
- update relevant documentation when behavior changes
- escalate unclear product, risk, or release decisions

Must not:

- equate passing tests with shippability
- weaken verification to satisfy implementation
- hide uncertainty
- expand scope without approval
- claim live behavior from mocked evidence
- store durable policy only in vendor-specific tooling

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
substance (see `context-sets/base.md`). Each stage
completes before the next begins; no skipping or working ahead.

1. **Specs agreed** — PRD/TRD written, reviewed by the Spec Reviewer Agent (hard gate), and agreed by Dave. *(PM/EM/Owner + Architect + Spec Reviewer)*
2. **Acceptance criteria** — explicit, written ACs for the unit of work. *(PM/EM/Owner)*
3. **Architecture summary** — per-change design derived from the TRD; the Issue is cut from this. *(Architect)*
4. **Test plan, confirmed red** — ACs translated into test code, run, and confirmed to fail before any implementation. *(Test Designer)*
5. **Implement to green** — minimum code to turn the failing tests green; mechanical checks (lint, types, static analysis) pass as part of "green." *(Coder — a different agent from the Test Designer for this unit)*
6. **Quality review** — judgment on maintainability, correctness, consistency, and test adequacy, over the diff and the mechanical results. *(Reviewer)*
7. **Skeptic/risk review** — judgment on false confidence, mocked-boundary and live-integration gaps, config/deploy risk, and release overclaims, over the whole evidence chain. *(Skeptic/Risk)*
8. **Release package** — assemble evidence and a ship recommendation. *(Release Manager)*
9. **Release gate** — routine changes flow to release on evidence; the consequential class requires the human's explicit go/no-go at the release decision (see below). *(Dave)*

The red-gate at step 4 is mandatory: a test that passes before implementation is
a broken test, not a head start. Quality review (6) and skeptic/risk review (7)
are deliberately separate — quality review asks "is this good?"; skeptic/risk
asks "where is this lying to us?" — and a change can pass one and fail the other.
Mechanical checks (lint/types/static analysis) are deterministic evidence folded
into "green," not a review step. Use a lighter process for low-risk changes, but
do not omit necessary evidence and do not skip the red-gate.

## Release gate

The human gate is the **release decision**, not a code decision and not the
commit (see "Source of truth" and README #5). A **two-tier** release gate governs
exposing changes to users (see
`policies/commit-and-change-control-policy.md`):

- **Routine changes** flow to release on evidence, without an explicit human
  go/no-go.
- **Consequential changes** require the human's explicit go/no-go at the release
  decision. The consequential class is anything touching auth, schema/migrations,
  security or privacy, irreversible operations, public-facing surfaces, a
  verification boundary, or core architecture (the standing TRD). When unsure
  which tier applies, treat the change as consequential and ask.

*Deploy* (code on prod) and *release* (functionality exposed to users) may be
separate events; where the release decision sits relative to commit and deploy
is recorded in the project's TRD, not here.

When deploy and release are separated, the usual mechanism is **feature flags**
(or canaries). Depend on a **vendor-neutral flag interface** (e.g. OpenFeature)
so the flag backend stays a swappable per-project TRD choice rather than a
lock-in — the same provider-independence logic as the vendor-tooling boundary.
The release gate attaches to the **exposure event**: flipping a flag that exposes
a consequential change *is* the gated release; adding a dark (off) flag is
routine. Every flag has an owner and a removal trigger, and stale flags are
tracked as debt and cleaned up — this is the main cost the mechanism introduces.

## Change package

A meaningful change should produce a change package containing:

1. Intent / problem statement
2. Acceptance criteria
3. Test plan
4. Implementation summary
5. Test results
6. Verification boundary updates
7. SLO status and error budget consumption for affected Top K user journeys
8. Review findings
9. Known gaps
10. Operational notes
11. `human-gate` GitHub issue reference, if the change is consequential
12. Release recommendation

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

Do not escalate routine implementation decisions that can be resolved through existing guidance.

## Relationship to tools

The `/ai/` directory is the source of truth for project operating guidance.

Tool-specific files may adapt these rules but should not be the sole location of durable policy.

## Operating standard

Production-grade software is intentionally specified, verified to declared boundaries, operationally supportable, observable, recoverable, and honest about remaining uncertainty.

