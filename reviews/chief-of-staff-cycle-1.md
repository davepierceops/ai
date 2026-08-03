# Review: roles/chief-of-staff.md — cycle 1

Verdict: ready-with-findings
Reviewed: roles/chief-of-staff.md @ 3383ede
Reviewer: Spec Reviewer Agent (Claude Code, cos-supersession-exec session)
Date: 2026-08-02
Scope: roles/chief-of-staff.md gate review — completeness, internal
consistency, traceability to docs/cycles/doc-review-2026-08-02-questions.md
(Q3a/Q3b/Q3c) and docs/cycles/cos-supersession-directive.md (D1-D5),
cross-check against sibling role docs and the documents this cycle's other
work items touched.
Cross-checked: roles/orchestrator-agent.md (superseded body), README.md,
context-sets/ai-native-engineering.md, OPEN-ITEMS.md, BACKLOG-v2.md,
policies/document-metadata-policy.md, policies/commit-and-change-control-policy.md,
roles/pm-em-owner.md, roles/architect-agent.md, roles/coder-agent.md,
roles/reviewer-agent.md, roles/skeptic-risk-agent.md,
roles/release-manager-agent.md, roles/test-designer-agent.md,
roles/context-quality-reviewer.md, skills/change-package-creation.md,
skills/spec-review-cycle.md, docs/cycles/doc-review-2026-08-02-directive.md,
docs/cycles/triage-2026-08-02-directive.md.
Not inspected: git blame / authorship of the chat session that produced the
revised body (out of reach from this session); no live external system
(GitHub `human-gate` issues) queried — repo has none open referencing this
role.
Findings: 2, both non-blocking
Prior cycle: none
Dave should inspect: F1 (repo-bound filename in a portable role doc) — my
ruling is below, but it is a judgment call, not a mechanical check.

## F1 — non-blocking
Claim: The read-sequence names `BACKLOG-v2.md` directly
(`roles/chief-of-staff.md` "The read-sequence", step 4 / closing note), a
repo-specific, versioned filename, inside a role document meant to be
portable methodology (`README.md`: "The portable documents in `/ai/` are
authoritative"; `policies/document-metadata-policy.md`: every adopting
project "stands up its own enforcement" rather than reusing this repo's
files by name).
Location: roles/chief-of-staff.md, "The read-sequence" section, closing
paragraph ("`bin/state` is a `BACKLOG-v2.md` entry...").
Evidence: verified by reading — grepped the live doc set
(`grep -rn "BACKLOG-v2"`) and confirmed `policies/document-metadata-policy.md`
(status: `agreed`) already names `BACKLOG-v2.md`, `OPEN-ITEMS.md`, and
`COLLAB-STATE.md` directly in its own Scope section, so this is not a novel
pattern introduced by `chief-of-staff.md` — it is consistent with an existing,
already-agreed precedent in this doc set.
Consequence: if `chief-of-staff.md` is loaded verbatim as governing context in
a different project repo without a `BACKLOG-v2.md`, the read-sequence's fourth
citation resolves to nothing; the agent would need to substitute the
project's equivalent tracker by judgment, which the doc does not currently
instruct it to do.
Fix (my ruling, per the directive's advisory to rule on this): treat as
repo-bound by design, consistent with `document-metadata-policy.md`'s
existing precedent — not a defect requiring wording before agreement. A
future, repo-set-wide convention-name abstraction (e.g., "the project's
backlog tracker" with a per-project pointer) is a legitimate follow-on, but
scoping it to this document alone, out of step with its sibling policy doc,
would create inconsistency rather than remove it. Non-blocking; Dave may
override this ruling.

## F2 — non-blocking (observation)
Claim: `chief-of-staff.md` has no dedicated "Non-goals" or "Required outputs"
heading, though most sibling role docs
(`roles/architect-agent.md`, `roles/coder-agent.md`, `roles/reviewer-agent.md`,
`roles/test-designer-agent.md`, `roles/release-manager-agent.md`,
`roles/skeptic-risk-agent.md`, `roles/context-quality-reviewer.md`) carry one
or both.
Location: roles/chief-of-staff.md, document structure (no matching `##`
heading).
Evidence: verified by reading — `grep -n "^## " roles/*.md` across the role
set; the content that a "Non-goals" section would carry is present under
`## Constraints` instead ("Does not execute packages... does not make
architecture decisions — escalates ambiguity to Dave").
Consequence: none functional — the constraint content is present, just under
a differently-named heading. Two sibling docs (`roles/pm-em-owner.md`,
`roles/skeptic-risk-agent.md`) already deviate from the
Responsibilities/Required-outputs/Non-goals shape, so this is not a break
from a strictly enforced template — there isn't one.
Fix: none required. Optional, cosmetic: rename `## Constraints` findings that
read as non-goals into a `## Non-goals` subsection for scan-consistency with
the majority of the set. Advisory only.

## Confirmation of directive-scoped cross-checks

- Traces cleanly to Q3a (binding constraint on state — "The binding
  constraint on state (Q3a)" section), Q3b (activation behavior — "Activation
  behavior — the defining property" section), and Q3c (naming) in
  `docs/cycles/doc-review-2026-08-02-questions.md`.
- D1-D5 of `docs/cycles/cos-supersession-directive.md` are each represented in
  the document body (supersession header = D1; D2 is correctly absent from
  this doc — it was ruled closed with no open item, nothing to state here;
  D3-D5 = "Decomposition and handoff" and "Prompt generation" sections,
  verbatim-consistent).
- No remaining live-document reference to `Orchestrator Agent` /
  `orchestrator-agent` outside this doc's own supersession statement, the
  frozen `roles/orchestrator-agent.md` body, and historical
  `docs/cycles/` / `docs/packages/` / `MANIFEST.md` tombstone records (out of
  scope per the directive's Constraints section).
- `bin/state` is referenced consistently between `roles/chief-of-staff.md`
  ("not yet built... a `BACKLOG-v2.md` entry") and the live `BACKLOG-v2.md`
  entry (`### bin/state`, "Render current state for the Chief of Staff...").
- No section overstates confidence beyond what is built; not-yet-built
  tooling (`bin/state`) is explicitly labeled as such.
