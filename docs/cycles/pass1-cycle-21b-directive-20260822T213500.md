# Directive — Pass 1, Cycle 21b: skills, the seven procedures

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

Before anything else, clone origin into a fresh directory beside this clone — ../fiducial-21b — and do all work there, including writing this directive file. Never write to the clone this session was started in. If, in the fresh clone, any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover. The clone may be deleted after the PR is open.

Documents in scope, all @ 5136960:
- skills/command-blocks.md
- skills/conversation-retro.md
- skills/boundary-audit.md
- skills/change-package-creation.md
- skills/evidence-review.md
- skills/release-readiness-review.md
- skills/test-plan-review.md

Rubric: docs/global-context/review-rubric.md @ 5136960, eleven criteria.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ 5136960, all through Pass 1. Read roles/context-quality-reviewer.md @ 5136960 first: it is this session's role.
Prior context: docs/batons/baton-20260822T153848.md, "What this session settled". Cycle 20 left two known items in this scope: skills/boundary-audit.md step 7 carries three gap labels where LEXICON defines four; skills/release-readiness-review.md was edited to method-only and its Output trimmed. Both are findings to confirm, not rediscover.

## Context

Fiducial is a bundle compiler; a skill is a procedure an agent in a bundle executes. A skill earns its place if it states a procedure no role or foundation file states, for an audience that runs it. Four of these seven are under 1.5 KB and may be restatements of their role's responsibilities; for each, answer whether the role document already carries the procedure. command-blocks.md has a criterion-9 quirk: its frontmatter carries name: and description: fields; disposition them against the metadata policy's schema. conversation-retro.md prescribes a retro filename; the repository's current retros use retro-<timestamp>.md; judge under criterion 9.

Retired terms: dispatch, sync block, track, prompt — every use is a finding under criterion 4; command-blocks.md is known to carry "sync block" in its description. Vendor and model names are findings under criterion 8.

## Instructions

1. Fetch origin/main; verify the tree contains 5136960 with no later edits to the seven files.
2. Read the role, the rubric, the baton section, and the four foundation files in full. Then the seven documents in full, and for each the role document(s) its audience: names.
3. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, retire, or merge-into (name the target). Then all eleven criteria. The finding list is the edit list an executor can apply.
4. Count and flag: rules restated from Core, decision-layer, LEXICON, operating-model, or the role the skill serves; output-shape lists with a home elsewhere; path-shaped references; vendor and model names; retired terms.
5. Check the seven against each other and against the roles they serve for any procedure stated twice.
6. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning; references to deleted files in files outside this scope; the two skills in cycle 21a; bin/ behaviour. Do not report any of these.
7. Write one artifact per file per the schema in skills/spec-review-cycle.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/ (1 if none). Verdict first. Not inspected required.
8. Commit on branch p1-cycle-21b-review, push to origin, open a pull request against main titled "Pass 1 cycle 21b: seven skill review artifacts" via the REST API with curl if gh cannot authenticate; if neither works, report the compare URL. Do not merge. No edits to any document. No status flip. Report the SHA read back from git.

## Report shape

One line per file: path, criterion-10 disposition, verdict, finding counts. Then branch, SHA, PR number or compare URL. Then one line: count of the seven whose procedure the role document already carries.
