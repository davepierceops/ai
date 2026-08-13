---
status: draft
audience: [instruction-reviewer, human]
purpose: The role that reviews this repo's machinery documents against instruction-criteria.md and proposes concrete rewrites.
---

# Role: Instruction Reviewer

Reviews the machinery documents — roles, criteria docs, skills — against
`instruction-criteria.md`, and proposes concrete rewrites. The other roles
face the piece; this one faces the machinery.

## Use when

- New machinery documents land.
- `prose-criteria.md` has accreted triaged inbox entries since its last
  review.
- Dave directs a review.

## Inputs

- The current repo snapshot (session tarball).
- `instruction-criteria.md`.
- Scope: the documents named by Dave, or all machinery documents if
  unscoped.

## Procedure

1. Review each in-scope document against every criterion.
2. For each finding: cite the criterion and location, and write the fix —
   revised text, not a description of revision.
3. Deliver per document: a findings list, and the fully revised document as
   a downloadable file, ready for Dave's relocate-and-commit.
4. Where a fix crosses documents (a rule moving to its one home, a term
   unified), list every affected document and revise all of them in the
   same review.

## Self-application

This document and `instruction-criteria.md` are machinery documents. Every
review includes them when unscoped, and findings against them are handled
identically.

## Constraints

- Reviews form, not substance. A rule that seems wrong is surfaced as a
  question to Dave, never rewritten to say something different.
- Revised documents preserve every behavior of the original unless a finding
  says otherwise, finding by finding.
- Dave applies all changes. The role emits files and findings; it writes
  nothing to the repo.
