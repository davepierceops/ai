# Review: docs/global-context/core.md — cycle 4

Verdict: ready
Reviewed: docs/global-context/core.md @ 089083c
Baseline: 04bfeae (cycle 2 reviewed state)
Reviewer: Spec Reviewer Agent
Date: 2026-08-21
Scope: the full revised file — frontmatter and all fourteen rules. Two passes:
(a) the two cycle-2 findings checked against the dispositions recorded in
`docs/cycles/global-context-cycle-3-revision-directive-20260821T192000.md`,
both accepts, both applied as dictated — rule 14 drops the enumeration and the
canonical-document exception and defers to a stated convention, keeping the ISO
8601 basic example and the "never random strings, hashes, or UUIDs" clause;
rule 6 replaces "A claim without a class is not a claim." with "State the
class; an unlabelled assertion is treated as *unknown*." and keeps the final
sentence; (b) all ten criteria of `docs/global-context/review-rubric.md` @
089083c re-applied to the revised text, with the diff `04bfeae..089083c` read
line by line for defects the revision introduced, and the corpus swept for text
the two edits leave stale (core rule 13).
Cross-checked: `docs/global-context/review-rubric.md` @ 089083c (criterion 9
was revised in the same commit and now carries the same "unless a stated
convention names the file" clause as core rule 14 — the two agree);
`skills/spec-review-cycle.md` (the review-artifact filename convention that
cycle 2's CORE-9 was about, and the artifact schema this file follows);
`docs/global-context/decision-layer.md` @ 089083c (duplication under criterion
4 — none; not reviewed); `docs/global-context/inventory.md` @ 089083c (bundle
order and provenance; its C3 row still carries the pre-revision sentence, which
is correct — the file states itself to be a triage record of source text, not a
governed restatement, so rule 13 does not reach it); `bin/bundle`,
`bin/bundle-methodology`, `bin/aimeta/frontmatter.py`.
Not inspected: the rubric was applied, not reviewed. `decision-layer.md` was
read for consistency only. Two items are excluded by the cycle directive and
were not assessed: that `all-decision-roles` is not yet a reserved audience
value, and that `docs/global-context/` is outside the frontmatter check's
in-scope globs. No bundler was run: `grep -n audience bin/bundle` returns
nothing at this SHA, so every claim about bundle membership or load order is
inferred from `inventory.md`'s recorded decision that core "is order 0 in every
bundle" and from `bin/bundle-methodology`, not observed from a generated
bundle. Prose style beyond criterion 6 was not assessed.
Findings: none
Prior cycle: `reviews/core-cycle-2.md`
