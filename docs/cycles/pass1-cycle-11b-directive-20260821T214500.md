# Directive — Pass 1, Cycle 11b: boundaries

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ 7310937da1ce0e2ab65ad9bd3fc1b7d82c530e46:
- boundaries/human-review-boundary.md
- boundaries/live-integration-boundaries.md
- boundaries/mocked-boundaries.md
- boundaries/vendor-tooling-boundary.md

Rubric: docs/global-context/review-rubric.md @ 7310937.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ 7310937, all through Pass 1.

## Context

Fiducial is a bundle compiler: files are sources, an agent receives a generated bundle selected by audience, and Core plus the decision layer now state the evidence rules, session kinds, block vocabulary, and working register. Each boundary file is reviewed for whether it still earns a place, and if so as what.

Retired terms: dispatch, sync block, track, prompt — every use is a finding under criterion 4 (LEXICON states the replacements). Vendor and model names are findings under criterion 8.

## Instructions

1. Fetch origin/main; verify the tree contains 7310937 with no later edits to the four files.
2. Read the rubric and all four foundation files in full. Then the four documents in full.
3. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, retire, or merge-into (name the target). Then all ten criteria. For retain-with-changes, the finding list is the edit list an executor can apply.
4. Count and flag: rules restated from Core, decision-layer, LEXICON, or operating-model, by rule or section; path-shaped references; vendor and model names; retired terms.
5. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning. Do not report any of these.
6. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/ (1 if none). Verdict first. Not inspected required.
7. Commit on branch p1-cycle-11b-review, push to origin, report the SHA read back from git. No pull request. No edits to any document. No status flip.

## Report shape

One line per file: path, criterion-10 disposition, verdict, finding counts. Then branch and SHA.
