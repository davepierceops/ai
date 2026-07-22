# Gate Review — Cycle 4: policies/document-metadata-policy.md

Reviewer: Dave (human agreement)
Date: 2026-07-21

Cycle 4 reviews a portability revision: the removal of cross-repo cycle
references from the policy so it can travel to projects adopting this
methodology without dangling references. This is a content revision, not
a confirmation pass — it changes agreed text and supersedes two earlier
decisions verified in cycle 3.

## Scope and reviewed state

- Document: `policies/document-metadata-policy.md`, status `in-review`,
  reviewed on `main` at commit **`ea6b44e`** (the portability revision).
- Prior agreed state: cycle 3 signed off the policy at `052559a` and its
  agreement package; this cycle reviews the changes committed on top of
  that agreed baseline.

## Changes reviewed

1. **Grandfather clause — de-referenced and parameterized.** Cycle 3's
   B2 verified the clause pointed at `docs/cycles/cycle-2-directive.md`
   as the canonical disposition record. That pointer is a cross-repo
   reference: correct in this repo, a dangling reference in any project
   that adopts the policy without this repo's cycle history. The clause
   now states that the adopting repo records its own one-time disposition
   list at adoption and its adoption record declares where that list
   lives; a document absent from the list does not qualify; if no list
   exists, the clause does not apply and normal rules govern. This
   supersedes cycle-3 B2's verified state — intentionally. For this repo,
   the existing `docs/cycles/cycle-2-directive.md` (as amended by
   cycle-3 B1) is that disposition list; no change to the directive is
   required.
2. **Out-of-scope enumeration — "cycle directives" removed.** Cycle
   directives were never in the path-based in-scope set, so their removal
   from the out-of-scope prose changes nothing mechanically; it removes a
   cycle reference from portable text.
3. **Agent behavior — cycle-directive clause replaced.** "unless a cycle
   directive says so" (for loading a draft methodology doc as governing
   context) becomes "unless the human explicitly directs it for a
   specific task." Same gate, no cycle dependency.
4. **`re-review-trigger` optional field — deleted.** The field fired on
   an event occurring in another document, producing no local diff for a
   hook to enforce on; the flip depended on a human or agent noticing,
   assigned as a "shared obligation" (unowned). An unenforceable control
   that lets a doc sit at `agreed` past the condition that should unseat
   it is precisely the "document falsely claiming review currency" the
   policy names as worse than an absent record. The field also carried
   an internal contradiction ("owner accepts the maintenance burden" vs.
   "shared obligation"). Deleted rather than inverted; the enforceable
   inversion (source doc carries a dependents list, editing the source
   flips dependents) is a dependency-graph build not currently justified.
   This was the only optional field, so the Optional fields section is
   removed. Blast radius confirmed nil: no in-scope document carried a
   `re-review-trigger:` line; surviving mentions are in review artifacts
   and cycle directives (out of scope, history).

## Regression / drift check

Clean. The revision from the agreed `052559a` baseline touches only the
policy file and only the hunks described above. No template, MANIFEST,
or enforcement change rides along. The three superseded cycle-3
verifications (B2's pointer, the out-of-scope "cycle directives" line,
the agent-behavior cycle clause) are superseded by explicit later
decision, not by drift.

## Sign-off

**Agreed.** Dave reviewed the revision at `ea6b44e` and agrees it. The
policy is now free of cross-repo cycle references and portable to
adopting projects. On agreement, the policy flips to `agreed` in a
clean frontmatter-only status-transition commit with `last-reviewed`
pointing at this artifact @ `ea6b44e`.

Reviewed state for the record: `policies/document-metadata-policy.md`
@ `ea6b44e` (main).
