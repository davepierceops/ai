---
status: draft
piece: converging-on-intent
purpose: Step-1 artifact — thesis, tier-tagged claims list, section plan. Awaiting Dave's approval before any prose exists.
---

# Working thesis

LLMs made building software fun to me again by reducing the burden —
and the lossiness — of translating intent into implementation dialects. In
doing so, they exposed something that was always true: software development
was always more ambiguous, emergent, and evidence-dependent than we liked
to admit.

# Thesis extension

The shift that matters moves the center of correctness from implementation
to specification, observation, and verification.

(Opinion tier — claim 12. The piece argues toward this and deliberately
stops short of the methodology it implies; §7 ends on the open question,
not the framework. Every section tests against the working thesis; §6–7
additionally test against the extension.)

# Claims list (pre-tagged; tiers are proposals awaiting Dave's correction)

| # | Claim | Tier | Note |
|---|---|---|---|
| 1 | Dave conflated coding with building software — part for whole — and filed his own work outside the category | inferred | Grounded in personal history; below proof. Refined from "distinct activities" after §1 |
| 2 | Dave's loss of enjoyment came from repeated re-learning of encodings, not loss of ability | inferred | Autobiographical self-report; honest tier is inference, not demonstration |
| 3 | The same underlying concepts recur across languages, tools, protocols, dialects | inferred | Decades of observation |
| 4 | Human intent → code is a lossy channel; encoding distorts meaning, not merely consumes time | inferred | The core conceptual move; §3 must make the inference legible |
| 5 | LLMs reduce the need to personally encode intent into every implementation dialect | inferred | Direct experience, no test shown in-piece |
| 6 | Loss does not disappear; it relocates to model interpretation | inferred | |
| 7 | Deterministic execution ≠ deterministic translation of intent; the old process was never clean | opinion | The declared hot take; flag clearest of all |
| 8 | Production is emergent and practically nondeterministic; every user mutation is a production change | inferred | SRE experience; candidate for demonstration if an example is shown |
| 9 | Source code and design cannot fully predict current production behavior | inferred | |
| 10 | SRE's core observability question is epistemic, not telemetry-collection | inferred | Recasting; borderline opinion |
| 11 | intent → system and system → understanding are complementary lossy channels | inferred | The piece's synthesis |
| 12 | The center of correctness is moving from implementation to specification, observation, and verification | opinion | The thesis extension; argued toward, not demonstrated — §7 stops before the methodology |
| — | "What evidence do we have that we're converging on what we intended?" | n/a | A question, not a claim; the piece ends on it unresolved by design |

No relayed claims currently. If §6 ends up citing SRE literature for
SLIs/SLOs or the observability framing, those become relayed and must be
attributed (attribution is mandatory per prose-criteria.md).

# Section plan

Piece target: ~2,200 words. Budgets below are per section, ±10%; a section
that cannot make its budget is an outline problem for the Editor, not a
license to run long. §1 landed at ~430.

## 1. The Problem Wasn't Building Software

**Budget:** 430 words (accepted)

**Intro note:** Broad claim, then personal realization

**Content note:** Coding ≠ building software

**Must contain**

* Tiny amount of personal history
* Longstanding self-description: "I'm not a coder; I don't enjoy coding"
* Recognition that coding and building software are not the same activity
* Enough of the realization to create tension without telling the whole story
* Personal history can recur later rather than being front-loaded

**Does not belong**

* Full chronology
* Detailed syntax/incantation argument
* LLM mechanics
* SRE
* Verification
* Proof of the thesis

**Job in the arc**

* Anchor the piece
* Establish the question being explored
* Create unresolved tension
* Give readers a reason to continue

**Exit condition**

* Reader understands the contradiction:

  * Enjoyed making systems do things
  * Believed for decades that coding was not enjoyable
* Reader wants to understand why

**Transition:** Why did coding stop being fun?

**Already covered — final text accepted 2026-08-13 (do not re-argue)**

* "I'm not a coder" self-description: established, then dissolved as a
  taxonomy error — coding mistaken for the whole of building software
* Career-names sketch spent in one line (sysadmin, quality, security,
  DevOps, infra, reliability) — do not re-catalog
* Enjoyment anchor set: the moment a system behaves as pictured
* Personal-history anchor placed: first real box at fifteen ("grokked") —
  later sections build on it, never re-introduce it
* Exit question asked verbatim: "why did the coding stop being fun?" —
  §2 opens by answering it, not restating it

---

## 2. The Incantations Stop Being Magic

**Budget:** 450 words

**Intro note:** Personal history in pieces

**Content note:** Novelty → fluency → overload

**Must contain**

* Early syntax as discovery and power — incantations, magic spells
* The same concepts arriving in new dialects, decade after decade
* Fluency was never the problem; relearning was. Loss of interest, not of
  ability
* Magic inverts: early, strange words grant power; later, nothing underneath
  is inexplicable
* Dave wrote little code — specs, designs, route tables, SQL; teams wrote
  the code

**Examples**

* Three chronological markers at most, one sentence each, drawn from: BASIC,
  Pascal, DR-DOS / VB, a networking absurdity, Solaris / BSD / OS/2, SQL
  dialects
* The section is the arc from wonder to overload, not the history

**Does not belong**

* Full lossiness argument
* SRE
* Verification
* Advice to junior engineers
* Nostalgia tour
* Exhaustive technology list

**Job in the arc**

* Explain why "I don't enjoy coding" became true of the part, not the whole
* Separate building from repeatedly learning new encodings
* Show the accumulation over decades
* Prepare the move from annoyance to engineering consequence

**Exit condition**

* Reader understands:

  * Syntax competence was not the problem
  * Repeated relearning became overload
  * The same underlying concepts kept appearing in new dialects
* Reader is ready for the claim that translation is not merely tedious

**Transition:** The cost was not only effort

---

## 3. Translation Is Lossy

**Budget:** 400 words

**Intro note:** Core conceptual move

**Content note:** Intent degraded through encoding

**Must contain**

* Distinction between effort and information loss
* Rich internal model compressed into implementation-specific forms
* Syntax, APIs, frameworks, conventions, and abstractions can distort intent
* Translation burden is not merely cognitive overhead
* Human intent → code as an imperfect channel

**Does not belong**

* Detailed LLM benefits
* SRE
* Verification methodology
* Determinism hot take in full

**Job in the arc**

* Upgrade the argument from "coding became tedious" to an engineering claim
* Establish lossiness as central vocabulary
* Explain why repeated translation affects more than productivity

**Exit condition**

* Reader accepts:

  * Human intent → implementation is lossy
  * Encoding can alter meaning, not merely consume time
* Reader is ready to ask what LLMs change about that channel

**Transition:** LLMs alter where the translation happens

---

## 4. LLMs Move the Lossy Boundary

**Budget:** 350 words

**Intro note:** What actually changed

**Content note:** Less encoding friction, new interpretation risk

**Must contain**

* LLMs reduce the need to personally encode intent into every implementation dialect
* More communication can happen closer to the level of the conceptual model
* Reduced syntax/API/configuration burden
* Loss does not disappear
* New loss appears in model interpretation
* Failure mode shifts:

  * Less "I expressed this incorrectly in the language"
  * More "the model inferred something I did not mean"
* LLM value is broader than syntax recall
* Tools framing only; no intelligence thesis required

**Does not belong**

* Claims that LLMs make software development lossless
* General AI-future discussion
* Anthropomorphizing
* Detailed verification method
* Universal claims about what people will do with the tool

**Job in the arc**

* Explain why building software feels different now
* Connect the personal realization to a technical mechanism
* Avoid the shallow "AI remembers syntax for me" version
* Create the new trust problem

**Exit condition**

* Reader understands:

  * Translation still exists
  * Its location and failure modes have changed
  * LLMs expose ambiguity rather than eliminating it

**Transition:** The old process was never clean either

---

## 5. The Ambiguity Was Always There

**Budget:** 300 words

**Intro note:** Hot take

**Content note:** Determinism was overstated

**Must contain**

* Intent → implementation was already lossy
* Deterministic execution ≠ deterministic translation of intent
* Human authors routinely misunderstand, omit, or distort requirements
* Authoring the code can create false confidence in the translation
* Production itself is emergent and practically nondeterministic
* Production is composed mostly of deterministic components interacting in complex ways
* System behavior is difficult to predict globally and moment to moment
* Production state changes continuously
* Every user mutation is also a change to the production environment
* Other ongoing changes:

  * deploys
  * configuration
  * dependencies
  * traffic
  * caches
  * queues
  * failures
  * data
* Source code and design cannot fully predict current production behavior
* LLMs make one existing ambiguity more obvious; they did not invent the underlying problem

**Does not belong**

* "Humans are just as unreliable as LLMs"
* Broad attack on SWEs
* Full SRE exposition
* Detailed verification methodology
* Deep distributed-systems digression

**Job in the arc**

* Break the false equation between deterministic components and deterministic systems
* Expand lossiness:

  * intent → code
  * code → running reality
* Establish that correctness cannot be inferred solely from implementation
* Make the SRE turn inevitable

**Exit condition**

* Reader accepts:

  1. Intent → implementation was never lossless
  2. Implementation → production behavior was never fully predictable
* The next question becomes:

  * What is the system actually doing?
  * How do we know?

**Transition:** This is familiar territory in SRE

---

## 6. SRE Has Been Asking This All Along

**Budget:** 150 words

**Prose constraint:** Make the SRE connection, establish the epistemic link, and get out before this becomes an SRE explainer.

**Intro note:** Major conceptual turn

**Content note:** Behavior, evidence, justified belief

**Must contain**

* Core SRE question:

  * What is the system actually doing?
  * What evidence supports that belief?
* Observability as an epistemic problem, not a telemetry-collection problem
* The running system gets a vote
* Source code, architecture, and intended behavior are insufficient evidence of actual behavior
* SLIs/SLOs as attempts to make "what matters" and "what counts as working" explicit
* Specification and verification are closely related to long-standing SRE concerns
* Beginning of the two-channel framing:

  * intent → system
  * system → understanding
* SRE has spent decades wrestling with the second channel
* LLM-assisted construction makes the first channel newly visible

**Does not belong**

* History of SRE
* Observability-tool catalog
* Detailed SLO mechanics
* "SRE had all the answers"
* "Software engineering should become SRE"
* Full LLM verification methodology

**Job in the arc**

* Ground the argument in the domain of direct experience
* Recast observability as a knowledge problem
* Connect production epistemology to software-construction epistemology
* Show that these are related problems, not merely analogous ones

**Exit condition**

* Reader understands:

  * intent → system and system → understanding are complementary lossy channels
  * evidence matters on both sides
* Reader is ready for the larger unresolved construction question

**Transition:** Apply the same question to building

---

## 7. Are We Converging on What We Intended?

**Budget:** 200 words

**Intro note:** Open outward

**Content note:** Evidence of intended behavior

**Must contain**

* One dominant unresolved question:

  * **What evidence do we have that the thing we're building is converging on what we intended?**
* Specification and verification as increasingly important control surfaces
* Code is not necessarily the right control surface
* Before implementation:

  * intent
  * constraints
  * invariants
  * acceptance criteria
* After implementation:

  * tests
  * evals
  * runtime behavior
  * observability
  * user-visible outcomes
* Verification effort should be calibrated to change risk
* "How much verification is this change worth?" as a major follow-up question
* Explicitly stop before solving the methodology

**Does not belong**

* Full verification framework
* Evidence-budget methodology
* Detailed agent architecture
* Complete theory of AI-native software delivery
* Neat final answer

**Job in the arc**

* Turn retrospective realization into forward-looking inquiry
* Show why the personal story matters beyond autobiography
* Establish the larger body of work this article seeds
* End open rather than resolved

**Exit condition**

* Reader leaves with one primary question:

  * **What evidence do we have that the thing we're building is converging on what we intended?**
* Other questions feel subordinate to that one
* Article points forward rather than pretending to finish the subject

**Transition:** Future work

---

# Follow-Up Topics / Seeds

* Observability of software construction
* Verification proportional to change risk
* Evidence budgets
* Verification as risk-priced investment
* Selective technical fluency
* Core vs. peripheral fluency
* Debugging in LLM-built systems
* Learning concepts vs. encodings
* Expertise after implementation gets cheaper
* Problem framing
* Decomposition
* Judgment and architectural taste
* Cross-discipline boundaries
* Cross-hierarchy boundaries
* Other boundary types not yet identified
* Management skills as one example of transferable higher-order skills
* Non-code control surfaces
* Code review vs. verification
* False confidence from non-expert code review
* Independent evidence
* LLM-to-LLM verification limits
* Runtime evidence
* Specification quality
* Intent legibility
* Model ambiguity
* Human-to-machine lossiness
* System-to-human lossiness
* SRE moved left
* Production as an emergent system
* User changes as production changes
* What technical mastery means when encoding can be delegated
* LLMs as tools: capability amplification without guaranteed competence
