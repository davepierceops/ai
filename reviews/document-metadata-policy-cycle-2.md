# Gate Review — Cycle 2: policies/document-metadata-policy.md

Reviewer: Spec Reviewer Agent (gate review; not the drafting instance)
Date: 2026-07-21

## Scope and reviewed state

- Document: `policies/document-metadata-policy.md`, status `in-review`,
  reviewed on `main` at commit **`d5e7b2c`** (cycle-2 revision).
- Staged agreement change package: branch `metadata-policy-agreement` at
  commit **`0230e11`** (parent: `d5e7b2c`) — `MANIFEST.md`,
  `specs/prd-template.md`, `specs/trd-template.md`. Reviewed as part of
  this gate because the policy's conditional-supersession clause couples
  these edits to the agreement change package. The branch correctly does
  **not** flip the policy to `agreed`; that lands at merge with the
  final review artifact's path and SHA.
- Cross-checked against: `policies/source-of-truth-policy.md`,
  `OPEN-ITEMS.md` (at `d5e7b2c`, including the `d733604` alignment
  commit), `skills/spec-review-cycle.md`, `REVIEW-v0.4.md`, and a fresh
  repo-wide survey of every `Status:` line.

## Cycle-1 resolution check

### Blocking findings

- **B1 (scope undefined) — resolved, with a residual gap.** The new
  Scope section defines the in-scope set as six directory globs
  (`policies/**`, `roles/**`, `context-sets/**`, `boundaries/**`,
  `skills/**`, `specs/**`) and explicitly excludes trackers, adapters,
  and instantiated project artifacts, while making project adoption of
  the schema mandatory with per-project enforcement (tracked in
  OPEN-ITEMS via `d733604`). All boundary cases cycle-1 listed are now
  decided. A hook can be written and the migration scoped — except for
  the root-level files neither list covers; see new finding **B1** below
  (a case cycle-1's inventory also missed).
- **B2 (vocabulary/migration) — substantially resolved.** Vocabulary is
  now `draft | in-review | agreed | superseded | deprecated`; `agreed`
  is declared the repo's standing verb and the repo-wide survey confirms
  no live use of "approved" outside historical review artifacts and the
  policy's own mention. The template-footer contradiction (`agreed` +
  `v<x.y>`) is resolved on the branch: footers removed, skeletons carry
  frontmatter. `placeholder` (`.claude/**`) and `active`
  (`COLLAB-STATE.md`) are resolved by the scope exclusions. `stable` →
  `agreed` is resolved in principle by the grandfather clause, but the
  clause's applicability criterion is undefined and the mapping itself
  is recorded nowhere canonical; see new findings **B2** and **B4**.
- **B3 (revision lifecycle) — resolved.** The Revision lifecycle section
  specifies: editing an `agreed` doc flips `status: in-review` and
  resets `last-reviewed: null` in the same commit; return to `agreed` on
  Dave's agreement with `last-reviewed` pointing at the new artifact; no
  trivial-edit exception, with rationale. Matches the triage decision.
  The rule as written collides with the supersession transition; see new
  finding **B3**.
- **B4 (agent-behavior ambiguity) — resolved.** Build-gating now covers
  `specs/` only; "build against" is defined (implement/modify/test code
  whose requirements derive from the spec; citing and discussing
  excluded); a task assignment establishes intent but the agent must
  surface status and get one per-task confirmation. Two agents reading
  this independently will apply it the same way. The companion
  context-loading rule for methodology docs is well-formed but its
  effect depends on the unresolved grandfather criterion (new **B2**):
  until that is decided, "follow the currently agreed methodology"
  describes a corpus of approximately one document.
- **B5 (supersession by a draft / MANIFEST conflict) — resolved.**
  Supersession is now conditional on agreement, and the policy states
  the MANIFEST edit and template-footer revision land in the same change
  package "the repo never holds both conventions as canonical." The
  branch stages exactly those edits, based on `d5e7b2c`, and leaves the
  status flip for merge time. No dual-canonical window exists in the
  staged sequence. Consistent with `policies/source-of-truth-policy.md`.

### Advisory findings

- **A1 (last-reviewed as date) — adopted.** Format is now
  `<reviews/path.md> @ <sha>`, pointing at the record the repo already
  holds instead of duplicating a date. Aligns with
  `skills/spec-review-cycle.md`'s reviewed-SHA recording.
- **A2 (SHA imprecision) — adopted.** "The version of a document at
  reference time is the SHA of the last commit touching the file."
- **A3 (null semantics) — adopted.** "Null ≡ absent" is stated under
  Conditional fields.
- **A4 (audience vocabulary) — adopted.** Values are `roles/` file slugs
  plus reserved `all-roles` and `human`; other values fail enforcement.
  The policy's own frontmatter and the branch skeletons validate against
  this. (Project-repo validation of slugs is unspecified; advisory A2
  below.)
- **A5 (approved vs. agreed) — adopted.** `agreed` wins repo-wide;
  OPEN-ITEMS was aligned in `d733604`.
- **A6 (re-review-trigger consequence) — adopted.** Consequence defined:
  the next agent or human to touch the document flips
  `status: in-review`.

All five cycle-1 blocking findings are resolved as triaged, and all six
advisories are dispositioned (all adopted). The findings below are new.

## Agreement change package review (branch @ `0230e11`)

- `MANIFEST.md`: drops `Tree version: v0.5` and its own `Status:` line
  (consistent — MANIFEST is an out-of-scope tracker whose "status is its
  content"), defers versioning to the policy, registers
  `policies/document-metadata-policy.md` in the document list (it was
  previously unregistered), and marks the version headings as historical
  record. Consistent with the policy text.
- `specs/prd-template.md` / `specs/trd-template.md`: skeleton footers
  (`Status: <draft|agreed> v<x.y>  Agreed by:`) removed; skeletons now
  open with compliant frontmatter (`status: draft`,
  `last-reviewed: null`, `audience: [all-roles, human]`) and a preamble
  citing the policy. The `v<x.y>` per-document version number is gone.
  Consistent with the policy — with one transitional inconsistency in
  the template files' own headers (advisory A1 below).
- Sequencing: `0230e11` is a child of `d5e7b2c`; merging the branch plus
  the status flip lands atomically after agreement. Correct.

## New findings

### B1 — Root-level governing documents fall in neither scope set (blocking)

- **Location:** Scope section; cross-ref `OPEN-ITEMS.md` (migration
  item), `operating-model.md:3`, `README.md:3`
- The scope principle says frontmatter applies to "documents that agents
  consume as governing context," but the in-scope set is six directory
  globs — and `operating-model.md` and `README.md` live at root, in
  neither the in-scope globs nor the out-of-scope enumeration. Both are
  required reading per the adapters and are unambiguously governing
  context; `operating-model.md` is the spine document. As written, the
  hook ("checks exactly the in-scope set") ignores them, the migration
  item ("convert every existing doc's plain `Status:` line") includes
  them, and the policy decides neither reading. `BACKLOG-v2.md` and
  `MERGE-NOTES-v0.4.md` are likewise undispositioned (presumably
  trackers/history, but the enumeration should say so). Cycle-1's B1
  inventory also missed these files; this is a completeness gap in both
  the finding and the fix. Needs Dave's judgment: either add the root
  governing docs to the in-scope set (as explicit paths) or exclude
  them explicitly with a stated rationale.

### B2 — The grandfather clause has no applicability criterion (blocking)

- **Location:** Required fields, grandfather clause; Agent behavior,
  context-loading rule; cross-ref `REVIEW-v0.4.md:121-123, 178-181`
- The clause covers "documents agreed before this policy's adoption,"
  but nothing defines which documents those are. The repo's `Status:`
  lines say `draft` for every methodology document except
  `context-sets/base.md` (`stable`) — yet `REVIEW-v0.4.md` records the
  spine docs as "**approved**" in its per-file table while its own
  sign-off checkboxes ("Spine reviewed and approved", "Tree approved as
  v0.4") are unchecked. So the repo's own record is ambiguous about
  what has been agreed, and the triage decision's `stable → agreed`
  mapping is recorded nowhere in the repo (see B4). The consequence is
  not cosmetic: the context-loading rule says agents follow "the
  currently agreed methodology" and must not load `draft` methodology
  docs as governing context. If migration carries the corpus over as
  `draft`, the policy forbids agents from following the operating model
  itself — the exact paradox cycle-1's B4 flagged, relocated. Needs
  Dave's explicit criterion or a per-document disposition list for
  migration: which existing documents enter migration as `agreed`
  (grandfathered, `last-reviewed: null`) and which remain genuinely
  `draft`.

### B3 — The revision-lifecycle rule makes supersession of an agreed document impossible (blocking)

- **Location:** Revision lifecycle, first bullet; Conditional fields
  (`superseded-by`)
- "When an `agreed` document is edited, the same commit flips
  `status: in-review` and resets `last-reviewed: null`" — with "no
  exceptions." Superseding or deprecating an agreed document requires
  editing it (to set `status: superseded` + `superseded-by`). Read
  literally, that edit must flip the document to `in-review`, so an
  agreed document can never legally reach `superseded` or `deprecated`.
  Two rules prescribe different outcomes for the same commit; two
  agents can read it either way, which is the failure class this policy
  exists to eliminate. One clause fixes it: state that transitions to
  `superseded`/`deprecated` (and the agreement flip itself) are status
  transitions, not revisions, and are exempt from the flip rule —
  content edits alone trigger it.

### B4 — Cycle-1 triage decisions have no committed decision record (blocking, process)

- **Location:** process; `skills/spec-review-cycle.md` (Directive step,
  Hard constraints); absence of `docs/cycles/` or any `*directive*`
  file in the repo
- This review cycle runs under `skills/spec-review-cycle.md`, which
  makes the committed cycle directive the decision record and audit
  trail ("the directives are the decision record"; "a directive without
  SHAs is invalid"). No cycle-1 directive exists anywhere in the repo.
  The seven triage decisions the revision implements — including the
  `stable → agreed` mapping, which appears in no canonical document —
  exist only in chat history. The revision itself is faithful to those
  decisions (verified against the decision summary supplied to this
  review), but the audit chain the policy establishes (`last-reviewed`
  → review artifact → reviewed SHA) has a hole at the triage step. Fix
  before agreement: commit the cycle-1 directive (and cycle-2's, when
  triaged) at the skill's prescribed location, or an equivalent
  canonical record of the decisions.

### A1 — The templates the package edits remain non-compliant with the policy it enacts (advisory)

- **Location:** branch `0230e11`, `specs/prd-template.md:3`,
  `specs/trd-template.md:3`
- Both template files are in-scope (`specs/**`), and the agreement
  package edits them — yet they still open with a plain
  `Status: draft` line and no frontmatter. At merge, the repo's newly
  agreed policy is violated by the two in-scope files the agreement
  package touched. General migration is deliberately a separate open
  item, but since these files are already being edited in the package,
  adding their frontmatter there is nearly free; otherwise, state that
  transitional non-compliance until migration is accepted.

### A2 — `audience` slug validation is undefined for project repos (advisory)

- **Location:** Required fields (`audience:`); Scope (project adoption
  mandate)
- Audience values are "`roles/` file slugs" — of this repo. Project
  repos must adopt the schema and stand up enforcement, but a project
  hook cannot validate slugs against a `roles/` directory it does not
  have. State whether projects validate against this repo's roles,
  their own role set, or reserved values only. Fold into the
  per-project enforcement open item.

### A3 — `last-reviewed` hard-codes the `reviews/` location (advisory)

- **Location:** Required fields (`last-reviewed:` format)
- The field is defined as "the path to the review artifact in
  `reviews/`," which projects adopting the schema may not have —
  `skills/spec-review-cycle.md` puts project cycle artifacts under
  `docs/cycles/`, and project reviewer findings have no prescribed
  home. Either relax the definition to "path to the review artifact"
  or state the project-repo convention in the setup guidance.

### A4 — `reviews/` is unregistered in MANIFEST and TREE (advisory)

- **Location:** `MANIFEST.md` (document list, both sides of the
  branch); `TREE.txt`
- `TREE.txt` predates `reviews/` and does not list it; MANIFEST's
  assembly record registers the policy (on the branch) but says nothing
  about review artifacts. Given registration is a maintained property
  (v0.5 explicitly "registered missing files"), decide whether
  `reviews/` contents are registered and regenerate `TREE.txt` at the
  next checkpoint.

### A5 — Nothing tracks standing up this repo's own enforcement hook (advisory)

- **Location:** Scope ("Enforcement (hooks) checks exactly the in-scope
  set"); `OPEN-ITEMS.md`
- OPEN-ITEMS tracks per-project enforcement and the migration, but no
  item tracks building the methodology repo's own hook that the Scope
  section presumes. Add it (or fold into the migration item) so the
  enforcement claim doesn't dangle.

### A6 — Auditability of the agreement flip commit (advisory)

- **Location:** Revision lifecycle; Required fields (`last-reviewed:`)
- After agreement, the last commit touching the file (the flip commit)
  necessarily differs from the SHA recorded in `last-reviewed` (the
  reviewed revision). That is by design, but verifying "the agreed
  content is the reviewed content" requires the flip commit to contain
  nothing but the frontmatter transition. State that constraint — it
  makes the reviewed-SHA-to-HEAD diff trivially auditable and interacts
  with the B3 fix (status transitions vs. revisions).

## Required changes (before Dave agrees)

1. Disposition the root-level documents — `operating-model.md`,
   `README.md`, `BACKLOG-v2.md`, `MERGE-NOTES-v0.4.md` — explicitly in
   or out of scope (B1). Dave's call.
2. Define the grandfather clause's applicability criterion: which
   existing documents enter migration as `agreed` (B2). Dave's call;
   a per-document list is acceptable.
3. Exempt status transitions (`superseded`, `deprecated`, the agreement
   flip) from the edit-flips-in-review rule (B3). Drafting fix.
4. Commit the cycle-1 (and subsequently cycle-2) triage directive or an
   equivalent canonical decision record (B4). Process fix.

## Advisory items

A1–A6 above. A1 (template frontmatter in the agreement package) is worth
taking now since the files are already in the package's diff; the rest
can ride the migration and setup-guidance items.

## Items requiring Dave's judgment

- Root-document scope disposition (B1).
- The grandfather criterion / migration disposition list (B2).
- Whether the agreement package also carries the templates' own
  frontmatter (A1) or accepts transitional non-compliance.

## Sign-off

**Not ready for Dave's agreement — but close.** All five cycle-1
blocking findings are resolved as triaged, all six advisories are
adopted, and the staged agreement package is consistent with the policy
and correctly sequenced (no dual-canonical window). The remaining
blockers are narrower than cycle-1's: two scope/migration decisions
only Dave can make (B1, B2), a one-clause internal contradiction in the
revision lifecycle (B3), and a missing committed decision record that
the repo's own review skill mandates (B4). Resolve the four required
changes and resubmit; absent surprises, cycle 3 should be a
confirmation pass.

Reviewed state for the record: `policies/document-metadata-policy.md`
@ `d5e7b2c` (main); agreement package @ `0230e11`
(`metadata-policy-agreement`).
