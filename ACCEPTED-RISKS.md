# Accepted Risks

This file tracks known risks that were reviewed and knowingly accepted rather
than fixed, per the release-readiness "known gaps and accepted risk" record
(`policies/release-readiness-policy.md`). Distinct from `OPEN-ITEMS.md`: an
open item is unresolved work; an entry here is resolved — a risk with a
stated owner's decision not to act on it, kept visible rather than absorbed.

Last updated: 2026-08-11

---

## 1. `bin/bundle --write` same-minute re-runs silently overwrite the prior output

**Source:** PR #70 review, 2026-08-11 (finding F1, docs/cycles/bundle-write-review-2026-08-11-directive.md).
Inherited from `bin/bundle-methodology`, which has carried the same behavior
since it shipped.

The written filename's stamp (`AC-BN-13`/`AC-BM-1`) is minute-resolution
(`%Y-%m-%d-%H%M`). Two `--write` runs against the same entry within the same
minute produce the same filename in the same `--out DIR`; the second run's
`dest.write_text(...)` silently overwrites the first with no collision
detection, no warning, and no distinct output.

**Declined 2026-08-11.** A same-minute re-run is a narrow, low-frequency
operator action (rerun the same bundle write twice in quick succession), and
the overwritten content is regenerable from the same repo state that
produced it — nothing is lost that cannot be reproduced by running the
command again. Adding collision handling (a sub-minute disambiguator, a
`--force` gate, etc.) was judged not worth the complexity for a
regenerable-artifact tool.

**Revisit if a real loss occurs** — i.e. if an operator relies on the
overwritten file's exact prior content (rather than the entry it renders)
and that content cannot be reconstructed.
