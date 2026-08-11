# Directive: PR #70 review fixes (F1, F2, F3) + accepted risks (F4)

Date: 2026-08-11
Route: fresh
Model: Sonnet 5
Track: A
Execution block: this file is the baton. First act: check out `bundle-write`,
sync from origin, commit this file verbatim to
docs/cycles/bundle-write-fixes-2026-08-11-directive.md on that branch, push,
then execute.

Context: reviews found these against the bundle-write branch. F1/F2/F3 are
accepted; fix on this branch. Do not re-review the rest of the diff.

## F1 — no file on --strict failure

--write currently writes the bundle to disk before the --strict dangling-
reference check runs, so a failed strict run (rc=1) still leaves a file and
prints `wrote <path>`. Fix: when --strict is set and a dangling reference
exists, exit with the policy failure having created no file and no directory,
and print no `wrote` line. Extend the spec (AC-BN-14 or a sibling AC in
§3.7.1) to state it. Test first, confirmed red behaviorally (current code
writes the file; the new test must catch that), then fix to green.

## F2 — tilde-expand explicit --out

`--out ~/x` currently creates a literal `~` directory under cwd. Fix: add
`.expanduser()` in resolve_out_dir — in BOTH bin/bundle and
bin/bundle-methodology (same function, verbatim copy; they must not diverge).
bin/bundle-methodology is explicitly permitted for this one change and
nothing else. Update AC-BN-12 wording so "tilde-expanded" covers explicit
--out values. Test first, confirmed red, for both tools.

## F3 — strengthen the content assertion

test_bn15's only content check asserts the entry's own header. Strengthen:
assert the written file is byte-identical to a `--format concat` stdout run
of the same entry (or assert every closure member's header appears). This is
a test-strengthening change: it should PASS against the current
implementation — if it fails, stop and surface, because that means the
implementation is wrong, not the test.

## F4 — accepted risk entry

Append to ACCEPTED-RISKS.md (create if absent, matching the repo's existing
conventions): same-minute --write re-runs silently overwrite the prior
output (minute-resolution stamp, no collision handling); inherited from
bundle-methodology, declined 2026-08-11, revisit if a real loss occurs.
F5 (error categorization on non-directory --out) declined without a risk
entry — safe failure, cosmetic exit class.

## Discipline and constraints

- Spec edits before tests, tests confirmed red before fixes (F1, F2).
- Full suite green after, except the pre-existing test_bn10 failure (fails
  on main; out of scope; do not touch).
- Do not open a PR. Push the branch, STOP, report: commits, red/green
  results per finding, files changed.
