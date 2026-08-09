# Directive — TP-2: build `bin/bundle-methodology` — davepierceops/ai

Date: 2026-08-09
Route: fresh
Model: Sonnet 5
Track: A

Tranche: Tooling (`docs/packages/tooling-decomposition.md`), package **TP-2**.

## Intent

One command regenerates the methodology-context-bundle correct-by-construction,
retiring the hand-assembly that has twice produced a broken bundle — a stale
commit cut pre-merge, and a shell `!` history-expansion corrupting every
separator (both recorded in `docs/global-retro-inbox.md`).

## Spec basis — derive ACs from these; do not invent behavior beyond them

- `decisions/log.md` @ `dec4b6b5fb2f26880a25cac1e144bdd581338720`, **DEC-000140** —
  the canonical rule: filename format, file-set rule, header pins, per-file blob
  short-SHA, `<!-- FILE n/N -->` separators, and a runnable interim procedure that
  is the reference behavior.
- The current uploaded bundle is the **golden output format**: a title +
  "derived artifact — do not edit / regenerate" line;
  `Source: davepierceops/ai @ <full HEAD SHA>`; `Generated: <YYYY-MM-DD-HHMM>`;
  the file-set rule statement; a numbered file list, each entry `(blob <short-sha>)`;
  and `<!-- FILE n/N: <path> @ <short-sha> -->` separators between file bodies.

## Package — spec-first, test-first

1. **Spec doc.** Write `docs/packages/bundle-methodology-spec.md` (intent, CLI,
   ACs below), mirroring `docs/packages/package-a-spec.md`. No lifecycle
   frontmatter (`docs/**` is out of metadata scope).

2. **Acceptance criteria** (the spec doc owns the canonical wording):
   - **AC-BM-1** Writes `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md` (timestamp
     at generation time) to the configured output dir.
   - **AC-BM-2** Header carries the title, the do-not-edit/regenerate line,
     `Source: davepierceops/ai @ <full HEAD SHA>`, `Generated: <stamp>`, and the
     file-set rule statement.
   - **AC-BM-3** File set = the fixed six-file spine (`context-sets/base.md`,
     `context-sets/spec-and-change-discipline.md`, `context-sets/collab-workflow.md`,
     `operating-model.md`, `roles/chief-of-staff.md`,
     `policies/commit-and-change-control-policy.md`) **plus** every `skills/*.md`
     whose `audience` frontmatter contains `all-roles` or `chief-of-staff`.
     Computed from the rule, never hardcoded — a new skill or an audience change is
     picked up automatically.
   - **AC-BM-4** Numbered file list; each entry `(blob <short-sha>)` where the SHA is
     that file's own blob (`git rev-parse --short HEAD:<path>`), not the repo HEAD.
   - **AC-BM-5** Each file body is preceded by a
     `<!-- FILE n/N: <path> @ <short-sha> -->` separator (n of N, 1-indexed).
   - **AC-BM-6** Every SHA is read from git — correct-by-construction, never
     hand-entered; runs on a synced `main`.
   - **AC-BM-7** Deterministic given HEAD: identical output modulo the timestamp line.
   - **AC-BM-8** Writes only the bundle file; no other repo mutation.

3. **Red-gate (mandatory).** Tests derived from the ACs, run and **confirmed to
   fail** before implementation. Strong form: a golden-comparison against a fixture
   tree (or a captured expected bundle), asserting header, file-set membership,
   per-file blob SHAs, and separators — modulo the timestamp line. The bundle is
   uploaded to projects, not committed, so do not assume a committed golden file;
   build the fixture. Confirm a behavioral red (not a missing-module red), then
   implement to green. Mechanical checks pass as part of green.

## Design fork — executor's architecture call; decide and document

`bin/bundle` already exists: a `depends-on` closure walker with
`--format list|json|concat`; `concat` emits body-only with `===== path @ sha =====`
separators and **no header**. `bin/bundle-methodology` needs the full header plus
the audience-rule file-set. Choose: **(a)** a new `bin/bundle-methodology`, or
**(b)** a mode that reuses `bin/bundle`'s concat body and wraps the header —
noting the separator forms differ (`=====` vs `<!-- FILE n/N -->`) and must be
reconciled or kept separate. Name-collision caution: `bin/bundle` emits the
reviewed-revision *cycle* bundle; this is the *context* bundle. Record the choice
and its rationale in the spec.

## Scope / do-not

- Touch only: the new script (or `bin/bundle`, if the mode approach is chosen),
  its tests, and `docs/packages/bundle-methodology-spec.md`.
- **Do not change the bundle format** — match the golden output. If the format
  looks wrong, STOP and surface; do not "improve" it.
- Do not touch other `bin/` tools or any methodology document.

## Executor obligations

- Confirm the working tree is on a synced `main` before starting.
- If the golden format and DEC-000140 disagree anywhere, STOP and surface.
- Land via branch + PR (main is protected). Report branch/PR.
- Report what was done, not what this directive said.

## Done

`bin/bundle-methodology` (or the chosen mode) generates a bundle byte-matching the
golden format modulo timestamp; spec doc + ACs written; tests confirmed
red-then-green; mechanical checks pass; branch + PR opened for Dave's review.
