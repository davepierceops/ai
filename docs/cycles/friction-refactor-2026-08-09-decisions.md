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
`bin/dispatch`, whose premise was a chat-side commit to gate. **Track** is
retained as the fourth requirement and redefined as the executor's repository
environment: Track A has a reachable remote and pushes; Track B has none and
commits locally, where a SHA exists at commit and resolves in that clone alone.
The two-consecutive-failure trigger is retained as a pure detector and relocated
to `policies/remote-write-verification-policy.md` Rule 4, preserving DEC-000080's
keep-reason without the track it used to open.
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
tracks run concurrently, on different tranches over disjoint spec territory; a
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
