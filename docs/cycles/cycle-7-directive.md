# Cycle 7 Directive — policies/document-metadata-policy.md (Package D — F6)

Date: 2026-08-02
Documents in scope:
- policies/document-metadata-policy.md @ fbbee6346a9224429d1d83b10a831fab242bdfaa
- docs/packages/package-d-change-package.md @ fbbee6346a9224429d1d83b10a831fab242bdfaa
- skills/spec-review-cycle.md @ fbbee6346a9224429d1d83b10a831fab242bdfaa
- OPEN-ITEMS.md @ fbbee6346a9224429d1d83b10a831fab242bdfaa
- skills/conversation-retro.md @ 7239ed2e2c105b341177f76d8f7a548bd69cef45
- reviews/expedited-log.md @ 7239ed2e2c105b341177f76d8f7a548bd69cef45

Review artifact: `reviews/document-metadata-policy-cycle-7.md`
Prior cycle: `reviews/document-metadata-policy-cycle-6.md`
Prior directive: `docs/cycles/cycle-6-directive.md`

Cycle 7 opened on a clean tree at `fbbee63`, per the commitment in the cycle-6
directive's execution notes. **Verdict `changes-required` — 3 blocking (B1
material), 4 non-blocking, 4 observations.** One of three cycle-6 blocking fixes
confirmed correct by re-execution; one present with a wrong number; one present
but incomplete. All six cycle-6 non-blocking fixes confirmed resolved.

The reviewer answered the convergence question it was asked and its judgment is
adopted as this directive's framing: the change is **converging, not diverging**
— the defect *kind* moved from design holes (cycle 5) to mis-sized fixes (cycle
6) to a short list and an arithmetic slip (cycle 7).

## Decisions

### B1 — accept, as a list edit, and the redesign is withdrawn
Finding: Condition 3's enumerated class is narrower than the class it defines.
Five in-scope documents match, are unnamed, and can have a gate deleted inside
the ceiling — `operating-model.md` (4 body lines removes both hard gates),
`roles/reviewer-agent.md` (2), `skills/conversation-retro.md` (4),
`boundaries/human-review-boundary.md` (1), `README.md` (2) — and no
release-specific document is enumerated despite "released" being in the class
definition.
Resolution: Extend the enumeration to fourteen documents: the five omissions,
the release trio the definition implied (`policies/release-readiness-policy.md`,
`roles/release-manager-agent.md`, `skills/release-readiness-review.md`),
`policies/source-of-truth-policy.md`, and the original five.

**The executor's proposed redesign is withdrawn on the reviewer's O2.** The
plan on reading B1 was to replace the enumeration with a fail-closed property
rule — exclude any document that states a gate, when in doubt excluded — on the
theory that a hand-maintained list in canonical text is the register class F7
spent a package removing. O2 refutes the premise directly: F7 removed registers
that **duplicate what a tool already derives**, and no tool can compute which
documents govern how work is reviewed. The list is a decision, not an
observation, and it is the same kind of artifact as the Scope globs directly
above it, which `bin/aimeta/scope.py` reads as the authority rather than checks
against one. Recorded because the reviewer wrote it as a warning — that
accepting the executor's framing would push the next round into replacing a
correct instrument with a judgment cycle 6 had already rejected — and the
warning was right.

The class definition is also tightened to what the reviewer measured: documents
stating a gate, hard stop, or enforcement rule over how **work** is reviewed,
agreed, or released. The earlier wording said "how documents are", which the
list never matched.

### B2 — accept
Finding: The cycle-6 N1 fix made the policy assert an exclusion held by
`skills/conversation-retro.md`, which the expedited path could delete in four
body lines — the fix that closed the last canonical contradiction created the
next one, in the same file.
Resolution: `skills/conversation-retro.md` joins condition 3's list, which is
the reviewer's preferred fix and is subsumed by B1's extension. The policy's
necessary-not-sufficient paragraph now points at a document the path cannot
reach.

### B3 — accept
Finding: §7 of the change package states "38 in-scope documents, 39 `status:
draft`, 1 `in-review`, 0 `agreed`" — parts summing to 40 against a total of 38.
Verified count: 37 draft.
Resolution: 37. No defence is offered and none exists: this is a measurement
copied into prose and then wrong, in the paragraph the release decision rests
on, in a package whose §8 is an argument against exactly that. The conclusion
the paragraph draws is unaffected — 0 `agreed` is correct — which is why it
survived three readings, and is the reason it is worth recording rather than
quietly correcting.

### N1 — accept
Finding: The Eligibility framing sentence is now wrong about two of the four
conditions it frames, and this is the third consecutive round in which that
sentence has been the defect.
Resolution: Shorten it — "Conditions 1–4 are facts about the change. Condition 5
is a human judgment, and it is the only one." — and stop enumerating how each is
checked. Condition 2 carries its own measurement instead: the `+`/`-` lines
below the frontmatter's closing `---`. The reviewer's diagnosis is adopted as
the reason: a framing sentence that restates a list is a second copy of the
list, and it drifted three times.

### N2 — accept
Finding: Condition 3's maintenance obligation is argued in the cycle-6 directive
and absent from the change package's Known gaps.
Resolution: A paragraph in §7 naming the obligation, the fact that cycle 7 found
its first instance immediately, and the borderline set that remains unsettled.
Also opened in `OPEN-ITEMS.md` with the forcing point the reviewer required as
its shipping condition.

### N3 — accept
Finding: §7 and §10 restate Package D's cost using a stale round count and a
number borrowed from §6's counting basis, understating the cost side of the
trade the package asks Dave to weigh.
Resolution: State the cost as it is — five edited documents, three cycle
directives, three review rounds.

### N4 — accept
Finding: The cycle-6 N3 fix left a mid-clause line break in canonical text.
Resolution: Re-wrapped. Recorded rather than fixed silently, for the reason the
finding gives: an unwrapped patch in a consistently hard-wrapped corpus is the
visible trace of an edit that was not re-read.

### O1–O4 — no action
Recorded as verified checks. O1 splits "present" from "correct" for the third
round running, which is what the re-execution is for. **O2 is the finding this
directive owes the most to** — see B1. O3 confirms six of six cycle-6
non-blocking fixes resolve rather than relocate, and rates the N4 SHA-form fix
better than the one it proposed. O4 confirms no regression across three commits
and three rounds: the policy diff against `16d99aa` still reduces to the same
three hunks.

## Deferred / out of scope

- Condition 3's borderline set — `policies/testing-policy.md`,
  `policies/verification-boundary-policy.md`, `roles/skeptic-risk-agent.md` —
  and whether the class definition narrows to the list or the list widens to the
  definition. `OPEN-ITEMS.md`, with the forcing point named.
- Everything deferred by `docs/cycles/cycle-5-directive.md`, unchanged.

## Execution notes

- **No cycle 8 is opened by this directive.** The reviewer's shipping judgment
  is that the design has held under three rounds of adversarial execution and
  what remains is bookkeeping. Opening a fourth round on the executor's own
  initiative would spend the human's budget past the point the gate itself
  reports diminishing returns. A cycle-8 confirmation pass over these edits is
  available and is Dave's call at the gate.
- The agreement flip is not executed by this directive. It waits on Dave's
  explicit go/no-go, and lands as a frontmatter-only commit with `last-reviewed`
  pointing at `reviews/document-metadata-policy-cycle-7.md` and the reviewed
  content SHA.
