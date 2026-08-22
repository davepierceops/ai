# Directive — Pass 1, Cycle 15 revision: reconcile after the merges

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

All paths @ c6bcc5412b5018f80280f975da059c99024f486f.

Documents in scope, with the review triaged for each (the newest reviews/<stem>-cycle-<n>.md for that stem, landed at c6bcc54):
- LEXICON.md
- operating-model.md
- context-sets/spec-and-change-discipline.md
- context-sets/testing-and-verification.md
- boundaries/human-review-boundary.md
- policies/verification-boundary-policy.md
- policies/source-of-truth-policy.md

Rubric: docs/global-context/review-rubric.md @ c6bcc54.

## Standing rule

Every finding in the seven artifacts is accepted and its Fix applied as written, except as decided below. Observations with no Fix produce no edit.

## Decisions

### Single homes
- Evidence-class vocabulary: LEXICON.md only. verification-boundary-policy.md drops its restatement and uses the terms.
- Mock checklist and the release-gap question: context-sets/testing-and-verification.md only, three-valued. verification-boundary-policy.md drops its copy and states in one line that a mocked boundary carries the checklist's answers.
- Canonical source-of-truth order: policies/source-of-truth-policy.md only. operating-model.md's Source of truth section reduces to the rule — specs are canonical, derived artifacts are views, conflict is a hard stop — with the tracker vendor hedge kept there.

### verification-boundary-policy.md filing location
The boundaries/ directory no longer holds boundary declarations. Durable boundaries are declared in the project's TRD or the policy's own declaration section, whichever the policy already names as the declaration home; state that and remove the boundaries/ instruction. Where the policy names neither, declare in the project TRD.

### source-of-truth-policy.md dangling reference
Its rule citing "the document-consistency principle" in spec-and-change-discipline: state the rule inline — a changed fact changes everywhere it appears — or, since Core 13 states it, cut the citation and rely on Core. Cut and rely on Core.

### spec-and-change-discipline S9 residual
Remove the OPEN-ITEMS.md path reference; state the instruction without a path.

### Any Fix that would add a path-shaped reference
Not applied; state the rule inline.

## Execution

1. Fetch origin/main; verify the tree contains c6bcc54 with no later edits to the seven files.
2. Apply every finding and decision. Re-read all seven end to end (Core 13); after deduplication, grep each term moved to its single home across the seven files and confirm it is stated once.
3. Run bin/check-frontmatter --all; stop on any failure other than the README warning.
4. Commit on branch p1-cycle-15-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Per file: one line, what changed. Then branch and SHA. Then any finding not applied as written, with reason.
