# Review: context-sets/base.md — cycle 1

Verdict: changes-required
Reviewed: `context-sets/base.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11a)
Date: 2026-08-21
Scope: the whole file — frontmatter and all nine body sections — against all ten
criteria of `docs/global-context/review-rubric.md` @ `7310937`. Criterion 4 was
judged line-by-line against the current text of `docs/global-context/core.md`,
`docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`,
all @ `7310937`. Mechanical sweeps run (verified by running `grep`): retired
terms, vendor and model names, path-shaped references. `bin/bundle`,
`bin/bundle-methodology`, `bin/aimeta/frontmatter.py`, and
`decisions/log.md` `DEC-000140` were read to establish the blast radius of a
retirement or merge.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `operating-model.md`, `context-sets/testing-and-verification.md`,
`context-sets/spec-and-change-discipline.md`, `policies/document-metadata-policy.md`,
`bin/bundle`, `bin/bundle-methodology`, `bin/aimeta/frontmatter.py`,
`decisions/log.md`, `CLAUDE.md`
Not inspected: the other five context sets were read in full for duplication
against this file, but their own ten-criteria gates are their own artifacts and
are not re-argued here. `docs/packages/package-a-spec.md` §3.7 (the `bin/bundle`
contract) was not read; the closure behaviour cited in B14 comes from the
script's own docstring, not from the spec. No claim is made about whether the
evidence vocabulary is used correctly in `reviews/`, `retros/`, or `specs/` —
the sweep for consumers of the eight terms was not run.
Findings: 14 — 7 blocking, 4 non-blocking, 3 observations
Prior cycle: none
Dave should inspect: the criterion-10 call in B1. Two dispositions are
defensible and the choice is yours, not the reviewer's — see B1 `Fix`.

## Criterion 10 — disposition

**merge-into: `LEXICON.md`** (the evidence vocabulary) **and `operating-model.md`**
(the standard response shape), retiring the remainder.

The file lands in bundles today — it is the `depends-on` root of all five other
context sets and the first entry of the `bin/bundle-methodology` spine. But
criterion 10 asks what it *contributes* that no other file in that bundle
states, and on that test the file is roughly 85% restatement. Two sections
survive the test:

- **Evidence vocabulary** (L54–66) — eight terms stated nowhere in Core, the
  Decision Layer, `LEXICON.md`, or `operating-model.md`. See the disposition in
  B5.
- **Standard response shape** (L68–83) — the seven-part shape of an agent's
  *reply*. `operating-model.md` §Change package specifies the twelve-part
  contents of a change *package*, which is a different artifact. Not a
  duplicate.

Everything else in the file — core identity, the core rule, the required-behavior
list, the must-not list, the meaningful-change definition, the verification rule,
the mock rule, the tooling rule, and the closing uncertainty rule — is stated by
Core, the Decision Layer, or `operating-model.md`, or by
`context-sets/testing-and-verification.md`. Findings B2, B3, B4, B6, B7, B8, B9
enumerate them.

**Cost of the merge.** Retiring the file is not a document-only edit. It is
named in four places that would have to change in the same package: the
`SPINE` list at `bin/bundle-methodology:26`; `decisions/log.md` `DEC-000140`,
which fixes that spine by decision; the `depends-on: [base]` frontmatter of the
other five context sets; and `CLAUDE.md`, whose required-reading list names
`context-sets/base.md`. None of these is a reason to keep a file that fails
criterion 10, but all four are in the blast radius and none fails loudly if
missed — `bin/bundle-methodology` would raise on a missing spine entry, while a
dangling `depends-on` only degrades `bin/bundle`'s closure (B14).

The alternative disposition — **retain-with-changes**, cutting the restatement
and keeping the two surviving sections in place — costs none of that and is
recorded in B1 with its tradeoff.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — B8, B9, B13 |
| 2 | `audience:` is the selector | partial — B10 |
| 3 | No path references | fail — B8, B9, B14 |
| 4 | Core states it → remove it here | fail — B2, B3, B4, B6, B7 |
| 5 | Agent instruction, not authoring principle | fail — B13 |
| 6 | Instructions, not rationale | pass |
| 7 | Session kind is explicit | fail — B11 |
| 8 | Tiers, not model names | fail — B8 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |

## Counts (instruction 4)

- **Rules restated from Core / Decision Layer / LEXICON / operating-model:** 24
  distinct rules across 7 of the file's 9 body sections. By section: Core
  identity 3; Core rule 1; Required behavior 9 of 12 bullets; Agents must not 7
  of 7 bullets; Standard response shape 1 (the meaningful-change paragraph, not
  the shape itself); Verification rule 1; Tooling rule 1; When uncertain 1.
- **Path-shaped references:** 2 — `decisions/log.md` (L41), `/ai/` (L112).
- **Vendor and model names:** 4 in one sentence — Claude, Codex, ChatGPT, IDE
  (L113).
- **Retired terms:** 0. Clean.

## B1 — blocking
Claim: The file does not earn its place as written; roughly 85% of it restates
Core, the Decision Layer, or `operating-model.md`, and only two sections
contribute anything unique.
Location: `context-sets/base.md` (whole file)
Evidence: Verified by reading — every body section mapped line-by-line against
the four foundation files @ `7310937`; the mapping is enumerated in B2, B3, B4,
B6, B7, B8, B9 and summarised in the Counts block. Verified by running: `grep`
sweeps for retired terms, vendor names, and path-shaped references over all six
in-scope files.
Consequence: An agent receiving a bundle reads the same rule two or three times
in one sitting — the evidence rule in Core §Evidence and again as this file's
"Core rule", the scope rule in Core rule 3 and again at L32 and again at L48.
Repetition inside a single bundle is not reinforcement; it is a second place a
rule can drift, and Core rule 13 makes every duplicate a maintenance obligation.
Fix: Move the evidence vocabulary to `LEXICON.md` (B5) and the standard response
shape to `operating-model.md`; retire the rest. Alternative, if the migration
cost stated in the criterion-10 disposition above is not worth paying now: **retain-with-changes** —
delete L13–52, L68–74, L85–118, keep the evidence vocabulary and the seven-part
response shape, and the file becomes a ~30-line evidence-model document that
still anchors `depends-on`, the `bin/bundle-methodology` spine, and
`DEC-000140` unchanged. The tradeoff is that the vocabulary then sits in a
context set rather than in the term registry, which is the arrangement B5 argues
against.

## B2 — blocking
Claim: "Core rule" (L19–24) restates Core rule 5.
Location: `context-sets/base.md:19-24`
Evidence: Verified by reading. This file: "Agent claims require evidence. Output
is trusted to the degree explicit, inspectable evidence supports it — not
because it sounds plausible." Core rule 5 @ `7310937`: "**Claims require
evidence.** Output is trusted to the degree inspectable evidence supports it."
The second sentences differ by two words.
Consequence: The bundle states its own foundational rule twice, in two files,
with two slightly different wordings. A later edit to one produces a repo that
says two things about its most load-bearing rule, and Core rule 9 then obliges
every reader who notices to stop and surface the disagreement.
Fix: Delete L19–24.
Related: B3, B4

## B3 — blocking
Claim: Nine of the twelve "Required behavior" bullets restate rules already
stated by Core or `operating-model.md`.
Location: `context-sets/base.md:30-42`
Evidence: Verified by reading, bullet by bullet against the foundation @
`7310937`. L30 (know your role; ask if unspecified) → `operating-model.md:191`
escalation trigger. L32 (keep scope explicit) → Core rule 3. L33 (state
assumptions) → `operating-model.md:69`. L35 (distinguish evidence from
inference) → Core rule 6. L36 (distinguish mocked/contract/live/browser/
production) → `operating-model.md:70`. L37 (state what remains unverified) →
Core rule 7. L39 (update docs when behavior changes) → `operating-model.md:71`.
L40 (summaries Dave can inspect) → `operating-model.md:18`. L38 (identify what
Dave needs to decide) → Core rule 2 plus `operating-model.md` §Escalation.
Non-duplicates: L31 (preserve Dave's intent), L34 (prefer small reviewable
changes), L41–42 (consult the decision log).
Consequence: Twelve bullets present as twelve obligations; nine are already
binding on the agent from Core and `operating-model.md` in the same bundle. The
list reads as additive and is not, which inflates the apparent rule count and
buries the three bullets that are genuinely new here.
Fix: Delete L30, L32, L33, L35, L36, L37, L39, L40. Keep L31, L34, L38, L41–42.
L36 in particular is the rule whose *terms* B5 relocates — the rule stays in
`operating-model.md`, the terms go to `LEXICON.md`.
Related: B2, B4

## B4 — blocking
Claim: All seven "Agents must not" bullets restate `operating-model.md`
§Responsibilities "Must not" or Core.
Location: `context-sets/base.md:44-52`
Evidence: Verified by reading. L46 → `operating-model.md:76`. L49 →
`operating-model.md:79`. L50 → `operating-model.md:78`. L51 →
`operating-model.md:77`. L47 (hide uncertainty) → Core rule 7. L48 (silently
broaden scope) → Core rule 3, and duplicates this file's own L32. L52 (claim
verified when only assumed) → Core rule 7 second sentence.
Consequence: Same as B2, multiplied by seven. L48 additionally duplicates a
bullet twenty lines above it in the same file, which is the drift condition
Core rule 13 exists to catch, present inside a single document.
Fix: Delete L44–52 entire.
Related: B2, B3, B13

## B5 — blocking
Claim: The evidence-class vocabulary has no single home. This file states eight
terms; `context-sets/testing-and-verification.md` restates five of them at
greater length; `operating-model.md` requires agents to distinguish them but
defines none.
Location: `context-sets/base.md:54-66`
Evidence: Verified by reading. This file defines mock-verified,
contract-verified, live-verified, browser-verified, production-verified,
unverified, deferred verification, accepted risk.
`context-sets/testing-and-verification.md:33-145` defines the first five again,
each with useful-for and does-not-prove lists, and defines none of the last
three. `operating-model.md:70` states the obligation ("distinguish mocked,
contract, live, browser, and production verification") without the terms;
`grep` over `operating-model.md` @ `7310937` returns no definition of any of
the eight, confirming the cycle-6 O3 removal. `grep` over `LEXICON.md` @
`7310937` returns none of the eight.
Consequence: The obligation to use the classes is binding and the definitions
are optional cargo — an agent bundled with `operating-model.md` but not with a
context set is required to distinguish five classes it has never been given. And
where both context sets *are* bundled, five of the eight terms are defined
twice, which is B2's drift risk on the vocabulary the evidence model rests on.
Fix: **Single home: `LEXICON.md`, as a new `## Evidence classes` section
carrying all eight terms with the one-line definitions currently at
`context-sets/base.md:56-66`.** Then delete L54–66 here, and reduce
`context-sets/testing-and-verification.md:33-145` from definitions to the
useful-for / does-not-prove operational detail that is its own contribution.
`LEXICON.md` is the right home on three grounds: its stated charter is "Terms
with a fixed meaning across this methodology," which is precisely what these
are; its `audience: [all-roles, human]` and `order: 2` put it in every bundle
Core reaches, so no session gets the obligation without the terms; and it
already carries a section of exactly this kind (§Spec state) plus the
retired-terms discipline that keeps a vocabulary honest. The runner-up is Core
§Vocabulary, on the precedent that Core rule 6 defines the four claim classes
inline — rejected because rule 6 defines *claim provenance* as part of stating a
rule, whereas these eight are nouns used by other documents, and Core is
deliberately 54 lines.

## B6 — blocking
Claim: The meaningful-change paragraph (L70–73) restates
`operating-model.md:95-99` near-verbatim.
Location: `context-sets/base.md:70-73`
Evidence: Verified by reading. This file: "A **meaningful change** warrants a
change package — any change affecting behavior, interfaces, tests, dependencies,
boundaries, or documentation of substance." `operating-model.md:96-97`: "A
meaningful change is any change that warrants a change package — any change
affecting behavior, interfaces, tests, dependencies, boundaries, or
documentation of substance." Identical after the colon.
Consequence: The definition that decides whether a change package is owed exists
in two files. If either list of six categories is ever extended, the repo grades
the same change two ways.
Fix: Delete L70–73. The trivial-change carve-out in the same paragraph
("typo fixes, comment edits, mechanical formatting … use a lighter shape") is
*not* in `operating-model.md` and should move there, appended to
`operating-model.md:99`, when the response shape moves under B1.

## B7 — non-blocking
Claim: The mock rule and the verification rule are each stated twice in the
context-set layer.
Location: `context-sets/base.md:85-107`
Evidence: Verified by reading. Mock rule L100–107 ("A mock is a claim with a
deferred proof" plus a four-item checklist) restates
`context-sets/testing-and-verification.md:23-31` (same sentence as the §Core
principle, plus a five-item checklist covering the same ground). Verification
rule L85–98 is restated in compressed form at
`context-sets/testing-and-verification.md:202-205`, which then points back here
by path.
Consequence: A bundle containing both context sets — which is every bundle,
since `testing-and-verification.md` declares `depends-on: [base]` — states the
mock rule twice with checklists of different lengths. An agent cannot tell
whether four items or five is the requirement.
Fix: Delete L85–107. `context-sets/testing-and-verification.md` is the file
whose subject this is, and its five-item form is the superset.
Related: B14

## B8 — blocking
Claim: The tooling rule names four vendors and points at a directory that does
not exist in this repository.
Location: `context-sets/base.md:110-114`
Evidence: Verified by running. `grep -niE 'claude|codex|chatgpt|IDE'` returns
L113: "do not make Claude, Codex, ChatGPT, IDE settings, or local memory the
only home for durable project policy." `ls ai` at repo root @ `7310937` returns
"No such file or directory" — the portable context is the repository root, not
`/ai/`.
Consequence: Two defects in five lines. The vendor list is criterion 8: it dates
the document to a particular tool generation and will be wrong the first time
the toolchain changes, while the rule it carries — `operating-model.md:199-201`
and `:79` — is already stated vendor-neutrally. The `/ai/` reference is worse
than path-shaped, it is false: an agent instructed to put portable context in
`/ai/` would create a directory this repo does not use.
Fix: Delete L110–114. `operating-model.md:199-201` states the rule
("These portable operating documents are the source of truth … Tool-specific
files may adapt these rules but should not be the sole location of durable
policy") with no vendor names and no path.

## B9 — non-blocking
Claim: The decision-log bullet references another file by path.
Location: `context-sets/base.md:41-42`
Evidence: Verified by running — `ls decisions/log.md` resolves, so the path is
live, not dangling. Criterion 3 is failed by the reference existing, not by its
being broken.
Consequence: An agent reading this inside a generated bundle is told to consult
a file it was not given and cannot open, and to cite an entry ID from it. The
instruction is unexecutable in the medium the file is written for, which puts
the agent into Core rule 11.
Fix: This one is not a simple deletion — the obligation is real and the decision
log genuinely cannot be inlined. State it without the path: "consult the
decision log before recommending or encoding anything an existing decision may
govern, and cite the governing entry by ID; if the log was not supplied, say so
rather than proceeding." That keeps the rule and makes the missing-input case
explicit instead of silent.
Related: B14

## B10 — non-blocking
Claim: The file claims a position in the bundle but carries no `order:`.
Location: `context-sets/base.md:1-9`
Evidence: Verified by reading. Frontmatter carries `audience: [all-roles,
human]` — two reserved values, confirmed against
`bin/aimeta/frontmatter.py:16` — but no `order:`. The file's own
`include-when:` says "Always. Every other context set assumes it," and all five
other context sets declare `depends-on: [base]`, so its position is not
incidental. The four foundation files all carry `order:` (Core 0, Decision Layer
1, LEXICON 2, operating-model 3).
Consequence: A bundle compiler ordering by `order:` places the four foundation
files deterministically and then has nothing to sort the context sets by. The
root context set can be emitted after the files that assume it.
Fix: Add `order: 4` (or the next value after `operating-model.md`), and give the
remaining context sets successive values. If B1's merge is taken this finding
dissolves with the file.

## B11 — non-blocking
Claim: Session kind is never stated.
Location: `context-sets/base.md:1-11`
Evidence: Verified by reading. `audience: [all-roles, human]` names roles, not
session kinds, and no body sentence says which kind the file governs. Compare
`docs/global-context/core.md:10` ("every agent session"),
`docs/global-context/decision-layer.md:10` ("Rules for decision sessions …
Execution sessions never receive this file"), and `operating-model.md:10`
("governs both session kinds").
Consequence: The file mixes both. "Identify what Dave actually needs to decide"
(L38) and the "Dave decision points" element of the response shape (L83) are
decision-session material; the mock rule and the verification rule are execution
material. An execution session cannot tell which of the two it is expected to
satisfy.
Fix: Add the one-line declaration the three foundation files carry. On the
sections that survive B1, the honest answer is "both kinds."

## B12 — observation
Claim: `include-when:` is an instruction to whoever assembles context, not to
the agent reading the file.
Location: `context-sets/base.md:7`
Evidence: Verified by reading. "Always. Every other context set assumes it."
Compare criterion 5. `grep` over `bin/` @ `7310937` shows `bin/bundle` consumes
`depends-on:` and `bin/bundle-methodology` consumes `audience:`; neither reads
`include-when:`, `purpose:`, or `context-set:`.
Consequence: Three of the four context-set-specific frontmatter fields are read
by nothing and instruct nobody in the bundle. They are the residue of the
pre-bundle selection mechanism that `audience:` replaced.
Fix: Drop `include-when:`, `purpose:`, and `context-set:` from every context
set. Keep `depends-on:` only for as long as `bin/bundle` computes closure from
it — see B14.

## B13 — observation
Claim: L32 and L48 state the same rule twice within this file.
Location: `context-sets/base.md:32,48`
Evidence: Verified by reading. L32: "keep scope explicit; do not silently
broaden it." L48: "silently broaden scope."
Consequence: Minor on its own; notable because Core rule 13 and this file's own
successor rule in `context-sets/spec-and-change-discipline.md:185-187`
("Document consistency") both make intra-document duplication the named defect.
Fix: Subsumed by B3 and B4, both of which delete one of the two.
Related: B4

## B14 — observation
Claim: Criterion 3 and `bin/bundle` are in direct tension: the tool treats
backticked repo-relative `*.md` paths in a document body as graph edges, and
criterion 3 calls those same strings defects.
Location: `context-sets/base.md:41` and, more broadly, all six in-scope files
Evidence: Verified by reading `bin/bundle` @ `7310937`, docstring lines 5–9:
"Edges are (a) `depends-on:` frontmatter entries resolved to
`context-sets/<name>.md` and (b) backticked repo-relative `*.md` paths in the
body that exist as files." Verified by running: the `grep` sweep across the six
files returns 26 path-shaped references, of which the in-body backticked `.md`
paths are live `bin/bundle` edges.
Consequence: Executing criterion 3 across the context sets silently degrades
`bin/bundle`'s closure to `depends-on` edges only. Nothing fails loudly — the
tool keeps running and returns a smaller set — so a bundle that used to reach
`policies/commit-and-change-control-policy.md` through
`context-sets/spec-and-change-discipline.md` simply stops reaching it, and the
first symptom is an agent missing a policy it was previously given.
Consequence for this file specifically: 2 of its edges (B8, B9) disappear, one
of which was already false.
Fix: Out of scope for a per-document edit list, and named here so the executor
does not discover it mid-sweep. Before criterion 3 is executed across
`context-sets/`, decide whether edge (b) survives: either `depends-on:` is
made complete enough to carry the closure alone, or `bin/bundle` gains an
explicit edge declaration that is not prose. This is a tooling decision, not a
document one.
Related: B9, B12
