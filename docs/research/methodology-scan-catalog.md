# External Methodology Scan — Phase 1 Catalog (Blind Discovery)

Findings-only catalog. No comparison, no adoption judgment, no cross-tradition dedup.
Track B run (no repository connector) — this file is emitted for the operator to land.

Checkpoint status: run complete. Shallow sweep (8 searches) + deep pass (14 searches) = 22/25 searches used.

---

## SDD-01 — Spec as authoritative source artifact
Practice: Write a structured, machine-readable specification (e.g. OpenAPI, structured Markdown) as the authoritative source of truth before implementation begins, from which code, tests, and documentation are derived.
Tradition: Spec-driven / spec-first development
Source: IBM "What is Spec-Driven Development?"; Microsoft for Developers, "Spec-Driven Development: A Spec-First Approach to AI-Native Engineering"
URL: https://www.ibm.com/think/topics/spec-driven-development ; https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/
Source type: vendor content
Source quality: mixed — vendor-authored but the artifact-precedence claim is specific and mechanical, not generic marketing.
Claim (stated): SDD "mandates that system intent be explicitly defined in a structured format ... before implementation begins," with the spec as "the authoritative source of truth."
Mechanism: Spec captures intent, behavior, edge cases, and non-functional requirements in a form both humans and LLMs can read and act on; implementation, tests, and docs are generated from it rather than written independently.

## SDD-02 — Spec-to-code pipeline via atomic task decomposition
Practice: Derive an implementation plan from the spec, break the plan into atomic tasks, and only then generate code — never generate code directly from the spec.
Tradition: Spec-driven / spec-first development
Source: Microsoft for Developers, "Spec-Driven Development: A Spec-First Approach to AI-Native Engineering"
URL: https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/
Source type: vendor content
Source quality: mixed — vendor blog, but the three-stage pipeline (spec → plan → atomic tasks → code) is a concrete, checkable mechanism.
Claim (stated): "The team (or an AI coding agent) first writes a detailed spec describing what the system should do, then derives an implementation plan, breaks it into atomic tasks, and only then generates the code."

## SDD-03 — Spec-first alignment before AI code generation
Practice: Define guardrails, requirements, constraints, acceptance criteria, and edge cases as shared context up front, before invoking AI generation, instead of prompting first and aligning later.
Tradition: Spec-driven / spec-first development
Source: Augment Code, "Spec-Driven Development & AI Agents Explained"; Kinde, "Beyond TDD: Why Spec-Driven Development is the Next Step"
URL: https://www.augmentcode.com/guides/spec-driven-development-ai-agents-explained ; https://www.kinde.com/learn/ai-for-software-engineering/best-practice/beyond-tdd-why-spec-driven-development-is-the-next-step/
Source type: vendor content
Source quality: mixed — vendor content-marketing; kept because the ordering claim (align-before-generate vs. prompt-then-align) is a specific, falsifiable workflow claim.
Claim (stated): "Instead of prompting first and aligning later, teams align first and let AI accelerate execution from a clear spec."

## DBC-01 — Contracts as caller/callee obligations
Practice: Attach explicit preconditions (caller obligations), postconditions (callee guarantees), and invariants (always-true conditions) to software components so correctness is enforced at interaction boundaries.
Tradition: Design-by-contract
Source: Bertrand Meyer, "Design by Contract" (chapter); Eiffel Software
URL: https://se.inf.ethz.ch/~meyer/publications/old/dbc_chapter.pdf ; https://www.eiffel.com/values/design-by-contract/
Source type: primary text
Source quality: strong — originating author's own formulation.
Claim (stated): "Software components interact through well-defined contracts consisting of preconditions, postconditions, and invariants, which precisely define the obligations of callers and the guarantees provided by callees, enabling correctness by construction and early detection of logical errors."

## FORMAL-01 — Temporal vs. structural specification split
Practice: Choose the formal-specification tool by property type — TLA+ for temporal properties of concurrent/distributed/fault-tolerant protocols, Alloy for structural properties, analyzed via bounded model checking.
Tradition: Formal and lightweight-formal methods
Source: "Alloy meets TLA+: An exploratory study" (arXiv)
URL: https://arxiv.org/pdf/1603.03599
Source type: primary text
Source quality: strong — peer-reviewed comparative study.
Claim (stated): "TLA+ focuses on temporal properties while Alloy is better suited to handle structural properties. Alloy is inherently static, thus the definition of dynamic properties usually relies on well-known idioms."

## FORMAL-02 — Property-based testing as formal-methods on-ramp
Practice: Use property-based testing (specifications resembling temporal-logic specs) as an incremental adoption path toward formal verification, rather than requiring teams to adopt a full model checker up front.
Tradition: Formal and lightweight-formal methods
Source: "Quickstrom: Property Based Acceptance Testing with LTL Specifications" (arXiv)
URL: https://arxiv.org/pdf/2203.11532
Source type: primary text
Source quality: strong — technical paper describing the tool's design rationale.
Claim (stated): "Property-based testing could be used as an incremental path towards more widespread adoption of formal verification among software engineers."
Inference (mine): Framed here as a graduated-rigor on-ramp practice rather than a specific tool feature.

## SAFETY-01 — Assurance-level scaling
Practice: Scale the required rigor of verification and process activity to a discrete, pre-assigned criticality level of the component, rather than applying uniform rigor everywhere.
Tradition: Safety-critical / high-assurance process
Source: Wind River, "Understanding DO-178C"; Parasoft, "Software Development Process for Safety-Critical Systems"
URL: https://www.windriver.com/solutions/learning/do-178c ; https://www.parasoft.com/blog/safety-critical-software/
Source type: vendor content
Source quality: mixed — vendor explainer, but the level-scaling mechanism itself is standard and independently corroborated across DO-178C (Design Assurance Level A–E), ISO 26262 (ASIL), and IEC 61508 (SIL).
Claim (stated): "DO-178C defines five software levels (criticality levels) ranging from Level A (most critical) to Level E (least critical)." Equivalent constructs: ASIL (ISO 26262), SIL (IEC 61508).

## SAFETY-02 — Parallel integral processes alongside development
Practice: Run verification, quality assurance, and configuration management as continuous processes in parallel with development activity, not as a final gate after coding completes.
Tradition: Safety-critical / high-assurance process
Source: Wind River, "Understanding DO-178C: Wind River's Insights on Aerospace Software Standards"
URL: https://www.windriver.com/solutions/learning/do-178c
Source type: vendor content
Source quality: mixed — vendor explainer restating a standard's structure; the parallel-process framing is a specific, checkable claim about DO-178C's lifecycle.
Claim (stated): "DO-178C covers the complete software lifecycle including planning, development, and integral processes needed to ensure correctness and robustness, including software verification, software quality assurance, configuration management, and certification liaison with regulatory authorities."

## SRE-01 — Error-budget consumption thresholds trigger policy escalation
Practice: Define concrete error-budget consumption thresholds (e.g. 64% within a rolling four-week window) that automatically trigger escalating governance responses, such as mandatory additional review for risky changes.
Tradition: Site reliability engineering
Source: Harness, "Site Reliability Engineering (SRE): A Step-by-Step Guide" (citing Google SRE error-budget policy pattern)
URL: https://www.harness.io/blog/site-reliability-engineering-sre-101-everything-you-need-to-know
Source type: vendor content
Source quality: mixed — vendor guide, but the specific threshold-triggered-escalation mechanism is a concrete governance pattern, not generic marketing.
Claim (stated): "Error budget policies establish concrete thresholds that trigger escalating responses, such as tightening approval processes and requiring additional review for risky changes at 64% budget consumption within a four-week rolling window."

## SRE-02 — Production Readiness Review gate
Practice: Apply a structured checklist assessment (SLOs defined, baseline data collected, SLI instrumentation verified, golden-signal instrumentation and dashboards in place) to a new service before it is allowed to receive production traffic.
Tradition: Site reliability engineering
Source: getdx.com, "What is SRE? Complete guide to site reliability engineering tools and practices"
URL: https://getdx.com/blog/site-reliability-engineering/
Source type: vendor content
Source quality: mixed — vendor guide; kept because it gives a concrete, checkable gate rather than a philosophy statement.
Claim (stated): "A minimal PRR checklist for any service entering production includes SLOs defined, baseline data collected, and SLI instrumentation verified, along with Four Golden Signals instrumented and dashboards created."

## DESIGNDOC-01 — ADR as single-decision, in-repo record
Practice: Record each significant architecture decision as its own short document (decision, context, consequences), stored as plain text/Markdown alongside the code it governs rather than in a separate wiki or tool.
Tradition: Design-doc cultures
Source: Michael Nygard (originator, 2011), as summarized in Didier Caroff, "Architecture Decision Record (ADR)"
URL: https://medium.com/geekculture/architecture-decision-record-adr-f822e45dafcf
Source type: secondary summary
Source quality: mixed — secondary account of Nygard's original ADR proposal; the one-decision-per-document-in-repo structure is a specific, verifiable claim about the format's design.
Claim (stated): "An ADR is a short document (often a simple Markdown file in a repository or a page in a docs system) that records a single significant decision along with its context and consequences."

## DESIGNDOC-02 — RFC-explores, ADR-records division of labor
Practice: Use two distinct document types at two distinct decision phases — an RFC to explore options and solicit feedback before a decision is made, and an ADR to record what was actually decided afterward.
Tradition: Design-doc cultures
Source: Lukas Niessen, "How to Make Architecture Decisions: RFCs, ADRs, and Getting Everyone Aligned" (ITNEXT)
URL: https://itnext.io/how-to-make-architecture-decisions-rfcs-adrs-and-getting-everyone-aligned-ab82e5384d2f
Source type: practitioner account
Source quality: mixed — individual practitioner's synthesis, not an organizational standard, but the phase-separation mechanism is concrete and checkable.
Claim (stated): "The RFC was about exploring options, the ADR is about recording what was decided."

## TEST-01 — Gherkin Given/When/Then as shared executable spec
Practice: Express acceptance criteria as structured natural-language scenarios (Given/When/Then) that are simultaneously readable by non-technical stakeholders and executable as automated tests.
Tradition: Test-first lineages (TDD/BDD/ATDD)
Source: Agile Alliance, "What is BDD (Behavior Driven Development)?"
URL: https://agilealliance.org/glossary/bdd/
Source type: secondary summary
Source quality: strong — Agile Alliance glossary is a recognized reference for the term's canonical definition.
Claim (stated): "BDD utilizes the Gherkin language, a semi-structured natural language, to express the acceptance criteria of user stories in human-readable acceptance tests written as scenarios framed by the Given, When, Then keywords."

## TEST-02 — Acceptance tests written before development starts
Practice: Write acceptance tests collaboratively (business customers, developers, testers) before development of the corresponding feature begins, so the test defines the target rather than verifying after the fact.
Tradition: Test-first lineages (TDD/BDD/ATDD)
Source: Wikipedia, "Acceptance test-driven development"
URL: https://en.wikipedia.org/wiki/Acceptance_test-driven_development
Source type: secondary summary
Source quality: mixed — tertiary/encyclopedic source, but the before-coding-begins ordering is a specific and standard claim about ATDD.
Claim (stated): "ATDD is a development methodology based on communication between the business customers, the developers, and the testers... ATDD encompasses acceptance testing, but highlights writing acceptance tests before developers begin coding."

## LLM-01 — Context as an evolving, curated playbook
Practice: Treat an LLM agent's working context as a living artifact refined through a repeated generate → reflect → curate cycle, rather than a static prompt assembled once.
Tradition: LLM-agent-native engineering
Source: "Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code" (arXiv), describing Agentic Context Engineering (ACE)
URL: https://arxiv.org/html/2508.08322v1
Source type: primary text
Source quality: strong — arXiv technical paper with a named, specific mechanism.
Claim (stated): "Agentic Context Engineering (ACE) treats contexts as 'evolving playbooks' refined through a generate-reflect-curate cycle."

## LLM-02 — Evaluation-Driven Development with LLM-as-judge
Practice: Design evaluations for models, data, and workflows (the LLM analog of writing tests), using an LLM-as-judge to assess semantic equivalence between generated and expected output where exact-match is unusable due to non-determinism.
Tradition: LLM-agent-native engineering
Source: "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture" (arXiv)
URL: https://arxiv.org/html/2411.13768v3
Source type: primary text
Source quality: strong — arXiv paper proposing a named process model.
Claim (stated): "Evaluation-Driven Development (EDD) is similar to test-driven development in traditional software engineering, except instead of writing tests for code, you design evaluations for your models, data, and workflows to guide iterative improvement... One powerful approach for handling non-determinism in LLM outputs is to use an LLM as a judge to evaluate whether generated output is semantically equivalent to the expected result."

## LLM-03 — Explicit agent-facing context files beyond source code
Practice: Maintain repo-level, agent-facing documentation files (distinct from source code and from human-oriented docs) that explicitly state architectural patterns and team conventions an agent needs but cannot reliably infer from code alone.
Tradition: LLM-agent-native engineering
Source: "Agent READMEs: An Empirical Study of Context Files for Agentic Coding" (arXiv)
URL: https://arxiv.org/pdf/2511.12884
Source type: primary text
Source quality: strong — empirical study of the practice across real repositories.
Claim (stated): "For agents to work effectively on software projects while adhering to architectural patterns and team conventions, they require not only access to source code but also explicit guidance."

## DBC-02 — Contract inheritance: weaken preconditions, strengthen postconditions
Practice: When a subclass overrides a contracted method, it may only weaken (relax) the inherited preconditions and may only strengthen (tighten) the inherited postconditions and invariants — never the reverse — so substitutability is preserved.
Tradition: Design-by-contract
Source: icontract (Python DbC library) documentation and README
URL: https://icontract.readthedocs.io/en/latest/introduction.html ; https://github.com/Parquery/icontract
Source type: practitioner account
Source quality: strong — library documentation describing a directly-verifiable, implemented behavior, consistent with Meyer's original DbC inheritance rule.
Claim (stated): "Icontract allows inheritance of the contracts and supports weakening of the preconditions as well as strengthening of the postconditions and invariants... indispensable for modeling many non-trivial class hierarchies."

## OTHER-01 — Consumer-driven contract testing
Practice: Have the calling service (consumer) author the interface contract — which endpoints it calls, request format, required response fields — and verify the providing service against that consumer-authored contract in isolation, without running full integration tests.
Tradition: other — contract testing (interface/API contracts between services; followed as a strong lead outside the seed list because it directly addresses the LLM-agent hallucinated-interface problem named in this directive's scope)
Source: Pact documentation; OneUptime, "How to Build Contract Testing with Pact"
URL: https://docs.pact.io/ ; https://oneuptime.com/blog/post/2026-01-30-contract-testing-pact/view
Source type: vendor content
Source quality: mixed — tool-vendor-adjacent sources, but the consumer-authors-the-contract mechanism and the central-broker-as-deploy-safety-source-of-truth claim are specific and mechanical.
Claim (stated): "In consumer-driven contract testing, the service that calls an API (the consumer) defines what it needs from the provider. These expectations become contracts that providers must satisfy." A Pact Broker "stores pacts, verification results, environments, and deployment metadata... becomes the source of truth for whether a consumer version and provider version are safe to deploy together."

## FORMAL-03 — Pre-implementation modeling to catch design-level bugs cheaply
Practice: Build a formal model of a system's design before writing implementation code, specifically to surface design/specification-level bugs while they are still cheap to fix, rather than after the system is built and would need rearchitecting.
Tradition: Formal and lightweight-formal methods
Source: Hillel Wayne, discussed in Gergely Orosz, "Formal methods with Hillel Wayne" (The Pragmatic Engineer)
URL: https://newsletter.pragmaticengineer.com/p/formal-methods-with-hillel-wayne
Source type: practitioner account
Source quality: mixed — secondary account of a practitioner's stated view, not a primary paper, but the stated cost-timing rationale is a specific and checkable claim.
Claim (stated): "Formal methods can be used to find design/specification level bugs that are tricky to find in other ways... the practical value from an industry perspective [is] finding these impactful bugs sooner and thus more cheaply, before you have to rearchitect a complex system."

## SAFETY-03 — Harm-based tri-level safety classification
Practice: Classify each software component into one of three safety classes based on the severity of harm its failure could cause (no injury possible / non-serious injury possible / death or serious injury possible), and document and justify that classification as a formal, approved artifact before scaling process rigor to it.
Tradition: Safety-critical / high-assurance process (medical-device SDLC)
Source: Greenlight Guru, "What are the IEC 62304 Safety Classifications?"; Jama Software, "What Is IEC 62304?"
URL: https://www.greenlight.guru/glossary/iec-62304 ; https://www.jamasoftware.com/requirements-management-guide/medical-devices/iec-62304/
Source type: vendor content
Source quality: mixed — vendor explainers of a named standard; the three-tier harm-based classification and its mandatory-documented-justification requirement are specific, checkable claims about IEC 62304.
Claim (stated): "IEC 62304 identifies three safety classes for medical device software: Class A (no injury or damage to health is possible), Class B (injury is possible, but not serious), and Class C (death or serious injury is possible)... This classification must be documented, justified, and approved."

## SAFETY-04 — Outcome-based compliance independent of lifecycle model
Practice: Specify the required lifecycle tasks and evidentiary outcomes a process must produce, without mandating which development methodology (waterfall, V-model, agile, iterative) is used to produce them.
Tradition: Safety-critical / high-assurance process (medical-device SDLC)
Source: Spyrosoft, "IEC 62304:2006 - software life cycle processes explained"
URL: https://spyro-soft.com/blog/healthcare/iec-623042006-software-life-cycle-processes-explained
Source type: vendor content
Source quality: mixed — vendor blog summarizing a standard's structure; the methodology-agnostic framing is a specific and checkable claim about how IEC 62304 is written.
Claim (stated): "IEC 62304 does not mandate a waterfall or V-model lifecycle, but instead requires that specific tasks and outcomes are achieved across the life cycle regardless of the development approach used, with Agile, hybrid, and iterative development models all acceptable provided required activities are performed and evidence is maintained."

## SAFETY-05 — Bidirectional requirements-to-code-to-test traceability
Practice: Maintain forward links from every requirement through design to code to test, and backward links from every test and code element back to the requirement that motivated it, so both untested requirements and unmotivated code/tests can be detected.
Tradition: Safety-critical / high-assurance process
Source: Parasoft, "Requirements Traceability Matrix for DO-178C Compliance"
URL: https://www.parasoft.com/learning-center/do-178c/requirements-traceability/
Source type: vendor content
Source quality: mixed — vendor explainer, but the bidirectionality mechanism and its dual purpose (coverage analysis vs. scope control) are specific and checkable.
Claim (stated): "Bidirectional traceability combines both directions and keeps the links consistent, and is the only approach that supports both coverage analysis (requirements missing tests) and scope control (tests or design elements with no requirement)."

## SRE-03 — Standard blameless postmortem artifact
Practice: Document every qualifying incident using a fixed artifact structure — summary, timeline, root-cause analysis, impact assessment, and corrective-action items each assigned an owner and due date — with the review process assuming good intent from participants rather than assigning individual fault.
Tradition: Site reliability engineering
Source: Google SRE, "Blameless Postmortem for System Resilience" (sre.google)
URL: https://sre.google/sre-book/postmortem-culture/
Source type: primary text
Source quality: strong — the originating organization's own published practice description.
Claim (stated): "Blameless postmortems are a cornerstone of Google's SRE practice, where the idea is to focus on what happened and why, not on who did it." Standard artifact includes "a summary, timeline, root cause analysis, impact assessment, and corrective action items with owners and due dates."

## SRE-04 — Maturity-gated, hypothesis-driven fault injection
Practice: Run fault-injection exercises against a stated hypothesis about system behavior under failure, with blast radius contained and a rollback plan in place, and gate whether experiments may run in production on a team's demonstrated maturity level (lower-maturity teams run in staging only, and earn the right to run in production).
Tradition: Site reliability engineering
Source: designgurus.io, "How do you run game days and chaos engineering exercises?"
URL: https://www.designgurus.io/answers/detail/how-do-you-run-game-days-and-chaos-engineering-exercises
Source type: secondary summary
Source quality: mixed — practitioner-guide synthesis rather than a primary organizational standard, but the maturity-gating mechanism is a specific, checkable governance claim distinct from chaos engineering's general philosophy.
Claim (stated): "Running your chaos experiments in production is a recommended practice as long as the fault injection can be contained and controlled, and you should have a rollback plan... However, if you're at L1-L2 (lower maturity levels), do not run in prod and earn the right by demonstrating the practice in staging."

## DESIGNDOC-03 — Write the future press release before building
Practice: Before building a product, write a narrative document that includes a mock press release dated as if the product has already launched, forcing the team to articulate the customer-facing outcome in plain customer language before committing engineering effort.
Tradition: Design-doc cultures
Source: Working Backwards (workingbackwards.com), "The Amazon Working Backwards PR/FAQ Process"
URL: https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
Source type: practitioner account
Source quality: strong — account from authors who worked directly on developing the practice at Amazon.
Claim (stated): "The PR/FAQ is a short narrative document... with two parts: A one-page mock press release written from a future date, announcing the launched product as if it already exists... written for the customer in a language a customer can understand."

## DESIGNDOC-04 — Silent-read-first review meeting
Practice: Open a design-review meeting with a fixed silent-reading period (no live presentation) during which all attendees read the full document, before opening the floor to discussion and challenge.
Tradition: Design-doc cultures
Source: coda.io, "Working Backwards | How write-ups help launch successful products like AWS, the Kindle & Prime Video"
URL: https://coda.io/@colin-bryar/working-backwards-how-write-an-amazon-pr-faq
Source type: practitioner account
Source quality: mixed — secondary practitioner retelling of the Amazon practice, but the meeting-structure mechanism (silent read before discussion) is specific and checkable.
Claim (stated): "At the beginning of every meeting at Amazon, everyone is granted a 20-minute window for silently perusing through the 6-page PR/FAQ" before the discussion portion begins.

## TEST-03 — Automatic shrinking to a minimal counterexample
Practice: When a generated random test case falsifies a property, automatically and repeatedly simplify that failing case (e.g. via binary search over the input space) until no smaller failing case can be found, and report only the minimal counterexample to the user.
Tradition: Test-first lineages (property-based testing, adjacent to TDD/BDD)
Source: QuickCheck documentation / Hackage; Jesper Cockx, "An introduction to property-based testing with QuickCheck"
URL: https://hackage.haskell.org/package/QuickCheck/docs/Test-QuickCheck.html ; https://jesper.sikanda.be/posts/quickcheck-intro.html
Source type: primary text
Source quality: strong — original tool's own documentation describing its own mechanism.
Claim (stated): "Expressions are continuously generated and checked until a counterexample is found; then the counterexample is repeatedly shrunk until the smallest expression that invalidates the property is found, and the locally minimal counterexample is then presented to the user."

## LLM-04 — Structural separation of instructions from untrusted content
Practice: Structure every agent prompt so system instructions, developer intent, and untrusted external content (retrieved documents, tool output, web content) occupy distinct, explicitly labeled channels — using delimiters, XML tags, or special tokens — so untrusted content is always treated as data and never as a command channel.
Tradition: LLM-agent-native engineering
Source: SoK-style synthesis in "Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis" (arXiv)
URL: https://arxiv.org/pdf/2604.02837
Source type: primary text
Source quality: strong — arXiv security-analysis paper naming a specific mechanism (spotlighting).
Claim (stated): "Structure every prompt so that system instructions, developer intent, and untrusted content occupy distinct, labeled channels, where retrieved and inbound content should enter as data only, never as a channel that can carry commands... Spotlighting, using delimiters, XML tags, or special tokens to mark untrusted external content distinctly from trusted instructions, is presented as a mitigation approach for indirect injection."

## LLM-05 — Periodic re-anchoring on the original objective
Practice: At periodic checkpoints during a long agentic task, have the agent restate the original objective in its own words and check whether its current action still advances it, to counteract instructions and constraints being diluted as context grows.
Tradition: LLM-agent-native engineering
Source: usewire.io, "Agent drift: why long-running AI agents lose the plot"
URL: https://usewire.io/blog/agent-drift-why-long-running-ai-agents-lose-the-plot/
Source type: practitioner account
Source quality: mixed — practitioner blog, not a controlled study, but the re-anchoring mechanism and its stated rationale (forcing the goal back into the attention distribution) are specific and checkable.
Claim (stated): "At periodic checkpoints, the agent restates the original objective in its own words and asks whether the current action advances it, which works because it forces the goal back to the top of the attention distribution."

## LLM-06 — Primacy/recency placement of critical instructions
Practice: Place the most critical instructions and constraints at the very start and/or very end of the context window, never buried in the middle, since model recall of mid-context information degrades sharply relative to the start and end.
Tradition: LLM-agent-native engineering
Source: Redis, "Context rot explained (& how to prevent it)"; original "Lost in the Middle" finding (Stanford, cited secondhand)
URL: https://redis.io/blog/context-rot/
Source type: secondary summary
Source quality: mixed — vendor/practitioner blog summarizing an underlying empirical study (Chroma's context-rot research and the Stanford "Lost in the Middle" paper), not the primary paper itself.
Claim (stated): "A 2023 Stanford study called 'Lost in the Middle' measured how well LLMs recall information based on where it sits in the context window, finding that performance drops by more than 30% when critical information lands in the middle... Models work best when relevant information sits at the very beginning or the very end of the context window."
Inference (mine): The "never put system instructions at the top of a very long prompt without also repeating them at the end" framing is my synthesis of the placement recommendation; the source states the recall-degradation finding and a general placement heuristic rather than that exact rule.

## LLM-07 — Decomposition authority stays with the orchestrator
Practice: Keep task-decomposition decisions exclusively with the orchestrating agent that holds full task context; never delegate the decision of how to scope or split a sub-task to the sub-agent that will execute it, since that sub-agent lacks the broader context needed to scope itself reliably.
Tradition: LLM-agent-native engineering
Source: Spring AI, "Spring AI Agentic Patterns (Part 4): Subagent Orchestration"
URL: https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/
Source type: vendor content
Source quality: mixed — framework-vendor blog, but the stated design rule (decomposition must not be delegated) is a specific, falsifiable architectural claim rather than generic advice.
Claim (stated): "A subagent doesn't have visibility into the broader task context, so it has no reliable basis for deciding what sub-tasks to create or how to scope them — decomposition is the orchestrator's job and stays there."

## LLM-08 — Validator-guided repair for hallucinated APIs
Practice: After generating code that calls an external API, validate the generated calls against the real API schema/reference and iteratively repair mismatches, rather than relying on generation-time accuracy alone.
Tradition: LLM-agent-native engineering
Source: "Mitigating API Hallucination in LLM-Generated Code via Structured Grounding, Selective Augmentation, and Validator-Guided Repair" (San José State University ETD)
URL: https://scholarworks.sjsu.edu/etd_projects/1761/
Source type: primary text
Source quality: strong — thesis/technical report with quantified results for the specific mechanism.
Claim (stated): "Validator-guided repair provides an efficient post-generation correction mechanism, achieving 96.6% pass rate with minimal overhead, and combining routing and repair yields the best overall performance achieving 98.63% pass rate."

## LLM-09 — Golden regression suite gates merge
Practice: Maintain a curated "golden" set of representative agent tasks with expected behaviors, version it alongside code/prompts in the same repository, run the full or a focused subset of it automatically on every pull request that touches the agent, and block the merge if any regression metric drops below a set threshold.
Tradition: LLM-agent-native engineering
Source: Slava Dubrov, "Evaluating AI Agents in Production: From Traces to Test Suites"
URL: https://slavadubrov.github.io/blog/2026/06/10/agent-evals-traces-to-test-suites/
Source type: practitioner account
Source quality: mixed — individual practitioner blog, but the CI-gating mechanism and versioning-alongside-code claim are specific and checkable practices, not generic advice.
Claim (stated): "On every pull request, run the full replay regression suite (~30 golden cases), and it should complete in under 5 minutes. Block merge if any regression metric drops below threshold... Version your golden dataset alongside code — store it in Git in the same repository as your agent's prompts and configuration."

## LLM-10 — Failure-driven regression dataset growth
Practice: For every diagnosed production failure, add a permanent labeled case (trace, label, dataset row, and scorer) to the regression suite, so a failure that recurs is one the test suite would now catch.
Tradition: LLM-agent-native engineering
Source: Slava Dubrov, "Evaluating AI Agents in Production: From Traces to Test Suites"
URL: https://slavadubrov.github.io/blog/2026/06/10/agent-evals-traces-to-test-suites/
Source type: practitioner account
Source quality: mixed — same individual practitioner blog as LLM-09; the failure-to-permanent-case mechanism is specific, but not corroborated by a second independent source in this pass.
Claim (stated): "Every diagnosed production failure should leave behind a trace, a label, a dataset row, and a scorer. A repeatable failure belongs in the regression suite."

---

## Coverage report

Total searches used: 22 / 25 (8 shallow sweep + 14 deep pass). Stopped 3 under the hard ceiling — later deep-pass searches were still surfacing new, non-redundant mechanisms (no forced padding), but per-tradition coverage had reached a reasonable breadth-plus-depth balance across all eight seed traditions plus one followed lead, so the remaining budget was banked rather than spent for its own sake.

- **Spec-driven / spec-first development** — covered well. 3 entries, all from the shallow sweep; the vein is heavy on vendor content-marketing as flagged in the directive, and the entries kept are the ones with concrete mechanical claims (spec-as-source-of-truth, spec→plan→atomic-tasks→code pipeline, align-before-generate ordering).
- **Design-by-contract** — thin. 2 entries (core contract triad; inheritance weakening/strengthening rule) plus one adjacent "other" entry (consumer-driven contract testing) followed as a strong lead because it addresses this directive's own hallucinated-interface concern. Did not find additional DbC-specific mechanical practices beyond the core triad and the inheritance rule within budget.
- **Formal and lightweight-formal methods** — covered well. 3 entries spanning tool-selection-by-property-type (TLA+ vs. Alloy), property-based testing as an adoption on-ramp, and pre-implementation modeling's cost-timing rationale.
- **Safety-critical / high-assurance process** — covered well. 5 entries spanning DO-178C (assurance-level scaling, parallel integral processes, bidirectional traceability) and IEC 62304 medical-device SDLC (harm-based classification, outcome-based/methodology-agnostic compliance) — both explicitly named sub-areas in scope were reached.
- **Site reliability engineering** — covered well. 4 entries spanning error-budget-triggered governance, production readiness review gates, blameless postmortem artifact structure, and maturity-gated chaos engineering.
- **Design-doc cultures** — covered well. 4 entries spanning ADR format, RFC/ADR phase separation, Amazon's PR/FAQ write-the-future-press-release practice, and the silent-read-first meeting structure.
- **Test-first lineages** — covered well. 3 entries spanning Gherkin Given/When/Then as shared executable spec, pre-coding acceptance-test authorship (ATDD), and property-based testing's automatic shrinking-to-minimal-counterexample mechanism.
- **LLM-agent-native engineering** — covered well, deepest vein of the scan. 10 entries spanning context-as-evolving-playbook, evaluation-driven development with LLM-as-judge, agent-facing context files, structural separation from untrusted content, periodic re-anchoring against instruction drift, primacy/recency placement, decomposition-stays-with-orchestrator, validator-guided repair for hallucinated APIs, and golden-suite/failure-driven regression testing. This bucket directly mapped onto the directive's named LLM-agent concerns (instruction drift, hallucinated interfaces, prompt-as-spec, instructions embedded in read material) and yielded a new practice on nearly every search — the richest vein in the scan.
- **Other (followed lead)** — consumer-driven contract testing (Pact), logged above with rationale: it is the closest durable-tradition analogue to LLM-agent hallucinated-interface risk, verifying interface expectations mechanically rather than trusting either side's assumption of the other's shape.

No tradition returned "found nothing," and no vein was cut off by the search ceiling — the ceiling was not reached.
