# Directive — TP-1: `bin/cycle-open` emits `Track:` — davepierceops/ai

Route: fresh
Model: Sonnet 5
Track: A

Tranche: Tooling (`docs/packages/tooling-decomposition.md`), package **TP-1**.

## Pinned refs — verify the working tree before editing

Reviewed at commit `206fc6e`. STOP conditions pin here, not to branch HEAD
(this directive's own commit moves that head).

- `bin/cycle-open` @ blob `237f789`
- `docs/packages/package-a-spec.md` @ blob `aaf6529` (AC-CO-3)
- `skills/spec-review-cycle.md` @ blob `435ebc4` — **agreed**; canonical
  cycle-directive format

## Intent

The agreed cycle-directive format in `skills/spec-review-cycle.md` carries a
`Track: <A | B>` field, placed immediately after `Date:` and before
`Documents in scope:`. `bin/cycle-open`'s skeleton generator does not emit it,
so every generated cycle directive needs `Track` hand-added. Make the generator
emit it, and re-align the spec AC that describes the skeleton. This retires the
interim hand-add.

## Changes — two coupled edits, test first

### 1. TEST (red-gate — mandatory, before the code edit)

Add or extend the `bin/cycle-open` test(s) to assert the generated skeleton
contains a `Track:` line in the required position — after the `Date:` line and
before `Documents in scope:` — per AC-CO-3 as corrected below. Run it and
**confirm it FAILS** against current code: `Track` is absent today, so this is a
genuine behavioral red, not a missing-module red. Only then make edit 2 to turn
it green.

### 2. CODE — `bin/cycle-open`, `render_directive` (~line 115)

Add a `Track: <A | B>` line to the generated skeleton, positioned exactly as the
canonical format has it: immediately after the `Date:` line, before
`Documents in scope:`. Emit it as the placeholder `Track: <A | B>`, matching the
other unfilled placeholders in the skeleton.

### 3. SPEC — `docs/packages/package-a-spec.md`, AC-CO-3

AC-CO-3 says the skeleton "matches the format in `skills/spec-review-cycle.md`"
but its inline enumeration omits `Track` — a drift from the now-agreed format.
Add a `Track:` line to that enumeration so the AC and the canonical format
agree. Routine edit: `package-a-spec.md` carries no lifecycle frontmatter
(`docs/**` is out of metadata scope). No status flips.

## Scope / do-not

- Touch only: `bin/cycle-open`, its test file(s), and AC-CO-3 in
  `docs/packages/package-a-spec.md`.
- Do **not** alter the cycle-directive format block in
  `skills/spec-review-cycle.md` — it is agreed and is the canonical source; the
  code and the AC conform to it, never the reverse.
- Do **not** flip any document status.

## Executor obligations

- Confirm the working tree matches the pinned blobs (or contains `206fc6e` in
  history with no intervening edits to the in-scope files) before editing.
- If the exact `Track` placement is ambiguous against the format block, STOP and
  surface — do not guess.
- Land via branch + PR (`main` is protected). Report the branch and PR number.
- Report what was done, not what this directive said.

## Done

`render_directive` emits `Track:`; AC-CO-3 enumerates `Track`; the test was
confirmed red then green; mechanical checks pass (`bin/tests/run`,
`bin/check-frontmatter --all` as applicable); branch + PR opened for Dave's diff
review.
