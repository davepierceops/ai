# Cycle 8 Directive — document-metadata-policy re-gate

Date: 2026-08-02
Documents in scope:
- `policies/document-metadata-policy.md` @ 086ff4b (reviewed state;
  byte-identical on main at 626442b)
- `vendors/README.md` @ 626442b
- `docs/packages/package-a-spec.md` @ 626442b
Review artifact: `reviews/document-metadata-policy-cycle-8.md` @ 64f2895
(on main via PR #7)

## Decisions

### B1 — modify (delete, do not restate)
Finding: `document-metadata-policy.md:140` — "Condition 5 is a human
judgment, and it is the only one" is false since W-1's fail-safe made
condition 3 a judgment for unclear cases, and it reinstates the
enumeration-only reading E2 rejected.
Resolution: delete the sentence. Fourth consecutive gate where this
sentence is the defect; it earns no fifth restatement. Verify the
surrounding paragraph still reads coherently without it and make no
other change to the section.

### B2 — accept
Finding: `vendors/README.md:34-56` still claims this policy "does not
list `vendors/**`", that the hook does not check those files, and that
the extension "was not done" — all false since ef4438b, and the file is
now itself inside the enforced set.
Resolution: correct the passage to state the current fact: `vendors/**`
is in the policy's in-scope globs as of ef4438b and the hook enforces
frontmatter on these files. Keep any surrounding rationale that remains
true; remove or restate only what ef4438b falsified.

### N1 — accept
Finding: the closing risk paragraph at
`document-metadata-policy.md:222-225` overstates the structural bound.
Resolution: restate per the reviewer's fix so the claimed bound matches
what the mechanisms actually guarantee. No new claims.

### N2 — modify (dereference, not bump)
Finding: AC-SC-1 in `docs/packages/package-a-spec.md` enumerates eight
globs while e22a2d3 moved its test to nine.
Resolution: remove the literal count from the AC. Restate AC-SC-1 so the
check is defined against the policy's scope section as the source of
truth for the glob set, whatever its size. Do not write "nine" — the
count is a derived fact whose home is the policy, and a literal here is
the same one-fact-two-homes drift this finding caught.

### N3 — reject (already resolved)
Finding: `skills/spec-review-cycle.md:89` still says "no tool checks it".
Resolution: no action. Fixed by b1773d0 (PR #6), merged to main before
the review ran; the reviewer's checkout predated the merge. The
confirmation pass verifies this at current main rather than taking this
directive's word for it.

## Deferred / out of scope
- The agreement flip — Dave's gate, after the confirmation pass.
- Any edit to `reviews/` artifacts, including cycle-8's own.
- `docs/packages/*-change-package.md` records (E5 standing disposition).

## Execution notes
- All three touched files are `draft` or out of frontmatter lifecycle;
  plain commits, no status ceremony. The policy file itself stays
  `in-review` — content edits only (B1, N1), no frontmatter change.
- One coherent commit per finding where practical; `bin/tests/run` and
  `check-frontmatter --all` green before opening the PR.
- On completion, hand back for the reviewer confirmation pass at the
  revised state.
