# Directive — Pass 1, Cycle 13 revision: decision-log obligation into the Decision Layer

Date: 2026-08-21
Route: fresh
Model: solid
Role: executor over canonical documents

Document in scope: docs/global-context/decision-layer.md @ 252048f5f3b0b5b0a8a1f5e8a1e0c6f4b9c2d7a3

## Decision (Dave, 2026-08-21)

The obligation formerly in context-sets/base.md — consult the decision log before recommending or encoding anything an existing decision may govern, and cite the governing entry — is a decision-session habit. Add it as a rule under "State and record", after the loose-end-tracker rule, worded as an instruction: "Before recommending or encoding anything an existing decision may govern, read the decision log and cite the governing entry by ID." Renumber.

## Execution

1. Fetch origin/main. If origin/main is not at the SHA above, use origin/main's actual SHA and report it; verify no later edits to decision-layer.md since 40b5ffe.
2. Add the rule. Re-read the file for numbering and consistency.
3. Run bin/check-frontmatter --all. Stop on any failure other than the known README warning.
4. Commit on branch p1-cycle-13-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Rule added, its number, rule count before → after. Branch and SHA.
