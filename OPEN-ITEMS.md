# Open Items

This file tracks open questions, deferred decisions, and outstanding fixes
for the AI operating model. Updated at defined checkpoints per
`context-sets/spec-and-change-discipline.md`.

Last updated: 2026-08-02

---

## wne-crm migration to current methodology — ad hoc first, extract adoption skill after

**DECIDED 2026-08-02 (chat), execution pending.** Bring wne-crm from the
old-iteration methodology to current, running the migration ad hoc, then
extract `skills/project-adoption.md` from the experience; catchable runs
under the drafted skill as its first validation before the skill gates to
`agreed`. Working plan (from the chat session; not yet a governed artifact):
install the shim/hook via the sibling-directory convention; frontmatter
migration of wne-crm governed docs with the grandfather-clause disposition
list + adoption record; move the kickoff bundle to the current 7-file
target; template reconciliation decision (existing PRD/TRD predate current
templates); stand up `retros/`. Precondition satisfied 2026-08-02: the cos
supersession package is fully landed.

---

## gh CLI TLS verification failure in the Claude Code sandbox — workaround used, cause unknown

**OPEN.** During cos-supersession execution (PR #13), `gh` could not verify
api.github.com's TLS certificate in the sandbox; the session created the PR
via `curl` using gh's stored token. Unresolved: whether curl verified the
cert (benign CA-bundle gap in gh) or ran unverified (token sent over an
unauthenticated connection). Next session: `curl -v https://api.github.com`
and inspect how the workaround was invoked. Until understood, treat
extract-token-and-curl as a deliberate exception, not a habit.

---

## Directive-execution mechanics are oral tradition — kickoff prompts restate governed rules

**Source:** chat triage session, 2026-08-02, at the dispatch of
`docs/cycles/triage-2026-08-02b-directive.md`. The kickoff prompt drafted for
the executor session ran ~30 lines. On inspection, every line was one of two
defects: a restatement of rules the directive or the canonical text behind it
already states (red-gate, no-flip, executor recusal, branch-plus-PR,
stop-and-surface), or a session mechanic with no canonical home at all,
re-invented at every dispatch — pull first and record the SHA executed, branch
naming, verify every push in `git log` before reporting it, run `bin/tests/run`
and `check-frontmatter --all` before opening the PR, report shape, STOP
semantics. Dave rejected the prompt and named the defect: a per-dispatch
restatement is an unversioned derived copy of governed text, and derived
copies written fresh drift — the same defect class as the pending-gate rule's
"derived body" clause and the write-access-boundary rationale. Worse, if the
executor *needs* the restatement to comply, that is the load-bearing-context
failure relocated from bundles to prompts.

**The rule, effective now:** a kickoff prompt is one line — "Execute
<directive path> from origin/main HEAD." Anything more is a signal of a gap in
canonical text; fix the gap there, once. (The b-directive execution ran on the
one-line kickoff and delivered clean, which is one data point that the
restatement was ceremony.)

**What's needed:** `skills/directive-execution.md` via normal
drafting-and-review process, giving the session-level mechanics above one
canonical home. When drafted, assess it against the expedited path's
ineligibility criterion — it states verification steps that function as
enforcement rules, so under the criterion-primary reading it is likely
ineligible whether or not it is ever named in the list.

---

## AC-CF-23 is silent on the likely failure — a single typo'd in-scope glob

**Source:** Package A release decision, 2026-08-01. Accepted as a known gap at
the human gate; recorded here so it is tracked rather than absorbed.

`bin/check-frontmatter --staged` warns (`WARN [empty-scope]`) when the in-scope
glob set matches **no** tracked path — the total-no-op case. Verified at the
gate: when one glob is typo'd (`policies/**` → `polices/**`) while the others
still match, the hook is **silent**, and a content edit to an `agreed` document
in the affected directory commits with `status: agreed` intact and no
diagnostic. That is the more likely failure of the two, and it is the one not
covered.

**Why it was scoped that way:** per-glob `WARN [unmatched-glob]` lines exist in
`--all` and were deliberately kept out of `--staged`, because a project repo
legitimately matches only `specs/**` and would emit warnings on every commit.
The AC was written against the rarer case; that was an authoring error at the
spec level, not an implementation defect.

**Current mitigation:** run `check-frontmatter --all` after any edit to the
metadata policy's Scope section. This is a habit, which is exactly the class of
control this initiative exists to replace.

**What's needed:** a diagnostic that distinguishes "this glob legitimately
matches nothing in this repo" from "this glob used to match and no longer
does." Candidate: compare the matched set against the previous commit's, and
warn only on a glob that lost all its matches. Unverified — the design is not
settled, which is why this is an open item rather than a fix.

---

## Write-access boundary for ai/ — read-only except OPEN-ITEMS.md (DECIDED, pending policy incorporation)

**Decided by Dave, 2026-07-31, effective immediately:** project sessions
(any agent working a project repo, in any role) treat everything in this
repo as read-only, with one exception: `OPEN-ITEMS.md`. Sessions may
append or amend open items here to capture methodology observations,
decisions, and gaps as they surface — that is the designed intake path.
All other files (roles, policies, context sets, skills, boundaries,
`operating-model.md`, README, MANIFEST) are canonical and change only
through this repo's own drafting-and-review process, in sessions whose
purpose is methodology work.

**Rationale:** canonical methodology docs changing as a side effect of
project sessions is the same defect class as spec drift — untracked,
unreviewed mutation of a source of truth. The single writable surface
gives project sessions somewhere to put what they learn without opening
that door. (This very entry is the worked example: the rule was decided
in a project session and recorded here rather than written into
`operating-model.md` directly.)

**What's needed:** fold the rule into canonical text — likely
`operating-model.md` "Relationship to tools" and/or a `boundaries/` doc,
plus a line in `roles/chief-of-staff.md` — via normal process. Until
then this entry is the binding statement.

---

## Model selection by role — make cost/capability a per-role, per-step decision

**Source:** wne-crm Orchestrator session, 2026-07-31 (cycle-10 closure). A
frontier-tier model ran the Orchestrator role for a session that was
majority-mechanical (SHA bookkeeping, write-verify loops, ref discipline,
handoff maintenance). The methodology names roles and session boundaries
but is silent on which model tier each role warrants — every session
implicitly inherits whatever model the operator happens to open.

**The observation:** the evidence model already externalizes much of the
safety. Where errors are detectable by construction — stats-guarded
writes, red-gates, verify-before-assert, re-gates — a cheaper model is
safe, because the guards catch drift regardless of who drifts. Capability
was load-bearing in that session at exactly three points: treating a
one-line stats anomaly (+3/−3 vs. expected +2/−2) as a stop condition
rather than noise; inventing a new guard mid-session (the stats-expectation
check on full-file MCP writes); and byte-exact long-context reproduction
of a ~107KB document. Judgment-dense work — spec-cycle triage, reviewer
disagreements, directive drafting with STOP conditions, handoff synthesis —
propagates mistakes into canonical documents and stays frontier.

**What's needed:** a methodology update — probably a section in
`operating-model.md` plus a line per role doc — covering:

1. **A model-tier recommendation per role,** chosen at session open the
   same way the role is chosen. Working hypothesis from the source
   session: efficient tier for Orchestrator-as-executor, Coder on routine
   packages, and mechanical directive execution; frontier tier for
   Spec Reviewer, Skeptic/Risk, Architect, spec-cycle Orchestration, and
   anything drafting canonical text.
2. **Assignment criteria,** not just a static table: (a) are this role's
   errors detectable by construction — i.e. do externalized guards catch
   them? (b) is long-context fidelity load-bearing? (c) do this role's
   judgments propagate into canonical documents or gates? Two or three
   "yes" answers → frontier.
3. **An evidence step before demotion:** trial the cheaper tier on a
   routine package with all guards active; the guard-fire rate is the
   signal. Tier decisions are recorded with that evidence, per the core
   rule — not assigned by intuition, including the intuition of the
   frontier model that proposed this item.
4. **Vendor neutrality per the tooling rule:** durable policy speaks in
   tiers (frontier / efficient), never model names. Concrete model
   choices live in per-project configuration, same as the flag-backend
   pattern.

**Note:** interacts with the session-boundary habit (fresh chat per
phase) — the phase boundary is the natural tier-switch point, so this
costs nothing operationally once the recommendation exists.

---

## Per-project frontmatter enforcement as a project-setup step

**Source:** Document metadata policy cycle-2 revision session, 2026-07-21.
The revised `policies/document-metadata-policy.md` mandates that every
project applying this methodology adopts the metadata schema for its spec
documents — adoption is not optional. But the methodology repo's hooks
cannot reach project repos, so each project must stand up its own
enforcement.

**What's needed:** "Stand up frontmatter enforcement" becomes a defined
project-setup step. This belongs in the per-project TRD/setup guidance
covering CI/CD mechanics — currently deferred territory per the v0.4
decision to map deploy/release mechanics in per-project TRDs. When that
guidance is written, include the frontmatter hook as a required setup item.
Blocked on the policy reaching `agreed`; sequenced with the CI/CD mechanics
mapping.

---

## ~~Build this repo's frontmatter-enforcement hook~~

**RESOLVED** by Package A (F1), 2026-08-01. `bin/check-frontmatter` plus the
managed pre-commit hook installed by `bin/install-hooks` enforce the in-scope
set, read from the policy at runtime.

Struck by Package D, 2026-08-02, on the handoff in
`docs/packages/package-c-change-package.md` §9. The entry had gone on asserting
"Blocked on the policy reaching `agreed`" after the policy was agreed, the hook
was live, and the work had shipped — a live tracker asserting a blocker that no
longer exists.

---

## ~~Migrate existing docs to YAML frontmatter per document-metadata-policy~~

**RESOLVED** by Package B (F2), 2026-08-01. 34 documents migrated to YAML
frontmatter with a repo-wide disposition list under the grandfather clause; one
batch gate review.

Struck by Package D, 2026-08-02, on the same handoff as the item above, for the
same reason: it still read "Blocked on the policy itself reaching `agreed`".

---

## ~~`bin/bundle` supersedes MANIFEST's bundle definitions~~ — WITHDRAWN

**Withdrawn 2026-08-01 by the Package C gate review**, which found the premise
false. The streamlining directive deferred this as "after F4 lands and closure
output is trusted"; F4 landed, and the deferral does not survive contact with
the tool.

`bin/bundle` computes a reference closure — what a document cites. A bundle is
a curated judgment — what a conversation needs. Measured against "Spec chat"
(`base` + `spec-and-change-discipline` + `ai-native-engineering`): unbounded
closure returns every context-set plus trackers and historical artifacts;
`--max-depth 1` returns two and misses `ai-native-engineering`. No depth returns
three — the count goes 2, 4, 6 — because `bin/bundle` walks two graphs that fail
in opposite directions: `depends-on` is too sparse (every context-set points
only at `base`), and in-body citations are too dense and not curatorial
(`ai-native-engineering` arrives at depth 2 as a citation inside a policy). The
distinguishing information is in each set's prose `include-when:` field, which
is editorial judgment, not a reference.

**Consequence:** `MANIFEST.md` is not pending automation by `bin/bundle`, and
both files now say so.

**The door left open, deliberately.** What was disproved is that *closure*
derives a bundle. What was not disproved is that bundles could be derived at
all: declaring membership as data — a `bundles:` frontmatter key, or a small
`bundles.yaml` — relocates the judgment into machine-readable form without
removing it. Not proposed, not costed, and a different change from closure
computation. **Enriching `depends-on` to fake it is rejected**: co-selection is
not dependency, and encoding it there corrupts the field for every other
consumer. If membership-as-data is ever built, MANIFEST's lists become a second
copy of a derivable fact and should move.

---

## ~~`TREE.txt` mention survives in the agreed metadata policy~~

**RESOLVED** by Package D, 2026-08-02, exactly as this entry planned: the rider
rode the F6 cycle that opened the document for a substantive reason, and the
mention left the out-of-scope list in the same diff the reviewer read.

Confirmed inert on the way out, by the cycle-5 gate review rather than on the
executor's say-so: `bin/aimeta/scope.py` stops parsing at the `Out of scope`
marker, so enforcement never read the prose; `check-frontmatter --all` and the
321-test `bin/` suite are unchanged by the removal.

---

## ~~The expedited path's log entry is unenforced — `flip-agreed` checks existence, not content~~ — PRECONDITION SATISFIED

**RESOLVED** by `docs/cycles/triage-2026-08-02b-directive.md` (W-2), 2026-08-02.
Tests `2556226` (red: 15 tests, 6 failing); implementation `4e90b03` (green:
336 tests, 0 failing). New `bin/aimeta/expedited.py` decides
the rule; `bin/flip-agreed`'s `check_review` and `bin/check-frontmatter`'s
`check_worktree` both consult it.

All four ACs below are implemented and covered. Two notes on what was decided
inside them, so the reading is not left to the next reader:

- **What counts as an entry.** A Markdown list item carrying `@ <sha>`, per the
  format the log documents. A SHA appearing only in the log's header prose does
  not satisfy a pointer, and there is a test for that.
- **`--staged` is deliberately not covered,** and this is the one place the
  implementation is narrower than a maximal reading of "over the whole in-scope
  set". The AC names `check-frontmatter`, and `check_worktree` serves both
  `--all` and path mode; hook mode was left alone because the log rule is a fact
  about the repository's review record rather than about the staged change, and
  a blocking hook that consults a file outside the commit can refuse a commit
  for a condition that commit did not cause. **Consequence, stated rather than
  absorbed:** a hand-edited frontmatter pointer at a log SHA that does not exist
  still commits, and is caught by the next `--all` run rather than at the hook.

**The precondition on the next agreement flip is satisfied.** The flip itself
remains gated: it needs the reviewer re-gate and Dave's approval, and this
directive does not authorize it.

**Original entry, kept for the record:**

**Source:** Package D cycle-5 gate review (B4), 2026-08-02. Verified by
running, in a scratch clone: with step 3 of the expedited sequence **skipped
entirely**, `bin/flip-agreed --review 'reviews/expedited-log.md @ <sha>'` exited
0 against a log holding no entries, and `check-frontmatter --all` then reported
the repo clean.

**Why it matters now and did not before.** A per-cycle review artifact had to be
*created* to satisfy the existence check, so existence was weak evidence that a
review happened. `reviews/expedited-log.md` exists permanently, so the same
check is satisfied vacuously and forever, for every document in the repo. The
policy now states the rule that carries the weight — the SHA cited in
`last-reviewed` must appear in an entry in the log — but nothing checks it.

**What's needed:** `bin/flip-agreed` (and probably `bin/check-frontmatter`)
verify that the cited SHA appears in the target artifact when that artifact is
the expedited log. Small and checkable. It is a `bin/` change with its own ACs
and tests, which is why it is not inside Package D — F6 is a routing change, and
the directive scopes Package D to F6 alone.

**Disposition at the Package D gate, 2026-08-02.** Named as a release risk, not
absorbed, and Dave decided: it does **not** block the Package D flip, because
the expedited path has zero addressable documents and therefore zero exposure.
It **is a hard precondition on the next agreement flip**, when a second document
reaches `agreed` and the exposure stops being zero. The check ships in `bin/`
with its own acceptance criteria and tests before that flip runs.

The ACs it needs, so the work starts from a spec rather than a description:
`flip-agreed --review` resolves the cited SHA against the target artifact's
contents when that artifact is the expedited log, and fails closed when the SHA
is absent; abbreviation is normalized through `git rev-parse` before comparison,
per the policy's stated rule; a non-log artifact keeps today's
existence-only behaviour; and `check-frontmatter` reports the same condition
over the whole in-scope set.

Recorded at the trip point as well as here: `skills/spec-review-cycle.md` step
11 states the precondition where the next cycle will actually run the flip.

---

## A policy edit can blind enforcement of itself — the self-referential scope hazard

**Source:** Package D cycle-5 gate review (B2), 2026-08-02. Pre-dates F6;
surfaced by testing F6's blast radius.

**Verified by running,** in a scratch clone: a single commit deleting the
`policies/**` line from the metadata policy's in-scope list dropped enforcement
from 38 files / 8 globs to 31 / 7, and the committed file still read
`status: agreed` with its prior `last-reviewed` intact — because
`bin/aimeta/scope.py` reads the globs from the policy on disk, so by the time
the hook evaluated the commit the file had already removed itself from scope and
the flip never fired. The mirror case is worse: when the flip does land first,
`flip-agreed` then refuses the document as "outside the frontmatter in-scope
set" and it cannot return to `agreed` by tool at all.

**Mitigated, not fixed.** F6 eligibility condition 3 keeps this policy off the
expedited path entirely, so the hazard is not *authorized*. It remains reachable
by any ordinary commit.

**What's needed:** the same diagnostic class as the typo'd-glob item at the top
of this file — compare the matched set against the previous commit's and warn on
a glob that lost all its matches. Both items are one fix.

---

## ~~Settle condition 3's enumerated class before a second document reaches `agreed`~~

**RESOLVED** by `docs/cycles/triage-2026-08-02b-directive.md` (W-1), 2026-08-02,
on Dave's decision at E2. Both open questions are answered in the same
restatement:

- **The borderline trio is in.** `policies/testing-policy.md`,
  `policies/verification-boundary-policy.md`, and `roles/skeptic-risk-agent.md`
  are named in condition 3's list. Each states a hard stop removable inside the
  ten-line ceiling, and a gate over work carries the same
  small-diff-removes-a-gate hazard as a gate over documents.
- **Neither narrowed nor widened — the criterion is primary.** The class is no
  longer "enumerated, not judged." A document stating a gate, a hard stop, or an
  enforcement rule is ineligible whether or not it is named, the list is an
  explicit floor ("at minimum"), and an added fail-safe clause makes an unclear
  case ineligible — mirroring the commit policy's "when in doubt,
  consequential."

The forcing point the entry named is honoured, not bypassed: the settlement
rides the same reviewer-gated cycle that returns
`policies/document-metadata-policy.md` to `agreed`, and no flip has run.

**Original entry, kept for the record:**

**Source:** Package D cycle-7 gate review (B1/B2/N2), 2026-08-02. The expedited
path's condition 3 excludes a named list of documents that state a gate, hard
stop, or enforcement rule. The list is normative, is not derivable by any tool,
and therefore has to be maintained by hand.

**It was incomplete on the day it was written.** Cycle 7 measured five in-scope
documents matching the class, unnamed, each with a gate removable inside the
ten-line ceiling: `operating-model.md` (4 body lines removes both hard gates),
`roles/reviewer-agent.md` (2), `skills/conversation-retro.md` (4),
`boundaries/human-review-boundary.md` (1), `README.md` (2). All five are now
named, along with the release trio the class definition implied.

**Unsettled, and Dave's call:** `policies/testing-policy.md` (the red-gate),
`policies/verification-boundary-policy.md` (boundary-declaration rules), and
`roles/skeptic-risk-agent.md` (a change-flow review step). Each states a gate or
enforcement rule over *work* rather than over documents, which is where the
class definition's edge falls. Also open: whether the class definition should be
narrowed to match the list, or the list widened to match the definition.

**The forcing point, named explicitly so this does not become the `TREE.txt`
mention again:** none of it is reachable until a second document reaches
`agreed`, because until then the expedited path has no addressable document at
all. That day arrives through a reviewer-gated cycle, so the gate is already
attached — **settle this list at that cycle, before the flip.**

---

## ~~Does the Spec Reviewer gate non-spec canonical documents? Two canonical documents disagree~~

**RESOLVED by Dave at the Package D gate, 2026-08-02, in favour of practice:**
the Spec Reviewer hard gate covers **any canonical document**, not `specs/`
only. `skills/spec-review-cycle.md` and the entire review record already said
so; the four contradicting documents were `draft`, and were corrected by plain
commit to match rather than being carried as a standing contradiction. Corrected:
`roles/spec-reviewer-agent.md` (the Activation clause, which was the origin of
the narrow reading), `README.md` principle 9, `operating-model.md` change-flow
step 1, and `boundaries/human-review-boundary.md`. Deliberately not part of
Package D's diff.

The one bounded exception is now named in the role doc: the expedited path
substitutes Dave's read for this gate under five stated conditions.

**Original entry, kept for the record:**

**Source:** Package D cycle-5 gate review (N2), 2026-08-02. Pre-dates F6.
Surfaced because F6 eligibility condition 4 has to rest on the answer.

`roles/spec-reviewer-agent.md` triggers the hard gate on "initial PRD or TRD
authorship" and "any revision to a **spec** document"; `README.md`,
`operating-model.md`, and `boundaries/human-review-boundary.md` all scope the
hard gate to spec documents, in three different formulations.
`skills/spec-review-cycle.md` scopes the cycle to "spec documents (PRD, TRD,
**or any canonical document**)".

**Practice follows the skill, not the role doc.** Every gate review in
`reviews/` is over a non-`specs/` document — four cycles over the metadata
policy, two over Package C, this one — including the four that produced the text
F6 amends. So the class of document that has received every gate review in this
repo's history is the class the role doc says is not gated.

**What's needed:** Dave's call on which reading is canonical, then reconcile the
two documents. F6 does not block on it: condition 4 defers to the gate wherever
it applies rather than defining its reach, and conditions 1–3 bound the override
to a ten-line single-file diff outside this policy either way.

---

## Review artifact schema — third-use feedback from the cycle-5 gate review

**Source:** Package D cycle-5 gate review, schema feedback section, 2026-08-02.
Cycle 2 of Package C asked for a third data point on two specific frictions;
this is it, plus two new ones. Not acted on in Package D — the F3 schema is
Package C's document and F6 does not authorize revising it beyond the
expedited-log carve-out.

1. **A `Severity:` qualifier inside `blocking` — friction confirmed, and it
   scales badly.** Six blocking entries here span two orders of magnitude of
   weight. The header line `Findings: 6 blocking` reads as six equal hard stops.
   The reviewer reports considering demoting two findings purely to keep the
   count honest — the schema shaping the finding. Proposed cheaper fix that
   avoids the "everyone ships past `Severity: low`" failure: let the count read
   `6 blocking (B1–B2 material)`.
2. **Omit-if-none header fields — no friction, but the reasoning is
   asymmetric.** `Not inspected` is required because omitting it is how an
   unbounded claim gets made by accident; `Dave should inspect` carries the same
   risk and is omit-if-none. `Cross-checked` and `Prior cycle` are fine as-is.
3. **New: the schema has no shape for a check that passed.** Dave named the
   compounding check as this review's priority and it passed, with no field for
   that. `observation` was the only bucket and its required `Consequence:` field
   ("what goes wrong, concretely") can never be filled by one — the artifact
   carries `Consequence: None` four times. Without those entries a reader cannot
   distinguish "the check passed" from "the check was never run", which is the
   distinction `Not inspected` exists to protect.
4. **New: the header names one revision where a revision review has two.**
   `Reviewed: <path> @ <sha>` fits a first-cycle review of a draft. Cycles 2+
   review a range; the baseline SHA is what makes the diff reproducible. A
   `Baseline:` field would carry it.

**What worked, recorded because it is load-bearing:** the
`verified by running` / `inferred by reading` split. B2 and B4 exist because the
field pushed the reviewer to execute the sequence instead of reasoning about it,
and both are things a reading-only review would have gotten wrong in the
confident direction.

---

## ~~Remove repo version number from MANIFEST.md~~

**Source:** Document metadata policy session, 2026-07-21.
`policies/document-metadata-policy.md` supersedes the "single version
declared once in `MANIFEST.md`" decision — git SHA is the version.

**RESOLVED** by Package C (F7), 2026-08-01. `MANIFEST.md` dropped its version
declaration in `0230e11`; `README.md`'s echo of it — `Tree version: v0.4 — see
MANIFEST.md for the changelog` — survived that commit and was removed here.

Worth recording why that mattered: the agreed metadata policy's supersession
clause requires that the removal land in the same change package as the
agreement, so that **the repo never holds both conventions as canonical**. From
`0230e11` until Package C, it did — MANIFEST said the SHA was the version while
README said the tree version was "the single source for what's current." Two
review cycles passed over that package without catching it. Found by the
Package C gate review, not by the executor.

---

## Adopt reviews/ directory for review history; migrate root REVIEW-*.md

**Source:** Document metadata policy review session, 2026-07-21. The cycle-1
gate review of `policies/document-metadata-policy.md` is being written to
`reviews/document-metadata-policy-cycle-1.md`, establishing `reviews/` as the
home for review-history artifacts.

**What's needed:** Make `reviews/` the standing convention for review history
and migrate the three existing root-level files (`REVIEW-v0.4.md`,
`REVIEW-NOTES-v0.3.md`, `REVIEW-NOTES-v0.2.md`) into it. Rationale: root is
crowding, and one home for review artifacts keeps them from scattering. Keep
reviewer findings (`reviews/`) distinct from triage decisions (cycle
directives) — the canonical-vs-derived split from
`policies/source-of-truth-policy.md`. Low priority; cheap now, cheaper than
running two conventions indefinitely.

---

## Project context configuration for WNRealtor-CRM (token optimization, workstream 1 of 2)

**Source:** Token optimization session, 2026-07-20. Workstream 2 (methodology
change) shipped as v0.5 (`skills/spec-review-cycle.md`, commit `a3ffe08`).
This item is the remaining workstream.

**What's needed:** Decide the Context panel file list and Instructions text
for the WNRealtor-CRM Claude project. Candidates already proposed:
`roles/spec-reviewer-agent.md`, writer style guide,
`boundaries/mocked-boundaries.md`, `skills/spec-review-cycle.md`. Exclusions
already decided: PRD/TRD (change every cycle),
`context-sets/collab-workflow.md` (artifact-pane default is the wrong mode
for that project's gate-cycle chats). Short behavioral directives (terse
tone, follow spec-review-cycle for gate reviews) go in Instructions, not
Context.

---

## Spec evolution policy — how does the spec stay canonical when reality diverges?

**Source:** Catchable Phase 1, 2026-07-15. The 511 SF Bay stops API returned a
response shape (`Contents.dataObjects.ScheduledStopPoint[]`) that differed from
what the TRD assumed. The bug was fixed in code and captured in a retro, but the
TRD was not updated. This is spec drift.

**The gap:** The operating model states that specs are canonical and that
conflicts are hard stops. But it is silent on what happens when live integration
discoveries, bug fixes, or real-world misalignments invalidate a spec assumption
mid-implementation. There is no policy for:

- When the spec must be updated (before the fix ships? after? never for bugs?)
- Who triggers the update (the agent that found the divergence? DAVE?)
- What constitutes a spec-worthy divergence vs. an implementation detail
- How to keep the spec trustworthy as a regeneration artifact over time

**Why this matters:** If the spec is the leverage point for LLM-driven
regeneration (e.g. rewrites, new platforms), spec drift silently erodes that
leverage. A spec that doesn't reflect reality can't reliably regenerate the
correct implementation.

**What's needed:** A lightweight policy — probably a section in
`context-sets/spec-and-change-discipline.md` — covering:
1. The trigger: what kinds of divergence require a spec update?
2. The timing: before fix, after fix, or at session end?
3. The owner: which role is responsible?
4. The mechanism: in-place edit to PRD/TRD, or a versioned amendment?

**Note:** This is distinct from the retro process open item. Retros capture what
went wrong; this policy governs ongoing spec maintenance as the codebase evolves.

---

## Add retrospective process to the operating model

**Source:** Catchable Phase 1, 2026-07-01. Missing `index.html` + `src/main.tsx`
reached `origin/main` with 225 passing tests. The architect role did not produce
a per-change architecture summary that listed browser entry files as explicit
deliverables.

**What's needed:** A lightweight retro step or trigger in the operating model —
when to run one, what it should capture (what happened, why it wasn't caught,
which role/gate failed, recommended process change), and where the output lives.
Retros are distinct from the skeptic/risk review: they happen after a failure is
discovered, not before release.

**Note:** The architect role instruction for Vite/React projects should be
updated immediately as a direct fix, independent of the broader retro process
definition.

---

## ~~A2 — Consequential-change class: confirm membership is complete~~

**RESOLVED.** The list is exhaustive. Updated
`policies/commit-and-change-control-policy.md` to state this explicitly.
Iterate via normal change process if additions are needed later.

---

## ~~A8 — Define "meaningful change"~~

**RESOLVED.** A meaningful change is any change that warrants a change package
— any change affecting behavior, interfaces, tests, dependencies, boundaries,
or documentation of substance. Trivial changes (typo fixes, comment edits,
purely mechanical formatting) do not require a change package and are not
meaningful in this sense. All affected documents should use this definition.

---

## ~~Reviewer gate vs. advisory~~

**RESOLVED.** The Reviewer Agent is a hard gate. A meaningful change does not
proceed to Skeptic/Risk review or release without Reviewer sign-off. Updated
`roles/reviewer-agent.md` and `policies/agent-review-policy.md`.

---

## ~~Per-file vs. single-file role granularity~~

**RESOLVED.** Roles operate per change unit. The Reviewer Agent reviews the
entire change as a single pass — all files, test plan, diff, and boundary
updates together. If only a subset was reviewed, the reviewer must state what
was and was not inspected. Updated `roles/reviewer-agent.md`.

---

## ~~Error budget exhaustion as a consequential-change trigger~~

**RESOLVED.** Any change to a code path for a Top K user journey whose SLO
error budget is at or below 20% remaining is automatically consequential,
regardless of other characteristics. Updated
`policies/commit-and-change-control-policy.md`.

---

## ~~SRE production readiness checklist~~

**RESOLVED (deferred).** Moved to `BACKLOG-v2.md`. Not blocking current
work. When tackled, likely a new context set or policy doc that extends the
definition of done in `context-sets/spec-and-change-discipline.md`.
