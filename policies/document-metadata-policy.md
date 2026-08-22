---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Document Versioning & Metadata

This file governs both session kinds; the conditions marked **Dave's** are
decision-session acts.

## Principle

Git is the versioning system. Document metadata carries only semantic
state that git cannot derive. Anything git history already knows — when
a doc changed, who changed it, what changed — is excluded from metadata.

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
- `vendors/**`
- `operating-model.md`
- `README.md`
- `LEXICON.md`

**Out of scope:**

- State and tracker artifacts: `MANIFEST.md`, `OPEN-ITEMS.md`,
  `COLLAB-STATE.md`, `BACKLOG-v2.md`, review artifacts
  (`reviews/**`, `REVIEW-*.md`), merge history (`MERGE-NOTES-v0.4.md`).
  Their status is their content.
- Adapters — the per-tool entry files that point a vendor's harness at
  this methodology, and their configuration directories. These are thin
  deployment targets, and leading YAML may collide with tool
  consumption.
- Instantiated project PRDs/TRDs. These live in project repos, not
  here, so this repo's enforcement does not reach them mechanically —
  but adoption is not optional. Every project applying this methodology
  adopts this metadata schema for its spec documents and stands up its
  own enforcement as part of project setup.

Enforcement (hooks) checks exactly the in-scope set.

## Versioning

- The version of a document at reference time is the SHA of the last
  commit touching the file. No per-document version numbers. No
  repo-wide version number in `MANIFEST.md`.
- Supersession is conditional on agreement: upon this policy reaching
  `agreed`, it supersedes the prior "single version declared once in
  `MANIFEST.md`" decision. The removal of the `Tree version` line from
  `MANIFEST.md` and the revision of the spec-template footers land in
  the same change package as the agreement.

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
  the reviewed commit SHA — or `null` if never reviewed.
  - Format: `<reviews/path.md> @ <sha>`
  - `status: agreed` requires a non-null `last-reviewed`.
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
  `human`. Any other value fails enforcement.

## Conditional fields

- `superseded-by:` required if and only if `status: superseded`. A path
  or URL to the successor.
- Null semantics: null ≡ absent. A key present with value `null` (e.g.,
  `superseded-by: null` on a draft) is permitted and treated as the
  field being absent.

## Revision lifecycle

- When an `agreed` document is edited, the same commit flips
  `status: in-review` and resets `last-reviewed: null`.
- Transitions to `superseded` / `deprecated`, and the agreement flip
  itself, are **status transitions**, not revisions, and are exempt
  from the edit-flips-in-review rule; content edits alone trigger it.
  A status-transition commit contains nothing but the frontmatter
  transition.
- The document returns to `agreed` when Dave agrees the revision, and
  `last-reviewed` points at the new review artifact.
- No exceptions for trivial edits **on the way out**. Every content
  edit to an `agreed` document flips it to `in-review`, whatever its
  size.

## Expedited return to `agreed`

The expedited path drops the reviewer-gated cycle — the findings
round-trip, the cycle directive, and the per-cycle review artifact.

### Eligibility

1. The revision is a **single commit** touching **exactly one** in-scope
   document and no other tracked path. A second file — including a
   tracker or an adapter edited alongside — escalates, and so does a
   revision spread across two commits.
2. The diff is **no more than ten changed lines of document body**,
   added plus deleted — the `+`/`-` lines below the frontmatter's
   closing `---`. Exceeding it costs a full cycle.
3. The document does not state a gate, a hard stop, or an enforcement
   rule governing how work or documents are reviewed, agreed, or
   released. **When it is unclear, it is ineligible.**

   The class includes, at minimum:
   - `policies/document-metadata-policy.md` — this document.
   - `policies/commit-and-change-control-policy.md`
   - `policies/source-of-truth-policy.md`
   - `policies/release-readiness-policy.md`
   - `policies/verification-boundary-policy.md`
   - `policies/project-setup-requirements.md` — effective when that
     document reaches `agreed`.
   - `roles/spec-reviewer-agent.md`
   - `roles/reviewer-agent.md`
   - `roles/release-manager-agent.md`
   - `roles/skeptic-risk-agent.md`
   - `skills/spec-review-cycle.md`
   - `skills/release-readiness-review.md`
   - `skills/conversation-retro.md`
   - `boundaries/human-review-boundary.md`
   - `operating-model.md`
   - `README.md`

   These return to `agreed` only through a full cycle. The list is
   normative where it names a document, and cannot bound the class; a
   repo that adds a governing document names it here, or substitutes
   its own paths for these.
4. The document is not under `specs/`. Spec agreement is gated by the
   Spec Reviewer Agent; this path does not reach that gate and does not
   override it.
5. **Dave's.** Dave reads the whole diff and agrees it **as-is**: zero
   findings, no dictated wording, no requested change.

*Any* finding escalates, however small; an edit that acquires one does
not get a second attempt at this path and becomes a full cycle.
Enforcement checks none of this: conditions 1, 2 and 4 bound how much an
unread diff could do; conditions 3 and 5 are judgments.

The five conditions are necessary, not sufficient. A document may
exclude its own revisions from this path, and the retro skill does.

### The record

Each expedited or doc-only agreement appends one line to
`reviews/expedited-log.md` naming the document, the reviewed SHA, the
date, and what changed — or, where the document is new and nothing
changed, what the document is; `last-reviewed` then reads
`reviews/expedited-log.md @ <sha>`.

`agreed` still requires a non-null `last-reviewed` naming an artifact
that exists, and **the SHA cited in `last-reviewed` must appear in an
entry in the log** — same commit, same form, so a checker matches pointer
to entry character-for-character or normalizes both through `git
rev-parse`. The log is append-only; entries are never edited or removed.

An adopting repo creates an empty `reviews/expedited-log.md` when it
stands up enforcement at project setup.

### Sequence

1. The content edit commits; the hook flips `status: in-review` and
   `last-reviewed: null`.
2. Dave reads the diff and agrees it as-is.
3. The log entry commits, naming the SHA from step 1.
4. A frontmatter-only status-transition commit flips the document back
   to `agreed`, with `last-reviewed` citing the log and the same step-1
   SHA the entry names.

Steps 3 and 4 stay separate commits, so the transition contains nothing
but the transition; step 3 lands before step 4.

## Doc-only cycle

A document co-authored with Dave in the artifact pane reaches `agreed` on his
sign-off, with no separate reviewer. It records as the expedited path does, per
"The record", but carries a co-authored document of **any size, new or
revised**, where the expedited path is capped at a ten-line revision.

The path reaches only documents in the frontmatter in-scope set above.

### Eligible when all five hold

1. **Prose, not a program.** Methodology or governance text in any format; a
   script or executable is out.
2. **Co-authored with Dave in the artifact pane — Dave's.** Drafted together,
   not finished elsewhere and presented for sign-off.
3. **Not a gate document.** Nothing stating a gate, hard stop, or enforcement
   rule over how work is reviewed, agreed, or released — the gate-document class
   defined by the expedited path's condition 3. That class takes the full
   reviewer cycle even when co-authored.
4. **Asked for, and agreed as-is — Dave's.** Dave asks for this path; at least
   one consistency sweep is run; Dave signs off with no open findings. Any
   finding escalates to a full cycle.

   A **consistency sweep** checks the document — and the documents it
   cross-references and that reference it — for any value or cross-reference
   the change has made stale. It extends the within-document consistency check
   already required to the document's neighbours. The co-authoring agent runs
   it before sign-off; "at least one" means the most recent sweep post-dates the
   final edit. Completion is attested by Dave's sign-off, not a separate
   artifact.
5. **Not under `specs/`.** Spec agreement is gated by the Spec Reviewer Agent;
   this path neither reaches that gate nor overrides it.

Enforcement checks none of this either: it verifies the pointer's format, that
the cited SHA resolves to an entry in the log, and that the transition commit is
frontmatter-only — it cannot see whether a document was co-authored, swept, or
asked for. The five conditions are necessary, not sufficient, here as on the
expedited path, and a document may exclude its own revisions from this path.

### Sequence

As the expedited path — content commit, then the log entry naming that SHA, then
a frontmatter-only flip to `agreed`, log entry before flip. One difference: a new
document's content commit lands it at `draft`, where an edit to an already-agreed
document flips it to `in-review`.

A doc-only agreement covers exactly one in-scope document, as the expedited path
does; several documents co-authored in one session are agreed as separate,
sequential agreements. The content commit touches only that document — a
companion tracked path (a `decisions/log.md` entry, an `OPEN-ITEMS.md` update)
lands in its own commit, per the expedited path's "no other tracked path" rule.

## Excluded fields (do not add)

- Version number — git SHA is the version.
- Last-modified date — git log.
- Author — git blame.
- Changelog — git history.

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
