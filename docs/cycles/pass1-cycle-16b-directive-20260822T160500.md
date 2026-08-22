# Directive — Pass 1, Cycle 16b: policies, document governance and evidence

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0:
- policies/document-metadata-policy.md
- policies/decision-log-policy.md
- policies/agent-review-policy.md
- policies/testing-policy.md

Rubric: docs/global-context/review-rubric.md @ 2a722bb.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ 2a722bb, all through Pass 1.
Prior context: docs/batons/baton-20260822T153848.md @ 2a722bb — read "What this session settled", "Agreement is blocked on scope", and "Known stale references" before reviewing.

## Context

Fiducial is a bundle compiler: files are sources, an agent receives a generated bundle selected by audience, and Core plus the decision layer state the evidence rules, session kinds, block vocabulary, and working register. These four policies govern document lifecycle and frontmatter, the decision log, agentic review, and testing. Each is reviewed for whether it still earns a place, and if so as what.

Retired terms: dispatch, sync block, track, prompt — every use is a finding under criterion 4 (LEXICON states the replacements). Vendor and model names are findings under criterion 8.

document-metadata-policy.md is the largest file in Pass 1 and the revision target for two settled decisions: extending the scope glob to docs/global-context/** and reserving all-decision-roles as an audience value, reserved value first. Those edits belong to the revision cycle, not this review. Report the scope-glob gap as a single finding that points at the baton; do not design the fix. Apply the rubric's length criterion to this file with particular care — the baton's rule is that documents which do not fit in working attention get skimmed.

## Instructions

1. Fetch origin/main; verify the tree contains 2a722bb with no later edits to the four files.
2. Read the rubric, the baton sections named above, and all four foundation files in full. Then the four documents in full.
3. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, retire, or merge-into (name the target). Then all ten criteria. For retain-with-changes, the finding list is the edit list an executor can apply.
4. Count and flag: rules restated from Core, decision-layer, LEXICON, or operating-model, by rule or section; path-shaped references; vendor and model names; retired terms. The baton lists a reference to a deleted path at decision-log-policy.md:65 — in scope, a finding; confirm the line and report any others.
5. Check the four against each other, and testing-policy.md against context-sets/testing-and-verification.md (through Pass 1; single home for the mock checklist), for any term or rule stated twice. Propose a single home where one is missing.
6. Known and out of scope: all-decision-roles is not yet a reserved audience value; the README unmatched-glob warning; references to deleted files in files outside this scope; the four policies in cycle 16a. Do not report any of these. The docs/global-context/ scope gap is in scope only as the one pointer finding stated in Context.
7. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/ (1 if none). Verdict first. Not inspected required.
8. Commit on branch p1-cycle-16b-review, push to origin, report the SHA read back from git. No pull request. No edits to any document. No status flip.

## Report shape

One line per file: path, criterion-10 disposition, verdict, finding counts. Then branch and SHA. Then, in one line each: the retired-term count across the four, any single-home proposal from step 5, and the document-metadata-policy line count with a one-word length verdict.
