# Cycle 3 Directive — policies/document-metadata-policy.md

Date: 2026-07-21
Documents in scope:
- `policies/document-metadata-policy.md` @ `052559a` (main)
- Agreement change package: branch `metadata-policy-agreement` @ `421fe8a`
  (`MANIFEST.md`, `specs/prd-template.md`, `specs/trd-template.md`)

Review artifact: `reviews/document-metadata-policy-cycle-3.md`
Prior cycle directive: `docs/cycles/cycle-2-directive.md`

Cycle 3 was a confirmation pass over the cycle-2 directive execution
(B1, B2, B3+A6, B4, A1, A5). All six directed items landed faithfully;
nothing regressed and no undirected changes rode along. One blocking
finding surfaced, located entirely in the decision record rather than in
the documents; it is dispositioned below.

## Decisions

### B1 (cycle 3) — accept
Finding: The cycle-2 migration disposition list contradicts the cycle-2
A1 decision for the two spec templates. `specs/prd-template.md` and
`specs/trd-template.md` appear in the cycle-2 list's "enter migration as
`agreed` (grandfathered)" set, while the same directive's A1 resolution
states their `agreed` status arrives via the normal gate, not the
grandfather clause, and their branch frontmatter correctly reads
`draft`. Because the amended grandfather clause makes that list the
canonical record, the repo would otherwise prescribe two dispositions
for the same two files.
Resolution: This directive supersedes those two lines of the cycle-2
migration disposition list. `specs/prd-template.md` and
`specs/trd-template.md` move from the grandfathered `agreed` set to the
`draft` set, per cycle-2 A1. They are next-gate candidates, not
grandfathered; their current revisions have not been re-gated since the
v0.4-agreed content changed on the agreement branch. The cycle-2
directive is committed history and is not edited; this entry is the
canonical correction the grandfather clause resolves to.

## Deferred / out of scope

- A2–A4 (cycle 2) remain deferred per the cycle-2 directive's execution
  notes; unchanged this cycle.

## Execution notes

- The agreement flip lands as its own commit touching only the policy
  frontmatter (`status: in-review` → `agreed`; `last-reviewed: null` →
  `reviews/document-metadata-policy-cycle-3.md @ 052559a`), immediately
  before the merge of the agreement package. This satisfies both the
  status-transition-commit-is-clean constraint (the flip commit contains
  nothing but the frontmatter transition) and the staged agreement
  sequence (flip then merge, nothing between). Advisory A1 (cycle 3).
- Reviewed content SHA is `052559a`; the flip changes frontmatter only,
  so `last-reviewed` points at that reviewed revision.
- Go granted by Dave on the cycle-3 report: resolve B1 as above, then
  flip and merge.
