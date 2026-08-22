Execution block. First: write this entire directive verbatim to docs/cycles/bundle-methodology-list-fix-20260821T224500.md, commit it on branch bundle-methodology-list-fix, push to origin, and include the SHA in your report.

# Directive — bin/bundle-methodology: drop two deleted files from its list

Date: 2026-08-21
Route: fresh
Model: cheap
Role: Coder

Scope: bin/bundle-methodology and its tests under bin/tests/, @ 40b5ffe84c111f39fe918f653643b430f12b60d5.

## Problem

context-sets/base.md and context-sets/collab-workflow.md were deleted at 40b5ffe. bin/bundle-methodology names both in its fixed membership list and exits 3 with "not found at HEAD". Its tests reference the same two paths.

## Instructions

1. Fetch origin/main; verify the tree is at 40b5ffe.
2. Remove the two paths from the membership list in bin/bundle-methodology. Change nothing else in the script — not the output format, not the repo name in the header, not the selection rule.
3. Update bin/tests/test_bundle_methodology.py so its expectations match the new list. Do not weaken any assertion beyond removing the two paths.
4. Run the test file. It must pass. Run bin/bundle-methodology --out /tmp and confirm exit 0 and a file written; report the Source line it stamps.
5. Commit on branch bundle-methodology-list-fix, push to origin, report the SHA read back from git. No pull request.

## Report shape

Lines removed from the script. Test result (pass count). The bundle's Source line. Branch and SHA.
