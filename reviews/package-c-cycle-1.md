# Gate Review — Package C, cycle 1

*Authored by the Spec Reviewer agent in the gate session, 2026-08-01.
**Condensed for the record by the orchestrator**, who committed it: the
reviewer's five-field finding entries were collapsed into prose paragraphs and
their `Evidence` lines were not carried over. That is a real loss — the
evidence lines are what made the claims checkable — and it is disclosed here
rather than hidden behind the word "transcribed", which is what an earlier
version of this note said.*

*It was **not** retrofitted forward into the schema this package introduces,
per that schema's own no-retrofit rule: an artifact is a record of what
happened, and rewriting it to match a later format is the drift this repo
exists to prevent. Cycle 2 is the first artifact written in the schema.*

*One figure below is wrong as authored and is left standing: B6 says "48
listed" for `TREE.txt`; the actual count was 49. Correcting a reviewer's
arithmetic inside their artifact would make it the executor's document. The
correction is recorded in `docs/packages/package-c-change-package.md`.*

Verdict: changes-required
Reviewed: working tree at `d778813` + 4 uncommitted modifications
(`MANIFEST.md`, `README.md`, `policies/commit-and-change-control-policy.md`,
`skills/spec-review-cycle.md`)
Reviewer: Spec Reviewer Agent (gate review; not the drafting instance)
Date: 2026-08-01
Findings: 8 blocking, 9 non-blocking, 3 observations
Prior cycle: none

Scope: the four-file diff, against `docs/cycles/streamlining-directive.md`
§Decisions F3/F5/F7 and §Execution sequence item 3;
`policies/document-metadata-policy.md` (`agreed`);
`policies/source-of-truth-policy.md`; `roles/spec-reviewer-agent.md`;
`policies/agent-review-policy.md`; plus a repo-wide sweep for references to
MANIFEST's file registry, the tree version, the changelog, the legacy `Status:`
convention, and the `human-gate` chat obligation. Not inspected: the `bin/`
implementations beyond CLI surface and MANIFEST-related test fixtures;
F1/F2/F4/F6 correctness (Packages A, B, D); whether `bin/bundle`'s closure
output is in fact correct.

## Blocking

**B1 — no change package exists for Package C, which F7 explicitly required.**
F7's own words: "the change should ride a reviewed change package given its
registry role." Packages A and B both produced one. The gate is being asked to
sign off on a change whose required evidence artifact was not produced.

**B2 — `AGENTS.md` still instructs agents to follow the superseded two-step
pending-gate procedure that F5 replaced.** `AGENTS.md:24-26` says "open a
`human-gate` GitHub issue and state it explicitly in the current response"; the
revised policy now says the opposite. `policies/source-of-truth-policy.md` names
an adapter contradicting a policy as a **hard stop**. This change therefore
ships a hard-stop condition into the repo. It is the exact defect class the
executor correctly caught in README, one file over. `CLAUDE.md` is fine — it
never carried the two-step text.

**B3 — F5 deletes the explicit request for a go/no-go without relocating it.**
The old step 1 required four things (name, class, evidence summary, **ask**);
the new one line requires three. The section still ends "Absence of a response
is not a go" — the ask is what converts silence into a detectable stall.

**B4 — F5 makes the GitHub issue the sole canonical record with no degraded
mode when GitHub is unreachable.** The directive records that MCP GitHub was
unavailable in the very session that authorised this change. The failure mode is
the observed default of the last session, not a hypothetical. Under the new
text an agent that cannot open the issue has no compliant path.

**B5 — MANIFEST's opening sentence describes contents the file does not have.**
It claims to hold "the context-set bundle definitions and the assembly notes";
there is no assembly-notes section. Two defects: the file's self-description is
false, in a change whose entire argument is that a second copy of a fact drifts
and then lies; and F7 decided the file retains assembly notes, which were
dropped.

**B6 — `TREE.txt` is the same hand-maintained derivable register F7 just
removed, is stale, and was explicitly deferred to this checkpoint.**
`git ls-files | wc -l` = 91 against 48 listed; omits all of `bin/`, `docs/`,
`reviews/`. `docs/cycles/cycle-2-directive.md` deferred it "to the next
checkpoint" — the MANIFEST rewrite *is* that checkpoint, and it fired without
honouring the deferral.

**B7 — the schema's verdict word `agreed` collides with the repo's standing
status vocabulary and asserts a decision the Spec Reviewer role is forbidden to
make.** `policies/document-metadata-policy.md` fixes `agreed` as "**Dave** has
agreed this document. This is the repo's standing verb."
`roles/spec-reviewer-agent.md` states the reviewer does not "make agreement
decisions (Dave decides)."

**B8 — the new schema and the two documents that already specify review outputs
are unreconciled.** `roles/spec-reviewer-agent.md` requires Scope, Findings,
Required changes, Advisory items, Sign-off; `policies/agent-review-policy.md`
requires seven outputs plus "What Dave should inspect". The schema's clean-pass
record has slots for none of the latter. I hit this myself and had to append a
section the schema does not define.

## Non-blocking

**N1** — `COLLAB-STATE.md` still asserts the superseded versioning convention as
a locked decision, at `:5` and `:14`. The README defect's twin.
**N2** — MANIFEST overstates what `check-frontmatter --all` tells a reader: it
reports a count, not a set.
**N3** — the `bin/bundle` supersession condition is not actionable and is
tracked nowhere. "Trusted in practice" cannot be observed to have happened.
**N4** — the findings-pass template reuses a header hardcoding `Findings: none`.
Followed literally, every review with findings declares it has none.
**N5** — `<full sha>` conflicts with the 7-char form used everywhere else,
including the agreed policy's own frontmatter.
**N6** — the schema does not say whether it applies retroactively, leaving the
only `agreed` document's review record non-conforming.
**N7** — F5 does not say which artifact wins when the issue body and the change
package disagree.
**N8** — three `OPEN-ITEMS.md` entries this initiative closed are still listed
as open and blocked.
**N9** — the two `.claude/` adapter READMEs are the last live users of the
convention README now declares dead.

## Observations

**O1 — the README scope addition was right, and the justification is stronger
than the executor stated.** The agreed metadata policy's supersession clause
requires that removal of the `Tree version` line land in the same change package
as the agreement — "the repo never holds both conventions as canonical." Commit
`0230e11` removed MANIFEST's line and left README's. The repo has been in
violation since; cycles 2 and 3 reviewed that package and did not catch it. The
executor under-argued the call rather than over-reached.

**O2** — MANIFEST's "four files were registered retroactively in v0.5" is
accurate; verified against `a3ffe08`.

**O3** — the tombstone's register is well-judged. One forward-looking statement
("this file with it") states a future deletion as settled when its trigger is
not actionable.

## What Dave should inspect

1. **B4** — the GitHub-unavailable fallback.
2. **B6** — `TREE.txt`; cycle 2 explicitly deferred it to this moment.
3. **B7** — the verdict words; decides whether reviewers can assert `agreed`.
4. **O1** — the README scope question. My answer is that it was correct and
   mandatory, not discretionary.

## Schema feedback (first use)

The verdict enum was the sharpest problem and surfaced "in the first five
seconds of writing." The clean-pass header does not survive contact with a
findings pass. `Scope:` as a single line is too small for a cross-document
review. The five-field finding entry is good and I would not change it —
`Claim` killed two findings that turned out to be restatements, and
`Consequence` correctly demoted two others to observations. Left out: "What
Dave should inspect" (undefined by the schema), a severity ordering within
`blocking`, and cross-finding relationships.
