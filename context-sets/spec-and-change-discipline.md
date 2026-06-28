---
context-set: spec-and-change-discipline
purpose: Spec-first sequencing, the red-gate, and day-to-day operating habits.
include-when: Any chat that produces specs, tests, implementation, or commits.
depends-on: [base]
status: draft v0.1
---

# Context Set: Spec and Change Discipline

Status: draft

This context set carries the spec-first, test-driven spine and the operating
habits that govern day-to-day work. It complements `base.md` (evidence model)
and `ai-native-engineering.md` (roles) by defining the *order* work happens in
and the *habits* agents hold to.

## Core philosophy

Development is **spec-first** and **test-driven**. Nothing is built until it has
been specified and its acceptance criteria are written. Tests are written before
implementation. Implementation exists only to make pre-written tests pass.

> Specifications are the source of truth, and a human verifies every
> consequential step before it lands.

## The canonical sequence

Each stage completes before the next begins. No skipping, no working ahead.

1. **PRD / TRD agreed.** Product and technical specs are written, reviewed by
   the Spec Reviewer (hard gate), and agreed by Dave (`specs/`). Specs are
   canonical; Issues are derived (`policies/source-of-truth-policy.md`).
2. **Acceptance criteria written.** Each unit of work has explicit, written ACs.
3. **Architecture summary.** The Architect derives a per-change architecture
   summary from the TRD. This is what a GitHub Issue is cut from.
4. **Tests written as code.** The Test Designer translates ACs into test code.
5. **Confirm all tests fail (red-gate).** Run the tests and verify they fail
   before any implementation. A test that passes before implementation is a
   broken test, not a head start.
6. **TDD to green.** The Coder implements only as much as needed to turn the
   failing tests green, with mechanical checks (lint, types, static analysis)
   passing as part of "green." (Test Designer and Coder are separate agents for
   the same unit of work.)

No implementation begins until specs and ACs for that work are complete.

Steps 1–6 above govern the spec and test discipline. The full change flow
continues through quality review, skeptic/risk review, release package, and
release gate. See `operating-model.md` for steps 7–9.

## Definition of done (spec discipline view)

A change is done when: intended behavior is implemented; the pre-written tests
were confirmed red, then green; evidence is summarized; verification boundaries
are documented; known gaps are explicit; quality review and skeptic/risk review
passes have occurred; and the change cleared the appropriate gate at the release
decision
(`policies/commit-and-change-control-policy.md`). Green tests alone are not
"done."

## Operating habits

- **Claude drafts, Dave verifies.** Agents propose; Dave disposes. Drafts of
  specs, fixes, and decisions are produced for Dave's review.
- **One question at a time.** When something needs Dave's input, ask a single
  question and wait, rather than batching several decisions into one message.
- **No assumptions on consequential calls.** When a decision is Dave's, frame
  the tradeoffs clearly and ask. Do not decide on Dave's behalf.
- **Frame tradeoffs crisply.** Present clear options with their tradeoffs; Dave
  makes calls quickly once the tradeoffs are clear. Prefer crisp framing over
  over-qualified hedging.
- **Proactive loose-end tracking.** Track open items, deferred decisions, and
  outstanding fixes in `OPEN-ITEMS.md` rather than relying on Dave to
  remember them. This file is updated at defined checkpoints:
  - **End of a work session** — flush current open items before context is lost.
  - **Before a release gate** — all open items must be accounted for: resolved,
    deferred with rationale, or accepted risk.
  - **Before a spec is agreed** — Spec Reviewer continuity scan findings land
    here if not immediately resolved.
  - **On demand** — Dave asks; agent produces current state immediately and
    updates the file.
  Surface items from `OPEN-ITEMS.md` when they become relevant to the work
  at hand.
- **Document consistency.** When editing a document, find *every* instance of a
  changed value across the whole document and update all of them before
  finishing. A value updated in one place but stale in another is a defect.
