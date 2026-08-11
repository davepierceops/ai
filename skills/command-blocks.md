---
status: agreed
last-reviewed: reviews/expedited-log.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3
audience: [all-roles, human]
name: command-blocks
description: Constrains fenced shell-command blocks handed to a human or agent to run as given — copyable as rendered, verbatim, captured output, explicit remotes, safe to re-run. Use when emitting a shell block, command, or command sequence for someone or something else to run, including the sync block preceding an execution block.
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

*Evidence* here is scoped: output that is cited later or that leaves the session
— a test run, a verification, anything a report will rest on. Output consumed
in-the-moment by the person running the block, and never referred to again, is
not evidence in this sense and needs no capture. A listing someone reads to
decide what to do next is the standard case — an `ls` before choosing which file
to act on, a `git status` before choosing whether to proceed. Where a document
emits such a block, it says so where the block is defined, so that a reviewer
running down these criteria is not left to guess whether the exemption was
claimed or forgotten.

**A sync or remote command names its remote and ref, and fails loudly.** State
both rather than leaning on branch-upstream configuration or an implied default:
a block runs in a clone whose config the author cannot see, and a `git pull`
resolved through the wrong upstream is silent about it. `origin` is a remote
*name*, not a protocol — it is a valid explicit remote and using it is fine.
What the rule is guarding is the other half: a bad sync fails loudly (non-zero
exit), so nothing downstream may act on the tree the sync produced without that
exit status having been checked. An unverified sync followed by unconditional
work is how a stale tree gets reported as current.

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

**A block pasted into an interactive shell must not terminate it.** The rule is
stated by effect: no construct that can end the shell the block runs in — on
most terminals closing its window. Guard preconditions by branching
(`if…elif…else…fi`) so a failed check prints and the block ends without ending
the session.

*Known instances, not the rule:* `exit`, `exec`, `logout`, `|| { …; exit; }`,
and `set -e` — which ends an interactive shell on the next failing command
exactly as `exit` does, while being the idiomatic opening line of a careful
multi-command block. The list is open; adopting projects should add the
constructs their own shells terminate on.

## Conformance criteria

Every command block satisfies all seven. An untested block is still a command
block, and still non-conformant.

- Every command is valid and non-harmful.
- Every command runs safely as given, with no manual step inside the fence.
- The whole is safe to re-run: re-running does not compound damage. (*Safe to
  re-run*, not *idempotent* — a block containing a commit, an issue creation,
  or an append to a log cannot be idempotent, and demanding it would make the
  rule unfollowable.)
- Any command producing evidence captures its output to a named path, where
  *evidence* is output cited later or leaving the session.
- The block renders with its delivery surface's copy control intact.
- The block cannot terminate the shell it is pasted into — no construct with
  that effect. Known instances: `exit`, `exec`, `logout`, `|| { …; exit; }`,
  `set -e`. Preconditions fall through via `if…elif…else…fi`.
- Every sync or remote command names its remote and ref, and its exit status is
  checked before anything downstream acts on the result.

New criteria are appended rather than slotted into body order. Other documents
cite these by ordinal rather than restating them — which is what keeps a rule
like criterion 6 in one place instead of drifting across two
(`decisions/log.md` `DEC-000100`) — so the existing numbering has to hold.
