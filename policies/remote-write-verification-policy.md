---
status: in-review
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Remote Write Verification

## The failure mode

A write through a tool-mediated transport can **succeed on the server and fail
to report success to the caller**. A timeout, a dropped response, a tool error
returned after the mutation already landed — in each case the agent's local view
says "failed" while the remote says "committed."

Two bad outcomes follow, and they are opposites:

- **Reporting a commit landed when it did not.** The agent says the work is
  pushed; the SHA does not exist; downstream steps cite a revision that was
  never written.
- **Retrying a write that already succeeded.** The agent re-sends and produces
  a duplicate commit, a duplicate file, or a conflict against its own
  successful write.

This discipline was learned across three sessions and lived only in chat
history — the memory-dependence anti-pattern the methodology names elsewhere.
It is written down here so it stops depending on anyone remembering it.

## The rules

### 1. Fetch back before reporting a commit landed

Never report a commit as landed on the strength of the write call's return
value. **Read it back** and confirm the SHA exists with the expected content.

The write call's return value is a claim about the write. The fetch-back is
evidence. This is `context-sets/base.md`'s evidence rule applied to the
transport: an unverified claim from a tool is still an unverified claim.

### 2. Read HEAD before retrying a timed-out write

A timed-out or errored write is **unknown**, not **failed**. Before retrying,
read the current HEAD and determine whether the write actually landed.

Retry only if HEAD shows it did not. Never retry blind.

### 3. `git log` is the source of record

Where a local clone exists, `git log` against the fetched remote is the
authority on what landed — not the tool's response, and not the agent's
recollection of what it sent.

State SHAs read from git. Never invent one.

Whether a pointer SHA may be abbreviated is not this policy's question — Rule 3
is about provenance. `skills/directive-dispatch.md` carries the narrow rule
where it applies, for dispatch blocks.

### 4. Two consecutive qualifying failures is a fact about the environment

A single transport failure is noise. **Two in a row is a signal** — the tooling
is degraded, or two concurrent sessions are contending for the same transport.
Stop, say so, and establish state before continuing. Do not absorb the second
failure as another retry.

- **Qualifying:** write timeouts; writes returning success but unconfirmable on
  read-back; transport errors (5xx, connection reset, connector absent
  mid-session).
- **Not qualifying:** auth/permission errors; not-found errors (almost always a
  wrong path or ref); any failure from the agent's own malformed call —
  including a write that lands but commits wrong content (Known gap, below).

**Counting.** Timed-out-but-confirmed-landed is not a failure; it resets the
count. Timed-out-and-confirmed-not-landed is one. A read-back that itself times
out is the second, and means state is unknown — that case fires Rule 2
immediately, at the first failure, and nothing here may delay it.

The pattern is kept for what it **detects**, not for any remedy it once opened:
a two-failure fire is how contention between concurrent sessions gets noticed at
all, and that diagnostic value holds whatever the underlying cause turns out to
be (`decisions/log.md` `DEC-000080`). It arrived in this repo as a trigger for
proposing an alternative directive-delivery track; that track is retired
(`skills/directive-dispatch.md`), and the detector is filed here instead, with
the transport failures it detects.

## Scope

The rules are written against any tool-mediated remote mutation. The GitHub MCP
tools are the instance that produced them and the one most often in use, but
nothing here depends on that transport: the failure is that a response is a
claim about a write rather than evidence of one, and every mediated transport
has it.

Rule 3 assumes git. Where a project uses another version control system, the
rule is that the repository's own log is authoritative over the tool's response.

**What this policy no longer governs: dispatch.** Directives travel as paste
blocks and are landed by the executor with ordinary local git
(`skills/directive-dispatch.md`), so no mediated write stands between a decision
and its record. That removed the largest and most consequential population of
chat-side writes these rules were written to cover. The rules are unchanged and
still binding — they now govern the mediated writes that remain, whichever
transport carries them, rather than a dispatch step that no longer exists.

**Where the agent cannot read its own write back**, the three rules have nothing
to verify with, and the obligation changes rather than lapsing: verification is
the operator's, and the agent reports only what the operator reported — never as
verified on its own authority. The tree's standing instance of this case was the
retired directive-delivery path, where the write landed in a local clone the
chat-side agent could not reach; the case is now hypothetical here, and the rule
is stated for the transports where it recurs.

## Relationship to existing rules

`skills/spec-review-cycle.md` constrains what crosses the chat boundary at all:
documents enter as uploads, full documents never leave, and the cycle directive
is delivered as a paste block rather than written through a tool. A cycle
therefore performs no mediated write. That is exposure removed, not exposure
verified — these rules still govern any write a session does make.

The same skill requires that reviewed commit SHAs are recorded in the directive
and calls one without SHAs invalid — which only holds if the SHAs recorded are
ones somebody actually read back.

`skills/directive-dispatch.md` is the other side of the same topic. Its executor
obligations cite this policy for the SHA an executor reports: read it back from
git, never from a write call's return.

## Known gap — landing is verified, content is not

These rules verify that a write **landed**. They do not verify that what landed
is what was intended.

The mirror failure is recorded in `OPEN-ITEMS.md`: a write whose response is
truthful and whose commit is real, because the *request* was wrong. A call
carrying a placeholder string as its content parameter replaced a ~64KB tracker
on the default branch with 19 bytes. Landing-verification alone would have
confirmed the destroyed file as a successful commit; what caught it was the
response `size` field.

Closing this gap means a content-expectation check alongside the landing check.
It is **not** specified here — it is open work, tracked in `OPEN-ITEMS.md`.

## Placement

Filed as a policy rather than under `vendors/`. The original draft placed it in
`vendors/claude-code/` on the reasoning that the mechanics were transport-
specific, and flagged the placement as contestable in the same breath. It was
contested and moved: by the test in `vendors/README.md` — would swapping vendors
leave the sentence true? — nothing in the three rules fails it.

**Still open, and unchanged by the move:** whether the underlying principle —

> A write through an unreliable transport is not evidence that the write landed.
> Verify before reporting, and read state before retrying.

— should also appear in `context-sets/base.md` beside the evidence vocabulary,
where it is always loaded. A rule in `base.md` and a detailed procedure here is
the normal shape, and promoting it is an edit to a governed document that has
not been done.

## Status of this draft

Drafted 2026-08-02 as `vendors/claude-code/mcp-write-verification.md` per the
doc-review directive, executing Q5. Moved and generalised 2026-08-06; the
transport-specific framing was the only vendor-bound content. Revised 2026-08-08
per `docs/cycles/trivium-gate-cycle-1-directive.md` (D7, D14): Rule 3 scoped back
to provenance, and Scope extended to the case where the agent cannot read its own
write back. Revised 2026-08-09 per
`docs/cycles/friction-refactor-2026-08-09-directive.md` (D1.2, D1.3): Scope
records that dispatch has left the mediated-write path entirely, so these rules
govern the writes that remain; the retired delivery track is no longer named as
the standing instance of the unverifiable-write case; and **Rule 4** is added,
carrying the two-consecutive-failure detector from
`skills/directive-dispatch.md`, where it existed only as an on-ramp to that
track. Nothing here is agreed.
