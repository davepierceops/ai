# Gate Review — Cycle 1: policies/document-metadata-policy.md

Reviewer: Spec Reviewer Agent (gate review, not a continuity scan; not the
drafting instance)
Date: 2026-07-21

## Scope

- Document: `policies/document-metadata-policy.md`, status `draft`,
  reviewed at commit `f96a313` (file introduced in `cbddf79`, unchanged
  since).
- Cross-checked against: `policies/source-of-truth-policy.md`,
  `MANIFEST.md` (v0.5, at `f96a313`), `skills/spec-review-cycle.md`,
  `OPEN-ITEMS.md`, and the repo-wide survey of existing `Status:` lines
  (all policies, roles, context-sets, boundaries, skills, specs, root
  docs, `.claude/` adapters).
- Spine-specific gate checks (NFR instantiation, journey tracing, SLOs)
  do not apply; this is a policy document.

Two claims verified up front:

- **Source-of-truth claim holds.** The policy's framing — derivable
  metadata is a second source of truth that will drift — is a faithful
  per-document application of the canonical-vs-derived principle in
  `policies/source-of-truth-policy.md`. Cross-reference is sound.
- **MANIFEST supersession target exists but is still live.** `MANIFEST.md`
  today declares `Tree version: v0.5` and states "the tree version above
  is the only version" — the convention this policy claims to supersede
  was used (v0.4 → v0.5 bump) in the same commit series that introduced
  this policy. See finding B5.

## Findings

### B1 — Scope of applicability is undefined (blocking)

- **Location:** Metadata format ("All methodology and spec documents")
- The policy implies mechanical enforcement (hooks checking frontmatter
  presence and field rules), but "methodology and spec documents" does
  not decide the boundary cases that actually exist in this repo:
  `MANIFEST.md`, `OPEN-ITEMS.md`, `TREE.txt`, `COLLAB-STATE.md`, review
  artifacts (`reviews/`, `REVIEW-*.md`), cycle directives, adapter files
  (`CLAUDE.md`, `AGENTS.md`, `.claude/**` — note adapters may have
  tool-consumption constraints on leading YAML), and instantiated
  project PRDs/TRDs (which `MANIFEST.md` explicitly carves out of the
  current convention; this policy is silent on whether it inherits that
  carve-out). A hook cannot be written, and the migration tracked in
  `OPEN-ITEMS.md` cannot be scoped, until the file set is defined.
  Needs Dave's judgment.

### B2 — Status vocabulary contradicts existing canonical usage (blocking)

- **Location:** Required fields, `status:` vocabulary
- The vocabulary `draft | in-review | approved | superseded | deprecated`
  does not cover statuses canonically in use today, and no migration
  mapping is given:
  - `specs/prd-template.md:127` and `specs/trd-template.md:166` embed a
    footer `Status: <draft|agreed> v<x.y>  Agreed by:` — `agreed` is not
    in the vocabulary, and `v<x.y>` is a per-document version number the
    policy's Excluded-fields section forbids. The canonical templates
    and the policy directly contradict each other.
  - `context-sets/base.md:10` is `stable` — unmapped. Mapping it to
    `approved` collides with "approved requires non-null last-reviewed"
    (no formal review record exists), so the migration outcome is
    undefined: fabricate a review record, or demote the repo's only
    stable doc.
  - `placeholder` (`.claude/*/README.md`) and `active`
    (`COLLAB-STATE.md`) — unmapped; may be resolved by B1's scope
    decision instead, but one of the two must decide them.
  Needs Dave's judgment on the mapping table (and on whether the
  template footers are revised under this policy or carved out).

### B3 — Lifecycle is incomplete: revising an approved document (blocking)

- **Location:** Required fields (`status:`, `last-reviewed:`)
- Revision of an agreed document is a first-class flow
  (`roles/spec-reviewer-agent.md` gates "any revision to a spec
  document"), but the policy does not say what `status` a previously
  `approved` doc holds while a revision is in flight, nor whether
  `last-reviewed` persists (now describing a different content state)
  or resets to null. An edited file still reading `approved:
  last-reviewed: Cycle 2 ...` is exactly the metadata-lying-about-state
  failure the Principle section warns against — applied to the policy's
  own fields. The agent-behavior rules key off `status`, so this gap
  has behavioral consequences.

### B4 — Agent-behavior rule is ambiguous and can block legitimate work (blocking)

- **Location:** Agent behavior, first bullet
- "Do not build against `draft` or `in-review` specs without explicit
  human direction" is underspecified on three axes:
  1. Does "specs" mean only `specs/` (PRD/TRD), or every document
     carrying frontmatter? If the latter, note that today every
     methodology doc except `base.md` is `draft` — a literal reading
     lets an agent refuse to follow the operating model itself, or
     demand blanket authorization every session.
  2. "Build against" is undefined (implement code from? cite? load as
     context?).
  3. "Explicit human direction" is undefined — does Dave assigning a
     task that references the draft spec qualify, or is a separate
     acknowledgment required?
  As written, the rule cannot be applied consistently by two agents
  reading it independently.

### B5 — Supersession stated in present tense by a draft; MANIFEST still declares the superseded convention (blocking)

- **Location:** Versioning ("This supersedes the prior 'single version
  declared once in MANIFEST.md' decision"); `MANIFEST.md:3-9`
- A draft cannot supersede a standing decision — per this policy's own
  agent-behavior section, drafts aren't even to be built against. Yet
  the text asserts "No repo-wide version number in `MANIFEST.md`" as a
  live rule while `MANIFEST.md` declares `Tree version: v0.5` and calls
  it "the only version." If Dave agrees the policy as written without
  the MANIFEST edit landing in the same change, the repo immediately
  holds two contradicting canonical documents — a hard stop under
  `policies/source-of-truth-policy.md`. The MANIFEST edit is tracked in
  `OPEN-ITEMS.md` ("blocked on the policy reaching approved"), but the
  coupling is not stated in the policy. Fix is small: condition the
  supersession ("upon approval of this policy"), and make the MANIFEST
  edit part of the same change package as approval.

### A1 — `last-reviewed` date vs. the excluded-fields rationale (advisory)

- **Location:** Required fields (`last-reviewed:`); Excluded fields
- Direct answer to the gate question: "approved requires non-null
  last-reviewed" and the excluded-fields list can both hold — no formal
  conflict; `last-reviewed` is none of the four excluded items. But the
  `YYYY-MM-DD` component is a hand-maintained date, and with `reviews/`
  becoming the standing home for review artifacts (per `OPEN-ITEMS.md`,
  established by this very file), review history becomes derivable from
  the repo — putting `last-reviewed` in tension with the policy's own
  "derivable metadata will drift and lie" rationale. Consider having
  `last-reviewed` point at the review artifact path and/or reviewed
  commit SHA (which `skills/spec-review-cycle.md` already records)
  rather than a free-standing date.

### A2 — "The version of any document is its git SHA" is imprecise (advisory)

- **Location:** Versioning
- Documents don't have SHAs; commits do. Specify: the version of a
  document at reference time is the SHA of the referencing commit (or
  the last commit touching the file). `skills/spec-review-cycle.md`
  already operationalizes this as "reviewed commit SHA per document" —
  align the wording so a hook or directive validator has one definition.

### A3 — `superseded-by` iff-rule vs. the policy's own frontmatter (advisory)

- **Location:** Conditional fields; the document's own frontmatter
- The field is "required if and only if `status: superseded`," yet the
  policy's own frontmatter carries `superseded-by: null` while `draft`.
  A strict hook must know whether key-present-with-null counts as
  absent. State it (recommended: null ≡ absent; presence with null is
  permitted).

### A4 — `audience:` has no defined value vocabulary (advisory)

- **Location:** Required fields (`audience:`)
- The policy's own frontmatter uses `all-roles` and `human`, neither of
  which is defined anywhere, and role names are not tied to `roles/`
  slugs. For "metadata-driven context assembly" to be more than
  freetext, define the value space (role file slugs plus reserved
  values) — otherwise the field drifts and is unenforceable.

### A5 — "approved" vs. the repo's standing verb "agreed" (advisory)

- **Location:** Required fields (`status:` vocabulary), repo-wide
- The operating model, spec templates, and role docs consistently say
  Dave "agrees" a document; this policy introduces `approved` for the
  same state (B2 covers the template collision specifically). Pick one
  term or state the equivalence, or the two words will read as two
  different gates.

### A6 — `re-review-trigger` has no defined consequence (advisory)

- **Location:** Optional fields
- The field names events that "force this doc back into review," but
  nothing says what happens when one fires: does `status` flip to
  `in-review`, and who is responsible for noticing the event? Optional
  field, so advisory — but as written it is a wish, not a rule.

## Required changes (before Dave agrees)

1. Define the in-scope file set precisely enough for a hook and for the
   migration (B1) — this is a judgment call for Dave, not the drafter.
2. Provide the status migration mapping for `agreed`, `stable`,
   `placeholder`, `active`, and resolve the spec-template footer
   contradiction (`agreed` + `v<x.y>`), including whether instantiated
   project PRDs/TRDs inherit MANIFEST's carve-out (B2).
3. Specify the revision lifecycle: status of an approved doc under
   revision, and `last-reviewed` persistence/reset semantics (B3).
4. Tighten the agent-behavior rule: define which documents it covers,
   what "build against" means, and what counts as explicit human
   direction (B4).
5. Condition the MANIFEST supersession on approval and couple the
   MANIFEST edit to the approval change package (B5).

## Advisory items

A1–A6 above. None block agreement individually, but A1 (last-reviewed
pointing at review artifacts/SHAs instead of a bare date) is worth
deciding now, since it changes the required-field format that every
migrated document will carry.

## Items requiring Dave's judgment

- The scope boundary (B1) and the status migration mapping (B2) are
  policy decisions, not drafting fixes.
- Terminology: "agrees" vs. "approved" (A5) — one word should win
  repo-wide.
- Sequencing: whether policy approval and the MANIFEST version-line
  removal land as one change package (B5).

## Sign-off

**Not ready for Dave's agreement.** The document is well-structured, its
sections are substantively answered, its rationale chain is intact, and
its central claim — that it applies the source-of-truth policy's
canonical-vs-derived principle per document — holds. But five blocking
findings remain: the enforcement scope is undefined (B1), the schema
contradicts canonical spec templates and leaves existing statuses
unmappable (B2), the most common lifecycle transition is unspecified
(B3), the agent-behavior rule can be read to block routine work (B4),
and agreeing the policy as written creates an immediate hard-stop
conflict with `MANIFEST.md` (B5). Resolve the five required changes and
resubmit for a cycle-2 gate check.
