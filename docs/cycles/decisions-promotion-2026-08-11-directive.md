# Directive: Decisions Promotion and Agreement Flips — 2026-08-11

Route: fresh
Model: Sonnet 5
Execution block: this directive travels as a paste block. Your first act —
before any other work — is Step 0 below.

## What this is

Post-merge closeout of PR #67 (`methodology/friction-2026-08-09`, merged to
main 2026-08-11). Two mechanical tasks under Dave's explicit direction:
promote three decision entries into `decisions/log.md`, and flip the
in-review documents to `agreed` with expedited-log entries. Dave's merge
review of PR #67 is the review these flips cite.

## Step 0 — Land this directive

1. `git fetch origin` and check out `main` at origin HEAD. Verify the PR #67
   merge is in history.
2. Write this directive, verbatim and in full, to
   `docs/cycles/decisions-promotion-2026-08-11-directive.md`.
3. Commit, record the SHA for the report.

All work lands on a branch `chore/decisions-promotion-2026-08-11` (branch
protection requires a PR; create the branch from main after Step 0's
verification, land everything including this directive there, push, and open
no PR — report the branch; the PR opens from the decision session).

## Task 1 — Promote three decisions

`docs/cycles/friction-refactor-2026-08-09-decisions.md` contains three
log-format entries under `### Proposed` headings: DEC-000160, DEC-000170,
DEC-000180.

1. Append them to `decisions/log.md` in ID order: 160, 170, 180. Extract the
   log-format entry bodies exactly — the `## DEC-0001XX` heading through the
   end of that entry — not the `### Proposed` wrapper headings and not the
   surrounding discussion prose. Match the log's existing entry separation
   convention (inspect the file; the tail is a plain entry ending).
2. D21 in the decisions file records that DEC-000180's ID is provisional on
   160 and 170 landing first, in that order — this task satisfies that
   condition. Verify no DEC-000160/170/180 already exists in the log before
   appending.
3. Context lines in each entry: conform any that say "pending promotion" or
   reference their own draft status — they are now log entries, not drafts.
   Change nothing else in the entry bodies. The source file in `docs/cycles/`
   is a historical record: do not edit it.

## Task 2 — Agreement flips

1. Enumerate the flip set from frontmatter, not from this directive:
   every `*.md` on main at `status: in-review` whose in-review status came
   from the PR #67 branch (the parent directives' work). Expected six to
   seven files (LEXICON, directive-dispatch, spec-review-cycle,
   remote-write-verification-policy, spec-and-change-discipline,
   chief-of-staff, possibly commit-and-change-control-policy) — but the
   frontmatter is the truth. Report any file at in-review you exclude, and
   why.
2. For each: add one entry to `reviews/expedited-log.md` per that file's own
   format (inspect existing entries), citing:
   - the reviewed state: the document's path @ the merged main SHA of PR #67's
     merge commit
   - the review: Dave's merge review of PR #67
     (https://github.com/davepierceops/ai/pull/67), 2026-08-11
3. Flip each with `bin/flip-agreed`, `last-reviewed` pointing at
   `reviews/expedited-log.md` @ the SHA of the commit that added the entries.
   The tool fails closed if the cited SHA doesn't resolve to a log entry —
   sequence the commits so it passes: log entries commit first, flips cite
   that commit.
4. Run `bin/check-frontmatter --all` and `bin/tests/run`; both must be clean
   modulo the known test_bn10 failure.

## Hard constraints

- No merge to main, no push to main, no force-push, no `gh`.
- `decisions/log.md` is edited exactly as Task 1 states — append-only, no
  edits to existing entries.
- No document outside the flip set changes status.
- This is mechanical execution of Dave's decisions, not a judgment session:
  an instruction that cannot be executed as written, or any ambiguity in the
  flip set or entry boundaries → stop that item and surface it. Do not
  decide.

## Final report

Triageable by CoS, opening with "executed `<path>`, landed as `<sha>`":
branch name and HEAD; the three promoted IDs and the log's new tail entry ID;
the flip set with each document's `last-reviewed` target; excluded in-review
files if any; test and frontmatter results; anything stopped.
