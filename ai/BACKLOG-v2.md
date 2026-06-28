# Backlog: AI Operating Model v2

Items deferred from the v0.4 spine review. Each entry names the idea and
enough context to pick it up cold.

---

## Methodology enhancements

### SRE-centric production readiness checklist
Add a checklist (probably a new context set or policy doc) covering production
readiness from an SRE perspective: runbooks, alerting, on-call coverage, rollback
procedure, capacity, SLO baselines, etc. Likely extends the definition of done
in `context-sets/spec-and-change-discipline.md` or lives as its own
`policies/production-readiness-policy.md`.

### Define "meaningful change" (A8)
"Meaningful change" is a load-bearing threshold used throughout the framework
(e.g. "produce change packages for meaningful changes", "when a meaningful
boundary is mocked") but is never defined. Needs a concrete definition that
agents can apply without ambiguity. Resolution should be checked for consistency
against the consequential-change class in
`policies/commit-and-change-control-policy.md`.
See also: `REVIEW-v0.4.md` finding A8.

### Confirm consequential-change class membership (A2)
The consequential class in `policies/commit-and-change-control-policy.md` was
expanded during the spine review but not formally signed off as complete. Revisit
and confirm the list is exhaustive, or explicitly note it is illustrative.
See also: `REVIEW-v0.4.md` finding A2.

---

## Cleanup passes (post-spine)

### Register Spec Reviewer role across the methodology
The Spec Reviewer role was created during the v0.4 spine review but is not yet
referenced in:
- `ai/README.md` (roles list)
- `AGENTS.md`
- `ai/operating-model.md` (9-step flow)

Update all three to include Spec Reviewer as a named role with its activation
points.

### Deferrable fixes from REVIEW-v0.4.md
- **A4**: red-gate behavior in `testing-policy.md` — verify it matches the
  locked definition in `commit-and-change-control-policy.md`.
- **A5**: Architect missing from the agent separation list — add to the
  relevant role or policy doc.
- **A6**: `methodology.md` reference in merge notes — confirm whether this file
  exists or the reference is stale; remove or redirect.

### Error budget exhaustion as a consequential-change trigger
When the error budget for a Top K user journey SLO is exhausted or critical,
any change to that journey's code path should arguably be treated as
consequential regardless of its other characteristics. Add "change proposed
while a relevant SLO error budget is exhausted or critical" to the consequential
class in `policies/commit-and-change-control-policy.md`. Requires deciding what
"critical" means (e.g. <10% remaining) and how the agent determines current
budget state.

---

### Reviewer role: gate vs. advisory
Whether the Reviewer Agent's output is a hard gate or advisory input to Dave
was noted as unresolved in the spine review. Needs a decision and a doc update.

### Per-file vs. single-file role granularity
Whether agent roles (Reviewer, Skeptic/Risk, etc.) operate per-file or per
change unit. Noted as open during the spine review.
