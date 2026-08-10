---
status: draft
last-reviewed: null
audience: [all-roles, human]
context-set: spec-and-change-discipline
purpose: Spec-first sequencing, the red-gate, and day-to-day operating habits.
include-when: Any chat that produces specs, tests, implementation, or commits.
depends-on: [base]
---

# Context Set: Spec and Change Discipline

This context set carries the spec-first, test-driven spine and the operating
habits that govern day-to-day work. It complements `base.md` (evidence model)
and `ai-native-engineering.md` (roles) by defining the *order* work happens in
and the *habits* agents hold to.

## Core philosophy

Development is **spec-first** and **test-driven**. Nothing is built that is not
specified: the spec and its acceptance criteria exist, and are correct, at the
moment work is handed to an executor. Tests are written before implementation.
Implementation exists only to make pre-written tests pass.

**Spec-first is a truth requirement, not an approval sequence.** The rule is that
the spec is true **at dispatch** and true **at rest** — not that every sentence
an executor reads was agreed before it was written. Agreement is a separate
event, and it lands at **reconciliation** (below). What generates the
truth requirement is the amnesiac executor: a session holds nothing but the
documents it is given, so those documents must be right at handoff. That the spec
must also have been pre-approved does not follow — it is a different property,
and the two were conflated for no gain and at the cost of an operator gate per
edit.

> Specifications are the source of truth, and human judgment gates the
> decisions that are actually judgment.

Those decisions are spec agreement and the release decision for the
consequential class. Everything between them is the routine class: agents
execute it, review it, and merge it autonomously once the evidence exists. The
gate anchors at the release decision, not at landing — see
`policies/commit-and-change-control-policy.md` for the two tiers and what
membership in the consequential class means.

## The canonical sequence

Each stage completes before the next begins. No skipping, no working ahead.

1. **PRD / TRD current, and agreed at rest.** Product and technical specs are
   written, reviewed by the Spec Reviewer (hard gate), and agreed by Dave
   (`specs/`) — that state holds on the default branch between deltas. Work
   derives from the **version of record**: the default branch when no delta is
   open, the tranche's spec branch while one is. Specs are canonical; Issues are
   derived (`policies/source-of-truth-policy.md`).
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

**A true red-gate is behavioral, not a missing-module red.** A test that fails
only because the module under test doesn't exist yet (`Cannot find package
'@/lib/services/x'`) proves nothing about whether the test's assertions are
correct — a wrong assertion fails the same way as a right one. This defeats
the purpose of Test/Coder separation: both agents can share the same blind
spot, and the shared blind spot survives to green. For any package where
Test/Coder separation matters (anything beyond trivial fixes), the Test
Designer must have enough of the interface contract (from the architecture
summary, step 3) to write tests that run against a stub or an interface with
deliberately wrong behavior, so the red-gate demonstrates the tests can
actually fail on bad logic — not just on an absent import. (Confirmed by Dave,
2026-07-24, closing the P3 contact-merge review: a real gap — region going
stale during merge — survived both implementation and a same-branch
independent test pass, because that pass ran second against already-green
code rather than as a true pre-implementation red-gate.)

Steps 1–6 above govern the spec and test discipline. The full change flow
continues through quality review, skeptic/risk review, release package, and
release gate. See `operating-model.md` for steps 7–9.

## Open spec delta

A tranche does not survive contact with implementation unchanged. Decisions get
made while building, by the person with the hot context, and the spec has to
absorb them. Gating each of those edits on a review cycle spends the operator's
attention at the rate the work generates questions, which is the wrong rate.

**The branch is the state.** During a tranche's execution, **Dave** edits spec
documents freely on a dedicated branch, `spec/<tranche-slug>`, with no reviewer
gate and no per-edit ceremony; commits land as he makes them. This interval is an
**open spec delta**. There is no new status value and no register — the branch
existing, with commits on it, is the whole of the machinery.

The licence is his, not the room's. Agents propose spec edits exactly as before,
and an agent that edits a spec document without being told to has not found a
loophole here — what an open delta removes is the *gate* on the owner's own
edits, not the rule about who authors canonical text
(`roles/spec-reviewer-agent.md`; `context-sets/collab-workflow.md`).

**Reconciliation closes the delta.** The spec is brought to full agreement with
what was actually built, and the accumulated diff goes through the reviewer gate
**once — once per delta, not once per edit** — arriving on the default branch as
a pull request (`skills/spec-review-cycle.md`, Reconciliation). The default
branch therefore never carries unreviewed spec text, and `agreed` there never
lies.

**A delta is bounded by its tranche and never spans two.** Reconciliation blocks
the next tranche's decomposition: decomposing from unreviewed spec is prohibited,
because a decomposition is a derived artifact and deriving one from text nobody
has gated propagates an ungated decision into every package under it. Dave may
invoke reconciliation early, mid-tranche, at will — frequent small
reconciliations are the encouraged norm, and the tranche boundary is a deadline
rather than a target.

**Mid-delta dispatches derive from the spec branch.** A directive issued while a
delta is open cites the spec branch and pins its SHA, not the default branch:
truth-at-handoff. Provenance survives — the SHA resolves, and what the executor
read is recoverable (`skills/directive-dispatch.md`).

**Concurrency is achieved by disjoint territory, never by merging.** At most two
tranches execute concurrently — never two deltas over one tranche — and they are
chosen so that their spec territory does not overlap. (The word for a concurrent
workstream is *tranche*, not *track*: `track` is fixed to the executor's
repository environment, `LEXICON.md`.) A spec document is **claimed** by
appearing in an open delta's diff, and a claimed document may not be claimed by a
second delta. The convergent-edit case — two deltas editing one document and
merging the result — is **refused, not tooled**: a merge of two ungated spec
edits is exactly the unreviewed text on the default branch that this design
exists to prevent. Where a project has no disjoint territory to claim, the second
tranche goes cross-project, or the work goes serial.

## Definition of done (spec discipline view)

A change is done when: intended behavior is implemented; the pre-written tests
were confirmed red, then green; evidence is summarized; verification boundaries
are documented; known gaps are explicit; quality review and skeptic/risk review
passes have occurred; and the change cleared the appropriate gate at the release
decision
(`policies/commit-and-change-control-policy.md`). Green tests alone are not
"done."

## Operating habits

- **Ask what a mechanism costs Dave in the loop.** Operator attention is this
  system's scarcest resource and the only one that does not parallelize: agents
  scale, review cycles scale, evidence scales, and he does not. So every proposed
  gate, check, confirmation, or ceremony is measured by how much of it it spends,
  and evidence integrity may not be bought by spending it as though it were free.
  This is a design test applied to mechanisms, not a licence to skip a gate that
  passes it — the gates that remain are the ones worth his attention, which is
  precisely why they must not be crowded by ones that are not.
- **Agents dispose of routine changes; Dave disposes of judgment calls.**
  Agents draft, review, and merge the routine class on evidence, without
  asking. What returns to Dave is the release decision for the consequential
  class and the agreement of any canonical document — specs and methodology
  documents alike. Drafts are produced for his agreement, not for his
  line-by-line verification (`boundaries/human-review-boundary.md`).
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
- **Derived/side-effect fields checklist.** Any change that writes an entity's
  primary fields (create, edit, merge, import) must also account for that
  entity's *derived* fields — values computed from primary fields rather than
  supplied directly (e.g. `region` derived from `mailingAddress`). Both the
  Coder and an independent Test Designer can share a blind spot around a
  derived field if neither treats it as part of the field set under test —
  it isn't "content" the way the primary fields are, so it's easy to omit from
  both the implementation and the test plan. Before calling a write-path
  package done, explicitly enumerate: what derived fields exist on this
  entity, and does this change's write path maintain them the same way every
  other write path does. (Added 2026-07-24, closing the P3 contact-merge
  review — F1: merge blank-filled `mailingAddress` but never re-derived
  `region`, and this survived both implementation and an independent test
  pass.)
