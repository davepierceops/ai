---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Commit and Change Control

## Purpose

This policy defines when a change flows to release automatically and when an
explicit human go/no-go is required. It rests on two **independent** axes that
must not be conflated:

- **Control surface (not revisited here).** The primary human control surface is
  spec, tests, and observability — not *human* code review. Code review is
  agentic (Reviewer, Skeptic/Risk) and its output is evidence. See README
  principle #5 and `boundaries/human-review-boundary.md`.
- **Release gate (this policy).** Independently of who reads the code, some
  changes warrant an explicit human go/no-go before they reach users.

The gate event is the **release decision**, not the commit. *Deploy* (code
running on prod) and *release* (functionality exposed to users) may be separate
events; where the release event sits relative to commit and deploy is a
per-project concern recorded in the project's TRD. When feature flags separate
the two, the gated release event is the **exposure** (e.g. the flag flip), not
the deploy. This policy speaks in terms of the release decision; each project's
TRD maps that to its actual CI/CD.

The resolution is a **two-tier release gate**.

## Tier 1 — Routine changes: flow on evidence

Routine, low-risk changes do **not** require an explicit human go/no-go. They
flow to release once the standard evidence exists: spec/ACs satisfied, tests
written and confirmed-red-then-green, agentic quality review and skeptic/risk
review passes done, and a
change package produced.

This is the default path. Do not manufacture approval ceremony for routine work.

## Tier 2 — Consequential changes: explicit human go/no-go

A change in the **consequential class** must be presented for the human's review
and receive a clear, explicit go before it is **released**. The following list
is exhaustive — if a change does not touch any of these, it is routine. When
unsure, treat as consequential and ask. The consequential class is any change
that touches:

- authentication or authorization,
- a schema or data migration,
- security or privacy controls,
- an irreversible or hard-to-reverse operation (data deletion, destructive
  migration),
- first exposure of a new surface or feature to users (e.g. a flag flip,
  a rollout, or a new endpoint going live),
- a breaking change to a public interface (API contract change, removed
  endpoint, changed response shape, renamed or removed UI flow),
- a change to pricing, billing, or entitlements,
- a change to user data visibility or sharing (what users can see about
  themselves or others),
- a **verification boundary** — adding/removing a live integration, changing a
  fixture for external data, or moving a boundary's verification class,
- core architecture (a change to the standing TRD),
- any change to a code path for a Top K user journey whose SLO error budget
  is at or below 20% remaining.

For these, the sequence is: present the change and its evidence → human reviews
the test and agent-review artifacts → explicit go/no-go → only on a go does it
release. If a go has not been explicitly given, the change does not reach users.

A per-change architecture summary that moves a boundary is, by definition, in
this tier.

## Red-gate (applies to both tiers)

Before any implementation, tests derived from the acceptance criteria must be
run and **confirmed to fail**. A test that passes before implementation is a
broken test, not a head start. Implementation proceeds only as far as needed to
turn the confirmed-failing tests green. See
`context-sets/spec-and-change-discipline.md`.

## Test/Coder separation (applies to both tiers)

For a given unit of work, the agent that writes the tests is not the agent that
implements it, and vice versa. This preserves tests as an independent
specification. See `context-sets/ai-native-engineering.md` and the Test Designer
and Coder role documents.

## Pending gate visibility

A change awaiting a go/no-go must never sit silently in a queue.

The **`human-gate` GitHub issue is the canonical record of a pending gate** —
one issue per pending change, opened when the change is ready for the gate.

Its body is **derived from the change package**, not written fresh: intent,
evidence summary, verification boundary, known gaps, and what is blocked until
a go. Writing it twice produces two copies that drift, and the issue is the one
that outlives the conversation.

**In chat, state one line**: the change, that it is in the consequential class,
a pointer to the issue, and **an explicit request for a go/no-go**. That line is
the notification; the issue is the record. Do not restate the evidence in chat —
a summary long enough to decide from is a summary long enough to drift from the
issue. But do not drop the ask: "Absence of a response is not a go" only holds
if someone was actually asked.

**Which artifact is canonical for what:** the issue is canonical for the
*existence and state* of a pending gate. The change package is canonical for
the *evidence*. If a derived issue body has drifted from its change package,
re-derive the body; do not reconcile in the other direction.

**When the issue cannot be opened** — GitHub unreachable, tooling degraded, no
remote — the chat statement carries the full derived body instead of a pointer,
and the change **does not proceed to release** until the issue is opened and
linked. The change package holds the record in the interim. This is not
hypothetical: the directive that introduced this rule was itself delivered as a
file because MCP GitHub was unavailable that session.

The `human-gate` label is canonical across all projects. Dave can query it
across repos to see every pending gate at any time.

The mechanism for routing the go/no-go response back into the workflow (e.g.
a comment on the issue, a chat reply, a label change) is a per-project concern
and must be named in the project's TRD operational concerns section.

A change does not proceed until the go is given explicitly. Absence of a
response is not a go.

## When in doubt

If it is unclear whether a change is routine or consequential, treat it as
consequential and ask. The cost of an unnecessary approval is small; the cost of
an unreviewed consequential change is not.
