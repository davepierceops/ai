# Collaboration State

Status: active

Tree: v0.4 — full spine review, carried-over files scan, post-spine cleanup, and open items resolution all complete.

## Decisions locked this session

- Test Designer / Coder separation: separate agents per unit of work.
- Standing TRD retained; per-change architecture summary sits between TRD and Issues.
- Gate model: two-tier, fired at the **release decision** (not commit); CI/CD mapping deferred to each project's TRD.
- Control surface vs release gate are independent axes; code review is **agentic** (Reviewer, Skeptic/Risk), not human, by default.
- Deploy != release; gate attaches to the exposure event.
- Versioning (A3): single tree version in `MANIFEST.md`; per-doc `Status` is a maturity word only.
- Change flow: quality review and skeptic/risk review are separate steps; mechanical checks fold into "green".
- Feature flags: vendor-neutral interface (e.g. OpenFeature), backend is a per-project TRD choice; flag lifecycle = owner + removal trigger.
- Spec Reviewer Agent: new role, hard gate before Dave agrees any spec or revision; two modes (gate review, continuity scan); three scan depths; optional proposals during continuity scan.
- PRD additions: user journeys (Top K, 1–9), user outcomes and measurement, NFR section, authoring checklist owned by Spec Reviewer.
- TRD additions: user journeys + SLOs (section 2), NFR cross-reference (section 8), checklist ownership moved to Spec Reviewer, Architect separation requirement.
- `human-gate`: canonical GitHub issue label for consequential changes awaiting go/no-go.
- `OPEN-ITEMS.md`: canonical loose-end tracking file; flushed at defined checkpoints.
- `collab-workflow.md`: new context set for document authorship/review workflow.
- A2 resolved: consequential-change class is exhaustive (not illustrative).
- A4 resolved: red-gate added to testing-policy.md.
- A5 resolved: Architect separation requirement added to architect-agent.md.
- A8 resolved: "meaningful change" = any change warranting a change package (behavior, interfaces, tests, dependencies, boundaries, or documentation of substance). Trivial changes excluded. Definition lives in `context-sets/base.md`.
- Reviewer Agent: hard gate (not advisory); operates per change unit (not per file).
- Error budget exhaustion: changes to a Top K journey code path with ≤20% error budget remaining are automatically consequential.
- SLOs and error budgets: added throughout as first-class concepts.

## Completed work

- Full spine walk (9 files)
- Full carried-over files scan (24 files)
- Post-spine cleanup (README.md, operating-model.md)
- All open items resolved or explicitly deferred to BACKLOG-v2.md
- OPEN-ITEMS.md created and cleared

## Open items

None. See `OPEN-ITEMS.md` (all resolved this session) and `BACKLOG-v2.md` for deferred work.

## Workflow note

Use standalone Markdown plus staged zip packages for collaborative review.
Avoid relying on editable chat canvas state as the only source of truth.
