# Directive — Agreement flip: Trivium D3-reversal docs — davepierceops/ai

Date: 2026-08-09
Route: fresh
Model: Sonnet 5
Track: A

Purpose: land the agreement flip for the three reversal docs — a
**frontmatter-only** status transition via `bin/flip-agreed`. Dave gave the
explicit agreement (2026-08-09); this directive enacts it.

Preconditions (verify before running):
- PR #62 merged — `reviews/spec-review-cycle-cycle-4.md` is on main.
- All three docs are `status: in-review` on main.

## Flip — run `bin/flip-agreed` once per doc

Read `bin/flip-agreed --help` first; `--review` takes the review-artifact pointer
it validates (existence + SHA resolution). Pointers:

- `skills/directive-dispatch.md` → `reviews/directive-dispatch-cycle-3.md @ a7a915cddf3ca1fef774c17942f1e9406cc3715a`
- `LEXICON.md` → `reviews/LEXICON-cycle-3.md @ a7a915cddf3ca1fef774c17942f1e9406cc3715a`
- `skills/spec-review-cycle.md` → `reviews/spec-review-cycle-cycle-4.md @ 2fe299cade4325e80a3d51d3e2513c970f921b20`

Each sets `status: agreed` and `last-reviewed:` to its pointer.

## Constraints

- **Frontmatter-only.** `bin/flip-agreed` enforces this; if any doc shows a
  non-frontmatter diff, STOP and surface.
- Do not touch document bodies, the mirrors' content, `DEC-000150`, or any other
  file.
- If any `flip-agreed` invocation fails its pointer/SHA validation, STOP and
  surface — do not hand-edit frontmatter to force it.
- Land all three flips via one branch + PR. Report branch/PR.

## Done

Three docs at `status: agreed` with the correct `last-reviewed` pointers; one PR
opened; the diff is frontmatter-only across exactly the three files.
