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
- `vendors/**`
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
flips to `in-review`, Dave still reads the whole change, and the
agreement still leaves a record that says what was read and when. What
is dropped is the reviewer-gated cycle — the findings round-trip, the
cycle directive, and the per-cycle review artifact.

### Eligibility

Conditions 1–4 are facts about the change. Condition 5 is a human
judgment, and it is the only one:

1. The revision is a **single commit** touching **exactly one** in-scope
   document and no other tracked path. A second file — including a
   tracker or an adapter edited alongside — escalates, and so does a
   revision spread across two commits.
2. The diff is **no more than ten changed lines of document body**,
   added plus deleted — the `+`/`-` lines below the frontmatter's
   closing `---`. Count the body only: the hook rewrites the
   frontmatter on every revision, by two lines or by four depending on
   whether `last-reviewed` was already null. That is a case analysis
   with a wrong answer in it, so there is no constant to subtract and
   no whole-file `--stat` to read; measure the body. The threshold is
   arbitrary, which is the point: a bright line cannot be negotiated
   with, and exceeding it costs a full cycle rather than blocking the
   change.
3. The document does not state a gate, a hard stop, or an enforcement
   rule governing how work is reviewed, agreed, or released. Such a
   document can use this path to weaken the review regime that
   authorizes the path, and a size ceiling cannot see the difference:
   four changed lines take both hard gates out of `operating-model.md`,
   one takes the spec-review gate out of
   `boundaries/human-review-boundary.md`. **The criterion decides, and
   the list below is a floor rather than a boundary.** A document
   stating a gate, a hard stop, or an enforcement rule is ineligible
   whether or not it is named here; being unnamed is not an exemption.
   A gate over work and a gate over documents carry the same hazard —
   a small diff removes a gate — so the class does not turn on which
   of the two a document governs. **When it is unclear whether a
   document states a gate, a hard stop, or an enforcement rule, it is
   ineligible**, mirroring the commit policy's "when in doubt,
   consequential."

   The class includes, at minimum:
   - `policies/document-metadata-policy.md` — this document.
     Enforcement reads its in-scope set from the Scope section above,
     so an edit here can narrow what is enforced, including enforcement
     of this document.
   - `policies/agent-review-policy.md`
   - `policies/commit-and-change-control-policy.md`
   - `policies/source-of-truth-policy.md`
   - `policies/release-readiness-policy.md`
   - `policies/testing-policy.md` — the red-gate.
   - `policies/verification-boundary-policy.md` — the
     boundary-declaration rules.
   - `policies/project-setup-requirements.md` — effective when that document
     reaches `agreed`. It is `draft` today, so it has no expedited revision
     to exclude yet; it is named now because its content is exactly this
     class (branch protection and frontmatter enforcement are the structural
     gates), and naming it later means relying on someone to remember.
   - `roles/spec-reviewer-agent.md`
   - `roles/reviewer-agent.md`
   - `roles/release-manager-agent.md`
   - `roles/skeptic-risk-agent.md` — a review step in the change flow.
   - `skills/spec-review-cycle.md`
   - `skills/release-readiness-review.md`
   - `skills/conversation-retro.md`
   - `boundaries/human-review-boundary.md`
   - `operating-model.md`
   - `README.md`

   These return to `agreed` only through a full cycle. The list is
   normative where it names a document — naming settles the question in
   advance, and a repo that adds a governing document names it here, or
   substitutes its own paths for these. What the list cannot do is bound
   the class: enumeration is not derivable, so it will lag, and the
   criterion is what covers the lag.
4. The document is not under `specs/`. Spec agreement is gated by the
   Spec Reviewer Agent (`roles/spec-reviewer-agent.md`); this path does
   not reach that gate and does not override it.
5. Dave reads the whole diff and agrees it **as-is**: zero findings, no
   dictated wording, no requested change.

Condition 5 is load-bearing, and it is not dressed up as structural.
What this path substitutes for the reviewer-gated cycle is Dave's own
read — not nothing. *Any* finding escalates, however small: the moment
there is a finding there is a revision to review, and whoever wrote it
is not its reviewer. An edit that acquires a finding does not get a
second attempt at this path — it becomes a full cycle per
`skills/spec-review-cycle.md`.

Enforcement checks none of this and cannot. A hook can count staged
files and changed lines; it cannot see whether the diff was read.
Conditions 1–4 bound how much an unread diff could do; condition 5 is
what makes the path a review at all.

The five conditions are necessary, not sufficient. A document may
exclude its own revisions from this path, and one does:
`skills/conversation-retro.md` routes anything a retrospective surfaces
through a full cycle regardless of size.

### The record

Each expedited agreement appends one line to `reviews/expedited-log.md`
naming the document, the reviewed SHA, the date, and what changed;
`last-reviewed` then reads `reviews/expedited-log.md @ <sha>`. The SHA
is what makes that pointer resolve to a single entry — many documents
point at one log, and the entry carrying the cited SHA is the one meant.

The mechanical rules are unchanged in form and weaker in effect, which
is worth stating rather than glossing. `agreed` still requires a
non-null `last-reviewed` naming an artifact that exists — but a
per-cycle artifact had to be *created* to satisfy that check, whereas
the log exists permanently, so its existence no longer evidences that
anything was reviewed. The rule carrying that weight instead: **the SHA
cited in `last-reviewed` must appear in an entry in the log.** A pointer
to a SHA the log does not name is a false claim of review, whether or
not tooling currently catches it. Same commit and same form — an
abbreviated pointer against a full-length entry is the same SHA and a
different string, so a checker either requires both to match
character-for-character or normalizes through `git rev-parse` first.

The log is append-only. Entries are not edited or removed when a
document is later revised or superseded: it records what was agreed and
when, which is history, not current state.

An adopting repo creates an empty `reviews/expedited-log.md` when it
stands up enforcement at project setup. Without it the first expedited
agreement fails on a missing review artifact, which reads as a review
problem rather than the setup omission it is.

### Sequence

1. The content edit commits; the hook flips `status: in-review` and
   `last-reviewed: null`.
2. Dave reads the diff and agrees it as-is.
3. The log entry commits, naming the SHA from step 1.
4. A frontmatter-only status-transition commit flips the document back
   to `agreed`, with `last-reviewed` citing the log and the same step-1
   SHA the entry names.

Steps 3 and 4 stay separate commits so that the status transition
contains nothing but the transition, per the rule above. Step 3 before
step 4, so the entry the pointer resolves to already exists when the
pointer is written.

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
