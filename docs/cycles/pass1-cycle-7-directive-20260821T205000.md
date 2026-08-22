# Directive — Pass 1, Cycle 7: re-gate foundation and docroot identity files

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ cb3e75a08b9719058f41c1fb18d6fbb25e234778:
- docs/global-context/core.md — baseline 089083c (cycle 4, ready)
- docs/global-context/decision-layer.md — baseline 04bfeae (cycle 2, ready)
- LEXICON.md — baseline 28d11fa (cycle 9, changes-required)
- operating-model.md — baseline 28d11fa (cycle 3, changes-required)
- engagements/working-with-dave.md — baseline 28d11fa (cycle 1, changes-required)

Prior cycles: reviews/core-cycle-4.md, reviews/decision-layer-cycle-2.md, reviews/LEXICON-cycle-9.md, reviews/operating-model-cycle-3.md, reviews/working-with-dave-cycle-1.md.
Decisions applied: docs/cycles/pass1-cycle-6-revision-directive-20260821T200000.md, pass1-cycle-6b-revision-directive-20260821T203000.md, pass1-cycle-6c-revision-directive-20260821T204500.md.
Rubric: docs/global-context/review-rubric.md @ cb3e75a.

## Rules in force that postdate some governed text

- A directive is one line stating session (fresh or existing) and model tier, then one execution block as a paste block, whose first instruction is to write the directive to a file, commit, push, and report the SHA. There is no sync block. Core's Vocabulary states this; any other file stating a sync block or citing-by-SHA-before-execution is stale and is a finding when that file is in scope, not here.
- "Dispatch" is retired. Its use in files outside this scope is a finding for their cycles, not here.
- "Track" is retired.

## Instructions

1. Fetch origin/main; verify the tree contains cb3e75a with no later edits to the five files.
2. For each file, confirm every prior-cycle finding is resolved as the applicable directive decided. A finding not resolved as decided is a finding.
3. Re-apply all ten rubric criteria to the current text of each file. New defects introduced by revision are findings. Check the five files against each other for a term stated in two places.
4. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; README's retirement leaves stale pointers in the metadata policy, CLAUDE.md, and AGENTS.md. Do not report any of these.
5. Write one artifact per file per the schema in skills/spec-review-cycle.md, with a Baseline: line after Reviewed: — reviews/core-cycle-7.md, reviews/decision-layer-cycle-7.md, reviews/LEXICON-cycle-10.md, reviews/operating-model-cycle-4.md, reviews/working-with-dave-cycle-2.md. A clean pass is the header and nothing else. Verdict ready means ready for Dave's agreement.
6. Commit on branch p1-cycle-7-review, push to origin, report the SHA read back from git. No pull request. No edits to any document. No status flip.

## Report shape

One line per file: path, verdict, finding counts. Then branch and SHA.
