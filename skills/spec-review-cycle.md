---
status: in-review
last-reviewed: null
audience: [spec-reviewer-agent, architect-agent, chief-of-staff, human]
---

# Skill: Spec Review Cycle

## Purpose

Execute one external-gate review cycle over spec documents (PRD, TRD, or any
canonical document) without full documents round-tripping through chat.

Chat is the decision layer. Claude Code is the execution layer. The spec
documents cross the chat boundary at most once, inbound, as uploads.

## Use when

- an external reviewer agent has produced gate findings against one or more
  canonical documents
- the findings require triage and document revision

For interactive co-authoring and artifact-pane review, use
`context-sets/collab-workflow.md` instead. This skill governs the
reviewer-gated cycle only.

## Hard constraints

- **One conversation per cycle.** Each cycle starts a fresh chat. Carry
  forward only reviewer findings and prior cycle directives — the directives
  are the decision record (rejections, dictated wording, deferred items).
  Never carry forward chat history.
- **Documents enter chat as uploads, never as mid-conversation fetches.**
  Upload the exact reviewed revision as attachments on the first message.
- **Full documents never leave chat.** No full-file pushes through MCP tools
  during a cycle. The cycle directive leaves as a paste block, so a cycle
  performs no tool-mediated write at all
  (`skills/directive-dispatch.md`; `policies/remote-write-verification-policy.md`).
- **Reviewed commit SHAs are recorded in the directive.** This is the
  staleness guard for uploads and the audit link from directive to reviewed
  state. A directive without SHAs is invalid. Mid-delta, those SHAs are on the
  tranche's spec branch, not the default branch (Reconciliation, below).

## Inputs

- reviewer findings (self-contained report from the reviewer agent)
- the reviewed documents, uploaded at the commit the reviewer reviewed
- prior cycle directive (pointer only, for continuity)

## Procedure

### 1. Triage (chat)

1. Start a fresh conversation. First message: reviewer findings + reviewed
   documents as uploads + reviewed commit SHA per document.
2. Triage each finding with Dave: **accept / reject / modify**. One finding
   at a time where judgment is required; batch the mechanical ones.
3. Record any wording or constraints Dave dictates verbatim.

### 2. Directive

4. Produce the cycle directive (format below) and emit it as a **paste block**.
   Chat does not commit it; the executor does, as its first act
   (`skills/directive-dispatch.md`). The directive names its own destination —
   `docs/cycles/cycle-<n>-directive.md`.
5. The cycle chat is done. Do not continue into execution in the same
   conversation.

### 3. Execution (Claude Code)

6. In the project clone, Claude Code writes the pasted directive verbatim to
   the named path, commits it, and reads the SHA back from git. It reports that
   SHA with its result — *"executed `<path>`, landed as `<sha>`"* — which is
   what the decision record cites.
7. Claude Code verifies the working tree matches the reviewed SHAs (or
   contains them in history with no intervening edits to the documents in
   scope); makes targeted edits per the directive; commits referencing the
   cycle number; pushes.
8. If a directive item cannot be executed as written, Claude Code stops and
   surfaces it — no improvisation on canonical documents.

### 4. Verify and re-gate

9. Dave reviews the git diff — the human control surface.
10. Hand the revised documents back to the reviewer for the gate re-check.
    Findings from that re-check open the next cycle at step 1.
11. On Dave's go, the agreement flip lands as a frontmatter-only
    status-transition commit, `last-reviewed` naming the review artifact and
    the reviewed SHA.

**Precondition on the agreement flip — enforced by tool since 2026-08-02.** The
expedited path in `policies/document-metadata-policy.md` makes
`reviews/expedited-log.md` a permanent `last-reviewed` target, which empties
the "the artifact exists" check for *every* document, not only expedited ones.
The rule that carries the weight instead is that the cited SHA must appear in
an entry in the log. `bin/flip-agreed` now enforces it, failing closed when the
cited SHA does not resolve to an entry in the log, and `bin/check-frontmatter`
reports the same condition over the in-scope set (`bin/aimeta/expedited.py`,
shipped red-then-green with its own acceptance criteria and tests, per Dave's
hard-precondition disposition after Package D — see the resolved entry in
`OPEN-ITEMS.md` for what the check does and does not cover).

### Fallback (no Claude Code available)

Claude outputs the edit set as old→new hunks in chat; Dave applies locally
and pushes. Full-file pushes through MCP remain prohibited.

## Reconciliation — the cycle that closes an open spec delta

During a tranche's execution, spec edits land on the tranche's spec branch with
no reviewer gate per edit (`context-sets/spec-and-change-discipline.md`, Open
spec delta). **Reconciliation** closes the delta, and it is this cycle, run over
the accumulated diff.

**What "once" quantifies:** the delta is gated once — as against once per edit —
not that a reconciliation may run only one cycle. A reconciliation that produces
blocking findings re-gates per step 10, exactly as any cycle does.

1. Bring the spec to full agreement with what was actually built. Reconciliation
   is not a review of intentions — a spec that still describes something the
   tranche did not build is not reconciled.
2. Open a pull request from `spec/<tranche-slug>` to the default branch. The
   diff under review is the whole delta, not one edit within it.
3. Run the cycle from step 1 of the Procedure, with the spec-branch SHAs as the
   reviewed revisions. Findings are triaged and executed against the spec
   branch; the PR updates in place.
4. On a clean gate, the pull request merges, and **then** Dave's agreement lands
   on the default branch as it always does: a frontmatter-only status transition,
   `last-reviewed` citing the review artifact and the reviewed spec-branch SHA.
   The order is load-bearing. Flipping on the spec branch first would set
   `agreed` on a branch that has not merged and might not, which is precisely the
   claim this design exists to make impossible; and the cited SHA still resolves
   after the merge, being an ancestor of the default branch.

**Why this holds `agreed` honest.** The default branch never carries unreviewed
spec text, so a document reading `agreed` there has in fact been through the
gate. What moved is *when* agreement attaches: to the version of record at
reconciliation, not to a version approved before building. Between deltas the
spec is true at rest, which is what the recreate-from-spec goal actually needs;
during one it is descriptive of decisions being made with hot context, and the
executor's requirement is truth-at-handoff, not agreement-in-advance.

**A reconciliation may be invoked early.** Dave may close a delta mid-tranche at
will, and frequent small reconciliations are the encouraged norm — the tranche
boundary is a deadline, not a target. A cycle over a small diff is cheap; a cycle
over a tranche's worth of accumulated edits is the expensive case this note
exists to discourage.

## Cycle directive format

```markdown
# Cycle <n> Directive — <project>

Date: <date>
Route: <fresh | existing context>
Model: <model — default Opus 5>
Track: <A | B>
Documents in scope:
- <path> @ <reviewed commit SHA>
- <path> @ <reviewed commit SHA>

## Decisions

### <finding id> — <accept | reject | modify>
Finding: <one-line restatement>
Resolution: <instruction to the executor; for "modify", exact intent;
for "reject", no action — recorded for audit>
Dictated wording: <pointer to the committed source — <path> @ <sha>, plus
field or section. Inline only where this directive is the origin of the
wording, in which case it is the source and downstream artifacts point here.
See `skills/directive-dispatch.md`.>

## Deferred / out of scope
- <item> — <where it is tracked>

## Execution notes
<constraints on how edits are made, if any>
```

Required fields: cycle number, route, model, track, documents in scope with SHAs,
one decision entry per finding (including rejections). Everything else as needed.

**All four requirements are stated per directive; fresh and Opus 5 are this
class's defaults.** `skills/directive-dispatch.md` requires every dispatch to
state route, model, track, and the execution block, and a reviewer-gated cycle
directive is no exception to that — it states all four, like any other dispatch.
What is specific to the class is which values it normally selects: **route
fresh** — one conversation per cycle, and execution starts a session that holds
none of it (Hard constraints above, and `skills/directive-dispatch.md` §1 Route)
— and **model Opus 5**, the selection that document's table makes for directive
execution over canonical documents (§2 Model). These are defaults, not fixities:
a cycle that needs existing context or a different model states that instead, and
the stated field governs. What route selects is the **execution** session
(`LEXICON.md`, the three layers): `existing context` names an already-running
*execution* session, and never releases the Hard constraints above or step 5's
prohibition on continuing into execution in the conversation that produced the
directive — whatever route is stated. The same framing is mirrored at
`skills/directive-dispatch.md` (Use when) and `LEXICON.md` (`Directive`).

## Review artifact schema

Review artifacts live in `reviews/` and are what `last-reviewed:` points at
(`policies/document-metadata-policy.md`), with one exception below. They are
read far more often than they are written, and almost always to answer one
question: *what did this review conclude?* So the verdict comes first, and a
clean pass stays short.

### What this schema governs

It governs the **artifact**. `roles/spec-reviewer-agent.md` and
`policies/agent-review-policy.md` govern the **review** — what must be
inspected and what must be reported. Where they name a required output, this is
where it goes:

| Required by the role / policy | Field here |
| --- | --- |
| Sign-off; Recommendation (the overall ship call) | `Verdict` |
| Required changes | entries marked `blocking` |
| Advisory items | entries marked `non-blocking` |
| Required follow-ups | per-finding `Fix` |
| Risks, verification gaps | `Consequence`, and `Not inspected` |
| Evidence inspected; Scope reviewed | `Scope`, `Cross-checked` |
| What Dave should inspect | `Dave should inspect` |

Note the entry field is `Fix`, not `Recommendation`.
`policies/agent-review-policy.md` uses "Recommendation" for the overall ship
call, and one word meaning two things across two canonical documents is the
ambiguity this table exists to remove.

**Filenames.** A review artifact is `reviews/<stem>-cycle-<n>.md`, where
`<stem>` is the reviewed document's basename without its extension and `<n>` is
the cycle number: `policies/document-metadata-policy.md` →
`reviews/document-metadata-policy-cycle-7.md`. The convention is mechanical on
purpose — `last-reviewed:` points at these paths and `bin/flip-agreed` validates
the pointer, so the path a reader needs is derivable from the document path
without looking it up. Where the stem already ends in `-cycle` or a digit, apply
the rule unchanged and let it repeat: this document's own artifacts are
`reviews/spec-review-cycle-cycle-1.md`. A special case would cost more than the
repetition does.

The schema governs artifacts written after it lands. **Existing artifacts in
`reviews/` are not retrofitted** — they are the review record of documents
already agreed, and rewriting a record of what happened to match a later format
would be the drift this repo exists to prevent.

One thing `last-reviewed:` points at is **not** an artifact in this sense:
`reviews/expedited-log.md`. The expedited path and the doc-only cycle in
`policies/document-metadata-policy.md` produce one line per agreement in a
shared append-only log, not a per-cycle document, and the header block above
would be absurd applied per line. The log's own format is specified where the
path is. The rule generalizes: this schema governs artifacts produced by a
review *cycle* — one document, one cycle, one verdict. A per-entry log is a
record of agreements, and its shape is defined by the policy that mandates it.

### Header

Every artifact opens with this block, clean pass or not:

```markdown
# Review: <document path> — cycle <n>

Verdict: ready | ready-with-findings | changes-required
Reviewed: <path> @ <sha, short or full>
Reviewer: <role, agent, or human>
Date: <YYYY-MM-DD>
Scope: <what was inspected>
Cross-checked: <other documents consulted for consistency, or none>
Not inspected: <stated explicitly — "nothing" is a claim, not a default>
Findings: <none | count by severity>
Prior cycle: <path to the previous review artifact, or none>
Dave should inspect: <the few items that need his judgment, or none>
```

`Cross-checked`, `Prior cycle`, and `Dave should inspect` are **omit-if-none** —
a clean pass should not have to write lines of `none`. The rest are required,
**including `Not inspected`**: that one is required precisely because omitting
it is how an unbounded claim gets made by accident.

`Verdict` is deliberately **not** the word `agreed`. `agreed` is the repo's
standing verb for a decision only Dave makes
(`policies/document-metadata-policy.md`), and `roles/spec-reviewer-agent.md`
forbids the reviewer from making it. `ready` means ready for Dave's agreement.

A clean or confirmation pass — one that finds nothing, or that confirms a prior
cycle's fixes — is this header and nothing else. No prose.

### Findings

One entry per finding, after the header:

```markdown
## <finding id> — <blocking | non-blocking | observation>
Claim: <one sentence — what is wrong>
Location: <path:line, or section name>
Evidence: <what was checked; verified by running vs. inferred by reading>
Consequence: <what goes wrong, concretely>
Fix: <what would resolve it>
Related: <other finding ids that are the same defect elsewhere, if any>
```

`Related` is **omit-if-none**; the other four entry fields are required.

`Evidence` distinguishing *verified by running* from *inferred by reading* is
not optional. In a documents repo, running `git log -S`, `git show <sha>:<path>`,
and `--help` is cheap, so *inferred by reading* should be rare. A finding whose
evidence line cannot be filled in is an observation, not a finding.

`Consequence` is the field that does the work. If you cannot state concretely
what goes wrong, the entry is an observation.

Order `blocking` entries by weight — the schema has one bucket for a design
hole and a wrong sentence, so the ordering is what carries the difference.

### Prose

Permitted where judgment genuinely does not compress — a material disagreement
between reviewers, or a risk that needs an argument rather than an assertion.
It is not the default, and it never replaces the verdict line.

### Why verdict-first

`last-reviewed` makes these artifacts load-bearing: a reader following the
pointer needs the conclusion, not the reasoning that produced it. Keeping the
clean case short also keeps the cheap case cheap — a review format expensive to
write is a review that gets skipped.

## Output

- A cycle directive, landed in git by the executor and cited by the SHA it
  reports back (audit trail)
- Revised documents committed by Claude Code, diff-reviewed by Dave
- Documents queued for reviewer re-gate
