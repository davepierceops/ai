---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Project Setup Requirements

## Purpose

This policy names what must be true about a repository **before** the
methodology governs work in it. These are adoption preconditions, not
day-to-day rules.

Most of them live **outside git** — in GitHub's configuration, in local hook
state, in tooling. Git cannot record them and no hook can enforce them, so
they are written down instead. That is the whole reason this document exists.

## The constraint on this document

**This list stays short.** It is a set of adoption preconditions, not a
project-setup manual. If it grows toward twenty items, that is a signal the
approach is wrong — not a reason for a longer list. Something that can be
enforced by a hook, derived from git, or checked by a script belongs there
instead of here.

## Requirements

### 1. Branch protection on the default branch

`main` (or the repo's default branch) is protected:

- **no force-push**
- **no branch deletion**

This is the structural gate. It is what makes "agents may push and merge"
safe to say: history on the default branch cannot be rewritten or destroyed,
whoever holds the credential.

Branch protection lives in GitHub's configuration, not in the repository.
Nothing in the repo can verify it. It is asserted here and confirmed by a
human at adoption.

*(Open: whether protection additionally requires a PR, required reviews, or
required status checks. Those are gates on the merge event, and this
methodology's human gate is the release decision, not the merge — see
`policies/commit-and-change-control-policy.md`. Left undecided pending the
push/merge posture reaching a canonical home.)*

### 2. Frontmatter enforcement

The repo stands up its own frontmatter enforcement for the in-scope document
set defined in `policies/document-metadata-policy.md`.

That policy mandates the metadata schema for every adopting project's spec
documents, and states plainly that adoption is not optional. But the
methodology repo's hooks cannot reach a project repo. Each project installs
its own — in this repo, `bin/install-hooks` installs the pre-commit hook that
runs `bin/check-frontmatter --staged`.

Hook installation is local state. It is per-clone, it is not tracked, and a
fresh clone has no hooks until someone runs the installer. This is a real
gap, not a formality.

### 3. An empty expedited-review log

`reviews/expedited-log.md` exists, even if empty.

`policies/document-metadata-policy.md` requires this explicitly: without it,
the first expedited agreement fails on a missing review artifact, "which
reads as a review problem rather than the setup omission it is."

### 4. A recorded grandfather disposition list, or none

If documents enter migration already marked `agreed`, the repo records a
one-time per-document disposition list naming exactly which ones, and its
adoption record declares where that list lives.

Per `policies/document-metadata-policy.md`: a document absent from the list
does not qualify, and **if no disposition list exists, the grandfather clause
does not apply at all**. Recording "none" is a valid and complete answer.

## Discharge note

This document, when agreed, discharges the `OPEN-ITEMS.md` entry
"Per-project frontmatter enforcement as a project-setup step" — that item
asked for exactly requirement 2 above, and Q1c decided it and the
startup-assumptions document are one document.

The OPEN-ITEMS entry is **not removed yet**. It is discharged when this
document reaches `agreed`, not when it is drafted.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.1) executing Q1c.
Nothing here is agreed.
