# Global Retro Inbox

Tracker-class artifact. No lifecycle frontmatter — status is its content,
same treatment as `OPEN-ITEMS.md` and `BACKLOG-v2.md`.

## Purpose

Raw, timestamped capture of methodology-level observations as they occur —
not tied to any single project. This is candidate material, not a decision
record and not a methodology change. Anything here that becomes a real
proposal still enters through the normal spec-review cycle
(`skills/spec-review-cycle.md`) — no second door.

Distinct from `skills/conversation-retro.md`, which governs per-project,
per-conversation, evidence-grounded retrospectives stored in each project's
`retros/`. This file is global, freeform, and append-only at capture time;
schema/synthesis discipline applies later, when an entry is actually worked.

## Entries

### 2026-08-04

- **Per-project decision log.** Every project should have a decision log;
  agents acting as arbiters should write to it, using a consistent schema,
  for every non-trivial decision. Two distinct benefits, not one: (1)
  agents facing a plausible-options choice check it first instead of
  re-deciding; (2) accepted tradeoffs stop getting relitigated — an agent
  rediscovering known problem X on something already knowingly accepted
  should find the entry and stand down, not raise it as a fresh finding.
  (2) maps to the existing `Accepted risk` term in `context-sets/base.md`
  rather than needing new vocabulary.
  Sketch discussed: per-project, tracker-class (`decisions/`, storage
  family matches `retros/`), one immutable file per decision —
  never edited, only superseded by a new entry. Two entry types:
  `decision` and `accepted-risk`. Schema roughly: id, date,
  decision-maker (role), status (proposed/decided/superseded), context,
  options considered, decision, rationale, consequences, related
  decisions.
  Non-trivial threshold agreed: spec/ACs didn't fully determine the
  choice — a different competent agent could plausibly have chosen
  differently (architecture/design approach, dependency/tool choice,
  data model/interface shape, deviation from stated methodology or
  precedent). Anything in the commit-and-change-control consequential
  class is automatically non-trivial too. Trivial: naming, formatting,
  mechanical refactors, anything the spec fully dictates, anything
  already captured as a review-artifact finding.
  Behavioral implication flagged, not yet drafted: this needs a *consult*
  obligation in agent behavior (likely `base.md` Required Behavior), not
  just a write schema — check the log before deciding, check for a
  matching `accepted-risk` before raising a finding, propose reopening
  explicitly rather than silently re-raising.
  Dave's disposition: don't draft the skill yet. Hold this for a batch
  evaluation alongside upcoming retros — expects several inbox/retro
  items will cluster into a single spec-review pass more efficiently
  than one-off handling.
