# Session state — 2026-08-05, AI-9 co-authoring

Derived working brief, disposable. Nothing below is committed or agreed.

## What changed about the task

AI-9 was briefed as a greenfield `skills/directive-authoring.md` migrating
twelve rules. It is not greenfield: `skills/directive-dispatch.md` already
exists (draft, 2026-08-02) and covers route, model, and the
committed-file-cited-by-path-and-SHA rule. AI-9 landed instead as a revision
plus two new files. The triage board should be updated.

## Decisions taken

1. Two of the twelve rules (verbatim-as-pasted; capture output) are not
   directive rules — they constrain fenced command blocks. Own file.
2. The remaining rules fold into `directive-dispatch.md` rather than a new
   `directive-authoring.md`. That file is dropped.
3. `name` and `description` frontmatter required on every skill.
4. Anthropic's skill-authoring guidance is adopted as the standard:
   https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
   Key point: brevity is not the rule. Cut what the model already knows; keep
   rationale that encodes a failure mode it cannot infer. Bare imperatives
   (all-caps MUST/NEVER) are flagged as an anti-pattern — the model follows
   the letter and misses unanticipated edge cases.
5. A lexicon is built and "lexicon conformity" joins the skills conformance
   pass. `LEXICON.md` lives at docroot.
6. `directive` = a single direction to an LLM. `directive file` = the
   committed file containing one or more. `dispatch` = the act (route + model
   + citation).
7. `paste block` is the genus; `dispatch block` and `execution block` are
   kinds. An earlier rename retiring "paste block" was wrong and is reverted.
8. Existing `*-directive.md` filenames are not renamed. `docs/cycles/` and
   `reviews/` are not retrofitted — they are the record of what happened.

## Artifacts produced (uncommitted, in chat only)

| File | State |
| --- | --- |
| `LEXICON.md` | draft, reviewed in session |
| `skills/execution-blocks.md` | draft, reviewed in session |
| `skills/directive-dispatch.md` | draft revision — **needs the paste-block revert and a lexicon-conformity pass before it is landable** |

All three enter the normal spec-review cycle. No second door.

## Facts established tonight (do not re-derive)

- `handoff` carries six distinct senses in the repo: the cycle directive file
  (`spec-review-cycle.md:57`), a `roles/coder-agent.md` section, the
  decomposition doc (`chief-of-staff.md`), the end-of-session open-items flush
  (`collab-workflow.md:44`), passed-forward debt
  (`package-c-change-package.md:226`), and `AGENTS.md:36`. Unusable as a
  trigger term. Lexicon fixes the meaning; `spec-review-cycle.md:57` is the
  named misuse.
- `paste-block` already meant *execution block* in
  `docs/global-retro-inbox.md:80-86`. Left alone — inbox, not governed.
- `directive` blast radius: 115 occurrences in governed documents (~15 files),
  150 in `docs/cycles/` + `reviews/` (not retrofitted), plus `bin/cycle-open`
  and `bin/tests/test_cycle_open.py`.
- `BACKLOG-v2.md:90` says "paste block" for the dispatch-block sense —
  in scope for the rename.

## Open, in priority order

1. **Blocker on the conformance pass.** Do `bin/check-frontmatter` and
   `bin/flip-agreed` tolerate `name`/`description` as unknown keys, or fail
   closed? Verify against one file before touching eight.
2. Sequencing: does the conformance pass ride with this work or follow it?
   (Asked, unanswered.)
3. `bin/` changes for the directive/directive-file split are code with tests —
   red-gate applies, not a sed.
4. Lexicon conformance criteria for execution blocks duplicate the content of
   `skills/execution-blocks.md`. Pick one home.
5. Skill name `directive-dispatch` under the new lexicon — keep or rename.
   Recommendation: keep.
6. **New, not yet discussed:** gate tooling is too much friction. Raised
   2026-08-05, no analysis done.

## Captured mid-session from another chat — 2026-08-05

Dave's correction, verbatim intent: *"THE defect is sending me two paste blocks
when you expect to interact with me between them. Send me the first one. I'll
send its output. Which may or may not change the second one anyway. Then give
me the second one."*

**Rule.** When a human intermediary must relay output between paste blocks,
send one block per turn. Wait for the output. Then compose the next block.

**Why it is the defect and not a lesser one.** Block two written before block
one has run is written against a *guess* at block one's output. Batching does
not merely inconvenience the relay — it commits to an untested assumption and
hides that it did so. The second block looks equally authoritative either way.

**Boundary.** The rule binds blocks handed to a human who must carry output
back. It does not bind a single block whose steps an agent executes itself
without a human in the loop — a dispatch block legitimately bundles sync and
citation in one fence for that reason.

**Proposed home:** `skills/execution-blocks.md`. It is a delivery constraint on
paste blocks, not a directive-authoring constraint. Not yet drafted into the
file.

**Second-order observation, worth a retro pointer of its own:** the corrected
session responded to the correction by naming a lesser defect first. Dave had
to distinguish *a* defect from *the* defect explicitly. Misidentifying the
severity of one's own error under correction is a distinct failure from the
original error.
