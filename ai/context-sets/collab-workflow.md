---
context-set: collab-workflow
purpose: How Dave and agents collaborate during document authorship and review.
include-when: Any chat that involves writing, editing, or reviewing methodology or project documents.
depends-on: [base]
---

# Context Set: Collaboration Workflow

Status: draft

This context set defines how Dave and agents work together when authoring,
editing, and reviewing documents. It applies to methodology documents and
project documents alike.

## Document review

When reviewing a document with Dave:

- Put the document under review into an artifact (right pane); discuss in chat
  (left pane).
- One document at a time. Do not advance to the next document until Dave signals
  done.
- In a multi-document review, when Dave says "ship", "done", or equivalent:
  mark the current document complete, load the next document into the artifact,
  and begin the review — all in one response.
- Claude drafts edits; Dave approves in the artifact before anything is locked.

## Authorship

- Claude drafts, Dave verifies. Agents propose; Dave disposes.
- Drafts of specs, fixes, and decisions are produced for Dave's review before
  being treated as agreed.
- One question at a time. When something needs Dave's input, ask a single
  question and wait rather than batching several decisions into one message.
- No assumptions on consequential calls. When a decision is Dave's, frame the
  tradeoffs clearly and ask. Do not decide on Dave's behalf.

## Session handoff

- Open items, deferred decisions, and outstanding fixes are tracked in
  `ai/OPEN-ITEMS.md` and flushed at the end of each work session.
- Session state is packaged as a zip for handoff between sessions; do not rely
  on chat history as the sole record of decisions made.
