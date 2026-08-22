# Review: context-sets/ai-native-engineering.md — cycle 4

Verdict: changes-required
Reviewed: `context-sets/ai-native-engineering.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11a)
Date: 2026-08-21
Scope: the whole file — frontmatter and all seven body sections — against all
ten criteria of `docs/global-context/review-rubric.md` @ `7310937`. Cycles 1–3
were narrow self-reviews of single edits; this is the file's first full
ten-criteria gate. Criterion 4 judged line-by-line against
`docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, and `operating-model.md` @ `7310937`. Mechanical sweeps run
(verified by running `grep`): retired terms, vendor and model names,
path-shaped references.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `operating-model.md`, `context-sets/base.md`,
`context-sets/spec-and-change-discipline.md`, `roles/chief-of-staff.md` (existence
and title only), `bin/bundle-methodology`, `decisions/log.md`
Not inspected: the bodies of `roles/chief-of-staff.md` and the other eight
`roles/` documents. This matters to A2 and A5, which assert that the role
roster and the per-role one-liners belong in `roles/` — the assertion rests on
`operating-model.md`'s change-flow parentheticals and on the `roles/` directory
listing, not on reading each role document. If a role document does *not*
already state its own one-liner, A5's fix acquires a step. `skills/directive-dispatch.md`
was not read; A7 reports the retired term at L54, not the state of that file.
Findings: 11 — 5 blocking, 3 non-blocking, 3 observations
Prior cycle: `reviews/ai-native-engineering-cycle-3.md`
Dave should inspect: nothing. The two rules worth saving (A1) are small and
their target is unambiguous.

## Criterion 10 — disposition

**merge-into: `operating-model.md`.**

The file lands in bundles — five context sets sit downstream of `base` and this
one is reachable — but it contributes exactly two rules that no other file in
the bundle states, and both are one sentence long:

- **The review boundary** (L46): "Whoever produces an artifact does not approve
  it." Not in Core, the Decision Layer, `LEXICON.md`, or `operating-model.md`.
  `operating-model.md` implies it structurally by assigning stages to distinct
  roles, but never states it as a rule.
- **Spec authorship / spec review separation** (L47–48): the Architect that
  drafts a spec does not act as the Spec Reviewer that certifies it. Also
  unstated in the four foundation files.

Everything else is restated. The team roster restates the roles
`operating-model.md` §Change flow already names in its stage parentheticals
(A2); the Separation-of-concerns bullets restate the stage descriptions those
same parentheticals attach to (A5); the tranche paragraph restates two
`LEXICON.md` entries (A3); the anti-patterns restate `operating-model.md`
§Responsibilities "Must not" as slogans (A4); the summary and core premise
restate `operating-model.md` §Summary and Core rule 5 with rationale attached
(A6, A9).

Two sentences do not earn a 94-line file in every bundle. Both belong under
`operating-model.md` §Responsibilities, beside the Test Designer / Coder
separation the same document already carries at `:106`.

**Cost of the merge.** Lower than `base.md`'s. This file is not in the
`bin/bundle-methodology` spine, is not named in `DEC-000140`, and is not in
`CLAUDE.md`'s required-reading list. It is referenced by
`context-sets/spec-and-change-discipline.md:15` ("complements … and
`ai-native-engineering.md` (roles)"), which is a `bin/bundle` edge that would
need removing in the same package, and no context set declares
`depends-on: [ai-native-engineering]`.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — A5, A3 |
| 2 | `audience:` is the selector | partial — A10 |
| 3 | No path references | fail — A5, A3 |
| 4 | Core states it → remove it here | fail — A2, A3, A4, A5, A6 |
| 5 | Agent instruction, not authoring principle | fail — A9 |
| 6 | Instructions, not rationale | fail — A6, A9 |
| 7 | Session kind is explicit | fail — A11 |
| 8 | Tiers, not model names | fail — A8 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |

## Counts (instruction 4)

- **Rules restated from Core / Decision Layer / LEXICON / operating-model:** 20
  across 6 of the 7 body sections. By section: Summary 3; Core premise 1; Team
  model 8 of 9 roles; Separation of concerns 6 of 7 bullets; Tranche paragraph 2
  (`LEXICON.md` §Tranche, §Open spec delta); Anti-patterns 5 of 7.
- **Path-shaped references:** 3 — `skills/directive-dispatch.md` (L55),
  `context-sets/spec-and-change-discipline.md` (L69), `roles/chief-of-staff.md`
  (L69).
- **Vendor and model names:** 4 — "Claude Code" (L53), "Claude, Codex, ChatGPT"
  (L94).
- **Retired terms:** 1 use plus 1 in a filename — "dispatched" (L54), and
  `directive-dispatch.md` inside the path at L55.

## A1 — blocking
Claim: The file does not earn its place; two sentences out of 94 lines are
unique, and both belong in `operating-model.md`.
Location: `context-sets/ai-native-engineering.md` (whole file)
Evidence: Verified by reading — every section mapped against the four foundation
files @ `7310937`; the mapping is enumerated in A2–A6 and summarised in the
Counts block. Verified by running: `grep` sweeps for retired terms, vendor
names, and path-shaped references.
Consequence: 94 lines of bundle budget for two rules. Worse than the waste: an
agent reading the roster here and the stage parentheticals in
`operating-model.md` gets nine role names in one file and eight in the other,
with no statement that they are the same list. The one that differs — Chief of
Staff — looks like a role this document adds, when in fact it is a role
`operating-model.md` omits.
Fix: Move L46 and L47–48 into `operating-model.md` §Responsibilities, as two
bullets beside the existing Test Designer / Coder separation. Add "Chief of
Staff" to `operating-model.md`'s role vocabulary in the same edit (A2). Retire
this file and remove the reference at
`context-sets/spec-and-change-discipline.md:15`.

## A2 — blocking
Claim: The team roster restates the roles `operating-model.md` §Change flow
already names, and differs from it by one entry without saying so.
Location: `context-sets/ai-native-engineering.md:27-37`
Evidence: Verified by reading. This file lists PM/EM/Owner, Chief of Staff,
Architect Agent, Spec Reviewer Agent, Test Designer Agent, Coder Agent, Reviewer
Agent, Skeptic/Risk Agent, Release Manager Agent. `operating-model.md:101-110`
names, in stage parentheticals: PM/EM/Owner, Architect, Spec Reviewer, Test
Designer, Coder, Reviewer, Skeptic/Risk, Release Manager, Dave. Eight of nine
match. Chief of Staff appears only here.
Consequence: Two rosters in one bundle, differing by one entry, neither
declaring itself canonical. An agent asked which roles exist has two answers and
Core rule 9 obliges it to surface the disagreement rather than pick one — which
is the correct behaviour and a waste of a turn.
Fix: Delete L27–37. Add "Chief of Staff" to `operating-model.md` where the role
vocabulary is established, so the canonical roster is complete in one place.

## A3 — blocking
Claim: The tranche paragraph restates two `LEXICON.md` entries and reaches for
two other files by path to do it.
Location: `context-sets/ai-native-engineering.md:64-69`
Evidence: Verified by reading. This file: "A **tranche** is a scope of agreed
spec proposed for implementation as one body of work … It is also the unit an
**open spec delta** is bounded by: spec edits made while the tranche executes
land on its spec branch and are gated together at reconciliation." `LEXICON.md`
@ `7310937` §Spec state: "**Tranche** — one concurrent workstream of build
work"; "**Open spec delta** — the interval during which a tranche's spec branch
carries edits that the default branch does not … A delta is bounded by its
tranche and never spans two." Same two definitions, different wording.
Consequence: `LEXICON.md` is the term registry and carries `order: 2`, so it is
in the bundle ahead of this file. The reader meets `tranche` defined once as
"one concurrent workstream of build work" and again, sixty-odd lines later, as
"a scope of agreed spec proposed for implementation as one body of work." These
are not the same definition — the first is about concurrency, the second about
scope and agreement — and nothing tells the reader they are meant to be.
Fix: Delete L64–69. If the scope-and-agreement sense is meant to be part of the
term, it belongs in the `LEXICON.md` entry, not in a second definition
elsewhere.
Related: A5

## A4 — blocking
Claim: Five of the seven anti-patterns restate `operating-model.md`
§Responsibilities "Must not", and two of the seven name vendors.
Location: `context-sets/ai-native-engineering.md:86-94`
Evidence: Verified by reading. L88 ("agent says it works") → Core rule 5. L89
("tests are green, therefore ship") → `operating-model.md:76`. L90 ("mocks imply
live behavior") → `operating-model.md:78`. L92 ("undocumented assumptions") →
`operating-model.md:69`. L94 ("policy living only in Claude, Codex, ChatGPT, or
another tool-specific surface") → `operating-model.md:79`. L93 ("hidden
vendor/tool dependencies") is the same rule as L94 stated abstractly — the
section says it twice. Not restated: L91 ("review summarizes only what changed,
not what could be wrong").
Consequence: The section reads as a list of seven distinct failure modes; five
are already prohibitions binding from `operating-model.md` in the same bundle,
and two of the seven are the same prohibition written twice. The one genuinely
new item (L91) is buried at position four.
Fix: Delete L86–94. L91 states something `operating-model.md:107-108` gestures
at ("skeptic/risk asks 'where is this lying to us?'") but does not make a rule;
if it is wanted as a rule it should move there as one sentence.
Related: A8

## A5 — blocking
Claim: Six of the seven Separation-of-concerns bullets restate the stage
descriptions in `operating-model.md` §Change flow.
Location: `context-sets/ai-native-engineering.md:51-62`
Evidence: Verified by reading. L56 (Coder creates implementation) →
`operating-model.md:106`. L57 (Test Designer defines how correctness is
evaluated) → `:105`. L58–59 (Spec Reviewer gates spec quality) → `:101`. L60
(Reviewer checks maintainability, correctness, consistency) → `:107`. L61
(Skeptic/Risk looks for false confidence) → `:108`. L62 (Release Manager
assesses whether evidence suffices) → `:109`. Not restated: L51–55, the Chief of
Staff bullet.
Consequence: Six one-line role summaries duplicating six stage descriptions in
the same bundle. The Chief of Staff bullet, the only one that is not a
duplicate, then points at `roles/chief-of-staff.md` by path (L69) for the detail
— so the file neither states the thing nor is the place it is stated.
Fix: Delete L56–62. The Chief of Staff bullet's operative content — assesses
state, proposes tranches, decomposes into ordered change packages, Dave approves
the decomposition before agentic work begins — is a stage `operating-model.md`
§Change flow does not have, sitting logically before its step 2. Move it there
as a stage, stripped of the vendor name (A8) and the retired term (A7), or
confirm it is already stated in `roles/chief-of-staff.md` and delete it here.
Related: A2, A7, A8

## A6 — non-blocking
Claim: Summary and Core premise restate `operating-model.md` §Summary and Core
rule 5, and attach rationale to both.
Location: `context-sets/ai-native-engineering.md:13-23`
Evidence: Verified by reading. L15 ("treating LLMs and LLM agents as the primary
implementation staff") → `operating-model.md:16`. L17 ("The goal is not to make
the human read all code") → `operating-model.md:18`. L21–23 ("Agents are useful
but structurally untrustworthy … their claims must be checked by evidence") →
Core rule 5. L17 and L23 are both argument for a rule stated elsewhere, which is
criterion 6.
Consequence: The bundle opens two files with the same thesis. The rationale in
particular is the kind of text that survives edits to the rule it justifies,
because nothing links them.
Fix: Delete L13–23.

## A7 — non-blocking
Claim: A retired term is in use.
Location: `context-sets/ai-native-engineering.md:54`
Evidence: Verified by running — `grep -niE '\bdispatch(ed|es|ing)?\b'` returns
L54: "Each package is then dispatched as a directive derived from the
decomposition doc." `LEXICON.md:63-64` @ `7310937`: "**Dispatch** — retired
2026-08-21. Write 'hand the directive to an execution session,' or 'direct.'"
Consequence: The retirement is one commit old and this is a live use of the
retired word in a file that ships in bundles. `LEXICON.md`'s touch rule (L14–15)
makes conforming it mandatory at the next edit of this file, and this review is
that occasion.
Fix: "Each package is then handed to an execution session as a directive derived
from the decomposition doc." The path `skills/directive-dispatch.md` at L55 also
carries the retired term in a filename; that file is out of scope here and its
name is its own question, but the reference goes away with A5's deletion either
way.
Related: A5

## A8 — non-blocking
Claim: Vendor names appear in two places.
Location: `context-sets/ai-native-engineering.md:53,94`
Evidence: Verified by running — `grep -niE 'claude|codex|chatgpt'` returns L53
("it operates in chat, not inside a Claude Code session") and L94 ("policy
living only in Claude, Codex, ChatGPT, or another tool-specific surface").
Consequence: L53 is the more damaging of the two: it defines the Chief of Staff
boundary in terms of one vendor's product, so the rule stops being stateable the
moment the toolchain changes, and an agent running somewhere else cannot tell
whether the boundary applies to it. Core §Vocabulary already draws exactly this
line vendor-neutrally — decision session versus execution session — and that is
the distinction L53 is reaching for.
Fix: L53 → "it operates as a decision session, not an execution session." L94 →
covered by A4's deletion.
Related: A4, A5

## A9 — observation
Claim: The Summary's second paragraph is an authoring principle, not an agent
instruction.
Location: `context-sets/ai-native-engineering.md:17`
Evidence: Verified by reading. "The goal is not to make the human read all code.
The goal is to make the system produce enough artifacts to support responsible
decisions." No verb in it is addressed to the agent reading it; it explains why
the methodology is shaped as it is.
Consequence: Criterion 5. It costs bundle budget and instructs nobody.
Fix: Subsumed by A6.

## A10 — observation
Claim: No `order:`, and three frontmatter fields that nothing reads.
Location: `context-sets/ai-native-engineering.md:1-9`
Evidence: Verified by reading and running. `audience: [all-roles, human]` — both
reserved values, valid per `bin/aimeta/frontmatter.py:16`. No `order:`.
`context-set:`, `purpose:`, and `include-when:` are read by neither `bin/bundle`
(which reads `depends-on:`) nor `bin/bundle-methodology` (which reads
`audience:`).
Consequence: `include-when: Any multi-role or implementation chat` is an
instruction to whoever assembles context — criterion 5 — and no assembler reads
it. The position problem is moot if A1 is taken.
Fix: Dissolves with the file under A1.

## A11 — observation
Claim: Session kind is never stated, and the file mixes both.
Location: `context-sets/ai-native-engineering.md:1-11`
Evidence: Verified by reading. No declaration. L51–55 describes a decision
session's work (assess state, propose tranches, decompose, get Dave's approval);
L56–62 and L73–82 describe execution-session obligations.
Consequence: Criterion 7. An execution session receiving this file cannot tell
that the Chief of Staff bullet does not apply to it.
Fix: Dissolves with the file under A1. If the alternative were taken, the honest
declaration is "both kinds," which is itself a sign the file is two files.
