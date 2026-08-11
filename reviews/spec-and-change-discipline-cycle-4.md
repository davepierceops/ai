# Review: context-sets/spec-and-change-discipline.md — cycle 4

Verdict: ready
Reviewed: `context-sets/spec-and-change-discipline.md` @ `4ccfaeb`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-10
Scope: one sentence — the concurrency parenthetical, which pointed at `track`'s
definition to explain why the word for a concurrent workstream is *tranche*.
Checked: (1) that the parenthetical still does its job with the definition it
cited now gone, since its whole function is to stop an agent reaching for
"track"; (2) the `LEXICON.md` pointer, which must now land on a tombstone rather
than a definition and still be informative; (3) whether the finding this
parenthetical was written to close —
`reviews/spec-and-change-discipline-cycle-1.md`, the tranche/track collision —
stays closed under the retirement, or is dissolved by it; (4) the rest of the
concurrency paragraph and the truth-at-handoff paragraph above it, for any other
dependency on the dispatch vocabulary; (5) the whole document grepped for
`track` again after the edit, to confirm the only survivor is the
loose-end-tracking bullet, an unrelated verb.
Cross-checked: `LEXICON.md` (`Track` tombstone; Spec state),
`skills/directive-dispatch.md`, `roles/chief-of-staff.md` (Open spec deltas),
`reviews/spec-and-change-discipline-cycle-1.md` (the collision finding) and
`-cycle-2.md`.
Not inspected: Definition of done, the loose-end bullets, and the derived-field
lesson — untouched since cycle 3.
Findings: none

One note. The cycle-1 finding is now closed *twice over*: the collision it named
was between two live terms, and one of them no longer exists. The parenthetical
is kept anyway rather than deleted, because the reason it existed — an agent
reaching for the nearest available word for a concurrent workstream — does not
depend on `track` being defined, and the tree still holds nine directives whose
headers read `Track: A`. A pointer that says "not this word, and here is why"
outlives the word.

Prior cycle: `reviews/spec-and-change-discipline-cycle-3.md`
