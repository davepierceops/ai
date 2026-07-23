---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Skill: Conversation Retrospective

## Purpose

Produce one retrospective per LLM conversation about a software project,
in a fixed schema, grounded in evidence from that conversation. The
retrospectives form a per-project corpus for later synthesis into
methodology changes and published writing.

Retros are an input to change, not a change mechanism. Any methodology
revision surfaced by a retro or a synthesis enters the repo through the
normal spec-review cycle. There is no second door into `agreed`
documents.

## Use when

- a working conversation on a project has concluded (or reached a
  natural boundary) and its durable lessons should be captured
- Dave directs a retro explicitly

Do not run retros on cycle chats governed by `skills/spec-review-cycle.md`
unless directed — their decision record is the cycle directive.

## Principles

- **Evidence-grounded.** Every observation cites what actually happened
  in the conversation. Separate Evidence from Interpretation explicitly.
- **Durable over incidental.** Capture techniques, workflows, belief
  changes, and engineering practices that transfer. Omit implementation
  details that do not.
- **New or evolved only.** Emphasize ideas that are new or materially
  changed in the session. Restating standing methodology is noise.
- **Accuracy over completeness.** Prefer omission to speculation. If the
  conversation contains few or no durable insights, the retro says so
  explicitly — a near-empty retro is a valid and useful result.
- **Structurally identical.** Every retro uses the schema below, so the
  corpus concatenates cleanly for synthesis.

## Storage

- Retros live in the project repo at `retros/`, sibling to the project's
  review artifacts. They are local project history and never travel to
  the methodology repo.
- Retros are state/tracker-class artifacts: exempt from
  `policies/document-metadata-policy.md` — no lifecycle frontmatter
  (`status`, `last-reviewed`, etc.). Their status is their content.
- The header block in the retro schema below is synthesis metadata
  (project, date, source pointer), not governance metadata. It serves
  corpus tooling and carries no lifecycle semantics.
- Pre-adoption corpora (e.g., Catchable's existing retros) are
  grandfathered as-is. Data, not governed documents.

## Filenames

`retro-<YYYYMMDD>-<HHMMSS>.md`, timestamp at generation time.

Filenames are opaque, collision-free handles only — never parse them for
meaning. The schema header is the canonical identity of a retro. This
convention is provisional and may be replaced; because no tooling reads
filenames, replacement is a pure rename.

Never generate "random" strings, hashes, or UUIDs for filenames — LLMs
repeat "random" strings and collide. If timestamp precision is
unavailable, emit `retro.md` and rename on save.

## Retro schema

```markdown
---
project: <project slug>
date: <YYYY-MM-DD>
source: <conversation pointer: title, URL, or export filename; null if none>
---

# Retro — <project> — <date>

## Context
<one paragraph: what the conversation was about, what was attempted>

## Evidence
<numbered, concrete observations of what happened; quotes or close
paraphrases of pivotal moments; no interpretation here>

## Interpretation
<what the evidence suggests; each item references the evidence numbers
it rests on>

## Durable insights
<techniques, workflow changes, belief changes that transfer beyond this
session; empty-with-a-statement if none>

## Candidate methodology changes
<specific proposed edits to methodology documents, if any, phrased as
inputs to a future review cycle — not as decisions>
```

## Synthesis

- **Project synthesis:** performed over a project's `retros/` directory.
  Output is a synthesis document in the same directory, clearly marked
  as synthesis, never overwriting source retros.
- **Cross-project synthesis:** a read operation, not a storage
  arrangement — concatenate the relevant `retros/` directories from
  local clones as needed. No shared corpus repo.
- Synthesis outputs feeding methodology changes are packaged as findings
  for a spec-review cycle.

## Output

- One Markdown file per conversation, delivered as a downloadable
  artifact where the client supports it; otherwise exactly one fenced
  Markdown block containing the entire document and nothing else.
