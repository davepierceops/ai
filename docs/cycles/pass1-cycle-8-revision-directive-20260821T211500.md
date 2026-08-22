# Directive — Pass 1, Cycle 8 revision: session definitions to Core

Date: 2026-08-21
Route: fresh
Model: frontier
Role: executor over canonical documents

Documents in scope, all @ 0f3711517d8a490f55b76b3ef87ddd31b195e3d0:
- docs/global-context/core.md
- docs/global-context/decision-layer.md
- LEXICON.md

Review triaged: reviews/LEXICON-cycle-10.md @ 0f37115.

## Decisions

### L8 — accept
Retired-terms Prompt entry: cut the clause "the one that opens a dispatch is a sync block". Confirm by grep that "dispatch" and "sync block" no longer appear in LEXICON.

### L9 — accept (Dave: single home, Core)
Session kinds are domain-neutral. Move LEXICON's two Sessions entries (decision session, execution session) into Core's Vocabulary section, placed first, before the three-layers statement. Take LEXICON's definition; where decision-layer's preamble states a detail LEXICON lacks, fold it in. Delete the Sessions section from LEXICON. Replace the decision-layer preamble with scope only: "Rules for decision sessions. Loads after Core and adds to it. Execution sessions never receive this file." — no definition.

## Execution

1. Fetch origin/main; verify the tree contains 0f37115 with no later edits to the three files.
2. Apply both decisions. Re-read all three files end to end for anything left inconsistent (Core 13). LEXICON's remaining sections should be Spec state, Tranche, and Retired terms.
3. Run bin/check-frontmatter --all. Stop and report on failure.
4. Commit on branch p1-cycle-8-revision, push to origin, report the SHA read back from git. No pull request. No status flip.

## Report shape

Per file: one line, before → after. Then branch and SHA. Then anything not applied as written.
