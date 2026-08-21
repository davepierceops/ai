# Directive — Pass 1, Cycle 1: review core and decision-layer

Date: 2026-08-21
Route: fresh
Model: frontier
Role: Spec Reviewer Agent

## Documents in scope

- `docs/global-context/core.md` @ 5aa02c5ac3f530efc06d1c5e4311eb41e8914855
- `docs/global-context/decision-layer.md` @ 5aa02c5ac3f530efc06d1c5e4311eb41e8914855

Rubric: `docs/global-context/review-rubric.md` @ the same SHA. Every finding
cites a rubric criterion number, or states that it falls outside the rubric.

## Context

These two files are the foundation every other file in this repository will
be judged against (rubric criterion 4). They are reviewed first, together,
because the decision layer assumes core and a gap in one may be the other.

`docs/global-context/inventory.md` is the triage record that produced them.
Read it for provenance; do not review it.

## Instructions

1. Verify the working tree is at the SHA above, or contains it with no later
   edits to the three files named. Stop and report if not.
2. Read the rubric in full, then both documents in full.
3. Review each document against all ten criteria. Additionally check:
   - internal consistency between the two files — a rule stated in both, or
     stated differently in each, is a finding;
   - whether any rule is unfollowable as written by an agent that has only
     the bundle and the repository;
   - whether core obeys its own rule 14 and the decision layer obeys its own
     rule 15.
4. Write one review artifact per document, using the schema in
   `skills/spec-review-cycle.md` (Review artifact schema):
   - `reviews/core-cycle-1.md`
   - `reviews/decision-layer-cycle-1.md`
   Verdict first. `Not inspected` is required. `Evidence` distinguishes
   verified-by-running from inferred-by-reading.
5. Commit both artifacts on branch `gc-cycle-1-review`, push to `origin`,
   and report the branch and commit SHA read back from git. Do not open a
   pull request. Do not edit either document. Do not flip any `status`.

## Report shape

One line per document: path, verdict, finding counts by severity. Then the
branch and SHA. Nothing else — the artifacts carry the detail.
