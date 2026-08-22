# Directive — Pass 1, Cycle 19a: roles, decision-side

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ ed926db:
- roles/chief-of-staff.md
- roles/spec-reviewer-agent.md
- roles/context-quality-reviewer.md
- roles/pm-em-owner.md
- roles/orchestrator-agent.md

Rubric: docs/global-context/review-rubric.md @ ed926db.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ ed926db, all through Pass 1.
Prior context: docs/batons/baton-20260822T153848.md — read "What this session settled". Then reviews/agent-review-policy-cycle-1.md finding A2: the review artifact schema in skills/spec-review-cycle.md owns the shape of a review's output; role documents state what the role inspects and decides, not what fields its report carries. Apply that as a settled rule.

## Context

Fiducial is a bundle compiler: an agent receives a generated bundle selected by audience, and a role document is the part of the bundle that tells the agent what it is for. Each is reviewed for whether it still earns a place, and if so as what. orchestrator-agent.md is superseded by chief-of-staff.md and retires this pass; review it only for content that survives nowhere else, and name the home for anything that does.

Retired terms: dispatch, sync block, track, prompt — every use is a finding under criterion 4. Vendor and model names are findings under criterion 8. chief-of-staff.md is expected to carry the most residue: its dispatch, prompt, and tranche-decomposition sections were written before the directive rule in Core; judge each against Core's current statement.

## Instructions

1. Fetch origin/main; verify the tree contains ed926db with no later edits to the five files.
2. Read the rubric, the baton section, finding A2, and all four foundation files in full. Then the five documents in full.
3. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, retire, or merge-into (name the target). Then all ten criteria. For retain-with-changes, the finding list is the edit list an executor can apply.
4. Count and flag: rules restated from Core, decision-layer, LEXICON, or operating-model, by rule or section; output-shape lists that belong to the artifact schema; path-shaped references; vendor and model names; retired terms.
5. Check the five against each other for any responsibility stated twice or assigned to two roles. Check each role's audience: value is its own slug.
6. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning; references to deleted files in files outside this scope; the six roles in cycle 19b. Do not report any of these.
7. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/ (1 if none). Verdict first. Not inspected required.
8. Commit on branch p1-cycle-19a-review, push to origin, open a pull request against main titled "Pass 1 cycle 19a: five role review artifacts (decision-side)". Do not merge. No edits to any document. No status flip. Report the SHA read back from git and the PR number.

## Report shape

One line per file: path, criterion-10 disposition, verdict, finding counts. Then branch, SHA, PR number. Then one line: the orchestrator content, if any, that has no home.
