# Directive — Pass 1, Cycle 21a: skills, the cycle and directive skills

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Documents in scope, all @ 5136960:
- skills/spec-review-cycle.md
- skills/directive-dispatch.md

Rubric: docs/global-context/review-rubric.md @ 5136960, eleven criteria.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ 5136960, all through Pass 1. Read roles/context-quality-reviewer.md @ 5136960 first: it is this session's role.
Prior context: docs/batons/baton-20260822T153848.md, "What this session settled" — in particular the directive rule: one line naming session and model tier, then one paste block whose first instruction is to write the directive to a file, commit, push, and report the SHA; nothing precedes it; dispatch, sync block, and track are retired.

## Context

Fiducial is a bundle compiler; a skill is a procedure an agent in a bundle executes. Both files in scope predate the directive rule in Core and were written for a world with tracks, sync blocks, and MCP-committed directives. Each is reviewed for whether it still earns a place, and if so as what.

skills/directive-dispatch.md: the baton records that it is renamed and rewritten to the directive rule. Answer criterion 10 as: what, if anything, survives beyond what Core already states — the executor obligations, the directive-authoring constraints, the naming schema — and propose the new filename per criterion 9 and the repository's skill-naming convention. Everything describing tracks, sync blocks, bin/dispatch, or Track B mechanics is retired content; confirm nothing in it survives unhomed.

skills/spec-review-cycle.md: two things live here that are not the cycle procedure — the cycle directive format and the review artifact schema. Cycle 17 made the artifact schema the single home for review output shape. Disposition each part separately: the procedure, the directive format (against Core's directive rule), and the artifact schema. Every path reference, vendor name, model name, and retired term is a finding.

## Instructions

1. Fetch origin/main; verify the tree contains 5136960 with no later edits to the two files.
2. Read the role, the rubric, the baton section, and the four foundation files in full. Then the two documents in full.
3. For each, answer criterion 10 first and explicitly; for directive-dispatch, per-section. Then all eleven criteria. The finding list is the edit list an executor can apply.
4. Count and flag: rules restated from Core, decision-layer, LEXICON, or operating-model; path-shaped references; vendor and model names; retired terms.
5. Cross-check: the cycle directive format in spec-review-cycle against Core's directive rule; the artifact schema against what cycle 17 and cycle 20 left in roles/reviewer-agent.md and roles/spec-reviewer-agent.md; both files against roles/context-quality-reviewer.md for which role runs a rubric cycle.
6. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning; references to deleted files in files outside this scope; the seven skills in cycle 21b; bin/ behaviour. Do not report any of these.
7. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/. Verdict first. Not inspected required.
8. Commit on branch p1-cycle-21a-review, push to origin, open a pull request against main titled "Pass 1 cycle 21a: two skill review artifacts (cycle and directive)" via the REST API with curl if gh cannot authenticate; if neither works, report the compare URL. Do not merge. No edits to any document. No status flip. Report the SHA read back from git.

## Report shape

One line per file: path, criterion-10 disposition (per section for directive-dispatch), verdict, finding counts. Then branch, SHA, PR number or compare URL. Then one line: the proposed new filename for directive-dispatch.
