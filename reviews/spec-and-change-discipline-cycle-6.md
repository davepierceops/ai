# Review: context-sets/spec-and-change-discipline.md — cycle 6

Verdict: changes-required
Reviewed: `context-sets/spec-and-change-discipline.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11a)
Date: 2026-08-21
Scope: the whole file — frontmatter and all six body sections — against all ten
criteria of `docs/global-context/review-rubric.md` @ `7310937`. Cycles 1–5 were
narrow self-reviews of single edits (cycle 5 was a confirmation pass over the
concurrency paragraph); this is the file's first full ten-criteria gate.
Criterion 4 judged line-by-line against `docs/global-context/core.md`,
`docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`
@ `7310937`, and additionally against `context-sets/collab-workflow.md`, which
duplicates one of this file's paragraphs near-verbatim. The two numbered
sequences in this file and in `operating-model.md` were aligned stage by stage
to check the cross-reference at L86–87. Mechanical sweeps run (verified by
running `grep`): retired terms, vendor and model names, path-shaped references.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `operating-model.md`, `context-sets/collab-workflow.md`,
`context-sets/base.md`, `bin/bundle`, `bin/bundle-methodology`,
`bin/aimeta/frontmatter.py`, `decisions/log.md` `DEC-000140`
Not inspected: `policies/commit-and-change-control-policy.md`,
`policies/source-of-truth-policy.md`, `roles/spec-reviewer-agent.md`,
`boundaries/human-review-boundary.md`, and `skills/spec-review-cycle.md`
§Reconciliation — all five are cited by this file and none was read. S9 counts
those citations as path-shaped references and confirms by `ls` that each
resolves; it makes no claim about whether the cited documents say what this file
says they say. The P3 contact-merge review of 2026-07-24, cited twice as
provenance (L80–83, L196–201), was not located or read; S8 treats those
parentheticals as rationale on their face without auditing the history they
assert. `OPEN-ITEMS.md` contents not inspected.
Findings: 12 — 5 blocking, 4 non-blocking, 3 observations
Prior cycle: `reviews/spec-and-change-discipline-cycle-5.md`
Dave should inspect: S5 — the `OPEN-ITEMS.md` register contradicts Decision
Layer rule 9 ("State is computed, never maintained"), and which one gives is
your call, not a drafting fix. Also S1's second half: the cross-reference at
L86–87 points at the wrong step range and silently drops quality review from the
flow, which is the kind of error that only shows up when someone follows it.

## Criterion 10 — disposition

**retain-with-changes.**

The file earns its place on three sections that nothing else in the bundle
states:

- **The behavioral red-gate** (L69–83). "A test that fails only because the
  module under test doesn't exist yet … proves nothing about whether the test's
  assertions are correct — a wrong assertion fails the same way as a right one."
  `operating-model.md:112` states that the red-gate is mandatory; only this file
  states what makes a red-gate real. Without it, Test Designer / Coder
  separation is satisfiable by a missing import, which is the failure mode the
  paragraph exists to close.
- **The open-delta operating rules** (L115–138), as distinct from the open-delta
  *definitions* (S6). Four rules appear here and nowhere else: reconciliation
  blocks the next tranche's decomposition; at most two tranches execute
  concurrently and never two deltas over one tranche; the convergent-edit case
  is refused rather than tooled; and a directive issued mid-delta cites the spec
  branch and pins its SHA rather than the default branch.
- **The derived/side-effect fields checklist** (L188–201). A concrete
  write-path obligation — enumerate an entity's derived fields and confirm this
  change's write path maintains them the way every other write path does —
  stated nowhere else in the corpus.

Everything else is restatement or rationale, and the finding list below is the
edit list. The file is roughly 201 lines and the edits remove or relocate about
half of it, leaving a document organised around the three sections above plus
the canonical sequence's genuinely additive material.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — S9 |
| 2 | `audience:` is the selector | partial — S11 |
| 3 | No path references | fail — S9 |
| 4 | Core states it → remove it here | fail — S1, S2, S4, S6 |
| 5 | Agent instruction, not authoring principle | fail — S8 |
| 6 | Instructions, not rationale | fail — S7 |
| 7 | Session kind is explicit | fail — S10 |
| 8 | Tiers, not model names | fail — S3 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — `spec/<tranche-slug>` is a branch name, not a filename, and `OPEN-ITEMS.md` is convention-named |

## Counts (instruction 4)

- **Rules restated from Core / Decision Layer / LEXICON / operating-model:** 19
  across 5 of the 6 body sections. By section: Core philosophy 2
  (`operating-model.md:20` spec-first/test-driven, `:110` the two-tier gate);
  The canonical sequence 6 (`operating-model.md:101-106`, stage for stage);
  Open spec delta 5 (`LEXICON.md` §Tranche, §Spec branch, §Open spec delta,
  §Reconciliation, §Claimed); Definition of done 1 (`operating-model.md:162-178`,
  as a lossy subset); Operating habits 5 (Decision Layer 1, 6, 9;
  Core rule 2, rule 13). One further paragraph — Operating habits' first bullet
  at L160–165 — is duplicated from `context-sets/collab-workflow.md:36-42`
  rather than from the foundation.
- **Path-shaped references:** 13 — the highest of the six files in scope.
  `base.md` (L14), `ai-native-engineering.md` (L15),
  `policies/commit-and-change-control-policy.md` (L42, L147),
  `specs/` (L51), `policies/source-of-truth-policy.md` (L54),
  `operating-model.md` (L87), `roles/spec-reviewer-agent.md` (L106),
  `context-sets/collab-workflow.md` (L106), `skills/spec-review-cycle.md` (L111),
  `skills/directive-dispatch.md` (L126), `LEXICON.md` (L132),
  `boundaries/human-review-boundary.md` (L165), `OPEN-ITEMS.md` (L174, L183).
- **Vendor and model names:** 1 — "GitHub Issue" (L57). Borderline: `LEXICON.md`
  and `operating-model.md:36` both name the tracker vendor
  ("currently GitHub Issues"), and `operating-model.md` hedges it with
  "currently" where this file does not.
- **Retired terms:** 4 uses — "dispatch" (L26), "dispatches" (L123),
  `directive-dispatch.md` inside the path at L126, "track" (L131, twice in one
  sentence, while forbidding the word).

## S1 — blocking
Claim: The canonical sequence restates `operating-model.md` §Change flow stage
for stage, renumbers it, and then hands off with a step range that omits quality
review entirely.
Location: `context-sets/spec-and-change-discipline.md:45-87`
Evidence: Verified by reading, both @ `7310937`, aligned stage by stage. This
file's 1 (PRD/TRD current and agreed at rest) = `operating-model.md`'s 1 (Specs
agreed). 2 (Acceptance criteria written) = its 2. 3 (Architecture summary) = its
3. This file then splits `operating-model.md`'s step 4 ("Test plan, confirmed
red") into two — 4 (Tests written as code) and 5 (Confirm all tests fail) — so
this file's 6 (TDD to green) is `operating-model.md`'s 5 (Implement to green).
`operating-model.md`'s own step 6 is Quality review. This file's L86–87 then
reads: "The full change flow continues through quality review, skeptic/risk
review, release package, and release gate. See `operating-model.md` for steps
7–9." Four stages are named; `operating-model.md`'s steps 7–9 are skeptic/risk
review, release package, and release gate — three stages. Quality review is
`operating-model.md`'s step 6 and is outside the range.
Consequence: Two defects, and the second is the live one. The duplication means
six stages are specified twice under two numbering schemes, so "step 4" means
"test plan, confirmed red" in one file and "tests written as code" in the other
— any directive or review artifact citing a step number is ambiguous across the
corpus. The cross-reference error means an agent that follows L87 literally,
reading `operating-model.md` steps 7–9, is handed a flow with no quality review
in it: it goes from green tests straight to skeptic/risk. `operating-model.md:107`
is a hard gate.
Fix: Two edits, and both are needed. (a) Delete this file's steps 1–4 and 6,
which restate `operating-model.md:101-106` and add nothing; keep step 5
(confirm all tests fail) only if the split from `operating-model.md`'s step 4 is
deliberate, and if it is, make the same split there so one numbering governs.
(b) Whatever survives, replace L86–87's numeric range with the stage names it
already lists — numbers that mean different things in two documents should not
be the pointer. Under criterion 3 the pointer goes away entirely (S9), which
resolves (b) by removal.
Related: S2, S9

## S2 — blocking
Claim: "Definition of done (spec discipline view)" is a lossy copy of
`operating-model.md` §Definition of done, and drops a condition this file's own
step 6 requires.
Location: `context-sets/spec-and-change-discipline.md:140-148`
Evidence: Verified by reading, both @ `7310937`. `operating-model.md:166-178`
lists eleven conditions. This file lists seven, in the same order, in the same
words. The four omitted: "mechanical checks (lint, types, static analysis)
pass"; "relevant verification has run"; "release readiness is clear"; "Dave has
enough information to assess risk". The first omission contradicts this file's
own L62–65, which requires "mechanical checks (lint, types, static analysis)
passing as part of 'green.'"
Consequence: A section headed "Definition of done" that is a strict subset of
the canonical definition, with no statement that it is a subset beyond the
parenthetical "(spec discipline view)". An agent reading this file — and this
file is in the `bin/bundle-methodology` spine, so it is in the decision-layer
bundle — has a seven-condition definition of done that omits mechanical checks,
which the same file made part of green forty lines earlier. The document
disagrees with itself, and the shorter list is the one under the heading a
reader looks for.
Fix: Delete L140–148. `operating-model.md:162-178` is the definition and is
complete. If a scoped view is genuinely wanted, it cannot be a subset presented
as a definition — it would have to be a pointer, which criterion 3 forbids, so
deletion is the only clean option.
Related: S1

## S3 — blocking
Claim: Retired terms are in live use — "dispatch" twice and "track" twice, the
latter in a sentence whose subject is that "track" is not a term of this
methodology.
Location: `context-sets/spec-and-change-discipline.md:26,123,126,131-132`
Evidence: Verified by running. `grep -niE '\b(dispatch(ed|es|ing)?|tracks?)\b'`
returns L26 ("the spec is true **at dispatch** and true **at rest**"), L123
("**Mid-delta dispatches derive from the spec branch.**"), L126 (the path
`skills/directive-dispatch.md`), and L131–132 ("The word for a concurrent
workstream is *tranche*, not *track*: `track` is not a term of this methodology
at all"). `LEXICON.md:63-64` @ `7310937` retires "dispatch" — "Write 'hand the
directive to an execution session,' or 'direct'" — and `:69-70` retires "track".
Consequence: The retirement landed one commit before the reviewed tree, and
`LEXICON.md`'s touch rule (L14–15) makes conforming this file mandatory at its
next edit; this review is that occasion. L26 is the costly one: "true at
dispatch" is the sentence that defines when the spec must be true, so the
retired word is load-bearing in the file's central rule. L131–132 is the
awkward one: it uses the retired term twice in order to say the term is retired,
which is a job `LEXICON.md` now does (S12).
Fix: L26 → "the spec is true **at handoff** and true **at rest**", matching L22
("at the moment work is handed to an executor"), which already uses the right
word four lines above. L123 → "**A directive issued mid-delta derives from the
spec branch.**" L131–132 → delete the parenthetical entirely (S12). L126's path
goes under S9.
Related: S12

## S4 — blocking
Claim: Five of the seven Operating habits restate Decision Layer or Core rules,
and one of the five is additionally duplicated verbatim in
`context-sets/collab-workflow.md`.
Location: `context-sets/spec-and-change-discipline.md:150-187`
Evidence: Verified by reading, all @ `7310937`. L166–168 ("**One question at a
time.** When something needs Dave's input, ask a single question and wait,
rather than batching several decisions into one message") → Decision Layer rule
1 ("**One question at a time.** Ask the one that matters most, wait, then the
next"). L169–171 ("**No assumptions on consequential calls.** When a decision is
Dave's, frame the tradeoffs clearly and ask") → Decision Layer rule 6 ("**Ask
the judgment calls.** When a decision is his, state the options and tradeoffs
and ask") and Core rule 2. L170–172 ("**Frame tradeoffs crisply.** Present clear
options with their tradeoffs") → Decision Layer rule 6 again — so the file
states the same rule twice, in adjacent bullets. L185–187 ("**Document
consistency.** When editing a document, find *every* instance of a changed value
across the whole document and update all of them") → Core rule 13 ("**A changed
fact changes everywhere it appears.**"), which is broader — Core requires it
across *every other document* too, where this bullet stops at "the whole
document". L160–165 ("**Agents dispose of routine changes**") →
`operating-model.md:119-131` two-tier gate plus Core rule 2, and is duplicated
near-verbatim at `context-sets/collab-workflow.md:36-42`.
Consequence: Two harms. The routine one is bundle-budget duplication. The
specific one is L185–187: it is a *narrower* restatement of Core rule 13 under a
heading a reader will treat as the rule, so an agent that follows it updates one
document and leaves the same stale value in five others — which is precisely the
failure Core rule 13 was written to prevent, and precisely the failure C7 of
this cycle found in `context-sets/collab-workflow.md:53` over the repository
rename.
Fix: Delete L160–165, L166–168, L169–171, L170–172, L185–187. Keep L152–159
(subject to S8) and L173–184 (subject to S5) and L188–201.
Related: S5, S8

## S5 — blocking
Claim: The `OPEN-ITEMS.md` bullet mandates a maintained register, which Decision
Layer rule 9 prohibits.
Location: `context-sets/spec-and-change-discipline.md:173-184`
Evidence: Verified by reading. This file mandates tracking open items, deferred
decisions, and outstanding fixes in `OPEN-ITEMS.md`, updated at four named
checkpoints — end of work session, before a release gate, before a spec is
agreed, on demand. Decision Layer rule 9 @ `7310937`: "**State is computed,
never maintained.** Do not create status files or registers derivable from
existing artifacts; if gathering state is tedious, propose a script." Verified
by running: `ls OPEN-ITEMS.md` resolves; the file exists and is 760+ lines. The
same obligation is stated again at `context-sets/collab-workflow.md:46-47`.
Consequence: An agent given the Decision Layer and this file is instructed both
to maintain a register and not to maintain registers. Core rule 9 forbids
resolving it by picking one, so the correct behaviour is to surface it — on
every session that reads both, which is every decision session, since this file
is in the `bin/bundle-methodology` spine alongside the material rule 9 governs.
The conflict is currently invisible because the two documents are rarely read
against each other; Pass 1 is what makes them get read against each other.
Fix: Not a drafting fix — Dave's call. Either open items are not derivable from
existing artifacts, in which case Decision Layer rule 9 needs a stated carve-out
naming `OPEN-ITEMS.md`; or they are, in which case rule 9's "propose a script"
applies and the register goes. Whichever way, the statement belongs in exactly
one file, and this one — with its four checkpoints — is the fuller of the two
copies, so `context-sets/collab-workflow.md:46-47` is the one deleted.
Related: S4

## S6 — non-blocking
Claim: The Open spec delta section restates five `LEXICON.md` entries before
stating the four rules that are its actual contribution.
Location: `context-sets/spec-and-change-discipline.md:89-138`
Evidence: Verified by reading, both @ `7310937`. `LEXICON.md` §Spec state
defines Tranche, Spec branch, Open spec delta, Reconciliation, and Claimed. This
file restates all five: L96–100 (spec branch, `spec/<tranche-slug>`, "the branch
existing, with commits on it, is the whole of the machinery" —
`LEXICON.md:21-27` says "The branch existing, with commits on it, is the
state"); L97–99 (open spec delta); L108–113 (reconciliation, including the
"once per delta, not once per edit" formulation `LEXICON.md:33` also carries);
L132–134 (claimed, including the second-delta prohibition).
Consequence: `LEXICON.md` carries `order: 2` and `audience: [all-roles, human]`,
so it precedes this file in every bundle. Five terms are defined, then redefined
fifty lines later in different words. `LEXICON.md`'s reconciliation entry adds
"Agreement attaches here, to the version of record," which this file does not
carry; this file's L110–113 adds "the default branch therefore never carries
unreviewed spec text, and `agreed` there never lies," which `LEXICON.md` does
not. Neither is complete and both present as the definition.
Fix: Delete the definitional sentences — L96–100, L108–113's first clause,
L132–134's first clause — and keep the four operating rules named in the
criterion-10 disposition. Move `LEXICON.md`'s missing clauses into `LEXICON.md`
in the same edit, per Core rule 13.

## S7 — non-blocking
Claim: Five passages are argument for rules rather than statements of them.
Location: `context-sets/spec-and-change-discipline.md:26-33,80-83,91-94,116-121,196-201`
Evidence: Verified by reading. L26–33: "That the spec must also have been
pre-approved does not follow — it is a different property, and the two were
conflated for no gain and at the cost of an operator gate per edit." L80–83: the
parenthetical provenance, "(Confirmed by Dave, 2026-07-24, closing the P3
contact-merge review: a real gap — region going stale during merge — survived
both implementation and a same-branch independent test pass …)". L91–94: "A
tranche does not survive contact with implementation unchanged. Decisions get
made while building, by the person with the hot context … which is the wrong
rate." L116–121: why reconciliation blocks decomposition. L196–201: the second
P3 provenance parenthetical.
Consequence: Criterion 6. Roughly 25 of 201 lines. The provenance parentheticals
(L80–83, L196–201) are the two worth arguing about: they record why a rule
exists, which has real value, but they record it inside the instruction an agent
must follow, where it competes for attention with the rule and cannot be
maintained independently of it.
Fix: Delete L26–33's final sentence, L91–94, and L116–121. For the two
provenance parentheticals, the rule survives and the history moves: `retros/` or
`decisions/log.md` is where "confirmed by Dave, 2026-07-24, closing the P3
contact-merge review" belongs, and the rule then stands on its own. Note that
L69–79 — the behavioral red-gate argument proper — is *not* in this list: it
states what makes a red-gate real, which is the rule itself, not a justification
for it.

## S8 — non-blocking
Claim: The first operating habit is a design test for whoever proposes
mechanisms, not an instruction to the agent reading it.
Location: `context-sets/spec-and-change-discipline.md:152-159`
Evidence: Verified by reading. "**Ask what a mechanism costs Dave in the loop.**
Operator attention is this system's scarcest resource … So every proposed gate,
check, confirmation, or ceremony is measured by how much of it it spends … This
is a design test applied to mechanisms, not a licence to skip a gate that passes
it." The bullet says of itself that it is a design test. Nothing in it directs
the agent's work on the change in front of it.
Consequence: Criterion 5, and criterion 6 for the second half. It is eight lines
of the methodology's own design rationale sitting in a context set that ships to
execution sessions, none of which propose mechanisms.
Fix: The principle is good and is genuinely used — it is the reasoning behind
the open spec delta and behind the two-tier gate. It belongs in the
instruction-writing criteria, per criterion 5, or in `docs/global-context/` with
the rubric. Delete from here.
Related: S4

## S9 — non-blocking
Claim: Thirteen path-shaped references, the most of any file in this cycle's
scope, and two of them are the sole statement of a rule.
Location: `context-sets/spec-and-change-discipline.md` — 13 sites, enumerated in
the Counts block
Evidence: Verified by running — `grep` for backticked repo-relative paths
returns 13 sites across 14 lines; `ls` confirms each resolves, so all are live
`bin/bundle` edges rather than dangling references.
Consequence: Criterion 1 and 3. Two are load-bearing rather than merely
decorative: L42–43 ("see `policies/commit-and-change-control-policy.md` for the
two tiers and what membership in the consequential class means") is the only
statement in this file of what makes a change consequential, and L86–87 is the
continuation of the change flow — the one S1 shows is also numerically wrong. An
agent given this file without those two documents has a spec-first sequence that
terminates at green and a two-tier gate whose tiers it cannot classify into.
Fix: Inline what the agent actually needs. For L42–43: `operating-model.md:126-131`
already enumerates the consequential class in one sentence, so this file can
drop the pointer entirely rather than restate it. For L86–87: see S1(b). The
remaining eleven go with the deletions in S1, S2, S4, S6, S7, S8, or become
prose without the backticked path. Note the tooling tension recorded at
`reviews/base-cycle-1.md` B14 — this file is the largest single contributor of
in-body `bin/bundle` edges, so it is where removing them changes closure most.
Related: S1

## S10 — observation
Claim: Session kind is never stated, and the file governs both.
Location: `context-sets/spec-and-change-discipline.md:1-16`
Evidence: Verified by reading. `audience: [all-roles, human]`; no declaration.
The canonical sequence, the red-gate, and the derived-fields checklist are
execution-session material. The operating habits — one question at a time, frame
tradeoffs crisply, no assumptions on consequential calls, ask what a mechanism
costs Dave — are decision-session material, and four of them duplicate the
Decision Layer, which states "Execution sessions never receive this file"
(`docs/global-context/decision-layer.md:10`).
Consequence: Criterion 7. The file smuggles decision-layer material into
execution bundles under `audience: [all-roles]`. S4's deletions remove most of
it, at which point the honest declaration is "execution sessions" for
everything except L152–159, which S8 removes.
Fix: After S4 and S8 land, add one line after the H1: "Rules for execution
sessions." If any decision-session habit is kept, the declaration has to be
"both kinds" and the audience question reopens.
Related: S4, S8

## S11 — observation
Claim: No `order:`, and three frontmatter fields that nothing reads.
Location: `context-sets/spec-and-change-discipline.md:1-9`
Evidence: Verified by reading and running. `audience: [all-roles, human]` — both
reserved, valid per `bin/aimeta/frontmatter.py:16`. No `order:`. `context-set:`,
`purpose:`, and `include-when:` are consumed by neither `bin/bundle` nor
`bin/bundle-methodology`.
Consequence: This file is second in the `bin/bundle-methodology` `SPINE`
(`bin/bundle-methodology:27`), so its position in that bundle is fixed by code
rather than by metadata. For any other bundle, nothing orders it after `base`,
which it declares `depends-on:` and whose evidence vocabulary it assumes.
Fix: Add `order:` after `context-sets/base.md`'s value. Drop `context-set:`,
`purpose:`, and `include-when:`.

## S12 — observation
Claim: The parenthetical forbidding "track" restates `LEXICON.md`, is rationale,
and uses the retired term twice to do it.
Location: `context-sets/spec-and-change-discipline.md:130-132`
Evidence: Verified by reading. "(The word for a concurrent workstream is
*tranche*, not *track*: `track` is not a term of this methodology at all,
`LEXICON.md`.)" `LEXICON.md:69-70` @ `7310937` now states the retirement
directly. Cycle 5's artifact records that this parenthetical was added to
prevent a tranche/track collision in a proposed `DEC-000170` — so it predates
the `LEXICON.md` entry that now does the job.
Consequence: Three criteria in one sentence: 4 (restates `LEXICON.md`), 6
(argues rather than instructs), and 8 (uses the retired word). It is also
self-undermining in a way a reader will notice — the sentence that says the word
is not a term of this methodology is the file's only use of it.
Fix: Delete L130–132. `LEXICON.md`'s retired-terms section carries this now, and
carries it for the whole corpus rather than for one paragraph.
Related: S3
