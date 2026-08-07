---
status: draft
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
  during a cycle. The only MCP write is the cycle directive (small).
- **Reviewed commit SHAs are recorded in the directive.** This is the
  staleness guard for uploads and the audit link from directive to reviewed
  state. A directive without SHAs is invalid.

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

### 2. Directive (handoff artifact)

4. Produce the cycle directive (format below). Commit it to the project repo
   at `docs/cycles/cycle-<n>-directive.md` — one small MCP write.
5. The cycle chat is done. Do not continue into execution in the same
   conversation.

### 3. Execution (Claude Code)

6. In the project clone, instruct Claude Code: execute the directive against
   the documents per this skill.
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

## Cycle directive format

```markdown
# Cycle <n> Directive — <project>

Date: <date>
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

Required fields: cycle number, documents in scope with SHAs, one decision
entry per finding (including rejections). Everything else as needed.

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

- A committed cycle directive (audit trail)
- Revised documents committed by Claude Code, diff-reviewed by Dave
- Documents queued for reviewer re-gate
