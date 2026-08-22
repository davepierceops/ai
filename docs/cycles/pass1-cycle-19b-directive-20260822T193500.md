# Directive — Pass 1, Cycle 19b: roles, execution-side

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

Documents in scope, all @ ed926db:
- roles/architect-agent.md
- roles/coder-agent.md
- roles/test-designer-agent.md
- roles/reviewer-agent.md
- roles/skeptic-risk-agent.md
- roles/release-manager-agent.md

Rubric: docs/global-context/review-rubric.md @ ed926db.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ ed926db, all through Pass 1.
Prior context: docs/batons/baton-20260822T153848.md — read "What this session settled". Then reviews/agent-review-policy-cycle-1.md finding A2: the review artifact schema in skills/spec-review-cycle.md owns the shape of a review's output; role documents state what the role inspects and decides, not what fields its report carries. Apply that as a settled rule. reviewer-agent.md and release-manager-agent.md were edited by cycle 17 (merge targets); docs/cycles/pass1-cycle-17-revision-directive-20260822T170000.md records what landed in each.

## Context

Fiducial is a bundle compiler: an agent receives a generated bundle selected by audience, and a role document is the part of the bundle that tells the agent what it is for. These six roles run in execution sessions. Each is reviewed for whether it still earns a place, and if so as what. operating-model.md's change flow already assigns each of these roles its step; a role document that restates the flow is restating operating-model.

Retired terms: dispatch, sync block, track, prompt — every use is a finding under criterion 4. Vendor and model names are findings under criterion 8.

## Instructions

1. Fetch origin/main; verify the tree contains ed926db with no later edits to the six files.
2. Read the rubric, the baton section, finding A2, the cycle-17 directive, and all four foundation files in full. Then the six documents in full.
3. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, retire, or merge-into (name the target). Then all ten criteria. For retain-with-changes, the finding list is the edit list an executor can apply.
4. Count and flag: rules restated from Core, decision-layer, LEXICON, or operating-model, by rule or section; output-shape lists that belong to the artifact schema or the change package; path-shaped references; vendor and model names; retired terms.
5. Check the six against each other for any responsibility stated twice or assigned to two roles; in particular reviewer-agent against skeptic-risk-agent, and test-designer-agent against coder-agent on the separation rule. Check each role's audience: value is its own slug. Check release-manager-agent's release-package list against operating-model's change package and report the relationship in one line.
6. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning; references to deleted files in files outside this scope; the five roles in cycle 19a. Do not report any of these.
7. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/ (1 if none). Verdict first. Not inspected required.
8. Commit on branch p1-cycle-19b-review, push to origin, open a pull request against main titled "Pass 1 cycle 19b: six role review artifacts (execution-side)". Do not merge. No edits to any document. No status flip. Report the SHA read back from git and the PR number.

## Report shape

One line per file: path, criterion-10 disposition, verdict, finding counts. Then branch, SHA, PR number. Then the release-package relationship line.
