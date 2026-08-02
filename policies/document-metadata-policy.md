---
status: in-review
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

## Scope

Frontmatter applies to documents that agents consume as governing
context; it does not apply to state trackers, adapters, or instantiated
project artifacts.

**In scope (frontmatter required):**

- `policies/**`
- `roles/**`
- `context-sets/**`
- `boundaries/**`
- `skills/**`
- `specs/**`
- `operating-model.md`
- `README.md`

**Out of scope:**

- State and tracker artifacts: `MANIFEST.md`, `OPEN-ITEMS.md`,
  `COLLAB-STATE.md`, `BACKLOG-v2.md`, review artifacts
  (`reviews/**`, `REVIEW-*.md`), merge history (`MERGE-NOTES-v0.4.md`).
  Their status is their content.
- Adapters: `CLAUDE.md`, `AGENTS.md`, `.claude/**`. These are thin
  deployment targets, and leading YAML may collide with tool
  consumption.
- Instantiated project PRDs/TRDs. These live in project repos, not
  here, so this repo's enforcement does not reach them mechanically —
  but adoption is not optional. Every project applying this methodology
  adopts this metadata schema for its spec documents and stands up its
  own enforcement as part of project setup. The exclusion here is about
  where the hook runs, not whether the policy applies.

Enforcement (hooks) checks exactly the in-scope set.

## Versioning

- The version of a document at reference time is the SHA of the last
  commit touching the file. No per-document version numbers. No
  repo-wide version number in `MANIFEST.md`.
- Supersession is conditional on agreement: upon this policy reaching
  `agreed`, it supersedes the prior "single version declared once in
  `MANIFEST.md`" decision. The removal of the `Tree version` line from
  `MANIFEST.md` and the revision of the spec-template footers land in
  the same change package as the agreement — the repo never holds both
  conventions as canonical.

## Metadata format

All in-scope documents begin with YAML frontmatter, fenced by `---`
lines, before any content.

## Required fields

- `status:` one of `draft | in-review | agreed | superseded | deprecated`
  - `agreed` = Dave has agreed this document. This is the repo's
    standing verb; "approved" is not used.
  - `superseded` = replaced; a successor exists.
  - `deprecated` = do not use; no replacement.
- `last-reviewed:` the path to the review artifact in `reviews/` plus
  the reviewed commit SHA — or `null` if never reviewed. Records
  semantic review state by pointing at the record git and the repo
  already hold, rather than duplicating it as a free-standing date.
  - Format: `<reviews/path.md> @ <sha>`
  - `status: agreed` requires a non-null `last-reviewed`. Agreement
    implies a review happened; an agreed doc with no review record
    fails review.
  - **Grandfather clause:** documents agreed before this policy's
    adoption may carry `last-reviewed: null` until their next revision,
    at which point normal rules apply. Applicability is not judged
    case-by-case: at adoption, the adopting repo records a one-time
    per-document disposition list naming which documents enter
    migration as `agreed` under this clause, and its adoption record
    declares where that list lives. A document absent from the list
    does not qualify. If no disposition list exists, the clause does
    not apply and normal rules govern.
- `audience:` list of roles that consume this document. Values are
  `roles/` file slugs plus two reserved values: `all-roles` and
  `human`. Any other value fails enforcement. Enables metadata-driven
  context assembly and lets a role-instance verify a doc applies to it.

## Conditional fields

- `superseded-by:` required if and only if `status: superseded`. A path
  or URL to the successor. A superseded doc without a pointer is a
  dangling reference and fails review.
- Null semantics: null ≡ absent. A key present with value `null` (e.g.,
  `superseded-by: null` on a draft) is permitted and treated as the
  field being absent.

## Revision lifecycle

- When an `agreed` document is edited, the same commit flips
  `status: in-review` and resets `last-reviewed: null`. Metadata
  describes the file's current content, not its history; an edited
  file claiming `agreed` with a past review record is lying. Review
  history is not lost — it lives in `reviews/` and git.
- Transitions to `superseded` / `deprecated`, and the agreement flip
  itself, are **status transitions**, not revisions, and are exempt
  from the edit-flips-in-review rule; content edits alone trigger it.
  A status-transition commit contains nothing but the frontmatter
  transition, so the diff from the reviewed SHA to HEAD remains
  trivially auditable.
- The document returns to `agreed` when Dave agrees the revision, and
  `last-reviewed` points at the new review artifact.
- No exceptions for trivial edits **on the way out**. Every content
  edit to an `agreed` document flips it to `in-review`, whatever its
  size. Enforcement cannot judge meaningfulness, and an escape hatch
  there invites misuse. What can be shortened is the way back.

## Expedited return to `agreed`

A document falsely claiming review currency is expensive. A full review
cycle over a one-line fix is merely tedious. The expedited path
shortens the second without weakening the first: the document still
flips to `in-review`, Dave still reads the change, and `agreed` still
requires a review record that exists and is pointed at. What is dropped
is the reviewer-gated cycle — the findings round-trip, the cycle
directive, and the per-cycle review artifact.

### Eligibility

Every condition is a fact about the change, not a judgment about its
importance:

1. The revision commit touches **exactly one** in-scope document and no
   other tracked path. A second file — including a tracker or an
   adapter edited alongside — escalates.
2. The document is not under `specs/`. Spec agreement is gated by the
   Spec Reviewer Agent (`roles/spec-reviewer-agent.md`); this path does
   not reach that gate and does not override it.
3. The revision is not to this section. The expedited path may not be
   the vehicle for widening, narrowing, or introducing itself.
4. Dave reads the whole diff and agrees it **as-is**: zero findings, no
   dictated wording, no requested change.

Condition 4 is the load-bearing one. *Any* finding escalates, however
small: the moment there is a finding there is a revision to review, and
whoever wrote it is not its reviewer. An edit that acquires a finding
does not get a second attempt at this path — it becomes a full cycle
per `skills/spec-review-cycle.md`.

Eligibility is Dave's to apply, and enforcement does not check it. A
hook can see one staged file; it cannot see whether the diff was read.
The mechanical rules are unchanged: `agreed` still requires a non-null
`last-reviewed` naming an artifact that exists.

### The record

Each expedited agreement appends one line to `reviews/expedited-log.md`
naming the document, the reviewed SHA, the date, and what changed;
`last-reviewed` then reads `reviews/expedited-log.md @ <sha>`. The SHA
is what makes that pointer resolve to a single entry — many documents
point at one log, and the entry carrying the cited SHA is the one meant.

The log is append-only. Entries are not edited or removed when a
document is later revised or superseded: it records what was agreed and
when, which is history, not current state.

### Sequence

1. The content edit commits; the hook flips `status: in-review` and
   `last-reviewed: null`.
2. Dave reads the diff and agrees it as-is.
3. The log entry commits, naming the SHA from step 1.
4. A frontmatter-only status-transition commit flips the document back
   to `agreed` with `last-reviewed` pointing at the log.

Steps 3 and 4 stay separate commits so that the status transition
contains nothing but the transition, per the rule above.

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

- The build-gating rule covers `specs/` documents (PRDs/TRDs) only.
  "Build against" means: implement, modify, or test code whose
  requirements derive from that spec. Citing or discussing a draft
  spec is not building against it.
- Do not build against a `draft` or `in-review` spec without explicit
  human confirmation. A task assignment referencing the spec
  establishes intent, but the agent must state the spec's current
  status and receive confirmation before proceeding. Confirmation is
  per-task, not per-session — one acknowledgment covers the whole
  task, not each action within it.
- Methodology documents (policies, roles, context-sets, boundaries,
  skills) are governed by context loading, not the build-gating rule:
  agents follow the currently agreed methodology; a `draft` methodology
  document is not loaded as governing context unless the human
  explicitly directs it for a specific task.
- Never consume `superseded` or `deprecated` docs except to follow a
  `superseded-by` pointer.
- Orchestrators may select context by `audience`.
