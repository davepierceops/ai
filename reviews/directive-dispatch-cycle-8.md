# Review: skills/directive-dispatch.md — cycle 8

Verdict: ready
Reviewed: `skills/directive-dispatch.md` @ `0a5d07f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-10
Scope: closing regression pass over the whole document, read start to finish
rather than by edit. Specifically looked for the two failure modes a section
deletion produces and that a diff-scoped read misses: a surviving forward
reference to the deleted section, and a rule whose only statement of its own
premise went with it. The first: `grep -rn "§[0-9]"` over all living text
returns `LEXICON.md:115` (`§3 Execution block`, correct after renumbering) and
`OPEN-ITEMS.md:1049`'s old `§3` pointer, which the C1 annotation replaced. The
second is what cycle 6's B1 found and fixed; this pass re-read *Use when*, the
three requirements, §3, *Writing the directive file*, and Executor obligations
against each other for any other instance, and found none — every remaining
"stop and surface" rule names the condition it stops on, and every step of the
land-first sequence is now stated in both places the document enumerates it.
Cross-checked: `LEXICON.md` (Dispatch; Blocks; Retired terms),
`skills/spec-review-cycle.md`, `policies/remote-write-verification-policy.md`,
`skills/command-blocks.md`; `bin/tests/run` (350/351) and
`bin/check-frontmatter --all` (exit 0) by execution.
Not inspected: as at cycles 6 and 7. Cycle 7's N1 stands, no fix taken.
Findings: none
Prior cycle: `reviews/directive-dispatch-cycle-7.md`
