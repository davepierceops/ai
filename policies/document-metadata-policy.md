---
status: draft
last-reviewed: null
audience: [all-roles, human]
superseded-by: null
---

# Policy: Document Versioning & Metadata

## Principle

Git is the versioning system. Document metadata carries only semantic
state that git cannot derive. Anything git history already knows — when
a doc changed, who changed it, what changed — is excluded from metadata,
because a duplicate record will drift from git and lie.

## Versioning

- The version of any document is its git SHA. No per-document version
  numbers. No repo-wide version number in `MANIFEST.md`.
- This supersedes the prior "single version declared once in
  `MANIFEST.md`" decision.

## Metadata format

All methodology and spec documents begin with YAML frontmatter, fenced
by `---` lines, before any content.

## Required fields

- `status:` one of `draft | in-review | approved | superseded | deprecated`
  - `superseded` = replaced; a successor exists.
  - `deprecated` = do not use; no replacement.
- `last-reviewed:` `Cycle N, <reviewer-role>, YYYY-MM-DD` — or `null` if
  never reviewed. Records semantic review state git cannot express.
  - `status: approved` requires a non-null `last-reviewed`. Approval
    implies a review happened; an approved doc with no review record
    fails review.
- `audience:` list of roles that consume this document. Enables
  metadata-driven context assembly and lets a role-instance verify a
  doc applies to it.

## Conditional fields

- `superseded-by:` required if and only if `status: superseded`. A path
  or URL to the successor. A superseded doc without a pointer is a
  dangling reference and fails review.

## Optional fields

- `re-review-trigger:` event(s) that force this doc back into review
  (e.g., "any change to human-gate flow"). Per-doc opt-in; owner accepts
  the maintenance burden.

## Excluded fields (do not add)

- Version number — git SHA is the version.
- Last-modified date — git log.
- Author — git blame.
- Changelog — git history.

Rationale: derivable metadata is a second source of truth. It will
drift, and a wrong metadata line is worse than an absent one. This is
the per-document application of the canonical-vs-derived principle in
`policies/source-of-truth-policy.md`.

## Agent behavior

- Agents treat `status` as authoritative: do not build against `draft`
  or `in-review` specs without explicit human direction; never consume
  `superseded` or `deprecated` docs except to follow a `superseded-by`
  pointer.
- Orchestrators may select context by `audience`.
