# Directive: review PR #70 (bundle --write)

Date: 2026-08-11
Route: fresh
Model: Sonnet 5
Track: A
Execution block: this file is the baton. First act: check out the
`bundle-write` branch, sync it from origin, commit this file verbatim to
docs/cycles/bundle-write-review-2026-08-11-directive.md on that branch,
push, then execute.

## Scope

Two review passes over the diff of `bundle-write` against `main`
(the --write change: docs/packages/package-a-spec.md §3.7.1,
bin/tests/test_bundle.py TestWriteMode, bin/bundle). The directive baton
commits are not under review.

1. **Quality review** — correctness, maintainability, consistency with
   bin/bundle-methodology's conventions, spec/test/implementation agreement,
   test adequacy against AC-BN-11..15.
2. **Skeptic/risk review** — where the evidence could be lying: the red-gate
   was argparse-level only (tests failed on `unrecognized arguments`, not on
   wrong behavior); check whether any assertion in TestWriteMode could pass
   against subtly wrong behavior. Also: partial-file guarantees on render
   failure, tilde expansion, stamp-collision behavior, and whether --write
   silently changes any existing non-write behavior.

Run the tests yourself; do not trust the prior report. Verify by running,
not by reading, wherever cheap.

## Constraints

- Findings only. Fix nothing, refactor nothing, commit nothing beyond the
  baton.
- Report per the review-artifact findings schema (Claim / Location /
  Evidence / Consequence / Fix), verdict first: ready | ready-with-findings |
  changes-required. Report is triageable by CoS, not formatted for a human.
- STOP after reporting.
