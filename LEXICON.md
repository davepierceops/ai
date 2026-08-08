---
status: agreed
last-reviewed: reviews/LEXICON-cycle-2.md @ 5e1dc1fb78d4c4a670d5ec749971e7b766d5924f
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

**Directive** — the complete package handed to an execution session. Four
parts, all four stated every time: **route** (fresh session or existing
context), **model**, **track** (A or B), and the **execution block**.
*Bounded exception:* a reviewer-gated cycle directive states track and the
execution block, and takes route (fresh) and model (Opus 5) as fixed by its
class rather than restating them per directive
(`skills/spec-review-cycle.md`, Cycle directive format).

**Dispatch** — the act of handing a directive to an execution session.

**Track A / Track B** — the two paths a directive takes to become citable.
Track A commits the directive file through repository tooling and cites it by
SHA. Track B produces it in an artifact, and Dave commits it from a local clone
using command blocks. Track B is operator-invoked; agents never infer it
(`skills/directive-dispatch.md`).

**Execution block** — the instructions an LLM agent session is to carry out.
Deliberately silent on delivery: the primary form cites a committed directive
file by path and SHA; the fallback carries the instructions inline. Both are
execution blocks.
*Not:* shell commands. Those are command blocks.

**Directive file** — the committed markdown file holding the instructions,
cited by path and the SHA of the commit that landed it. One per intended
execution session; self-contained, meaning the executor needs the file and the
repository and nothing from the conversation that produced it.

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
explicitly named remote and ref. Precedes every **Track A** execution block in
a dispatch. Track B has no sync block: it is same-machine and commit-not-push,
so the executor already holds the commit and there is no remote to fetch from —
the sync step is carried by the echoed dispatch line instead
(`skills/directive-dispatch.md`, Track B mechanics).

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

A handoff into another *decision* session has no term yet. Naming it is open
work, tracked at `OPEN-ITEMS.md:800` ("A handoff into another decision session
has no name").

## Prompt

**Prompt** — text composed for a session to act on, generated at execution
time and not committed (`roles/chief-of-staff.md`, `.prompts/`).

*Not:* a directive. A directive file is committed and citable; a prompt is
regenerable and disposable. Where both exist for the same work, the directive
file is canonical.
