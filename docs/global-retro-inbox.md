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

### 2026-08-04 (3)

- **Standing behavior: self-contained test paste-blocks from sandboxed
  coder agents.** Dave repeatedly has to tell coder agents running inside
  Claude Code sandboxes: give me a paste-block that writes to files you
  control, not one that expects me to copy-paste output back to you. When
  a coder agent asks Dave to run tests outside the sandbox (e.g. against a
  live service, browser, or anything the sandbox can't reach), the
  paste-block it hands him should write its own output to a file/log the
  agent already has access to — not print to Dave's terminal for him to
  relay back manually. Proposed as standard behavior, not a one-off
  reminder each time.
  Likely home: a required-behavior line in `context-sets/base.md` (agent
  behavior, cross-role) or a role doc for the Coder specifically — not yet
  decided, batching per prior entries' disposition.

### 2026-08-04 (4)

- **Open question for retro consolidation: is GitHub MCP flakiness still
  real?** A lot of existing directives (MCP write-verification via
  independent fetch, timeout-recovery-by-reading-HEAD-first, small-writes-
  only during spec-review cycles) exist to handle GitHub MCP being flaky.
  Dave thinks this may have just been fixed but isn't sure. Action, not
  just an observation: **at retro-consolidation time, ask Dave whether he
  still believes it's fixed.** If yes, audit the above directives for ones
  that only exist to work around a problem that no longer exists, and
  propose removing/loosening them through the normal spec-review cycle.
  Do not preemptively relax any of the existing verification directives
  before that confirmation — this entry is a flag to revisit, not a
  decision to relax anything yet.
  (Mildly on the nose: GitHub MCP timed out three times in a row while
  logging this exact entry, before succeeding on retry.)

### 2026-08-05

- **Ticket-system topic for next retro: near-zero-friction ticket capture.**
  Dave needs a way to get small, quick items into a ticket system with
  effort on the order of "open tool, type five words, leave" — not a
  workflow that requires enough context-switch/ceremony that low-cycle
  moments just get dropped instead of captured. Distinct from this
  chat/inbox mechanism (which is for methodology-level retro material);
  this is about day-to-day project ticket creation (presumably GitHub
  Issues, per existing tooling, though the actual system isn't decided
  here). Not scoped or drafted — parked as a discussion topic for the
  next retro, not a design yet.

### 2026-08-07

- **Skill docs drift into persuasive register at a length that may hurt
  adherence.** `directive-dispatch.md` was long and persuasive rather than
  brief and directive — rules followed by paragraph-long justifications, war
  stories, meta-commentary. Dave's real-world observation: CoS often does not
  follow the skill closely, and length may be part of why. A compression pass
  this session ("make things less persuasive, shorter, and more directive")
  cut it ~46% (3071→1653 words) with every rule, the model table, and both
  command blocks preserved. Method: state the rule directively, cut the
  argument for it; where a rule's only record of a real failure was its war
  story, cut the story and rely on the external pointer (decision log, retro,
  the policy the rule already cites). Hypothesis to test: if CoS follows the
  compressed version noticeably better, that is evidence the *whole skill
  corpus* wants this pass. Candidate batch item: a directive-register
  compression sweep across all skills, with a shared "state the rule, cut the
  argument" convention captured somewhere governing (LEXICON or a meta-skill
  on how skills are written). The compressed `directive-dispatch.md` landed
  this session (commit 3e2487a).

- **Track B procedure gaps found by running it for real (first real Track B
  run).** Four distinct fixes, all landed in `directive-dispatch.md` this
  session except where noted:
  - *Download relocation.* The desktop client ignores chosen download location
    and writes to `~/Downloads`, appending a collision suffix (`name (1).md`)
    on name clash. Old mechanics assumed a chosen path. New flow: pre-flight
    `ls` establishes what is present, relocate block moves the exact filename
    into place and never inspects the destination (so it is correct for edits
    to existing files, not just new files), standalone sync block dropped.
  - *Pre-flight glob was wrong.* Globbed `<name>.md*` — but the collision
    suffix lands *before* the extension (`directive-dispatch (1).md`), so that
    glob misses every collision copy. Fix: glob on the **stem**
    (`<stem>*`). Dave's test caught this: four files present, the buggy glob
    matched one. Also reframed: the pre-flight surfaces state for Dave to
    judge, it is not a machine "count equals one" check, because a stem glob
    also catches legitimately-different files sharing the stem.
  - *Stale-artifact-in-pane hazard.* The reply carrying the pre-flight/relocate
    blocks must ALSO present the exact file those blocks move, in the same
    turn. Across a long session the artifact pane holds whatever was shown
    last; blocks referencing "the file" while a different file is displayed is
    a silent wrong-file hazard. Rule: artifact and blocks ship together or not
    at all. (Not yet written into the doc — batch item.)
  - *Emit the canonical filename as a copyable atom.* For a sharp operator,
    handing just the filename (its own paste-box, nothing else) is often more
    useful than a canned `ls`/`rm`/`cp` block — they assemble the verb around
    it faster than they can read a supplied block. Split: hand the name as an
    atom for operator-judged inspection steps; reserve whole tested blocks for
    load-bearing steps (the relocate/commit). (Not yet in the doc — batch
    item.)
  - *Append vs. replace.* The doc's Track B mechanics only cover whole-file
    replacement (`mv`). Appending to an existing tracker (like this inbox) is a
    different operation with a different re-run hazard: naive `cat >>` run
    twice appends twice. Needs a marker-guarded append (skip if the entry's
    dated heading already present). (Not yet in the doc — batch item.)

- **`bin/dispatch` deferral reasoning updated.** The doc previously said "Track
  B has never been run" as grounds not to build tooling. It has now been run
  (this session), and the run reshaped the relocate block. Claim corrected in
  the doc; build triggers restated (block stabilises across enough runs, or
  first hand-tweak needed).
