---
status: in-review
last-reviewed: null
audience: [all-roles, human]
name: directive-dispatch
description: Hands work from a decision session to an execution session as a paste block the executor lands in git, with explicit route, model, and track. Use when work moves from chat to an execution session — including when a reviewer, skeptic, or risk role sends a fix, re-check, or remediation to Claude Code — and when writing a directive or the block that starts a session executing it.
---

# Skill: Directive Dispatch

## Purpose

Hand a unit of work from chat to an execution session without losing the
decisions that produced it.

A directive does two jobs, and they have different lifespans. **Transport** —
getting the instructions to the executor — expires the moment execution starts.
**Record** — what was decided and what it was executed against — is worth
nothing at dispatch and everything later. Only the record needs git, and the
executor, not chat, is the party for whom git is cheap.

So the directive travels as a **paste block**, and the executor's first act is
to land it: write it to `docs/cycles/`, commit it, read the SHA back, and report
*"executed `<path>`, landed as `<sha>`"*. The SHA is established **post-hoc**.
That is early enough — nothing consumes it before the report, and the report is
what the decision record cites. This holds for **every** directive class,
reviewer-gated cycle directives included.

What this leaves as the integrity question is not provenance but
**paste-arrival-intactness**: did the whole directive arrive? That is already
governed — a paste block is copied and pasted in its entirety (`LEXICON.md`) —
and a directive that arrives truncated fails its own self-containment test
before it fails anything else.

## Use when

Any time work moves from a triage/decision session to an execution session.

Reviewer-gated spec review cycles are governed by `skills/spec-review-cycle.md`
(one conversation per cycle, documents as uploads, reviewed SHAs recorded). The
rules here apply to that file too, without exception: a reviewer-gated cycle
directive states all four requirements per directive, like any other dispatch.
Route *fresh* and model *Opus 5* are the usual selection for that class — the
defaults `skills/spec-review-cycle.md` records (Cycle directive format), stated
per directive and overridable — not an exemption from stating them. Where both
documents state the same requirement, this is the general statement; reconciling
the rest of the duplication is open work.

## The four requirements

Every dispatch states all four, explicitly, every time. An unstated one is a
defect. A class may have a usual selection for a part; that is a default to
state, not a licence to omit it.

### 1. Route — fresh or existing context

State which, and why. A wrong route fails silently.

- **Fresh** — the default. The directive is self-contained; a fresh session
  cannot be contaminated by triage context the directive excluded.
- **Existing context** — only when the work depends on state the running
  session holds and the directive cannot carry.

### 2. Model — selected against quality and cost

State which model, and why. Table (v1, deliberately crude):

| Work | Model |
|---|---|
| Directive execution over canonical documents; spec authorship; review gates; anything where a wrong answer is expensive and hard to detect | Opus 5 |
| Implementation against a written spec with tests; routine review; well-bounded refactors | Sonnet 5 |
| Mechanical, verifiable work — reformatting, renaming, list extraction, checks with an obvious right answer | Haiku 4.5 |

### 3. Track — A or B

The track states the **executor's** repository environment. Delivery no longer
varies — every directive arrives as a paste block — so what the track decides is
how the directive becomes citable and what the report may claim.

**Track A** — the default. The executor has a working tree and a reachable
remote: it commits the directive, pushes, and reports the pushed SHA.

**Track B** — the executor has a working tree but **no reachable remote**: the
forge is down, no credential is present, or the machine is offline. It commits
the directive locally and reports that SHA. A SHA exists the moment `git commit`
runs; no remote is required, and pushing later does not change it. **Same-machine
only** — an unpushed commit resolves in that clone and nowhere else, so a Track B
SHA is citable only there until it is pushed, and the report says so.

**Track B is operator-invoked. The agent never infers it.** Default to A. An
executor that finds the remote unreachable under a Track A dispatch **stops and
surfaces it** rather than silently degrading to a local commit: the track is what
the report is measured against, and a report that quietly changes its own
standard is the failure this requirement exists to prevent.

### 4. Execution block — the directive itself

A dispatch is two paste blocks, in order.

1. A **sync block** bringing the executor's clone current from an explicitly
   named remote and ref; construct it per `skills/command-blocks.md`. **State it
   every time**, even when the clone should be current: a stale clone reporting
   missing work is evidence about the clone, not the repo. Where the work derives
   from an open spec delta, the ref is the spec branch, not the default branch
   (`context-sets/spec-and-change-discipline.md`). Track B has no sync block —
   there is no remote to fetch from — and the working-tree-current check happens
   in the executor's own clone instead.
2. The **directive**, as one paste block, opening with the instruction to land
   it before doing anything else:

```
Execution block: this directive travels as a paste block. Your first act —
before any other work — is to write it verbatim and in full to
docs/cycles/<name>.md, commit it, and record the SHA.
```

- **Companion documents already in git are cited, not pasted** — path and SHA
  each. One copy exists; a pasted copy will be the stale one. A directive that
  has already landed is re-dispatched the same way.
- **Do not establish the directive's own SHA before dispatch.** There is nothing
  to gate on it, and a chat-side commit reintroduces the transport this form
  removes.

## Writing the directive file

One self-contained directive per session: the executor needs the paste block and
the repository, nothing from the conversation.

- **Exclusive working trees for split directives.** Two sessions sharing a tree
  mutate each other's preconditions. Prefer not splitting; where unavoidable,
  state the tree assignment in each directive.
- **Pin STOP conditions to the reviewed ref**, not the head of the branch the
  directive lands on — the directive's own commit moves that head.
- **Mid-delta directives derive from the spec branch, not the default branch**,
  and pin its SHA: truth-at-handoff
  (`context-sets/spec-and-change-discipline.md`).
- **No blanket constraint may contradict an explicit instruction in the same
  file.** Read the constraint block against the instruction list before sending.
- **Scope Do-not lists to the blast radius.** Where a required consistency fix
  reaches outside it, name that file as explicitly permitted.
- **Carry dictated wording as a pointer** (`<path>@<sha>` plus field/section),
  never restated — unless the directive is itself the wording's origin, in which
  case it carries it inline and downstream artifacts point at it.

## Executor obligations

- **Land the directive first.** Before any other work, write it verbatim and in
  full to `docs/cycles/` per the naming schema, commit it, and **read the SHA
  back from git** — never report a SHA on the strength of a write call's return
  (`policies/remote-write-verification-policy.md`).
- **Concurrent tree mutation → stop and surface.** Files this session did not
  change moving, HEAD moving, an index lock: do not re-read and continue.
- **An instruction that cannot be executed as written → stop and surface.** No
  improvisation, no silent partial execution.
- **Report what was done, not what the directive said** — opening with
  *"executed `<path>`, landed as `<sha>`"*.

## Directive file naming schema — proposed

Two forms, both working with `bin/cycle-open`:

**Numbered** — reviewer-gated cycles over a document under review:

```
docs/cycles/cycle-<n>-directive.md
```

**Slugged and dated** — everything else:

```
docs/cycles/<slug>-<YYYY-MM-DD>-directive.md
```

Companion documents share the stem, change the suffix
(`<slug>-<YYYY-MM-DD>-questions.md`). The date is an identifier, not a derivable
fact — slugs recur across time; `doc-review-2026-08-02` does not.

Schema is a proposal (Q2 records none existed); the part of this draft most
likely to want revision.

## Status of this draft

Drafted 2026-08-02 per `docs/cycles/doc-review-2026-08-02-directive.md` (W3.4),
executing Q2. Extended 2026-08-05 (sync step, directive-authoring constraints,
executor obligations; AI-9 rule set). Conformed to `LEXICON.md` (draft)
2026-08-06. Track B mechanics rewritten 2026-08-07, compressed to directive
register, and extended the same day. Revised 2026-08-08 per
`docs/cycles/trivium-gate-cycle-1-directive.md` (D1, D2, D3, D9, D10, D11) and
again per `docs/cycles/trivium-gate-cycle-2-directive.md` (R1), which put the
cycle-directive class back under the all-four rule. Rewritten 2026-08-09 per
`docs/cycles/friction-refactor-2026-08-09-directive.md` (D1.1–D1.4): the
directive now travels as a paste block and is landed by the executor, with the
SHA reported post-hoc; the `~/Downloads` delivery mechanics, their pre-flight and
relocate/commit/echo blocks, and the two-consecutive-failure Track B on-ramp are
retired, the last of these relocated to
`policies/remote-write-verification-policy.md` (Rule 4), which is where the
transport failures it detects are governed; Track is redefined as the executor's
repository environment; and the deferred `bin/dispatch` section is dropped,
because the discipline it would have enforced was chat-side and no longer exists
(`BACKLOG-v2.md` records the retirement). Nothing here is agreed.
