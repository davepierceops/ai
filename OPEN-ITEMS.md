# Open Items

This file tracks open questions, deferred decisions, and outstanding fixes
for the AI operating model. Updated at defined checkpoints per
`context-sets/spec-and-change-discipline.md`.

Last updated: 2026-07-01

---

## ~~A2 — Consequential-change class: confirm membership is complete~~

**RESOLVED.** The list is exhaustive. Updated
`policies/commit-and-change-control-policy.md` to state this explicitly.
Iterate via normal change process if additions are needed later.

---

## ~~A8 — Define "meaningful change"~~

**RESOLVED.** A meaningful change is any change that warrants a change package
— any change affecting behavior, interfaces, tests, dependencies, boundaries,
or documentation of substance. Trivial changes (typo fixes, comment edits,
purely mechanical formatting) do not require a change package and are not
meaningful in this sense. All affected documents should use this definition.

---

## ~~Reviewer gate vs. advisory~~

**RESOLVED.** The Reviewer Agent is a hard gate. A meaningful change does not
proceed to Skeptic/Risk review or release without Reviewer sign-off. Updated
`roles/reviewer-agent.md` and `policies/agent-review-policy.md`.

---

## ~~Per-file vs. single-file role granularity~~

**RESOLVED.** Roles operate per change unit. The Reviewer Agent reviews the
entire change as a single pass — all files, test plan, diff, and boundary
updates together. If only a subset was reviewed, the reviewer must state what
was and was not inspected. Updated `roles/reviewer-agent.md`.

---

## ~~Error budget exhaustion as a consequential-change trigger~~

**RESOLVED.** Any change to a code path for a Top K user journey whose SLO
error budget is at or below 20% remaining is automatically consequential,
regardless of other characteristics. Updated
`policies/commit-and-change-control-policy.md`.

---

## ~~SRE production readiness checklist~~

**RESOLVED (deferred).** Moved to `BACKLOG-v2.md`. Not blocking current
work. When tackled, likely a new context set or policy doc that extends the
definition of done in `context-sets/spec-and-change-discipline.md`.

---

## Add retrospective process to the operating model

**Source:** Catchable Phase 1, 2026-07-01. Missing `index.html` + `src/main.tsx`
reached `origin/main` with 225 passing tests. The architect role did not produce
a per-change architecture summary that listed browser entry files as explicit
deliverables.

**What's needed:** A lightweight retro step or trigger in the operating model —
when to run one, what it should capture (what happened, why it wasn't caught,
which role/gate failed, recommended process change), and where the output lives.
Retros are distinct from the skeptic/risk review: they happen after a failure is
discovered, not before release.

**Note:** The architect role instruction for Vite/React projects should be
updated immediately as a direct fix, independent of the broader retro process
definition.
