# Directive — Administrative Streamlining (Findings F1–F7)

Date: 2026-08-01
Source: chat triage over `streamlining-findings.md` (Fable session).
All seven findings accepted by Dave. This directive records the
decisions and sequences execution. Changes to agreed documents enter
through the normal spec-review cycle — this directive authorizes
drafting and cycle-opening, not direct edits to `agreed` docs.

Reviewed state: `davepierceops/ai` @ HEAD of main at session time.
Executor must record actual SHAs at execution start (F4's `cycle-open`
does this once built; manually until then).

## Decisions

### F1 — accept
Scripted frontmatter flips + pre-commit auto-flip hook.
Deliverables: `bin/flip-agreed` (self-verifying frontmatter-only
commit); pre-commit hook flipping `agreed → in-review` +
`last-reviewed: null` on content edits to in-scope files. Closes
OPEN-ITEMS "Build this repo's frontmatter-enforcement hook."

### F2 — accept
Batch migration of 30 legacy-header docs to YAML frontmatter,
status-preserving mechanical transform; one repo-wide disposition list
per the grandfather clause; one batch gate review. Closes OPEN-ITEMS
"Migrate existing docs to YAML frontmatter."

### F3 — accept
Verdict-first review artifact schema: fixed ~10-line record for
clean/confirmation passes; structured finding entries otherwise; prose
permitted, not default. Edit target: `skills/spec-review-cycle.md`
(add artifact schema section).

### F4 — accept (with architecture decision)
`bin/cycle-open` (directive skeleton with SHAs read from git; reviewed-
revision bundle emission) and `bin/bundle` (reference-closure
computation from entry-point context-sets). Resolves the open
manual-vs-scripted closure decision: scripted.
Architecture (decided in triage): scripts live canonically in
`/ai/bin/` only — never copied to project repos. Projects install a
thin shim (hook config invoking the script from the local `/ai` clone,
located via `AI_METHODOLOGY_HOME` env var or sibling-directory
convention — executor proposes one in the change package). Scripts
inherit the portability constraint: no hardcoded project paths; repo
root discovered from invoking repo; in-scope globs read from the
metadata policy, not baked in. Closes OPEN-ITEMS "Per-project
frontmatter enforcement" (setup = install shim).

### F5 — accept
`human-gate` issue becomes the single canonical pending-gate record;
chat statement reduces to a one-line pointer; issue body templated
from the change package (`bin/gate-open`, optional). Edit target:
`policies/commit-and-change-control-policy.md` (Pending gate
visibility section).

### F6 — accept
Expedited review path for zero-finding single-file diffs: hook flips
`in-review`; Dave reads the diff; scripted flip to `agreed` pointing
`last-reviewed` at a one-line entry in `reviews/expedited-log.md`.
Structural eligibility: one file, agreed as-is with zero findings; any
finding, dictated wording, or second file escalates to a full cycle.
Edit target: `policies/document-metadata-policy.md` (revises the
"No exceptions for trivial edits" clause — this document is `agreed`,
so this change REQUIRES a full spec-review cycle; the expedited path
cannot be used to introduce itself).

### F7 — accept
MANIFEST.md sheds derivable registers: file registry replaced by
metadata-policy in-scope globs; changelog obligation ends (historical
sections frozen with tombstone note); retains bundle definitions and
assembly notes pending `bin/bundle` supersession. MANIFEST is
tracker-class (out of frontmatter scope) but the change should ride a
reviewed change package given its registry role.

## Execution sequence

1. **Package A (scripts):** F1 + F4. New files under `bin/` + hook.
   No agreed-document edits; normal review for new skills-class
   tooling. F2's transform script rides here.
2. **Package B (batch migration):** F2, using Package A's hook and
   transform. Includes the disposition list and its declared location.
   One batch gate review.
3. **Package C (ceremony policy edits):** F3 + F5 + F7, batched into
   one review cycle — shared rationale (ceremony reduction, no routing
   change). Targets: spec-review-cycle skill, commit-and-change-control
   policy, MANIFEST.
4. **Package D (routing change):** F6 alone, full spec-review cycle
   against the agreed metadata policy.

## Deferred / out of scope

- `bin/gate-open` (F5) — optional, build when a consequential change
  next reaches a gate.
- `bin/bundle` superseding MANIFEST bundle definitions — after F4
  lands and closure output is trusted.
- wne-crm shim installation — after Package A lands.

## Execution notes

- MCP GitHub was unavailable this session; this directive is delivered
  as a file for local commit. Suggested path:
  `docs/cycles/streamlining-directive.md`. Claude Code commits it,
  then executes Package A.
- Findings source (`streamlining-findings.md`) may be committed
  alongside for the record or kept out of the repo — Dave's call at
  commit time.
