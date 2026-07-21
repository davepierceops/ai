# Technical Requirements Document (TRD) — Template

Status: draft

## What this is

The TRD is the **standing technical specification** for the project. It is
canonical: it is the authoritative description of *how* the system is built,
sitting directly beneath the PRD (which owns *what* is built and *why*).

The TRD is slow-moving. It changes when the architecture changes, not once per
feature. Per-feature technical design does **not** live here — it lives in the
per-change **architecture summary** the Architect Agent produces for each unit
of work (see "Relationship to other artifacts").

## Authorship

- **Drafted by:** the Architect Agent.
- **Agreed by:** Dave (PM/EM/Owner). The TRD is not in force until Dave agrees.
- **Maintained by:** whoever holds the Architect role for a change that alters
  standing architecture updates this document as part of that change, per the
  document-consistency principle (update *every* affected section, not one).

## Relationship to other artifacts

```
PRD  (product, standing)        ← what / why, Dave owns
  └─ TRD (technical, standing)   ← how, Architect drafts / Dave agrees   [THIS DOC]
       └─ per unit of work:
            ├─ Acceptance Criteria        (Dave owns; derived from PRD)
            ├─ Architecture Summary       (Architect; derived from TRD)   ← feeds Issues
            ├─ Test Plan (confirmed red)  (Test Designer)
            └─ Implementation             (Coder)
                 └─ GitHub Issues          (derived, tracking only)
```

The TRD is the durable technical anchor. GitHub Issues are **derived** from it
(via the per-change architecture summary), never the source of truth. If an
Issue and the TRD disagree, that is a **hard stop** requiring Dave's
resolution — see `policies/source-of-truth-policy.md`.

---

## Required sections

A complete TRD must contain the following. Keep each section as short as it can
be while still being a real answer; this is an anchor, not an essay.

### 1. System overview
The shape of the system in a few sentences: major components and how they fit.
What kind of system this is (service, app, PWA, CLI, etc.).

### 2. User journeys and SLOs

Inherit the Top K journeys from the PRD (section 3). Do not redefine them here.
For each journey, define:

- **SLO**: the service level objective — what "good enough" looks like for this
  journey in production. Examples: p95 latency, success rate, error budget.
- **Measurement mechanism**: how the SLO is observed (telemetry, synthetic
  checks, user-facing error rates, etc.).
- **Alerting threshold**: at what point a breach triggers action.

SLOs here are the technical instantiation of the user outcomes defined in the
PRD. If a journey has no SLO, name it explicitly as unverified and track it as
an open question.

### 3. Architecture and boundaries
- Components and their responsibilities.
- Interfaces between components.
- External dependencies (APIs, providers, data stores, auth, browser/PWA
  surfaces).
- The important **boundaries** — the points where this system meets something
  it does not control. Each durable boundary should be declared per
  `policies/verification-boundary-policy.md` and, when cross-cutting, recorded
  under `boundaries/`.

### 4. Verification boundaries (standing)
This is the TRD's link to the evidence model. For each material standing
boundary, name:
- the production surface,
- how it is currently represented (live / contract / mock / assumed),
- its verification class (`mock-verified`, `contract-verified`, `live-verified`,
  `browser-verified`, `production-verified`, `unverified`, `deferred`,
  `accepted-risk`, `blocking`),
- the deferred-verification path, if any.

Durable boundary *types* live in `boundaries/`; this section instantiates the
ones that apply to *this* system. Per-change boundary movement is recorded in
the change's architecture summary and boundary audit, not here — but if a change
makes a boundary movement permanent, reflect it here.

### 5. Data and state
Key data shapes, persistence, ownership, and lifecycle. Where state lives and
who is authoritative for it.

### 6. Failure modes and recovery
For the system as a whole: how it fails, how failure is detected, what the user
sees, and how it recovers or is rolled back. (Per-change failure analysis lives
in the change package; this is the standing picture.)

### 7. Operational concerns
Observability, configuration/secrets, quotas/billing exposure, deployment
assumptions, and anything required to operate the system responsibly. Ties to
`context-sets/production-grade-software.md`.

State the **release model** for this project: whether *deploy* (code on prod)
and *release* (functionality exposed to users) are separate events or collapsed
into one, and therefore where the human release go/no-go physically sits relative
to commit and deploy. The operating model defines the gate as the *release
decision*; this section maps that to this project's actual CI/CD. See
`policies/commit-and-change-control-policy.md`.

If deploy and release are separated, record the **flag mechanism**: prefer a
vendor-neutral interface (e.g. OpenFeature) and name the backend (config/YAML
file, Flipt, Flagsmith, etc.) as a swappable choice, not a lock-in. Note the
flag-lifecycle expectation: each flag has an owner and a removal trigger.

### 8. Constraints, NFRs, and non-goals

Technical constraints the design must respect. This section is the technical
instantiation of the PRD's non-functional goals (PRD section 4). For each NFR
dimension defined in the PRD, state the concrete technical target or constraint
here, or explicitly mark it N/A for this system:

- **Performance**: specific latency/throughput targets and how they are enforced.
- **Reliability**: uptime targets, error budgets, retry/fallback strategies.
- **Scalability**: load model, bottlenecks, growth headroom.
- **Security**: auth mechanism, data protection approach, threat surface.
- **Maintainability**: modularity decisions, dependency constraints, debt policy.
- **Usability**: technical constraints serving UX goals (e.g. bundle size, TTI).
- **Observability**: what is instrumented, how, and where it surfaces.
- **Portability / Compatibility**: runtime, platform, and API version constraints.
- **Compliance**: technical controls required by regulatory or legal NFRs.

Also state explicit technical non-goals — things this architecture deliberately
does not attempt. Prefer boring, understandable designs.

### 9. Open technical questions
Standing unknowns that need resolution. Each should name what would resolve it.
Track these as loose ends rather than relying on memory.

---

## Authoring checklist

Before Dave agrees a TRD (or a TRD revision), the Spec Reviewer should confirm:

- [ ] Every component has a named responsibility and its interfaces are listed.
- [ ] Every external dependency is captured as a boundary with a verification
      class (section 4).
- [ ] No section overstates confidence — assumed behavior is labeled assumed.
- [ ] Failure modes and recovery are addressed at the system level.
- [ ] Non-goals are explicit.
- [ ] Open questions name what would resolve them.
- [ ] The change is consistent across the whole document — no value updated in
      one place and stale in another.

---

## Skeleton (copy this into a project TRD)

Instantiated project TRDs carry YAML frontmatter per
`policies/document-metadata-policy.md`. `status: agreed` requires a non-null
`last-reviewed`; the document's version is its git SHA — no per-document
version numbers.

```markdown
---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# TRD: <project name>

## 1. System overview
## 2. User journeys and SLOs
## 3. Architecture and boundaries
## 4. Verification boundaries (standing)
## 5. Data and state
## 6. Failure modes and recovery
## 7. Operational concerns
## 8. Constraints, NFRs, and non-goals
## 9. Open technical questions
```
