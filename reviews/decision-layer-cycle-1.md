# Review: docs/global-context/decision-layer.md — cycle 1

Verdict: changes-required
Reviewed: docs/global-context/decision-layer.md @ 5aa02c5
Reviewer: Spec Reviewer Agent
Date: 2026-08-21
Scope: the full file — frontmatter and all fifteen rules — against all ten
criteria of `docs/global-context/review-rubric.md` @ 5aa02c5, plus the three
additional checks the cycle directive names: internal consistency with core,
followability by an agent holding only the bundle and the repository, and
whether the file obeys its own rule 15.
Cross-checked: `docs/global-context/core.md` @ 5aa02c5 (consistency and
duplication); `LEXICON.md` (session, block, and dispatch vocabulary);
`docs/global-context/inventory.md` @ 5aa02c5 (provenance of each rule, not
reviewed); `bin/aimeta/frontmatter.py` and `bin/bundle-methodology` (what
`audience:` actually selects today); `skills/spec-review-cycle.md` and
`docs/cycles/global-context-cycle-1-directive-20260821T181500.md` (rule 15 and
rule 12 applied to real artifacts).
Not inspected: the rubric itself was applied, not reviewed. `inventory.md` was
read for provenance only, per the directive. No bundler was run over this
file — `bin/bundle --audience` does not exist at this SHA, so every claim about
which bundles this file lands in is inferred from the recorded 2026-08-20
decision and from `bin/bundle-methodology`'s current `MATCHING_AUDIENCE`, not
observed from a generated bundle. Whether each register rule accurately
describes how Dave wants to be worked with is his judgment, not a reviewable
property, and was not assessed.
Findings: 5 blocking, 2 non-blocking, 2 observations
Dave should inspect: DL-1 (the `audience:` vocabulary cannot express what this
file needs — a design gap, not a value to change), DL-2 (which definition of
"decision session" is canonical), and DL-4 with CORE-2 (rubric criterion 4
versus the recorded "command blocks in core" decision).

## DL-1 — blocking
Claim: The frontmatter selects the exact audience the body forbids.
Location: `docs/global-context/decision-layer.md:4` (`audience: [all-roles,
human]`); contradicted at `:9` ("Execution sessions never receive this file")
Evidence: Verified by running. `bin/aimeta/frontmatter.py:16` defines
`RESERVED_AUDIENCE = {"all-roles", "human"}`, and
`./bin/check-frontmatter docs/global-context/decision-layer.md` exits 0 — nothing
detects the conflict. Inferred by reading `inventory.md:148`, the decision that
governs the field: "Membership is declared in each document's `audience:`
frontmatter; values are bundle names (`chief-of-staff`, `editor`, `executor`…).
`all-roles` expands to every bundle." An executor bundle is named there; the
value `all-roles` reaches it. Verified by running `grep -n "executor"
bin/bundle-methodology`, which returns nothing — the executor bundle does not
exist yet, which is why the contradiction is latent rather than firing today.
Consequence: The moment `bin/bundle --audience executor` is built as recorded,
this file lands in the executor bundle and every execution session receives the
register, pace, and dispatch rules the file's own first paragraph withholds from
it. Rubric criterion 2 makes `audience:` the selector — so where the selector
and the prose disagree, the selector is what runs, and the prose is a claim no
mechanism honours. The root cause is that the vocabulary has no way to say
"every role except execution sessions": `all-roles` over-selects, and
enumerating role slugs means editing this file every time a role is added.
Fix: Dave's call on the mechanism. Either enumerate the decision-session role
slugs here and accept the maintenance, or add an exclusion to the audience
vocabulary (an `exclude:` field, or a reserved `all-decision-roles` value) and
state it where `all-roles` is defined. Whichever is chosen, the bundler check
that lands with it should fail closed on a file whose prose withholds itself
from an audience its frontmatter selects.

## DL-2 — blocking
Claim: The file defines "decision session" by a test that contradicts
`LEXICON.md` and that this very session fails.
Location: `docs/global-context/decision-layer.md:9` ("Rules for decision
sessions — any session that interacts with Dave directly")
Evidence: Verified by reading `LEXICON.md:46-60`, which defines the terms this
file is using: a decision session "produces the artifacts that direct and record
work … but it does not carry out the changes a directive specifies," an
execution session is "an LLM agent session carrying out a directive against a
working tree," and — explicitly — "The boundary is role in the flow, not
capability." Direct interaction with Dave is not the test there. Verified by
demonstration: the session producing this artifact is an execution session by
LEXICON's definition, carrying out
`docs/cycles/global-context-cycle-1-directive-20260821T181500.md` against a
working tree, and it interacts with Dave directly in a terminal. It satisfies
this file's test and fails LEXICON's.
Consequence: The one sentence that decides whether an agent should be reading
this file at all gives the wrong answer for the most common shape of execution
session in this repository. An agent applying it concludes it is a decision
session and applies rules deliberately withheld from it — most consequentially
rule 12's vocabulary and rule 15's block criteria, which govern what it hands
back. And it compounds DL-1: a file whose frontmatter over-selects and whose
prose test also over-selects has no remaining boundary at all.
Fix: State the boundary LEXICON states — a decision session decides and directs;
the work a directive specifies happens elsewhere. Do not define it by who the
session talks to.

## DL-3 — blocking
Claim: Rule 15's body claims a scope its own heading and rule 12 contradict,
and several of its criteria are meaningless at that scope.
Location: `docs/global-context/decision-layer.md:42` ("**Command blocks, in
full.** Every block handed to someone else satisfies all of these")
Evidence: Verified by demonstration against this cycle's own artifacts. Rule 12
defines three block kinds; "every block handed to someone else" reaches all
three. Applied to an execution block: the directive this session is executing
states no expected output and declares no blast radius —
`grep -cE 'expected output|blast radius'` over it returns 0 — so under rule 15's
literal wording the directive is non-conformant, though rule 12 makes it a
different kind of thing entirely, with no shell to terminate and no output line
to predict. The same reading condemns a one-line paste block of a SHA, which
rule 15's own final bullet mandates. Inferred by reading: the heading says
"Command blocks," the body says "Every block," and both cannot be the scope.
Consequence: The rule is either applied literally, which makes conforming
execution blocks and paste blocks impossible to write, or its stated scope is
ignored — and once an agent learns to ignore a stated scope, the shell-safety
criteria in the same list lose their force too. Those are the criteria Dave
named specifically (`inventory.md:94`), so this is the rule that can least
afford to be read loosely.
Fix: Change "Every block handed to someone else" to "Every command block,"
matching the heading and rule 12. The final bullet's one-line paste block is a
paste block, not a command block — state it as its own rule rather than as a
criterion of this one.

## DL-4 — blocking
Claim: Rule 15's first five criteria restate core rule 15, which rubric
criterion 4 forbids.
Location: `docs/global-context/decision-layer.md:42-51`, against
`docs/global-context/core.md:33`
Evidence: Inferred by reading, clause by clause. Core rule 15: "runs verbatim as
pasted, cannot terminate their shell, is safe to re-run, has no placeholders,
states its expected output in one line below, and declares blast radius above it
if destructive." All six reappear here as bullets 1, 2, 3, 4, and 5. Verified by
reading `inventory.md:155`, which records the duplication as intentional:
"Command blocks in core: one compressed conditional … Full criteria are
decision-layer + `command-blocks.md`." Rubric criterion 4 as written admits no
such compression: "The file does not restate a rule that Core or the Decision
Layer already states."
Consequence: Both files reach a decision session in the same bundle, so the
restatement buys nothing there and costs context in the one file sized for a
small window. The durable cost is drift: core rule 13 requires a changed fact to
be updated everywhere it appears, and nothing enforces that across these two
files. The first amendment to the command-block criteria that lands in one file
and not the other produces exactly the one-current-one-stale defect core names.
Fix: Resolve with CORE-2 — either core drops rule 15 and this file is the single
home, or criterion 4 is amended to permit a stated compression with a named
authoritative copy. The two documents must be fixed together; fixing one alone
moves the contradiction rather than closing it.
Related: CORE-2

## DL-5 — blocking
Claim: The file's position in a bundle is load-bearing and stated in prose, but
no `order:` field carries it.
Location: `docs/global-context/decision-layer.md:1-5` (frontmatter); `:9`
("Loads after Core and adds to it")
Evidence: Verified by running. `grep -rn "order:" --include="*.md" .` returns no
document frontmatter carrying the field. `./bin/check-frontmatter` on this file
exits 0, so nothing detects the absence. Inferred by reading: rubric criterion 2
requires `order:` "where its position in a bundle matters," and
`inventory.md:148` fixes this file at 1.
Consequence: "Loads after Core" is asserted in the body of the file whose
loading order is in question, with no field a bundler can sort on. Combined with
DL-1, the two properties that decide where and when this file appears are both
prose claims that no mechanism reads.
Fix: Add `order: 1` to the frontmatter. `bin/aimeta/frontmatter.py` accepts
unknown keys, so this lands safely ahead of the bundler work.
Related: CORE-3

## DL-6 — non-blocking
Claim: Several rules carry "Never X" restatements that rubric criterion 6 cuts.
Location: `docs/global-context/decision-layer.md:13` ("Never stack questions");
`:35` ("Never 'executed.'"); `:36` ("Never shell.")
Evidence: Inferred by reading, against criterion 6's own wording. "Never stack
questions" restates "One question at a time" in the negative and adds nothing.
The two in rule 12 are a closer call: they draw the boundary between adjacent
defined terms, which is the work a glossary entry does, and are the enforcement
half of the three-layers rule at `:39`.
Consequence: `:13` is pure cost. The rule 12 pair is defensible and is flagged
so the decision is made rather than defaulted — a criterion applied
inconsistently across the corpus is worse than either reading applied
consistently, and these two files are the worked example the rest will be judged
against.
Fix: Cut `:13`. Decide explicitly whether criterion 6 reaches contrastive
definitions inside a vocabulary entry; if it does, cut `:35` and `:36` too.

## DL-7 — non-blocking
Claim: Rule 12's `baton` entry states a broader sense than `LEXICON.md` defines,
in a file whose purpose is to fix the vocabulary.
Location: `docs/global-context/decision-layer.md:38`
Evidence: Verified by reading `LEXICON.md:155-161`: "**Baton** — the artifact a
decision session hands its successor decision session … *Not:* a directive, and
*not:* a dispatch." This file says only "A *baton* is the artifact that carries
it," attached to a handoff of any kind — which admits a decision-to-execution
handoff, the case LEXICON excludes. Verified by reading `inventory.md:79` and
`:190`: row D6 already flags a live collision, since `writing/section-writer.md`
uses "baton" for a closing paragraph, and that repository is now merged in.
Consequence: The term arrives in every decision-session bundle in its widest
sense, at the moment a second sense from the merged writing corpus is in the
same repository. A vocabulary rule that is looser than the lexicon it draws from
cannot do the disambiguating work it exists for.
Fix: Carry LEXICON's restriction — a baton passes between decision sessions —
and resolve the writing-repo collision, which `inventory.md:190` already records
as open.

## DL-8 — observation
Claim: The file satisfies criterion 8, but two canonical documents it must
coexist with do not.
Location: `docs/global-context/decision-layer.md:41` (rule 14) and `:37` (rule
12, `Directive`)
Evidence: Verified by reading. This file passes cleanly: rule 14 names three
workload tiers with no vendor names, rule 12 requires route and model stated
every time, and "track" does not appear. Verified by running `grep -n "Opus"`
over the corpus: `skills/spec-review-cycle.md:156` specifies
`Model: <model — default Opus 5>` in the cycle directive format and argues the
default at `:182-197`, and `LEXICON.md:69` states "model *Opus 5*."
Consequence: None for this file — recorded so the criterion-8 sweep over those
two documents later in Pass 1 finds the conflict already located, and so the
tier→name mapping that `inventory.md:172` schedules for
`skills/directive-dispatch.md` is understood as the thing that reconciles them.
Fix: None here. Carry to the cycles that review those documents.

## DL-9 — observation
Claim: Every rule in the file traces to an inventory row dispositioned for the
decision audience, and every such row is present.
Location: whole file, against `docs/global-context/inventory.md` @ 5aa02c5
Evidence: Inferred by reading, row by row over the inventory's decision-audience
rows: A4/A5→3, B1→1, B2/B3→2, B4→5, B5→6, B7→7, B8→4, B10→8, D1–D4/D6–D9→12,
D10→13, D13→14, E1–E3/E5–E10→15, G1→9, G9→10, G10→11. No row marked for the
decision audience is missing, and no rule here lacks a row. Rows dispositioned
elsewhere (B9/G3 discarded, E4 parked, G8 to the engineering layer) are
correctly absent. Outside the rubric — traceability to the triage that produced
the file, not one of the ten criteria.
Consequence: None. Recorded because a completeness claim about a promotion pass
is worth making explicitly rather than leaving as an absence of findings, and
because the same sweep over core also came back clean.
Fix: None.
