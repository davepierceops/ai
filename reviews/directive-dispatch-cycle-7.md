# Review: skills/directive-dispatch.md — cycle 7

Verdict: ready
Reviewed: `skills/directive-dispatch.md` @ `0a5d07f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-10
Scope: confirmation pass over cycle 6's B1 and B2, plus a regression read of the
regions those fixes touched. B1: the push obligation is present in both places
the document enumerates the landing steps — the Purpose paragraph and the
land-first executor obligation — and the unreachable-remote obligation now
excepts a rule the document states. B2: the false historical claim is gone,
replaced by the argument that actually carries the point (the party writing the
directive is not the party that can know the executor's remote state). Also
checked: the two wording fixes taken this cycle, and whether the push obligation
contradicts anything in `policies/remote-write-verification-policy.md`, which
governs what a report may claim about a write.
Cross-checked: `policies/remote-write-verification-policy.md` (Rules 1–3; Scope,
the cannot-read-its-own-write-back paragraph), `skills/spec-review-cycle.md`
(Procedure steps 6–7), `LEXICON.md` (`Directive file`; `Track` tombstone);
`bin/tests/run` by execution (350/351, `test_bn10` the known failure);
`bin/check-frontmatter --all` by execution (clean, exit 0).
Not inspected: the model table, the naming schema, *Writing the directive file* —
as at cycle 6.

## N1 — `LEXICON.md` defines "landed" and is silent on the push

Severity: non-blocking
Claim: `LEXICON.md`'s `Directive file` entry reads "written and committed by the
**executor** as its first act, and thereafter cited by path and the SHA of the
commit that landed it." With the push now required here, "landed" carries a
condition its own definition does not state.
Location: `LEXICON.md`, Dispatch, `Directive file`
Evidence: Verified by reading both at `0a5d07f`. No contradiction: the lexicon
says what a directive file *is*, and the procedure for producing one is this
document's. But a reader taking "the commit that landed it" as the whole
condition would find a local commit sufficient.
Consequence: Small. The operative rule is stated where an executor reads it, and
`policies/remote-write-verification-policy.md` independently forbids reporting a
write as landed on anything but read-back evidence. The seam is definitional, not
behavioral.
Fix: None taken — the blast radius is C1–C5 and this is a definitional tightening
that neither C1 nor a consistency requirement reaches. It belongs to whatever
cycle next opens `LEXICON.md` on the touch rule.

Findings: 1 non-blocking (no fix taken)
Prior cycle: `reviews/directive-dispatch-cycle-6.md`
