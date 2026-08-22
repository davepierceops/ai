# Review: context-sets/testing-and-verification.md — cycle 1

Verdict: changes-required
Reviewed: `context-sets/testing-and-verification.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11a)
Date: 2026-08-21
Scope: the whole file — frontmatter and all eleven body sections — against all
ten criteria of `docs/global-context/review-rubric.md` @ `7310937`. This is the
file's first review artifact of any kind. Criterion 4 judged line-by-line
against `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, and `operating-model.md` @ `7310937`, and additionally against
`context-sets/base.md` @ `7310937`, which states the same evidence vocabulary
this file elaborates. The five class definitions were compared word for word
against `context-sets/base.md:56-66` to establish T1's drift claim. Mechanical
sweeps run (verified by running `grep`): retired terms, vendor and model names,
path-shaped references.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `operating-model.md`, `context-sets/base.md`,
`context-sets/production-grade-software.md`, `specs/prd-template.md` (the "Top K"
definition line only), `bin/aimeta/frontmatter.py`, `bin/bundle`,
`bin/bundle-methodology`
Not inspected: whether the eight evidence terms are used correctly in the
repository's own `reviews/`, `retros/`, `boundaries/`, and `roles/` documents —
that sweep was not run, and T1's single-home recommendation is made on the
placement argument alone, not on a survey of consumers. The SLO and error-budget
material at L134–144 and L196–197 was read but not checked against
`boundaries/live-integration-boundaries.md`, `roles/release-manager-agent.md`,
or `specs/trd-template.md`, so no claim is made about whether its
production-verified reporting requirements agree with theirs. The confidence
ledger example's factual accuracy about jsdom and TileLayer behaviour was not
tested; T4 concerns the example's provenance, not its correctness.
Findings: 10 — 3 blocking, 3 non-blocking, 4 observations
Prior cycle: none
Dave should inspect: T1 — this file and `context-sets/base.md` both define the
evidence classes, they have already drifted in two places, and the single-home
decision (recommended: `LEXICON.md`) determines what this file is reduced to.
That recommendation is stated in full at `reviews/base-cycle-1.md` B5.

## Criterion 10 — disposition

**retain-with-changes.**

The file earns its place, but on less of itself than it looks. Its definitions
of the five verification classes are a second copy of
`context-sets/base.md:56-66` (T1). What is genuinely its own is the operational
material wrapped around them:

- **The useful-for / does-not-prove tables** (L37–145). For each class, what the
  evidence supports and — the half that does the work — what it specifically
  does not. Nothing else in the corpus states that mock-verified does not prove
  third-party auth, live schema stability, deployment config, quota state, or
  CORS rules. This is the file's reason to exist.
- **The confidence ledger** (L147–165), as a form: claim, evidence, boundary,
  deferred verification. Stated nowhere else, though its worked example is
  borrowed from another project (T4).
- **Test plan requirements** (L167–180) — ten items. `operating-model.md`
  §Change package names a test plan as item 3 of a change package but never says
  what one contains.
- **Boundary-sensitive areas** (L182–200) — the default-suspect list, plus the
  closing instruction that boundary-sensitive means "do not overclaim," not
  "must be overtested."
- **Minimal acceptable practice** (L219–227) — the floor for a small or
  early-stage project. Unstated elsewhere.

Five sections of real contribution against three that duplicate. The finding
list below is the edit list; its shape depends on T1's single-home decision,
which is why T1 is first.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — T3, T4, T7 |
| 2 | `audience:` is the selector | partial — T9 |
| 3 | No path references | fail — T3 (one site, the file's only one) |
| 4 | Core states it → remove it here | fail — T1, T2, T3, T5, T6 |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | pass — L13–19 frames but does so in two sentences that each carry a rule |
| 7 | Session kind is explicit | fail — T8 |
| 8 | Tiers, not model names | partial — T4 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |

## Counts (instruction 4)

- **Rules restated from Core / Decision Layer / LEXICON / operating-model:** 4
  direct — `operating-model.md:70` (the obligation to distinguish the classes,
  which this file's §Verification classes implements), `operating-model.md:76`
  and `:78` (two anti-patterns), Core rule 7 (one anti-pattern). The larger
  duplication in this file is **against `context-sets/base.md`, not against the
  foundation**: 5 class definitions (T1), the mock rule and its checklist (T2),
  and the green-suite rule (T3) — 7 restatements across 3 sections.
- **Path-shaped references:** 1 — `context-sets/base.md` (L204). The lowest
  non-zero count in this cycle's scope.
- **Vendor and model names:** 1 tool name, twice — "jsdom" (L160, L235). No
  vendor or model names.
- **Retired terms:** 1 — "tracking" (L136), in the ordinary-verb sense.
  See T10; the defect is in the `LEXICON.md` retirement entry, not here.

## T1 — blocking
Claim: The file defines five of the eight evidence classes that
`context-sets/base.md` also defines, and the two copies have already drifted in
two places.
Location: `context-sets/testing-and-verification.md:33-145`
Evidence: Verified by reading, word for word against `context-sets/base.md:56-66`
@ `7310937`. Two definitions differ substantively. (a) Live-verified —
`base.md`: "against a real external system **or deploy-like service**"; this
file L84: "against a real external service." The deploy-like-service case is in
one copy and not the other. (b) Production-verified — `base.md`: "through
deployed telemetry, monitoring, synthetic checks, or real production signals";
this file L125: "through telemetry, monitoring, synthetic checks, **logs**, or
real production signals." Logs are in one copy and not the other. Three
definitions match in substance (mock-, contract-, browser-verified). Verified by
running: `grep` over `operating-model.md` @ `7310937` confirms it states the
obligation at `:70` and defines none of the terms; `grep` over `LEXICON.md`
confirms it carries none of the eight.
Consequence: The evidence model is the thing this repo's core rule rests on, and
its vocabulary is defined twice with two disagreements. An agent asked whether a
check against a staging deploy is live-verified gets "yes" from
`context-sets/base.md` and "no" from this file — and both files are
`audience: [all-roles, human]`, both reachable from `base`, so it will routinely
have both. Core rule 9 then forbids resolving it by preference. The
staging-deploy case is not hypothetical; it is the single most common ambiguity
this vocabulary is asked to settle.
Fix: Depends on the single-home decision, recommended in full at
`reviews/base-cycle-1.md` B5: **move all eight terms to `LEXICON.md`**. Then
delete the one-line definition that opens each of the five subsections here
(L39, L63, L84, L104, L125) and keep the useful-for / does-not-prove lists,
which are this file's contribution and belong nowhere else. The subsections
become "what this class does and does not support," with the term itself defined
once, upstream, in the file that exists to define terms. Reconcile the two drift
points into the `LEXICON.md` entries in the same edit, per Core rule 13 — both
the deploy-like-service case and logs should survive.
Related: T2, T3

## T2 — blocking
Claim: The mock rule is stated in both this file and `context-sets/base.md`,
with checklists of different lengths.
Location: `context-sets/testing-and-verification.md:22-31`
Evidence: Verified by reading, both @ `7310937`. Both files state "A mock is a
claim with a deferred proof" as a display quote. This file then asks five
questions: what production behavior is being represented; what does this test
verify; what does it not verify; where is the missing side verified; if not
verified, is that gap blocking, deferred, or accepted.
`context-sets/base.md:100-107` asks four: what the mock verifies; what it does
not verify; where the deferred verification happens; whether the gap blocks
release. This file's Q1 — what production behavior is being represented — has no
counterpart in `base.md`, and its Q5 offers three outcomes (blocking, deferred,
accepted) where `base.md`'s Q4 is binary (blocks release or not).
Consequence: An agent given both cannot tell whether the mock disclosure
requirement is four items or five, and the two versions disagree on the shape of
the answer to the last one — binary in one, three-valued in the other. The
three-valued form is the one that matches this repo's own vocabulary, since
`context-sets/base.md:66` defines "accepted risk" as a distinct class; so the
shorter copy is the wrong one, and it is the copy in the file the whole
context-set tree depends on.
Fix: Keep this file's five-question form and delete
`context-sets/base.md:100-107` — the deletion is already on `base.md`'s edit
list at `reviews/base-cycle-1.md` B7. No change to this section.
Related: T1

## T3 — blocking
Claim: §What green means both restates `context-sets/base.md` and cites it by
path — the file's only path-shaped reference, spent on the one thing it did not
need to say.
Location: `context-sets/testing-and-verification.md:202-205`
Evidence: Verified by reading. The section reads in full: "See
`context-sets/base.md`. A green test suite proves only that the tested scenarios
passed under the conditions represented by the tests — not shippability."
`context-sets/base.md:85-98` states the same rule and then enumerates six things
green does not mean. Verified by running: this is the only backticked
repo-relative `.md` path in the file.
Consequence: Criterion 3 and criterion 4 in four lines. The pointer is
unfollowable inside a bundle, and the sentence after it makes the pointer
pointless — the rule is already restated, in compressed form, right there. If
`context-sets/base.md` is retired or reduced (see `reviews/base-cycle-1.md` B1),
this is a dangling reference and a `bin/bundle` edge that stops resolving.
Fix: Delete L202–205. The rule is stated by `operating-model.md:76`
("equate passing tests with shippability" is prohibited) and, in its enumerated
form, wherever `context-sets/base.md`'s §Verification rule lands. This file's
§Summary already opens with the stronger version of the same point: "The central
risk is not undertesting. The central risk is **overclaiming what a test
proves**."
Related: T1

## T4 — non-blocking
Claim: The confidence ledger's worked example is drawn from a different
project's domain and names a library.
Location: `context-sets/testing-and-verification.md:151-163`
Evidence: Verified by reading. The example's two claims are "Geocoding request
parser handles valid provider response" and "Map page renders a TileLayer
component," with evidence "Component test in jsdom" and deferred verification
"browser smoke test with network observation." Verified by running: `grep -niE
'jsdom'` returns L160 and L235. Nothing elsewhere in the six in-scope files
concerns geocoding, maps, or tiles; `context-sets/production-grade-software.md`
and `operating-model.md` are domain-neutral throughout.
Consequence: Criterion 1, and criterion 8 at the margin. An agent reading a
generated bundle for an arbitrary project is shown the methodology's only worked
example of its ledger format in the vocabulary of a maps application it is not
working on. The form is what the section teaches and the form survives
translation, so the cost is confusion rather than error — but "TileLayer" and
"jsdom" are the two most concrete nouns in the section, and concreteness is what
a reader anchors on. `jsdom` additionally dates the example to one test
runtime.
Fix: Rewrite both entries against a domain-neutral pair — an external API client
and a rendered view — naming no library. Two lines each; the format is
unchanged. L235's anti-pattern ("treating jsdom rendering as browser rendering")
is the same defect and has the same fix: "treating a headless DOM as browser
rendering."

## T5 — non-blocking
Claim: Three of the eight anti-patterns restate prohibitions already binding
from `operating-model.md` or Core.
Location: `context-sets/testing-and-verification.md:229-240`
Evidence: Verified by reading. L234 ("treating mocked fetch tests as live API
verification") → `operating-model.md:78` ("claim live behavior from mocked
evidence"). L233 ("using coverage as proof of correctness") → `operating-model.md:76`
("equate passing tests with shippability") and Core rule 5. L240 ("shipping with
implicit unverified boundaries") → Core rule 7 ("**Say what is unverified.**").
Not restated: L235 (jsdom, see T4), L236 (agent review as evidence without
stating what was reviewed), L237 (fixtures without knowing what assumptions they
encode), L238 (adding live tests to every unit run), L239 (refusing mocks
because live behavior matters). The last two are the section's best entries —
both push back against overcorrection and appear nowhere else.
Consequence: Modest. Eight items presented as one list, three of which are
restatements, so the section reads as more additive than it is. The two
overcorrection entries are the reason to keep it.
Fix: Delete L233, L234, L240. Keep the other five.

## T6 — non-blocking
Claim: §Required output overlaps `context-sets/base.md`'s standard response
shape without either file acknowledging the other.
Location: `context-sets/testing-and-verification.md:207-217`
Evidence: Verified by reading. This file requires, when tests are written or
reviewed: what is verified; what is not verified; what is mocked; what
assumptions the fixture encodes; whether live/browser/production verification is
needed; how the verification boundary is recorded; whether any gap blocks
release. `context-sets/base.md:75-83` requires, for substantial implementation,
review, or release work: Role, Intent, Evidence, Boundary, Gaps,
Recommendation, Dave decision points. Three map directly — verified/not-verified
→ Evidence and Boundary; whether a gap blocks release → Gaps and Dave decision
points.
Consequence: An agent doing test review owes two output shapes, one seven-part
and one seven-part, that neither nest nor compose, and no sentence in either file
says how they relate. The likely behaviour is that it satisfies whichever it read
last. Lower weight than T1 because the two lists do not contradict — they are
differently cut, not disagreeing.
Fix: State the relation in one clause here: this section is the
verification-specific expansion of the Evidence, Boundary, and Gaps elements of
the standard response shape, not a second shape. That keeps both and removes the
ambiguity without a path reference, since the standard response shape will be in
the same bundle wherever it lands.

## T7 — observation
Claim: "Top K" is used as a defined term and is defined only in a per-project
spec template no methodology bundle carries.
Location: `context-sets/testing-and-verification.md:135,196`
Evidence: Verified by running. `grep -rn "Top K"` across the tree @ `7310937`
finds the only definition at `specs/prd-template.md:43`; `specs/trd-template.md:59`
forbids redefining it; `grep` over `LEXICON.md` returns no entry. Eight
governing documents use the term.
Consequence: Criterion 1. Same defect reported at
`reviews/production-grade-software-cycle-1.md` P4, recorded here because this
file is a second site — L134–138 makes SLO target compliance and error budget
consumption part of what production-verified means, so the undefined term sits
inside a class definition.
Fix: `LEXICON.md` entry, per P4. No edit owed in this file beyond whatever T1
does to the surrounding definition.

## T8 — observation
Claim: Session kind is never stated.
Location: `context-sets/testing-and-verification.md:1-11`
Evidence: Verified by reading. `audience: [all-roles, human]`; no declaration.
Compare `docs/global-context/core.md:10`,
`docs/global-context/decision-layer.md:10`, `operating-model.md:10`.
Consequence: Criterion 7. Unlike
`context-sets/spec-and-change-discipline.md` (S10 of this cycle), the answer here
is unambiguous — every section governs an execution session writing, reviewing,
or relying on tests. The gap is a missing sentence, not mixed content.
Fix: Add one line after the H1: "Rules for execution sessions."

## T9 — observation
Claim: No `order:`, and three frontmatter fields that nothing reads.
Location: `context-sets/testing-and-verification.md:1-9`
Evidence: Verified by reading and running. `audience: [all-roles, human]` — both
reserved, valid per `bin/aimeta/frontmatter.py:16`. No `order:`. `context-set:`,
`purpose:`, and `include-when:` are consumed by neither `bin/bundle` (reads
`depends-on:`) nor `bin/bundle-methodology` (reads `audience:`).
Consequence: This file declares `depends-on: [base]` and, under T1's fix, will
depend on `LEXICON.md` having stated the eight terms first. Nothing in the
metadata orders it after either.
Fix: Add `order:` after `context-sets/base.md`'s value. Drop `context-set:`,
`purpose:`, and `include-when:`.

## T10 — observation
Claim: A retired term appears, in a sense `LEXICON.md` does not carve out.
Location: `context-sets/testing-and-verification.md:136`
Evidence: Verified by running — `grep -niE '\btracking\b'` returns L136: "error
budget consumption — tracking how much of the allowed failure budget has been
spent." `LEXICON.md:69-70` @ `7310937` retires "Track" with the reason stated
(a directive has no third part) but no scope clause.
Consequence: On a literal reading of the retirement, the ordinary verb is
retired too, and this line violates it. The reading is almost certainly not
intended — `operating-model.md:143` and `:155` use the same sense and are
through Pass 1 — so the defect is in the retirement entry.
Fix: `LEXICON.md`'s `Track` entry needs the carve-out its `Prompt` entry already
models. No edit owed in this file. Reported identically at
`reviews/collab-workflow-cycle-2.md` C9.
