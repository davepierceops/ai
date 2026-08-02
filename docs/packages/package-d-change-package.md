# Change Package — Package D: Expedited Review Path (F6)

Directive: `docs/cycles/streamlining-directive.md` — F6, the routing change,
sequenced last and deliberately alone (Execution sequence item 4). Cycle
directive: `docs/cycles/cycle-5-directive.md`. Review artifact:
`reviews/document-metadata-policy-cycle-5.md`.

**Tier: consequential.** It changes how a document reaches `agreed` — this
repo's own review routing — so it requires Dave's explicit go/no-go at the
release decision rather than flowing on evidence.

**The constraint that shaped the package:** the expedited path may not be used
to introduce itself. Package D ran the full mechanics — `cycle-open` with SHAs
read from git, an independent Spec Reviewer gate, a triage directive, a review
artifact, this change package, and a human gate — for a change whose entire
purpose is to make some future changes cheaper than exactly that.

---

## 1. Intent

`policies/document-metadata-policy.md` said: *"No exceptions for trivial edits.
Enforcement cannot judge meaningfulness, and an escape hatch invites misuse. A
typo-fix review cycle is cheap; a document falsely claiming review currency is
not."*

The first sentence conflates two different things, and the cost showed up
before F6 was drafted. Package C found an inert `TREE.txt` mention in that
policy's out-of-scope list — a reference to a file it had just deleted — and
**left it there on purpose**, because correcting it would have cost a full
reviewer-gated cycle. That deferral is itself the argument: the repo chose to
carry a known-wrong line rather than pay the ceremony to fix it.

F6 separates the two halves. The flip **out** of `agreed` stays unconditional —
enforcement genuinely cannot judge meaningfulness, so every content edit flips
the document to `in-review` whatever its size. What gets shortened is the way
**back**: a bounded path where Dave's own read of the diff substitutes for the
reviewer-gated cycle, and the agreement leaves a one-line record.

The rider rode the same cycle by design: since Package D opens that document
anyway, the `TREE.txt` cleanup lands in the same diff the reviewer read, rather
than sitting in `OPEN-ITEMS.md` waiting for a cycle of its own.

## 2. What changed

| File | Change |
| --- | --- |
| `policies/document-metadata-policy.md` | **F6.** The "No exceptions for trivial edits" clause is scoped to the outbound flip; a new `## Expedited return to agreed` section carries five eligibility conditions, the record format, and the four-step sequence. **Rider:** `TREE.txt` removed from the out-of-scope list. |
| `reviews/expedited-log.md` | New. Empty append-only log; one line per expedited agreement, the target of `last-reviewed` on documents agreed that way. |
| `skills/spec-review-cycle.md` | **B3.** The F3 artifact schema governs per-cycle artifacts; a per-entry log is carved out explicitly. Required — see §4. |
| `skills/conversation-retro.md` | **B5.** "There is no second door into `agreed` documents" was made false by this change. Scoped to retros, where it remains true. Required — see §4. |
| `OPEN-ITEMS.md` | Closes the `TREE.txt` item; discharges the Package C §9 handoff; opens four items from the gate's deferred set. |
| `docs/cycles/cycle-5-directive.md` | The triage record — one entry per finding, including the rejection. |

## 3. Review

One gate review by an independent Spec Reviewer agent, not the drafting
instance. **Verdict: `changes-required` — 6 blocking, 8 non-blocking, 4
observations.** Every blocking finding is fixed; seven of eight non-blocking
accepted or modified, one rejected with reasoning recorded.

Two of the six blocking findings exist because the reviewer **ran the sequence
in a scratch clone instead of reading it**, and both would have shipped
otherwise:

- **B2 — the expedited path could have disabled enforcement.** As first
  drafted, condition 3 protected only the expedited section, so the Scope globs
  a few paragraphs above were themselves expeditable. Demonstrated: one
  single-file commit deleting the `policies/**` line dropped enforcement from
  38 files / 8 globs to 31 / 7, and the committed file still read
  `status: agreed` with its prior `last-reviewed` intact — because
  `bin/aimeta/scope.py` reads the globs from the policy on disk, so by the time
  the hook evaluated the commit the file had already removed itself from scope
  and the flip never fired. The mirror case is worse: when the flip does land
  first, `flip-agreed` refuses the document as outside the in-scope set and it
  cannot return to `agreed` by tool at all. The condition now excludes the whole
  policy.

- **B4 — the "an artifact that exists" guarantee is now vacuous.** With step 3
  of the sequence skipped entirely, `flip-agreed --review 'reviews/expedited-log.md
  @ <sha>'` exited 0 against a log holding no entries, and
  `check-frontmatter --all` then reported the repo clean. The check was
  substantive when each cycle had to *create* an artifact to satisfy it; the log
  exists permanently, so it is satisfied vacuously and forever, for every
  document in the repo. See §6 — this is the one open risk at the gate.

The other four:

- **B1 — the section contradicted its own opening sentence.** It asserted every
  eligibility condition was a fact about the change, then made the load-bearing
  one Dave's reaction to it, and bounded diff size nowhere. On the text as
  drafted, a complete rewrite of `roles/spec-reviewer-agent.md` in one file that
  Dave found persuasive on first read was eligible.
- **B3 — a canonical-vs-canonical contradiction.** The F3 schema that landed one
  commit earlier defines its governed set as exactly what `last-reviewed:`
  points at, and explicitly does not grandfather artifacts written after it. The
  log is written after it and carries none of the seven required header fields.
  Silence is the one option `policies/source-of-truth-policy.md` forecloses.
- **B5 — `skills/conversation-retro.md` says there is no second door.** F6
  builds one. The sentence's first clause is scoped to retros; the second was
  stated as a general property of the repo and became false.
- **B6 — no change package existed.** This document. It was sequenced after
  triage, but the finding is right that its absence left the review artifact as
  the sole account of a change it is supposed to be independent of.

## 4. Three documents outside the edit target, and why that is not scope creep

`skills/spec-review-cycle.md` (B3) and `skills/conversation-retro.md` (B5) were
each edited by one clause. Both are reconciliations the gate required, not
additions: under `policies/source-of-truth-policy.md` a canonical document
contradicting another is a **hard stop**, and leaving either alone would have
shipped one.

This is the defect class Package C caught one file over — `AGENTS.md`
contradicting the revised F5 policy — and recorded as its lesson. It recurred
here in the same shape and was caught the same way, by the gate rather than by
the executor, twice in two packages. Worth stating plainly rather than filing
as a coincidence: **the drafter has now missed the downstream-contradiction
check in two consecutive packages.** The control that caught it both times is an
independent reviewer instructed to cross-check, which is the control the
operating model says is doing the work.

`OPEN-ITEMS.md` is a tracker, out of frontmatter scope, and Package C §9
explicitly assigned its stale entries to "whoever next opens `OPEN-ITEMS.md` for
a substantive reason." Package D is that opener, so the two entries still
claiming "Blocked on the policy reaching `agreed`" are struck — the policy is
agreed, the hook is live, and the migration shipped in Package B.

## 5. Decisions the gate forced, and one it did not settle

**The ten-line ceiling (B1) is a bright line, and arbitrary on purpose.** The
reviewer offered an either/or: add a structural size bound, *or* drop the "every
condition is a fact about the change" framing — but not both. Package D does
both, because the "not both" guarded against keeping a false framing alongside a
bound, and the framing is not being kept: conditions 1–4 are now named as facts,
condition 5 as the one human judgment, and the section says so in the sentence
that used to claim otherwise.

**The count excludes the hook's own frontmatter flip.** Found by the executor
after triage, measuring the rider against the new rule: the flip is four changed
lines on every revision, so charging them to the author would have silently
reduced a ten-line allowance to six. The rider itself is two body lines; a real
cosmetic fix has room.

**The motivating example would not qualify under the rule it motivated.** B2's
fix excludes `policies/document-metadata-policy.md` from the expedited path
entirely, and the `TREE.txt` mention lived in that policy. So F6's own worked
example — the thing Package C pointed at when it said "this is the cost F6
exists to reduce" — still requires a full cycle. This is stated rather than
glossed: the path covers every other in-scope document, and excluding the one
document whose Scope section defines what enforcement checks is the right trade,
but the headline example is not among the changes it makes cheaper.

**The `specs/` exclusion is kept and is not fully settled (N1/N2).** Condition 4
defers to the Spec Reviewer hard gate rather than defining its reach. The
reviewer showed that reach is genuinely unsettled: `roles/spec-reviewer-agent.md`,
`README.md`, `operating-model.md`, and `boundaries/human-review-boundary.md` all
scope the hard gate to **spec** documents, while `skills/spec-review-cycle.md`
scopes the cycle to "any canonical document" — and **practice follows the
skill**: every gate review in `reviews/` is over a non-`specs/` document,
including the four cycles that produced the text F6 amends. Re-pointing
condition 4 at "documents the Spec Reviewer hard-gates" would rest it on that
unsettled definition, which is worse than resting it on a path. Kept as-is,
tracked in `OPEN-ITEMS.md` as a decision for Dave, and **surfaced at the gate**
per `policies/source-of-truth-policy.md` rather than reconciled by the executor.

**N6 rejected.** Cycle 4 of this document removed cross-repo references for
portability, and the new text adds three repo-relative pointers. But cycle 4
removed pointers into *this repo's cycle history*, which is genuinely absent
from an adopting repo; `roles/` and `skills/` citations resolve through an
adopting project's `/ai` clone, and the policy already cites
`policies/source-of-truth-policy.md` on the same footing. Recorded rather than
silently kept: cycle 4's removal was narrower than its wording reads.

## 6. Evidence

- `bin/check-frontmatter --all`: exit 0, **38 files matched from 8 globs** —
  unchanged by the `TREE.txt` removal, confirming the mention was inert.
  `bin/aimeta/scope.py` stops parsing at the `Out of scope` marker, so
  enforcement never read that prose.
- `python3 -m unittest discover -s bin -t bin -q`: **321 tests, OK**, before and
  after.
- **The hook flipped this policy itself.** Committing the F6 draft printed
  `FLIPPED policies/document-metadata-policy.md: agreed -> in-review (content
  edit)` — Package A's F1 hook, exercised on the document that defines its scope.
- The four documents edited in the fix round are `draft` or out of frontmatter
  scope, so no further status flip was triggered. Verified: statuses unchanged.
- Repo-wide `grep` for `TREE`: remaining hits are the frozen MANIFEST tombstone,
  dated cycle/review/package artifacts, and unrelated `EMPTY_TREE`/`WORKTREE`
  identifiers in `bin/`.

**Verification boundary.** Every mechanical claim above is bounded to this
repo's clone with `AI_METHODOLOGY_HOME` pointing at itself. The expedited path
has **not** been exercised in an adopting project repo or through the shim
configuration, and it has not been exercised end-to-end here either — no
document has yet been agreed through it. The first real use is unverified.

## 7. Known gaps and release risks

**Release risk, named rather than absorbed — the log entry is unenforced (B4).**
The policy now states the rule that carries the weight: the SHA cited in
`last-reviewed` must appear in an entry in the log. Nothing checks it.
`flip-agreed` verifies the artifact exists, the pointer parses, and the SHA
resolves to a commit — it never reads the file. Until that is fixed, any
document can reach `agreed` pointing at a record of nothing, and
`check-frontmatter --all` will call the repo clean. The fix is small and
checkable, but it is a `bin/` change with its own ACs and tests, and the
directive scopes Package D to F6 alone. **Dave's call at the gate whether it
lands before agreement.** Tracked in `OPEN-ITEMS.md`.

**The self-referential scope hazard survives for ordinary commits (B2).**
Condition 3 keeps the expedited path away from this policy, so the hazard is no
longer *authorized* — but any ordinary commit narrowing the in-scope globs still
blinds enforcement of the file making the change. Pre-dates F6. Tracked, paired
with the existing typo'd-glob diagnostic item, which is the same fix.

**Whether the Spec Reviewer gates non-spec canonical documents is unresolved
(N2).** Two canonical documents disagree, practice follows one of them, and
condition 4 is written to survive either answer. Tracked as a decision.

**Untested by construction.** Condition 5 is a human judgment; nothing verifies
it and nothing can. The claim this package makes is that conditions 1–4 bound
how much an unread diff could do — one commit, one file, ten body lines, not
this policy, not a spec — not that the diff will be read.

**F3 schema third-use feedback is recorded, not acted on.** The reviewer
supplied the third data point cycle 2 asked for on the `Severity:` qualifier,
plus three more observations. Package D touches that schema only for the B3
carve-out; the rest is tracked.

## 8. The compounding check

Dave named this one at cycle open, and it is the reason the check was run rather
than assumed: F6's log design had to respect the rule Package C wrote down in
its §8b —

> A derived measurement may live in a dated record — a change package, a review
> artifact, a commit message — but not in canonical text.

**It holds, in both directions, verified by reading every added line of the
diff.** Nothing in the new policy text imports a count, rate, or summary from
the log. The log's own header forecloses the reverse explicitly: *"It carries no
totals, rates, or rollups, and nothing derived from it belongs in canonical
policy text."*

The check also sharpened a distinction worth keeping. Conditions 1 and 2 put
numbers in canonical text — "exactly one" file, "no more than ten changed
lines" — and those are **not** the pattern §8b forbids. A threshold applied to a
diff at decision time is computable from `git show --stat` and cannot age; a
stored measurement of something that keeps changing will drift and then lie. The
count Package C wrote into MANIFEST was the second kind, which is why it moved
from 51 to 53 inside the package that recorded it. This one is the first kind.

The temptation this design specifically declined: an escalation rule of the form
*"if the expedited path has been used more than N times on one document, require
a full cycle."* It is the natural next feature, and it would put a derived count
of log entries into canonical policy text — §8b's exact failure, one package
after the rule was written. Not adopted, and recorded here so a later reader
knows it was considered rather than overlooked.

## 9. The rule this package produced

> **An existence check is evidence only while the thing has to be created.**

`last-reviewed` pointing at a file that exists was meaningful for four cycles
because each cycle produced a new artifact, and producing it was the work.
Pointing that same check at a permanent shared log preserves its form and empties
it — the tool still passes, the policy sentence still reads true, and the
guarantee is gone. Nothing in the diff looked wrong; B4 was found by executing
the sequence with a step deliberately skipped.

The general shape: when an artifact changes from per-event to permanent, every
check that merely asserts its existence silently becomes a no-op. The fix is not
a better sentence — it is to name what the check now has to look *inside* for,
which is why the policy states the SHA-in-log rule even though no tool enforces
it yet. A rule stated and unenforced is a gap; a rule unstated is a lie.

## 10. Release recommendation

**Recommend release, conditional on Dave's decision on the B4 tooling gap.**

The change is internally consistent, its two canonical contradictions are
reconciled in the same diff, the compounding check passes, and the mechanics were
verified by execution rather than by reading. The open risk is that the path's
one mechanical guarantee is currently hollow — recoverable at any time by a small
`bin/` change, and bounded in the meantime by the fact that the path has no users
yet.

Two things need Dave's judgment at the gate:

1. **Does the `flip-agreed` SHA-in-log check land before agreement, or after?**
2. **N2 — does the Spec Reviewer gate non-spec canonical documents?** A hard stop
   surfaced rather than resolved, per `policies/source-of-truth-policy.md`. F6
   does not block on it.

On go, the agreement flip lands as its own frontmatter-only commit with
`last-reviewed` pointing at `reviews/document-metadata-policy-cycle-5.md` and the
reviewed content SHA. It is not executed by this package.

## 11. Remaining sequence

F1–F7 are complete with this package. The streamlining directive's remaining
deferred items are `bin/gate-open` (F5, optional, build when a consequential
change next reaches a gate) and the wne-crm shim installation. The `bin/bundle`
supersession item was withdrawn by the Package C gate on a false premise.
