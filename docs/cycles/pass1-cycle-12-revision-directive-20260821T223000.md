# Directive — Pass 1, Cycle 12 revision: context-sets and boundaries

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

All paths @ cceef9a28c5e5d5dd312a36d0554f3471e05f85b.

Reviews triaged (one per document in scope):
- reviews/base-cycle-1.md
- reviews/ai-native-engineering-cycle-4.md
- reviews/collab-workflow-cycle-2.md
- reviews/production-grade-software-cycle-1.md
- reviews/spec-and-change-discipline-cycle-6.md
- reviews/testing-and-verification-cycle-1.md
- reviews/human-review-boundary-cycle-1.md
- reviews/live-integration-boundaries-cycle-1.md
- reviews/mocked-boundaries-cycle-1.md
- reviews/vendor-tooling-boundary-cycle-2.md

Merge targets (edited only to receive merged content and the decisions below): operating-model.md, LEXICON.md, policies/verification-boundary-policy.md, policies/source-of-truth-policy.md, docs/global-context/decision-layer.md.

Rubric: docs/global-context/review-rubric.md @ cceef9a. Every file touched leaves conformant to all ten criteria.

## Standing rule for this directive

Every finding in the ten artifacts is accepted and its Fix applied as written, unless a decision below overrides it. Observations with no Fix produce no edit. Where a Fix says the matter is Dave's, the decision below is his answer.

## Dispositions (Dave, 2026-08-21)

- context-sets/base.md — merge-into. Evidence-class vocabulary (mock-, contract-, live-, browser-, production-verified; unverified; deferred verification; accepted risk) goes to LEXICON.md as a new section "Evidence classes". The response-shape content goes to operating-model.md. Everything else in base.md is restated Core and is cut. Delete the file.
- context-sets/ai-native-engineering.md — merge-into operating-model.md per its review. Delete the file.
- context-sets/collab-workflow.md — retire. Carry the multi-document sequencing (one document at a time; "ship" advances one) only if decision-layer rule 10 does not already state it — it does; carry nothing. Delete the file.
- context-sets/production-grade-software.md, spec-and-change-discipline.md, testing-and-verification.md — retain-with-changes per their reviews.
- boundaries/live-integration-boundaries.md, mocked-boundaries.md — merge-into policies/verification-boundary-policy.md: any sentence stating a rule the policy lacks moves there; the contradicting YAML schema in mocked-boundaries is discarded, the policy's schema stands. Delete both files.
- boundaries/vendor-tooling-boundary.md — merge-into policies/source-of-truth-policy.md: the five-step Required discipline moves there, reworded per N2 (no product names). Delete the file.
- boundaries/human-review-boundary.md — retain-with-changes per its review.

## Decisions overriding or settling a Fix

### OPEN-ITEMS.md vs decision-layer rule 9 (collab-workflow C4 and any sibling finding)
OPEN-ITEMS.md stays. Decision-layer rule 9 gains one sentence: "A loose-end tracker is a record, not derived state." Context sets keep their OPEN-ITEMS instruction where it is not a restatement of that tracker's own header.

### bin/bundle closure edges (any finding citing it)
Criterion 3 proceeds as written. bin/bundle's path-following closure mode is retired, replaced in Pass 2 by audience selection. No edit to bin/ here. Append one line to OPEN-ITEMS.md under its open section recording this.

### "error budget" (every retired-term finding on it)
Not a use of the retired term. Add to LEXICON.md's Track retirement entry a carve-out matching Prompt's: "error budget" and similar SRE compounds are not the retired term.

### spec-and-change-discipline step range (its blocking finding)
Fix the range so quality review is in the continuing flow; cross-check against operating-model.md's current step numbering after the merges land.

### Any Fix that would add a path-shaped reference
Not applied; state the rule inline instead.

## Execution

1. Fetch origin/main; verify the tree contains cceef9a with no later edits to the ten files or the five merge targets.
2. Apply merges first, then deletions, then in-place edits, then the decisions above. For each deleted file, grep the whole repository (excluding reviews/, docs/cycles/, retros/, decisions/) for its path and report every remaining reference; do not edit files outside scope to remove them — list them.
3. Re-read every touched file end to end (Core 13). Run bin/check-frontmatter --all; if the only failures are globs now matching nothing because of deletions, report them and proceed; any other failure, stop.
4. Commit on branch p1-cycle-12-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Per file: one line — retained/merged/deleted, and for retained or merge-target files the section count before → after. Then remaining out-of-scope references to deleted paths, grouped by file. Then branch and SHA. Then any finding not applied as written, with reason.
