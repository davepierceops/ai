---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Commit and Change Control

## Purpose

This policy defines two things its title promises: how a change reaches the
default branch (**commit control**), and when a change reaching users requires
an explicit human go/no-go (**change control**).

The second half rests on two **independent** axes that must not be conflated:

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

The first half — commit control — is deliberately **structural rather than
gated**. Because the gate event is the release decision, the mechanics of
getting a change onto the default branch are bounded by configuration that
holds whoever is acting, not by asking a human per push. Those mechanics are
stated in "Commit, push, and merge" below.

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

## Commit, push, and merge

### Push mechanics

**Plain `git push` is allowed for agents.** It requires no per-push approval.
An approval here would be ceremony on an event this policy does not gate, and
ceremony on a frequent event is how a gate stops being read.

**Force-push is denied**, and denied at two layers, because the layers fail
differently:

- **Client-side** — a deny rule in the agent runner's configuration, and it
  must hold in *every* permission mode, including the modes that otherwise
  skip prompting. A deny that a permissive mode waives is not a deny.
- **Server-side** — branch protection on the default branch (below). This is
  the layer that makes it a guarantee rather than a habit: it binds every
  credential that reaches the repository, including ones no local
  configuration has ever seen.

The client-side rule catches the mistake early and cheaply. The server-side
rule is what the guarantee actually rests on.

### Branch protection is the structural gate

Every adopting repo protects its default branch:

- **no force-push**
- **no branch deletion**
- **changes land via pull request**
- **bypass disallowed, including for administrators**

The last one carries the others. Protection that administrators may bypass
binds only the credentials that were never the risk — an agent holding an
admin-capable token is governed by the honour system, and the protection
reads as a control while enforcing nothing against the actor most able to
break it.

This is what makes "agents may push and merge" safe to state. History on the
default branch cannot be rewritten or destroyed whoever holds the credential,
and every change arrives as a reviewable unit.

Branch protection lives in the forge's configuration, not in the repository,
so nothing in the repo can verify it. It is an adoption precondition, and the
setup checklist is `policies/project-setup-requirements.md` — this policy
states the requirement; that document states what must be true before the
methodology governs work in a repo. Do not duplicate its checklist here.

### Agents may open and merge pull requests

For the **routine class**, agents open a pull request and merge it. No human
gate fires at the merge. The gates are elsewhere and both are named already:
the release decision (Tier 2 above), and the agreement of a canonical
document (`roles/spec-reviewer-agent.md`, a hard gate before Dave agrees).

For the **consequential class**, the merge is not what is gated either — the
*exposure* is. Wherever deploy and release are separate events, a merged pull
request is not a released change, and Tier 2 governs the release.

The pull request is therefore a mechanism for auditability and for making the
change a reviewable unit, not a human approval step. Requiring a human review
on the PR itself would reintroduce human diff-reading as the default control
surface, which `boundaries/human-review-boundary.md` deliberately removes.

### Spec branches and the reconciliation pull request

Spec edits made while a tranche is executing land on `spec/<tranche-slug>`
without a per-edit gate (`context-sets/spec-and-change-discipline.md`, Open spec
delta). Commit control is unaffected: branch protection binds the **default
branch**, and a spec branch reaches it only through the **reconciliation pull
request**, which carries the reviewer gate over the whole accumulated diff
(`skills/spec-review-cycle.md`). The gate is not removed — it is charged once, at
the event where judgment is actually being exercised, instead of once per edit.

Two things follow, and both are structural rather than promised. Unreviewed spec
text cannot reach the default branch, because nothing reaches it except through a
pull request. And a document reading `agreed` on the default branch has been
through the gate, because the transition that sets it is a status-transition
commit made after the reconciliation cycle closes
(`policies/document-metadata-policy.md`).

Force-push, bypass, and the agreement verb are unchanged: a spec branch is an
ordinary branch, and agreement remains Dave's.

## When in doubt

If it is unclear whether a change is routine or consequential, treat it as
consequential and ask. The cost of an unnecessary approval is small; the cost of
an unreviewed consequential change is not.
