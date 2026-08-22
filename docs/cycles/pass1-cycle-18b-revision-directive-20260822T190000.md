# Directive — Pass 1, Cycle 18b: dead entries in the gate-document class list

Date: 2026-08-22
Route: fresh
Model: standard
Role: Coder

Document in scope: policies/document-metadata-policy.md, at origin/main HEAD.

In the gate-document class list, remove every entry naming a file that does not exist in the tree, except README.md, which stays until Pass 2. Verify each removal with git: the file is absent at HEAD and its deletion commit is on main. Expected: policies/testing-policy.md and policies/agent-review-policy.md; report any others found. No other edit.

bin/check-frontmatter --all passes. Commit, push, open a pull request against main titled "Pass 1 cycle 18b: remove deleted files from the gate-document class list". Do not merge.

Report: each entry removed with its deletion commit; branch, SHA, PR number.
