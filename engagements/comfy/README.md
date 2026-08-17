---
status: draft
last-reviewed: null
audience: [all-roles, human, client]
---

# Engagement Pack: Comfy

This directory adapts the parent operating model (the root of this repository)
for a client engagement: brownfield SRE work at Comfy, beginning with making
ephemeral test environments spin up faster.

This document is written to be shown to the client. It explains how an
AI-native engineering practice is governed when the system belongs to someone
else.

## The parent model in one breath

Dave is final authority; LLM agents act as the implementation team. Trust
comes from evidence, not from watching the typing: specifications, tests,
reviews, verification boundaries, and operational signals. The core rule is:
manage the proof, not the code.

## What survives unchanged

The evidence discipline survives whole. Agent claims require evidence. Every
diff is reviewed by a clean-context agent that did not write it — run here as
a standing gate on every diff, tighter than the parent, which requires
independent review only for meaningful changes. Green anything does not imply
shippability beyond the verified boundary. Escalation on ambiguity is
mandatory, and it terminates at Dave.

## What an engagement inverts

### The system precedes the spec

The parent model is spec-first because greenfield work starts from a blank
page. An engagement starts inside a running system that is partly undocumented
and partly hidden. Discovery therefore precedes specification, and the
canonical artifact chain becomes:

**System Map** (discovered, with per-claim provenance) → **Measurement
Baseline** (the instrumented truth about where time goes) → **Improvement
Proposal** (a change with a stated expected delta) → **change packages**.

Archaeology before architecture. See `roles/cartographer.md` and
`skills/system-discovery.md`.

### The red-gate becomes the baseline-gate

The parent model requires tests confirmed failing before implementation. The
engagement translation: **the baseline is the failing test.** No optimization
is implemented until the stopwatch exists, the baseline distribution is
captured, and the expected delta is stated in advance. An improvement that
cannot state its expected delta is not ready to build. After the change, the
same stopwatch either shows the delta or it does not. See
`skills/baseline-measurement.md`.

### Ownership becomes guest posture

In the parent model Dave owns every gate. Here Dave is a guest in the client's
system. Everything lands as a pull request; nothing is pushed. The client's
humans hold the release gate on their own systems. Within the agent team, Dave
remains the final authority; how decisions are negotiated with the client is
Dave's job as a professional, not the machinery's.

### Ceremony has a floor and an override log

The engagement runs the minimum ceremony that preserves the evidence chain:
baseline-gate, clean-context skeptic review on every diff, and a lean change
package. Every ceremonial element is trivially overridable by Dave — the
override is logged, and the log is reviewed at the retro. Overrides are data
about ceremony fit, not exceptions to be ashamed of. See
`policies/override-log-policy.md`.

### Agents get zero write access to the client's cloud

Agents operate read-only in the client's infrastructure, with narrowly named
carve-outs only where discovery strictly requires them. Mutations flow through
pull requests and human-executed applies. This policy is not overridable in
the field. See `policies/client-credentials-policy.md`.

## The crew

Four roles, adapted from the parent cast:

- `roles/chief-of-staff-engagement.md` — state, triage, and next steps; the
  role Dave invokes most.
- `roles/cartographer.md` — discovery; produces the System Map and the
  instrumentation plan; read-only by construction.
- `roles/implementer.md` — writes the Terraform, workflow changes, and
  measurement code, from agreed proposals, delivered as PRs.
- `roles/skeptic-engagement.md` — clean-context review of every diff; lean
  format, standing gate, Dave-overridable.

## Key principles

1. Manage the proof, not the code — and in an engagement, the first proof is
   the measurement.
2. Discovery precedes specification; every System Map claim carries its
   provenance.
3. The baseline is the failing test.
4. Every diff gets clean-context review.
5. Agents are read-only in the client's world; humans move the levers.
6. Ceremony is minimal, overridable, and every override is logged.
7. Escalation terminates at Dave.

## Metadata convention

Pack documents follow the parent frontmatter format
(`../../policies/document-metadata-policy.md`) with two pack-local
extensions: `audience` may include `client` — a document written to be shown
to Comfy — and the engagement role slugs defined in `roles/` here.
Enforcement does not yet reach `engagements/**`; extending the parent
policy's scope is a recorded open item and takes a full review cycle, as that
policy is a named gate document.
