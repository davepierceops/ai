# Cycle 1 Directive — policies/document-metadata-policy.md

Date: 2026-07-21 (retroactive reconstruction — recorded alongside the
cycle-2 directive per cycle-2 finding B4; decisions were made in the
cycle-1 triage chat and are reconstructed from the cycle-2 review's
resolution check and the decision summary supplied to that review)
Documents in scope:
- `policies/document-metadata-policy.md` @ `f96a313` (introduced in
  `cbddf79`, unchanged since, at review time)

Review artifact: `reviews/document-metadata-policy-cycle-1.md`

## Decisions

### B1 — accept
Finding: Scope of applicability is undefined.
Resolution: Add a Scope section. In-scope set: six directory globs —
`policies/**`, `roles/**`, `context-sets/**`, `boundaries/**`,
`skills/**`, `specs/**`. Explicitly exclude trackers, adapters
(`CLAUDE.md`, `AGENTS.md`, `.claude/**`), and instantiated project
artifacts. Project adoption of the schema is mandatory, with per-project
enforcement tracked in `OPEN-ITEMS.md`.

### B2 — modify
Finding: Status vocabulary contradicts existing canonical usage.
Resolution: Vocabulary is `draft | in-review | agreed | superseded |
deprecated` — `agreed` replaces `approved` (merges A5). `stable` maps to
`agreed` via a grandfather clause for documents agreed before the
policy's adoption (`last-reviewed: null`). Template footers
(`Status: <draft|agreed> v<x.y>  Agreed by:`) are removed in the
agreement change package; skeletons carry compliant frontmatter.
`placeholder` and `active` are resolved by the scope exclusions rather
than mapping.

### B3 — accept
Finding: Lifecycle is incomplete — revising an agreed document.
Resolution: Add a Revision lifecycle section: editing an `agreed`
document flips `status: in-review` and resets `last-reviewed: null` in
the same commit; return to `agreed` on Dave's agreement with
`last-reviewed` pointing at the new review artifact. No trivial-edit
exception, with rationale stated.

### B4 — accept
Finding: Agent-behavior rule is ambiguous and can block legitimate work.
Resolution: Build-gating covers `specs/` documents only. Define "build
against": implement, modify, or test code whose requirements derive from
the spec; citing and discussing are excluded. A task assignment
establishes intent, but the agent must surface the document's status and
obtain one per-task confirmation. Add the companion context-loading rule
for methodology documents (follow the currently agreed methodology; do
not load `draft` methodology docs as governing context).

### B5 — accept
Finding: Supersession stated in present tense by a draft; MANIFEST still
declares the superseded convention.
Resolution: Condition the supersession on agreement. The `MANIFEST.md`
edit and the template-footer revision land in the same change package as
the agreement, so the repo never holds both conventions as canonical.
Stage the package on a branch; the status flip to `agreed` lands at
merge.

### A1 — adopt
Resolution: `last-reviewed` format is `<reviews/path.md> @ <sha>` —
pointer to the review artifact and reviewed commit, not a free-standing
date.

### A2 — adopt
Resolution: The version of a document at reference time is the SHA of
the last commit touching the file.

### A3 — adopt
Resolution: Null ≡ absent, stated under Conditional fields; key present
with null is permitted.

### A4 — adopt
Resolution: `audience` values are `roles/` file slugs plus reserved
`all-roles` and `human`; other values fail enforcement.

### A5 — adopt
Resolution: `agreed` wins repo-wide over `approved`; `OPEN-ITEMS.md`
aligned in `d733604`. (Merged into B2's vocabulary.)

### A6 — adopt
Resolution: Consequence of a `re-review-trigger` firing: the next agent
or human to touch the document flips `status: in-review`.

## Deferred / out of scope

- Per-project enforcement mechanics — tracked in `OPEN-ITEMS.md`.
- Repo-wide migration to frontmatter — tracked in `OPEN-ITEMS.md`.

## Execution notes

Executed prior to this record: the cycle-2 revision of the policy
(`d5e7b2c` on main, including the `d733604` OPEN-ITEMS alignment) and
the staged agreement package (branch `metadata-policy-agreement` @
`0230e11`). The cycle-2 gate review verified the revision faithful to
these decisions.
