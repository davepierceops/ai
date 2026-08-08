# External Methodology Scan — Phase 2 Findings (Diff and Grade)

Executes `docs/research/methodology-scan-phase2-diff.md` against
`docs/research/methodology-scan-catalog.md` (35 entries) and
`docs/research/methodology-scan-catalog-gap.md` (15 entries) — 50 practices —
with the `davepierceops/ai` methodology corpus loaded.

**These are cycle inputs, not decisions.** No methodology document was edited.
Adoption is Dave's and enters through the normal review cycle.

**Run complete.** All 50 catalogued practices classified and graded. Sections
below are ordered per the directive: contradictions lead, then gaps, then
convergences, then no-action; within each section, by adoption-worthiness.
Grading was performed in eight batches by tradition, checkpointed after each;
this file is the reordered final state.

## How to read a finding

Each entry carries the directive's schema plus a one-line reason per rubric axis.

- **Bucket** — gap / contradiction / convergence / no-action.
- **Methodology position** — cited by path and section, with the decision-log ID
  where one governs. "None" is stated explicitly, never implied.
- **Coverage** — equivalent / adjacent (partial gap) / none / n/a. *Adjacent is
  not "already covered"* and is never collapsed into it.
- **Scores** — relevance · mechanism · source · cost, each low/medium/high.
  Score is independent of bucket: a contradiction can score high, and a
  high-scoring contradiction is a priority finding. **Cost is information for
  sequencing, not a penalty** — `h` on cost does not lower a finding's rank.
- **Case** — for a gap, what it would add; for a contradiction, the external
  practice at its strongest and the choice it opposes; for a convergence, the
  shared mechanism and the independent position it confirms.
- **Cycle input** — the specific proposed change, phrased as an input to a
  spec-review cycle. Several findings deliberately propose *nothing*, or propose
  being folded into another finding rather than raised separately.

---

# Contradictions (3)

A serious external practice does the opposite of a deliberate methodology choice. Not adopted here; surfaced with the external case stated at its strongest so re-litigation runs against a real argument. Ordered by adoption-worthiness; these lead the document per the directive.

## SAFETY-04 — Outcome-based compliance independent of lifecycle model
Bucket: contradiction
Methodology position: `operating-model.md` §Change flow ("Each stage completes before the next begins; no skipping or working ahead"); `context-sets/spec-and-change-discipline.md` §The canonical sequence; `policies/testing-policy.md` §Red-gate ("This rule applies to all tiers of change"); `policies/commit-and-change-control-policy.md` §Red-gate and §Test/Coder separation (both "applies to both tiers"); `context-sets/ai-native-engineering.md` §Team model ("two separations are mandatory rather than optional")
Coverage: n/a
Scores: relevance h · mechanism h · source m · cost h
Score reasons:
- relevance — the methodology mandates a lifecycle and has had to carve exceptions out of it repeatedly; that is the failure mode this practice addresses.
- mechanism — specify required tasks and evidentiary outcomes, leave the sequence to the team; concrete and directly contrastable with what is written today.
- source — vendor blog summarizing a standard's structure, though the methodology-agnostic framing is a checkable claim about how IEC 62304 is written (catalog: mixed).
- cost — high and structural: it would rewrite the change flow's status from mandate to default.
Case: **The external practice opposes the methodology's core structural choice,
and its strongest case is made from this repo's own history.** IEC 62304
deliberately does not mandate waterfall, V-model, agile, or iterative — it
requires that specific tasks be performed and specific evidence be maintained,
and is silent on the order. This methodology does the opposite: it mandates the
order (nine stages, no skipping, no working ahead), mandates the red-gate for all
tiers, and mandates Test/Coder separation — while stating an outcome-based thesis
at the top ("Manage the proof, not the code"; "the system must produce enough
specification, verification, review, and operational evidence to support
responsible release decisions"). Those two commitments are not the same
commitment, and the tension has been paid for in decisions: `decisions/log.md`
DEC-000010 through DEC-000060 are, in sequence, six rulings that carve routes
around the mandated process — a doc-only cycle, its narrowing, its re-narrowing,
a restored carve-out, and finally an owner override for a single additive line.
Each was necessary because the mandate specifies *method*, so any case the
method did not anticipate needs an exception rather than a re-derivation. An
outcome-specified regime would have admitted each of those cases by asking the
one question that actually matters — was the required evidence produced by
someone who did not produce the artifact — and would not have needed a ruling.
The counter-case is equally real and is why this is Dave's to re-litigate: the
mandated sequence is what makes the red-gate unskippable, and "produce
equivalent evidence some other way" is exactly the reasoning an agent uses to
skip it. A mandate is legible to an LLM in a way an outcome is not.
Cycle input: Propose re-litigating the mandate-versus-outcome question explicitly, scoped to one concrete test: could the change flow be restated as *required outcomes plus required independence*, with the nine-stage sequence demoted to the default realization of those outcomes? If yes, the expedited path and the doc-only cycle stop being exceptions and become instances. If no, record the reason in `decisions/log.md`, because it is currently unwritten and six decisions have been spent implying it.

## LLM-06 — Primacy/recency placement of critical instructions
Bucket: contradiction
Methodology position: `policies/source-of-truth-policy.md` §Canonical order and §Keeping derived artifacts honest; `MANIFEST.md` §What is no longer here ("a second copy of a derivable fact drifts and then lies"); `policies/document-metadata-policy.md` §Excluded fields ("derivable metadata is a second source of truth. It will drift, and a wrong metadata line is worse than an absent one"); `boundaries/vendor-tooling-boundary.md` §Required discipline ("Do not add new durable policy only in the adapter")
Coverage: n/a
Scores: relevance h · mechanism m · source m · cost l
Score reasons:
- relevance — every governed document in this repo is loaded into a context window, so placement effects apply to the entire corpus by construction.
- mechanism — a placement heuristic (start and end, never the middle); the sharper "repeat critical instructions at both ends" framing is the cataloguer's own inference, flagged as such.
- source — a vendor blog summarizing an underlying empirical study rather than the study itself (catalog: mixed).
- cost — very low, if it is confined to generated bundles rather than source documents.
Case: **The external practice opposes the methodology's most deeply-held
structural rule.** This repo has spent real effort eliminating second copies —
it emptied `MANIFEST.md` on that principle, excluded four metadata fields on it,
and treats a duplicated fact as a defect that will eventually lie. LLM-06 says
that for an LLM reader, a single canonical copy buried mid-context is *worse
than* a deliberate duplicate at the edges, because recall degrades sharply in
the middle. Both cannot be followed as stated. The strongest case for the
external practice is that the methodology has already half-conceded it and knows
it: `docs/global-retro-inbox.md` 2026-08-07 defines a bin for "**load-bearing
repetition** — restated on purpose so a rule stays salient when an agent reaches
the moment from different entry points; keep, possibly mark as intentional so it
is not later 'helpfully' de-duped," and adds "LLM adherence can genuinely
benefit from repetition — do not reflexively DRY." That is LLM-06's claim,
written by this project, without a rule to act on. The resolution the diff
suggests is that the two rules govern *different artifacts*: source documents
keep one canonical home (drift is a maintenance property), while **assembled
bundles** are generated, never hand-edited, and therefore cannot drift — so
duplication for salience is free there. `bin/bundle` already exists, and
`docs/global-retro-inbox.md` already proposes it emit a complete pinned bundle.
Cycle input: Propose that the queued drift-audit tranche decide the placement question alongside the duplication question, since one rule must serve both — recommended shape: one canonical home in source documents, salience duplication permitted only in generated bundles, with critical rules placed at the head and repeated at the tail of the assembled artifact. Triage together with DBC-04, which pulls in the opposite direction from the same principle.

## DESIGNDOC-02 — RFC-explores, ADR-records division of labor
Bucket: contradiction
Methodology position: `skills/spec-review-cycle.md` §Hard constraints ("One conversation per cycle ... Carry forward only reviewer findings and prior cycle directives ... Never carry forward chat history"); `LEXICON.md` §Prompt ("a prompt is regenerable and disposable"); `roles/chief-of-staff.md` (prompts gitignored, never committed); `policies/decision-log-policy.md` §Entry format (the record is the ruling plus its context, not the exploration)
Coverage: n/a
Scores: relevance h · mechanism h · source m · cost m
Score reasons:
- relevance — options considered and discarded are the expensive part of a decision, and this methodology deliberately does not keep them.
- mechanism — two artifacts at two phases, the first commentable and open before the decision, the second closed and terminal after it.
- source — an individual practitioner's synthesis rather than an organizational standard (catalog: mixed), though the phase-separation mechanism is concrete.
- cost — moderate: a new committed artifact class and a rule for when one is required.
Case: **The external practice opposes a deliberate choice.** This methodology
holds that chat is the decision layer and only the *decision* becomes durable:
directives are committed, prompts are explicitly disposable, cycle chats are
one-shot with history never carried forward. There is no artifact anywhere in
the corpus whose purpose is to hold an option under consideration. The RFC
tradition says that is the artifact that matters most, because the reasoning
that eliminated the alternatives is what stops them being re-proposed. The
strongest case is that the methodology has already conceded the point twice
under pressure and paid for it both times: `MANIFEST.md` keeps a frozen
tombstone explicitly "because they explain decisions whose reasoning is not
otherwise recoverable, and deleting them would lose that," and
`policies/decision-log-policy.md` created the Context field for the stated
purpose that "a reader can consult the decision without reopening the cycle chat
it came from" — both are RFC-shaped needs met by retrofitting a record-shaped
artifact. The counter-case is real and is why this is Dave's call: a durable
exploration artifact is a second place a not-yet-true statement lives, and the
one-conversation rule exists to stop stale context contaminating a fresh
session — which is the same hazard, viewed from the other side.
Cycle input: Propose re-litigating whether exploration deserves a committed artifact, scoped narrowly: not a full RFC process, but whether the decision-log entry should carry the alternatives and the reasoning that eliminated them (which is DESIGNDOC-06's proposal, and would resolve this contradiction at the cheapest point rather than by adding a document class).

---

# Gaps (31)

The methodology holds no position on the problem, or holds an adjacent position that is not equivalent (a partial gap, not "already covered"). Ordered by adoption-worthiness, high first.

## LLM-04 — Structural separation of instructions from untrusted content
Bucket: gap
Methodology position: none. The corpus contains no security position on ingested content — no mention of prompt injection, untrusted input, or channel separation anywhere in the governed set.
Coverage: none
Scores: relevance h · mechanism h · source h · cost l
Score reasons:
- relevance — high and concrete: agents in this workflow routinely ingest content nobody in the loop wrote, and the corpus has no rule for it.
- mechanism — system instructions, developer intent, and untrusted content occupy distinct labeled channels; spotlighting via delimiters or tags marks the untrusted portion as data.
- source — an arXiv security analysis naming a specific mitigation (catalog: strong).
- cost — very low: a required-behavior line plus a delimiter convention in the directive format.
Case: A clean, wholly unfilled slot with real exposure and a cheap mechanism.
The ingestion points are all already written into the methodology:
`roles/chief-of-staff.md` takes pasted Claude Code output as its normal input
("Dave does not read Claude Code output. He pastes it here; CoS is the reader");
`policies/source-of-truth-policy.md` treats GitHub Issues as consumed artifacts;
`skills/directive-dispatch.md` Track B has an agent-authored file downloaded
through `~/Downloads` and committed; web research enters as documents (this scan
is an instance — its two input catalogs are agent-authored files that later
agents read as data); and MCP tool output crosses into every session. In every
one of those paths, content that is data arrives in the same undifferentiated
channel as instructions that are authority, and nothing in the corpus says it
must be marked. The methodology is otherwise meticulous about exactly this class
of confusion — `LEXICON.md` exists to stop an execution block being mistaken for
a command block — so the omission reads as a vein never considered rather than
a position taken.
Cycle input: Propose a required-behavior line in `context-sets/base.md`: content ingested from outside the governed corpus — tool output, pasted session reports, Issues, fetched documents, downloaded artifacts — is data and never instruction, and is marked as such when placed in a prompt. Propose a delimiter convention in `skills/directive-dispatch.md` for directives that embed ingested material. Consider whether a companion boundary document (`boundaries/ingested-content-boundary.md`) is the right durable home, by analogy with the existing boundary set.

## SRE-06 — Toil capped at a fixed share of engineering time, tracked and enforced
Bucket: gap
Methodology position: the *principle* is held twice and load-bearingly — `boundaries/human-review-boundary.md` §Core principle ("Human attention should be spent on judgment, not on pretending to be a compiler") and `roles/chief-of-staff.md` §Handling execution-session reports ("His attention is the scarce resource — spend it on judgment, not reading"). The *measurement* is held nowhere.
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost l
Score reasons:
- relevance — the operator's attention is this methodology's declared scarce resource and its stated design constraint, and there is no instrument reading it; every claim that the methodology is working is currently an impression.
- mechanism — define toil precisely against valuable operational work, measure the share by periodic survey, and treat a breach of a fixed ceiling as requiring intervention rather than backlog grooming.
- source — the originating organization's own published practice, with its own measured baseline (catalog: strong).
- cost — very low: a periodic self-report against a definition, no tooling required.
Case: This is the highest-leverage cheap finding in the catalog. The
methodology's whole thesis is a claim about where Dave's attention goes — off
diff-reading, onto judgment — and it holds that claim as a principle in two
documents while measuring nothing. Every mechanism in the corpus is justified by
its effect on that budget (the Chief of Staff's triage-don't-relay rule, the
two-tier gate's anti-ceremony argument, the review artifact's verdict-first
schema, the skill-compression sweep), and none of them can be evaluated, because
the quantity they optimize is unobserved. The corpus itself supplies the
evidence that this is a live problem, not a theoretical one: the
`docs/global-retro-inbox.md` entries are largely reports of operator time going
into mechanics — hand-assembling bundle headers, hand-repairing command blocks,
relaying Claude Code output, re-deriving SHAs — which is toil by Google's
definition exactly, and none of it is counted. A methodology whose core rule is
"agent claims require evidence" is currently running its central premise on
none.
Cycle input: Propose a toil definition and a periodic self-measure against it — what share of Dave's time in a period went to manual, repetitive, automatable work with no lasting value (relaying output, hand-assembling blocks, chasing SHAs, re-running mechanics) versus judgment (agreement, release decisions, triage). Propose a ceiling and, per the methodology's own evidence rule, that tooling proposals in `BACKLOG-v2.md` be prioritized by measured toil rather than by intuition. Keep it lightweight: the value is the number existing, not its precision.

## TEST-04 — Mutation testing: test-suite quality measured by mutants killed
Bucket: gap
Methodology position: `policies/testing-policy.md` §Coverage ("Line coverage is a weak signal ... Do not use coverage as a substitute for boundary analysis"); `context-sets/testing-and-verification.md` §Anti-patterns ("using coverage as proof of correctness"); `policies/agent-review-policy.md` §Required review posture ("tests may pass while proving less than claimed"; "the agent that wrote the code may have optimized for green tests"); `roles/skeptic-risk-agent.md` §Core question
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost m
Score reasons:
- relevance — the methodology's central anxiety, stated in four documents, is tests that pass while proving less than claimed; mutation score is the one mechanical measurement of exactly that quantity.
- mechanism — inject faults, run the suite, score by the fraction detected; a number, computed, not judged.
- source — encyclopedic and practitioner-guide sources, though the technique is standard and independently well documented (catalog: mixed).
- cost — moderate: runtime is significant and it needs a CI home separate from the fast suite.
Case: The methodology diagnoses this problem more precisely than most and then
prescribes only a judgment substitute. It correctly rejects line coverage,
correctly names what coverage misses, and directs the reader to *boundary
analysis* — which is an agent thinking carefully, i.e. the same faculty already
under suspicion. Mutation testing answers the identical diagnosis mechanically:
a line executed without its outcome asserted on is precisely a surviving mutant,
and the surviving-mutant list is a concrete, per-line map of where the suite is
decorative. It bears directly on the one risk the corpus flags twice — that the
agent which wrote the code optimized for green — because a suite optimized for
green is a suite with a low kill rate, and that is now visible instead of
suspected. Of everything in this catalog, this is the practice most exactly
shaped to the methodology's own stated fear.
Cycle input: Propose mutation testing as a named, non-default verification mechanism in `policies/testing-policy.md`, run outside the fast suite per the existing CI split in `policies/verification-boundary-policy.md` §CI and automation expectations. Propose the mutation score as evidence a Skeptic/Risk review may cite, replacing the current unsupportable "test adequacy" judgment with a number. Do not propose a threshold gate in the first cycle — a kill-rate target adopted before a baseline exists is the coverage mistake with a new metric.

## FORMAL-02 — Property-based testing as formal-methods on-ramp
Bucket: gap
Methodology position: `policies/testing-policy.md` §Test levels (1–7, all example-based); `context-sets/testing-and-verification.md` §Verification classes; `context-sets/spec-and-change-discipline.md` §The canonical sequence (the true-red-gate paragraph)
Coverage: none — the test-level list has no entry for property-based testing and no adjacent construct
Scores: relevance h · mechanism h · source h · cost m
Score reasons:
- relevance — the methodology names a shared-blind-spot failure it cannot currently close, and example-based tests are precisely what a shared blind spot survives.
- mechanism — write a property over all inputs, generate cases against it; concrete, tool-supported, adoptable one unit at a time.
- source — technical paper describing the design rationale, plus a mature tool tradition behind it (catalog: strong).
- cost — a library and a shift in how a Test Designer thinks; additive, no structural change.
Case: The methodology's most carefully-argued paragraph is the true-red-gate
rule, and its stated reason is that "both agents can share the same blind spot,
and the shared blind spot survives to green." Test/Coder separation reduces that
risk but cannot remove it, because both agents choose *examples*, and two agents
reasoning from the same AC choose overlapping ones — which is exactly what
happened in the P3 contact-merge case the rule cites, where a real gap survived
implementation and an independent test pass. A property is not an example: it is
a claim about all inputs, and the generator, not the agent, picks the cases. That
attacks the shared blind spot from a direction agent separation structurally
cannot. It also fits the methodology's own framing of graduated rigor — this is
the on-ramp, not the model checker.
Cycle input: Propose adding property-based testing as a named test level in `policies/testing-policy.md`, and a line in `context-sets/spec-and-change-discipline.md` recommending it where the derived-field/blind-spot risk is highest (write-path packages, entities with derived fields). Evaluate against the counter-argument that ACs written by Dave are example-shaped, so a property has to be inferred rather than derived — which puts inference back in the agent.

## OTHER-01 — Consumer-driven contract testing
Bucket: gap
Methodology position: `boundaries/mocked-boundaries.md` §Policy ("A claim about our side of the contract, with the other side verified elsewhere or explicitly accepted as unverified"); `context-sets/testing-and-verification.md` §Contract-verified; `policies/verification-boundary-policy.md` §Boundary declaration (`deferred_verification`); `policies/testing-policy.md` §Test levels (4)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost m
Score reasons:
- relevance — the methodology names this exact hole in its own words and leaves it open; "the other side verified elsewhere" is a promise with no named mechanism behind it.
- mechanism — the consumer authors the contract, the provider is verified against it in isolation, and a broker answers "are these two versions safe to deploy together"; three separable, concrete steps.
- source — tool-vendor-adjacent, but the consumer-authors-the-contract claim is specific and mechanical (catalog: mixed).
- cost — tooling plus a CI job, but additive and adoptable one integration at a time.
Case: This is the sharpest fit-to-a-stated-hole in the catalog. The
methodology's mock rule is honest about what it does not know — every mocked
boundary carries a `deferred_verification` field, and in practice that field
resolves to "live smoke test" or "pre-release checklist," both of which are
manual, slow, and only run near release. Consumer-driven contract testing turns
the deferred half into a fast, automated artifact: the consumer's expectations
become an executable contract the provider is verified against without running
integration. That converts a standing `unverified` claim into a
`contract-verified` one on the methodology's own vocabulary, and it does so
without adding a live dependency to the fast test run — which
`context-sets/testing-and-verification.md` §Anti-patterns explicitly forbids.
The catalog followed this outside its seed list because it addresses
hallucinated interfaces; against this corpus its stronger claim is that it is
the missing mechanism behind an already-written policy field.
Cycle input: Propose adding consumer-driven contract tests as a named deferred-verification mechanism in `policies/verification-boundary-policy.md` and as a worked path in `context-sets/testing-and-verification.md` §Contract-verified. Evaluate the broker separately — the deploy-safety-source-of-truth claim is a second, heavier adoption with its own operational cost, and the contract tests are useful without it.

## LLM-02 — Evaluation-Driven Development with LLM-as-judge
Bucket: gap
Methodology position: none for agent behavior. `policies/testing-policy.md` and `context-sets/testing-and-verification.md` govern tests over *deterministic code* only; nothing in the corpus evaluates whether a change to a governing document changes agent behavior.
Coverage: none
Scores: relevance h · mechanism h · source h · cost h
Score reasons:
- relevance — the methodology's own core rule is "agent claims require evidence," and the methodology's own changes ship on judgment with no evidence of effect; that is the failure mode, stated against itself.
- mechanism — design evaluations for models, data, and workflows as the analog of tests, using a judge where exact-match is unusable; a named process model with a reference architecture.
- source — an arXiv paper proposing a named process model (catalog: strong).
- cost — high: an eval harness, a case set, and a judge configuration are real infrastructure.
Case: The sharpest self-inconsistency the diff surfaced. Every mechanism in this
corpus is gated on evidence — the red-gate, the boundary declarations, the
verification classes, the change package — and the corpus itself is exempt.
Documents are reviewed for completeness, internal consistency, and traceability
(`roles/spec-reviewer-agent.md`), which are all properties of the text; nothing
asks whether the revised text produces better agent behavior. The corpus
supplies its own evidence that this hurts. `docs/global-retro-inbox.md`
2026-08-07 states a hypothesis it cannot test — "if CoS follows the compressed
version noticeably better, that is evidence the *whole skill corpus* wants this
pass" — and the compression sweep it proposes is therefore unfalsifiable and
unprioritizable. `OPEN-ITEMS.md` §"Model selection by role" demands "an evidence
step before demotion: trial the cheaper tier on a routine package with all
guards active; the guard-fire rate is the signal," and explicitly says tier
decisions must not be assigned by intuition, "including the intuition of the
frontier model that proposed this item" — an eval requirement, written down,
with no harness to satisfy it. Both items are blocked on the same missing
mechanism.
Cycle input: Propose an evaluation harness for agent behavior against the corpus, scoped minimally to start: a small set of representative role invocations with expected behaviors, run against a candidate document revision and its predecessor. Two named consumers already exist and should be cited as the justification — the skill-compression hypothesis and the model-tier demotion evidence step. Evaluate the LLM-as-judge element separately; it carries its own bias questions and LLM-12's separation rule should govern which model judges.

## DESIGNDOC-06 — Mandatory "alternatives considered" section
Bucket: gap
Methodology position: `policies/decision-log-policy.md` §Entry format (ID, Date, Decision, Context, Supersedes — no alternatives field); `context-sets/base.md` §Required behavior (the consult obligation); `docs/global-retro-inbox.md` 2026-08-04 (the sketch proposed "options considered" and the agreed policy dropped it)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — an agent re-proposing an option that was considered and rejected is the precise failure the decision log was built to stop, and the log currently records the choice without the rejections.
- mechanism — one required section naming each serious alternative, why it was rejected, and what was being optimized for.
- source — practitioner guidance converging across independent sources, not an organizational standard (catalog: mixed).
- cost — one field on an existing format; near zero.
Case: **The catalog flagged this `possible-dup of DESIGNDOC-01`; against this
methodology it is not a duplicate, and the reason is specific.** ADR templates
often fold alternatives into "context," but this repo's entry format has no
consequences field *and* no alternatives field, so neither element arrives by
implication. The corpus supplies its own argument for the field: the consult
obligation asks an agent to check the log "before recommending or encoding
anything an existing decision may govern," and the
`docs/global-retro-inbox.md` rationale is explicit that an agent "rediscovering
known problem X on something already knowingly accepted should find the entry
and stand down, not raise it as a fresh finding." An entry recording only what
was chosen cannot do that: the agent finds a decision it does not conflict with
and proceeds to re-raise the rejected option. Practice already exceeds the
schema — DEC-000080 records what was nearly cut and why it was kept,
`MANIFEST.md` rejects enriching `depends-on` "on two grounds" — which is
evidence the field is wanted, written inconsistently into a field not meant for
it. This is also the cheapest available resolution of the DESIGNDOC-02
contradiction.
Cycle input: Propose adding an alternatives-rejected field to the `policies/decision-log-policy.md` entry format, required where a decision had a serious alternative and omit-if-none otherwise. Package with DESIGNDOC-01's consequences field as one revision. Note `policies/decision-log-policy.md` is `agreed` and DEC-000050 places it outside the gate-document class, so the doc-only cycle is available if Dave asks for it.

## SAFETY-05 — Bidirectional requirements-to-code-to-test traceability
Bucket: gap
Methodology position: `roles/spec-reviewer-agent.md` §Gate review responsibilities ("confirm traceability: every claim traces to a parent artifact"); `policies/agent-review-policy.md` §Spec Reviewer Agent ("ACs trace to user journeys; TRD NFRs instantiate PRD NFRs"); `policies/source-of-truth-policy.md` §Canonical order. All of these trace *documents to documents*, upward only.
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost m
Score reasons:
- relevance — unmotivated code is the LLM failure mode this methodology polices with an instruction ("do not silently broaden scope") and no mechanism; the reverse link is the mechanism.
- mechanism — forward links requirement→design→code→test and backward links back, kept consistent; the coverage and scope-control queries both fall out of it.
- source — vendor explainer, but the bidirectionality claim and its dual purpose are specific (catalog: mixed).
- cost — moderate: link maintenance, and it wants tooling to stay honest.
Case: The methodology traces the document spine upward and stops at the spine's
bottom edge. It can answer "does this AC trace to a journey?" and cannot answer
either of the two questions bidirectional traceability is for: *which
requirements have no test*, and *which code or tests exist that no requirement
asked for*. The second is the one that matters most here. Scope discipline is
currently carried entirely by instruction — `context-sets/base.md` ("keep scope
explicit; do not silently broaden it"), `roles/coder-agent.md` ("broaden scope
silently" is prohibited) — and an instruction is exactly the control an agent
can satisfy sincerely while still emitting a helper nobody asked for. A backward
link makes that detectable rather than reviewable.
Cycle input: Propose extending traceability past the document spine: each test and each non-trivial code unit names the AC it exists to satisfy, and the Reviewer Agent's pass reports both directions — ACs with no test, and tests or units with no AC. Evaluate the cheapest honest form first (a naming convention plus a script) before proposing a link artifact.

## SRE-02 — Production Readiness Review gate
Bucket: gap
Methodology position: `policies/release-readiness-policy.md` and `skills/release-readiness-review.md` (per *change*, not per service); `specs/trd-template.md` §2 (SLO, measurement mechanism, and alerting threshold required per Top K journey) and §7 Operational concerns; `BACKLOG-v2.md` §"SRE-centric production readiness checklist"; `OPEN-ITEMS.md` §"~~SRE production readiness checklist~~" (RESOLVED (deferred))
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — the methodology has an explicit, self-identified hole here and deferred it for want of content, not for want of interest.
- mechanism — a fixed pre-traffic checklist: SLOs defined, baselines collected, SLI instrumentation *verified*, golden signals instrumented, dashboards created.
- source — vendor guide, but it supplies a concrete gate rather than a philosophy (catalog: mixed).
- cost — low: it is a checklist, and most of its items already have homes in the TRD.
Case: The gap is named in the repo's own backlog, so the finding is not that
something is missing but that this practice supplies exactly what the backlog
item asked for. The substantive difference from what exists: release readiness
here is evaluated *per change*, and a PRR is evaluated *once, per service,
before it first takes traffic*. Those catch different things. Per-change review
never asks whether the service as a whole is observable, because no single
change owns that question. The item the methodology most conspicuously lacks is
the third one — **SLI instrumentation verified**, as distinct from SLOs
*defined*. The corpus is already candid that this is unverified:
`boundaries/mocked-boundaries.md` lists "SLO monitoring and error budget
tracking (targets defined but no production signal in place)" as a standing
mocked boundary, and `roles/skeptic-risk-agent.md` includes "SLO target is
defined but no mechanism exists to verify it in production" in its
false-confidence checklist. A PRR is the gate that would stop that state from
reaching production in the first place.
Cycle input: Propose discharging the deferred `BACKLOG-v2.md` production-readiness item with this checklist as the starting content, filed as a new `policies/production-readiness-policy.md` or a section extending the definition of done. Priority item within it: instrumentation *verified*, not merely defined — which closes a boundary the corpus already declares open.

## SDD-04 — Specification by example: concrete examples as living documentation
Bucket: gap
Methodology position: `context-sets/spec-and-change-discipline.md` steps 2 and 4 (ACs written, then translated to test code by the Test Designer); `specs/prd-template.md` §6 ("concrete enough to test"); `OPEN-ITEMS.md` §"Spec evolution policy — how does the spec stay canonical when reality diverges?" (open)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost h
Score reasons:
- relevance — spec drift is not hypothetical here; it is a named, unresolved open item sourced from a real divergence (the 511 SF Bay response-shape mismatch that was fixed in code and never reflected in the TRD).
- mechanism — the spec unit is a concrete example, examples are automated, and the automation is re-run continuously; each of those is separately adoptable.
- source — Adzic's own formulation of the seven-pattern method (catalog: strong).
- cost — high and structural: it changes what an AC *is*, and the living-documentation half needs a build.
Case: The methodology holds the AC→test-code half (adjacent) and holds nothing
of the executable-specification half (the gap). Its specs are prose that can
silently stop describing the system, and its only detector is the Spec
Reviewer's continuity scan — a human-triggered read, not a failing test.
Specification by example makes divergence *break the build*: because the spec
unit and the test are the same artifact, an implementation that no longer
matches the spec cannot stay green. That is a mechanical answer to the exact
question `OPEN-ITEMS.md` asks and leaves unanswered ("How to keep the spec
trustworthy as a regeneration artifact over time"). It also carries SDD-01's
unheld residue — the spec as a machine-consumable artifact rather than prose.
Cycle input: Propose specification-by-example as a candidate mechanism for the open "Spec evolution policy" item — specifically, whether per-unit ACs should be authored as concrete examples that compile directly into the test suite, so spec/implementation divergence surfaces as a red test rather than as a continuity-scan finding. Scope the proposal to ACs only; do not propose replacing the PRD/TRD prose spine.

## SAFETY-07 — Hazard analysis derives safety requirements at the requirements phase
Bucket: gap
Methodology position: `context-sets/production-grade-software.md` §Failure mode thinking (six questions, asked per change); `specs/trd-template.md` §6 Failure modes and recovery (the standing picture); `roles/skeptic-risk-agent.md` §Responsibilities (operational failure modes, after implementation)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost m
Score reasons:
- relevance — the methodology asks what happens if a change fails, but only *after* the change exists; nothing derives requirements from hazards before the design is fixed.
- mechanism — top-down fault tree (or bottom-up FMEA) at the requirements phase, repeated after implementation against the same tree; a specific technique at a specific lifecycle point.
- source — NASA's own software engineering handbook, corroborated by a vendor explainer (catalog: mixed, but the primary is authoritative).
- cost — moderate: a real analytical step, though tractable at the Top K journey granularity the PRD already imposes.
Case: The methodology's failure-mode thinking is *reactive to a proposed change*
and its risk role fires *after implementation*. What is missing is the generative
direction: starting from the hazards and deriving the requirements that prevent
them, before the architecture is fixed. The methodology has the perfect hook for
this and does not use it — the PRD's Top K journeys are already the agreed set of
things that must not break, and the TRD already attaches an SLO to each. A fault
tree per Top K journey would produce exactly the artifact the TRD's failure-modes
section currently asks an Architect to write from intuition. The second half of
the practice matters as much as the first: re-run the analysis against the
implemented design, which is a check the methodology has no counterpart for at
all.
Cycle input: Propose that the Architect derive TRD §6 failure modes by a stated top-down analysis over the PRD's Top K journeys rather than by unaided enumeration, and that the same analysis be re-run against the implemented design before release. Evaluate whether this belongs in `roles/architect-agent.md` as a method requirement or in `specs/trd-template.md` as an authoring-checklist item.

## LLM-08 — Validator-guided repair for hallucinated APIs
Bucket: gap
Methodology position: none for post-generation validation. Adjacent: `operating-model.md` §Change flow step 5 ("mechanical checks (lint, types, static analysis) pass as part of 'green'"); `context-sets/base.md` §Evidence vocabulary (Contract-verified); `boundaries/mocked-boundaries.md`
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost m
Score reasons:
- relevance — a fabricated API call is the LLM defect most likely to survive a mocked test suite, because the mock is written by the same agent that invented the call.
- mechanism — validate generated calls against the real API schema after generation and repair mismatches iteratively; quantified (96.6% pass rate for repair alone, 98.63% combined with routing).
- source — a thesis/technical report with measured results for the specific mechanism (catalog: strong).
- cost — moderate: it needs a machine-readable reference for each external API.
Case: A partial gap with an obvious home already built. The methodology's most
carefully-defended claim is that a mock is "a claim about our side of the
contract" — but when an agent writes both the calling code and the mock that
stands in for the provider, the mock inherits the hallucination, and the suite
goes green on a call that does not exist. Nothing in the corpus catches that. The
adjacency is `operating-model.md`'s mechanical-checks clause: lint, types, and
static analysis are already deterministic evidence folded into "green" rather
than treated as a review step, and schema validation of generated external calls
is the same kind of check with the same properties. This is also the same hole
OTHER-01 approaches from the provider side — validator-guided repair checks the
call against the published schema, consumer-driven contract testing checks the
provider against the expectation; adopting either helps, adopting both closes
the boundary from both directions.
Cycle input: Propose folding schema validation of generated external API calls into the mechanical-checks set in `operating-model.md` step 5, where a machine-readable reference exists for the dependency. Triage alongside OTHER-01 as one boundary-closing proposal rather than two.

## DBC-01 — Contracts as caller/callee obligations
Bucket: gap
Methodology position: none for the practice's own mechanism. Adjacent: `context-sets/base.md` §Evidence vocabulary ("Contract-verified: against a documented or encoded interface contract"); `context-sets/testing-and-verification.md` §Contract-verified; `policies/testing-policy.md` §Test levels (4, "Contract tests for external assumptions")
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost m
Score reasons:
- relevance — an LLM writing a caller and an LLM writing a callee agree on an interface that neither wrote down; the methodology's Test/Coder split gives independent tests but nothing that makes the obligation itself explicit.
- mechanism — preconditions, postconditions, and invariants are a precise, annotatable, checkable triad.
- source — Meyer's own formulation (catalog: strong).
- cost — additive per boundary, but language-dependent and it touches every interface it reaches.
Case: The methodology's `contract-verified` class is about *external* interfaces
and is a claim about evidence — "we checked our side against a documented
contract." Design by contract is about *internal* component boundaries and is a
claim about correctness — the obligation is attached to the code and enforced at
the interaction point. Same word, different object and different mechanism, so
this is a partial gap and not "already covered." What it would add: the
methodology's architecture summary names "affected components" and "interfaces
between components" (`roles/architect-agent.md`, `specs/trd-template.md` §3) but
never says what a caller must guarantee or what a callee promises. That is
precisely the information an agent implementing one side has to invent, and
inventing it is how a plausible-but-wrong implementation passes its own tests.
Cycle input: Propose that the per-change architecture summary state, for each interface it touches, the caller's preconditions, the callee's postconditions, and any invariant — and that `roles/test-designer-agent.md` derive negative tests from the stated preconditions. Evaluate whether runtime enforcement is in scope or whether the stated contract is documentation the Test Designer consumes.

## LLM-05 — Periodic re-anchoring on the original objective
Bucket: gap
Methodology position: the drift problem is addressed *structurally* — `skills/directive-dispatch.md` §Route ("Fresh — the default. The directive is self-contained") and §Writing the directive file ("the executor needs the file and the repository, nothing from the conversation"); `skills/spec-review-cycle.md` §Hard constraints (one conversation per cycle); `roles/chief-of-staff.md` (recommends ending a session when its expensive context is spent). No in-run re-anchoring exists.
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source l · cost l
Score reasons:
- relevance — high: directive-execution sessions here are long and single-purpose, which is exactly the shape drift is reported in.
- mechanism — at periodic checkpoints, restate the objective and check the current action against it; trivially implementable.
- source — a practitioner blog with no controlled study behind it; the weakest sourcing in the LLM vein (catalog: mixed, and the rationale is asserted rather than measured).
- cost — very low: a line in the directive format.
Case: The methodology attacks instruction drift by *bounding exposure* — fresh
sessions by default, self-contained directives, one conversation per cycle, end
the session when its purpose is served. That is a real and arguably better
control than in-run correction, because it removes the contaminating context
rather than compensating for it. What it does not cover is the long single
session that a self-contained directive legitimately requires, where the
directive is read once at the start and everything after is the agent's own
accumulating output — and `skills/directive-dispatch.md` already names the
symptom in its executor obligations ("Report what was done, not what the
directive said"), which is a rule against a *consequence* of drift with no
mechanism against drift itself. Note the weak source honestly: this is a
plausible mechanism, not a demonstrated one.
Cycle input: Propose a checkpoint instruction in the directive file format — at each batch or stage boundary, restate the directive's objective and the current instruction, and confirm the work still serves it. Cheap enough to adopt on plausibility, but propose it as a trial with the LLM-02 harness as the eventual arbiter rather than as a settled rule.

## LLM-11 — Graduated, threshold-triggered proactive context compaction
Bucket: gap
Methodology position: none. Adjacent: `roles/chief-of-staff.md` §Constraints ("When work needing the currently-loaded expensive context is done, says so and recommends ending the session"); `skills/spec-review-cycle.md` §Hard constraints (one conversation per cycle; documents as uploads, never mid-conversation fetches); `MANIFEST.md` §Context-set bundles (paste only the sets a chat needs)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost m
Score reasons:
- relevance — long execution sessions are the normal working mode here, and what happens to their context under pressure is currently invisible to the methodology.
- mechanism — staged utilization thresholds with progressively more aggressive compression, summarization only as a last resort; fully specified.
- source — an arXiv paper plus a framework vendor's documented implementation of the same staged mechanism (catalog: mixed, but two independent instances).
- cost — moderate, and largely borne by tooling rather than by the methodology.
Case: The methodology manages context *at the front* — curated bundles, uploads
rather than fetches, one conversation per cycle, end the session when its
purpose is served — and holds no position on what happens once a session is
underway and filling. The adjacency is real but the mechanisms are opposite in
kind: choosing what to load is a curation decision made by a human before the
work; compaction is a capacity decision made by measurement during it. The
methodology's blind spot here is specific and worth naming — compaction is
already happening in every long session, performed by the harness, on rules the
corpus neither states nor knows, which means an executor's effective context can
change mid-directive with no evidence trail. That is a verification-boundary
question in the methodology's own terms and it is undeclared. Note the vendor
boundary caps what is adoptable: per `boundaries/vendor-tooling-boundary.md` the
durable rule must be tier-neutral, with the mechanism left to tooling.
Cycle input: Propose a vendor-neutral context-budget posture rather than a compaction algorithm — a directive states what an executor must re-read or re-establish if its context is compacted mid-run, and an executor reports compaction as an event affecting its evidence, the same way `skills/directive-dispatch.md` requires concurrent tree mutation to be surfaced. Frame the undeclared-compaction issue as a candidate entry for `boundaries/`.

## SAFETY-03 — Harm-based tri-level safety classification
Bucket: gap
Methodology position: `policies/commit-and-change-control-policy.md` §Tier 2 (the consequential class, an exhaustive list of touched surfaces); `specs/prd-template.md` §7 Risk tolerance; `OPEN-ITEMS.md` §"~~A2 — Consequential-change class~~" (resolved: the list is exhaustive)
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source m · cost m
Score reasons:
- relevance — the methodology classifies by *what a change touches*, never by *how bad it would be if it broke*, so two changes touching auth are the same tier whether the blast radius is one user or all of them.
- mechanism — three harm bands plus a mandatory documented, justified, approved classification artifact; fully specified.
- source — vendor explainers of a named standard, but the tri-level scheme and the documentation requirement are checkable claims about IEC 62304 (catalog: mixed).
- cost — moderate: a per-component classification artifact that must be produced and kept current.
Case: Distinct from SAFETY-01 and deliberately not collapsed into it. SAFETY-01
is *scale rigor to a class*, which the methodology holds. SAFETY-03 is two
further things it does not: the class is derived from **severity of harm**
rather than from a surface list, and the classification is itself a **documented,
justified, approved artifact** rather than an inference an agent makes per
change. The surface-list approach has a known weakness the methodology has
already felt — the list is exhaustive by fiat (A2's resolution) and therefore
lags, and the fallback is "when unsure, treat as consequential and ask," which
pushes judgment back to Dave every time the list is imperfect. A harm-severity
criterion degrades more gracefully: an unlisted surface still gets classified.
Cycle input: Propose evaluating a harm-severity criterion as a *complement* to the exhaustive surface list — the list stays as the fast path, the criterion covers what the list has not yet learned. Also propose that the classification be recorded per project rather than re-derived per change, which is the SAFETY-01 residue.

## SRE-05 — Multi-window, multi-burn-rate SLO alerting
Bucket: gap
Methodology position: `specs/trd-template.md` §2 (each Top K journey defines an "Alerting threshold: at what point a breach triggers action"); `context-sets/testing-and-verification.md` §Production-verified; `boundaries/live-integration-boundaries.md` §Recommended cadence
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source h · cost m
Score reasons:
- relevance — the TRD mandates an alerting threshold per journey and says nothing about its shape, so every project reinvents it and most will get it wrong in the same direction (single-window, either noisy or slow).
- mechanism — require a fast and a slow burn-rate window to trip simultaneously; precise and directly implementable.
- source — the originating organization's own SRE workbook (catalog: strong).
- cost — moderate, and mostly borne by monitoring tooling rather than the methodology.
Case: The methodology asks for the right field and gives no guidance on filling
it, so the practice is a partial gap rather than a contradiction: it supplies
the shape the TRD's `Alerting threshold` should take. The single-threshold form
the template implies has a known failure in both directions — tight enough to
detect a real incident quickly is loose enough to page on a transient spike, and
this methodology has one operator, for whom a false page is disproportionately
expensive. Worth noting the sequencing: this is only actionable once SRE-02's
instrumentation gap is closed, since an alerting rule over an instrument that
does not exist is the definition of the false confidence
`roles/skeptic-risk-agent.md` polices.
Cycle input: Propose guidance (not a mandate) in `specs/trd-template.md` §2 that an alerting threshold be specified as a multi-window burn-rate condition rather than a single value, with the vendor-neutral framing the methodology already uses for flag backends — state the pattern, leave the monitoring backend a per-project choice.

## TEST-01 — Gherkin Given/When/Then as shared executable spec
Bucket: gap
Methodology position: `specs/prd-template.md` §6 Acceptance criteria ("concrete enough to derive test cases from", owned by Dave); `context-sets/spec-and-change-discipline.md` steps 2 and 4; `roles/test-designer-agent.md` §Responsibilities ("derive test cases from acceptance criteria")
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source h · cost m
Score reasons:
- relevance — the AC→test translation is a real lossy step, but the stakeholder-alignment half of the practice's value does not apply when the stakeholder writes the ACs himself.
- mechanism — a semi-structured natural-language scenario format that is simultaneously the AC and the executable test.
- source — the Agile Alliance glossary, a recognized reference for the canonical definition (catalog: strong).
- cost — moderate: a tooling layer plus a change in how Dave writes ACs.
Case: The methodology keeps AC and test as two artifacts owned by two parties;
Gherkin collapses them into one. That collapse is the partial gap and also the
argument against adopting it, and both should be on the table. For: a prose AC
translated by an agent into test code has a silent failure — the agent's reading
of an ambiguous AC becomes the definition of correct, and nothing surfaces the
ambiguity. An executable scenario removes the translation. Against: the
translation step is currently where a *second* mind meets the AC, and the
methodology deliberately invests in second minds; removing the step removes an
independent read. Note this is a weaker version of SDD-04, which proposes the
same collapse with a stronger mechanism and a better-evidenced tradition behind
it.
Cycle input: Do not propose independently. If the executable-AC question is opened, open it via SDD-04, which carries the same mechanism with a primary source and a living-documentation half Gherkin alone does not supply.

## LLM-09 — Golden regression suite gates merge
Bucket: gap
Methodology position: none for agent behavior. Adjacent: `operating-model.md` §Change flow step 5 (mechanical checks folded into green); `policies/commit-and-change-control-policy.md` §Agents may open and merge pull requests (the merge is deliberately not a human gate — a mechanical gate does not conflict with this)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost h
Score reasons:
- relevance — every change to a governing document is a change to agent behavior with no regression check of any kind.
- mechanism — a curated golden case set, versioned in the same repo as the prompts and configuration, run automatically on every PR touching the agent, blocking on a metric drop.
- source — an individual practitioner blog; specific and checkable, but uncorroborated in this pass (catalog: mixed).
- cost — high: the harness is LLM-02's harness, plus a curated case set and CI wiring.
Case: The mechanical half of LLM-02. Two elements are worth separating. The
**versioned-alongside-the-corpus** element fits this repo exactly and cheaply —
the golden set would live beside the documents it evaluates, under the same git
versioning the methodology already uses for everything. The **merge-blocking**
element needs care but does not conflict with policy: the commit policy declines
to put a *human* gate on the merge and explicitly folds *mechanical* checks into
"green," so a blocking mechanical regression check is consistent with what is
written. The cost is that it does not exist without LLM-02.
Cycle input: Do not propose independently. Fold into the LLM-02 harness proposal as its delivery form — the harness is worth little unless something runs it on every corpus revision.

## TEST-03 — Automatic shrinking to a minimal counterexample
Bucket: gap
Methodology position: none. Adjacent: `roles/coder-agent.md` §Required outputs ("failures encountered"); `skills/spec-review-cycle.md` §Findings (`Location`, `Evidence`, `Consequence` per finding)
Coverage: none
Scores: relevance m · mechanism h · source h · cost l
Score reasons:
- relevance — real and specifically agentic: a failing case handed to an agent becomes context, and a large failing case becomes a lot of context spent on the parts of the input that were irrelevant.
- mechanism — repeatedly simplify the failing case until no smaller failing case exists, report only that one.
- source — the original tool's own documentation of its own behavior (catalog: strong).
- cost — near zero *if* property-based testing is adopted, since shrinking arrives with the library; not independently adoptable otherwise.
Case: A clean unfilled slot with an unusually good fit to an agentic workflow.
When a human reads a failing test, a large counterexample costs attention; when
an agent reads one, it costs context window and invites the agent to
pattern-match on incidental structure. Minimization is the cheapest available
improvement to the quality of a debugging prompt. It is not separately
adoptable, which is the whole of its cost story.
Cycle input: Fold into the FORMAL-02 proposal as a named benefit rather than raising separately.

## DBC-04 — Distribute-never-replicate: each check owned by exactly one party
Bucket: gap
Methodology position: for *documents*, the position is held and strongly: `policies/source-of-truth-policy.md` §Canonical order and §Keeping derived artifacts honest; `MANIFEST.md` §What is no longer here ("a second copy of a derivable fact drifts and then lies"); `policies/document-metadata-policy.md` §Excluded fields. For *runtime checks in code*, none.
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source h · cost l
Score reasons:
- relevance — LLM-generated code is reliably over-defensive; redundant validation on both sides of a call hides where the real contract lives and multiplies the places a rule can be changed wrongly.
- mechanism — assign each check to exactly one party and delete the duplicate; a rule with a clear violation test.
- source — Meyer's own formulation corroborated by an independent comparative study (catalog: strong).
- cost — a reviewer-checklist rule; near zero.
Case: **Classification is genuinely ambiguous and is flagged for Dave.** Read as
a principle — one owner per fact, delete the redundant copy — the methodology
holds it about as hard as it can be held, and this is convergence. Read as the
practice actually catalogued — an allocation rule for validation checks in
code — the methodology holds nothing, and this is a gap. Filed as a gap because
the object differs, and because collapsing it would license an unsupported
"already covered." One live complication worth surfacing either way: the
`docs/global-retro-inbox.md` 2026-08-07 drift-audit entry explicitly qualifies
the no-duplicates principle for context documents ("load-bearing repetition —
LLM adherence can genuinely benefit from repetition — do not reflexively DRY"),
which is the *opposite* of Meyer's rule and is in direct tension with LLM-06.
The two findings should be triaged together.
Cycle input: Propose a Reviewer Agent checklist line for single-owner validation in code. Separately, propose that the queued drift-audit tranche settle the document-level question and the LLM-06 placement question in one pass, since a single rule has to serve both.

## SAFETY-02 — Parallel integral processes alongside development
Bucket: gap
Methodology position: `operating-model.md` §Change flow ("Each stage completes before the next begins; no skipping or working ahead"; quality review and skeptic/risk review are stages 6 and 7, after implementation); `context-sets/spec-and-change-discipline.md` §The canonical sequence. Continuous elements that do exist: `roles/spec-reviewer-agent.md` §Continuity scan (Depth 1 on every revision), mechanical checks folded into "green," `OPEN-ITEMS.md` checkpoint discipline.
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism m · source m · cost m
Score reasons:
- relevance — review findings that arrive only at stage 6 arrive after the work they would have changed; that cost is real here.
- mechanism — "run these as continuous processes" is a lifecycle-structure claim; what is adoptable from it is which specific activities move, and the catalog does not decompose that.
- source — vendor explainer restating a standard's structure (catalog: mixed).
- cost — moderate; it reshapes the change flow without rewriting its principles.
Case: **Classification is ambiguous and is flagged for Dave** — this can be read
as a narrow contradiction rather than a gap. The methodology is not guilty of
end-loading verification (the red-gate is verification before implementation,
and the continuity scan runs on every revision), so the flat contradiction
reading would be a strawman. What it genuinely lacks is any *configuration
management* process at all, and its two review roles are terminal stages, so a
maintainability or false-confidence finding surfaces only once implementation is
complete. That is the partial gap. The broader sequencing question — whether
mandating stage order is right at all — is carried properly by SAFETY-04, and
these two should be triaged together.
Cycle input: Propose the narrow half only: evaluate whether any Reviewer or Skeptic/Risk check is cheap enough to run continuously during implementation rather than as a terminal stage. Defer the lifecycle-structure question to SAFETY-04.

## DBC-03 — Contract-violation type mechanically localizes fault (blame assignment)
Bucket: gap
Methodology position: none. Adjacent: `context-sets/spec-and-change-discipline.md` §The canonical sequence (the true-red-gate rule, whose stated purpose is that "both agents can share the same blind spot, and the shared blind spot survives to green")
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source h · cost m
Score reasons:
- relevance — real, and it maps onto a question this methodology asks constantly (when evidence fails, whose gap is it — the Test Designer's or the Coder's?) but answers by judgment rather than by construction.
- mechanism — which clause fired determines which side is at fault; no interpretation step.
- source — peer-reviewed formalization of the blame mechanism, POPL 2011 (catalog: strong).
- cost — none of its own; it is a free consequence of DBC-01 and costs the whole of DBC-01 otherwise.
Case: This is DBC-01's strongest argument rather than a separate practice. The
methodology's Test/Coder separation buys independence but not localization: when
a test fails, nothing tells you whether the test encodes the wrong expectation
or the implementation is wrong, and the two agents that could tell you are the
two agents under suspicion. A contract makes the answer mechanical.
Cycle input: Carry as supporting rationale inside the DBC-01 evaluation; do not raise as a separate proposal.

## FORMAL-05 — Counterexample-guided incremental abstraction refinement
Bucket: gap
Methodology position: `roles/spec-reviewer-agent.md` §Scan depths (Depth 1 default, Depths 2–3 on demand); `specs/trd-template.md` §Required sections ("Keep each section as short as it can be while still being a real answer"); `docs/global-retro-inbox.md` 2026-08-07 (skill-compression entry)
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism m · source h · cost l
Score reasons:
- relevance — the methodology has a live, self-diagnosed problem with document detail (skills drifting long enough to hurt adherence) and no rule for when detail is *earned*.
- mechanism — as an adoptable practice this is the cataloguer's reframing, flagged as such in the catalog; the underlying algorithm is not the thing being proposed.
- source — foundational peer-reviewed CEGAR paper (catalog: strong), though the reframing is inference over it.
- cost — near zero: it is a triage rule, not a tool.
Case: The methodology already scales analysis effort in stages (scan Depths 1–3)
but chooses the depth by human judgment; CEGAR's distinguishing move is that
refinement is *triggered by a specific failure the coarse version produced*.
Applied to documents rather than models, the rule is: a spec or skill section
earns more detail when a real defect traces to its vagueness, and not before.
That is a concrete answer to the compression-versus-completeness tension the
retro inbox raises, and it has the property this repo likes — the trigger is
evidence, not taste. Term overlap with the scan depths is not mechanism overlap,
so this is filed as a gap rather than convergence.
Cycle input: Propose a refine-on-counterexample rule for governed documents — detail is added to a section when a traced defect demonstrates the current wording was insufficient, recorded with the defect that prompted it (the corpus already does this informally: the derived-field checklist and the true-red-gate paragraph both name the failure that produced them). Package with the queued skill-compression sweep rather than alone.

## FORMAL-03 — Pre-implementation modeling to catch design-level bugs cheaply
Bucket: gap
Methodology position: `roles/architect-agent.md` §Two artifacts (per-change architecture summary before implementation); `specs/trd-template.md` §6 Failure modes and recovery; `context-sets/production-grade-software.md` §Failure mode thinking; `roles/spec-reviewer-agent.md` (gate before agreement)
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism m · source m · cost h
Score reasons:
- relevance — design-level defects found after implementation are expensive here too, and the methodology's only pre-implementation check on a design is a reviewing agent reading prose.
- mechanism — as catalogued this is a cost-timing rationale rather than a mechanism; the mechanisms are FORMAL-01, -04, and -05.
- source — secondary account of a practitioner's stated view, not a primary paper (catalog: mixed).
- cost — high; it is the whole formal-methods adoption, justified.
Case: The methodology already models before building — that is what the
architecture summary and the Spec Reviewer gate are — so the *timing* claim is
convergent. What is adjacent-not-equivalent is the object: a prose design read by
a reviewing agent is checked by judgment, and a formal model is checked by a
tool, which is the difference between a reviewer who might notice a hole and a
tool that enumerates them. That distinction matters more, not less, when the
reviewer is an LLM whose misses are correlated with the author's.
Cycle input: No standalone proposal. Carry as the rationale line if FORMAL-01, FORMAL-04, or FORMAL-05 is ever taken up.

## SRE-04 — Maturity-gated, hypothesis-driven fault injection
Bucket: gap
Methodology position: none. Adjacent constraints: `LEXICON.md` §Sessions ("Nothing here authorizes acting against a deployed or production system"); `policies/commit-and-change-control-policy.md` §Tier 2 (irreversible operations are consequential); `context-sets/production-grade-software.md` §Failure mode thinking (asked, not tested)
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source m · cost h
Score reasons:
- relevance — the methodology asks "can the system recover?" and answers from reasoning; the answer is never tested. But no system under this methodology is currently operating at a scale that earns the exercise.
- mechanism — a stated hypothesis, contained blast radius, a rollback plan, and a maturity gate on production runs; unusually well specified.
- source — practitioner-guide synthesis rather than a primary standard (catalog: mixed), though the maturity-gating element is distinctive.
- cost — high: it needs a production system, monitoring that works, and an operator with time.
Case: An unfilled slot whose value is deferred rather than absent. The
methodology's recovery claims are reasoned, not verified — every "can the system
recover?" answer in a change package is an assertion of exactly the kind
`roles/skeptic-risk-agent.md` exists to challenge, and the skeptic has no
mechanism to challenge it with. The maturity-gating half is the part worth
noting now: it is a governance pattern (earn the right to run in production by
demonstrating in staging) structurally identical to the methodology's own
tier-and-evidence instincts, and it is what would make the practice adoptable
without contradicting the standing prohibition on acting against production.
Cycle input: No proposal now. Park behind SRE-02 — a production readiness gate that verifies instrumentation is the precondition for any fault-injection exercise being informative rather than merely destructive.

## DESIGNDOC-03 — Write the future press release before building
Bucket: gap
Methodology position: `specs/prd-template.md` §1 Problem and intent, §2 Users and use cases, §5 User outcomes and measurement
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source h · cost l
Score reasons:
- relevance — real but not acute: the PRD already forces the customer-value question, and this project's PM and its user are frequently the same person, which is the condition the practice is least needed in.
- mechanism — a mock press release written from a future date, in customer language; unambiguous and checkable.
- source — an account from authors who developed the practice at Amazon (catalog: strong).
- cost — low: one optional section.
Case: The PRD asks for the same information in analytic register — problem,
users, outcomes, measurement. What the PR/FAQ adds is a *forcing function on
register*: writing the outcome in language a customer would recognize surfaces
vagueness that a goals list absorbs comfortably. That is a genuine partial gap
rather than a restatement, but its value here is smaller than in a large
organization, because the PRD is agreed by the same person who holds the product
intent, so the alignment failure the practice targets has fewer places to hide.
Cycle input: Low priority. If proposed, propose it as an optional PRD front-section rather than a required one, and only if a real instance of vague intent surviving §1 and §5 is observed first — per the refine-on-counterexample rule proposed under FORMAL-05.

## FORMAL-04 — Model-based test generation from formal behavioral models
Bucket: gap
Methodology position: none. Adjacent: `roles/test-designer-agent.md` (tests derived from ACs by an agent, deliberately a different agent from the Coder); `context-sets/ai-native-engineering.md` §Team model (Test Designer / Coder separation is mandatory)
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source m · cost h
Score reasons:
- relevance — real: the methodology's independence guarantee currently rests on two agents being different instances, which is a weaker independence than a generator provides.
- mechanism — traverse the model to a coverage criterion, emit inputs plus oracles; fully specified.
- source — practitioner explainer corroborated by a peer-reviewed derivation method (catalog: mixed).
- cost — high: someone must author and maintain the behavioral model, and the model becomes a second spec.
Case: An unfilled slot with a real argument and a real counter-argument, both
worth stating. For: generated tests are independent of the implementing agent by
construction, which is a stronger form of the property Test/Coder separation
exists to buy. Against: the blind spot does not disappear, it relocates into the
model, and the model is authored by an agent — so the methodology would be
trading a checkable separation for an unchecked artifact unless the model itself
is gated.
Cycle input: No proposal at this cost. If taken up, it must be sequenced behind a decision on who authors and gates the behavioral model, because an ungated model reintroduces the blind spot it was adopted to remove.

## DBC-02 — Contract inheritance: weaken preconditions, strengthen postconditions
Bucket: gap
Methodology position: none. The corpus holds no position on language-level or object-oriented design rules.
Coverage: none
Scores: relevance m · mechanism h · source h · cost l
Score reasons:
- relevance — real (an agent specializing a type and tightening its precondition silently breaks existing callers) but narrow and language-dependent; it is not among the failure modes this methodology is organized around.
- mechanism — an exact rule with an unambiguous violation test.
- source — implemented, directly-verifiable library behavior consistent with Meyer's original rule (catalog: strong).
- cost — a single reviewer-checklist line; near zero.
Case: An unfilled slot, but a small one, and it is entirely downstream of
DBC-01 — the inheritance rule has nothing to govern until contracts are stated.
Its independent value is as a Reviewer Agent check in codebases that use
inheritance, where an LLM's instinct to "tighten validation" in an override is
exactly the wrong direction.
Cycle input: Do not propose independently. If DBC-01 is taken up, fold the substitutability rule into `roles/reviewer-agent.md` as one checklist line.

## TEST-05 — Transformation Priority Premise
Bucket: gap
Methodology position: `context-sets/spec-and-change-discipline.md` step 6 ("The Coder implements only as much as needed to turn the failing tests green"); `roles/coder-agent.md` §Responsibilities ("keep changes small and coherent")
Coverage: adjacent (partial gap)
Scores: relevance l · mechanism h · source h · cost m
Score reasons:
- relevance — low against this workflow: TPP presupposes a human working a red-green loop in small increments, and an LLM Coder handed a failing suite writes the whole implementation in one pass, so the transformation sequence it constrains does not occur.
- mechanism — a ranked transformation list with a strict most-specific-first rule; entirely precise.
- source — the originating author's own formulation, corroborated independently (catalog: strong).
- cost — moderate, and mostly the cost of changing how the Coder is prompted to work.
Case: An unfilled slot whose premise this workflow largely does not satisfy. The
methodology holds the minimal-implementation half ("only as much as needed") and
not the ordering half, so it is a partial gap on paper. In practice, the failure
TPP prevents — premature overgeneralization forcing a rewrite — shows up
differently with an LLM Coder: not as a wrong transformation order but as a
whole speculative abstraction delivered at once. The corresponding control is
scope discipline, which the methodology already has, and traceability, which
SAFETY-05 proposes. Recorded for completeness, not proposed.
Cycle input: None. Note if the workflow ever moves to incremental agent-driven red-green loops, the relevance grade changes and this should be re-scored.

## FORMAL-01 — Temporal vs. structural specification split
Bucket: gap
Methodology position: none. `specs/trd-template.md` §6 asks how the system fails at the system level, in prose; nothing selects a verification formalism.
Coverage: none
Scores: relevance l · mechanism h · source h · cost h
Score reasons:
- relevance — the failure modes this methodology is organized around are overclaiming what evidence proves and unverified integration boundaries, not the temporal correctness of concurrent protocols; the projects it governs (a CRM, a transit app) are not distributed-protocol work.
- mechanism — choose the tool by property type; a clear, decidable selection rule.
- source — peer-reviewed comparative study (catalog: strong).
- cost — very high: a new formalism, a new toolchain, and a skill this team does not have.
Case: A genuine unfilled slot, but the problem it fills is largely not this
project's problem. Recorded so the vein is not lost: if a future project under
this methodology is concurrent or fault-tolerant, this is the entry that says
which tool answers which question.
Cycle input: No proposal. Park; revisit only if a project in scope becomes concurrency- or protocol-shaped.

---

# Convergences (14)

A shared *mechanism* with a position this methodology reached independently — not shared vocabulary. Ordered by what a cycle input could still add: entries with an unheld residue first, pure confirmations last.

## SAFETY-06 — Goal Structuring Notation assurance case
Bucket: convergence
Methodology position: `context-sets/testing-and-verification.md` §Confidence ledger (Claim / Evidence / Boundary / Deferred verification); `operating-model.md` §Change package (12 items); `policies/release-readiness-policy.md` §Release package; `README.md` key principle #1 ("Manage the proof, not the code"); `skills/evidence-review.md` §Procedure (list claims, match each to evidence, identify unsupported claims)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost m
Score reasons:
- relevance — this methodology's entire product is an argument that a change is safe to release; it has the artifact and not the argument structure.
- mechanism — goal, strategy, context, evidence, decomposed until each branch terminates in a direct evidence reference; a fully specified notation.
- source — the originating academic paper plus an independent corroborating summary (catalog: strong).
- cost — moderate: an additional artifact, though it largely restructures material the change package already contains.
Case: Real convergence on the load-bearing idea — an explicit, reviewable
artifact connecting claims to evidence, produced so a release decision rests on
something inspectable rather than on assurance. The confidence ledger is
recognizably the same instinct, arrived at independently. **What GSN has and the
ledger does not is the *strategy* node: the stated inference from a top-level
claim down to its sub-claims.** The methodology's ledger is flat — a list of
(claim, evidence, boundary) triples — and the step from "here are eleven
verified claims" to "therefore this is safe to release" is made by the Release
Manager in prose and by Dave in judgment, with the inference itself never
written down. That is the one step in the whole evidence chain that is currently
unreviewable, and it is the step where an overclaim would hide: a complete
ledger with a bad inference over it looks exactly like a complete ledger. Since
the methodology's own thesis is that the inference from evidence to release is
the human's real work, making that inference an artifact is unusually on-target.
Cycle input: Propose evaluating a goal-structured layer over the change package — top claim ("this change is releasable"), the stated strategies that decompose it (e.g. "by covering each affected Top K journey", "by discharging each material boundary"), each branch terminating in a ledger entry. Test it on one past change package before proposing it as a requirement; the failure mode to watch for is ceremony, which `policies/commit-and-change-control-policy.md` already warns is how a gate stops being read.

## LLM-12 — Separate-agent adversarial critic to counter self-review bias
Bucket: convergence
Methodology position: `context-sets/ai-native-engineering.md` §Team model ("Whoever produces an artifact does not approve it"; Test Designer/Coder and Architect/Spec Reviewer separations mandatory); `roles/spec-reviewer-agent.md` §Activation ("may not be the same agent instance that drafted the document under review"); `policies/agent-review-policy.md` §Required review posture ("the agent that wrote the code may have optimized for green tests"); `skills/spec-review-cycle.md` §Review artifact schema (structured verdict, blocking/non-blocking, per-finding Claim/Location/Evidence/Consequence/Fix)
Coverage: equivalent on the separation mechanism; one sub-claim adjacent (below)
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — self-preference bias is the failure this entire methodology's review architecture is built to defeat.
- mechanism — maker and checker split across separate context, instructions, and ideally models, with a structured verdict and bounded retry rounds.
- source — vendor-authored guides, though both independently cite the same measured phenomenon (catalog: mixed).
- cost — near zero for the residue identified below.
Case: Among the strongest convergences in the scan, and independently derived —
the methodology reached the self-preference rationale in its own words ("the
agent that wrote the code may have optimized for green tests") and built three
mandatory separations plus a structured-verdict schema on it. **One sub-claim is
adjacent and is the finding worth acting on:** the practice specifies a
*different model*, and `context-sets/ai-native-engineering.md` explicitly
permits the opposite — "The same underlying model may fill multiple roles across
a project, but the role boundaries must remain explicit." The external evidence
says self-preference is a property of the *model*, not of the instance, so a
fresh instance of the same model is a weaker checker than the separation implies.
This matters here because it gives the live `OPEN-ITEMS.md` §"Model selection by
role" item a second axis it does not currently have: that item reasons entirely
about cost versus capability, and never considers varying the model for
*independence*. Its criteria — are this role's errors detectable by
construction, do its judgments propagate into canonical documents — are exactly
the criteria that should also decide where instance-separation is insufficient.
The second residue is smaller: bounded retry rounds. The methodology re-gates
until clean with no bound, and the source reports rounds 1–2 capture 75% of the
improvement, which is an argument for a bound but not a strong one.
Cycle input: Propose that the open model-selection item add an independence axis — where a review's independence is load-bearing (Spec Reviewer over a gate document, Skeptic/Risk over a consequential change), the reviewing agent should run a different model from the authoring agent, not merely a different instance. This is a line in a document already queued for revision, not a new mechanism. Do not propose a retry bound; the evidence is thin and unbounded re-gating has not been observed to cost anything here.

<!-- APPEND-POINT -->

## SRE-03 — Standard blameless postmortem artifact
Bucket: convergence
Methodology position: `skills/conversation-retro.md` (fixed schema, evidence-grounded, Evidence separated from Interpretation, feeding changes only through the normal cycle); `docs/global-retro-inbox.md`; `OPEN-ITEMS.md` §"Add retrospective process to the operating model" (live, sourced from a real production escape)
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source h · cost l
Score reasons:
- relevance — the open item exists because a real failure reached `origin/main` with 225 passing tests and produced no structured artifact.
- mechanism — a fixed artifact structure with named, dated, owned corrective actions; each element separately adoptable.
- source — the originating organization's own published practice (catalog: strong).
- cost — low: the schema and the storage convention already exist and would be extended, not built.
Case: Substantial convergence on mechanism — fixed schema, evidence-grounded,
stored in-repo, feeding process change through a governed route rather than
directly ("Retros are an input to change, not a change mechanism"). Three
elements are adjacent rather than equivalent and are the partial gap. **Trigger:**
the retro fires at the end of a *conversation*; a postmortem fires on an
*incident*. The methodology's live open item is precisely about an incident with
no conversation boundary attached, so the existing trigger would not have caught
it. **Corrective actions:** the retro schema ends at "candidate methodology
changes"; the postmortem requires each action to carry an owner and a due date,
and that is the field that converts a retrospective into a change. **Impact
assessment:** absent entirely. Blamelessness itself is the one element that
transfers least — the participants here are agents — though the underlying rule
(explain what happened and why, not who) is already how `decisions/log.md`
entries are written.
Cycle input: Propose discharging the open retrospective item by adding an incident trigger and an owned/dated corrective-action section to `skills/conversation-retro.md`, or by a sibling skill if the conversation-scoped and incident-scoped artifacts should stay separate. Note the retro skill routes its own revisions through a full cycle regardless of size, so this cannot take the expedited path.

## LLM-10 — Failure-driven regression dataset growth
Bucket: convergence
Methodology position: `context-sets/spec-and-change-discipline.md` (the true-red-gate paragraph and the derived-field checklist, each added by name and date after a specific escape — "Confirmed by Dave, 2026-07-24, closing the P3 contact-merge review"; "Added 2026-07-24, closing the P3 contact-merge review — F1"); `decisions/log.md` (append-only, one entry per ruling); `skills/conversation-retro.md` §Retro schema (candidate methodology changes); `docs/global-retro-inbox.md`
Coverage: adjacent (partial gap)
Scores: relevance h · mechanism h · source m · cost m
Score reasons:
- relevance — a failure that recurs after being diagnosed is the cheapest possible defect to prevent and the most embarrassing to repeat.
- mechanism — every diagnosed failure leaves a trace, a label, a dataset row, and a scorer; four artifacts, of which this methodology produces one.
- source — the same individual practitioner blog as LLM-09, uncorroborated in this pass (catalog: mixed).
- cost — moderate, and dependent on LLM-02's harness for the scorer half.
Case: Genuine convergence on the discipline and a precise gap on the mechanism.
This repo does honor the rule that a diagnosed failure leaves something
permanent behind — the two additions to `spec-and-change-discipline.md` name the
review that produced them, which is exactly the practice — and the decision log
generalizes it. **What it leaves behind is a prose rule an agent must read and
remember to apply, where the practice requires a scorer that runs.** The
difference is the difference between the corpus and a test suite, and this
methodology knows what that difference is worth everywhere except when the
subject is itself. The P3 contact-merge escape is the case in point: it produced
two well-written paragraphs, and if the same blind spot recurs, nothing fires —
a reviewer has to notice, again.
Cycle input: Record the convergence. Propose that the LLM-02 harness's first golden cases be drawn from the failures the corpus already documents — the P3 derived-field escape and the missing-module red-gate — so the case set starts from real diagnosed defects rather than invented ones, and each documented escape gains a scorer to go with its paragraph.

## DESIGNDOC-01 — ADR as single-decision, in-repo record
Bucket: convergence
Methodology position: `policies/decision-log-policy.md` (whole document); `decisions/log.md`; `context-sets/base.md` §Required behavior (the consult obligation); `docs/global-retro-inbox.md` 2026-08-04 (the originating sketch)
Coverage: equivalent on the mechanism; one element differs by deliberate choice, one is missing
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — a decision that cannot be found is re-litigated, and with agents it is re-litigated by every session that meets the same fork.
- mechanism — one record per significant decision, plain text, in the repo beside the work it governs, superseded rather than edited.
- source — secondary account of Nygard's original proposal (catalog: mixed), though the format is independently well attested.
- cost — already held; zero.
Case: Convergence on mechanism, with a documented divergence that is a
*deliberate opposite choice* rather than an oversight — and it is worth flagging
as arguably a narrow contradiction. ADR is one file per decision;
`policies/decision-log-policy.md` is explicit that this repo chose the reverse
("One file, not one file per entry — the single file *is* the index"), and
`docs/global-retro-inbox.md` shows the one-file-per-decision form was the
original sketch and was rejected. That choice buys grep-ability and a guaranteed
next-ID rule, and it is well argued; nothing here should reopen it. **The
genuinely missing element is different: ADR records decision, context, *and
consequences*, and this repo's entry format has no consequences field**
(ID, Date, Decision, Context, Supersedes). The consult obligation in
`context-sets/base.md` asks an agent to honor a decision without telling it what
the decision costs, so an agent meeting a live constraint cannot tell whether it
is a known accepted consequence or a new problem — which is exactly the
distinction the `docs/global-retro-inbox.md` sketch wanted (`accepted-risk`
entries so "an agent rediscovering known problem X ... should find the entry and
stand down").
Cycle input: Propose adding a consequences (or accepted-cost) field to the `policies/decision-log-policy.md` entry format. Do not reopen the one-file question. Coordinate with DESIGNDOC-06, which proposes a second field on the same format — one cycle, not two.

## SAFETY-01 — Assurance-level scaling
Bucket: convergence
Methodology position: `policies/commit-and-change-control-policy.md` §Tier 1 / §Tier 2 (two-tier release gate); `operating-model.md` §Change flow ("Use a lighter process for routine changes"); `context-sets/base.md` §Standard response shape (meaningful vs. trivial change); `OPEN-ITEMS.md` §"~~A8 — Define 'meaningful change'~~" (resolved)
Coverage: equivalent on the mechanism; one axis differs (below)
Scores: relevance h · mechanism h · source h · cost l
Score reasons:
- relevance — uniform rigor everywhere is unaffordable for a single operator, and unscaled rigor is how a gate stops being read; the methodology says so in as many words.
- mechanism — a discrete, pre-assigned class determines the required process; concrete and enforceable.
- source — vendor explainer, but the level-scaling mechanism is independently corroborated across DO-178C, ISO 26262, and IEC 61508 (catalog: mixed, corroboration noted).
- cost — already held; zero.
Case: Genuine independent convergence on a mature mechanism. The methodology's
two-tier gate does what DAL/ASIL/SIL do — a change's class is fixed in advance
and determines the process it must clear — and it reached the same anti-ceremony
rationale ("do not manufacture approval ceremony for routine work"). **One axis
is genuinely different and is the interesting residue:** assurance levels are
assigned to *components*, and this methodology assigns tiers to *changes*. A
component-level assignment says "this code path is always high-rigor"; a
change-level assignment re-derives that judgment every time, from a list of
touched surfaces. The methodology is already half-way across that line — the
error-budget trigger ("any change to a code path for a Top K user journey whose
SLO error budget is at or below 20% remaining") is a component-flavored rule
wearing change-level clothing.
Cycle input: Propose evaluating whether the consequential class should admit standing component-level designations alongside the change-level surface list — i.e. whether a project's TRD may declare certain code paths permanently consequential. Note this interacts with SAFETY-03, which supplies the classification basis.

## DESIGNDOC-05 — Named shepherd drives open-ended proposal discussion to closure
Bucket: convergence
Methodology position: `roles/chief-of-staff.md` §Activation behavior and §Handling execution-session reports ("Work the queue one item at a time. Do not leave an item until every question it raises is answered"); `skills/spec-review-cycle.md` §Cycle directive format ("one decision entry per finding (including rejections)"); `context-sets/ai-native-engineering.md` §Team model ("Whoever produces an artifact does not approve it")
Coverage: adjacent (partial gap)
Scores: relevance m · mechanism h · source h · cost l
Score reasons:
- relevance — a proposal with no owner of convergence stalls; this methodology has a role whose entire purpose is preventing that, so the acute form of the problem is already handled.
- mechanism — a named non-author responsible for keeping discussion moving, ensuring every concern is answered, and moving to a fixed final comment period.
- source — the Rust project's own governing process document (catalog: strong).
- cost — low.
Case: Strong convergence on two of three elements, independently reached. The
**named non-author driver** is the Chief of Staff, and the author/driver
separation is the same rule the corpus states generally as "whoever produces an
artifact does not approve it." The **every-concern-answered** guarantee is
enforced harder here than in the RFC process: a cycle directive is *invalid*
without one decision entry per finding, rejections included, so a concern cannot
be closed by being ignored. The third element is adjacent — there is no **fixed
final comment period**. Closure comes from Dave's sign-off, which for a single
operator is faster and probably better; the residue an FCP would add is a
bounded window in which a late objection is still in order, which this
methodology currently handles by re-gating rather than by a waiting period.
Cycle input: Record as confirmation. No FCP proposed — the mechanism exists to manage many reviewers, and there is one.

## SRE-01 — Error-budget consumption thresholds trigger policy escalation
Bucket: convergence
Methodology position: `policies/commit-and-change-control-policy.md` §Tier 2 ("any change to a code path for a Top K user journey whose SLO error budget is at or below 20% remaining"); `OPEN-ITEMS.md` §"~~Error budget exhaustion as a consequential-change trigger~~" (RESOLVED); `BACKLOG-v2.md` §Error budget exhaustion as a consequential-change trigger (its origin); `context-sets/testing-and-verification.md` §Production-verified
Coverage: equivalent
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — reliability debt that does not change how risky work is governed is reliability debt nobody acts on.
- mechanism — a numeric budget threshold automatically escalates the review regime; identical in kind to what is written.
- source — vendor guide, but the threshold-triggered-escalation pattern is concrete (catalog: mixed).
- cost — already held; zero.
Case: Textbook independent convergence, and the paper trail proves it was
independent: the trigger entered through `BACKLOG-v2.md`, was decided in
`OPEN-ITEMS.md`, and landed in the commit policy, with no reference to the SRE
literature anywhere in the chain. Same mechanism, same rationale, different
threshold and different escalation (Google's example tightens approval at 64%
consumed; this methodology moves a change into the consequential class at 20%
budget remaining). Worth recording precisely because it is the strongest
available evidence that this methodology's governance instincts land where a
mature tradition landed.
Cycle input: Record as confirmation. One optional refinement: the external pattern uses *graded* thresholds with escalating responses, where this methodology has a single binary trip point — consider whether a second, earlier threshold with a lighter response is worth having.

## LLM-01 — Context as an evolving, curated playbook
Bucket: convergence
Methodology position: `context-sets/` (the whole directory, plus `MANIFEST.md` §Context-set bundles); `roles/context-quality-reviewer.md` (evaluates the corpus specifically as LLM context artifacts); `skills/conversation-retro.md` → `docs/global-retro-inbox.md` → `skills/spec-review-cycle.md` (the reflect-and-curate loop); `policies/document-metadata-policy.md` §Agent behavior
Coverage: equivalent on the mechanism; one element differs by deliberate choice
Scores: relevance h · mechanism h · source h · cost l
Score reasons:
- relevance — a static prompt cannot absorb what a session learns, and this project's entire product is the corpus that gets loaded.
- mechanism — generate, reflect on what happened, curate the context accordingly; a named cycle with named stages.
- source — an arXiv technical paper naming a specific mechanism (catalog: strong).
- cost — already held; zero.
Case: Deep convergence, independently reached and in one respect further
developed. The corpus *is* an evolving playbook: it is refined by reflection on
execution (retros and the global inbox), it has a role whose only job is judging
it as context rather than as prose, and it has metadata governing which
documents an agent may load as authority. The one element that differs is
deliberate and should not be read as a gap: ACE curates **automatically at
runtime**, and this methodology curates only **through a gated review cycle** —
`docs/global-retro-inbox.md` states the rule as "no second door," and
`skills/conversation-retro.md` routes retro-surfaced changes through a full
cycle even where a shortcut would otherwise apply. That is a considered trade of
adaptation speed for the guarantee that no agent silently edits its own
governing context, and it is the right trade for a corpus that defines gates.
Cycle input: Record as confirmation. Flag one live tension for triage rather than change: the corpus is curated for correctness and never measured for effect, which is LLM-02's finding.

## SDD-02 — Spec-to-code pipeline via atomic task decomposition
Bucket: convergence
Methodology position: `context-sets/spec-and-change-discipline.md` §The canonical sequence (steps 1–6); `operating-model.md` §Change flow (steps 1–5); `roles/chief-of-staff.md` §Decomposition and handoff; `context-sets/ai-native-engineering.md` §Separation of concerns
Coverage: equivalent
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — an agent handed a whole spec and told to build it is the exact over-scoping failure the practice names.
- mechanism — a named intermediate artifact between spec and code is concrete and its absence is detectable.
- source — vendor blog, but the three-stage pipeline is a checkable structural claim (catalog: mixed).
- cost — already held; zero.
Case: Same mechanism, reached independently and with more structure: the
methodology interposes *two* derivation steps the source has one of — the
per-change architecture summary (`roles/architect-agent.md`, derived from the
TRD, the artifact an Issue is cut from) and the tranche decomposition doc
(`roles/chief-of-staff.md`: "smallest independently executable units, in
dependency order"). It also adds a staleness guard the source lacks: the decomp
doc pins the PRD/TRD SHAs it derived from (DEC-000070).
Cycle input: Record as confirmation; no change proposed.

## SDD-01 — Spec as authoritative source artifact
Bucket: convergence
Methodology position: `policies/source-of-truth-policy.md` §Canonical order; `operating-model.md` §Source of truth; `README.md` principle #8; `context-sets/spec-and-change-discipline.md` §Core philosophy
Coverage: equivalent on the core mechanism; adjacent on one sub-claim (below)
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — implementation drifting from unstated intent is the failure this whole methodology is built against.
- mechanism — artifact precedence plus a declared derived/canonical ordering is concrete and checkable.
- source — vendor content, but the precedence claim is mechanical rather than promotional (catalog: mixed).
- cost — already fully held; adoption cost is zero.
Case: Shared mechanism, not shared vocabulary — the spec is authored before
implementation, downstream artifacts (ACs, architecture summary, Issues) are
*views* onto it, and a derived artifact contradicting a canonical one is a hard
stop rather than a merge conflict. The methodology arrived at this independently
and states it more strongly than the source does (the hard-stop rule has no
counterpart in the cited SDD material). **One sub-claim is adjacent, not
equivalent, and should not be collapsed:** SDD-01 specifies a *structured,
machine-readable* spec from which code is *generated*. This methodology's specs
are prose Markdown templates (`specs/prd-template.md`, `specs/trd-template.md`),
and it derives *tests* from ACs, never code from spec. That residue is carried
by SDD-04, which is filed as a gap.
Cycle input: Record as confirmation; no change proposed here. The machine-readable/generated residue is proposed under SDD-04.

## TEST-02 — Acceptance tests written before development starts
Bucket: convergence
Methodology position: `context-sets/spec-and-change-discipline.md` §The canonical sequence (steps 4–6); `policies/testing-policy.md` §Red-gate; `policies/commit-and-change-control-policy.md` §Red-gate ("applies to both tiers"); `roles/test-designer-agent.md`
Coverage: equivalent, and the methodology's form is strictly stronger
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — a test written after the implementation describes the code rather than the requirement; that is the failure both traditions are built around.
- mechanism — write acceptance tests before development of the feature begins; unambiguous and checkable.
- source — a tertiary encyclopedic source, though the ordering claim is standard (catalog: mixed).
- cost — already held; zero.
Case: Equivalent on the ordering mechanism, and the methodology adds two things
ATDD does not require. It requires the tests to be **run and confirmed failing**
before implementation, and it goes further still in insisting the failure be
*behavioral* rather than a missing-module error — a distinction ATDD has no
counterpart for and which this repo learned from a specific escape
(`context-sets/spec-and-change-discipline.md`, the true-red-gate paragraph). And
it requires **different agents** for test authorship and implementation, where
ATDD's collaborative authorship deliberately puts the same people on both. The
collaborative element is the one ATDD has that this does not, and it is the same
question TEST-01 and SDD-04 raise.
Cycle input: Record as confirmation. No change proposed.

## LLM-07 — Decomposition authority stays with the orchestrator
Bucket: convergence
Methodology position: `roles/chief-of-staff.md` §Decomposition and handoff (CoS reads the whole spec and decomposes; "Does not execute packages") and §Prompt generation; `context-sets/ai-native-engineering.md` §Separation of concerns; `skills/directive-dispatch.md` §Writing the directive file ("the executor needs the file and the repository, nothing from the conversation")
Coverage: equivalent
Scores: relevance h · mechanism h · source m · cost l
Score reasons:
- relevance — a sub-agent scoping its own sub-task is scoping from a fragment, and it cannot know what it cannot see.
- mechanism — decomposition decisions stay with the context-holding orchestrator and are never delegated downward; a falsifiable architectural rule.
- source — a framework-vendor blog, though the design rule is specific rather than generic (catalog: mixed).
- cost — already held; zero.
Case: Precise convergence, independently reached, and the methodology's version
is more explicit about *why*: the Chief of Staff reads the agreed PRD and TRD in
full because "proposals derive from whole-spec comprehension, not a fragment,"
and executors receive self-contained directives specifically so they cannot and
need not reason about scope. The one difference is directional and favors the
methodology — it also forbids the orchestrator from executing, which the source
does not require, so the separation is enforced from both ends.
Cycle input: Record as confirmation. No change proposed.

## LLM-03 — Explicit agent-facing context files beyond source code
Bucket: convergence
Methodology position: the entire `/ai/` corpus; `CLAUDE.md` and `AGENTS.md` (adapters); `boundaries/vendor-tooling-boundary.md`; `policies/source-of-truth-policy.md` §Canonical order (the portable/adapter split)
Coverage: equivalent, and the methodology's form is stronger
Scores: relevance h · mechanism h · source h · cost l
Score reasons:
- relevance — architectural patterns and team conventions are exactly what an agent cannot infer from code, and inferring them wrongly is silent.
- mechanism — maintain repo-level agent-facing documentation distinct from source and from human docs.
- source — an empirical study of the practice across real repositories (catalog: strong).
- cost — already held; zero.
Case: The practice is this project's premise, so convergence is total, and the
methodology holds two refinements the study does not cover: the portable
source-of-truth versus vendor-adapter split
(`boundaries/vendor-tooling-boundary.md`: "Context Sets are the constitution.
Vendor artifacts are deployment targets"), and lifecycle metadata that tells an
agent which documents are authoritative right now
(`policies/document-metadata-policy.md` §Agent behavior). Recorded as
confirmation with no residue.
Cycle input: None.

---

# No-action (2)

Out of scope (failed problem relevance), or a duplicate of a position already fully held.

## SDD-03 — Spec-first alignment before AI code generation
Bucket: no-action
Methodology position: `context-sets/spec-and-change-discipline.md` §The canonical sequence ("No implementation begins until specs and ACs for that work are complete"); `specs/prd-template.md` §6 Acceptance criteria; `MANIFEST.md` §Context-set bundles (the shared-context mechanism)
Coverage: equivalent
Scores: relevance h · mechanism l · source l · cost l
Score reasons:
- relevance — prompt-first-align-later is a real and common failure mode.
- mechanism — an ordering assertion with no mechanism beyond what SDD-01 and SDD-02 already supply.
- source — vendor content-marketing, the weakest sourcing in the SDD vein (catalog: mixed, kept only for the falsifiable ordering claim).
- cost — nothing to adopt.
Case: Duplicate of a position already fully held. The align-before-generate
ordering is SDD-01 and SDD-02 restated as a slogan; the "guardrails and shared
context up front" half is the context-set bundle mechanism. Nothing here is a
mechanism this methodology does not already run.
Cycle input: None.

## DESIGNDOC-04 — Silent-read-first review meeting
Bucket: no-action
Methodology position: n/a — out of scope
Coverage: n/a
Scores: not graded (failed problem relevance, per the rubric)
Case: Out of scope. The practice addresses a failure mode of multi-attendee
review meetings: attendees who have not read the document shaping the discussion
anyway. This operating model has no meetings. Its review events are an agent
reading a document and emitting a findings artifact, and Dave reading a git diff
— in both cases reading the whole artifact is the activity, not a precondition
someone might skip. The nearest analogue in the corpus,
`roles/chief-of-staff.md`'s "Do not info-dump the report and let Dave find what
matters," is a rule about *what* is surfaced, not about reading before speaking,
so it is neither convergence nor the same problem.
Cycle input: None.

---

# Summary

## Counts

| Bucket | Count |
|---|---|
| Contradiction | 3 |
| Gap | 31 |
| Convergence | 14 |
| No-action | 2 |
| **Total** | **50** |

Of the 31 gaps, 22 are **partial** gaps (coverage `adjacent`) and 9 are complete
(coverage `none`). Of the 14 convergences, 8 carry an unheld residue recorded as
a cycle input; 6 are pure confirmations proposing no change.

## Highest-value findings across all buckets

Seven, in the order I would triage them.

1. **SAFETY-04 (contradiction) — outcome-based compliance versus a mandated
   lifecycle.** The methodology states an outcome-based thesis ("manage the
   proof, not the code") and implements a method mandate (nine stages, no
   working ahead, red-gate and Test/Coder separation mandatory on all tiers).
   Six decision-log entries, DEC-000010 through DEC-000060, are in sequence
   rulings that carve routes around that mandate. IEC 62304's posture — specify
   the required tasks and evidentiary outcomes, mandate no lifecycle — would
   have admitted each of those cases as an instance rather than an exception.
   Highest stakes in the scan and the only finding that reaches the spine.

2. **LLM-04 (gap) — no position on untrusted ingested content.** The corpus has
   no rule anywhere about content that arrives as data rather than authority,
   and the ingestion points are all already written into it: pasted Claude Code
   reports (`roles/chief-of-staff.md`), GitHub Issues, Track B downloads, MCP
   tool output, fetched research documents. Cheapest high-relevance fix in the
   catalog — a required-behavior line and a delimiter convention.

3. **TEST-04 (gap) — mutation testing.** The methodology diagnoses the problem
   precisely in four documents ("tests may pass while proving less than
   claimed"; "the agent that wrote the code may have optimized for green tests";
   coverage is a weak signal) and prescribes only a judgment substitute. Kill
   rate is the one mechanical measurement of exactly that quantity. The best
   fit-to-stated-fear in the scan.

4. **SRE-06 (gap) — toil measured against a ceiling.** The operator's attention
   is this methodology's declared scarce resource and the justification for
   nearly every mechanism in it, and nothing measures it. Very low cost, high
   relevance, strong source. A methodology whose core rule is "agent claims
   require evidence" currently runs its central premise on none.

5. **SAFETY-06 (convergence, partial) — the assurance-case *strategy* node.**
   The confidence ledger is GSN's instinct reached independently, but flat: the
   inference from "here are eleven verified claims" to "therefore releasable" is
   never written down, and that is the one step in the evidence chain where an
   overclaim would hide undetected.

6. **LLM-02 (gap) — evaluation-driven development for the corpus itself.** Two
   live items are blocked on the same missing harness: the skill-compression
   hypothesis (`docs/global-retro-inbox.md` 2026-08-07, explicitly untestable as
   written) and the model-tier demotion evidence step (`OPEN-ITEMS.md`, which
   demands evidence and has no mechanism to produce it). High cost, but it
   unblocks work already queued.

7. **DESIGNDOC-06 (gap) — an alternatives-rejected field on the decision-log
   entry format.** One field, near-zero cost, directly serving the log's own
   stated purpose: an agent that finds only the choice and not the rejections
   proceeds to re-raise the rejected option, which is the failure the consult
   obligation exists to prevent. Practice already exceeds the schema
   (DEC-000080, `MANIFEST.md`); the field would make it consistent.

## Ambiguous classifications — flagged rather than forced

Six. Each is recorded in the bucket I judged more defensible, with the competing
reading stated in its Case.

- **DBC-04 (filed gap; arguably convergence).** Read as a principle — one owner
  per fact, delete the redundant copy — the methodology holds it hard. Read as
  the practice catalogued — validation-check allocation in code — it holds
  nothing. Filed as a gap because the object differs and collapsing it would
  license an unsupported "already covered."
- **SAFETY-02 (filed gap; arguably contradiction).** The flat contradiction
  reading would be a strawman — the red-gate *is* verification before
  implementation. What is genuinely absent is configuration management and any
  continuously-running review. The sequencing question proper is carried by
  SAFETY-04; triage the two together.
- **LLM-06 (filed contradiction; arguably a different object).** The methodology's
  no-second-copy rule governs *source documents*, and the placement heuristic
  governs *assembled context*. Filed as a contradiction because one rule
  currently has to serve both and they pull opposite ways — which
  `docs/global-retro-inbox.md` already half-recognizes.
- **DESIGNDOC-01 (filed convergence; contains a deliberate opposite choice).**
  ADR is one file per decision; `policies/decision-log-policy.md` chose the
  reverse explicitly and argued it well. Not filed as a contradiction because
  the *mechanism* — in-repo, plain-text, per-decision, superseded not edited —
  is fully shared, and the granularity difference should not be reopened.
- **LLM-12 (filed convergence; one sub-claim arguably contradicts).** The
  practice specifies a different *model* for the checker;
  `context-sets/ai-native-engineering.md` explicitly permits the same model
  across roles. Filed as convergence because the source says "ideally," not
  "must" — but the residue is the actionable part of the finding.
- **SAFETY-01 versus SAFETY-03.** One tradition's level-scaling is split across
  two buckets: the *scale-rigor-to-a-class* mechanism is convergence, and the
  *harm-severity basis plus documented approved classification* is a gap. Split
  deliberately rather than collapsed; if Dave reads them as one practice, they
  should be triaged as one item.

## Proposals that should be packaged together

Raising these separately would produce overlapping cycles.

- **Boundary closure from both sides:** OTHER-01 (consumer-driven contract
  testing) + LLM-08 (validator-guided repair). Same boundary, opposite
  directions.
- **Property-based testing bundle:** FORMAL-02 + TEST-03 (shrinking arrives with
  the library and is not independently adoptable).
- **Decision-log entry format:** DESIGNDOC-06 (alternatives rejected) +
  DESIGNDOC-01 (consequences). One revision to one format. DEC-000050 places
  `policies/decision-log-policy.md` outside the gate-document class, so the
  doc-only cycle is available if Dave asks for it.
- **The duplication/placement tranche:** LLM-06 + DBC-04 + the queued
  drift-audit item in `docs/global-retro-inbox.md`. One rule must serve source
  documents and assembled bundles both.
- **The evaluation harness:** LLM-02 (the harness) + LLM-09 (its delivery form)
  + LLM-10 (its first golden cases, drawn from failures the corpus already
  documents) + LLM-05 (whose adoption should be a trial the harness eventually
  arbitrates).
- **Lifecycle structure:** SAFETY-04 + SAFETY-02, per the ambiguity note above.

## Scope and limits of this pass

- **Coverage is the catalogs', not the field's.** Phase 1's gap pass reported
  that every tradition still converted queries to finds when its search ceiling
  hit, so no tradition can be called saturated. Absence of a practice from these
  50 is not evidence it does not exist.
- **Source strength was carried forward, not re-verified.** No source was
  re-read in this phase; the `source` axis restates the catalog's own assessment,
  and where the catalog flagged a claim as the cataloguer's inference rather than
  the source's (FORMAL-05, LLM-06), the finding says so.
- **Two practices are graded against a workflow that may change.** TEST-05's low
  relevance rests on LLM Coders not working incremental red-green loops, and
  LLM-11's cost rests on compaction being a vendor concern. Both should be
  re-scored if those hold differently.
- **Nothing here is a recommendation to adopt.** Every "cycle input" is phrased
  as a proposal for a review cycle to consider, several deliberately propose no
  change, and six convergences propose nothing at all.
