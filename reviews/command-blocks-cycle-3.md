# Review: skills/command-blocks.md — cycle 3

Verdict: ready-with-findings
Reviewed: `skills/command-blocks.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the two edits made this cycle — the evidence-scope paragraph's closing
sentences and the ordinal-stability sentence under Conformance criteria. Both
existed only to cite the retired Track B blocks in `skills/directive-dispatch.md`
and had to be re-grounded. Checked that the seven criteria, their wording, and
their numbering are untouched.
Cross-checked: `skills/directive-dispatch.md` (whole document, at this SHA and
at `582fb6f^`), `LEXICON.md` (Blocks), `decisions/log.md` `DEC-000100`,
`DEC-000120`.
Not inspected: the body rules other than the evidence rule, and the criteria
themselves — unchanged, and last gated at cycle 2; no block was executed this
cycle, since the document publishes none.
Findings: 1 observation
Prior cycle: `reviews/command-blocks-cycle-2.md`

## O1 — observation
Claim: The replacement sentence states an obligation ("Where a document emits
such a block, it says so where the block is defined") where the original stated a
fact about one document.
Location: `skills/command-blocks.md`, evidence-scope paragraph, final sentence
Evidence: Verified by running `git show 582fb6f^:skills/command-blocks.md`. The
prior text read "…the Track B pre-flight `ls` in `skills/directive-dispatch.md`
is the tree's live instance, and that document says so where the block is
defined" — an observation about an instance. The new text generalizes it to any
document claiming the exemption.
Consequence: A mild widening rather than a defect: the practice being generalized
is the one the retired instance followed, and the alternative — deleting the
clause with the instance — would have removed the only thing making the exemption
auditable, since a claimed exemption and a forgotten capture are indistinguishable
from the block alone. Recorded because the generalization was not directed by the
directive and should be visible as a choice.
Fix: None taken. Delete the clause if the widening is unwanted; nothing else
depends on it.
