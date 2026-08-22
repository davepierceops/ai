# Review: policies/source-of-truth-policy.md — cycle 1

Verdict: changes-required
Reviewed: policies/source-of-truth-policy.md @ 2b9c856
Baseline: none — first Pass 1 review. The file was a cycle-12 merge target,
edited only to receive the five-step Required discipline from the retired
boundaries/vendor-tooling-boundary.md and to reword the adapter paragraph per
that review's N2; its pre-existing text has never been through a rubric gate.
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file — frontmatter and all six body sections — against all ten
criteria of docs/global-context/review-rubric.md @ 2b9c856. Two passes. (a) The
cycle-12 merge checked, verified by running `git diff cceef9a 2b9c856 --
policies/source-of-truth-policy.md`: §Adapter discipline arrived with its five
steps, and the adapter paragraph was reworded to drop three product names and
the path reference to the retired boundary file — so the merge did remove
vendor names at the site it touched. What it did not do is reconcile the rest of
the file, and instruction 3 makes the surviving path-shaped references and
vendor names findings now; both required lists are below. (b) All ten criteria
applied to the current text. Criterion 4 judged line by line against
docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md,
and operating-model.md @ 2b9c856. Mechanical sweeps run, all verified by running
grep: path-shaped references, vendor and product and tool names, retired terms.
All nine in-scope files cross-checked against each other for a term or rule
stated twice — SOT2 and SOT5 are that pass's results, and both are against
operating-model.md. The cross-reference at :63-64 was checked against the
document it names rather than taken on its face; SOT1 is what that check found.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
operating-model.md, context-sets/spec-and-change-discipline.md,
context-sets/testing-and-verification.md,
context-sets/production-grade-software.md,
boundaries/human-review-boundary.md, policies/verification-boundary-policy.md @
2b9c856; reviews/spec-and-change-discipline-cycle-6.md S4 (the deletion SOT1
turns on); the cycle-12 revision directive (the merge instruction and the N2
rewording).
Not inspected: the rubric was applied, not reviewed. roles/spec-reviewer-agent.md
was not read, so the Depth 1 / Depth 2 / Depth 3 scan levels at :70-71 were
confirmed undefined *within the nine* by running grep and were not checked for
whether that document defines them or defines them as this file describes;
SOT3's claim is about their absence from the bundle, not about their content.
specs/prd-template.md and specs/trd-template.md were not read; SOT3 treats them
as bundle-absent, which `bin/bundle-methodology` supports, and makes no claim
about whether they say what :16-18 says they say. Whether the five-step adapter
discipline survived the merge complete — that no step of
boundaries/vendor-tooling-boundary.md's Required discipline was dropped — was
not verified against the deleted file; the cycle-12 report is the record for
that. The hard-stop procedure at :49-57 was not tested against any real
conflict. Files outside the nine were not read. The one "track" occurrence, at
:22, was swept against LEXICON.md's Track retirement and is reported there, at
reviews/LEXICON-cycle-12.md L11; no edit is owed here for it. No bundler was
run; `bin/bundle-methodology` was read and neither includes this path nor
consumes `order:`. The directive's excluded items were not assessed.
Findings: 7 — 3 blocking, 2 non-blocking, 2 observations
Prior cycle: none — first artifact for this document
Dave should inspect: SOT1 — this file's §Keeping derived artifacts honest rests
its only rule on "the document-consistency principle in
context-sets/spec-and-change-discipline.md", and cycle 12 deleted that principle
from that file. The rule survives as Core rule 13, which is broader; whether the
sentence is rewritten against Core or dropped is a call, not a mechanical fix.
And SOT2 — the canonical order is now stated in full in two files that land in
the same bundle, reported symmetrically at reviews/operating-model-cycle-5.md O8.

## Criterion 10 — disposition

**retain-with-changes.**

The file earns its place on three sections that nothing else in the nine states:

- **§Conflicts are a hard stop** (:42-57), specifically the three-step
  procedure: stop work on the conflicted item; surface the conflict in the
  current response, naming both artifacts, quoting the contradicting content,
  and saying explicitly that this is a hard stop; wait for Dave.
  operating-model.md:39-40 asserts that a conflict *is* a hard stop and states no
  procedure. The two closing prohibitions — "Do not silently reconcile. Do not
  pick the version that is easier to implement" — are stated nowhere else.
- **§Adapter discipline** (:31-40) — the five steps, arrived from the retired
  boundaries/vendor-tooling-boundary.md. operating-model.md:86 prohibits storing
  durable policy only in vendor tooling and gives no procedure for creating an
  adapter correctly.
- **The enumeration of what counts as vendor-specific AI tooling** (:27-29) —
  agent frameworks, skills, hooks, memory files, IDE integrations, and the
  instruction files they read. This is the sentence that makes the prohibition
  applicable to a specific artifact, and it is unique to this file.

Three sections do not earn their place as written: §Canonical order duplicates
operating-model.md §Source of truth (SOT2); §Keeping derived artifacts honest
rests on a deleted principle (SOT1); §Proactive drift detection describes a
role's behavior and leans on two path-shaped references and three undefined
terms (SOT3, SOT6). The finding list is the edit list, and the file is coherent
after it.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — SOT1, SOT3 |
| 2 | `audience:` is the selector | partial — `[all-roles, human]`, both reserved (`bin/aimeta/frontmatter.py:16`); no `order:`, though the file states the canonical order operating-model.md (`order: 3`) also states. No consequence demonstrable: verified by running, no bundler consumes `order:`, so no entry is opened |
| 3 | No path references | fail — SOT3 (4 sites) |
| 4 | Core states it → remove it here | partial — zero restatements of the Decision Layer; :59-64's rule is a narrower form of Core rule 13 reached through a broken pointer (SOT1). The larger duplication is against operating-model.md: SOT2, SOT5 |
| 5 | Agent instruction, not authoring principle | partial — SOT6 |
| 6 | Instructions, not rationale | pass — §Purpose states the rule's effect in one clause and every other section issues instructions |
| 7 | Session kind is explicit | **fail** — SOT4 |
| 8 | Tiers, not model names; route and model, not track | partial — zero model names and zero retired terms in the retired sense, verified by running grep; one vendor name at two sites, SOT2 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |

## Required lists (instruction 3)

- **Path-shaped references: 4.** :16 — "**PRD** (`specs/prd-template.md`)"; :18
  — "**TRD** (`specs/trd-template.md`)"; :64 —
  "`context-sets/spec-and-change-discipline.md`"; :71 — "See
  `roles/spec-reviewer-agent.md`." Verified by running grep for backticked
  repo-relative paths. :64 is also SOT1; the other three are SOT3.
- **Vendor, product, and tool names: 1 name at 2 sites.** "GitHub" — :21 ("the
  artifact a GitHub Issue is cut from") and :22 ("5. **GitHub Issues** —
  **derived PM artifacts**"). Verified by running grep. Zero model names, zero
  tool names. Both sites are SOT2.
- **Retired terms: 0 in the retired sense.** "track" appears once, at :22 ("They
  track and organize work"), in the ordinary verb sense; it is reported against
  LEXICON.md's carve-out wording at reviews/LEXICON-cycle-12.md L11, not here.

## SOT1 — blocking
Claim: §Keeping derived artifacts honest attributes its rule to a principle in
context-sets/spec-and-change-discipline.md that cycle 12 deleted from that file.
Location: policies/source-of-truth-policy.md:59-64
Evidence: Verified by reading. The section reads: "When a canonical document
changes, derived artifacts downstream of it may go stale. The agent making the
change is responsible for flagging which derived artifacts now need updating,
per the document-consistency principle in
`context-sets/spec-and-change-discipline.md`." Verified by running `grep -in
"document.consistency\|every instance of a changed value"
context-sets/spec-and-change-discipline.md` @ 2b9c856 — no match. Verified by
reading reviews/spec-and-change-discipline-cycle-6.md S4, which directed the
deletion of that file's ":185-187" bullet — "**Document consistency.** When
editing a document, find *every* instance of a changed value across the whole
document and update all of them" — on the ground that it was a *narrower*
restatement of Core rule 13 ("A changed fact changes everywhere it appears"),
which requires it across every other document too. Verified by running `git diff
cceef9a 2b9c856 -- context-sets/spec-and-change-discipline.md`: the bullet is
gone, and this file was edited in the same commit without the reference being
swept.
Consequence: The rule this section states is real and survives — Core rule 13
carries it, more strongly. What is broken is the support: the only justification
offered for the agent's flagging obligation names a principle that no longer
exists anywhere, in a document that no longer contains it. Inside a generated
bundle the pointer is unfollowable regardless (criterion 1 and 3), so the
sentence arrives as an obligation with its authority named and absent; outside a
bundle, an agent that does follow it reads the whole file and finds nothing,
which is the worse outcome because it looks like the agent missed something. And
S4's reasoning cuts against restating it here in the same narrow form: the
deleted bullet stopped at "the whole document", where the obligation this
section needs is the cross-document one.
Fix: State the rule and drop the attribution: "When a canonical document
changes, derived artifacts downstream of it may go stale. The agent making the
change flags which derived artifacts now need updating." Core rule 13 states the
general principle and reaches this file's readers in the same bundle, so nothing
is lost and the criterion-3 defect goes with the sentence.
Related: SOT3

## SOT2 — blocking
Claim: §Canonical order states the five-step order operating-model.md §Source of
truth also states, and names the tracker vendor where operating-model.md
deliberately hedges it.
Location: policies/source-of-truth-policy.md:14-29
Evidence: Verified by reading both @ 2b9c856. This file :16-24 enumerates, in
five numbered items: PRD, canonical for what and why; TRD, canonical for how;
acceptance criteria derived from the PRD, owned by Dave; per-change architecture
summary derived from the TRD; and "**GitHub Issues** — **derived PM artifacts**.
They track and organize work. An Issue is a *view onto the specs*, not an
independent source of truth." operating-model.md:34-40: "The order is: **PRD**
(product) → **TRD** (technical) → acceptance criteria → per-change architecture
summary → **tracker issues** (currently GitHub Issues). Tracker issues are
derived PM artifacts — a view onto the specs, never an independent source of
truth. If a derived artifact conflicts with a canonical one … it is a **hard
stop**." The order is identical and the derived-artifact claim is
near-verbatim. Verified by running grep: both files carry `audience: [all-roles,
human]`, so both land in every bundle together. Verified by reading: this file
names the vendor twice — as the label of rank 5 and at :21 as the artifact an
architecture summary is cut into — with no hedge, where operating-model.md names
it once and marks it provisional with "currently".
Consequence: An agent holding the bundle gets the canonical order twice. The two
do not contradict on the order, so no work stops — the cost is elsewhere. First,
the hedge: "currently" is the anti-lock-in signal, and stripped of it this file
seats a specific tracker product at rank 5 of the source-of-truth hierarchy, in
the document whose title claims authority over exactly that question. An
adopting project on a different tracker reads its own hierarchy as naming a
product it does not use. Second, Core rule 13: any future change to the order,
or to the tracker, has to find both copies. This file is the one more likely to
be missed by an edit prompted by the change flow, and the one whose name makes a
reader treat it as governing.
Fix: One home, and the recommendation is this file — it is named for the
question and already carries the hard-stop procedure operating-model.md only
names — with operating-model.md §Source of truth compressing to the hard-stop
rule and the one line that specifications are canonical. Either way the vendor
is hedged in whichever copy survives: rank 5 becomes "**tracker issues**
(currently GitHub Issues)" and :21 becomes "the artifact a tracker issue is cut
from". Reported symmetrically at reviews/operating-model-cycle-5.md O8; the two
findings are one edit.
Related: SOT5

## SOT3 — blocking
Claim: Four path-shaped references, two of them to spec templates no methodology
bundle carries, and one carrying the only definition of three terms this file
uses.
Location: policies/source-of-truth-policy.md:16, :18, :64, :71
Evidence: Verified by running grep for backticked repo-relative paths — four
sites, enumerated in the Required lists above. Verified by reading each. :16 and
:18 attach `specs/prd-template.md` and `specs/trd-template.md` to the two ranks
the whole hierarchy rests on. :64 is SOT1's broken pointer. :71 is the load-
bearing one: ":70-71" reads "Continuity scans run automatically on every spec
revision (Depth 1) and on demand at greater scope (Depth 2, Depth 3). See
`roles/spec-reviewer-agent.md`." Verified by running `grep -nE 'Depth [123]'`
over all nine in-scope files — two hits, both on this line. Verified by reading
`bin/bundle-methodology`: its file set is a hardcoded four-file spine plus
matching skills, so no methodology bundle carries specs/ or roles/.
Consequence: Criterion 3 at four sites and criterion 1 behind it. The concrete
failure is Depth 1 / 2 / 3. They are presented as fixed scan levels with defined
scopes — one automatic, two on demand — and the file states what triggers each
without stating what any of them covers, then names the document that does. An
agent in a bundle is told a Depth 1 scan runs automatically on every spec
revision and has no way to know what it inspects, so it cannot tell whether one
has happened or what a Depth 2 would add; it will produce plausible answers
about scans it has no definition of. :16 and :18 are the milder case — the
hierarchy is legible without the filenames, which name templates rather than a
project's actual PRD and TRD, so in an adopting project they point at documents
that do not exist under those names.
Fix: Delete the paths at :16 and :18; "**PRD** — product intent. Canonical for
*what* and *why*" states the rank without them. :64 goes with SOT1's rewrite.
For :71, either state what the three depths cover, in one clause each, or state
the rule without them — "The Spec Reviewer Agent is the designated mechanism for
proactively catching drift between canonical and derived artifacts before it
reaches a hard stop. Continuity scans run on every spec revision and at wider
scope on demand." — which is the rule this file actually needs and which SOT6
would reduce it to anyway.
Related: SOT1, SOT6

## SOT4 — non-blocking
Claim: Session kind is never stated.
Location: policies/source-of-truth-policy.md:1-9
Evidence: Verified by reading. The frontmatter carries `status`,
`last-reviewed`, and `audience`, and no body line names a session kind; the H1 is
followed directly by §Purpose. Compare
policies/verification-boundary-policy.md:9-10, the sibling policy in scope,
which reads "This policy governs both session kinds: decision sessions and
execution sessions" — a line the cycle-12 merge added there and not here.
Verified by running grep across the nine: seven of the nine now open with the
declaration; this file and LEXICON.md are the two that do not, and LEXICON.md's
case is reported separately at reviews/LEXICON-cycle-12.md L12 as an observation
because a lexicon is reference rather than rules. This file is rules.
Consequence: Criterion 7. Unlike boundaries/human-review-boundary.md at cycle 1,
where the content was genuinely split and the audience value was in question, the
answer here is unambiguous and simply unstated: the hard-stop procedure and the
adapter discipline bind any agent that hits a conflict or writes an adapter, and
the flagging obligation at :59-64 binds whoever is making a change — both kinds.
The gap is a missing sentence rather than mixed content, which is the cheapest
class of criterion-7 failure. Non-blocking rather than an observation because
this is a first gate and the file is the only rules document in scope without
the line, so the omission is a real inconsistency rather than a stylistic one.
Fix: Add one line after the H1: "This policy governs both session kinds:
decision sessions and execution sessions." — matching
policies/verification-boundary-policy.md:9-10 word for word, since the two
policies are siblings and there is no reason for them to phrase it differently.

## SOT5 — non-blocking
Claim: The adapter rule is stated here and twice in operating-model.md.
Location: policies/source-of-truth-policy.md:26-29
Evidence: Verified by reading all three @ 2b9c856. This file :26-29: "The
portable operating-model documents (context sets, policies, roles, skills,
boundaries) are canonical for *how the project is run*. Vendor-specific AI
tooling … is an adapter, never the sole home of a durable rule."
operating-model.md:86, under Agents → Must not: "store durable policy only in
vendor-specific tooling". operating-model.md:229-231, §Relationship to tools:
"These portable operating documents are the source of truth for project
operating guidance. Tool-specific files may adapt these rules but should not be
the sole location of durable policy." Verified by running grep: no fourth site
in the nine.
Consequence: Three statements of one rule across two files that land in the same
bundle. They agree, so nothing stops. The cost is that the reader cannot tell
which is the operative form, and a future change has to find all three. This
file's copy is the one that earns its place — it is the sentence the five-step
§Adapter discipline hangs off, and its enumeration of what counts as
vendor-specific AI tooling is what makes the prohibition applicable to a
specific artifact. The redundancy is in operating-model.md, where the rule
appears as a prohibition at :86 and again as a closing note at :229-231.
Fix: No edit owed here. The fix is operating-model.md's, reported at
reviews/operating-model-cycle-5.md O9: delete §Relationship to tools, keep the
prohibition at :86, and let this file carry the enumeration and the discipline.
Related: SOT2

## SOT6 — observation
Claim: §Proactive drift detection describes a role's behavior rather than
instructing the reader.
Location: policies/source-of-truth-policy.md:66-71
Evidence: Verified by reading. The section in full: "The Spec Reviewer Agent is
the designated mechanism for proactively catching drift between canonical and
derived artifacts before it reaches a hard stop. Continuity scans run
automatically on every spec revision (Depth 1) and on demand at greater scope
(Depth 2, Depth 3). See `roles/spec-reviewer-agent.md`." No sentence directs the
reading agent's work; the section states what another role does. Rubric criterion
5 asks that every rule be an instruction to the agent reading it. This is the
same class of defect reviews/human-review-boundary-cycle-1.md B5 recorded
against that file's description of Dave's reading habits, and
reviews/verification-boundary-policy-cycle-1.md V8 records against that policy's
four role obligations.
Consequence: None demonstrable, which is why this is an observation. The section
is informational and does no harm on its own — the reader is told a safety net
exists, which is a reasonable thing for a policy about conflicts to say. What
makes it worth recording is that it is also where SOT3's worst path reference
and its three undefined terms sit, so the section needs an edit regardless, and
the criterion-5 question determines how much of it survives that edit.
Fix: If the section is kept, one clause turns it: the reader's obligation is to
surface suspected drift rather than to wait for a scan. If it is reduced to the
first sentence, as SOT3's fix would allow, criterion 5 is satisfied by brevity —
the sentence then names where the guarantee comes from, which supports the
hard-stop rule the file exists for.
Related: SOT3

## SOT7 — observation
Claim: §Purpose and §Conflicts are a hard stop state the same rule at the top and
middle of the file.
Location: policies/source-of-truth-policy.md:11-13
Evidence: Verified by reading. §Purpose: "This policy fixes what is canonical and
what is derived, so that disagreements between artifacts are resolved by
authority rather than by guessing." §Conflicts are a hard stop, :57: "Do not
silently reconcile. Do not pick the version that is easier to implement." The
second is the first stated as an instruction; "resolved by authority rather than
by guessing" and "do not pick the version that is easier to implement" are the
same prohibition.
Consequence: None demonstrable. §Purpose is two lines, it states the rule's
effect rather than arguing for it, and criterion 6 is not engaged — this is not
rationale, it is a compressed statement of what follows. Recorded only so the
pair is on the record: if a future edit strengthens one, the other is the place
to check. The file's criterion-6 result is a pass on the strength of this
distinction.
Fix: None owed.
