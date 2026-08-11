# Review: skills/spec-review-cycle.md — cycle 6

Verdict: changes-required
Reviewed: `skills/spec-review-cycle.md` @ `7d4d03a`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: re-gate of cycle 5's B1 and B2, and a regression check over the
Reconciliation section, which both fixes edited.
Cross-checked: `policies/commit-and-change-control-policy.md` (Spec branches and
the reconciliation pull request), `policies/document-metadata-policy.md`
(Revision lifecycle; status transitions), `LEXICON.md` (Spec state),
`context-sets/spec-and-change-discipline.md` (Open spec delta).
Not inspected: Hard constraints, Procedure steps 1–11, the Cycle directive
format, and the Review artifact schema — cleared in cycle 5 and untouched since.
Findings: 1 blocking
Prior cycle: `reviews/spec-review-cycle-cycle-5.md`

**Cycle 5 findings, re-checked.** B2 (the flip's position relative to the merge)
is **resolved**: step 4 states post-merge, on the default branch, with the reason
and with the note that the cited SHA still resolves. B1 is **not** resolved — see
below.

## B1 — blocking
Claim: The fix for cycle 5's B1 added a paragraph explaining what "once"
quantifies, and removed the only occurrence of "once" from the section it
explains.
Location: `skills/spec-review-cycle.md`, Reconciliation, lead paragraph against
the paragraph immediately following
Evidence: **Verified by running** `git show 7d4d03a^:skills/spec-review-cycle.md`
against `7d4d03a`. The lead previously read "run once over the accumulated diff";
the fix rewrote it to "run over the accumulated diff" and then added **What
"once" quantifies:** beneath it. The word appears nowhere above the paragraph
defining it.
Consequence: A reader meets a definition of a term the section never used and has
to reconstruct which claim it disambiguates. Worse, the rule itself is now
*absent* rather than ambiguous: nothing in the section any longer says the delta
is gated a bounded number of times, which was the substance of D2.2. The fix
removed the claim instead of clarifying it.
Fix: Restore the quantifier to the lead — "gating the accumulated diff **once**"
— and keep the clarifying paragraph beneath it.
