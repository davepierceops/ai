### 2026-08-04 (2)

- **Portable `/retro`-style capture command, per repo.** A few-keystrokes
  invocation ("`/retro <note>`" or similar) that tells the LLM to append
  the note to that repo's inbox — the same mechanism just built ad hoc in
  this chat (`docs/global-retro-inbox.md`), generalized into something
  every repo gets, including `davepierceops/ai` itself. Would apply
  equally to project repos' `retros/`-adjacent capture and to this repo's
  global inbox.
  Relationship to existing artifacts: distinct from
  `skills/conversation-retro.md` (whole-conversation, evidence-grounded,
  triggered at a natural end) and from the decision-log idea above
  (structured, schema'd, decision-specific). This is the lightest-weight
  of the three — arbitrary freeform notes, low-friction, no schema at
  capture time.
  Dave's observation: once this exists for the `ai` repo itself, this
  chat thread (used as an ad hoc inbox front-end) becomes unnecessary —
  the command replaces it.
  Not drafted yet — batching with the decision-log item and upcoming
  retros per the prior entry's disposition.
