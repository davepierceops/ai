---
status: agreed
last-reviewed: reviews/directive-dispatch-cycle-2.md @ 5e1dc1fb78d4c4a670d5ec749971e7b766d5924f
audience: [all-roles, human]
name: directive-dispatch
description: Hands work from a decision session to an execution session as a committed directive cited by path and SHA, with explicit route, model, and track. Use when work moves from chat to an execution session — including when a reviewer, skeptic, or risk role sends a fix, re-check, or remediation to Claude Code — and when writing a directive or the block that starts a session executing it.
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
rules here apply to that file too, with one bounded exception: a reviewer-gated
cycle directive states its **track** and its execution block per directive, and
takes **route** and **model** as fixed by its class — route *fresh*, model
*Opus 5* — stated once in `skills/spec-review-cycle.md` (Cycle directive format)
rather than restated on every cycle. Where both documents state the same
requirement, this is the general statement; reconciling the rest of the
duplication is open work.

## The four requirements

Every dispatch states all four, explicitly, every time. An unstated one is a
defect — except where a class fixes a part in advance and says so, which today
is the reviewer-gated cycle directive above.

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
credentialed connector, degraded tooling, an absent connector, or contention
between concurrent sessions competing for the same transport. Mechanics below.

**Track B is operator-invoked. The agent never infers it.** Default to A; use B
only when Dave names it.

**Exception: the agent may propose Track B after two consecutive qualifying
tooling failures** — evidence it directly observed. The trigger is kept as much
for what it detects as for the track it opens: a two-failure fire is how
contention between concurrent sessions gets noticed at all, and that diagnostic
value holds whatever the underlying cause turns out to be (`decisions/log.md`
`DEC-000080`).

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
  In Track A that step is a sync command block preceding the execution block;
  construct it per `skills/command-blocks.md`. Track B carries the step
  differently — see Track B mechanics.
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

**Invariant: the canonical file is the only `directive-dispatch`-style match in
`~/Downloads` that the relocate block will move.** The relocate block moves an
*exact* filename, so stray siblings do not corrupt a commit — but a stale copy
of the *canonical* name from a prior session would. The pre-flight surfaces
what is there; Dave judges. It is not a machine "count equals one" check.

1. Draft the file in an artifact. Title the artifact with the exact filename it
   should download as. **Present that exact artifact in the same reply as the
   pre-flight/relocate blocks** — the pane holds whatever was shown last, and
   blocks that reference "the file" while a different file is displayed are a
   silent wrong-file hazard. Artifact and blocks ship together or not at all.
2. **Pre-flight** — emit a command block listing every download that shares the
   stem. Glob on the **stem**, not the full filename: the collision suffix lands
   *before* the extension (`directive-dispatch (1).md`), so a glob anchored after
   `.md` misses the copies. `<stem>` is the canonical filename without its
   extension.

   ```
   ls ~/Downloads/<stem>*
   ```

   Dave runs it and downloads the artifact (either order), then reads the
   listing. A single canonical file → proceed. Collision copies (`<stem> (1).md`)
   or a stale canonical file present → Dave clears what should not be there
   (`rm ~/Downloads/<stem>*` clears all of them) and re-downloads. The listing is
   for Dave's eye; he judges what belongs, because a stem glob also catches
   legitimately-different files that share the stem. The listing is deliberately
   *not* captured to a file: it is consumed in-the-moment and never cited again,
   which is the exempt case in `skills/command-blocks.md`'s evidence rule.
3. **Relocate, commit, echo** — one block. `<canonical-name>` is `<stem>` with
   its extension; the relocate moves the exact filename, so no glob here. The
   echo has **two forms** — use the one that fits:
   - *Dispatch* (the commit is a directive a fresh session will execute next):
     `echo "sync, then read and execute <dest-path> @ $(git rev-parse HEAD)"`
   - *Plain commit* (nothing to execute — a doc, a tracker, an inbox entry):
     `echo "committed <dest-path> @ $(git rev-parse HEAD)"`

   ```
   if [ ! -f ~/Downloads/<canonical-name> ]; then
     echo "STOP: ~/Downloads/<canonical-name> not found — run the pre-flight ls, then re-download."
   else
     mv -f ~/Downloads/<canonical-name> <dest-path> && \
     git add -- <dest-path> && \
     { git diff --cached --quiet -- <dest-path> || git commit -q -m "<message>" -- <dest-path>; } && \
     echo "<echo form per above>"
   fi
   ```

   For a dispatch, Dave pastes the echoed line into the execution session.

- **Both blocks emit in the same turn.** The one-per-turn relay rule does not
  bind: the relocate block reads the same whatever the pre-flight prints. Dave
  reads the pre-flight, not the next block.
- **The relocate block never inspects the destination.** It works for a new path
  or an edit to an existing file alike. The source-existence check is the only
  guard: a missing source (forgotten pre-flight) prints STOP and runs no git
  command.
- **Guards fall through; they never terminate the shell.** These blocks are
  pasted into an interactive shell. Preconditions branch with `if…else…fi`, so a
  failed check prints and ends the block without ending the session. The rule and
  the constructs it covers live in `skills/command-blocks.md`, criterion 6.
- **Run from the clone root.** `<dest-path>` in the relocate and append blocks is
  repo-relative, and neither block states nor checks the working directory, so
  the prose that ships with them carries the assumption: Dave pastes them into a
  shell already sitting in the correct clone. A structural guard would need the
  *expected* clone path, which the block does not carry generically, and a bare
  "am I in a repo" check would pass in the wrong clone — the case that actually
  bites.
- **Safe to re-run.** A second run finds the source gone and stops at the guard —
  correct, since an empty `~/Downloads` cannot distinguish "already committed"
  from "never downloaded." `git diff --cached --quiet` makes the commit a no-op
  when nothing changed.
- **Commit, not push.** A SHA exists the moment `git commit` runs; no remote
  required. Push whenever the remote returns — the SHA does not change.
- **Keep the echoed line plain:** one line, no markdown, no backticks, double
  quotes only. A block needing hand-repair has failed the command-block rule.
- **Same-machine only.** An unpushed commit resolves in that clone and nowhere
  else.
- **Sync is carried by the echoed line, not by a sync block, and it is not a
  remote fetch.** The tracks differ here because Track B is same-machine and
  commit-not-push (above): the execution session runs in the clone that already
  holds the unpushed commit, so a Track A fetch has no remote to fetch the
  directive from and could check out a tree that does not contain it. What the
  word `sync` asks for on that line is a working-tree-current check *in that same
  clone* — HEAD at the echoed SHA, no uncommitted edits to the files in scope.
  `LEXICON.md` scopes the sync block to Track A for this reason.
- **Verification moves to Dave.** The agent must not report a Track B write as
  verified — only what Dave reported.
- **Routing:** work needing git *history* (blast-radius, `git log -S`, resolving
  a `last-reviewed` SHA, staleness guards) is Track A — a downloaded snapshot
  carries no history. Drafting over current file contents fits Track B.
- **Emit the canonical filename as its own paste block** — nothing else on the
  line — for operator-assembled inspection steps (`ls`, `rm`, `cp`). A sharp
  operator assembles the verb around the name faster than reading a supplied
  block, but only if the name is copyable as an atom; bare inline text forces a
  hand-select, which is the friction the atom removes. Reserve whole tested
  blocks for load-bearing steps (relocate/commit).
- **Append vs. replace.** The relocate block *replaces* a file (`mv`). Appending
  to an existing tracker (an inbox, a log) is a different operation: naive
  `cat >>` run twice appends twice. Guard it with the entry's own marker (e.g. a
  dated heading) — skip the append if the marker is already in the target — and
  `rm` the source after, since `cat >>` leaves it in place where `mv` would not:

  ```
  if [ ! -f ~/Downloads/<canonical-name> ]; then
    echo "STOP: ~/Downloads/<canonical-name> not found — re-download, then re-run."
  elif grep -qF "<marker>" <dest-path>; then
    echo "SKIP: <marker> already present — not appending again."
  else
    cat ~/Downloads/<canonical-name> >> <dest-path> && \
    rm -f ~/Downloads/<canonical-name> && \
    git add -- <dest-path> && \
    git commit -q -m "<message>" -- <dest-path> && \
    echo "committed <dest-path> @ $(git rev-parse HEAD)"
  fi
  ```

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
it — discipline made unskippable. Deferred to `BACKLOG-v2.md`: the skill can be
run manually. What ends the deferral is stated below — the two build triggers,
and the expiry condition.

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
standalone sync block dropped). Compressed to directive register, and Track B mechanics extended (same-turn
artifact rule, stem glob, name-as-atom, append-vs-replace, two echo forms)
2026-08-07. Revised 2026-08-08 per `docs/cycles/trivium-gate-cycle-1-directive.md`
(D1, D2, D3, D9, D10, D11): Track B sync semantics, the shell-termination rule
reduced to a pointer, the cycle-directive bounded exception, the `bin/dispatch`
count dropped, the clone-root assumption stated, and the two-failure trigger's
keep-reason cited. Nothing here is agreed.
