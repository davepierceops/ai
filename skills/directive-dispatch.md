---
name: directive-dispatch
description: Hands work from a decision session to an execution session as a committed directive cited by path and SHA, with explicit route, model, and track. Use when work moves from chat to an execution session — including when a reviewer, skeptic, or risk role sends a fix, re-check, or remediation to Claude Code — and when writing a directive or the block that starts a session executing it.
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Skill: Directive Dispatch

## Purpose

Hand a unit of work from chat to an execution session without losing the
decisions that produced it. A chat-paste dispatch has no SHA, no commit, and no
audit trail, and nothing outlives the conversation.

## Use when

Any time work moves from a triage/decision session to an execution session.

Reviewer-gated spec review cycles are governed by `skills/spec-review-cycle.md`
(one conversation per cycle, documents as uploads, reviewed SHAs recorded). The
rules here apply to that file too. Where both state the same requirement, this
is the general statement; reconciling the duplication is open work.

## The four requirements

Every dispatch states all four, explicitly, every time. An unstated one is a
defect.

### 1. Route — fresh or existing context

State which, and why. A wrong route fails silently.

- **Fresh** — the default. The directive is self-contained; a fresh session
  cannot be contaminated by triage context the directive excluded.
- **Existing context** — only when the work depends on state the running
  session holds and the directive cannot carry.

### 2. Model — selected against quality and cost

State which model, and why. Table (v1, deliberately crude; moves to a
`bin/dispatch` config when that ships):

| Work | Model |
|---|---|
| Directive execution over canonical documents; spec authorship; review gates; anything where a wrong answer is expensive and hard to detect | Opus 5 |
| Implementation against a written spec with tests; routine review; well-bounded refactors | Sonnet 5 |
| Mechanical, verifiable work — reformatting, renaming, list extraction, checks with an obvious right answer | Haiku 4.5 |

### 3. Track — A or B

**Track A** — the default. The directive file is committed through repository
tooling; the execution block cites it by path and SHA.

**Track B** — the no-repository-tooling path: private repos without a
credentialed connector, degraded tooling, or an absent connector. Mechanics
below.

**Track B is operator-invoked. The agent never infers it.** Default to A; use B
only when Dave names it.

**Exception: the agent may propose Track B after two consecutive qualifying
tooling failures** — evidence it directly observed.

- **Qualifying:** write timeouts; writes returning success but unconfirmable on
  read-back; transport errors (5xx, connection reset, connector absent
  mid-session).
- **Not qualifying:** auth/permission errors (Track B still needs credentials);
  not-found errors (almost always a wrong path or ref); any failure from the
  agent's own malformed call — including a write that lands but commits wrong
  content (see `policies/remote-write-verification-policy.md`).

**Counting.** Timed-out-but-confirmed-landed is not a failure; it resets the
count. Timed-out-and-confirmed-not-landed is one. A read-back that itself times
out is the second, and means state is unknown.

**A read-back that times out → stop and establish state immediately.** Fires at
the first failure; not a track question; do not let the track proposal delay it.

The proposal is one line. If Dave declines, do not raise it again without a new
qualifying failure.

### 4. Execution block — cited by path and SHA

The primary form cites a **committed and pushed** directive file by path and the
SHA of the commit that landed it. In order:

1. Write the directive file to `docs/cycles/` (naming below).
2. Commit and push it.
3. **Read the SHA back from git.** Never invent it, never abbreviate a pointer
   SHA, never quote a SHA from a write call's return without verifying it landed
   (`policies/remote-write-verification-policy.md`).
4. Emit the dispatch block:

```
<sync block>

Read and execute <relative/path/to/directive-file.md> @ <sha>.
```

Plus any companion documents, each with its own path and SHA.

- **State the sync step every time**, even when the clone should be current: a
  stale clone reporting missing work is evidence about the clone, not the repo.
  Construct it per `skills/command-blocks.md`.
- **Do not paste the directive's contents alongside the citation.** One copy
  exists, in git. A pasted copy will be the stale one.
- **Inline fallback:** where the file cannot be committed (no tooling, no
  remote), the block carries instructions inline. This is a fallback, not an
  equal option — no SHA, no commit, no audit trail. State when and why it is
  taken; commit as soon as the obstruction clears.

## Track B mechanics

Ordering inverts: the file is agreed before any commit exists. Track B delivers
the file as an artifact Dave downloads into the clone. The desktop client writes
to `~/Downloads` and appends a collision suffix (`name (1).md`) when a file of
that name is already there.

**Invariant: exactly one matching file in `~/Downloads`.** The pre-flight
establishes it; the relocate block trusts it and does not re-derive it.

1. Draft the file in an artifact. Title the artifact with the exact filename it
   should download as.
2. **Pre-flight** — emit a command block listing the download target:

   ```
   ls ~/Downloads/<canonical-name>*
   ```

   Dave runs it and downloads the artifact (either order). Nothing before
   download → clean. Exactly one → proceed. More than one → Dave clears
   (`rm ~/Downloads/<canonical-name>*`) and re-downloads. The `*` catches the
   ` (n)` suffix.
3. **Relocate, commit, echo** — one block:

   ```
   test -f ~/Downloads/<canonical-name> || { echo "STOP: ~/Downloads/<canonical-name> not found — run the pre-flight ls, then re-download." >&2; exit 1; }
   mv -f ~/Downloads/<canonical-name> <dest-path> && \
     git add -- <dest-path> && \
     { git diff --cached --quiet -- <dest-path> || git commit -q -m "<message>" -- <dest-path>; } && \
     echo "sync, then read and execute <dest-path> @ $(git rev-parse HEAD)"
   ```

   Dave pastes the echoed line into the execution session.

- **Both blocks emit in the same turn.** The one-per-turn relay rule does not
  bind: the relocate block reads the same whatever the pre-flight prints. Dave
  reads the pre-flight, not the next block.
- **The relocate block never inspects the destination.** It works for a new path
  or an edit to an existing file alike. The `test -f` on the *source* is the only
  guard: a missing source (forgotten pre-flight) is a hard stop before any git
  command runs.
- **Safe to re-run.** A second run finds the source gone and halts on `test -f` —
  correct, since an empty `~/Downloads` cannot distinguish "already committed"
  from "never downloaded." `git diff --cached --quiet` makes the commit a no-op
  when nothing changed.
- **Commit, not push.** A SHA exists the moment `git commit` runs; no remote
  required. Push whenever the remote returns — the SHA does not change.
- **Keep the echoed line plain:** one line, no markdown, no backticks, double
  quotes only. A block needing hand-repair has failed the command-block rule.
- **Same-machine only.** An unpushed commit resolves in that clone and nowhere
  else.
- **Verification moves to Dave.** The agent must not report a Track B write as
  verified — only what Dave reported.
- **Routing:** work needing git *history* (blast-radius, `git log -S`, resolving
  a `last-reviewed` SHA, staleness guards) is Track A — a downloaded snapshot
  carries no history. Drafting over current file contents fits Track B.

## Writing the directive file

One self-contained directive file per session: the executor needs the file and
the repository, nothing from the conversation.

- **Exclusive working trees for split directives.** Two sessions sharing a tree
  mutate each other's preconditions. Prefer not splitting; where unavoidable,
  state the tree assignment in each directive.
- **Pin STOP conditions to the reviewed ref**, not the head of the branch the
  directive lands on — the file's own commit moves that head.
- **No blanket constraint may contradict an explicit instruction in the same
  file.** Read the constraint block against the instruction list before
  committing.
- **Scope Do-not lists to the blast radius.** Where a required consistency fix
  reaches outside it, name that file as explicitly permitted.
- **Carry dictated wording as a pointer** (`<path>@<sha>` plus field/section),
  never restated — unless the directive is itself the wording's origin, in which
  case it carries it inline and downstream artifacts point at it.

## Executor obligations

- **Concurrent tree mutation → stop and surface.** Files this session did not
  change moving, HEAD moving, an index lock: do not re-read and continue.
- **An instruction that cannot be executed as written → stop and surface.** No
  improvisation, no silent partial execution.
- **Report what was done, not what the directive said.**

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

## `bin/dispatch` — deferred

Intended end state: a `bin/dispatch` that refuses to emit the dispatch block
until the directive is committed and pushed, and stamps the git-read SHA into
it — discipline made unskippable. Deferred to `BACKLOG-v2.md`: seven cycles have
run without a slip, so the failure mode is theoretical and the skill can be run
manually.

Track B's relocate/commit/echo block is the same idea in shell. Track B has now
been run once (2026-08-07), which reshaped the block. **Two triggers to build:**
the block stabilises across enough runs to encode without churning, or it first
requires a hand-tweak before it runs. If a dispatch ever ships with an
uncommitted or wrong-SHA directive, the deferral has expired.

## Status of this draft

Drafted 2026-08-02 per `docs/cycles/doc-review-2026-08-02-directive.md` (W3.4),
executing Q2. Extended 2026-08-05 (sync step, directive-authoring constraints,
executor obligations; AI-9 rule set). Conformed to `LEXICON.md` (draft)
2026-08-06. Track B mechanics rewritten 2026-08-07 (pre-flight for the
`~/Downloads` collision-suffix problem; destination-blind relocate block;
standalone sync block dropped). Compressed to directive register 2026-08-07.
Nothing here is agreed.
