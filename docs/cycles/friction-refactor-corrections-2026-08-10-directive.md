# Directive: Friction Refactor Corrections — 2026-08-10

Route: fresh
Model: Opus 5
Execution block: this directive travels as a paste block. Your first act —
before any other work — is Step 0 below.

Note: this directive states route, model, and execution block only. Track is
retired by item C1 below; this directive is written to the post-C1 rule.

## What this is

Morning-triage corrections to the branch `methodology/friction-2026-08-09`,
decided by Dave on 2026-08-10 after reviewing the overnight run. Same autonomy
model as the parent directive
(`docs/cycles/friction-refactor-2026-08-09-directive.md`): decide and log where
you would normally ask, self-review until clean, nothing merges, nothing flips
to `agreed`. Work on the **existing branch** — do not branch from main.

## Step 0 — Land this directive

1. `git fetch origin` and check out `methodology/friction-2026-08-09` at
   origin HEAD.
2. Write this directive, verbatim and in full, to
   `docs/cycles/friction-refactor-corrections-2026-08-10-directive.md`.
3. Commit, push, record the SHA for the report.

## Binding decisions

### C1 — Tracks are removed entirely

The overnight run kept `Track` and redefined it as the executor's repository
environment (its decision D1). Dave reverses this: the surviving sense covers
only "the remote is unreachable," and forge downtime does not warrant standing
instruction lines. **This explicitly reverses DEC-000150's stated-field
requirement as it applies to track** — record the reversal in the decisions
log, citing DEC-000150, formatted for Dave to promote to `decisions/log.md`.

- The four requirements become **three**: route, model, execution block.
  Every statement of "all four" changes everywhere it appears.
- LEXICON: Track A / Track B entries are removed. Leave a tombstone in the
  retired-terms style of the Prompt entry (C4): not a term of this
  methodology; the unreachable-remote case is handled by the executor
  stopping and surfacing (`skills/directive-dispatch.md`).
- `skills/directive-dispatch.md`: requirement 3 deleted; the
  unreachable-remote behavior survives as an executor obligation — an
  executor that cannot push **stops and surfaces it**; it does not silently
  commit locally and report a same-machine SHA as if pushed.
- Sync block: LEXICON and directive-dispatch lose the Track A scoping; the
  sync block precedes every execution block, full stop.
- `policies/remote-write-verification-policy.md` Rule 4: Dave confirmed the
  rule stays (his triage, 2026-08-10). Sweep its text and Scope section for
  track language; the detector's action is "stop and establish state,"
  which no longer needs a track to point at.
- TP-1 (`bin/cycle-open`, shelved): its spec references tracks. Disposition:
  annotate the backlog entry that the track field is retired, so an
  unshelving doesn't resurrect it. Do not rewrite the shelved spec.
- Sweep the whole branch: `grep -ri "track" --include="*.md"` and judge each
  hit. Historical records (review artifacts, decision logs, status-of-draft
  notes, `docs/cycles/`) are **not** retrofitted — they record what was true
  when written. Living canonical text is conformed.

### C2 — "Baton" names the decision-to-decision handoff artifact

- New LEXICON entry under Handoff:

  > **Baton** — the artifact a decision session hands to its successor
  > decision session: the composed package of unfinished responsibility —
  > state, open questions, decisions in flight — that lets the receiver
  > continue without the conversation that produced it. A baton passes
  > between decision sessions; a directive dispatches work to an execution
  > session. The two never blur.

  Adjust wording to the LEXICON's register; the boundary sentence is the
  load-bearing part.
- This closes `OPEN-ITEMS.md:800` ("a handoff into another decision session
  has no name") — strike it per that file's convention.
- Touch-rule sweep: where existing text describes the artifact (not the act)
  of a decision-to-decision handoff, conform it. Candidates the triage named:
  the end-of-session flush framing in `context-sets/collab-workflow.md`, the
  handoff entry's own prose. The change-package forward-debt use in
  `roles/coder-agent.md` context is coder-to-successor and stays "handoff."

### C3 — `.prompts/` machinery is retired

- `roles/chief-of-staff.md`: the "Prompt generation — at execution time, not
  before" subsection is removed. Its replacement is one sentence stating the
  standing rule: work is dispatched per `skills/directive-dispatch.md`; the
  decomposition doc is the source the directive derives from. Nothing else
  from the subsection survives — `.prompts/` files were never written and the
  one-line-kickoff practice it predates is itself superseded by the paste
  transport.
- Remove `.prompts/` from `.gitignore` if present.
- Sweep for other `.prompts/` references.

### C4 — "Prompt" is retired as a methodology term

- The LEXICON Prompt entry becomes a tombstone — an entry that exists only to
  deflect:

  > **Prompt** — not a term of this methodology. What is meant is one of:
  > *directive*, *execution block*, *instruction*, *command block*, *baton*,
  > or, for inbound material a session acts on (reviewer findings, execution
  > reports, uploads), the specific name of that material. The colloquial
  > sense — any text sent to an LLM — is too broad to do work here.

- **Do not trust the term list above.** Sweep the LEXICON and every skill for
  the full set of typed-at-or-consumed-by-a-session artifacts and make the
  tombstone's routing exhaustive. Dave's triage caught an incomplete
  inventory produced from memory (missing baton, companion document,
  reviewer findings, uploads); the sweep is the fix, and this instruction is
  the record of why.
- Sweep living canonical text for "prompt" used as a term and replace with
  the precise word. Same historical-record exemption as C1.

### C5 — test_sc1 fixed (explicitly permitted outside blast radius)

- The two `test_sc1` failures pre-existing on origin/main assert a hardcoded
  in-scope list omitting `LEXICON.md`, stale since 1f5b715. Fix the **test**
  to match the policy's actual in-scope rule. If the in-scope set is
  derivable rather than listable, prefer deriving it so the test cannot go
  stale the same way twice; log the choice either way.
- `bin/tests/run` must end ≥ 349/350 (test_bn10 remains known-failing and
  tracked; do not touch it).

## Self-review and decision log

Per the parent directive's model: reviewer-role pass over the changed set,
artifacts to `reviews/` on the branch continuing each document's cycle
sequence, marked self-review; fix blockings; cap 5 cycles. Decision log
continues in `docs/cycles/friction-refactor-2026-08-09-decisions.md` —
append a dated section, numbering continuing from D20.

## Hard constraints

Parent directive's constraints hold: no merge, no push to main, no
force-push, no `agreed` flips, `decisions/log.md` untouched, no `gh`.
Blast radius is C1–C5 plus required consistency edits; C5 is the one
permitted exception and is bounded to the test file(s) it names.
An instruction that cannot be executed as written → stop that item, log it,
continue with the rest.

## Final report

Triageable by CoS, opening with "executed `<path>`, landed as `<sha>`":
branch HEAD; documents changed one line each; grep-sweep counts for C1 and
C4 (hits found / conformed / exempted-as-historical); test run result;
review cycles and final verdicts; decision-log entries added, flagging any
needing Dave's eye.
