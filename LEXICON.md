---
status: agreed
last-reviewed: reviews/expedited-log.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3
audience: [all-roles, human]
---

# Lexicon

Terms with a fixed meaning across this methodology. Where a term has drifted,
the `Not:` line records what it does not mean.

Governed like any canonical document: changes enter through a review cycle.

**Adoption scope.** This lexicon states what terms mean going forward. It does
not describe the current tree, and conforming the tree is not a precondition
for using these definitions in new work.

**The touch rule:** any file edited for another reason is conformed to this
lexicon as part of that edit. Conformity spreads with the work rather than as
a migration. Files nobody has reason to touch keep their older usages
indefinitely, and that is the intended outcome, not a defect.

These definitions were chosen to match existing usage wherever it was already
consistent, so the debt across the tree is small. `directive` and `execute`
keep the senses the corpus already gave them. The terms that genuinely needed
fixing are `handoff`, which carried six senses, and the block distinctions
below.

## The three layers

Work moves through three layers, and the words below are assigned by layer.
Keeping them separate is the whole point of this section.

1. **Decision** — happens in chat.
2. **Execution** — happens in an LLM agent session (currently Claude Code).
3. **Shell** — commands run in a `bash`-type shell.

`execute` and `execution` belong to layer 2, always. This matches every
existing use in the repo: `roles/chief-of-staff.md` uses "execution" for layer-2
Claude Code work ("execution belongs to Claude Code"), and
`skills/spec-review-cycle.md` names Claude Code the execution layer. **Never**
use `execute` or `execution` for layer 3. Shell work is done by *command
blocks*, and that term is reserved for it.

## Sessions

**Decision session** — triages, decides, and produces the artifacts that direct
and record work: directives, session records, tracker updates. It reads freely
and writes these artifacts, but it does not carry out the changes a directive
specifies.

**Execution session** — an LLM agent session carrying out a directive against a
working tree.

Nothing here authorizes acting against a deployed or production system. Whether
an agent may do so at all, and under what gate, is
`policies/commit-and-change-control-policy.md`'s question, not this file's.

The boundary is role in the flow, not capability. A decision session may hold a
clone and may commit; what makes it a decision session is that the work the
directive specifies happens elsewhere.

## Dispatch

**Directive** — the complete package handed to an execution session. Three
parts, all three stated every time: **route** (fresh session or existing
context), **model**, and the **execution block**. No class is exempt from stating
a part. A class may have defaults: a reviewer-gated cycle directive defaults to
route *fresh* and model *Opus 5*, states them like any other dispatch, and may
override them (`skills/spec-review-cycle.md`, Cycle directive format).

**Dispatch** — the act of handing a directive to an execution session.

**Track** — not a term of this methodology. It named a directive-delivery path,
then the executor's repository environment (A: reachable remote; B: none), and
both senses are retired. Nothing about the executor's environment is stated in a
directive; the one case the term still covered — the remote is unreachable — is
an executor obligation instead: an executor that cannot push **stops and
surfaces it** (`skills/directive-dispatch.md`, Executor obligations). For a
concurrent workstream the word is *tranche*
(`context-sets/spec-and-change-discipline.md`).

**Execution block** — the instructions an LLM agent session is to carry out.
Delivered as a paste block carrying the directive itself; where the directive
already exists in git, the block cites it by path and SHA instead. Both are
execution blocks.
*Not:* shell commands. Those are command blocks.

**Directive file** — the markdown file holding the instructions, written and
committed by the **executor** as its first act, and thereafter cited by path and
the SHA of the commit that landed it. One per intended execution session;
self-contained, meaning the executor needs the paste block and the repository
and nothing from the conversation that produced it.

**Instruction** — one direction within a directive file. Individually
executable, and individually refusable: an instruction that cannot be executed
as written stops the session.

**Companion document** — a committed file a directive requires the executor to
read before acting. Cited with its own path and SHA.

## Blocks

**Paste block** — a fenced block intended to be copied in its entirety and
pasted in its entirety somewhere else. The general form; execution blocks and
command blocks are both delivered as paste blocks.

**Command block** — a paste block whose content is shell commands intended to
run as given. Governed by `skills/command-blocks.md`.
*Not:* instructions to an LLM. Those are execution blocks. Never described as
executing or being executed.

**Sync block** — the command block that brings a clone current from an
explicitly named remote and ref. Precedes every execution block in a dispatch,
full stop (`skills/directive-dispatch.md`, §3 Execution block).

## Spec state

**Spec branch** — the branch a tranche's spec edits land on, named
`spec/<tranche-slug>`. Git is the machinery; there is no status value for this
and no register recording it. The branch existing, with commits on it, is the
state.

**Open spec delta** — the interval during which a tranche's spec branch carries
edits that the default branch does not. During it Dave edits spec documents
freely, with no reviewer gate and no per-edit ceremony. A delta is bounded by
its tranche and never spans two.

**Reconciliation** — closing a delta: the spec is brought to full agreement with
what was actually built, and the whole accumulated diff goes through the reviewer
gate **once** — once per delta, not once per edit — arriving on the default
branch as a pull request. Agreement attaches here, to the version of record,
which is why
`agreed` on the default branch never lies
(`context-sets/spec-and-change-discipline.md`, `skills/spec-review-cycle.md`).

**Claimed** — of a spec document: appearing in an open delta's diff. A claimed
document may not be claimed by a second open delta. Concurrency comes from
claiming disjoint territory, never from merging convergent edits.

## Handoff

**Handoff** — transfer of unfinished responsibility between sessions or roles,
and the set of things that must travel with it for the receiver to continue.

*Not:* a directive. *Not:* a paste block or any block. A dispatch is one
mechanism by which a handoff is carried out; calling the mechanism the handoff
loses the distinction between the transfer and the artifact.

Established uses consistent with this: the end-of-session flush of open items
(`context-sets/collab-workflow.md`), what a coder agent includes when passing
work on (`roles/coder-agent.md`), debt a change package deliberately did not
touch and passes forward (`docs/packages/package-c-change-package.md`).

**Baton** — the artifact a decision session hands its successor decision
session: the composed package of unfinished responsibility — state, open
questions, decisions in flight — that lets the receiver continue without the
conversation that produced it. **A baton passes between decision sessions; a
directive dispatches work to an execution session. The two never blur.**

*Not:* a directive, and *not:* a dispatch. A baton is what a
decision-to-decision handoff carries, in the sense the entry above gives
"handoff" — one artifact class within it, named because that particular transfer
had no name and kept borrowing one.

## Retired terms

**Prompt** — not a term of this methodology. What is meant is one of:

- **What a decision session hands an execution session** — a *directive*; its
  committed form is a *directive file*, its transport is an *execution block*,
  and one direction inside it is an *instruction*.
- **What a decision session hands its successor decision session** — a *baton*.
- **What a directive points the executor at** — a *companion document*.
- **What runs in a shell** — a *command block*; the one that opens a dispatch
  is a *sync block*.
- **What a session loads as standing context** — a *context set*, a *role
  document*, a *skill document*, a *policy*, a *boundary document*.
- **What a session derives work from** — the *decomposition doc*, a *change
  package*, the *acceptance criteria*, the *spec* (PRD/TRD).
- **Inbound material a session acts on** — the specific name of that material:
  *reviewer findings*, a *review artifact*, an *execution report*, an *upload*,
  a *retro*.

The colloquial sense — any text sent to an LLM — is too broad to do work here.

*Not covered by this retirement:* an approval **prompt**, meaning a tool
interrupting to ask a human to authorise a step
(`vendors/claude-code/environment-config.md`). That is a different word in a
different domain, and it keeps its ordinary meaning.

**Track** — see the tombstone under Dispatch.
