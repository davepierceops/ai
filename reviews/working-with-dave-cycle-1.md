# Review: engagements/working-with-dave.md — cycle 1

Verdict: changes-required
Disposition (criterion 10): retain-with-changes — the engagement residue is
genuinely unique and earns a place: who Dave is and the Comfy engagement
context, the infra verification ladder (plan- / apply- / serving- /
delta-verified), and the client guardrails (zero write access to client
systems). Everything else in the file is core or decision-layer restated and is
stripped; frontmatter is added so the file can land in a bundle at all.
Reviewed: `engagements/working-with-dave.md` @ `26f8f10`
Reviewer: Spec Reviewer Agent (frontier)
Date: 2026-08-21
Scope: full text against all ten rubric criteria (`docs/global-context/review-rubric.md`
@ 26f8f10), criterion 10 answered first per the cycle-5 directive; criterion 4
judged against the current text of core.md and decision-layer.md @ 26f8f10.
Criterion 3 count: zero path-shaped references — the only cycle-5 document with
none. Criterion 9: no filenames prescribed — pass.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`.
Not inspected: whether the engagement facts are current (the file is undated and
carries no review pointer — see W6); any other file under `engagements/`.
Findings: 3 blocking, 2 non-blocking, 1 observation
Dave should inspect: the audience value for engagement-scoped files (W1) — the
known set has no engagement-shaped selector, and inventing one is a frontmatter
decision, not an edit.

## W1 — blocking
Claim: No frontmatter — no `status`, `last-reviewed`, or `audience` (criterion 2).
Location: line 1
Evidence: verified by reading @ 26f8f10; the file opens directly with the title.
Consequence: the compiler has no selector, so the file lands in no bundle —
which also means it currently fails criterion 10 mechanically, whatever its
content merits. It is the only cycle-5 document outside the metadata scheme
entirely.
Fix: add the standard frontmatter block; audience needs an engagement-scoped
decision-session value plus `human` — the value itself is Dave's call.

## W2 — blocking
Claim: The bulk of the file restates core and decision-layer rules (criterion 4),
with rule numbers.
Location: "Your job", "Mechanics", "Evidence", "Client guardrails"
Evidence: side-by-side reading @ 26f8f10 — "One question at a time. Never stack
questions… ask the most load-bearing one, wait, then the next" → DL-1; "Terse.
Pithy bullets over paragraphs. No preamble" → DL-2; "Pasted output is your
input… Triage — lead with what matters, one line per item; hold or discard the
rest" → DL-2; "If you see a landmine in the path, say so in one line while
handing him what he asked for" → DL-3 (near-verbatim); "Pre-stage… draft it and
present it ready" → DL-5; the Paste blocks bullet (deliverables complete, not a
fragment) → DL-7/DL-8; the Directives bullet (standalone block, everything the
session needs, report triageable) → DL-13; the Command blocks bullet (one
purpose per block, no placeholders with the question asked above, expected
output in one line under, blast radius before anything destructive) → DL-15;
"Every claim carries its class… observed / inferred / told / unknown" and "A
claim without a stated class is not a claim" → Core 6; "'Could not determine'
beats a guess" → Core 7 (verbatim); "Never phrase one class as a stronger one"
→ Core 7; "Client secret values never enter your context… never its value" →
Core 1 (client-scoped instance).
Consequence: this file predates the foundation and is now an uncontrolled
second statement of thirteen of its rules; any core or decision-layer revision
leaves this copy asserting the old text with equal authority.
Fix: strip every restated rule; keep the engagement residue named in the
disposition. The secrets guardrail keeps its client-scoped sentence only if it
adds scope beyond Core 1 (it does not — cut it; the zero-write-access guardrail
is the unique one and stays).

## W3 — blocking
Claim: The preamble is a file-loading instruction that contradicts the bundle
model and itself (criterion 1).
Location: lines 3–4 — "Load this file in every session, alongside one role
file. It is the complete contract — nothing else needs to be read from
anywhere."
Evidence: verified by reading.
Consequence: a bundle reader cannot load files, and the sentence claims
completeness while requiring a second file in the same breath; under the
compiler, selection is the frontmatter's job (W1), not the prose's.
Fix: delete the preamble; W1's frontmatter replaces it.

## W4 — non-blocking
Claim: Session kind is not explicit (criterion 7): the register and mechanics
rules are decision-session material, but the file addresses "every session".
Location: preamble, "Mechanics"
Evidence: inferred by reading against the decision-layer preamble's session
definitions.
Consequence: as written it would push chat-register rules into execution
bundles.
Fix: after W2's strip, what remains (engagement context, verification ladder,
guardrails) is plausibly both-kinds material; state that scope in one line.

## W5 — non-blocking
Claim: One vendor name (criterion 8): "terraform plan" (line 49), hedged with
"or equivalent". No model names.
Location: "Evidence", plan-verified entry
Evidence: verified by reading.
Consequence: minor; the ladder is otherwise tool-neutral.
Fix: "a dry run (e.g. terraform plan)" already isolates it; acceptable as is,
or drop the example.

## W6 — observation
Claim: The engagement facts are stated in an undated present tense — "He is
onsite at a client (Comfy)… under time pressure" — with no review pointer to
say when they were last true.
Location: "Who you are working with"
Evidence: verified by reading; no date appears anywhere in the file.
Consequence: the file cannot go stale visibly; W1's `last-reviewed` field is
the existing mechanism for this.
Fix: covered by W1.
