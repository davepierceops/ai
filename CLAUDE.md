# Claude Adapter

This file is an adapter for Claude-based tools. It is not the source of truth.

Authoritative project guidance lives under `/ai/`.

## Required reading

For substantial work, read these first:

- `README.md`
- `operating-model.md`
- the canonical specs under `specs/` (PRD, TRD)
- `context-sets/base.md`
- relevant context sets under `context-sets/`
- relevant policies under `policies/`
- relevant role documents under `roles/`
- relevant skill documents under `skills/`
- relevant boundary documents under `boundaries/`

## Operating model

Dave acts as PM, EM, owner, and operator. Agents are the implementation team. Dave does not default to human line-by-line code review.

Therefore, agents must produce evidence, not just plausible claims.

## Required behavior

- State assumptions.
- Keep scope clear.
- Work spec-first: specs and ACs before tests, tests confirmed failing before implementation.
- Keep test authorship and implementation in separate agents for the same unit of work.
- Get the human's go/no-go at the release decision for consequential changes; routine changes flow to release on evidence.
- Treat tests as bounded evidence.
- Distinguish mocked, contract, live, browser, and production verification.
- Update verification boundaries when mocks or integrations change.
- Produce change packages for meaningful changes.
- Identify known gaps and release risks.

## Core rule

Manage the proof, not the code.

## Collaborative document review

See `context-sets/collab-workflow.md`. That context set is the portable
source of truth for how Dave and agents collaborate during document authorship
and review. The rules there apply in full.
