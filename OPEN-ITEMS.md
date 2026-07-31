# Open Items

This file tracks open questions, deferred decisions, and outstanding fixes
for the AI operating model. Updated at defined checkpoints per
`context-sets/spec-and-change-discipline.md`.

Last updated: 2026-07-31

---

## Write-access boundary for ai/ — read-only except OPEN-ITEMS.md (DECIDED, pending policy incorporation)

**Decided by Dave, 2026-07-31, effective immediately:** project sessions
(any agent working a project repo, in any role) treat everything in this
repo as read-only, with one exception: `OPEN-ITEMS.md`. Sessions may
append or amend open items here to capture methodology observations,
decisions, and gaps as they surface — that is the designed intake path.
All other files (roles, policies, context sets, skills, boundaries,
`operating-model.md`, README, MANIFEST) are canonical and change only
through this repo's own drafting-and-review process, in sessions whose
purpose is methodology work.

**Rationale:** canonical methodology docs changing as a side effect of
project sessions is the same defect class as spec drift — untracked,
unreviewed mutation of a source of truth. The single writable surface
gives project sessions somewhere to put what they learn without opening
that door. (This very entry is the worked example: the rule was decided
in a project session and recorded here rather than written into
`operating-model.md` directly.)

**What's needed:** fold the rule into canonical text — likely
`operating-model.md` "Relationship to tools" and/or a `boundaries/` doc,
plus a line in `roles/orchestrator-agent.md` — via normal process. Until
then this entry is the binding statement.

---

## Model selection by role — make cost/capability a per-role, per-step decision

**Source:** wne-crm Orchestrator session, 2026-07-31 (cycle-10 closure). A
frontier-tier model ran the Orchestrator role for a session that was
majority-mechanical (SHA bookkeeping, write-verify loops, ref discipline,
handoff maintenance). The methodology names roles and session boundaries
but is silent on which model tier each role warrants — every session
implicitly inherits whatever model the operator happens to open.

**The observation:** the evidence model already externalizes much of the
safety. Where errors are detectable by construction — stats-guarded
writes, red-gates, verify-before-assert, re-gates — a cheaper model is
safe, because the guards catch drift regardless of who drifts. Capability
was load-bearing in that session at exactly three points: treating a
one-line stats anomaly (+3/−3 vs. expected +2/−2) as a stop condition
rather than noise; inventing a new guard mid-session (the stats-expectation
check on full-file MCP writes); and byte-exact long-context reproduction
of a ~107KB document. Judgment-dense work — spec-cycle triage, reviewer
disagreements, directive drafting with STOP conditions, handoff synthesis —
propagates mistakes into canonical documents and stays frontier.

**What's needed:** a methodology update — probably a section in
`operating-model.md` plus a line per role doc — covering:

1. **A model-tier recommendation per role,** chosen at session open the
   same way the role is chosen. Working hypothesis from the source
   session: efficient tier for Orchestrator-as-executor, Coder on routine
   packages, and mechanical directive execution; frontier tier for
   Spec Reviewer, Skeptic/Risk, Architect, spec-cycle Orchestration, and
   anything drafting canonical text.
2. **Assignment criteria,** not just a static table: (a) are this role's
   errors detectable by construction — i.e. do externalized guards catch
   them? (b) is long-context fidelity load-bearing? (c) do this role's
   judgments propagate into canonical documents or gates? Two or three
   "yes" answers → frontier.
3. **An evidence step before demotion:** trial the cheaper tier on a
   routine package with all guards active; the guard-fire rate is the
   signal. Tier decisions are recorded with that evidence, per the core
   rule — not assigned by intuition, including the intuition of the
   frontier model that proposed this item.
4. **Vendor neutrality per the tooling rule:** durable policy speaks in
   tiers (frontier / efficient), never model names. Concrete model
   choices live in per-project configuration, same as the flag-backend
   pattern.

**Note:** interacts with the session-boundary habit (fresh chat per
phase) — the phase boundary is the natural tier-switch point, so this
costs nothing operationally once the recommendation exists.

---

## Per-project frontmatter enforcement as a project-setup step

**Source:** Document metadata policy cycle-2 revision session, 2026-07-21.
The revised `policies/document-metadata-policy.md` mandates that every
project applying this methodology adopts the metadata schema for its spec
documents — adoption is not optional. But the methodology repo's hooks
cannot reach project repos, so each project must stand up its own
enforcement.

**What's needed:** "Stand up frontmatter enforcement" becomes a defined
project-setup step. This belongs in the per-project TRD/setup guidance
covering CI/CD mechanics — currently deferred territory per the v0.4
decision to map deploy/release mechanics in per-project TRDs. When that
guidance is written, include the frontmatter hook as a required setup item.
Blocked on the policy reaching `agreed`; sequenced with the CI/CD mechanics
mapping.

---

## Build this repo's frontmatter-enforcement hook

**Source:** Document metadata policy cycle-2 directive (A5), 2026-07-21.
The policy's Scope section states "Enforcement (hooks) checks exactly the
in-scope set," but nothing tracked standing up the methodology repo's own
hook.

**What's needed:** Build the frontmatter-enforcement hook over the
in-scope set as amended by cycle-2 B1: the six directory globs plus
`operating-model.md` and `README.md`. Blocked on the policy reaching
`agreed`; sequenced with the frontmatter migration item below.

---

## Migrate existing docs to YAML frontmatter per document-metadata-policy

**Source:** Document metadata policy session, 2026-07-21. New
`policies/document-metadata-policy.md` (draft) establishes YAML frontmatter
as the metadata format for all methodology and spec documents.

**What's needed:** Convert every existing doc's plain `Status:` line to
frontmatter with the required fields (`status`, `last-reviewed`, `audience`).
Blocked on the policy itself reaching `agreed`. Migration is mechanical but
`audience` requires a per-doc judgment call.

---

## Remove repo version number from MANIFEST.md

**Source:** Document metadata policy session, 2026-07-21.
`policies/document-metadata-policy.md` supersedes the "single version
declared once in `MANIFEST.md`" decision — git SHA is the version.

**What's needed:** Edit `MANIFEST.md` to drop the version declaration and
state the git-SHA-is-the-version rule (or point to the policy). Blocked on
the policy reaching `agreed`; per the revised policy, this edit and the
spec-template footer revision land in the same change package as the
agreement.

---

## Adopt reviews/ directory for review history; migrate root REVIEW-*.md

**Source:** Document metadata policy review session, 2026-07-21. The cycle-1
gate review of `policies/document-metadata-policy.md` is being written to
`reviews/document-metadata-policy-cycle-1.md`, establishing `reviews/` as the
home for review-history artifacts.

**What's needed:** Make `reviews/` the standing convention for review history
and migrate the three existing root-level files (`REVIEW-v0.4.md`,
`REVIEW-NOTES-v0.3.md`, `REVIEW-NOTES-v0.2.md`) into it. Rationale: root is
crowding, and one home for review artifacts keeps them from scattering. Keep
reviewer findings (`reviews/`) distinct from triage decisions (cycle
directives) — the canonical-vs-derived split from
`policies/source-of-truth-policy.md`. Low priority; cheap now, cheaper than
running two conventions indefinitely.

---

## Project context configuration for WNRealtor-CRM (token optimization, workstream 1 of 2)

**Source:** Token optimization session, 2026-07-20. Workstream 2 (methodology
change) shipped as v0.5 (`skills/spec-review-cycle.md`, commit `a3ffe08`).
This item is the remaining workstream.

**What's needed:** Decide the Context panel file list and Instructions text
for the WNRealtor-CRM Claude project. Candidates already proposed:
`roles/spec-reviewer-agent.md`, writer style guide,
`boundaries/mocked-boundaries.md`, `skills/spec-review-cycle.md`. Exclusions
already decided: PRD/TRD (change every cycle),
`context-sets/collab-workflow.md` (artifact-pane default is the wrong mode
for that project's gate-cycle chats). Short behavioral directives (terse
tone, follow spec-review-cycle for gate reviews) go in Instructions, not
Context.

---

## Spec evolution policy — how does the spec stay canonical when reality diverges?

**Source:** Catchable Phase 1, 2026-07-15. The 511 SF Bay stops API returned a
response shape (`Contents.dataObjects.ScheduledStopPoint[]`) that differed from
what the TRD assumed. The bug was fixed in code and captured in a retro, but the
TRD was not updated. This is spec drift.

**The gap:** The operating model states that specs are canonical and that
conflicts are hard stops. But it is silent on what happens when live integration
discoveries, bug fixes, or real-world misalignments invalidate a spec assumption
mid-implementation. There is no policy for:

- When the spec must be updated (before the fix ships? after? never for bugs?)
- Who triggers the update (the agent that found the divergence? DAVE?)
- What constitutes a spec-worthy divergence vs. an implementation detail
- How to keep the spec trustworthy as a regeneration artifact over time

**Why this matters:** If the spec is the leverage point for LLM-driven
regeneration (e.g. rewrites, new platforms), spec drift silently erodes that
leverage. A spec that doesn't reflect reality can't reliably regenerate the
correct implementation.

**What's needed:** A lightweight policy — probably a section in
`context-sets/spec-and-change-discipline.md` — covering:
1. The trigger: what kinds of divergence require a spec update?
2. The timing: before fix, after fix, or at session end?
3. The owner: which role is responsible?
4. The mechanism: in-place edit to PRD/TRD, or a versioned amendment?

**Note:** This is distinct from the retro process open item. Retros capture what
went wrong; this policy governs ongoing spec maintenance as the codebase evolves.

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
