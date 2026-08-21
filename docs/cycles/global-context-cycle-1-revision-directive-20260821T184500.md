# Directive — Pass 1, Cycle 1 revision: core and decision-layer

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

Documents in scope:
- `docs/global-context/core.md` @ 5aa02c5ac3f530efc06d1c5e4311eb41e8914855
- `docs/global-context/decision-layer.md` @ 5aa02c5ac3f530efc06d1c5e4311eb41e8914855

Reviews triaged: `reviews/core-cycle-1.md`, `reviews/decision-layer-cycle-1.md`
@ 063ab0f3d9f4818e31605bc8b809d0045dccc562.

Rubric: `docs/global-context/review-rubric.md` @ 5aa02c5. Every edit below must
leave both files conformant to all ten criteria.

## Decisions

### CORE-1 — accept
Rescope rule 14 to names an agent generates — session artifacts, retros,
directives, captured output. State that a canonical document keeps a stable
descriptive name. Keep the "no random strings, hashes, or UUIDs" clause; it is
the substance of the rule, not a restatement.

### CORE-2 — accept (Dave: single home)
Delete rule 15 from core. The decision layer is the only home for
command-block criteria. Rubric criterion 4 stands as written. Renumber.

### CORE-3 — accept
Add `order: 0` to core's frontmatter.

### CORE-4 — accept
Rule 13: one scope, the wide one. A changed fact is updated everywhere it
appears, across files, not only within the document.

### CORE-5 — accept
Cut "This file references nothing." Restate precedence as an instruction to the
reader: a rule elsewhere that conflicts with a rule here does not waive it. Use
the term "layer" for any file that adds rules; drop "domain layer."

### CORE-6 — accept
Cut "No improvisation, no silent partial execution" (rule 11) and "One current
and one stale is a defect" (rule 13). Rule 14's "never random" clause survives
per CORE-1.

### CORE-7 — accept
Scope rule 6 to claims that carry weight: assertions about state, results,
verification, and completeness.

### CORE-8 — accept
Rule 12: add the retry clause — read current state before retrying a write
that appeared to fail.

### DL-1 — accept (Dave: option b)
Set `audience: [all-decision-roles, human]`. `all-decision-roles` is a new
reserved value: every role whose sessions are decision sessions. Its definition
and bundler expansion are Pass 2 work; do not edit the metadata policy or
`bin/` here. If `bin/check-frontmatter` rejects the value, stop and report.

### DL-2 — accept (Dave: LEXICON's definition)
Replace the opening test. A decision session decides and directs; the work a
directive specifies happens in an execution session. Do not define it by who
the session talks to.

### DL-3 — accept
Rule 15: "Every command block handed to someone else". Move the final bullet
(a value he will type is emitted as its own one-line paste block) out of rule
15 into its own rule under Blocks and dispatch.

### DL-4 — accept
Resolved by CORE-2. Rule 15 is now the sole statement; no edit to its criteria
beyond DL-3.

### DL-5 — accept
Add `order: 1` to the decision layer's frontmatter.

### DL-6 — modify (Dave)
Cut "Never stack questions" from rule 1. Keep *Never "executed."* and *Never
shell.* in rule 12 — criterion 6 does not reach contrastive definitions inside
a vocabulary entry.

### DL-7 — accept
Rule 12 baton entry: a baton passes between decision sessions only. The
writing-corpus collision is tracked in `inventory.md`; not addressed here.

### DL-8 — observation, no action
Carried to the cycles over `skills/spec-review-cycle.md` and `LEXICON.md`.

### DL-9 — observation, no action

## Execution

1. Verify the tree contains 063ab0f with no later edits to the two documents.
2. Apply every decision above. Renumber rules where deletions or moves change
   the count; then re-read both files end to end for any rule number cited in
   prose that is now wrong (core rule 13 applies to this edit).
3. Run `bin/check-frontmatter --all`. Stop and report on failure.
4. Commit both files on branch `gc-cycle-1-revision`, push to `origin`, report
   branch and SHA read back from git. Do not open a pull request. Do not flip
   `status`.

## Report shape

Per document: one line, rules before → after. Then branch and SHA. Then any
decision that could not be applied as written, with the reason.
