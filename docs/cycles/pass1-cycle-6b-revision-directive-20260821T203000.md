# Directive — Pass 1, Cycle 6b: Core vocabulary matches the dispatch rule

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

Document in scope: docs/global-context/core.md @ e9229267dbff35feab5ff133fabdde0a0dcad8d1

## The rule (Dave, 2026-08-21, dictated)

A dispatch is one line — "Run the following in a [fresh | existing] session, model [frontier | solid | cheap]" — followed by one paste block: the execution block. The execution block's first instruction is to write the entire directive to a file, commit it, push it, and return the SHA in the report. There is no sync block. Nothing precedes the execution block.

## Decisions

### V1 — Sync block entry
Delete it.

### V2 — Execution block entry
Replace with: "a paste block of instructions an LLM agent session is to carry out. Its first instruction is to write the directive to a file, commit, push, and report the SHA. Never shell commands — those are command blocks."

### V3 — Directive entry
Replace with: "the complete package handed to an execution session: one line stating route (fresh or existing session) and model tier, then the execution block as a paste block. All three stated every time. A class may have defaults, stated like any other dispatch, the model default as a tier."

### V4 — Directive file entry
Keep; it already states the executor writes and commits it as its first act.

## Execution

1. Fetch origin/main; verify the tree contains e922926 with no later edits to core.md.
2. Apply V1–V3. Re-read the Vocabulary section and the rest of the file for any remaining reference to a sync block or to citing a directive by path and SHA before execution; fix per the rule above (Core 13). Do not touch any other file; other files stating the old rule are later cycles.
3. Commit on branch p1-cycle-6b-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

One line per entry changed, before → after, abbreviated. Then branch and SHA.
