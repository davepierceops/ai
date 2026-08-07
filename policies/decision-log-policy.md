---
status: agreed
last-reviewed: reviews/expedited-log.md @ 01fb1030e06dffa555ff6482eeda9a90f9e2b461
audience: [all-roles, human]
---

# Policy: Decision Log

## Purpose

So a decision made once can be found and honored — not silently re-litigated or
contradicted because no one knew it existed.

The log is the one place a decision resolves to; the consult obligation is what
makes it get read.

## The log

Each project keeps one append-only log at `decisions/log.md`. The methodology
repo (`davepierceops/ai`) keeps its own, for methodology decisions.

One file, not one file per entry — the single file *is* the index. Entries are
appended; existing entries are never edited or deleted.

## Entry format

```markdown
## DEC-000070 — <short title>
Date: <YYYY-MM-DD>
Decision: <the ruling, one or two sentences>
Context: <the problem it settled, briefly>
Supersedes: DEC-000030   (omit if none)
```

- **ID** — `DEC-NNNNNN`, assigned in steps of 10 starting at `DEC-000010`,
  unique within the project's log, never reused. It is the resolvable handle:
  `grep DEC-000070 decisions/log.md` lands on the entry. A cited decision with no
  defined path back to its definition is the defect this log removes.
- **Context** carries the *why* so a reader can consult the decision without
  reopening the cycle chat it came from.
- Decisions are Dave's; a "who" field would be noise, so there is none.

**Assigning an ID.** Read the log — you are opening it to append anyway — take
the last entry's number, add ten. Append-only guarantees the last entry holds
the highest ID, so last-plus-ten is always the next free number.

**Resolving a duplicate ID.** If two entries ever land on the same number
(concurrent appends), renumber the later ones by +1 *within the gap* —
`DEC-000410` → `DEC-000411`, `DEC-000412` — never by another ten. Ordering is
preserved, and a stale reference to the old number still resolves within a row
or two in an ordered log. The step of ten exists for exactly this: there is
always room to bump a collision without disturbing its neighbours.

## Reversal and supersession

A decision is never edited in place. To change or reverse one, append a new
entry whose `Supersedes:` names the old ID. The old entry stays as the
historical record. Whether a decision is still live is answered by searching its
ID in later `Supersedes:` lines. (If that reverse lookup ever gets tedious, a
`Superseded-by:` back-reference is the obvious addition — not built now.)

## Consult obligation

The log is inert without the obligation to read it. This line is added to
`context-sets/base.md` required behavior:

> - consult the project's decision log (`decisions/log.md`) before recommending
>   or encoding anything an existing decision may govern, and cite the governing
>   entry by ID

That obligation is the half that closes the C1a misses: in each, the relevant
decision existed but was never looked up.
