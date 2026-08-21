# Directive — Pass 1, Cycle 5: docroot identity files

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ 26f8f10406e6cfe6e7e2fd733f63548ce43b33ba:
- LEXICON.md
- README.md
- operating-model.md
- engagements/working-with-dave.md

Rubric: docs/global-context/review-rubric.md @ 26f8f10.
Foundation: docs/global-context/core.md and docs/global-context/decision-layer.md @ 26f8f10 (both verdict ready; criterion 4 is judged against their current text).

## Context

Fiducial is a bundle compiler. Files are sources; an agent receives only a generated bundle selected by audience. These four files are the repository's self-description and vocabulary. Each is reviewed for whether it still earns a place under that model, and if so, in what form.

## Instructions

1. Fetch origin/main and verify the tree contains 26f8f10 with no later edits to the four files.
2. Read the rubric, core, and decision-layer in full. Then read the four documents in full.
3. Review each against all ten criteria. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, or retire. A retire verdict names where any surviving content goes.
4. Additionally flag: every rule restated from core or decision-layer (criterion 4), with the rule number; every path-shaped reference (criterion 3), counted; every vendor or model name (criterion 8).
5. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope. Do not report either.
6. Write one artifact per document per the schema in skills/spec-review-cycle.md: reviews/LEXICON-cycle-9.md, reviews/README-cycle-3.md, reviews/operating-model-cycle-3.md, reviews/working-with-dave-cycle-1.md. Verdict first. Not inspected required.
7. Commit on branch p1-cycle-5-review, push to origin, report the SHA read back from git. No pull request. No edits to any document. No status flip.

## Report shape

One line per document: path, criterion-10 disposition, verdict, finding counts. Then branch and SHA.
