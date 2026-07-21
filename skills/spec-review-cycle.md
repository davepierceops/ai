# Skill: Spec Review Cycle

Status: draft

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
Dictated wording: <verbatim, if any — executor must use as-is>

## Deferred / out of scope
- <item> — <where it is tracked>

## Execution notes
<constraints on how edits are made, if any>
```

Required fields: cycle number, documents in scope with SHAs, one decision
entry per finding (including rejections). Everything else as needed.

## Output

- A committed cycle directive (audit trail)
- Revised documents committed by Claude Code, diff-reviewed by Dave
- Documents queued for reviewer re-gate
