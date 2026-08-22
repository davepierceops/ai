---
status: draft
last-reviewed: null
audience: [all-roles, human]
order: 4
depends-on: []
---

# Context Set: Spec and Change Discipline

This context set governs both session kinds: decision sessions and execution
sessions. It carries the spec-first, test-driven spine — the *order* work
happens in — and the habits agents hold to.

## Core philosophy

Development is **spec-first** and **test-driven**. Nothing is built that is not
specified: the spec and its acceptance criteria exist, and are correct, at the
moment work is handed to an executor. Tests are written before implementation.
Implementation exists only to make pre-written tests pass.

**Spec-first is a truth requirement, not an approval sequence.** The rule is that
the spec is true **at handoff** and true **at rest** — not that every sentence
an executor reads was agreed before it was written. Agreement is a separate
event, and it lands at **reconciliation** (below). What generates the truth
requirement is the amnesiac executor: a session holds nothing but the documents
it is given, so those documents must be right at handoff.

> Specifications are the source of truth, and human judgment gates the
> decisions that are actually judgment.

Those decisions are spec agreement and the release decision for the
consequential class. Everything between them is the routine class: agents
execute it, review it, and merge it autonomously once the evidence exists. The
gate anchors at the release decision, not at landing.

## The red-gate

**A true red-gate is behavioral, not a missing-module red.** A test that fails
only because the module under test doesn't exist yet (`Cannot find package
'@/lib/services/x'`) proves nothing about whether the test's assertions are
correct — a wrong assertion fails the same way as a right one. This defeats
the purpose of Test Designer / Coder separation: both agents can share the same
blind spot, and the shared blind spot survives to green. For any package where
that separation matters (anything beyond trivial fixes), the Test Designer must
have enough of the interface contract, from the architecture summary, to write
tests that run against a stub or an interface with deliberately wrong behavior,
so the red-gate demonstrates the tests can actually fail on bad logic — not just
on an absent import.

Spec and test discipline governs steps 1 through 5 of the change flow. The flow
continues through quality review, skeptic/risk review, release package, and
release gate — steps 6 through 9.

## Open spec delta

**The licence is the owner's, not the room's.** Agents propose spec edits
exactly as before, and an agent that edits a spec document without being told to
has not found a loophole here — what an open delta removes is the *gate* on the
owner's own edits, not the rule about who authors canonical text.

**Reconciliation blocks the next tranche's decomposition.** Decomposing from
unreviewed spec is prohibited. Dave may invoke reconciliation early,
mid-tranche, at will — frequent small reconciliations are the encouraged norm,
and the tranche boundary is a deadline rather than a target.

**A directive issued mid-delta derives from the spec branch.** It cites the spec
branch and pins its SHA, not the default branch: truth-at-handoff. Provenance
survives — the SHA resolves, and what the executor read is recoverable.

**Concurrency is achieved by disjoint territory, never by merging.** At most two
tranches execute concurrently — never two deltas over one tranche — and they are
chosen so that their spec territory does not overlap. The convergent-edit case —
two deltas editing one document and merging the result — is **refused, not
tooled**: a merge of two ungated spec edits is exactly the unreviewed text on the
default branch that this design exists to prevent. Where a project has no
disjoint territory to claim, the second tranche goes cross-project, or the work
goes serial.

## Operating habits

- **Proactive loose-end tracking.** The loose-end tracker `OPEN-ITEMS.md` is
  updated at defined checkpoints, rather than relying on Dave to remember:
  - **End of a work session** — flush current open items before context is lost.
  - **Before a release gate** — all open items must be accounted for: resolved,
    deferred with rationale, or accepted risk.
  - **Before a spec is agreed** — Spec Reviewer continuity scan findings land
    here if not immediately resolved.
  - **On demand** — Dave asks; agent produces current state immediately and
    updates the file.

  Surface items from the tracker when they become relevant to the work at hand.
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
  other write path does.
