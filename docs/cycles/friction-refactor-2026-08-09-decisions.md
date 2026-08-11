# Decisions taken autonomously — friction refactor, 2026-08-09

Executing `docs/cycles/friction-refactor-2026-08-09-directive.md`. Every call
below is one that would normally have gone to Dave. Each states the question, the
options, what was chosen, and why. Nothing here is agreed; this file is the
review surface for the branch.

Ordered by weight, not by the order taken. **D1–D5 are the ones most worth
Dave's eye** — they are the calls where a different answer would produce a
materially different branch.

---

## D1 — Track survives as the fourth requirement, redefined as the executor's environment

**Question.** D1.3 retires Track B's delivery mechanics. Track was *defined* as a
delivery path ("the two paths a directive takes to become citable"). If delivery
no longer varies, does the Track requirement survive at all?

**Options.**
(a) Drop Track. The four requirements become three: route, model, execution
block.
(b) Keep Track, redefined as the **executor's repository environment**: Track A =
reachable remote, commit and push; Track B = no reachable remote, commit locally,
report the local SHA.
(c) Keep the label but leave it undefined, letting usage settle it.

**Chosen: (b).**

**Why.** Three things point the same way. `DEC-000150` is the most recent agreed
decision on this and says track "is required per directive, because it genuinely
varies" — dropping it silently reverses an agreed decision that this directive did
not name. Dave's own header on this directive states `Track: A (git push
available; no MCP in the loop)`, which is already an executor-environment
statement, not a delivery statement. And the surviving half is real: old Track B
was always *commit-not-push, same-machine only*, and that half is exactly what
still varies once the `~/Downloads` machinery is gone. So (b) is a narrowing to
the part that survived rather than a reuse of a retired label for an unrelated
meaning — but it *is* a redefinition of a term in an agreed lexicon, which is why
it leads this list.

Against (a): it also reaches `bin/cycle-open`'s pending TP-1 spec, which
`DEC-000150` requires to emit Track. Against (c): the lexicon exists to stop
exactly that.

**Consequence recorded.** `LEXICON.md` carries a `Not:` line —
"*Not:* a delivery choice. Every directive is delivered the same way, as a paste
block." — so the old reading cannot be re-derived from the new definition.

---

## D2 — The two-consecutive-failure detector lands in `policies/remote-write-verification-policy.md` as Rule 4

**Question.** D1.3 requires the two-failure contention/degradation detector
(`DEC-000080`'s keep-reason) to survive somewhere sensible. Where?

**Options.**
(a) Keep it in `skills/directive-dispatch.md`, decoupled from the track it used
to open.
(b) `policies/remote-write-verification-policy.md`.
(c) `context-sets/base.md`, beside the evidence vocabulary.
(d) `roles/chief-of-staff.md`, as a state-assessment signal.

**Chosen: (b)** — a new Rule 4, carrying the qualifying/not-qualifying lists and
the counting rules verbatim, plus the keep-reason and its `DEC-000080` citation.

**Why.** The detector's qualifying list is *entirely* transport failures — write
timeouts, unconfirmable-on-read-back writes, 5xx and connection resets. That is
the exact subject matter of the remote-write policy, which already owns "a
response is a claim about a write rather than evidence of one." It also satisfies
D1.2's framing directly: the verification apparatus now "governs only the MCP
writes that remain," and this is a rule about those writes.

Against (a): `skills/directive-dispatch.md` no longer has a mediated transport
anywhere in its path, so the rule would sit in a document whose subject no longer
includes the failures it detects — the drift this repo exists to prevent.
Against (c): `base.md` is always loaded and deliberately short; a
qualifying-failure taxonomy is procedural detail, and there is already an open
item about what belongs in `base.md` from this policy (`OPEN-ITEMS.md`, "Promote
the write-verification principle"), which this would pre-empt without a decision.
Against (d): the detector fires inside whichever session hits the failures; CoS
is not in that loop.

**One thing changed in the move.** The rule was previously framed as *propose
Track B* — a remedy. It is now framed as *stop, say so, establish state* — the
detection, with no remedy attached. The remedy was the track that is gone;
`DEC-000080` says the trigger was kept for what it detects, not for what it
opened, so this is that decision applied rather than extended.

---

## D3 — `bin/dispatch` is retired, not re-specified

**Question.** The deferred `bin/dispatch` would "refuse to emit the dispatch
block until the directive is committed and pushed, and stamp the git-read SHA
into it." Chat no longer commits. Does the tool get a new specification, or does
it die?

**Options.**
(a) Retire it. Drop the section from the skill; record the retirement in
`BACKLOG-v2.md`.
(b) Re-aim it at the executor side: a tool that lands a pasted directive, commits
it, and emits the report line.
(c) Leave the backlog entry alone as out of scope.

**Chosen: (a).**

**Why.** The tool's entire premise was making a chat-side discipline
unskippable — and that discipline no longer exists to skip. (b) would be
inventing a new tool under an old name: landing a directive is `write, git add,
git commit, git rev-parse`, in a session that by definition already has git, and
this directive's own Step 0 ran it without difficulty. Building a tool for it
fails the design test D2.7 names — it spends effort on something that costs the
operator nothing. (c) leaves a backlog entry whose rationale is false, which is
the stale-value defect the directive's item 2 calls out.

**Also removed:** the two build triggers, which were written against the
`~/Downloads` relocate block. Recorded in `BACKLOG-v2.md` under a struck heading
rather than deleted, so the retirement is legible rather than silent.

---

## D4 — Reconciliation is a variant of the existing cycle, not a new skill

**Question.** D2.2 defines reconciliation. Where is it specified — a new
`skills/spec-reconciliation.md`, or inside `skills/spec-review-cycle.md`?

**Options.**
(a) A section in `skills/spec-review-cycle.md`.
(b) A new skill document.
(c) Only in `context-sets/spec-and-change-discipline.md`, with no procedure.

**Chosen: (a)** — a `## Reconciliation` section, with the rules of the delta
itself in `context-sets/spec-and-change-discipline.md` and each consuming document
carrying only its own operative slice.

**Why.** D2.2 says the diff goes through the reviewer gate "**once, as a single
cycle**" — reconciliation *is* the existing cycle, differing only in what is in
scope (a delta's whole diff) and how it arrives (a PR from the spec branch). A
separate skill would duplicate the procedure and then drift from it. (c) leaves
"arriving as a PR" unspecified, and a procedure nobody wrote is a procedure
re-invented per use.

**Placement rule applied throughout Change 2:** the delta's *rules* live in
`context-sets/spec-and-change-discipline.md` (one canonical statement);
`skills/spec-review-cycle.md` carries the cycle mechanics; `roles/chief-of-staff.md`
carries the three consequences that bind that role;
`policies/commit-and-change-control-policy.md` carries the branch-protection
argument; `LEXICON.md` carries definitions only. Each points at the canonical
statement rather than restating it.

---

## D5 — Spec-state terms are added to `LEXICON.md`, against a literal reading of D2.1

**Question.** D2.1 says the spec-branch design needs "no new status value, no
lexicon machinery beyond pointing at git." Does that forbid lexicon entries for
*spec branch*, *open spec delta*, *reconciliation*, and *claimed*?

**Options.**
(a) Add short definitional entries that point at git and at the canonical rules.
(b) Add nothing to `LEXICON.md`; let the terms live only where the rules are.

**Chosen: (a)** — a `## Spec state` section, four entries, each two to five
lines, each pointing outward.

**Why.** Reading D2.1 as forbidding definitions would leave four load-bearing
terms — one of which, *reconciliation*, gates a tranche boundary — defined
nowhere fixed, in a repo whose lexicon exists precisely because `handoff` once
carried six senses. The clause it constrains is "machinery": a status value, a
register, a tracked state. The entries added assert the opposite of machinery —
"the branch existing, with commits on it, is the state" — which is D2.1's own
sentence. If Dave reads this as over-reach, the section deletes cleanly without
touching any rule.

---

## D6 — The sync block survives the transport change

**Question.** The dispatch used to be sync block + citation. With the directive
itself now in the paste, is the sync block still required?

**Chosen.** Yes — a dispatch is two paste blocks, sync then directive.

**Why.** The sync block never existed to fetch the directive; it existed so the
executor works against a current tree, and "a stale clone reporting missing work
is evidence about the clone, not the repo" is unaffected by how the directive
arrived. `DEC-000090` (sync block is Track A only) survives with its *reason*
restated: under the new Track B there is no reachable remote to fetch from, so
the step is a working-tree-current check in the executor's own clone. The
conclusion is unchanged; only the premise moved, which is why the decision is not
being re-opened.

**Added under D2.4:** where a delta is open, the sync block names the spec
branch as its ref.

---

## D7 — An executor that finds the remote unreachable under Track A stops rather than degrading

**Question.** Not specified by the directive. Under the new Track definitions,
what does an executor do when dispatched Track A and the push fails?

**Chosen.** Stop and surface; do not silently commit locally and report as if
Track B had been dispatched.

**Why.** Track B remains operator-invoked and never inferred — that rule is
carried over intact. Without this clause the redefinition creates a hole the old
definition did not have: an executor could satisfy "Track B" by discovering it
mid-run, and the report's standard would change without anyone deciding it. This
is an invented guard, flagged as such.

---

## D8 — Revision notes are updated only where that convention already exists

**Question.** Work item 5 says update each document's status-of-this-draft notes
"per its own convention." `skills/directive-dispatch.md` and
`policies/remote-write-verification-policy.md` have such a section. `LEXICON.md`,
`skills/command-blocks.md`, `skills/spec-review-cycle.md`,
`roles/chief-of-staff.md`, and the context sets do not. Do they get one?

**Options.**
(a) Update where the convention exists; add nothing where it does not.
(b) Add a revision note to every document touched.

**Chosen: (a).** A note was drafted for `skills/command-blocks.md` and then
removed.

**Why.** `policies/document-metadata-policy.md` is explicit that "anything git
history already knows — when a doc changed, who changed it, what changed — is
excluded from metadata, because a duplicate record will drift from git and lie."
Introducing the convention to five more documents propagates exactly that. The
directive's phrase is "per its own convention," and a document with no such
section has the convention of not having one. Every edit is legible from
`git log`, this file, and the review artifacts.

---

## D9 — Status flips were made by hand, not left to the hook

**Question.** The pre-commit hook flips `agreed` → `in-review` on content edits.
Rely on it, or set the frontmatter explicitly?

**Chosen.** Set explicitly: `status: in-review`, `last-reviewed: null`, on all
six previously-`agreed` documents revised — `skills/directive-dispatch.md`,
`skills/command-blocks.md`, `skills/spec-review-cycle.md`,
`roles/chief-of-staff.md`, `LEXICON.md`, and
`policies/remote-write-verification-policy.md`. The other six documents changed
were already `draft`, and trackers carry no frontmatter.

**Why.** The result is identical and the intent is explicit in the diff rather
than applied to it. `bin/check-frontmatter --all` exits 0 on the result. Note
that this discards the `last-reviewed` pointers to cycle-3 / cycle-4 / expedited
artifacts, which is what `policies/document-metadata-policy.md` requires — the
history is not lost, it is in `reviews/` and git.

---

## D10 — Decomposition always pins default-branch SHAs

**Question.** D2.3 prohibits decomposing from unreviewed spec. `roles/chief-of-staff.md`
requires the decomposition doc to pin the spec SHAs it derived from. Which SHAs,
when a delta may be open?

**Chosen.** Stated explicitly: because decomposition requires a closed delta,
those SHAs are always default-branch SHAs.

**Why.** This is D2.3 followed through rather than a new rule, but it was not
stated anywhere and a reader could reasonably have concluded a decomp may pin a
spec-branch SHA. Making it explicit closes the gap between "reconciliation blocks
decomposition" and the pinning rule that `DEC-000070` settled.

---

## D11 — Blast radius extended beyond the directive's known-affected list

**Question.** Item 2 says not to trust the given list. Which documents outside it
were changed?

**Chosen additions**, each with the conflict that forced it:

- `README.md` — principle 9 read "agreed by Dave **before work begins**", which
  D2.6 directly contradicts.
- `roles/spec-reviewer-agent.md` — the gate fired on "any revision … before Dave
  agrees the revision"; under D2.2 a delta's revisions gate together. A gate
  document contradicting the new rule is the serious direction.
- `context-sets/ai-native-engineering.md` — carries the second definition of
  *tranche*; now names the delta it bounds.
- `BACKLOG-v2.md` — the `bin/dispatch` entry (D3).
- `OPEN-ITEMS.md` — three new entries (D12).

**Not changed, deliberately:** `CLAUDE.md` and `AGENTS.md` (adapters; their
spec-first lines say "specs and ACs before tests", which remains true and does not
conflict); `MANIFEST.md`, `docs/global-retro-inbox.md`, `retros/`,
`docs/session-2026-08-05-state.md`, `docs/research/` (records of what happened —
the same reason `reviews/` is not retrofitted); `decisions/log.md` (forbidden;
see D13).

---

## D12 — Three open items opened rather than left implicit

**Question.** The two changes create gaps nothing currently covers. Is opening
`OPEN-ITEMS.md` entries in scope for a directive that says "this is not a general
cleanup pass"?

**Chosen.** Yes, three entries: the open spec delta has never been run; the
disjoint-territory claim rule is unenforced; `bin/cycle-open` / TP-1 against the
changed meaning of Track.

**Why.** These are consequences of tonight's changes, not pre-existing debt —
which is the line the "no general cleanup" constraint draws. The repo's own
operating habit requires proactive loose-end tracking rather than relying on Dave
to remember, and the claim rule in particular is a stated rule with no enforcement
and a silent, expensive failure mode.

---

## D13 — Decision-log entries are proposed, not written

Per the hard constraint, `decisions/log.md` is untouched. Two entries are drafted
below for Dave to promote after the morning review. IDs follow `DEC-000150`.

**Amended 2026-08-10** by the corrections run, self-review cycle 2. Neither
entry had been promoted, so both drafts were corrected in place rather than
superseded — a draft is not yet a decision, and shipping a known-wrong entry into
an append-only log to fix it one line later is the failure the log's
whole-entry-supersession rule makes expensive. Two corrections: `DEC-000160`'s
track clause is removed, leaving the entry silent on track so that promoting it
does not install a decision the proposed `DEC-000180` would immediately have to
reverse; and `DEC-000170`'s "at most two **tracks** run concurrently" is
corrected to "tranches", the word
`context-sets/spec-and-change-discipline.md` fixes for a concurrent workstream
and the one this branch's own concurrency parenthetical exists to enforce. The
2026-08-09 text is recoverable from git; see `d02c98c`.

### Proposed — DEC-000160 — Directives travel as paste blocks; the executor lands them and reports the SHA post-hoc

```
## DEC-000160 — Directives travel as paste blocks; the executor lands them and reports the SHA post-hoc
Date: 2026-08-09
Decision: A directive is dispatched as a paste block. The executor's first act is
to write it to `docs/cycles/`, commit it, read the SHA back from git, and report
"executed <path>, landed as <sha>". The SHA is established post-hoc and is
sufficient for the decision record. This applies to every directive class,
reviewer-gated cycle directives included. Chat-side tool-mediated writes leave the
dispatch path entirely; `policies/remote-write-verification-policy.md` accordingly
governs the mediated writes that remain rather than a dispatch step. The
`~/Downloads` delivery path — pre-flight glob, relocate/commit/echo blocks,
artifact-and-blocks-in-one-turn — is retired, and with it the deferred
`bin/dispatch`, whose premise was a chat-side commit to gate. This entry is
silent on **track**, which the 2026-08-10 corrections retire outright; the
proposed `DEC-000180` carries that, and supersedes `DEC-000150`.
The two-consecutive-failure trigger is retained as a pure detector and relocated
to `policies/remote-write-verification-policy.md` Rule 4, preserving DEC-000080's
keep-reason without the delivery path it used to open.
Context: a directive does two jobs — transport, whose value expires at execution,
and record, whose value accrues later. Only the record needs git, and the executor
is the party for whom git is cheap. The integrity question shifts from provenance
to paste-arrival-intactness, already governed by the parse-atomic paste rules. Dave
confirmed post-hoc SHAs are sufficient for the decision record. Executed as
`docs/cycles/friction-refactor-2026-08-09-directive.md` (D1.1–D1.4).
Supersedes: —
```

### Proposed — DEC-000170 — Open spec delta: spec branches are ungated; agreement attaches at reconciliation

```
## DEC-000170 — Open spec delta: spec branches are ungated; agreement attaches at reconciliation
Date: 2026-08-09
Decision: During a tranche's execution, spec documents may be edited freely on
`spec/<tranche-slug>` with no reviewer gate and no per-edit ceremony — an **open
spec delta**; the branch is the state, with no new status value and no register.
**Reconciliation** closes it: the spec is brought to full agreement with what was
built, and the whole accumulated diff goes through the reviewer gate once, as a
single cycle, arriving on the default branch as a pull request. A delta is bounded
by its tranche and never spans two; reconciliation blocks the next tranche's
decomposition, and decomposing from unreviewed spec is prohibited. Reconciliation
may be invoked early at will, and frequent small reconciliations are the norm.
Mid-delta dispatches derive from the spec branch and pin its SHA. At most two
tranches execute concurrently, over disjoint spec territory; a
document is claimed by appearing in an open delta's diff and may not be claimed by
a second, and the convergent-edit case is refused rather than tooled.
Context: agreement attaches to the version of record at reconciliation, not to a
version pre-approved before building. The amnesiac-executor constraint requires
truth-at-handoff, not agreement-in-advance, and the recreate-from-spec goal needs
the spec true at rest between deltas rather than at every instant during one. The
design test applied: operator attention is the system's scarcest,
non-parallelizable resource, and evidence integrity may not be purchased by
spending it as if it were free. Executed as
`docs/cycles/friction-refactor-2026-08-09-directive.md` (D2.1–D2.7).
Supersedes: —
```

---

## D14 — Nothing was flipped to `agreed`, and nothing merged

Stated for completeness, not because it was a judgment call. All work is on
`methodology/friction-2026-08-09`. No `agreed` status was set. `decisions/log.md`
is unmodified. `gh` was not invoked. No force-push.

---

## D16 — Trackers get no review artifact

**Question.** The directive says one review artifact per document over the full
changed set. `BACKLOG-v2.md` and `OPEN-ITEMS.md` were changed. Do they get
`reviews/BACKLOG-v2-cycle-1.md` and the like?

**Chosen.** No. Twelve artifacts were written, covering the twelve canonical
documents changed; the two trackers were reviewed as cross-checks within them.

**Why.** `policies/document-metadata-policy.md` puts trackers out of the
frontmatter scope on the grounds that "their status is their content", and
`skills/spec-review-cycle.md` says review artifacts are what `last-reviewed:`
points at. A tracker has no `last-reviewed:` to point, so the artifact would be a
document nothing references, in a directory whose entire purpose is to be
referenced. The changes themselves are small and mechanical — one struck backlog
entry, three new open items.

---

## D17 — Self-review found six blocking findings; all were fixed in cycle 2

Recorded because the directive asks for the judgment calls, and "what did the
self-review actually catch" is the question that decides whether the exercise
was real. Cycle 1 verdicts and the fixes are in `reviews/`; the substantive
catches were:

- **The word `track` collided with itself.** D2.5's phrase "at most two tracks"
  reused a term `LEXICON.md` had just been made to fix. Resolved by not using
  Dave's word: "at most two tranches executing concurrently."
- **The delta's editing licence named nobody.** D2.1 says *Dave* may edit spec
  documents freely; the transcription dropped the subject, which in a context set
  loaded into every implementation chat reads as licensing any agent to edit spec
  ungated. That was the worst defect found and it was introduced by this
  execution, not by the directive.
- **"Once, as a single cycle" forbade its own re-gate.** Fixed by stating what
  "once" quantifies.
- **The agreement flip had no stated position relative to the merge**, while
  `policies/commit-and-change-control-policy.md` asserted a structural guarantee
  that depends on it. Fixed by stating post-merge, on the default branch, with
  the reason.

---

## D19 — Cycle 3 was scoped to the documents cycle 2 changed

**Question.** The directive says one review artifact per document, per cycle.
Cycle 3 is a confirmation pass. Do the nine documents that reached verdict `ready`
at cycle 2 and were not edited since get a cycle-3 artifact each?

**Chosen.** No. Cycle 3 covers the three documents the cycle-2 fixes touched —
`context-sets/spec-and-change-discipline.md`, `skills/spec-review-cycle.md`,
`LEXICON.md`. The other nine stand at their cycle-2 verdict.

**Why.** A confirmation artifact over an unedited document that already passed
records nothing and points `last-reviewed` at a review that inspected no change.
`skills/spec-review-cycle.md` is explicit that a review format expensive to write
is a review that gets skipped, and that the clean case is kept cheap on purpose.
The regression risk the extra pass would cover was already covered: every cycle-2
artifact for those nine states in its Scope what it cross-checked against the
cycle-1 fixes.

**Where this could be wrong.** If Dave wants a per-document artifact at the final
cycle regardless, the nine are unedited since `7d4d03a` and the pass is cheap to
run.

**Cycle count:** three cycles run, of the five permitted. Cycle 3 closed with no
blocking findings outstanding.

---

## D20 — Two undocumented red tests were reported, not recorded

**Question.** `bin/tests/run` finishes 347/350. One failure,
`test_bn10_bundle_base_yields_exactly_itself`, is already tracked in
`OPEN-ITEMS.md`. The other two —
`test_sc1_extracts_the_in_scope_list_in_document_order` and
`test_sc1_load_globs_reads_the_policy_from_the_methodology_home` — are tracked
nowhere. Do they get an open item?

**Chosen.** No. Reported in the final report instead.

**Why.** Both are pre-existing and unrelated: `policies/document-metadata-policy.md`
is byte-identical to `origin/main` on this branch (`git diff origin/main --` is
empty), and the tests assert a hardcoded in-scope list that omits `LEXICON.md`,
which entered the policy at `1f5b715` — a stale assertion from that change, not
from this one. Recording it would be the general cleanup pass the directive
excludes; leaving it silent would be worse, so it goes in the report where Dave
triages it.

**Diagnosis, for whoever picks it up:** the fix is to the test, not the policy —
the policy is `agreed` and correct, and the expected list in
`bin/tests/test_scope.py` was not updated when `LEXICON.md` was added to it.

---

## D18 — What was *not* done, and why

- **`policies/verification-boundary-policy.md`** — `OPEN-ITEMS.md` proposes
  folding the content-check rule there. Untouched: that is a pre-existing open
  item, not a consequence of these changes, and acting on it would be the general
  cleanup pass the directive excludes.
- **`context-sets/base.md`** — likewise untouched, for the same reason (D2's
  rejection of option (c)).
- **No worked example of a reconciliation cycle** was written. The design has
  zero executions behind it; a fabricated example would read as evidence.
  Tracked in `OPEN-ITEMS.md` instead.

---

# Corrections run — 2026-08-10 directive

Executing `docs/cycles/friction-refactor-corrections-2026-08-10-directive.md`.
Same model as above: every call below is one that would normally have gone to
Dave. Numbering continues from D20. **D21 and D22 are the ones most worth Dave's
eye** — D21 is a reversal of an agreed decision, and D22 is the one place the
directive's own instruction had to be read against itself.

---

## D21 — DEC-000150's track requirement is reversed; the entry is drafted, not written

**Question.** C1 removes `track` from the methodology. `DEC-000150` is agreed and
states "**track is required per directive**, because it genuinely varies", and
carries a tooling consequence for `bin/cycle-open`. The hard constraints forbid
touching `decisions/log.md`. How is the reversal recorded?

**Chosen.** Drafted below as a proposed `DEC-000180`, for Dave to promote.
`decisions/log.md` is untouched.

**Why.** `policies/decision-log-policy.md` supersedes **whole entries**, not
halves — the precedent it names is `DEC-000030`'s carve-out going dead under
`DEC-000040`, and `DEC-000150` itself restates `DEC-000110`'s track half inline
for exactly this reason. So the proposed entry restates the route/model half it
means to keep rather than pointing at a superseded entry for it.

**The ID is provisional.** `DEC-000150` is the last entry actually in the log.
The overnight run drafted `DEC-000160` and `DEC-000170` (D13), also unpromoted.
`DEC-000180` assumes those two land first, in that order. If Dave promotes this
one alone, it is `DEC-000160`; if he promotes some other subset, the ID moves
with it. Last-plus-ten is computed against the log, not against a queue of
drafts, so this is the one field of the entry that cannot be settled here.

### Proposed — DEC-000180 — Track is retired; the dispatch requirements are three, not four

```
## DEC-000180 — Track is retired; the dispatch requirements are three, not four
Date: 2026-08-10
Decision: `track` is removed from the methodology entirely. A dispatch states
**three** requirements, all three every time: route, model, and the execution
block. `DEC-000150`'s route/model half is carried forward unchanged and restated
here so it stays live under whole-entry supersession: a reviewer-gated cycle
directive states every requirement like any other dispatch, with route *fresh*
and model *Opus 5* as class defaults — stated per directive and overridable, not
fixed by class. What is reversed is `DEC-000150`'s other half, "track is required
per directive, because it genuinely varies": it does not vary in any way a
directive can usefully state. The one condition the term still covered after
`DEC-000160` retired its delivery sense — the executor's remote is unreachable —
is not a property of the work being dispatched and is not knowable by the party
writing the directive. It is an executor obligation instead: an executor that
cannot push stops and surfaces it, and never commits locally and reports a
same-machine SHA as if it were pushed (`skills/directive-dispatch.md`, Executor
obligations). `LEXICON.md` carries a tombstone rather than a definition. The
sync block precedes every execution block with no exception. Consequence for
tooling: `bin/cycle-open` (TP-1, shelved) emits Route and Model and no Track;
`DEC-000150`'s "must emit Route, Model, and Track" is superseded, and
`OPEN-ITEMS.md` carries the guard against resurrecting the field on unshelving.
Context: owner override (Dave), per
`docs/cycles/friction-refactor-corrections-2026-08-10-directive.md` (C1), after
reviewing the overnight run that had kept track and redefined it
(`docs/cycles/friction-refactor-2026-08-09-decisions.md` D1). The reason the
redefinition failed: forge downtime is a transient property of the executor's
machine, and a standing instruction line stating it is a line that is wrong
whenever it matters. A field nobody can fill correctly in advance is worse than
no field, because a stated value is what a report gets measured against.
Supersedes: DEC-000150
```

---

## D22 — The Track tombstone stays under Dispatch; a `Retired terms` section holds Prompt

**Question.** C1 asks for a Track tombstone "in the retired-terms style of the
Prompt entry (C4)". C4 turns the `## Prompt` section into a tombstone. Does the
lexicon grow a retired-terms section holding both, or do the tombstones stay
where their terms were?

**Chosen.** Both. The Track tombstone stays in place under `## Dispatch`, where
`Track A / Track B` was; `## Prompt` is renamed `## Retired terms`, holds the
Prompt tombstone in full, and cross-references Track.

**Why.** "Retired-terms style" reads as a style instruction, not a placement
one — the load-bearing property of a tombstone is that it sits where a reader
looks the term up. Someone reading an August directive that says `Track: A` opens
the lexicon at Dispatch. Moving the entry to a section at the end of the file
would make the deflection depend on the reader already knowing the term is
retired, which is the one thing they do not know. `## Retired terms` is the
Prompt entry's existing home renamed, so nothing moved for it either.

---

## D23 — The Prompt tombstone routes by class, and exempts the approval-prompt sense

**Question.** C4 says "do not trust the term list above" and requires the
tombstone's routing be exhaustive over "typed-at-or-consumed-by-a-session
artifacts". A flat list of every such artifact runs to fifteen-plus items and
reads as a catalogue rather than a deflection.

**Chosen.** Route by class, naming instances under each: what a decision session
hands an execution session; what it hands its successor decision session; what a
directive points at; what runs in a shell; what a session loads as standing
context; what it derives work from; inbound material it acts on. The sweep found,
beyond the directive's six: *companion document*, *sync block*, *paste block*,
*context set*, *role document*, *skill document*, *policy*, *boundary document*,
*decomposition doc*, *change package*, *acceptance criteria*, *spec*, *review
artifact*, *upload*, *retro*.

**Also chosen: a stated exemption.** The tombstone ends with a *Not covered*
clause for the **approval prompt** — a tool interrupting to ask a human to
authorise a step (`vendors/claude-code/environment-config.md` uses it seven
times, `policies/commit-and-change-control-policy.md` once). That is a different
word in a different domain, and without the clause the next sweeper conforms
those eight hits and makes the documents worse. The exemption is what stopped
this run from doing so.

---

## D24 — Which "prompt" and "track" hits were conformed, and which were left

**Question.** C1 and C4 both exempt historical records and both require judging
every hit. Where is the line?

**Chosen.** Conformed: living canonical text that *asserts* something in the
present tense. Left: anything whose truth is indexed to when it was written —
`reviews/`, `docs/cycles/`, `retros/`, `docs/research/`,
`docs/global-retro-inbox.md`, `decisions/log.md`, `MERGE-NOTES-*`,
`REVIEW-NOTES-*`, `REVIEW-v0.4.md`, and the `## Status of this draft` revision
notes inside otherwise-conformed documents.

**The revision-note case is the one worth stating.** `skills/directive-dispatch.md`
and `policies/remote-write-verification-policy.md` both carry revision notes that
say "Track B mechanics rewritten 2026-08-07" and the like. Those sentences are
true — they describe an edit that happened — and rewriting them would make the
document lie about its own history. Each gets a new dated clause recording this
retirement instead, which is the convention D8 established.

**`roles/orchestrator-agent.md` is exempt on a different ground.** It is
`status: superseded` and frozen (`roles/chief-of-staff.md` says so), and it
carries four "prompt" hits. A frozen document is not living canonical text.

---

## D25 — Three open items were struck or annotated, not left to rot

**Question.** C3 retires `.prompts/`. Three `OPEN-ITEMS.md` entries and one
backlog-shaped entry depend on machinery this run removed. Trackers are not
mentioned in the blast radius.

**Chosen.** All four touched, as required consistency edits.

- **"Chat-originated package prompts have no compliant write path"** — struck.
  The rule it called unsatisfiable no longer exists, and the recommendation it
  reached (the executor commits the record of what it ran) is what the paste
  transport already does.
- **"A handoff into another decision session has no name"** — struck, per C2.
- **"Directive-execution mechanics are oral tradition"** — marked **superseded in
  part**, not struck. Its "the rule, effective now: a kickoff is one line"
  paragraph is dead, but the gap it names is not: branch naming, the
  tests-and-`check-frontmatter`-before-PR gate, and STOP semantics still have no
  canonical home. Striking it whole would have lost a live gap; leaving it whole
  would have left a dead rule reading as current.
- **"`bin/cycle-open` and the changed meaning of Track"** — retitled and headed
  with the do-not-resurrect annotation C1 asked for. The shelved spec is not
  rewritten.

---

## D26 — `test_sc1` derives its expectation, and gains a guard test

**Question.** C5 prefers deriving the in-scope set over listing it. Deriving it
with `scope.parse_in_scope_globs` — the function under test — would make AC-SC-1
assert nothing at all.

**Chosen.** Derive it in the test module by an **independent, stricter** read of
the same policy text: a whole-line bullet whose entire content is one backticked
entry. `aimeta/scope.py` collects every backticked span on any line starting with
`-`, so the two agree only while the policy states one glob per bullet with no
backticked prose between the markers. That is a real differential check, not a
tautology.

**And a guard.** Both sides of AC-SC-1 now read the same file, so a derivation
that silently returned `[]` would make every assertion pass vacuously.
`test_sc1_the_derived_expectation_is_not_vacuous` asserts a floor of four entries
and four anchors, including `LEXICON.md` — the entry whose absence caused this
failure in the first place.

**Consequence for the count.** The suite is 351 tests, not 350. The directive's
bar was "≥ 349/350"; the equivalent is 350/351, which is what it runs, with
`test_bn10` the single known failure and untouched.

---

## D27 — Dates cite the directive, not the day the work ran

**Question.** The directive is dated 2026-08-10 and names Dave's triage that day.
The execution ran 2026-08-11 (`git log`). Which date goes in revision notes?

**Chosen.** 2026-08-10, the directive's date, everywhere a revision note or a
resolution cites this work — matching the existing convention, which
`reviews/directive-dispatch-cycle-3.md` records explicitly ("its date is the
directive's date rather than the landing date"). `OPEN-ITEMS.md`'s `Last updated:`
field is the exception and reads 2026-08-11, because that field is a fact about
the file rather than a citation of a decision.

**Flagged for Dave** only because the two dates differ visibly in the same
commit, which no prior run had.

---

## D29 — Two unpromoted decision drafts were corrected in place, not superseded

**Question.** Self-review cycle 2 found that the overnight run's proposed
`DEC-000160` asserts "**Track** is retained as the fourth requirement and
redefined as the executor's repository environment", and that its proposed
`DEC-000170` says "at most two **tracks** run concurrently". If Dave promotes
them as drafted, the log acquires a track decision the same morning's `DEC-000180`
reverses, and a second entry using a word the branch retires.

**Options.**
(a) Leave both drafts alone; have `DEC-000180` supersede `DEC-000160` as well.
(b) Correct both drafts in place and record the amendment.
(c) Leave them and flag it in the report for Dave to fix by hand.

**Chosen: (b).**

**Why.** (a) is the trap `policies/decision-log-policy.md` names explicitly:
supersession is whole-entry, so superseding `DEC-000160` to kill one clause would
also kill the paste-transport decision that is the entire point of this branch —
which is how `DEC-000030`'s carve-out went dead under `DEC-000040`. (c) spends
Dave's attention on a mechanical correction, which the operating model treats as
the scarce resource. A draft is not yet a decision: nothing cites these entries,
`decisions/log.md` is untouched, and the 2026-08-09 text is in git at `d02c98c`.
Correcting a draft costs nothing; promoting a known-wrong entry into an
append-only log costs a supersession cycle.

**`DEC-000160` is left silent on track** rather than restating the retirement,
so that the two entries do not both legislate it. `DEC-000180` carries it and
supersedes `DEC-000150`, which is where the requirement it reverses actually
lives.

**Flagged for Dave.** This is an edit to the overnight run's decision record,
made by the run reviewing it.

---

## D28 — What was *not* done, and why

- **`decisions/log.md`** — untouched, per the hard constraint. Three entries now
  await promotion: `DEC-000160`, `DEC-000170` (overnight run), `DEC-000180`
  (this one), in that order.
- **`roles/orchestrator-agent.md`** — untouched. Superseded and frozen; see D24.
- **`vendors/claude-code/environment-config.md`** — untouched. Its seven
  "prompt" uses are all the approval-prompt sense; see D23.
- **The shelved TP-1 spec** — not rewritten, per C1's explicit instruction. Only
  the tracker entry guarding it was annotated.
- **`test_bn10`** — untouched, per C5. Still red, still tracked in
  `OPEN-ITEMS.md`.
- **Nothing flipped to `agreed`; nothing merged; no force-push; no `gh`.**
