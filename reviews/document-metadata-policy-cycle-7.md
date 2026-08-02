# Review: policies/document-metadata-policy.md — cycle 7

Verdict: changes-required
Reviewed: `policies/document-metadata-policy.md` @ `fbbee63` (baseline `4176b6b`)
Reviewer: Spec Reviewer Agent (same instance as cycles 5 and 6; not the drafting instance)
Date: 2026-08-02
Scope: execution of `docs/cycles/cycle-6-directive.md` — the three blocking fixes and all six non-blocking fixes, all accepted, none rejected. Second-pass review of `docs/packages/package-d-change-package.md`, including the new §5a. Re-measurement of condition 3's enumerated class against every in-scope document, re-execution of the cycle-6 B3 Case A / Case B experiment against the new body-only formulation, and a regression sweep across `16d99aa..fbbee63`.
Cross-checked: `docs/cycles/cycle-6-directive.md`, `docs/cycles/cycle-5-directive.md`, `docs/packages/package-d-change-package.md`, `reviews/document-metadata-policy-cycle-5.md`, `reviews/document-metadata-policy-cycle-6.md`, `skills/spec-review-cycle.md`, `skills/conversation-retro.md`, `roles/spec-reviewer-agent.md`, `roles/reviewer-agent.md`, `roles/release-manager-agent.md`, `policies/source-of-truth-policy.md`, `policies/agent-review-policy.md`, `policies/commit-and-change-control-policy.md`, `policies/release-readiness-policy.md`, `operating-model.md`, `README.md`, `boundaries/human-review-boundary.md`, `context-sets/base.md`, `OPEN-ITEMS.md`, `bin/aimeta/scope.py`, `bin/check-frontmatter`, `bin/flip-agreed`
Not inspected: `docs/packages/package-a-spec.md` ACs, `docs/packages/package-b-*`, `MANIFEST.md` beyond the frozen tombstone, `.claude/**`, `reviews/document-metadata-policy-cycle-1..4.md` and `reviews/package-c-cycle-1..2.md` beyond passages under citation, the remaining `context-sets/`, `skills/`, and `boundaries/` documents except where measured for condition 3. No adopting project repo or shim was exercised. The expedited path has still never been run on a real agreement — it cannot be, per B3 below.
Findings: 3 blocking (B1 material), 4 non-blocking, 4 observations
Prior cycle: `reviews/document-metadata-policy-cycle-6.md`
Dave should inspect: B1 (the enumerated class in condition 3 is incomplete on the day it was written — five measured omissions, `operating-model.md` chief among them), B3 (§7 of the change package states 39 draft documents out of 38, in the paragraph the release decision rests on), and the **Shipping judgment** section at the end, which answers the question the coordinator asked about whether this converges.

---

## B1 — blocking
Claim: Condition 3's enumerated class is narrower than the class it defines; at least five in-scope documents match the definition, are not named, and can have a gate deleted inside the ten-line ceiling.
Location: `policies/document-metadata-policy.md:156-172`
Evidence: **Verified by running,** in a scratch clone at `fbbee63`, measuring body-only changed lines for each deletion. Condition 3 defines the class as *"The document does not govern how documents are reviewed, agreed, or released"* and then fixes it by enumeration — *"a document not named here is not excluded by this condition"* — naming five paths. Measured omissions:

| document (not named) | edit | body lines |
| --- | --- | --- |
| `operating-model.md` | drop `(hard gate)` from change-flow steps 1 and 6 | **4** |
| `roles/reviewer-agent.md` | delete the Reviewer Agent hard-gate clause (`:11-12`) | **2** |
| `skills/conversation-retro.md` | delete the expedited-path exclusion (see B2) | **4** |
| `boundaries/human-review-boundary.md` | delete *"spec review (Spec Reviewer Agent gate before Dave agrees any spec)"* from Required replacement controls | **1** |
| `README.md` | delete the hard gate from principle 9 | **2** |

For completeness, the one candidate that does **not** fit: deleting `policies/source-of-truth-policy.md`'s entire *"Conflicts are a hard stop"* section measures 17 lines, over the ceiling. Separately, the class definition says *"reviewed, agreed, or **released**"*, and no release-specific document is enumerated — `policies/release-readiness-policy.md`, `roles/release-manager-agent.md`, and `skills/release-readiness-review.md` are all absent, with only `policies/commit-and-change-control-policy.md` carrying the release half.
Consequence: `operating-model.md` is the document that defines the change flow, both hard gates, and the release gate, and four changed lines take both gates out of it. `roles/reviewer-agent.md` states the Reviewer hard gate that `policies/agent-review-policy.md` — which *is* on the list — restates; the policy is protected and the role doc that owns the rule is not. The cycle-6 B2 fix therefore closes the two holes I measured last round and leaves the same hole open in five other places, which is the predictable cost of an enumeration and the reason the enumeration has to be right on arrival. It is not reachable today (B3's empty addressable set covers it) and becomes reachable the first day any of these five reaches `agreed`.
Fix: Extend the enumeration. `operating-model.md`, `roles/reviewer-agent.md`, and `boundaries/human-review-boundary.md` are the three I would argue are unambiguously in the stated class; `README.md` and `skills/conversation-retro.md` are judgment calls Dave should make, and the release trio is a fourth question. Alternatively, keep the list short and drop the class *definition* sentence, so the list stops advertising a scope it does not cover — but then the list has no principle behind it and the next document is added by argument rather than by rule.
Related: B2

## B2 — blocking
Claim: The cycle-6 N1 fix made the policy depend on an exclusion that lives in a document the path can edit in four lines.
Location: `policies/document-metadata-policy.md:193-197` against `skills/conversation-retro.md:16-20`
Evidence: **Verified by running.** The new paragraph reads: *"The five conditions are necessary, not sufficient. A document may exclude its own revisions from this path, and one does: `skills/conversation-retro.md` routes anything a retrospective surfaces through a full cycle regardless of size."* Deleting the clause it points at — *" — including where the expedited path in `policies/document-metadata-policy.md` would otherwise apply. That door exists; a retro-surfaced revision does not use it"* — measures `git diff --numstat` = `1 3`: **four changed body lines**. `skills/conversation-retro.md` is in scope, is not this policy, is not on condition 3's list, and is not under `specs/`, so conditions 1–4 are satisfied by that commit.
Consequence: The policy names an external constraint on its own path and cannot hold it. An expedited four-line edit to the retro skill silently makes the policy's paragraph at `:193-197` false — it will go on asserting that a document excludes its revisions after the exclusion is gone. This is the shape cycle 6 checked for and cycle 5 found twice (`AGENTS.md`, `conversation-retro.md`): a canonical document asserting something about another canonical document that the other one no longer says. Here the fix that resolved the last instance created the next one, in the same file.
Fix: Either add `skills/conversation-retro.md` to condition 3's enumeration — cheap, and it is arguably in the class already since it routes revisions — or state the dependency defensively at `:193-197` ("as of this writing, one does"), which is honest but leaves the drift. The first is better.
Related: B1

## B3 — blocking
Claim: §7's status enumeration is arithmetically impossible and states the wrong number, in the paragraph the release recommendation rests on.
Location: `docs/packages/package-d-change-package.md:242-245`
Evidence: **Verified by running.** §7 reads: *"verified by enumerating the in-scope set: **38 in-scope documents, 39 `status: draft`, 1 `in-review` (this policy), 0 `agreed`.**"* Counting `status:` across the in-scope set resolved through `bin/aimeta/cli.in_scope_files`: **38 files — `Counter({'status: draft': 37, 'status: in-review': 1})`.** The correct figure is 37. As written the parts sum to 40 against a stated total of 38, so the line is internally impossible before it is checked against anything.
Consequence: The number is presented as the verified enumeration behind the release recommendation, it is the specific fact cycle-6 B1 required the package to state, and it is wrong by two in a way that a reader who does the addition will catch immediately — which costs the package credibility on the paragraph that most needs it. It is also, precisely, a measurement copied into prose and then wrong, in a document whose §8 exists to reason about that failure. The conclusion the paragraph draws is unaffected: 0 `agreed` is correct, so the addressable set is empty and everything downstream of that holds.
Fix: 37. Nothing else in §7 changes.

---

## N1 — non-blocking
Claim: The Eligibility framing sentence is now wrong about two of the four conditions it frames — the third time this sentence has drifted from the list beneath it.
Location: `policies/document-metadata-policy.md:139-141`
Evidence: **Verified by running.** The sentence still reads *"Conditions 1–4 are facts about the change, readable from `git show --stat` and a path prefix."* Condition 2 now counts *body* lines with the frontmatter excluded, which `git show --stat` cannot produce — it reports whole-file insertions and deletions, and the cycle-6 B3 fix deliberately removed the `git diff --numstat` reference without naming a replacement command. Condition 3 is now a path *equality against a five-item enumeration*, not a path prefix. Conditions 1 and 4 still match the sentence.
Consequence: Small in practice — a reader with a ten-line diff can see the frontmatter block and skip it — but the sentence is the one a reader uses to decide whether they can apply the conditions mechanically, and it now overstates that for half of them. Recorded with its lineage because this is the third round in a row that this sentence has been the defect: cycle-5 B1 found it claiming condition 4 was a fact when it was a judgment; cycle-6 B3 found the constant it introduced was wrong; it is now wrong about the two conditions those fixes produced. A framing sentence that restates a list is a second copy of the list.
Fix: Either name the measurement in condition 2 (`git diff --numstat` on the diff with the frontmatter block excluded, or "count the `+`/`-` lines below the closing `---`"), or shorten the framing sentence to "Conditions 1–4 are facts about the change; condition 5 is a human judgment, and it is the only one" and stop enumerating how each is checked.

## N2 — non-blocking
Claim: Condition 3's maintenance obligation is argued in the directive and absent from the change package's Known gaps.
Location: `docs/packages/package-d-change-package.md:171-181` (§5a) and `:239-...` (§7), against `docs/cycles/cycle-6-directive.md:63-64`
Evidence: Inferred by reading, both texts quoted. The directive states the trade explicitly: *"The list carries a maintenance obligation, which is a real cost and the cheaper one."* §5a describes the enumeration and its fail-open semantics but never says it must be maintained, and §7 — the section a reader consults to decide on release — lists four gaps, none of which is this one. §8, which is the package's standing discussion of what may and may not live in canonical text, discusses conditions 1 and 2's numbers and does not mention that condition 3 just added a five-item register.
Consequence: The gap is real and B1 is its first instance, arriving in the same commit that created the list. A reader of §7 alone would not know the list needs revisiting whenever a governing document is added or a repo reorganizes; the policy's own portability clause at `:171-173` tells adopting repos to substitute their own, which is exactly when it will be forgotten. See O2 for why this is nevertheless the right trade.
Fix: One bullet in §7. The directive's sentence already says it well enough to lift.

## N3 — non-blocking
Claim: §7 and §10 restate Package D's cost using numbers that are stale or borrowed from a different counting basis.
Location: `docs/packages/package-d-change-package.md:253-255` and `:343`
Evidence: **Verified by running.** §7: *"Package D's cost is a consequential-tier cycle over three documents and two review rounds."* §10: *"verified by execution rather than by reading, across two gate rounds."* This is the third gate round. And "three documents" is §6's counting basis — documents outside F6's own deliverables and cycle records — used here for a *cost* claim, where the cost is five edited documents (`policies/document-metadata-policy.md`, `reviews/expedited-log.md`, `skills/spec-review-cycle.md`, `skills/conversation-retro.md`, `OPEN-ITEMS.md`) plus three directives and three review artifacts.
Consequence: Understates the cost side of a trade the package is explicitly asking Dave to weigh, in the paragraph that congratulates itself for stating both directions. The N5 fix that established the counting basis is correct where it was applied (§4, §6); the number then travelled into §7 under a different meaning, which is the same drift one level down.
Fix: Say what the cost actually was, or drop the number and say "a consequential-tier cycle and three review rounds."

## N4 — non-blocking
Claim: The N3 fix left a mid-sentence line break in canonical text.
Location: `skills/spec-review-cycle.md:116-118`
Evidence: **Verified by running** `sed -n '114,120p'`. The four inserted words pushed the wrap: *"…points at\n(`policies/document-metadata-policy.md`), with one exception below. They are\nread far more often than\nthey are written…"* — a five-word line followed by a four-word line, mid-clause.
Consequence: Cosmetic only, and it renders identically. Recorded because this repo's canonical documents are hard-wrapped consistently and an unwrapped patch is the visible trace of an edit that was not re-read — the same class of tell as the placeholder text cycle-5 N8 found in the directive.
Fix: Re-wrap the paragraph.

---

## O1 — observation
Claim: Of the three cycle-6 blocking fixes, one is confirmed correct by re-execution, one is present with the wrong number, and one is present but incomplete.
Location: `git diff 4176b6b fbbee63`
Evidence: **Verified by running,** fix by fix. **Cycle-6 B3 — confirmed correct.** The constant is gone; condition 2 now reads *"no more than ten changed lines of document body … there is no constant to subtract; measure the body"*, and it names why the constant was wrong rather than deleting it silently. Re-running the Case A / Case B experiment in a scratch clone: a two-line body insertion into an `agreed` `README.md` produced whole-file `numstat` of `4 2` in Case A and `3 1` in Case B — still divergent, as it must be — while the **body-only count was 2 in both**. The divergence the finding was about is gone. **Cycle-6 B1 — present, wrong number.** §7 now states the empty addressable set, in both directions, with the *"cannot be exercised"* correction and the reduced B4 exposure both spelled out; §5's qualifier holds (*"the eligibility conditions are a statement about changes, not a claim about which documents exist"*) and §10 carries it into the recommendation. The enumeration behind it is B3. **Cycle-6 B2 — present, incomplete.** Condition 3 is now a class, enumerated not judged, on the grandfather clause's fail-open design; it closes both holes I measured last round and leaves five open (B1).
Consequence: None beyond the findings. Recorded because "the fix is present" and "the fix is correct" have now diverged in three consecutive rounds, and the split is what the re-execution is for.

## O2 — observation
Claim: Condition 3's list is not the F7 defect class, and the trade is legitimate in kind even though B1 shows it was mispriced in fact.
Location: `policies/document-metadata-policy.md:156-172` against `docs/packages/package-c-change-package.md:192-224` (§8b) and the F7 rationale
Evidence: Inferred by reading, with the distinction checked against both sources. F7 removed registers that **duplicate something a tool already derives** — `MANIFEST.md`'s file registry, its changelog, `TREE.txt` — on the ground that a second copy of a derivable fact drifts and then lies. §8b generalized that to derived *measurements* in canonical text. Condition 3's list duplicates nothing: no tool can compute "which documents govern how documents are reviewed," and the list is a decision, not an observation. It is the same kind of artifact as the Scope section's in-scope globs directly above it — canonical, hand-maintained, and correctly so, since `bin/aimeta/scope.py` reads them as the authority rather than checking them against one.
Consequence: The coordinator's framing — that this is the defect class F7 spent a package removing — does not hold, and I want that on the record rather than absorbed, because accepting it would push the next round toward replacing a correct enumeration with a judgment the directive already rejected for good reason. What B1 shows is not that the list is the wrong instrument but that this instance of it was incomplete on arrival, which is a fixable fact rather than a structural objection. The maintenance obligation is real and is N2.

## O3 — observation
Claim: All six cycle-6 non-blocking fixes resolve rather than relocate; one of them produced B2.
Location: `git diff 4176b6b fbbee63`
Evidence: **Verified by running,** each against its finding. **N1** — the necessary-not-sufficient paragraph at `:193-197` restores the condition list's completeness and leaves the retro rule in the skill that owns it; resolved, and it is what B2 is about. **N2** — §5a's *"The departure, recorded as a departure"* restates the hook-flip constant as a process deviation rather than a finding, names the rule it broke, and notes the gate caught it in one cycle; resolved. **N3** — *"with one exception below"* at `skills/spec-review-cycle.md:117`; resolved, see N4 for the wrap. **N4** — the SHA rule at `:211-217` now says *"Same commit and same form … either requires both to match character-for-character or normalizes through `git rev-parse` first"*, which is exactly the comparison the deferred tool needs; resolved, and better than the fix I proposed. **N5** — §6 states the counting basis once and names the three documents; resolved where applied, see N3 for the leak. **N6** — `OPEN-ITEMS.md` now reads *"all scope the hard gate to spec documents, in three different formulations"*, which is what the evidence supports; resolved.
Consequence: None. Six for six on resolution; the residue is B2, N3, and N4.

## O4 — observation
Claim: No regression and no ride-along across three commits and three review rounds, and the cycle-open sequence was followed as the directive said it would be.
Location: `16d99aa..fbbee63`
Evidence: **Verified by running.** `git diff 16d99aa fbbee63 -- policies/document-metadata-policy.md` still reduces to **three hunks** — the frontmatter, the single out-of-scope line (the rider), and the revision-lifecycle-through-Sequence region — unchanged in count and location from cycle 6, after two further fix rounds. `git diff --stat 4176b6b fbbee63` shows six paths, all named by `docs/cycles/cycle-6-directive.md`. `git status` is clean at `fbbee63` with nothing staged, and the directive at `:16-22` records the cycle-6 `cycle-open` deviation and commits cycle 7 to the intended sequence — which held. `python3 -m unittest discover -s bin -t bin -q`: **321 tests, OK**. `bin/check-frontmatter --all`: *"38 file(s) matched, from 8 configured glob(s)"*, exit 0.
Consequence: None.

---

## Shipping judgment

The coordinator asked for this only if the verdict were not `changes-required`. It is, so I am outside the condition — but the question behind it is the one that matters at three rounds, and answering it is more useful than standing on the exemption.

**This is converging, not diverging.** The counts barely moved (6/8, then 3/6, now 3/4), but the counts are the wrong instrument; the *kind* changed. Cycle 5 found design holes — an unbounded path, a self-amending policy, a vacuous enforcement check, two canonical contradictions. Cycle 6 found the fixes for those holes were mis-sized and mis-scoped. Cycle 7 found one enumeration that is short by five entries, one pointer into a document that can be edited, and one arithmetic slip. Nothing in this round is a question about whether the design works. That is what convergence looks like, and I do not think a fourth round produces a fourth class of defect.

**Of the three blocking findings, one must be fixed and two are shippable.** B3 is a false number in the paragraph Dave decides from; it is a one-character fix and there is no version of "ship with it" that is defensible, because the package's own §8 is an argument against exactly that. B1 and B2 are different: both are unreachable today and stay unreachable until a second document reaches `agreed` through a full cycle — which is itself a reviewer-gated event, so the forcing point for fixing the enumeration arrives with a gate already attached to it. A reasonable owner ships B1 and B2 provided they are recorded in `OPEN-ITEMS.md` with that forcing point named explicitly: *before the second document is agreed, settle condition 3's list.* Recorded without the forcing point, they become the `TREE.txt` mention again — a known-wrong line carried because fixing it costs a cycle.

**The residual risk, stated plainly.** If Package D is agreed with B1 and B2 open, the exposure is: on the first day a governing document other than this policy reaches `agreed`, a single-file ten-line commit can remove a hard gate from `operating-model.md`, `roles/reviewer-agent.md`, `boundaries/human-review-boundary.md`, or `README.md`, or delete the retro exclusion, with Dave's read as the only control. That control is not nothing — condition 5 is a human reading a diff of at most ten lines, and a deleted hard gate is conspicuous in ten lines. The risk is that it is *quiet*: no tooling flags it, no reviewer sees it, and the resulting document goes on saying `agreed`. Combined with the B4 tooling gap, which is still open, the failure mode is a document that reaches `agreed` pointing at a log entry nobody wrote, having removed a gate nobody reviewed. Both halves are cheap to close and neither is closed.

**What I would tell an owner.** Fix B3, decide B1 as a list edit rather than a redesign, add one line for B2, and ship. The design has held under three rounds of adversarial execution; what is left is bookkeeping on a list, and bookkeeping does not get better by holding the change.
