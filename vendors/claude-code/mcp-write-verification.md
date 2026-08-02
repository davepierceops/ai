---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# GitHub MCP — Write Verification

## The failure mode

A write through the GitHub MCP tools can **succeed on the server and fail to
report success to the caller**. A timeout, a dropped response, a tool error
returned after the mutation already landed — in each case the agent's local
view says "failed" while the remote says "committed."

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
authority on what landed — not the MCP tool's response, and not the agent's
recollection of what it sent.

State SHAs read from git. Never abbreviate a SHA that will be used as a
pointer, and never invent one.

## Relationship to existing rules

`skills/spec-review-cycle.md` already constrains *how much* goes through MCP:
"The only MCP write is the cycle directive (small)," and full documents never
round-trip. That constraint limits exposure to this failure mode; it does not
address verifying the writes that do happen. These rules cover the gap.

The same skill requires that "Reviewed commit SHAs are recorded in the
directive" and calls a directive without SHAs invalid — which only holds if
the SHAs recorded are ones somebody actually read back.

## Placement note — this is a judgment call, and it is contestable

Filed under `vendors/claude-code/` because the mechanics are specific to the
GitHub MCP transport: which calls can partially fail, and what reading back
looks like.

But **the principle is not vendor-specific**:

> A write through an unreliable transport is not evidence that the write
> landed. Verify before reporting, and read state before retrying.

That generalizes to any tool-mediated remote mutation, and by the test in
`vendors/README.md` — would swapping vendors leave the sentence true? — it
belongs in the core doc set, most plausibly as a rule in `context-sets/base.md`
alongside the evidence vocabulary.

Promoting it there is an edit to a governed document and was **not** done
here. Flagged for triage.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.5) executing Q5.
Placement was the executor's call per that item. Nothing here is agreed.
