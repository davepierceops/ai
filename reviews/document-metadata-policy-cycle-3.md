# Gate Review — Cycle 3: policies/document-metadata-policy.md

Reviewer: Spec Reviewer Agent (gate review; not the drafting instance)
Date: 2026-07-21

Cycle 3 is a confirmation pass. Cycle 2 signed off "not ready, but
close," identifying four required changes (B1–B4) and six advisories.
This cycle verifies the cycle-2 directive execution landed as directed
— it does not reopen settled decisions.

## Scope and reviewed state

- Document: `policies/document-metadata-policy.md`, status `in-review`,
  reviewed on `main` at commit **`052559a`** (cycle-2 directive
  execution).
- Staged agreement change package: branch `metadata-policy-agreement` at
  commit **`421fe8a`** (parent chain: `421fe8a` → `0230e11` →
  `d5e7b2c`) — `MANIFEST.md`, `specs/prd-template.md`,
  `specs/trd-template.md`. The branch correctly does not flip the policy
  to `agreed`.
- Confirmed against: `docs/cycles/cycle-2-directive.md` (the triage
  decision record being executed), `reviews/document-metadata-policy-cycle-2.md`
  (the findings being closed), `skills/spec-review-cycle.md`, and the
  full commit history on both refs from the reviewed cycle-2 state.

## Directive execution check

- **B1 (root-doc scope) — resolved as directed.** `operating-model.md`
  and `README.md` added as explicit in-scope paths alongside the six
  globs; `BACKLOG-v2.md` added to the tracker enumeration and
  `MERGE-NOTES-v0.4.md` named as merge history. Matches the directive.
- **B2 (grandfather criterion) — resolved as directed.** The clause now
  states applicability is not judged case-by-case and points at
  `docs/cycles/cycle-2-directive.md` as the canonical disposition
  record. The policy edit is faithful. (A defect in the referenced list
  itself is finding B1 below.)
- **B3 + A6 (status-transition exemption) — resolved as directed.** The
  Revision lifecycle clause landed with the dictated intent: `superseded`
  / `deprecated` transitions and the agreement flip are status
  transitions exempt from the edit-flips-in-review rule; content edits
  alone trigger it; a status-transition commit contains nothing but the
  frontmatter transition, keeping the reviewed-SHA-to-HEAD diff
  auditable. Coexists cleanly with the "no exceptions for trivial edits"
  bullet, which now unambiguously governs content edits only.
- **B4 (decision record) — satisfied by `be2a98f`.** Adds
  `docs/cycles/cycle-1-directive.md` (retroactive, marked as such,
  reviewed state `f96a313` recorded — valid per the skill's SHA
  requirement) and `docs/cycles/cycle-2-directive.md`. The cycle-1
  reconstruction is consistent with the cycle-2 resolution check.
- **A1 (template frontmatter) — resolved as directed.** `421fe8a`
  (child of `0230e11`) touches only the two template files, replacing
  the plain `Status: draft` header with compliant three-field
  frontmatter; skeletons untouched. The branch leaves the policy file
  unchanged since `d5e7b2c`, so main's `052559a` revision prevails at
  merge — no conflict, no dual-canonical window.
- **A5 (enforcement-hook item) — resolved as directed.** New
  `OPEN-ITEMS.md` entry scoped to the B1-amended in-scope set, blocked
  on `agreed`, sequenced with the migration item. Only addition in the
  file.

Deferred items A2–A4 were out of scope this cycle per the cycle-2
directive's execution notes.

## Regression / drift check

Clean within the reviewed range. Main from `d5e7b2c` → `052559a`
comprises exactly three commits: the cycle-2 review artifact
(out-of-scope history per the policy), the B4 directives commit
(`be2a98f`), and the directed edits commit (`052559a`, touching only the
directed hunks). The branch comprises the reviewed `0230e11` plus the A1
commit (`421fe8a`). No undirected changes rode along on either ref. (A
later `BACKLOG-v2.md` note, `32fa15b`, is an out-of-scope tracker edit
and does not touch the policy, templates, or agreement package.)

## New findings

### B1 — The canonical disposition list contradicts the directive's own A1 decision (blocking, record-only)

- **Location:** `docs/cycles/cycle-2-directive.md` (migration
  disposition list vs. A1 resolution); cross-ref the amended grandfather
  clause in the policy.
- The cycle-2 migration disposition list places `specs/prd-template.md`
  and `specs/trd-template.md` in the "enter migration as `agreed`
  (grandfathered)" set, while the same directive's A1 resolution states
  their `agreed` status arrives via the normal gate, not the grandfather
  clause — and their branch frontmatter correctly reads `draft`. Since
  the policy's amended grandfather clause makes that list the canonical
  record, the repo would prescribe two dispositions for the same two
  files; a migration executor could legitimately flip them to `agreed`.
  Neither decision is reopened — both are sound; they collide on two
  entries. **Resolved:** `docs/cycles/cycle-3-directive.md` supersedes
  those two lines, moving the templates from the grandfathered set to the
  `draft` set per cycle-2 A1. The committed cycle-2 directive is history
  and is not edited.

### A1 — Flip-commit sequencing at merge (advisory)

- **Location:** Revision lifecycle (status-transition-commit constraint);
  staged agreement sequence.
- A single merge commit carrying MANIFEST + template edits *and* the
  status flip would violate the policy in the act of enacting it. The
  flip is therefore sequenced as its own commit (policy frontmatter
  only, `last-reviewed` → this artifact + reviewed SHA) immediately
  before the merge, with nothing between. Both the clean-transition rule
  and the staged "flip then merge" sequence hold.

## Sign-off

**Ready for agreement and merge.** All six directed items landed
faithfully; nothing regressed and no undirected changes rode along. The
single blocker (B1) was located entirely in the decision record, not the
documents, and is resolved in `docs/cycles/cycle-3-directive.md` per
cycle-2 A1. On Dave's go, the policy flips to `agreed` in a clean
frontmatter-only commit and the agreement package merges immediately
after.

Reviewed state for the record: `policies/document-metadata-policy.md`
@ `052559a` (main); agreement package @ `421fe8a`
(`metadata-policy-agreement`); decision records `be2a98f` and the
cycle-3 directive.
