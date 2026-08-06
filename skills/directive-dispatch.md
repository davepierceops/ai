---
name: directive-dispatch
description: Hands work from a decision session to an execution session as a committed directive cited by path and SHA, with explicit route, model, and sync step. Use when work moves from chat to an execution session — including when a reviewer, skeptic, or risk role needs to send a fix, re-check, or remediation to Claude Code — and when writing a directive or the block that starts the session executing it.
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Skill: Directive Dispatch

## Purpose

Hand a unit of work from a chat session to an execution session without losing
the decisions that produced it.

The failure this prevents: work dispatched as a chat paste. The instructions
have no SHA, no commit, and no audit trail; the executing session cannot tell
which revision of the decisions it is executing; and nothing outlives the
conversation.

## Use when

Any time work moves from a triage/decision session to an execution session.

For reviewer-gated spec review cycles, `skills/spec-review-cycle.md` governs the
procedure — one conversation per cycle, documents as uploads, reviewed SHAs
recorded — and specifies the per-finding decision block a cycle directive
adds. The rules in this skill apply to that file as they do to any other. Where
the two documents state the same requirement, this one is the general statement;
`spec-review-cycle.md` states it again in cycle terms rather than deriving it,
and reconciling that duplication is open work.

## The four requirements

Every dispatch states all four. Explicitly, every time. An unstated one is a
defect, not a default.

### 1. Route — fresh instance or existing context

State which, and say why.

- **Fresh** — the default for directive execution. The directive is
  self-contained by construction, and a fresh session cannot be contaminated
  by triage-conversation context that the directive deliberately did not
  include. `skills/spec-review-cycle.md` makes this a hard constraint for
  review cycles ("One conversation per cycle").
- **Existing context** — only when the work genuinely depends on state the
  running session holds and the directive cannot carry.

The reason "explicit every time" matters: the wrong route fails *silently*.
An existing-context session executing a directive will quietly blend its prior
assumptions into the work, and nothing in the output announces it.

### 2. Model — selected against quality and cost

State which model, and why that one.

Hard-coded table, v1:

| Work | Model |
|---|---|
| Directive execution over canonical documents; spec authorship; review gates; anything where a wrong answer is expensive and hard to detect | Opus 5 |
| Implementation against a written spec with tests; routine review; well-bounded refactors | Sonnet 5 |
| Mechanical, verifiable work — reformatting, renaming, list extraction, checks with an obvious right answer | Haiku 4.5 |

This table is **deliberately crude**. It is a starting point that makes the
selection explicit and reviewable; it is not a claim about optimal routing.
When `bin/dispatch` is built the table moves into a config file it reads, so
"hard-coded for now" is one edit away from "configured" — but it stays a
stated choice per dispatch either way.

### 3. Track — A or B

**Track A** is the path: the directive file is committed through repository
tooling, and the execution block cites it by path and SHA.

**Track B** is the no-repository-tooling path, for sessions that cannot reach
the repo — private repos without a credentialed connector, degraded tooling, or
a client where the connector is absent. Mechanics below.

**Track B is operator-invoked.** The agent **never infers** it. Track is about
the operator's environment — which repo, which client, what already holds a
connection — and an agent has no access to those facts. Default to A; use B only
when Dave names it.

**The one exception: the agent may propose Track B after two consecutive
qualifying tooling failures.** This is evidence the agent directly observed,
not a guess about the environment.

Qualifying: write timeouts; writes that return success but cannot be confirmed
on read-back; and transport-level errors (5xx, connection reset, a connector
absent mid-session).

Not qualifying: auth and permission errors — Track B still needs credentials to
push, so switching hides the problem one step further on; not-found errors,
which are almost always a wrong path or ref; and any failure caused by the
agent's own malformed call.

That last exclusion covers a case worth naming, because it does not look like an
agent defect at first glance: **a write that lands successfully but commits
wrong content.** The response is truthful and the commit is real — the request
was wrong. This has happened: a call carrying a placeholder string as its
content parameter replaced a ~64KB tracker on the default branch with 19 bytes,
and landing-verification alone would have confirmed the destroyed file as a
successful commit (see `policies/remote-write-verification-policy.md`).
Repository tooling was working perfectly throughout. Switching tracks over it
would carry the defect to a new path and lose the tooling that caught it.

The exclusion matters most as a class: without it, "tooling is flaky" becomes an
available excuse for the agent's own defects.

Counting: a write that times out but is confirmed landed on read-back is not a
failure — the response was lost, not the work — and resets the count. A write
that times out and is confirmed *not* landed is one. A read-back that itself
times out is the second, and is the worst case, because state is now unknown.
Any successful write resets the count.

Separately and immediately: a read-back that times out means **stop and
establish state** before doing anything else. That fires at the first failure
and is not a track question. Do not let the track proposal delay it.

The proposal is one line asking, not a drafted Track B directive. If Dave
declines, the agent does not raise it again on the same evidence — only after a
new qualifying failure occurs.

### 4. Execution block — instructions, normally cited by path and SHA

The primary form cites a **committed and pushed** directive file, as a path plus
the SHA of the commit that landed it.

The rules, in order:

1. Write the directive file to `docs/cycles/` (naming below).
2. Commit it. Push it.
3. **Read the SHA back from git.** Never invent it, never abbreviate a SHA
   used as a pointer, and never quote a SHA from a write call's return value
   without verifying it landed — see
   `policies/remote-write-verification-policy.md`.
4. Only then emit the dispatch block.

Dispatch block form — a sync command block, then the execution block:

```
<sync block>

Read and execute <relative/path/to/directive-file.md> @ <sha>.
```

Plus any companion documents the directive requires the executor to read
first, each with its own path and SHA.

The sync step is stated every time, including when the executing clone should
already be current. A stale clone reporting that the work is not there is
evidence about the clone, not about the repository, and the symptom does not
announce which one it is. Construct the sync block per
`skills/command-blocks.md`.

**Do not paste the directive file's contents alongside the citation.** The point
of the citation is that exactly one copy exists and it is the one in git. A
pasted copy is a second copy, and it will be the stale one.

**The inline fallback, and what it costs.** Where the file cannot be committed —
tooling unavailable, no remote — the execution block carries the instructions
inline. This is a fallback, not an equal option: inline instructions have no
SHA, no commit, and no audit trail, which is the failure this skill opens by
naming. State when it is taken and why, and commit the file as soon as the
obstruction clears.

## Track B mechanics

The ordering inverts. Under Track A the file is committed through repository
tooling, then cited. Under Track B the file is agreed before any commit exists.

1. Draft the directive file in an artifact. Dave reviews it there.
2. Emit a sync command block. Dave runs it against the local clone.
3. Dave downloads the artifact into the clone.
4. Emit a command block that commits the file **and echoes the dispatch line
   with the SHA already interpolated**.
5. Dave pastes that output into the execution session.

Command blocks at steps 2 and 4 are governed by `skills/command-blocks.md`,
including the rule that they are sent one per turn, since Dave relays output
between them.

**Commit, not push.** A SHA exists the moment `git commit` runs — no remote
required. This is what makes Track B a real break-glass path: it works when the
forge is unreachable, not merely when a connector is missing. Push whenever the
remote returns; the SHA does not change.

The step-4 block ends with something of this shape:

```
git commit -q -m "<message>" -- <path> && \
  echo "sync, then read and execute <path> @ $(git rev-parse HEAD)"
```

**Keep the echoed line plain**: one line, no markdown, no backticks, double
quotes only. The content barely varies — a path known at authoring time and one
`git rev-parse` — so the only thing that breaks these blocks is quoting. A block
needing hand-repair before it runs has already failed the command-block rule
that it runs verbatim as given.

**Track B assumes a same-machine execution session.** An unpushed commit
resolves in that clone and nowhere else.

**What Track B costs, stated rather than discovered.** Verification moves to
Dave. Track A ends with the agent fetching the file back and comparing; Track B
ends when Dave reports what the block printed. The agent must not report a
Track B write as verified — only what Dave reported.

**Routing, for Dave not the agent.** Work needing git *history* — blast-radius
checks, `git log -S`, resolving a `last-reviewed` SHA, staleness guards — does
not fit Track B, because a downloaded snapshot carries files without history.
Drafting and reasoning over current file contents fit it well. If a session
needs history, it is Track A.

## Writing the directive file

One self-contained directive file per intended session. Self-contained means
the executor needs the file and the repository, and nothing from the
conversation that produced it.

**Exclusive working trees for split directive files.** Two sessions sharing a
tree mutate each other's preconditions mid-execution, and neither one's STOP
conditions still mean what they said at authoring time. Prefer not splitting;
where unavoidable, state the tree assignment in each directive.

**Pin STOP conditions to the reviewed ref** — the commit the decision was made
against. Never to the head of the branch the directive lands on: the
file's own commit moves that head, so the executor stops on arrival every
time.

**No blanket constraint may contradict an explicit instruction in the same
file.** Read the constraint block against the instruction list before
committing. The executor is correct to stop, and the cost is a wasted session.

**Scope Do-not lists to the blast radius.** A list scoped wider will sometimes
forbid touching a file holding a stale instance of a value the change requires
updating, forcing the executor to choose which rule to break. Where a required
consistency fix reaches outside the radius, name that file as explicitly
permitted.

**Carry dictated wording as a pointer** — `<path>@<sha>` plus field or section
— never restated. A pointer either resolves or it does not; a restatement can
be subtly wrong and look correct. Where the directive is itself the origin
of the wording, it carries it inline and *is* the source, and downstream
artifacts point at the directive.

## Executor obligations

Stated here because the authoring rules above are written against them.

**Concurrent tree mutation → stop.** Files changing that this session did not
change, HEAD moving, an index lock appearing: stop and surface it. Do not
re-read and continue — every precondition was checked against a tree that no
longer exists.

**An instruction that cannot be executed as written → stop and surface it.** No
improvisation, no silent partial execution.

**Report what was done, not what the directive said.** The directive is intent;
the report is evidence.

## Directive file naming schema — proposed

Two forms. Both already work with `bin/cycle-open`.

**Numbered**, for reviewer-gated cycles over a document under review, where
the cycle number is the meaningful identifier and cycles are inherently
ordered:

```
docs/cycles/cycle-<n>-directive.md
```

**Slugged and dated**, for everything else — a slug naming the work plus the
ISO date it was issued:

```
docs/cycles/<slug>-<YYYY-MM-DD>-directive.md
```

Companion documents share the stem and change the suffix:

```
docs/cycles/<slug>-<YYYY-MM-DD>-questions.md
```

Both forms are already in use: the numbered form throughout the metadata
policy cycles, and the slugged-and-dated form for
`doc-review-2026-08-02-directive.md` and its `-questions.md` companion.

Rationale for the date: slugs collide across time. `doc-review` will recur;
`doc-review-2026-08-02` will not. The date is in the *filename*, not in
metadata, precisely because it is an identifier here rather than a derivable
fact about the file — git's timestamp records when the file was committed,
which is a different thing from which dispatch this directive belongs to.

**This schema is a proposal.** Q2 records that no schema existed; this is the
first attempt at one, and it is the part of this draft most likely to want
revision.

## `bin/dispatch` — deferred, and why that is acceptable

The intended end state, per the F4 lesson that discipline belongs in tooling:
a `bin/dispatch` that takes a directive file, **refuses to emit the dispatch
block until it is committed and pushed**, and stamps the git-read SHA
into it — making the discipline impossible to skip rather than merely written
down.

It is deferred to `BACKLOG-v2.md`. The reasoning: seven cycles have run
without a slip on this discipline, so the failure mode is theoretical for now,
and the skill can be exercised manually while that remains true.

Track B's step-4 block is the same idea done in shell, and it is deliberately
not the tool yet — Track B has never been run, so building against it now means
building against a design with no use behind it. **Two triggers to build:**
Track B has been exercised enough to know what the block actually needs, or the
first time the block requires a hand-tweak before it runs.

**The honest caveat:** "no slips yet" is evidence about the past under
consistent attention, and this entire document exists because chat-history
discipline decays. If a dispatch ever ships with an uncommitted or
wrong-SHA directive, that is the signal the deferral has expired — and it
should be treated as expiry, not as a one-off to correct and move past.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.4) executing Q2.
Extended 2026-08-05 with the sync step, the directive-authoring
constraints, and the executor obligations, migrating the AI-9 rule set.
Conformed to `LEXICON.md` (draft) 2026-08-06. Nothing here is agreed.
