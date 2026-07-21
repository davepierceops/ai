# Product Requirements Document (PRD) — Template

Status: draft

## What this is

The PRD is the **standing product specification**: the authoritative description
of *what* is being built and *why*. It is canonical and sits at the top of the
spec spine, above the TRD.

The PRD owns product intent. It is Dave's document.

## Authorship

- **Owned and agreed by:** Dave (PM/EM/Owner). Product intent, user value,
  prioritization, and acceptance criteria are Dave's responsibilities.
- **Drafted with:** agents may draft and propose, but the PRD is not in force
  until Dave agrees. Claude drafts, Dave verifies.

## Relationship to other artifacts

The PRD is the parent of the TRD and the source from which acceptance criteria
are derived. GitHub Issues are downstream tracking artifacts derived from these
specs, never an independent source of truth. PRD/Issue conflicts are a hard stop
(see `policies/source-of-truth-policy.md`).

---

## Required sections

### 1. Problem and intent
The problem being solved and who has it. Why this is worth building now.

### 2. Users and use cases
Who uses this and the concrete situations in which they do.

### 3. User journeys

Define the **Top K** journeys — the K most important journeys out of all possible
journeys this product could support — where K is between 1 and 9. The total
number of possible journeys may be much larger; that's fine. This section
captures only the ones that matter most right now. These are the canonical
journeys from which goals, acceptance criteria, and measurement all trace back.
If more than 9 journeys feel equally critical, pick the 9 most critical, ship
this PRD, and create a backlog item noting that additional journeys remain
undefined. A large journey space signals a product still finding PMF —
over-defining it up front creates churn, not clarity.

For each journey:
- **Actor**: who is doing this.
- **Trigger**: what causes them to start.
- **Steps**: the sequence of actions and system responses.
- **Expected outcome**: what success looks like for the user.

These journeys are inherited by the TRD, which defines SLOs for each.

### 4. Goals and non-goals

#### Functional goals
What the product or change must do. Concrete outcomes, not feature lists.

#### Non-functional goals
The quality bar the product must meet. Address each dimension; "N/A" is a valid
answer where the dimension is not a constraint for this product.

- **Performance**: latency, throughput, and response time targets.
- **Reliability**: uptime, error rate, and fault tolerance expectations.
- **Scalability**: load handling and growth headroom.
- **Security**: authentication, data protection, and threat model.
- **Maintainability**: ease of change, extension, and debugging.
- **Usability**: accessibility, learnability, and UX quality bar.
- **Observability**: logging, metrics, alerting, and traceability.
- **Portability / Compatibility**: platform, browser, or API version constraints.
- **Compliance**: regulatory, legal, or data residency requirements.

#### Non-goals
What this deliberately does not try to do. NFR-specific exclusions (e.g. "sub-100ms
latency is out of scope for v1") belong as a note inside the relevant dimension
above rather than here.

### 5. User outcomes and measurement
How we will know the product improved things for users. This is distinct from
acceptance criteria: ACs gate whether the implementation is correct; this section
defines the signals — quantitative or qualitative — that confirm the change
produced real user value. Name the metric or signal, the baseline if known, and
the mechanism by which it will be observed (telemetry, user feedback, manual
review, etc.).

### 6. Acceptance criteria
The explicit, written conditions a unit of work must meet to be accepted. These
are the source the Test Designer derives test cases from, so they must be
concrete enough to test. Per-unit ACs may live here or in the unit's own
artifact, but they derive from this document.

### 7. Risk tolerance
What kind of risk is acceptable for this product and what is not. This feeds the
release gate and the consequential-change classification.

### 8. Open product questions
Standing product unknowns, each naming what would resolve it.

---

## Authoring checklist

Before Dave agrees a PRD (or a PRD revision), the Spec Reviewer should confirm:

- [ ] All required sections are present and substantively answered.
- [ ] Top K user journeys are defined, each with actor, trigger, steps, and expected outcome.
- [ ] K is between 1 and 9; if more journeys exist, a backlog item is noted.
- [ ] Functional goals are concrete outcomes, not feature lists.
- [ ] Every NFR dimension is addressed or explicitly marked N/A.
- [ ] User outcomes and measurement names signals, baselines, and observation mechanisms.
- [ ] Acceptance criteria are concrete enough to derive test cases from.
- [ ] Risk tolerance is stated explicitly, not implied.
- [ ] Open questions each name what would resolve them.
- [ ] No section contradicts another within this document.
- [ ] The document is consistent with any existing TRD (if one exists).

---

## Skeleton (copy this into a project PRD)

Instantiated project PRDs carry YAML frontmatter per
`policies/document-metadata-policy.md`. `status: agreed` requires a non-null
`last-reviewed`; the document's version is its git SHA — no per-document
version numbers.

```markdown
---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# PRD: <project name>

## 1. Problem and intent
## 2. Users and use cases
## 3. User journeys
## 4. Goals and non-goals
### Functional goals
### Non-functional goals
### Non-goals
## 5. User outcomes and measurement
## 6. Acceptance criteria
## 7. Risk tolerance
## 8. Open product questions
```
