# Review: skills/directive-dispatch.md — cycle 4

Verdict: ready-with-findings
Reviewed: `skills/directive-dispatch.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the whole document, which was rewritten this cycle. Checked: (1) that the
retired Track B delivery mechanics leave no dangling reference anywhere in the
tree; (2) that the redefined Track is consistent with `LEXICON.md` and with
`decisions/log.md` `DEC-000150`; (3) that the two-failure detector's relocation
preserves `DEC-000080`'s keep-reason; (4) that the sync-block requirement
survives with `DEC-000090`'s conclusion intact; (5) every path cited resolves at
this SHA.
Cross-checked: `LEXICON.md` (Dispatch; Blocks; Spec state),
`policies/remote-write-verification-policy.md` (Rule 4; Scope; Relationship to
existing rules), `skills/command-blocks.md` (evidence scope; conformance
criteria), `skills/spec-review-cycle.md` (Hard constraints; Procedure steps 4
and 6), `context-sets/spec-and-change-discipline.md` (Open spec delta),
`decisions/log.md` `DEC-000080`, `DEC-000090`, `DEC-000100`, `DEC-000150`,
`BACKLOG-v2.md` (`bin/dispatch`).
Not inspected: whether a paste-delivered directive survives arrival intact in
Dave's actual client — the document rests the integrity claim on the paste-block
definition, and no delivery was rehearsed; the naming schema, unchanged and
still marked a proposal.
Findings: 2 non-blocking
Prior cycle: `reviews/directive-dispatch-cycle-3.md`
Dave should inspect: N1 — the retirement removed the tree's only worked command
blocks, which two other documents used as their reference instances.

## N1 — non-blocking
Claim: Retiring Track B's mechanics removed every worked command block in the
governed tree, leaving `skills/command-blocks.md` a rule set with no instance.
Location: `skills/directive-dispatch.md`, whole document (the removed Track B
mechanics section)
Evidence: **Verified by running.**
`grep -rn '^```' skills/*.md policies/*.md roles/*.md context-sets/*.md LEXICON.md`
at `582fb6f` returns only markdown/yaml/text template fences and this document's
paste-block and path templates — no shell command block anywhere in the governed
set. The tree's remaining runnable shell is `decisions/log.md` `DEC-000140`'s
generation procedure, which is a decision-log entry, not a published block.
`reviews/command-blocks-cycle-2.md` records the retired blocks as "still the
tree's only published command blocks", so this is a known dependency now broken.
Consequence: An author writing a command block has seven conformance criteria and
nothing conformant to read. That is a teaching loss, not a correctness defect —
the criteria are self-contained and mechanically checkable, and the sync block a
dispatch emits is one line.
Fix: None taken this cycle; adding an example purely to have one would be
inventing a block with no use behind it, which is the error
`BACKLOG-v2.md` records against `bin/dispatch`. If a conformance pass over the
skills is run (`OPEN-ITEMS.md`, "Skills conformance pass"), an example belongs in
`skills/command-blocks.md` itself rather than here.

## N2 — non-blocking
Claim: The Track definitions cover "remote unreachable" but not "no repository at
all", which was the case the retired Track B originally existed for.
Location: `skills/directive-dispatch.md`, §3 Track
Evidence: Verified by reading the retired text at `582fb6f^`: old Track B was
"the no-repository-tooling path: private repos without a credentialed connector,
degraded tooling, an absent connector." The new Track B is narrower — a working
tree with no reachable remote.
Consequence: An executor with no working tree cannot land the directive, and the
document gives it no instruction. In practice this is empty: the executor is a
session holding a clone by definition, and one that holds none cannot execute a
directive against a repository either, so the failure is caught by "an
instruction that cannot be executed as written → stop and surface." Recorded
because the narrowing was deliberate and should not later read as an oversight.
Fix: None required. Revisit only if an executor environment without a clone ever
becomes real.
