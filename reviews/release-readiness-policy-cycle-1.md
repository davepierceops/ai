# Review: policies/release-readiness-policy.md — cycle 1

Verdict: changes-required
Reviewed: policies/release-readiness-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent (execution session, frontier tier)
Date: 2026-08-22
Scope: the whole file, 77 lines, against all ten rubric criteria at docs/global-context/review-rubric.md @ 2a722bb.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/verification-boundary-policy.md, policies/commit-and-change-control-policy.md, policies/project-setup-requirements.md, roles/release-manager-agent.md, context-sets/testing-and-verification.md — all @ 2a722bb.
Not inspected: bin/ implementations; the four policies not in this cycle's scope; roles/ other than release-manager-agent.md; skills/; specs/, engagements/, writing/, vendors/.
Findings: 8 — 6 blocking, 2 non-blocking
Dave should inspect: the criterion-10 disposition. This is the one file of the four that I am recommending be removed rather than fixed, and the merge target narrows its audience from `all-roles` to the Release Manager. RR-1 sets out why nothing is lost by that; the judgment is his.

## Criterion 10 first — disposition

**Merge-into `roles/release-manager-agent.md`, then retire.**

The file lands in the `all-roles` bundle, and criterion 10 asks whether it
contributes something no other file in that bundle states. It does not.
Taking it section by section against the tree at 2a722bb:

- **Core rule** (:15) and **Ship/no-ship** support (:71) — Core rule 5.
- **Release package** (:19-30) — nine of its ten items are verbatim in
  `roles/release-manager-agent.md`:27-36, and the list overlaps
  `operating-model.md`'s change package.
- **`human-gate` issue** (:32-34) — `policies/commit-and-change-control-policy.md`
  states it, with mechanics this file does not have.
- **Required checks** (:36-49) — a menu of check names attached to no rule.
- **Known gaps** (:51-60) — Core rule 7 for the obligation; the four statuses
  are a second vocabulary for the release-impact labels in
  `policies/verification-boundary-policy.md`:104-109 (see RR-4).
- **Ship/no-ship recommendation** (:62-69) — verbatim in
  `roles/release-manager-agent.md`:44-49.
- **Dave's role** (:73-77) — Core rule 2 and Core rule 7.

The residue is a role's output schema, and the role document already carries it.
`roles/release-manager-agent.md` is the merge target: it is where the release
package and the recommendation vocabulary already live, and it is the audience
that acts on them.

**What the audience narrowing costs, and why it is safe.** Merging moves this
content from `all-roles` to `[release-manager-agent, chief-of-staff, human]`.
Nothing an all-roles reader needs goes with it: the release-decision obligation
is Core rule 2, the state-the-gaps obligation is Core rule 7, the release-impact
vocabulary belongs in LEXICON (RR-4), the boundary discharge conditions are in
`policies/verification-boundary-policy.md`:169-179 at `all-roles`, and the gate
mechanics are in `policies/commit-and-change-control-policy.md` at `all-roles`.
Every all-roles reader keeps what binds them.

**One thing must not be lost in the merge.** The four release-impact statuses
must land in a single home before this file is deleted, or the divergence in
RR-4 becomes a silent deletion of one of the two vocabularies.

## Criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — RR-6 |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`; moot on the merge |
| 3 | No references to other files by path | fail — RR-6, 1 path reference |
| 4 | Core states it → remove it here | fail — RR-2, RR-5 |
| 5 | Agent instruction, not authoring principle | fail — RR-7 |
| 6 | Instructions, not rationale | pass — the file is terse throughout |
| 7 | Session kind is explicit | fail — RR-8 |
| 8 | Tiers, not model names; route and model, not track | fail — RR-6 (vendor name); no model names, no retired terms |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |
| 10 | The file earns its place or is retired | merge-into `roles/release-manager-agent.md`, as above |

## RR-1 — blocking
Claim: The file fails criterion 10: every section is stated by another file in the same bundle, and the residue is a role's output schema that the role document already carries.
Location: policies/release-readiness-policy.md (whole file)
Evidence: Verified by reading all cross-checked files at 2a722bb; the section-by-section mapping is set out in the disposition above. The strongest single piece: `roles/release-manager-agent.md`:27-36 lists the release package as Change summary / User-visible behavior / Test evidence / Verification boundary status / SLO status and error budget consumption for affected Top K user journeys / Live-browser verification status, if relevant / Operational risks / Rollback or mitigation path / Known gaps / Ship-no-ship recommendation and Dave decision points. This file's :19-30 is the same ten items in the same order; items 1-9 differ only in "for any affected" versus "for affected" at item 5.
Consequence: Two files in one bundle stating one ten-item list. When a release package field is added or dropped, one copy is edited and the other is not, and neither reader can tell which is current.
Fix: Merge into `roles/release-manager-agent.md` and delete this file. RR-2 through RR-8 are the disposal instructions for each section; nothing in them is an edit to keep this file alive.

## RR-2 — blocking
Claim: The release package list is stated three times in the tree — here, in the role document, and (as the change package) in operating-model.
Location: policies/release-readiness-policy.md:17-30; roles/release-manager-agent.md:23-36; operating-model.md "Change package"
Evidence: Verified by reading all three at 2a722bb. The role document's list is 9/10 verbatim with this one (RR-1). operating-model's change package is a twelve-item list covering intent, ACs, test plan, implementation summary, test results, verification boundary updates, SLO status and error budget for affected Top K journeys, review findings, known gaps, operational notes, the `human-gate` tracker issue reference, and a release recommendation — a superset in scope, a different cut in shape. operating-model states plainly that the change package is the artifact and the release reply is not it; this file does not draw that distinction.
Consequence: Three lists, two of them near-identical and one deliberately different, with nothing stating how they relate.
Fix: On the merge, `roles/release-manager-agent.md` keeps the release-package list as the Release Manager's output schema, and states in one line that it is assembled from the change package rather than written fresh — the same derivation rule `policies/commit-and-change-control-policy.md`:105-108 states for the gate issue.
Related: RR-1

## RR-3 — blocking
Claim: The ship/no-ship recommendation vocabulary is stated verbatim in two files.
Location: policies/release-readiness-policy.md:62-69; roles/release-manager-agent.md:42-49
Evidence: Verified by reading both at 2a722bb. Both give exactly: ship / ship with accepted risks / do not ship / needs Dave decision.
Consequence: A controlled vocabulary with two homes is a controlled vocabulary that will acquire a fifth value in one of them.
Fix: Delete here. The role document keeps it — it is the role that emits the value.
Related: RR-1

## RR-4 — blocking
Claim: The known-gap statuses are a second, differently-worded vocabulary for the release-impact labels in `policies/verification-boundary-policy.md`, and neither file acknowledges the other.
Location: policies/release-readiness-policy.md:55-60; policies/verification-boundary-policy.md:104-109
Evidence: Verified by reading both at 2a722bb. This file: must fix before release / acceptable for release / deferred with follow-up / requires Dave decision. That file: `blocking` (must be resolved before release) / `deferred` (intentionally postponed with a named mechanism) / `accepted-risk` (Dave or the release process has explicitly accepted the gap) / `not-material` (known but not relevant to the release decision). The first three pair one-to-one on meaning and differ on every word. The fourth pair does not correspond: "requires Dave decision" is an unresolved gap awaiting judgment; `not-material` is a resolved gap that does not bear on the release. That file additionally states the discharge conditions at :169-179 and calls the labels' meanings normative; LEXICON.md already houses "Accepted risk" and "Deferred verification" under Evidence classes.
Consequence: A release package written from this file and a boundary declaration written from that one label the same gap with different words, and a reader reconciling them has to guess whether "requires Dave decision" is a fifth state or a synonym. Core rule 9 applies: the disagreement must be surfaced, not resolved by picking one.
Fix: **This is the single-home proposal.** One release-impact vocabulary, defined in `LEXICON.md` beside the evidence classes it already carries, with the fifth state — a gap awaiting Dave's judgment — either added as a named label or explicitly folded into `blocking`. `policies/verification-boundary-policy.md` keeps the discharge conditions and uses the LEXICON labels; `roles/release-manager-agent.md` uses them for known gaps in the release package. Both LEXICON and verification-boundary-policy are through Pass 1, so this is Dave's call before the merge proceeds.
Related: RR-1

## RR-5 — blocking
Claim: Five statements restate Core.
Location: policies/release-readiness-policy.md:15, :53, :71, :75, :77
Evidence: Verified by reading docs/global-context/core.md at 2a722bb. :15 "A release decision must be based on explicit evidence, known gaps, and accepted risk" and :71 "The recommendation must be supported by evidence" — Core rule 5, "Claims require evidence. Output is trusted to the degree inspectable evidence supports it." :53 "Known gaps must be stated explicitly" and :77 "risk should not be hidden or implied" — Core rule 7, "Say what is unverified. Never report assumed as verified." :75 "Dave makes the release decision" — Core rule 2, "Dave decides. You propose. Agreement, release, prioritization, and publication are his."
Consequence: Five lines restating rules that load first in every bundle and cannot be waived, in a file loaded after them.
Fix: Delete. None of it carries to the merge target.
Related: RR-1

## RR-6 — blocking
Claim: The `human-gate` requirement restates `policies/commit-and-change-control-policy.md`, references it by path, and names a vendor.
Location: policies/release-readiness-policy.md:32-34
Evidence: Verified by reading. The text: "For consequential changes, a `human-gate` GitHub issue must also be open and linked in the release package before Dave's go/no-go is sought. See `policies/commit-and-change-control-policy.md`." That policy states the same requirement at :98-137 with the mechanics this line lacks. `roles/release-manager-agent.md`:20 and :38-40 state it a third time. This file's only path reference is here, and "GitHub" is its only vendor name; operating-model's change package item 11 uses the neutral "tracker issue."
Consequence: Criterion 3, criterion 4, and criterion 8 fail on three lines. A fourth statement of one requirement, using the vendor-bound name.
Fix: Delete. The role document already carries the Release Manager's half of it and should use "tracker issue"; `policies/commit-and-change-control-policy.md` remains the single home for the requirement.
Related: RR-1

## RR-7 — non-blocking
Claim: The Required checks section states no rule — it is a list of check names introduced by a sentence that declines to bind anything.
Location: policies/release-readiness-policy.md:36-49
Evidence: Verified by reading: "The required checks depend on risk, but common checks include:" followed by ten items from unit tests to accessibility spot checks. Nothing states when any of them is required, who decides, or what happens if one is skipped. `policies/verification-boundary-policy.md`:141-155 states the rule this section gestures at — live and browser checks separate from the default unit suite, chosen by the risk of the boundary rather than a fixed schedule — and `context-sets/testing-and-verification.md`:220-222 states the floor (keep fast mocked/unit tests; at least one live or browser smoke test for material external or user-visible integrations).
Consequence: Criterion 5 — an agent cannot act on it. A reader looking for the rule finds a menu, and the two files that do state the rule are not named.
Fix: Delete. The rule is already stated in two files that are through Pass 1 or in scope elsewhere; nothing here needs to carry to the merge target.
Related: RR-1

## RR-8 — non-blocking
Claim: The file does not state which session kind it is for.
Location: policies/release-readiness-policy.md:1-11
Evidence: Verified by reading; no session-kind statement. `policies/verification-boundary-policy.md`:9-10, a peer policy through Pass 1, opens with one, and `operating-model.md`:9 does the same.
Consequence: The release decision is Dave's and the package is assembled by an agent; which session kind assembles it is left to inference.
Fix: On the merge, `roles/release-manager-agent.md` states the session kind for the role. Nothing to fix here.
Related: RR-1
