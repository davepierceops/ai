# Cycle 6 Directive — policies/document-metadata-policy.md (Package D — F6)

Date: 2026-08-02
Documents in scope:
- policies/document-metadata-policy.md @ 4176b6b3d14c90dce851cd0c7e6fb866f23211ba
- docs/packages/package-d-change-package.md @ 4176b6b3d14c90dce851cd0c7e6fb866f23211ba
- reviews/expedited-log.md @ 7239ed2e2c105b341177f76d8f7a548bd69cef45
- skills/spec-review-cycle.md @ 7239ed2e2c105b341177f76d8f7a548bd69cef45
- skills/conversation-retro.md @ 7239ed2e2c105b341177f76d8f7a548bd69cef45
- OPEN-ITEMS.md @ 7239ed2e2c105b341177f76d8f7a548bd69cef45

Review artifact: `reviews/document-metadata-policy-cycle-6.md`
Prior cycle: `reviews/document-metadata-policy-cycle-5.md`
Prior directive: `docs/cycles/cycle-5-directive.md`

`bin/cycle-open` was not used to open this cycle. It refuses documents with
uncommitted modifications, correctly, and by the time cycle 6 reported, the
triage edits were already in the working tree. The SHAs above are read from git
per path and name the reviewed state — `4176b6b` for the two documents the
reviewer read at HEAD, `7239ed2` for the four last touched in the fix round.
Recorded rather than glossed: opening the cycle before editing is the sequence
`cycle-open` is built for, and cycle 7 should follow it.

Cycle 6 was a confirmation pass over the cycle-5 directive execution plus a
first-pass review of the change package. **Verdict `changes-required` — 3
blocking, 6 non-blocking, 4 observations.** Four of six cycle-5 blocking fixes
confirmed correct by re-execution; the two exceptions are both in the ten-line
ceiling and are B2 and B3 below.

## Decisions

### B1 — accept
Finding: The expedited path has no addressable document in this repo — not "no
users yet" but nothing it can be applied to. Verified: 38 in-scope documents, 0
`agreed`; the path is a *return* to `agreed`, and on the day Package D is agreed
this policy becomes the only `agreed` document and condition 3 excludes it. §5,
§7, and §10 of the change package read as "not yet exercised" where the accurate
statement is "cannot be exercised."
Resolution: State it in §7 with the enumeration behind it, carry it into §10's
recommendation, and qualify §5's "covers every other in-scope document" as a
statement about conditions rather than about documents. State both directions:
it makes the change's realizable benefit zero today, **and** it reduces the B4
exposure to zero in the interim. The reviewer flagged that the same missing fact
would have supported the recommendation; a package that only reports the half
that helps is the failure this repo's evidence rule exists to prevent.

### B2 — accept
Finding: Condition 3's own rationale is under-applied. Deleting the Spec
Reviewer hard-gate clause from `roles/spec-reviewer-agent.md` measures three
changed body lines; deleting the B3 carve-out just added to
`skills/spec-review-cycle.md` measures nine. Both are under the ten-line ceiling
and both were inside the path — so the expedited path could remove the hard gate
or re-open the contradiction cycle 5 closed, in one commit with no reviewer.
Resolution: Take the reviewer's first option and reject the second. Condition 3
becomes a class — documents governing how documents are reviewed, agreed, or
released — **enumerated, not judged**, on the same design as the grandfather
clause's disposition list: a document not named is not excluded. Named:
`policies/document-metadata-policy.md`, `policies/agent-review-policy.md`,
`policies/commit-and-change-control-policy.md`, `roles/spec-reviewer-agent.md`,
`skills/spec-review-cycle.md`. The alternative — "an expedited edit may not
delete or weaken a stated gate" — is rejected for the reason the reviewer gave
when offering it: it reintroduces exactly the judgment conditions 1–4 exist to
avoid. The list carries a maintenance obligation, which is a real cost and the
cheaper one.

### B3 — accept
Finding: The ceiling's stated exclusion — the hook's flip is "four of those
lines on every revision" — is wrong for grandfathered documents, where
`last-reviewed` is already null and the flip rewrites only `status:`, costing
two. Verified by running: `numstat` `4 2` versus `2 1`. An author subtracting 4
measures a twelve-line edit as ten, and the grandfather clause is exactly how
adopting repos arrive at that state.
Resolution: Drop the constant. Condition 2 counts changed lines of **document
body**, frontmatter excluded — no subtraction, no case analysis. The text names
why the constant is gone rather than silently removing it, since "two or four
depending" is the argument for not having one.

### N1 — accept
Finding: The B5 fix put a sixth eligibility exclusion in
`skills/conversation-retro.md` while the policy frames its five conditions as
the complete list.
Resolution: One paragraph after the conditions — the five are necessary, not
sufficient; a document may exclude its own revisions, and `conversation-retro.md`
does. Restores the list's completeness without moving the retro rule out of the
skill that owns it.

### N2 — accept, recorded as a process deviation
Finding: The hook-flip exclusion was an undirected edit to the canonical
document under review. `skills/spec-review-cycle.md` says an item that cannot be
executed as written goes back to triage — no improvisation on canonical
documents — and the improvised text is the one that carried B3's false statement
into the policy.
Resolution: Nothing to undo; B3 reworks that text regardless. Record it in the
change package **as a departure rather than as a finding**, which is how §5 first
presented it. The observation behind it was correct and the route was not, and
the gate caught it in one cycle — which is the argument for the rule.

### N3 — accept
Finding: The B3 carve-out is correct, but the schema's lead definition thirty
lines above still reads unqualified.
Resolution: Four words at the definition — "with one exception below."

### N4 — accept
Finding: The SHA-identity rule the deferred tooling will implement does not
specify abbreviation; `frontmatter.py` accepts 7–40 characters, so an
abbreviated pointer and a full-length entry are the same commit and different
strings.
Resolution: One clause in the rule — same commit and same form, or normalize
through `git rev-parse` before comparing. The rule is being written now so a
tool can be written against it later, so it has to say which comparison the tool
makes.

### N5 — accept
Finding: The change package counts the same set of edited documents twice and
gets three in one section and four in another; the actual fix-round commit
touches seven paths.
Resolution: Name the basis once — documents outside F6's own deliverables and
its cycle records — and use one number. Recorded because this is a package whose
§8 is about numbers copied into prose drifting from what they count.

### N6 — accept
Finding: The new `OPEN-ITEMS.md` N2 entry says three documents "say the same in
the same words"; they are three different formulations agreeing on scope.
Resolution: "all scope the hard gate to spec documents." Overstating one side is
the wrong error in an entry whose purpose is to ask Dave to settle a
disagreement.

### O1–O4 — no action
Recorded as verified checks. O1 confirms four of six cycle-5 blocking fixes
correct by re-execution and accepts the executor's "both halves" reasoning on
cycle-5 B1. **O2 is the check Dave named:** the compounding rule still holds
after the fix round, and the reviewer calls the declined count-based escalation
rule the strongest thing in the package — identifying the obvious next feature
as §8b's exact failure and recording the decision not to take it.

## Deferred / out of scope

Unchanged from `docs/cycles/cycle-5-directive.md`. No new deferrals: every
cycle-6 finding is dispositioned in this cycle.

## Execution notes

- The agreement flip is not executed by this directive. It waits on Dave's
  explicit go/no-go.
- Cycle 7 opens with `bin/cycle-open` **before** any edit, per the note above.
