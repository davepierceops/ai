---
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

For reviewer-gated spec review cycles specifically, `skills/spec-review-cycle.md`
governs — it is the more specific procedure and it already carries these
requirements. This skill is the general case.

## The three requirements

Every dispatch states all three. Explicitly, every time. An unstated one is a
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

### 3. Artifact — a committed directive, cited by path and SHA

The directive is a markdown file, **committed and pushed**, dispatched as a
path plus the SHA of the commit that landed it.

The rules, in order:

1. Write the directive to `docs/cycles/` (naming below).
2. Commit it. Push it.
3. **Read the SHA back from git.** Never invent it, never abbreviate a SHA
   used as a pointer, and never quote a SHA from a write call's return value
   without verifying it landed — see
   `vendors/claude-code/mcp-write-verification.md`.
4. Only then emit the paste block.

Paste block form:

```
Read and execute <relative/path/to/directive.md> @ <sha>.
```

Plus any companion documents the directive requires the executor to read
first, each with its own path and SHA.

**Do not paste the directive's contents into the dispatch.** The point of the
citation is that exactly one copy exists and it is the one in git. A pasted
copy is a second copy, and it will be the stale one.

## Directive naming schema — proposed

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
a `bin/dispatch` that takes a directive file, **refuses to emit the paste
block until the file is committed and pushed**, and stamps the git-read SHA
into the block — making the discipline impossible to skip rather than merely
written down.

It is deferred to `BACKLOG-v2.md`. The reasoning: seven cycles have run
without a slip on this discipline, so the failure mode is theoretical for now,
and the skill can be exercised manually while that remains true.

**The honest caveat:** "no slips yet" is evidence about the past under
consistent attention, and this entire document exists because chat-history
discipline decays. If a dispatch ever ships with an uncommitted or
wrong-SHA directive, that is the signal the deferral has expired — and it
should be treated as expiry, not as a one-off to correct and move past.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.4) executing Q2.
Nothing here is agreed.
