# Review: docs/global-context/core.md — cycle 1

Verdict: changes-required
Reviewed: docs/global-context/core.md @ 5aa02c5
Reviewer: Spec Reviewer Agent
Date: 2026-08-21
Scope: the full file — frontmatter and all fifteen rules — against all ten
criteria of `docs/global-context/review-rubric.md` @ 5aa02c5, plus the three
additional checks the cycle directive names: internal consistency with the
decision layer, followability by an agent holding only the bundle and the
repository, and whether the file obeys its own rule 14.
Cross-checked: `docs/global-context/decision-layer.md` @ 5aa02c5 (consistency
and duplication); `docs/global-context/inventory.md` @ 5aa02c5 (provenance of
each rule, not reviewed); `bin/aimeta/frontmatter.py`, `bin/bundle-methodology`,
`bin/check-frontmatter` (what the frontmatter machinery actually enforces);
`skills/spec-review-cycle.md` (review-artifact filename convention);
`LEXICON.md` (session and block vocabulary).
Not inspected: the rubric itself was applied, not reviewed. `inventory.md` was
read for provenance only, per the directive. No bundler was run over these
files — `bin/bundle --audience` does not exist at this SHA, so every claim about
bundle membership is inferred from the recorded 2026-08-20 decision and from
`bin/bundle-methodology`'s current `MATCHING_AUDIENCE`, not observed from a
generated bundle. Prose style beyond rubric criterion 6 was not assessed.
Findings: 3 blocking, 4 non-blocking, 1 observation
Dave should inspect: CORE-1 (the scope of rule 14 is a corpus-wide question,
not a wording fix) and CORE-2 (whether rubric criterion 4 or the recorded
"command blocks in core" decision gives — the two cannot both stand).

## CORE-1 — blocking
Claim: Rule 14 states the filename convention without the scope qualifier the
rubric itself carries, so as written it condemns almost every file in this
repository, including `core.md`.
Location: `docs/global-context/core.md:32`
Evidence: Verified by running. `git ls-files '*.md' | wc -l` returns 217;
`git ls-files '*.md' | grep -cE '[0-9]{8}T[0-9]{6}\.md$'` returns 2. So 215 of
217 markdown files fail the rule as literally stated. `ls reviews | wc -l`
returns 70 and none carries a timestamp — and the two artifacts this very
directive orders (`reviews/core-cycle-1.md`, `reviews/decision-layer-cycle-1.md`)
are named by `skills/spec-review-cycle.md`'s `<stem>-cycle-<n>.md` convention,
which rule 14 forbids. Inferred by reading: rubric criterion 9 scopes the same
rule to "any filename the file **prescribes or generates**"; rule 14 drops that
scope. Inventory row F5, the rule's source, is about generated names ("Never
generate 'random' strings … for filenames").
Consequence: An agent that reads core literally and then writes a review
artifact, a policy, or a role document has a direct conflict between two rules
it holds and no stated way to resolve it. It either invents a scope the text
does not grant, or it names a canonical document with a timestamp and breaks the
`last-reviewed:` pointer convention that `bin/flip-agreed` validates. Both
outcomes are silent.
Fix: Scope the rule to the names an agent generates — session artifacts, retros,
directives, captured output — and say that a canonical document keeps its stable
descriptive name. Rubric criterion 9's own wording is the model.

## CORE-2 — blocking
Claim: Rule 15 governs a situation only a decision session is in, yet core is
the one file every execution session receives.
Location: `docs/global-context/core.md:33` ("A command block handed to a
human"); related at `:16` ("Chat is never the sole record") and `:14` ("Dave
decides. You propose.")
Evidence: Inferred by reading. Rubric criterion 7 requires the file to say
"nothing only the other kind needs." `decision-layer.md:9` reserves
Dave-facing interaction to decision sessions; handing a human a command block is
that interaction. Verified by reading `inventory.md:93-100`, which records the
audience for inventory rows E1/E2/E3/E8 as "both (core: compressed
conditional)" — the duplication is deliberate, which is why this is a design
question and not a slip.
Consequence: Two costs, both real. First, an execution session carries a rule it
can never trigger, in the file explicitly "sized for a small context window"
(`inventory.md:146`). Second, and worse, it forces the same six clauses into
both files: five of core rule 15's six clauses reappear at
`decision-layer.md:42-51`. Core rule 13 — "a changed fact changes everywhere it
appears" — then makes any future edit to command-block criteria a two-file edit
with no mechanism enforcing it, and one current plus one stale is a defect by
core's own definition.
Fix: Dave's call between two consistent designs — drop rule 15 from core and let
the decision layer be the single home (rubric criterion 4 as written), or keep
the compressed conditional in core and amend criterion 4 to permit a stated
compression. Either resolves it; neither half of the current arrangement does.
Related: DL-4

## CORE-3 — blocking
Claim: The file's position in a bundle is load-bearing and stated in prose, but
no `order:` field carries it.
Location: `docs/global-context/core.md:1-5` (frontmatter); `:9` ("Load first")
Evidence: Verified by running. `grep -rn "order:" --include="*.md" .` returns no
document frontmatter carrying the field — only prose uses of the word.
`./bin/check-frontmatter docs/global-context/core.md` exits 0, so nothing today
detects the absence. Inferred by reading: rubric criterion 2 requires `order:`
"where its position in a bundle matters"; `inventory.md:148` fixes the sequence
(core 0, decision layer 1, role 2, skills 3) and `inventory.md:154` states "Core
references nothing and is order 0 in every bundle."
Consequence: The ordering exists only as prose inside the file being ordered. A
bundler assembling by `audience:` has nothing to sort on and will emit files in
whatever order it discovers them — which for the file whose first instruction is
"Load first" is precisely the failure the field exists to prevent. Adding
`order:` is safe today: `bin/aimeta/frontmatter.py` validates known fields and
flags only excluded ones, so an unknown key passes.
Fix: Add `order: 0` to the frontmatter. The bundler work that reads it is
already a recorded follow-up (`inventory.md:175`).
Related: DL-5

## CORE-4 — non-blocking
Claim: Rule 13's bolded statement and its body state two different scopes for
the same rule.
Location: `docs/global-context/core.md:31`
Evidence: Inferred by reading. The bold reads "A changed fact changes everywhere
it appears"; the body narrows to "find every place **in the document** that
states the same thing." Verified by reading `inventory.md:125`: source row G6 is
the narrow form ("change a value everywhere in the document"), so the bold is a
generalization introduced in this file.
Consequence: The two readings differ exactly where it matters. Under the bold,
an agent updating a rule in core must also update its restatement in the
decision layer — which is what CORE-2 shows is required. Under the body, it need
not, and the stale copy is not a defect. An agent editing both files has no
stated answer.
Fix: Pick one scope and state it in both places. Given CORE-2, the wider reading
is the one the corpus needs.

## CORE-5 — non-blocking
Claim: The header sentence states an authoring principle rather than an agent
instruction, and introduces a term the bundle never defines.
Location: `docs/global-context/core.md:9`
Evidence: Inferred by reading. "This file references nothing" tells the reading
agent nothing to do — it is a constraint on whoever writes the file, which
rubric criterion 5 sends elsewhere. "a domain layer may add rules but never
waives these" likewise instructs the author of a domain layer. Verified by
reading `decision-layer.md:9`: that file calls itself "Decision Layer" and says
it "Loads after Core and adds to it" — it never uses the term "domain layer," so
an agent holding both files cannot tell whether the two names denote the same
thing.
Consequence: An agent that receives core plus one other layer and hits a
conflict must decide whether the second file is a "domain layer" whose rules
core outranks. The term that would settle it is used once, undefined, and not
picked up by the file it appears to name.
Fix: Cut "This file references nothing." Restate the precedence clause as an
instruction to the reader — a rule elsewhere that conflicts with one here does
not waive it — and use one name for the thing that adds rules, matching whatever
the decision layer calls itself.

## CORE-6 — non-blocking
Claim: Several rules carry "Never X" restatements or trailing justifications
that rubric criterion 6 cuts.
Location: `docs/global-context/core.md:29` ("No improvisation, no silent partial
execution"); `:31` ("One current and one stale is a defect"); `:32` ("Never
'random' strings, hashes, or UUIDs")
Evidence: Inferred by reading, against criterion 6's own wording: "'Never X'
restatements of a stated rule and trailing justifications are cut." Each cited
clause restates the rule immediately preceding it in the negative or asserts
its consequence.
Consequence: Small per instance, and cumulative in the file whose stated design
constraint is a small context window. It also sets the pattern that the rest of
the corpus will be judged against under criterion 6 — the two foundation files
are the worked example.
Fix: Cut the three clauses. Note that `:32`'s "never random strings" is the
clause inventory row F5 actually carries, so if rule 14 is rescoped per CORE-1
it may be the surviving half rather than the cut one — resolve CORE-1 first.

## CORE-7 — non-blocking
Claim: Rule 6 is unscoped and, read as written, is not followable.
Location: `docs/global-context/core.md:21`
Evidence: Inferred by reading. "Every claim carries its class … A claim without
a class is not a claim" attaches no boundary — every declarative sentence an
agent emits is a claim, so the literal requirement is a provenance tag on every
sentence of every output. This artifact does not do that, and no artifact in
`reviews/` does.
Consequence: A rule no output can satisfy is either ignored wholesale, which
costs the discipline it exists to create, or applied literally, which makes
output unreadable. Neither is the intent, and the file does not say which.
Fix: Scope it to the claims that carry weight — assertions about state, results,
verification, and completeness — as the sources in inventory rows C2/C3 do.

## CORE-8 — observation
Claim: Rule 12 drops the read-HEAD-before-retrying clause from the policy row it
was promoted from.
Location: `docs/global-context/core.md:30`
Evidence: Verified by reading `inventory.md:108`, row F1: "Read it back before
reporting it landed; **read HEAD before retrying**; the repo's own log is the
source of record." Rule 12 carries the read-back and the F3 content clause
("Confirm the correct content landed") but not the retry clause. Inventory row
F2, the adjacent retry rule, is marked D (discard); F1 is marked H with the note
"core; +F3 clause," so the omission is not covered by the F2 discard. Outside
the rubric — this is traceability to the triage that produced the rule, not one
of the ten criteria.
Consequence: An agent whose write appears to fail retries against unknown state
and lands the change twice. This is the specific failure the source policy
existed to prevent, and it is the one clause of the row that is gone.
Fix: Add the clause, or record that it was dropped deliberately when the
compression to one line was made.
