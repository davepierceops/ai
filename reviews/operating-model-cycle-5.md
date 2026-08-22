# Review: operating-model.md — cycle 5

Verdict: ready-with-findings
Reviewed: operating-model.md @ 2b9c856
Baseline: cb3e75a (cycle 4 reviewed state, ready)
Reviewer: Spec Reviewer Agent (Pass 1, cycle 14; frontier)
Date: 2026-08-21
Scope: the full file. Three passes. (a) The cycle-12 edits checked against the
decisions that ordered them, verified by running `git diff cb3e75a 2b9c856 --
operating-model.md`: the standard response shape arrived from the retired
context-sets/base.md as a seven-element section that closes with the sentence
distinguishing it from the change package; the Chief of Staff role arrived from
the retired context-sets/ai-native-engineering.md under Responsibilities; and
the two mandatory separations — whoever produces an artifact does not approve
it, and the Architect that drafts a spec does not act as the Spec Reviewer —
landed under Agents. All three are stated once here and nowhere else in the
nine, verified by running grep. Cycle 4's seven findings remain resolved. (b)
All ten rubric criteria (docs/global-context/review-rubric.md @ 2b9c856)
re-applied to the current text. Criterion 3 verified by running grep for
backticked repo-relative paths — zero; the one parenthetical pointer, `(see
"Source of truth")` at :136, names a section of this same file. Criterion 8
verified by running grep — zero model names. (c) All nine in-scope files
cross-checked against each other for a term or rule stated twice. This is the
pass cycle 4 deferred: its Not-inspected line named "duplication against
policies/* and context-sets/*" as unassessed and deferred it to those files'
cycles, and both policies are now in scope for the first time. Two duplications
surfaced, both against policies/source-of-truth-policy.md, and both are below.
Everything cycle 4 certified as stated-only-here still is: the
meaningful-change definition, the nine-stage change flow, the two-tier release
gate, the twelve-item change package, the eleven-condition definition of done,
and the escalation triggers appear in none of the other eight.
Cross-checked: docs/global-context/decision-layer.md, LEXICON.md,
context-sets/spec-and-change-discipline.md,
context-sets/testing-and-verification.md,
context-sets/production-grade-software.md,
boundaries/human-review-boundary.md, policies/verification-boundary-policy.md,
policies/source-of-truth-policy.md @ 2b9c856; the cycle-12 revision directive
(the three merge-in decisions); `bin/bundle-methodology` (the hardcoded spine).
Not inspected: the rubric was applied, not reviewed. Duplication against
policies and context sets *outside* the nine — notably whether
policies/commit-and-change-control-policy.md states the release-gate tiers a
third time, which cycle 3 and cycle 4 both deferred and which instruction 3
scopes out of this cycle; it remains unassessed and is the obvious next place to
look. Whether the escalation triggers or the change-flow role assignments agree
with the role documents in roles/ was not checked. The vendor hedges at :36
("currently GitHub Issues") and :153 ("e.g. OpenFeature") were re-read and are
unchanged from the text cycle 4 passed; O8 concerns the *second* copy of the
first one, not this file's handling of it. No bundler was run;
`bin/bundle-methodology` was read and places this file second in a hardcoded
spine, after context-sets/spec-and-change-discipline.md — relevant to O8 and to
reviews/spec-and-change-discipline-cycle-7.md S14, and noted rather than
observed in a generated bundle. The directive's excluded items, including the
README unmatched-glob warning, were not assessed.
Findings: 2 — 0 blocking, 2 non-blocking
Prior cycle: reviews/operating-model-cycle-4.md
Dave should inspect: O8 — the canonical source-of-truth order is now stated in
full in two files that land in the same bundle, and which one is its home is a
placement call rather than a drafting fix. The recommendation below is that the
enumeration goes to the policy and this file keeps the hard-stop rule, but the
spine puts this file in the decision-layer bundle and the policy is not in that
spine, which cuts the other way.

## O8 — non-blocking
Claim: §Source of truth and policies/source-of-truth-policy.md §Canonical order
state the same five-step order and the same hard-stop rule, and they disagree on
how the tracker is named.
Location: operating-model.md:32-41
Evidence: Verified by reading both @ 2b9c856. This file: "The order is: **PRD**
(product) → **TRD** (technical) → acceptance criteria → per-change architecture
summary → **tracker issues** (currently GitHub Issues). Tracker issues are
derived PM artifacts — a view onto the specs, never an independent source of
truth. If a derived artifact conflicts with a canonical one (an issue against
the spec, an architecture summary against the TRD), it is a **hard stop**."
policies/source-of-truth-policy.md:14-24 enumerates the identical five steps,
numbered, with the same derived-artifact claim in the same words for step 5 ("An
Issue is a *view onto the specs*, not an independent source of truth"), and
:42-57 states the hard stop and adds the three-step agent procedure this file
does not carry. The substantive difference is the vendor: this file names it
once and hedges it — "currently GitHub Issues" — where the policy names it twice,
unhedged, as the label of the canonical rank itself ("5. **GitHub Issues**") and
as the artifact an architecture summary is cut into (":21"). Verified by running
grep: both files carry `audience: [all-roles, human]`, so both are selected into
the same bundles.
Consequence: An agent holding the bundle gets the canonical order twice. The
copies do not contradict on the order, so Core rule 9 is not triggered and no
work stops — which is why this is non-blocking. What it does cost is the hedge:
this file's "currently" is the anti-lock-in signal, and an agent reading the
policy's copy alone concludes that a specific tracker product occupies rank 5 of
the source-of-truth hierarchy. Under Core rule 13 a future change to the order,
or to the tracker, has to find both copies or one goes stale — and the copy most
likely to be missed is the one in the file whose title does not say
"source of truth".
Fix: One home. The recommendation is that the enumerated order lives in
policies/source-of-truth-policy.md, which is named for it and already carries
the hard-stop procedure this file only names, and that §Source of truth here
compresses to the hard-stop rule plus the one-line statement that specifications
are canonical — which is what the rest of this file actually depends on. If the
call goes the other way, because `bin/bundle-methodology`'s spine carries this
file and not the policy, then the policy's §Canonical order is what goes, and
the hedge "currently" must survive into whichever copy remains.
Related: O9

## O9 — non-blocking
Claim: The adapter rule — durable policy never lives only in vendor-specific
tooling — is stated three times, twice inside this file.
Location: operating-model.md:86 and :227-231
Evidence: Verified by reading all three @ 2b9c856. This file :86, under Agents
→ Must not: "store durable policy only in vendor-specific tooling". This file
:229-231, under §Relationship to tools: "These portable operating documents are
the source of truth for project operating guidance. Tool-specific files may
adapt these rules but should not be the sole location of durable policy."
policies/source-of-truth-policy.md:26-29: "The portable operating-model
documents (context sets, policies, roles, skills, boundaries) are canonical for
*how the project is run*. Vendor-specific AI tooling — agent frameworks, skills,
hooks, memory files, IDE integrations, and the instruction files they read — is
an adapter, never the sole home of a durable rule", followed by a five-step
§Adapter discipline the cycle-12 decision moved there from the retired
boundaries/vendor-tooling-boundary.md. Verified by running grep: no fourth site
in the nine.
Consequence: Three statements of one rule, and the two in this file are eleven
lines apart in reading order at the top and bottom of the same document, so a
reader meets it as a prohibition under Agents and again as a closing note
without either acknowledging the other. The prohibition at :86 is the operative
form — it is in the Must-not list an agent checks itself against — and
§Relationship to tools adds nothing to it. The policy's copy is the one that
earns its place, because it is the sentence the five-step §Adapter discipline
hangs off.
Fix: Delete §Relationship to tools (:227-231). The prohibition at :86 states the
rule as an agent instruction, and the enumeration of what counts as
vendor-specific AI tooling — the part :229-231 gestures at without stating —
lives in policies/source-of-truth-policy.md:26-29 with the discipline it
governs.
Related: O8
