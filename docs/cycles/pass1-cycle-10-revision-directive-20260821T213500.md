# Directive — Pass 1, Cycle 10 revision: LEXICON retired terms

Date: 2026-08-21
Route: fresh
Model: solid
Role: executor over canonical documents

Document in scope: LEXICON.md @ 96c46fdad48cec09b6e2ed8f999099a57c8e1166
Review triaged: reviews/LEXICON-cycle-11.md @ 96c46fd.

## Decision

### L10 — accept (Dave)
Add three entries to Retired terms, matching the existing Prompt entry's form — the word, then what to write instead:
- Dispatch — retired 2026-08-21. Write "hand the directive to an execution session," or "direct."
- Sync block — retired 2026-08-21. Nothing precedes the execution block; the executor fetches as its first act.
- Track — retired 2026-08-21. A directive states route and model tier; there is no third part.
No other text changes. "No entry added in its place" (cycle 6c) meant no replacement term, not no retirement record.

## Execution

1. Fetch origin/main; verify the tree contains 96c46fd with no later edits to LEXICON.md.
2. Apply the decision. Re-read the Retired terms section for form consistency.
3. Run bin/check-frontmatter --all. Stop and report on failure.
4. Commit on branch p1-cycle-10-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Entries added, one line each. Then branch and SHA.
