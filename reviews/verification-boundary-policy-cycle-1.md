# Review: policies/verification-boundary-policy.md — cycle 1

Verdict: changes-required
Reviewed: policies/verification-boundary-policy.md @ 2b9c856
Baseline: none — first Pass 1 review. The file was a cycle-12 merge target,
edited only to receive merged content from the retired
boundaries/live-integration-boundaries.md and boundaries/mocked-boundaries.md;
its pre-existing text has never been through a rubric gate.
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter and all fourteen body sections — against all
ten criteria of docs/global-context/review-rubric.md @ 2b9c856. Two passes. (a)
The cycle-12 merge checked, verified by running `git diff cceef9a 2b9c856 --
policies/verification-boundary-policy.md`: five additions landed — the
session-kind line at :9-10, the mock-contract sentence at :22-23, `cadence` and
`failure response` in the boundary declaration, and the risk-based cadence rule
at :160-163. The contradicting YAML schema from mocked-boundaries.md was
discarded and this file's schema stands, as the decision required. What the
decision did not do is reconcile the merged file against the rest of the corpus,
and instruction 3 makes the path-shaped references and vendor names the executor
left in place findings now; both required lists are below. (b) All ten criteria
applied to the current text. Criterion 4 judged line by line against
docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md,
and operating-model.md @ 2b9c856. Mechanical sweeps run, all verified by running
grep: path-shaped references, vendor and product and tool names, retired terms.
All nine in-scope files cross-checked against each other for a term or rule
stated twice — this file is the largest single source of that duplication in the
scope, and V1, V2, and V5 are its three sites.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, context-sets/testing-and-verification.md,
context-sets/production-grade-software.md,
context-sets/spec-and-change-discipline.md,
boundaries/human-review-boundary.md, policies/source-of-truth-policy.md @
2b9c856; reviews/testing-and-verification-cycle-1.md (T2 and T4, both of which
recur here); the cycle-12 revision directive (the merge instruction and the
Evidence-classes home).
Not inspected: the rubric was applied, not reviewed. Whether the four role
obligations at :167-177 agree with roles/spec-reviewer-agent.md,
roles/reviewer-agent.md, roles/skeptic-risk-agent.md, and
roles/release-manager-agent.md — those files are outside the nine and none was
read, so V8 concerns the form of that section, not whether the obligations it
assigns are the ones those documents accept. The TRD's "standing verification
boundary section", which :170-171 requires the Spec Reviewer to check against,
was not located or read; V3's claim is about the `boundaries/` half of that
sentence, not the TRD half. Whether the merged sentences from the two retired
boundary files are complete — that no rule those files stated was dropped — was
not verified; the cycle-12 report is the record for that and this review did not
re-derive it. The YAML example's factual accuracy about any real provider was not
tested; V4 concerns its provenance, not its correctness. No bundler was run;
`bin/bundle-methodology` was read and neither includes this path nor consumes
`order:`. The directive's excluded items were not assessed.
Findings: 8 — 3 blocking, 3 non-blocking, 2 observations
Prior cycle: none — first artifact for this document
Dave should inspect: V2 — cycle 12 made LEXICON.md the single home for the
evidence-class vocabulary, and this file's §Required status labels is the second
home that decision was meant to eliminate; the two lists disagree on three of
nine entries. And V3 — §Documentation location tells agents to put durable
verification boundaries in `boundaries/`, which the same cycle-12 merge emptied
of them, so the policy now prescribes a home its own execution removed.

## Criterion 10 — disposition

**retain-with-changes.**

The file earns its place on five sections that nothing else in the nine states:

- **§Boundary declaration** (:38-53) — the eleven fields a declaration carries,
  including the `cadence`, `failure response`, and `owner or trigger` triple.
  context-sets/testing-and-verification.md carries the confidence *ledger* form
  (claim, evidence, boundary, deferred verification), which is four fields and a
  different artifact; nothing else names what a durable boundary record holds.
- **§Required triggers** (:122-134) — nine conditions under which a declaration
  must be created or updated. Stated nowhere else. This is the section that makes
  the policy operational rather than descriptive.
- **§Release impact labels** (:113-120) — four-valued, and `not-material` appears
  in no other file in the corpus, LEXICON.md included.
- **§CI and automation expectations** (:149-165), specifically the risk-based
  cadence rule the cycle-12 merge added: choose the mechanism by the risk of the
  boundary, not by a fixed schedule.
- **§Release requirement** (:179-188) — the four states every material boundary
  must be in before release, and "Implicit unknowns are not acceptable."

Three sections do not earn their place as written: §Policy statement's question
list (V1), §Required status labels (V2), and §Boundary types (V5), which
together are the duplication findings below. §Non-goals and the "important rule"
pair are rationale (V6). The finding list is the edit list, and the file is
coherent after it.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — V3, V4 |
| 2 | `audience:` is the selector | partial — `[all-roles, human]`, both reserved (`bin/aimeta/frontmatter.py:16`); no `order:`, though the file uses the evidence-class labels LEXICON.md (`order: 2`) defines and the response obligations operating-model.md (`order: 3`) states. No consequence demonstrable: verified by running, no bundler consumes `order:`, so no entry is opened |
| 3 | No path references | fail — V3 (3 sites, all `boundaries/`) |
| 4 | Core states it → remove it here | pass against Core and the Decision Layer specifically — zero restatements of either. The duplication in this file is against LEXICON.md and context-sets/testing-and-verification.md: V1, V2, V5 |
| 5 | Agent instruction, not authoring principle | partial — V8 |
| 6 | Instructions, not rationale | fail — V6 |
| 7 | Session kind is explicit | **pass** — :9-10, added by the cycle-12 merge |
| 8 | Tiers, not model names; route and model, not track | partial — zero model names and zero retired terms, verified by running grep; three product and tool names, V4 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename; `boundary: stadia.geocoding` is a declaration identifier, not a filename |

## Required lists (instruction 3)

- **Path-shaped references: 3.** All three are `boundaries/` — :140 ("`boundaries/`
  for durable cross-cutting boundaries"), :147 ("prefer `boundaries/` or a
  dedicated project verification ledger"), :170 ("durable boundaries declared in
  `boundaries/`"). Verified by running grep for backticked repo-relative paths.
  No other file path appears. All three are V3.
- **Vendor, product, and tool names: 3 names at 4 sites.** "jsdom" — :29 (in the
  list of things a test may use) and :94 ("jsdom replacing a real browser").
  "stadia" — :57, as the identifier `boundary: stadia.geocoding`. "MSW" — :59
  ("MSW handler with canned response fixture"). Verified by running grep. All
  four are V4. Zero model names.
- **Retired terms: 0.** Verified by running grep for "prompt", "dispatch",
  "sync block", and "track" in all forms.

## V1 — blocking
Claim: §Policy statement's six-question checklist is
context-sets/testing-and-verification.md's five-question checklist stated again,
and this file's version of the release-gap question contradicts this file's own
release-impact labels.
Location: policies/verification-boundary-policy.md:27-36
Evidence: Verified by reading both @ 2b9c856, item for item. This file :29-36 —
1. What production behavior is represented? 2. What did the evidence verify?
3. What did the evidence not verify? 4. What verification is required elsewhere?
5. Does the gap block release? 6. Who or what owns the follow-up?
context-sets/testing-and-verification.md:25-31 — 1. What production behavior is
being represented? 2. What does this test verify? 3. What does this test not
verify? 4. Where is the missing side verified? 5. If not verified, is that gap
blocking, deferred, or accepted? Items 1 through 4 are the same obligation in
near-identical words; item 5 is binary here and three-valued there; item 6 has no
counterpart there. The framing sentence above each list differs as well: this
file's :22-23, added by cycle 12, against that file's display quote at :24.
Verified by reading this file against itself: §Release impact labels at :113-120
requires every material gap to be labelled `blocking`, `deferred`,
`accepted-risk`, or `not-material`, and §Release requirement at :179-188 repeats
the same four states as prose — so question 5's yes/no cannot produce the answer
the same file demands eighty lines later. Verified by running grep: both files
carry `audience: [all-roles, human]`, so both land in every bundle together.
Consequence: This is the defect reviews/testing-and-verification-cycle-1.md T2
recorded against context-sets/base.md and cycle 12 closed by deleting that copy —
reappearing at a new pair, and this time the wrong copy is in the file that owns
the label vocabulary. An agent given both cannot tell whether the disclosure
requirement is five items or six. Worse, an agent that follows this file alone
answers "does the gap block release?" with "no" and has said nothing about
whether the gap is deferred with a named mechanism or accepted as risk — which
is exactly what §Release requirement then refuses to let it ship without. The
policy makes an obligation and withholds the vocabulary needed to discharge it,
in the same document.
Fix: Two edits. (a) Replace :33 with the three-valued form: "If not verified, is
that gap blocking, deferred, or accepted?" — which removes the internal
contradiction regardless of the home decision. (b) Make this file the single
home for the checklist, since it carries item 6 and the label vocabulary that
item 5 resolves into, and delete context-sets/testing-and-verification.md:25-31,
keeping its display quote at :24. If the home goes the other way instead, item 6
moves there and :29-36 goes.
Related: V2, V5

## V2 — blocking
Claim: §Required status labels is a second home for the evidence-class
vocabulary the cycle-12 decision single-homed in LEXICON.md, and the two lists
disagree on three of nine entries.
Location: policies/verification-boundary-policy.md:99-111
Evidence: Verified by reading both @ 2b9c856. This file lists nine labels:
`mock-verified`, `contract-verified`, `live-verified`, `browser-verified`,
`production-verified`, `unverified`, `deferred`, `accepted-risk`, `blocking`.
LEXICON.md §Evidence classes defines eight terms and opens "The classes an
evidence claim is labelled with. Every verification claim carries one." Five
match exactly. Three do not: LEXICON.md's term is "Deferred verification" where
this file's label is `deferred`; LEXICON.md's is "Accepted risk" where this
file's is `accepted-risk`; and `blocking` is a label here and is not an evidence
class in LEXICON.md at all. Verified by reading this file against itself:
`blocking`, `deferred`, and `accepted-risk` appear again four lines later at
:115-120 as three of the four §Release impact labels, so the file lists the same
three strings twice under two headings that mean different things — one a status
of the evidence, the other a status of the gap. Verified by running grep:
context-sets/testing-and-verification.md now carries no class definitions at
all, having deleted them at T1 in favour of LEXICON.md, so this file is the one
remaining second copy in the corpus.
Consequence: Cycle 12 moved the evidence vocabulary to LEXICON.md precisely
because it was defined twice and had drifted; this is the third copy it did not
find, and it has drifted the same way. An agent labelling a gap has two lists
with different strings and no statement of which governs, and Core rule 9
forbids resolving that by preference. The concrete failure is `blocking`: it
appears in this file's evidence-class list, where it is not an evidence class —
a gap that blocks release can be `mock-verified` — so a declaration can carry
`verification_class: blocking`, which is well-formed against this list and
meaningless against LEXICON.md's. The two-lists-in-one-file problem compounds it:
the reader has no way to tell that :99-111 and :113-120 are answering different
questions.
Fix: Delete :99-111. LEXICON.md's Evidence classes states the eight terms and is
`order: 2`, so it precedes this file wherever both are selected; a one-line
statement here — that every claim carries one of the evidence classes and every
material gap carries one of the release-impact labels below — states the
obligation without restating the vocabulary. `blocking` is not lost: it survives
as a release-impact label at :115, which is where it belongs.
Related: V1

## V3 — blocking
Claim: §Documentation location and §Reviewer obligations prescribe `boundaries/`
as the home for durable verification boundaries, and the cycle-12 merge that
edited this file is what emptied it of them.
Location: policies/verification-boundary-policy.md:136-147 and :167-171
Evidence: Verified by running `ls boundaries/` @ 2b9c856 — one file,
human-review-boundary.md, which is a control-surface boundary and declares no
verification boundary. Verified by running `git show --stat 40b5ffe`: the
cycle-12 revision deleted boundaries/live-integration-boundaries.md,
boundaries/mocked-boundaries.md, and boundaries/vendor-tooling-boundary.md, and
merged the first two *into this file*. Verified by reading: :140 lists
"`boundaries/` for durable cross-cutting boundaries" first among six places
boundary information may live; :147 instructs "For durable or repeated
boundaries, prefer `boundaries/` or a dedicated project verification ledger";
:169-171 instructs "The Spec Reviewer Agent should check that durable boundaries
declared in `boundaries/` are consistent with the TRD's standing verification
boundary section, and flag drift as a continuity finding." All three sentences
survive the merge unedited.
Consequence: Three failures at once, and the third is the live one. Criterion 3:
these are the file's only path-shaped references. Criterion 1: an agent reading
a generated bundle cannot open a directory. And the instruction itself no longer
works — the policy tells an agent to prefer a home that this same cycle emptied,
and gives the Spec Reviewer a standing obligation to check declarations in a
directory that contains none, so the check passes vacuously forever and reports
no drift because there is nothing there to drift. In an adopting project the
directory may not exist at all. The `boundaries/` convention was the corpus's
own arrangement, and the merge that dissolved it left the sentences that point
at it.
Fix: Restate the rule without the directory. :138-147 becomes a statement of
where boundary information belongs by kind — a project verification ledger for
durable or repeated boundaries, inline test comments for small local ones, a
change package or release-readiness review for release-relevant ones — with no
path. :169-171 becomes the obligation without its location: the Spec Reviewer
checks that declared durable boundaries are consistent with the TRD's standing
verification boundary section and flags drift as a continuity finding.
Related: V4

## V4 — non-blocking
Claim: The worked YAML example is drawn from a different project's domain and
names three products or tools, and a second tool name appears in the
policy statement.
Location: policies/verification-boundary-policy.md:54-76, and :29 and :94
Evidence: Verified by running grep for vendor, product, and tool names over the
current text — four sites, three names. :57 `boundary: stadia.geocoding`; :59
`representation: "MSW handler with canned response fixture"`; :94 "jsdom
replacing a real browser"; :29 "When a test uses a mock, fixture, jsdom, fake
timer, fake API…". The example's unverified claims are "domain/CORS rules allow
production browser usage", "quota and billing state are valid", and its deferred
verification is "live geocoding smoke test". Verified by reading: nothing else in
the nine in-scope files concerns geocoding or maps —
context-sets/testing-and-verification.md carried the identical defect at T4 and
was rewritten domain-neutral in cycle 12, and grep confirms zero occurrences of
"jsdom" or "TileLayer" there now. This file is where the pattern survives.
Consequence: Criterion 1, and criterion 8 at the margin. T4's reasoning applies
unchanged: the form is what the section teaches and the form survives
translation, so the cost is confusion rather than error. But this example is
longer and more concrete than the one T4 fixed — twenty-one lines of YAML naming
a specific geocoding provider — and it is the methodology's only worked example
of a boundary declaration, so it is what an agent for an arbitrary project
anchors on. "jsdom" additionally dates two sentences to one test runtime, which
is the same defect T4's fix resolved with "a headless DOM".
Fix: Rewrite the example against a domain-neutral pair, keeping every field and
changing only the nouns: an external API client and its request-parsing
boundary, with the representation named generically ("HTTP mock handler with a
canned response fixture") and the boundary identifier following suit. :29 and
:94 take T4's fix: "a headless DOM" for both, matching
context-sets/testing-and-verification.md:224.
Related: V3

## V5 — non-blocking
Claim: §Boundary types is a second sixteen-item enumeration overlapping
context-sets/testing-and-verification.md §Boundary-sensitive areas, with one
entry stated in both, and :153 states as an expectation what that file states as
an anti-pattern.
Location: policies/verification-boundary-policy.md:78-97 and :153
Evidence: Verified by reading both @ 2b9c856. Nine of this file's sixteen types
pair with an area in that file's sixteen: mocked HTTP APIs / external APIs;
mocked authentication and mocked authorization / auth and authorization; mocked
browser APIs / browser-only behavior; mocked map/tile providers and mocked
geolocation / maps, tiles, geolocation; mocked service workers / service workers
and PWA offline behavior; mocked storage / storage and persistence; mocked time /
time, timers, and scheduling; local environment variables replacing deployed
secrets/config / environment variables. One is not a pair but the same entry
twice: :97, "SLO targets and error budget state not yet connected to production
monitoring", against that file's :190-191, "SLO targets and error budget state —
production signals that tests cannot capture; error budget exhaustion is a
release-relevant condition". Separately, :153 — "Live/browser checks should
normally be separate from the default unit suite" — is that file's :228
anti-pattern, "adding live tests to every unit run", stated positively.
Consequence: Lower weight than V1 and V2 because the two lists are differently
cut and do not contradict — this one names representation mechanisms, that one
names areas where a claim is easy to overstate. The cost is that an agent asking
"what counts as a boundary?" gets two sixteen-item answers in one bundle with no
statement of how they relate, and any future addition has to be made in both:
the duplicated SLO entry already shows the two copies diverging, one framed as a
monitoring gap and the other as a release condition.
Fix: State the relation in one clause here — this list is representation
mechanisms, the boundary-sensitive-areas list is where claims are easy to
overstate — which is the move that closed the analogous overlap at
context-sets/testing-and-verification.md:198-199 and costs one line. Cut :97 in
favour of that file's fuller entry. :153 stands; an expectation addressed to a
suite and a prohibition addressed to an agent are worth stating separately.
Related: V1

## V6 — non-blocking
Claim: §Non-goals and the "important rule" pair argue for the policy rather than
instruct, and both restate rules the file has already stated.
Location: policies/verification-boundary-policy.md:165 and :190-194
Evidence: Verified by reading. :165 — "The important rule is not "run live tests
constantly." The important rule is "know which claims require
live/browser/production evidence."" :190-194, §Non-goals in full — "This policy
does not require live tests for every dependency in every run. It requires that
confidence boundaries be visible, intentional, and tied to release judgment."
Both are the same construction: a denial of a misreading followed by a
restatement. The rule each restates is already stated as an instruction — :27,
"Agents must not let tests imply broader confidence than they actually support",
and :14, "This policy makes verification boundaries visible and intentional." The
anti-over-testing point is additionally carried as an instruction at
context-sets/testing-and-verification.md:194 ("Boundary-sensitive does not mean
"must be overtested." It means "do not overclaim."") and as an anti-pattern at
its :229.
Consequence: Criterion 6, at seven lines. The cost is small and is the usual one:
text that defends a rule rather than stating it survives edits to the rule it was
defending, and a §Non-goals section is the natural place a future editor puts a
real constraint, where a reader looking for rules will not find it. Both
passages also sit at section boundaries — one closes §CI and automation
expectations, the other closes the file — which is where a reader skimming for
obligations stops reading.
Fix: Delete :165 and :190-194 including the §Non-goals heading. :27 and :14
state both rules as instructions, and §Release requirement's closing line
("Implicit unknowns are not acceptable") is the assertion the file should end
on.

## V7 — observation
Claim: §Release requirement restates §Release impact labels as prose.
Location: policies/verification-boundary-policy.md:179-188
Evidence: Verified by reading both. :113-120 labels each material gap `blocking`
("must be resolved before release"), `deferred` ("intentionally postponed with a
named mechanism"), `accepted-risk` ("Dave or the release process has explicitly
accepted the gap"), or `not-material` ("known but not relevant to the release
decision"). :181-188 requires that before release every material boundary is in
one of four states: "verified by an appropriate mechanism"; "explicitly deferred
with a named path"; "explicitly accepted as a known risk by Dave"; "explicitly
marked not material to the release". Three map one to one. The fourth does not:
`blocking` is a gap that must be resolved, and "verified by an appropriate
mechanism" is the resolved state — so the prose list names the outcome where the
label names the condition.
Consequence: None demonstrable, and the mismatch on the fourth entry is arguably
the point rather than a defect — a label describes a gap now, a release
requirement describes where every gap must have landed by then. Recorded because
the two lists are sixty lines apart and neither mentions the other, so a reader
meeting the second has no signal that it is the first one's discharge condition,
and V2's fix touches the same vocabulary.
Fix: If wanted, one clause at :179 tying the four states back to the four
labels. Not owed.

## V8 — observation
Claim: §Reviewer obligations assigns work to four named roles in the third
person, where the reader is one role.
Location: policies/verification-boundary-policy.md:167-177
Evidence: Verified by reading. Four sentences: "The Spec Reviewer Agent should
check…"; "The Reviewer Agent should check whether boundaries are named and
documented"; "The Skeptic/Risk Agent should challenge overbroad confidence
claims"; "The Release Manager Agent should ensure material boundary gaps are
resolved, deferred, or accepted before release." Rubric criterion 5 asks that
every rule be an instruction to the agent reading it. The file carries
`audience: [all-roles, human]`, so all four arrive at every agent, three of them
addressed to someone else.
Consequence: None demonstrable — an agent filling one of the four roles can find
its own line, and the section is short. Recorded because it is the one place in
the file where criterion 5 is answered by convention rather than by construction,
and because :169-171's obligation is unsatisfiable for a separate reason (V3),
which means the section needs an edit anyway.
Fix: If the section is rewritten for V3, the cheap form is second person under a
role heading, or a single sentence naming the obligation and letting the role
documents claim it. Whether the four obligations are the ones roles/ accepts was
not checked — see Not inspected.
Related: V3
