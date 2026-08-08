---
name: command-blocks
description: Constrains fenced shell-command blocks handed to a human or agent to run as given — copyable as rendered, verbatim, captured output, explicit remotes, safe to re-run. Use when emitting a shell block, command, or command sequence for someone or something else to run, including the sync block preceding an execution block.
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Skill: Command Blocks

A command block is a paste block whose content is shell commands intended to run
as given. It is not an execution block — that term is reserved for instructions
to an LLM agent (`LEXICON.md`). Command blocks are emitted in many contexts that
involve no directive at all.

**A block runs verbatim as pasted.** No manual steps inside a fence. A fence is
a paste contract, and a manual step inside one breaks it silently: it is either
skipped as a comment or it halts the block partway with no signal about which
half ran. Manual steps go in prose outside the fence, or into the directive file
if there is one.

**Blocks producing evidence capture output to a named file** (`tee` or
equivalent), and the block or its surrounding instruction names the path.
Output that only reaches the terminal scrolls and is gone. If the output is not
worth capturing, it was not evidence.

**Name remotes explicitly; do not rely on the `origin` alias.** `origin`'s
protocol is environment state, and when the environment cannot authenticate it,
the failure surfaces as a downstream symptom — missing work, empty results —
rather than as an auth error.

**The block must be copyable in the surface that delivers it.** A block the
reader cannot copy whole is not a paste block at all — it fails the definition
(`LEXICON.md`) before any rule below applies. This failure is invisible from the
author's side: the text is well-formed, every command is valid, and the problem
appears only in rendering, which the author does not see. So avoid constructs
known to break the surface in use.

*Known instance, not the rule:* heredocs (`<<'EOF'`) suppress the copy control
in the Claude desktop client. Prefer repeated `-m` flags for multi-paragraph
commit messages. Surfaces differ — adopting projects should substitute their own
known cases and keep the principle.

**Send one block per turn when a human must relay output between blocks.** Wait
for the output, then compose the next. A second block written before the first
has run is written against a guess at its output — batching does not merely
inconvenience the relay, it commits to an untested assumption and hides that it
did so. This binds blocks handed to a human intermediary; it does not bind a
sequence an agent runs itself with no one in the loop.

**A block pasted into an interactive shell must not terminate it.** `exit`,
`exec`, `logout`, and `|| { …; exit; }` end the shell the block runs in — on most
terminals closing its window. Guard preconditions by branching
(`if…elif…else…fi`) so a failed check prints and the block ends without ending
the session.

## Conformance criteria

Every command block satisfies all six. An untested block is still a command
block, and still non-conformant.

- Every command is valid and non-harmful.
- Every command runs safely as given, with no manual step inside the fence.
- The whole is safe to re-run: re-running does not compound damage. (*Safe to
  re-run*, not *idempotent* — a block containing a commit, an issue creation,
  or an append to a log cannot be idempotent, and demanding it would make the
  rule unfollowable.)
- Any command producing evidence captures its output to a named path.
- The block renders with its delivery surface's copy control intact.
- The block cannot terminate the shell it is pasted into: no `exit`, `exec`, or
  `logout`, and no `|| { …; exit; }` guard. Preconditions fall through via
  `if…elif…else…fi`.
