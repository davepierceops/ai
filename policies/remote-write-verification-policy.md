---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Remote Write Verification

This policy governs both session kinds: decision sessions and execution
sessions. Its rules govern any tool-mediated remote mutation, because the
failure is that a response is a claim about a write rather than evidence of one.

## The rules

### 1. The repository's own log is the source of record

Where a local clone exists, `git log` against the fetched remote is the
authority on what landed — not the tool's response, and not the agent's
recollection of what it sent. Where a project uses another version control
system, the rule is the same: the repository's own log is authoritative over the
tool's response.

State SHAs read from the log. Never invent one.

### 2. Two consecutive qualifying failures is a fact about the environment

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
out is the second, and means state is unknown — that case fires immediately, at
the first failure, and nothing here may delay it.

The detector is kept for what it **detects**: a two-failure fire is how
contention between concurrent sessions gets noticed at all, and that diagnostic
value holds whatever the underlying cause turns out to be.

## Known gap — landing is verified, content is not

These rules verify that a write **landed**. They do not verify that what landed
is what was intended. The mirror failure is a write whose response is truthful
and whose commit is real, because the *request* was wrong: a call carrying a
placeholder string as its content parameter replaced a ~64KB file on the default
branch with 19 bytes. Landing-verification alone would have confirmed the
destroyed file as a successful commit; what caught it was the response `size`
field.

Closing this gap means a content-expectation check alongside the landing check.
It is **not** specified here — it is open work.
