# Cycle 5 Directive — policies/document-metadata-policy.md (Package D — F6)

Date: 2026-08-02
Documents in scope:
- policies/document-metadata-policy.md @ 16d99aad2ef180e2c8b8a4f904ff8c11e0e62049
- reviews/expedited-log.md — new file, no prior revision

Review artifact: `reviews/document-metadata-policy-cycle-5.md`
Prior cycle: `reviews/document-metadata-policy-cycle-4.md`
Authorizing directive: `docs/cycles/streamlining-directive.md` — F6, plus the
rider assigned to this cycle by `docs/packages/package-c-change-package.md` §6
and §10.

Header SHAs written by `bin/cycle-open --cycle 5` at execution start, read from
git. The reviewed revision is `bb9a796`, the F6 draft committed on top of that
baseline; the cycle-5 gate review returned `changes-required` with 6 blocking,
8 non-blocking, and 4 observations.

**Standing constraint, restated because it governs the whole package:** the
expedited path may not be used to introduce itself. Package D runs the full
mechanics — reviewer gate, directive, review artifact, change package, human
go/no-go — for a change whose entire purpose is to make some future changes
cheaper than that.

## Decisions

### B1 — modify
Finding: The section asserted every eligibility condition was a fact about the
change, then made the load-bearing one a judgment, and bounded the diff's size
nowhere — so a full single-file rewrite of any policy was eligible on the text
as written.
Resolution: Do **both** halves of the reviewer's either/or, which the finding
allowed only as alternatives. Add a structural bound — no more than ten changed
lines, added plus deleted, per `git diff --numstat` — *and* correct the framing
so conditions 1–4 are named as facts and condition 5 as the one human judgment.
The reviewer's "but not both" guarded against keeping a false framing alongside
a bound; the framing is not being kept, it is being fixed. The threshold is
arbitrary and the text says so: a bright line that can be argued with is not a
bright line, and exceeding it costs a full cycle rather than blocking anything.

### B2 — accept
Finding: Condition 3 protected only the expedited section, leaving the Scope
globs expeditable; demonstrated in a scratch clone that one single-file edit
dropped enforcement from 38 files / 8 globs to 31 / 7 with no diagnostic, no
status flip, and no route back to `agreed` by tool.
Resolution: Widen the condition from "this section" to this **document**.
`policies/document-metadata-policy.md` returns to `agreed` only through a full
cycle. The condition states the mechanism — enforcement reads its in-scope set
from the Scope section — so the exclusion reads as a reason rather than a
carve-out. The underlying hazard pre-dates F6 and survives this fix for ordinary
commits; it is tracked in `OPEN-ITEMS.md` with the diagnostic that would close
it, paired with the existing typo'd-glob item.

### B3 — accept
Finding: `reviews/expedited-log.md` is a `last-reviewed:` target that does not
conform to the F3 review artifact schema, which defines its governed set as
exactly what `last-reviewed:` points at and does not grandfather artifacts
written after it landed — a canonical-vs-canonical contradiction, and a hard
stop under `policies/source-of-truth-policy.md`.
Resolution: Amend `skills/spec-review-cycle.md` with the carve-out, in the
generalized form: the schema governs artifacts produced by a review *cycle* —
one document, one cycle, one verdict — and a per-entry log is a record of
agreements whose shape is defined by the policy mandating it. Giving each log
line a `Verdict:` header was the other option and is absurd at one line per
entry. Silence was the one option `source-of-truth-policy` forecloses.

### B4 — modify
Finding: Step 3 of the sequence is unenforced. `flip-agreed` exited 0 against a
completely empty log and `check-frontmatter --all` then called the repo clean,
so the "an artifact that exists" guarantee is vacuous — permanently, and for
every document in the repo.
Resolution: Correct the policy's claim rather than let it stand, and state the
rule that actually carries the weight: **the SHA cited in `last-reviewed` must
appear in an entry in the log.** The policy now says plainly that the mechanical
rules are unchanged in form and weaker in effect, and why. The tooling fix —
have `flip-agreed` verify the cited SHA appears in the target artifact — is a
`bin/` change with its own ACs and tests, and the directive scopes Package D to
F6 alone, so it is tracked in `OPEN-ITEMS.md` and **named as a release risk at
the gate rather than absorbed as a known gap**. Dave decides at the gate whether
it must land before agreement.

### B5 — accept
Finding: `skills/conversation-retro.md` states "There is no second door into
`agreed` documents"; F6 builds one and does not amend it.
Resolution: One-clause amendment, in the direction the reviewer identified as
the sentence's actual intent: the door exists, and a retro-surfaced revision
does not use it. Scoping the claim to retros keeps it true.

### B6 — accept
Finding: No Package D change package exists, for the change the directive itself
classifies as the routing change.
Resolution: `docs/packages/package-d-change-package.md`, before agreement. It
was always sequenced after triage; the finding is correct that its absence at
review time left this artifact as the sole account of a change it is supposed to
be independent of.

### N1 — modify; N2 — defer with a decision request
Finding: The `specs/` exclusion protects the two lowest-consequence documents in
this repo and admits the highest-consequence ones, and means something
materially different in an adopting project repo; separately, two canonical
documents disagree on whether the Spec Reviewer gates a non-spec document at
all.
Resolution: Keep the `specs/` condition. With B1's ten-line ceiling and B2's
this-document exclusion in place, the scenario that made the inversion bite — a
full rewrite of a governing document on one human read — is no longer eligible,
so the residual override is bounded to a ten-line single-file diff. Re-pointing
the condition at "documents the Spec Reviewer hard-gates" was the reviewer's
alternative and is rejected **for now**, on the reviewer's own N2 evidence: that
definition is unsettled, and a condition resting on an unsettled definition is
worse than one resting on a path. The unsettled definition is a pre-existing
canonical contradiction, is tracked in `OPEN-ITEMS.md` as a decision for Dave,
and is surfaced to him at the gate per `policies/source-of-truth-policy.md`.

### N3 — accept
Finding: The path assumed one revision is one commit and said nothing about a
revision spanning two, leaving `last-reviewed` pointing at a mid-revision state.
Resolution: Fold into condition 1 — the revision is a single commit; a revision
spread across two escalates. Conditions 1 and 5 already assumed it.

### N4 — modify
Finding: The mandated log entry duplicates the date and the commit subject,
which git already holds — the pattern this policy's own Principle forbids.
Resolution: Keep both fields; state in the log header that the SHA is
authoritative, the date and clause are reader convenience, and `git show` wins
on conflict. Dropping them was the alternative; a log of bare paths and hashes
is a log nobody reads, and §8b of the Package C change package explicitly
licenses derived facts inside a dated record. The tension is real and is now
named in the file rather than left for a later reader to rediscover.

### N5 — accept
Finding: The `OPEN-ITEMS.md` entry this rider resolves was left live and is now
factually stale — it still reads "still names it" and "deliberately not fixed".
Resolution: Struck and marked resolved by Package D. Package D is also the
opener that discharges the handoff in `docs/packages/package-c-change-package.md`
§9: the two entries still claiming "Blocked on the policy reaching `agreed`" are
struck, since the policy is agreed, the hook is live, and the migration shipped
in Package B.

### N6 — reject, with the reasoning recorded
Finding: The new text reintroduces repo-relative document references of the kind
cycle 4 removed for portability.
Resolution: No edit. Cycle 4 removed pointers into *this repo's cycle history*
(`docs/cycles/cycle-2-directive.md`), which is genuinely absent from an adopting
repo. The new references are intra-methodology citations — `roles/`, `skills/` —
which an adopting project reaches through its `/ai` clone, and which this policy
already makes at the same footing when it cites
`policies/source-of-truth-policy.md`. Recorded rather than silently kept: cycle
4's removal was narrower than its wording reads. The third instance the finding
names, `reviews/expedited-log.md`, is answered by N7 instead.

### N7 — accept
Finding: The path requires `reviews/expedited-log.md` to exist and never says an
adopting repo creates it; the first expedited agreement there would fail on a
missing review artifact, reading as a review problem rather than a setup
omission.
Resolution: One clause in the record subsection — the adopting repo creates the
empty log when it stands up enforcement at project setup.

### N8 — accept
Finding: The cycle 5 directive was untracked and still carried its unfilled
template placeholders; the audit link from `16d99aa` to this review existed only
in a working tree.
Resolution: This document, committed, with placeholders removed and
`reviews/expedited-log.md` added to the documents in scope.

### O1–O4 — no action
Recorded as verified checks. **O1 is the one Dave named:** the compounding rule
from `docs/packages/package-c-change-package.md` §8b holds in both directions —
no count, rate, or summary crosses from the log into canonical policy text, and
the log's header forecloses the reverse. The reviewer notes the distinction that
keeps B1's ten-line ceiling legitimate under the same rule: it is a threshold
applied to a diff at decision time, computable from `git diff --numstat`, not a
stored measurement that can age.

## Deferred / out of scope

- `flip-agreed` verifying the cited SHA appears in the log (B4) —
  `OPEN-ITEMS.md`, and named as a release risk at the Package D gate.
- The self-referential scope hazard for ordinary commits (B2) —
  `OPEN-ITEMS.md`, paired with the existing typo'd-glob diagnostic item.
- Whether the Spec Reviewer gates non-spec canonical documents (N2) —
  `OPEN-ITEMS.md`, as a decision for Dave.
- F3 review artifact schema changes from third-use feedback —
  `OPEN-ITEMS.md`. Package D touches that schema only for the B3 carve-out.

## Execution notes

- The agreement flip is **not** executed by this directive. It lands as its own
  frontmatter-only commit after Dave's explicit go/no-go, with `last-reviewed`
  pointing at `reviews/document-metadata-policy-cycle-5.md` and the reviewed
  content SHA.
- Package D is treated as **consequential** for the release gate. It changes how
  a document reaches `agreed`, which is this repo's own review routing.
- Three documents outside `policies/document-metadata-policy.md` are edited, all
  as reconciliations the gate required rather than as scope expansion:
  `skills/spec-review-cycle.md` (B3), `skills/conversation-retro.md` (B5), and
  `OPEN-ITEMS.md` (N5 plus the Package C §9 handoff). All are `draft` or
  out-of-scope, so no additional status flip is triggered.
