# Trivium Reviewer Gate — Directive

Date: 2026-08-07
Route: fresh session
Model: Opus 5
Role: spec-reviewer-agent (hard gate)

## Documents in scope

Review each at origin/main @ `81bd2de` (PR #45 merged; read back from git).

- LEXICON.md
- skills/command-blocks.md
- skills/directive-dispatch.md
- skills/spec-review-cycle.md
- policies/remote-write-verification-policy.md

## Task

Act as spec-reviewer-agent. Gate-review each document above per
`roles/spec-reviewer-agent.md` and `policies/agent-review-policy.md`. Produce one
review artifact per document at `reviews/<doc-stem>-cycle-1.md`, following the
Review artifact schema in `skills/spec-review-cycle.md` — verdict-first header,
per-finding entries, omit-if-none fields.

## Constraints

- Verdict is `ready | ready-with-findings | changes-required`. Never `agreed` —
  agreement is Dave's, post-gate.
- Do not modify the documents under review. Do not flip `status` frontmatter.
- Evidence lines distinguish verified-by-running from inferred-by-reading. This
  is a docs repo: run `git log -S`, `git show <sha>:<path>`, and
  `bin/check-frontmatter --all` rather than inferring. A finding whose evidence
  line cannot be filled is an observation, not a finding.
- Cross-check each document against the others in scope and against the
  documents it cites (LEXICON terms; the policies and skills it points to) for
  consistency; record cross-checks in the header.
- Two of the five changed today (`command-blocks`, `directive-dispatch`:
  interactive-safe Track B guards, and the no-`exit`-in-pasted-blocks rule).
  Review the current state at the pinned SHA, not history.

## Output

Five committed review artifacts under `reviews/`, one per document. Commit
referencing this directive. Findings return to chat to open the triage cycle
(`skills/spec-review-cycle.md`). Do not agree, do not flip status.

## STOP conditions

- A document in scope is absent at the pinned SHA → stop and surface.
- An instruction here cannot be executed as written → stop and surface. No
  improvisation on canonical documents.
