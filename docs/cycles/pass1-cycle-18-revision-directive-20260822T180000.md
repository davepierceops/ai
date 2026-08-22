# Directive — Pass 1, Cycle 18: document-metadata-policy compression

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Coder, executing reviewer dispositions

Base: origin/main @ a3d7c96c4020f554a41ba633641687980a05f790.
Document in scope: policies/document-metadata-policy.md (372 lines).
Review artifact: reviews/document-metadata-policy-cycle-13.md, on main. Read it in full before editing.
Foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, docs/global-context/review-rubric.md.

## Dispositions

D1 — do not apply. The scope glob is extended in Pass 2, after all-decision-roles is reserved. Do not touch lines 23-34 beyond what D2 requires.

D2 — apply. Cut each of the thirteen justification passages to the rule it justifies, keeping the operative sentence. The four passages the artifact marks load-bearing each survive as exactly one sentence: "when it is unclear, it is ineligible"; "the list is normative where it names a document, and cannot bound the class"; "any finding escalates, however small"; "the SHA cited in last-reviewed must appear in an entry in the log". No rule is removed; no condition is removed; no status value, field, or route to agreed changes meaning. Target: under 290 lines.

D3 — apply. "route" becomes "path" at the five cited lines; LEXICON is not edited.

D4 — apply as the Fix states: state the rule at 228 and 320; delete the parenthetical paths at 207-208, 218, 311, 317-318, 351.

D5 — apply. The adapter exclusion is stated by class, no vendor named.

D6 — apply. Session-kind line under the title; mark the named conditions as Dave's.

D7 — do not apply. Line 198 goes with the glob at line 33 in Pass 2.

D8 — apply. Delete the superseded-by: null line.

## Status

Set status: draft, last-reviewed: null on three files: policies/document-metadata-policy.md, policies/decision-log-policy.md, skills/spec-review-cycle.md. All governed documents sit at draft through Pass 1 and re-enter agreement together. If the pre-commit hook objects to a direct draft flip, report the objection and stop; do not work around the hook.

## Verification

1. Line count before and after.
2. Every status value, every frontmatter field, every condition on each path to agreed, and every sequence step present in the original is present in the result. List them as a checklist in the PR body with a line number each.
3. bin/check-frontmatter --all passes. bin/flip-agreed is not run.
4. grep for: the four retired terms; Claude, GitHub, MCP; "route"; path-shaped references outside the exempt lists (scope globs, gate-document class list, reviews/expedited-log.md, decisions/log.md).

## Output

Commit on p1-cycle-18-revision, push, open a pull request against main titled "Pass 1 cycle 18 revision: document-metadata-policy compression". Do not merge. PR body carries the verification-2 checklist and, per finding, applied as written or varied with one line.

## Report shape

Line count before → after. Findings applied / varied, one line each. Verification-4 survivors with reasons. Status-flip outcome. Branch, SHA, PR number.
