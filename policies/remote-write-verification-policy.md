---
status: draft
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

State SHAs read from git. Never abbreviate a SHA that will be used as a
pointer, and never invent one.

## Scope

The rules are written against any tool-mediated remote mutation. The GitHub MCP
tools are the instance that produced them and the one most often in use, but
nothing here depends on that transport: the failure is that a response is a
claim about a write rather than evidence of one, and every mediated transport
has it.

Rule 3 assumes git. Where a project uses another version control system, the
rule is that the repository's own log is authoritative over the tool's response.

## Relationship to existing rules

`skills/spec-review-cycle.md` already constrains *how much* goes through the
transport: "The only MCP write is the cycle directive (small)," and full
documents never round-trip. That constraint limits exposure to this failure
mode; it does not address verifying the writes that do happen. These rules cover
the gap.

The same skill requires that reviewed commit SHAs are recorded in the directive
file and calls one without SHAs invalid — which only holds if the SHAs recorded
are ones somebody actually read back.

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
transport-specific framing was the only vendor-bound content. Nothing here is
agreed.
