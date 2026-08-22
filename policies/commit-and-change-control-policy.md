---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Commit and Change Control

This policy governs both session kinds: decision sessions and execution
sessions.

## Purpose

This policy defines two things its title promises: how a change reaches the
default branch (**commit control**), and when a change reaching users requires
an explicit human go/no-go (**change control**).

## The consequential class

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

A per-change architecture summary that moves a boundary is, by definition, in
this class.

## Pending gate visibility

This section governs decision sessions.

A change awaiting a go/no-go must never sit silently in a queue.

The **`human-gate` tracker issue is the canonical record of a pending gate** —
one issue per pending change, opened when the change is ready for the gate.

Its body is **derived from the change package**, not written fresh: intent,
evidence summary, verification boundary, known gaps, and what is blocked until
a go.

**In chat, state one line**: the change, that it is in the consequential class,
a pointer to the issue, and **an explicit request for a go/no-go**. That line is
the notification; the issue is the record. Do not restate the evidence in chat,
and do not drop the ask.

**Which artifact is canonical for what:** the issue is canonical for the
*existence and state* of a pending gate. The change package is canonical for
the *evidence*. If a derived issue body has drifted from its change package,
re-derive the body; do not reconcile in the other direction.

**When the issue cannot be opened** — the tracker unreachable, tooling
degraded, no remote — the chat statement carries the full derived body instead
of a pointer, and the change **does not proceed to release** until the issue is
opened and linked. The change package holds the record in the interim.

The `human-gate` label is canonical across all projects. Dave can query it
across repos to see every pending gate at any time.

The mechanism for routing the go/no-go response back into the workflow (e.g.
a comment on the issue, a chat reply, a label change) is a per-project concern
and must be named in the project's TRD operational concerns section.

A change does not proceed until the go is given explicitly. Absence of a
response is not a go.

## Commit, push, and merge

### Push mechanics

**Plain `git push` is allowed for agents.** It requires no per-push approval.

**Force-push is denied**, and denied at two layers:

- **Client-side** — a deny rule in the agent runner's configuration, and it
  must hold in *every* permission mode, including the modes that otherwise
  skip prompting. A deny that a permissive mode waives is not a deny.
- **Server-side** — branch protection on the default branch, which binds every
  credential that reaches the repository, including ones no local configuration
  has ever seen.

### Branch protection is the structural gate

Branch protection on the default branch is the structural gate this policy's
push posture rests on; it lives in the forge's configuration, not in the
repository, so nothing here can verify it, and it is an adoption precondition
confirmed by a human.

### Agents may open and merge pull requests

For the **routine class**, agents open a pull request and merge it. No human
gate fires at the merge. The gates are elsewhere and both are named already:
the release decision, and the reviewer gate that precedes Dave's agreement of a
canonical document.

For the **consequential class**, the merge is not what is gated either — the
*exposure* is. Wherever deploy and release are separate events, a merged pull
request is not a released change, and the release decision is where the
explicit go/no-go attaches.

### Spec branches and the reconciliation pull request

Spec edits made while a tranche is executing land on `spec/<tranche-slug>`
without a per-edit gate. Commit control is unaffected: branch protection binds
the **default branch**, and a spec branch reaches it only through the
**reconciliation pull request**, which carries the reviewer gate over the whole
accumulated diff. The gate is not removed; it is charged once, at the
reconciliation, instead of once per edit.

Two things follow. Unreviewed spec text cannot reach the default branch, because
nothing reaches it except through a pull request. And a document reading
`agreed` on the default branch has been through the gate, because the transition
that sets it is a frontmatter-only status-transition commit made after the
reconciliation cycle closes.
