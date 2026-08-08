# External Methodology Scan — Phase 1 Gap-Pass Catalog

Findings-only catalog. Second discovery pass against `methodology-scan-catalog.md` as
known-set. Same traditions, diversified queries (failure-mode framings, primary-source
framings, alternative vocabulary). No comparison, no adoption judgment.

Track B run (no repository connector) — this file is emitted for the operator to land.

Checkpoint status: run complete. 15/15 searches used (hard ceiling reached). 15 new entries.

---

## SDD-04 — Specification by example: concrete examples as living documentation
Practice: Derive the specification from concrete, collaboratively-authored examples of system behavior rather than abstract prose or schema, then automate those examples into an executable, continuously-revalidated "living documentation" system that stays synchronized with the implementation as it evolves.
Tradition: Spec-driven / spec-first development
Source: Gojko Adzic, "Specification by Example: How Successful Teams Deliver the Right Software" (Manning)
URL: https://www.manning.com/books/specification-by-example ; https://gojko.net/books/specification-by-example/
Source type: primary text
Source quality: strong — originating author's own formulation of the seven-pattern method.
Claim (stated): "An automated specification with examples, still in a human-readable form and easily accessible to all team members, becomes an executable specification." Seven patterns: "Deriving scope from goals, specifying collaboratively, illustrating using examples, refining the specification, automating validation without changing specifications, validating frequently and evolving a documentation system."
Mechanism: Distinct from SDD-01 (structured document as source of truth, consumed once pre-implementation) — here the spec unit is a concrete example, not an abstract structured artifact, and the deliverable is a documentation system kept continuously in sync via ongoing automated re-validation, not a single upfront artifact.

## DBC-03 — Contract-violation type mechanically localizes fault (blame assignment)
Practice: Use which contract clause was violated (precondition vs. postcondition/invariant) to mechanically determine whether the caller or the callee is at fault, narrowing the debugging search space without manual investigation.
Tradition: Design-by-contract
Source: Christos Dimoulas et al., "Correct Blame for Contracts: No More Scapegoating" (POPL 2011); Gary T. Leavens & Yoonsik Cheon, "Design by Contract with JML"
URL: https://www2.ccs.neu.edu/racket/pubs/popl11-dfff.pdf ; http://www.cs.toronto.edu/~chechik/courses05/csc410/readings/jmldbc.pdf
Source type: primary text
Source quality: strong — peer-reviewed papers formalizing the blame mechanism.
Claim (stated): "A precondition failure points to an issue in the caller, which provided invalid arguments... A postcondition failure in a routine signals a bug within the callee itself, as the inputs satisfied the precondition but the output violated the expected result." Blame assignment "comes with enough information to almost always locate the actual source of the bug."

## DBC-04 — Distribute-never-replicate: each check owned by exactly one party
Practice: Assign each correctness check (validation, range check, non-null check, etc.) to exactly one party in an interaction — caller or callee, never both — and remove any redundant duplicate check on the other side, instead of checking defensively everywhere.
Tradition: Design-by-contract
Source: Bertrand Meyer, "Applying Design by Contract"; "A Comparison of Defensive Development and Design by Contract" (ResearchGate)
URL: https://pages.mtu.edu/~aebnenas/teaching/spring2010/cs3141/readings/meyerPDF.pdf ; https://www.researchgate.net/publication/220877942_A_Comparison_of_Defensive_Development_and_Design_by_Contract
Source type: primary text + secondary comparative study
Source quality: strong — Meyer's own formulation, corroborated by an independent comparative study.
Claim (stated): "Distribute, but never replicate... If the contract is precise and explicit, there is no need for redundant checks... introducing redundant code is never a good idea, either because it makes the code harder to understand, or because new bugs are directly introduced in the new checks."
Note: related to DBC-01/02 (same source lineage) but a distinct mechanism — an allocation-of-responsibility rule (remove duplicate checks) rather than the contract-annotation structure itself. Recorded, not merged.

## FORMAL-04 — Model-based test generation from formal behavioral models
Practice: Generate concrete test cases (inputs plus oracles) automatically by traversing an abstract formal behavioral model (e.g., a state machine) according to a chosen coverage criterion, rather than hand-writing test cases.
Tradition: Formal and lightweight-formal methods
Source: Abstracta, "Model-Based Testing Using State Machines"; "Formal Derivation of Finite State Machines for Class Testing" (Springer)
URL: https://abstracta.us/blog/software-testing/model-based-testing-using-state-machines/ ; https://link.springer.com/chapter/10.1007/978-3-540-49676-2_4
Source type: secondary summary + primary text (peer-reviewed chapter)
Source quality: mixed — practitioner explainer corroborated by a peer-reviewed derivation method.
Claim (stated): "The main aspect of model-based testing is to automate the generation of test cases from explicit behavior models such as state machines... Each abstract test case may correspond to one or more specific test cases... they also include the test oracles to automatically evaluate the test execution."

## FORMAL-05 — Counterexample-guided incremental abstraction refinement
Practice: Verify against the coarsest abstract model that could plausibly prove or disprove the property, and add detail to the model only in response to a spurious counterexample that coarse model produced, rather than building a fully detailed model upfront.
Tradition: Formal and lightweight-formal methods
Source: "Counterexample-guided abstraction refinement for symbolic model checking" (Journal of the ACM, CEGAR); "A Survey on Refinement in Formal Methods and Software Engineering"
URL: https://dl.acm.org/doi/10.1145/876638.876643 ; https://www.warse.org/IJATCSE/static/pdf/file/ijatcse16814sl2019.pdf
Source type: primary text
Source quality: strong — foundational peer-reviewed CEGAR paper.
Claim (stated): "Abstract models may admit erroneous ('spurious') counterexamples, and symbolic techniques analyze such counterexamples and refine the abstract model correspondingly... if the abstract model checking generates a counterexample, it should be checked if the counterexample is an actual counterexample for the concrete model."
Inference (mine): Framed here as an adoptable modeling-effort strategy (start coarse, refine only where a counterexample demands it) rather than describing a specific tool's internal algorithm.

## SAFETY-06 — Goal Structuring Notation assurance case: explicit claim-to-evidence argument
Practice: Build an explicit, graphical argument structure that decomposes a top-level safety claim (goal) into sub-goals via stated inference strategies, contexts, and assumptions, terminating each branch in a direct reference to supporting evidence — as its own artifact, separate from the requirements and test documents it draws on.
Tradition: Safety-critical / high-assurance process
Source: "The Goal Structuring Notation – A Safety Argument Notation" (originating GSN paper, University of York); Wikipedia, "Goal structuring notation"
URL: https://www.researchgate.net/publication/228990118_The_goal_structuring_notation-a_safety_argument_notation ; https://en.wikipedia.org/wiki/Goal_structuring_notation
Source type: primary text + secondary summary
Source quality: strong — originating academic paper plus a corroborating encyclopedic summary of the same notation.
Claim (stated): GSN's "four principle elements" are goal (a safety claim), strategy (the inference between a goal and its supporting sub-goals), evidence/solution, and context. "A goal is decomposed into sub-goals until a point is reached where claims can be supported by direct reference to available evidence."
Mechanism: Distinct from SAFETY-01 (criticality-level-scaled rigor) and SAFETY-05 (bidirectional requirements/code/test traceability) — GSN's mechanism is an explicit, reviewable argument artifact connecting a top-level claim to evidence via stated inference steps, not a rigor-scaling scheme or a traceability link structure.

## SAFETY-07 — Hazard analysis derives safety requirements at the requirements phase
Practice: Perform top-down fault tree analysis (and/or bottom-up FMEA) during the requirements phase, before architecture is finalized, to systematically derive safety/diagnostic requirements from presupposed hazards — then repeat the analysis later to check the implemented design against those hazards.
Tradition: Safety-critical / high-assurance process
Source: NASA Software Engineering Handbook, "8.7 — Software Fault Tree Analysis"; Jama Software, "What Is Fault Tree Analysis (FTA)?"
URL: https://swehb.nasa.gov/spaces/SWEHBVC/pages/140640490/8.7+-+Software+Fault+Tree+Analysis ; https://www.jamasoftware.com/blog/fault-tree-analysis/
Source type: primary text (NASA handbook) + vendor content
Source quality: mixed — NASA handbook is an authoritative process standard; corroborated by a vendor explainer with a consistent claim.
Claim (stated): "The requirements phase is the time to perform a preliminary software fault tree analysis (SFTA), which is a 'top-down' analysis, looking for the causes of presupposed hazards... Aerospace teams may use fault trees during early architecture assessment to derive safety requirements, then again to check the implemented design."
Mechanism: Distinct from SAFETY-03 (classify components by harm severity) and SAFETY-06 (argument-structure artifact) — this is a specific analytical technique for generating the safety requirements themselves, applied at a specific lifecycle point (before architecture, then repeated post-implementation).

## SRE-05 — Multi-window, multi-burn-rate SLO alerting
Practice: Page on SLO/error-budget burn only when a fast (short-window) burn-rate signal and a slower (long-window) burn-rate signal both exceed their thresholds simultaneously, rather than alerting on either window alone, so transient spikes are filtered out without sacrificing fast detection of sustained incidents.
Tradition: Site reliability engineering
Source: Google SRE Workbook, "Alerting on SLOs"
URL: https://sre.google/workbook/alerting-on-slos/
Source type: primary text
Source quality: strong — originating organization's own published SRE workbook.
Claim (stated): "The multi-window multi-burn-rate (MWMBR) approach... combines a fast-burning short window with a slower-burning long window. Both must be true simultaneously for the alert to fire... By requiring a longer window to also exceed a threshold, you ensure the problem is sustained."
Mechanism: Distinct from SRE-01 (budget-consumption level triggers a governance/review-process change) — this is an alert-signal design technique for the paging decision itself, not a policy escalation mechanism.

## SRE-06 — Toil capped at a fixed share of engineering time, tracked and enforced
Practice: Define "toil" precisely (manual, repetitive, automatable, tactical work with no lasting value) as distinct from valuable operational work, measure the share of team time spent on it via periodic survey, and treat exceeding a fixed ceiling (Google's stated target: no more than 50%) as a management problem requiring intervention, not just an engineering backlog item.
Tradition: Site reliability engineering
Source: Google SRE Book, "Eliminating Toil"
URL: https://sre.google/sre-book/eliminating-toil/
Source type: primary text
Source quality: strong — originating organization's own published practice description.
Claim (stated): Toil is "manual, repetitive, automatable, tactical work that scales with service growth" and produces no lasting value. Google SREs should spend "no more than 50% of their time on operational tasks," and "exceeding 50% toil is a management problem, not just an engineering problem." Quarterly Google surveys show actual average toil around 33%.
Mechanism: Distinct from SRE-01 (error-budget consumption thresholds gating governance) — this caps and measures a different resource (manual operational labor time, not reliability risk spend) and the enforcement lever is organizational/managerial, not a review-process trigger.

## DESIGNDOC-05 — Named shepherd drives open-ended proposal discussion to closure
Practice: Assign a specific named individual (not the proposal's author) the explicit responsibility of keeping a design-proposal discussion moving, ensuring every raised concern receives a response, and moving the proposal into a fixed final-comment-period once discussion has reached a stable point — rather than leaving the discussion open-ended with no owner of convergence.
Tradition: Design-doc cultures
Source: Rust RFC process, "RFC 1068: Rust Governance" (rust-lang/rfcs)
URL: https://rust-lang.github.io/rfcs/1068-rust-governance.html ; https://github.com/rust-lang/rfcs/blob/master/text/1068-rust-governance.md
Source type: primary text
Source quality: strong — the governing project's own process document.
Claim (stated): "RFCs are either closed immediately (if they are clearly not viable), or else assigned a shepherd who is responsible for keeping the discussion moving and ensuring all concerns are responded to... When discussion has reached a fixed point, the RFC PR will be put into a final comment period (FCP)."
Mechanism: Distinct from DESIGNDOC-02 (RFC-explores/ADR-records document-type separation) — this is a role/responsibility mechanism for driving a single document's discussion to closure, not a division of labor between two document types.

## DESIGNDOC-06 — Mandatory "alternatives considered" section documenting rejected options
Practice: Require every design document to include a section that names each alternative approach seriously considered, states why it was rejected, and makes the optimization criteria explicit — proactively answering "why didn't you do X" rather than presenting only the chosen approach.
Tradition: Design-doc cultures
Source: "How to Write an Effective Software Design Document" (Refactoring English); design-doc template guidance (multiple practitioner sources)
URL: https://refactoringenglish.com/excerpts/write-an-effective-design-doc/
Source type: practitioner account
Source quality: mixed — practitioner guidance converging across multiple independent sources on the same section requirement, but not an organizational standard.
Claim (stated): "The 'Alternatives considered' section should explain what else was on the table and why each option was rejected... Don't just list alternatives — explain the trade-offs, why you didn't choose the 'obvious' solution, and what you're optimizing for."
Status: `possible-dup of DESIGNDOC-01` — DESIGNDOC-01's ADR structure already includes "context and consequences," and many ADR templates fold alternatives into that; unsure whether this is a distinct mechanism (mandatory rejected-options disclosure) or a restatement of ADR's existing context field under different vocabulary. Recorded rather than dropped or silently merged.

## TEST-04 — Mutation testing: test-suite quality measured by mutants killed, not lines covered
Practice: Automatically inject small deliberate faults ("mutants") into the source code, run the existing test suite against each mutant, and score test-suite quality by the fraction of mutants the suite detects (kills) — exposing gaps that line/branch coverage metrics cannot, since a line can be executed without its outcome being asserted on.
Tradition: Test-first lineages (test-quality assessment, adjacent to TDD/BDD)
Source: Wikipedia, "Mutation testing"; testRigor, "Understanding Mutation Testing: A Comprehensive Guide"
URL: https://en.wikipedia.org/wiki/Mutation_testing ; https://testrigor.com/blog/understanding-mutation-testing-a-comprehensive-guide/
Source type: secondary summary
Source quality: mixed — encyclopedic and practitioner-guide sources, but the mechanism (kill/survive scoring via injected faults) is a specific, standard, and independently well-documented technique.
Claim (stated): "A test kills a mutated program (mutant)... if its outcome for the mutant deviates from the outcome for the unmodified program... The percentage of mutants killed by a given test suite serves as a metric for test quality... A surviving mutant indicates a gap in your test suite."
Mechanism: Distinct from TEST-03 (shrinking a property-based-testing counterexample to minimal form) — mutation testing scores an existing suite's fault-detection power via injected faults; it does not generate test inputs or minimize failing cases.

## TEST-05 — Transformation Priority Premise: ordered transformation list bounds TDD's generalization step
Practice: In the TDD red-green step, restrict the allowed code changes that make a failing test pass to a ranked list of "transformations" (e.g., null→constant before constant→variable, before unconditional→if, before scalar→array, before adding recursion/iteration) ordered from most-specific to most-general, and always apply the highest-priority (most specific) transformation that suffices — never jumping straight to a more general one — to prevent both premature overgeneralization and dead-end under-generalization.
Tradition: Test-first lineages (TDD)
Source: Robert C. Martin ("Uncle Bob"), "The Transformation Priority Premise"; Wikipedia, "Transformation Priority Premise"
URL: https://en.wikipedia.org/wiki/Transformation_Priority_Premise ; https://cleancoders.com/episode/clean-code-episode-24-p1
Source type: primary text (originating author) + secondary summary
Source quality: strong — originating author's own formulation, corroborated by an independent encyclopedic summary.
Claim (stated): Transformations "have a priority or preferred ordering, which if maintained through the ordering of tests, will prevent impasses or long outages in the red/green/refactor cycle... By writing tests using transformation priority order, you should not reach a point where one test causes you to rewrite an entire method."
Mechanism: Distinct from TEST-01/02/03 (Gherkin scenarios, pre-coding acceptance tests, PBT shrinking) — TPP constrains how the implementation step itself proceeds once a test exists, not how tests are written or scored.

## LLM-11 — Graduated, threshold-triggered proactive context compaction
Practice: Continuously monitor context-window utilization against a series of staged thresholds (e.g., 70/80/85/90/99%) during a long agent run, and apply progressively more aggressive compression at each stage — first compacting verbose tool outputs into reference pointers, then trimming older messages via a sliding window, only invoking full LLM-based summarization as a last resort — so context size is kept stable and the hard limit is rarely reached reactively.
Tradition: LLM-agent-native engineering
Source: "Beyond Compaction: Structured Context Eviction for Long-Horizon Agents" (arXiv); Microsoft Learn, "Compaction" (Agent Framework docs)
URL: https://arxiv.org/pdf/2606.11213 ; https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction
Source type: primary text + vendor documentation
Source quality: mixed — arXiv paper plus a framework vendor's own documented implementation of the same staged mechanism.
Claim (stated): "The goal is to keep context size stable before it ever approaches hard limits, with most sessions never triggering reactive measures when proactive management is working correctly... Five stages activate at progressive pressure thresholds (70%, 80%, 85%, 90%, 99%)... At 80% threshold, older tool result messages are replaced with compact reference pointers."
Mechanism: Distinct from LLM-01 (context as a curated playbook refined via generate-reflect-curate) and LLM-06 (primacy/recency placement) — this is a capacity-management mechanism triggered by measured utilization, not a content-curation or placement heuristic.

## LLM-12 — Separate-agent adversarial critic to counter self-review bias
Practice: Route generated output through a distinct critic agent — running in a separate context, and ideally a different model, from the one that produced the output — to adversarially review it and return a structured verdict (pass/fail, specific issues with line references, severity), rather than having the generating agent review its own work; feed the critic's specific objections back to the generator for a bounded number of retry rounds.
Tradition: LLM-agent-native engineering
Source: MindStudio, "What Is the Verifier Pattern in Multi-Agent Systems?"; Augment Code, "Adversarial Code Review: Why the Maker Shouldn't Grade the Checker"
URL: https://www.mindstudio.ai/blog/verifier-pattern-multi-agent-systems-independent-review ; https://www.augmentcode.com/guides/adversarial-code-review
Source type: vendor content
Source quality: mixed — vendor-authored guides, but both independently cite the same measured phenomenon (self-preference bias) as the rationale, and the structured-verdict mechanism is specific and checkable.
Claim (stated): "LLMs recognized their own output and showed self-preference relative to neutral judging conditions... making the writing agent a weak checker for its own incorrect output." "Adversarial code review splits maker from checker across separate context, instructions, and models... Rounds 1–2 capture 75% of improvement... bounded retries with reasons converging; blind retries oscillate."
Mechanism: Distinct from LLM-09/10 (versioned golden regression suite gating merge, failure-driven dataset growth) — this is a per-output real-time review architecture (which agent reviews, and why it must not be the same agent), not a CI-gated static test corpus.

---

## Yield report

- **New mechanism-distinct entries added: 15.**
- **Candidates rejected as duplicates by mechanism: 0** (one entry, DESIGNDOC-06, was recorded but flagged `possible-dup of DESIGNDOC-01` per the directive's instruction not to silently drop or merge borderline cases).
- **Searches used: 15 / 15** (hard ceiling reached exactly; stopped per budget, not because a tradition ran dry).

### Per-tradition results
- **Spec-driven / spec-first development** — 1 new find: SDD-04 (specification by example / living documentation). Reached via alternative vocabulary (example-driven rather than structured-document-driven spec).
- **Design-by-contract** — 2 new finds: DBC-03 (blame-assignment fault localization), DBC-04 (distribute-never-replicate non-redundancy rule). Reached via failure-mode framing (how DbC localizes bugs) and comparison framing (DbC vs. defensive programming). Previously flagged "thin" in the source catalog; this pass filled it out with primary/peer-reviewed sources (POPL paper, Meyer's own writing).
- **Formal and lightweight-formal methods** — 2 new finds: FORMAL-04 (model-based test generation from behavioral models), FORMAL-05 (counterexample-guided incremental abstraction refinement). Reached via alternative vocabulary (test generation, refinement) distinct from pass 1's tool-selection and adoption-path framings.
- **Safety-critical / high-assurance process** — 2 new finds: SAFETY-06 (GSN assurance-case argument structure), SAFETY-07 (hazard-analysis-derived requirements via fault tree/FMEA). Reached via primary-source framing (GSN's originating paper; NASA handbook) distinct from pass 1's DO-178C/IEC-62304 vendor-explainer framing.
- **Site reliability engineering** — 2 new finds: SRE-05 (multi-window multi-burn-rate alerting), SRE-06 (toil budget cap). Reached via alternative vocabulary (burn rate, toil) distinct from pass 1's error-budget-governance and postmortem framings.
- **Design-doc cultures** — 2 new finds: DESIGNDOC-05 (named shepherd role), DESIGNDOC-06 (alternatives-considered section, possible-dup of DESIGNDOC-01). Reached via a different document-culture lineage (Rust's open-source RFC governance) rather than pass 1's Amazon-centric sources.
- **Test-first lineages** — 2 new finds: TEST-04 (mutation testing), TEST-05 (Transformation Priority Premise). Reached via failure-mode framing (what coverage metrics miss) and primary-source framing (Robert Martin's own TDD refinement).
- **LLM-agent-native engineering** — 2 new finds: LLM-11 (graduated proactive context compaction), LLM-12 (separate-agent adversarial critic). Still the richest vein even on a second, diversified pass — both queries used framings (capacity-threshold management; self-review-bias mitigation) not present in pass 1's 10 entries, and both surfaced strong mechanism-distinct results on the first try.

### Traditions where diversified queries still returned only known practices
None. Every tradition yielded at least one mechanism-distinct new entry on this pass — including Design-by-contract, which pass 1 flagged as its thinnest vein. No tradition can be called genuinely saturated based on this budget; the 15-search ceiling was reached with every query still converting to a usable find, so remaining gap is plausible in all eight traditions, not just the ones sampled.
