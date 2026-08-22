---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Project Setup Requirements

These are adoption preconditions, confirmed before either session kind begins
work in a repo. Confirming them is the human's.

## Purpose

This policy names what must be true about a repository **before** the
methodology governs work in it. They are not day-to-day rules.

Most of them live **outside git** — in the forge's configuration, in local hook
state, in tooling. Git cannot record them and no hook can enforce them, so
they are written down instead.

## Requirements

### 1. Branch protection on the default branch

`main` (or the repo's default branch) is protected:

- **no force-push**
- **no branch deletion**
- **changes land via pull request**
- **bypass disallowed, including for administrators**

The last one carries the others.

This is the structural gate. It is what makes "agents may push and merge"
safe to say: history on the default branch cannot be rewritten or destroyed,
whoever holds the credential.

Branch protection lives in the forge's configuration, not in the repository.
Nothing in the repo can verify it. It is asserted here and confirmed by a
human at adoption.

### 2. Frontmatter enforcement

The repo runs its own frontmatter check over its spec documents at commit time.

The in-scope set is the documents agents consume as governing context —
policies, role documents, context sets, boundary documents, skill documents,
spec documents, vendor documents, and the operating model, the lexicon, and the
readme at the root. State trackers, adapters, and instantiated project
artifacts are out of scope. Adoption of the metadata schema is not optional for
an adopting project's spec documents, and the methodology repo's hooks cannot
reach a project repo, so each project installs its own. (In this repo, the
instance is `bin/install-hooks`, which installs a pre-commit hook running
`bin/check-frontmatter --staged`.)

Hook installation is local state. It is per-clone, it is not recorded in git,
and a fresh clone has no hooks until someone runs the installer. This is a real
gap, not a formality.

### 3. An empty expedited-review log

`reviews/expedited-log.md` exists, even if empty. Without it, the first
expedited agreement fails on a missing review artifact, which reads as a review
problem rather than the setup omission it is.

### 4. A recorded grandfather disposition list, or none

If documents enter migration already marked `agreed`, the repo records a
one-time per-document disposition list naming exactly which ones, and its
adoption record declares where that list lives.

A document absent from the list does not qualify, and **if no disposition list
exists, the grandfather clause does not apply at all**. Recording "none" is a
valid and complete answer.
