# Directive — DEC-000060 owner-override flip of document-metadata-policy.md

Issued: 2026-08-07
Reviewed ref (STOP pin): `origin/main` @ `4e4e01b` (Merge pull request #40).
Executing session: **fresh instance, Opus 5** (directive execution over
canonical documents).

Self-contained: you need this file and the repository, nothing from the
conversation that produced it. Follow `skills/command-blocks.md` for any command
block you emit, the expedited path in `policies/document-metadata-policy.md` for
the agreement mechanics, `bin/flip-agreed`'s own contract for the transition, and
`policies/remote-write-verification-policy.md` after the push. Those govern; this
directive does not restate them.

## Precondition

Confirm `policies/document-metadata-policy.md`, `decisions/log.md`, and
`reviews/expedited-log.md` are at their `4e4e01b` state. If any has diverged from
the reviewed ref, STOP and surface it — the decision below was made against
`4e4e01b`.

## Decision (origin: this directive)

DEC-000060 — owner override. Dave, as project owner, agrees adding `LEXICON.md`
to the in-scope set of `policies/document-metadata-policy.md` and re-affirms the
document `agreed` **without a review cycle**, overriding the doc-only route's
condition-3 exclusion of enforcement-rule documents **for this revision only**.
This does not create a general owner-flip route for enforcement-rule documents.

## Work — three commits on branch `lexicon-in-scope-2026-08-07`

### Commit 1 — scope edit, frontmatter untouched

Add exactly one line, `` - `LEXICON.md` ``, to the "In scope (frontmatter
required)" list in `policies/document-metadata-policy.md`, immediately after the
`` - `README.md` `` line. Do **not** edit the frontmatter block.

Verify with `git show` that this commit's diff is the single added list line and
touches nothing in the frontmatter. Record this commit's SHA as **SHA1**.

(The prior local attempt failed because a `status: agreed → in-review` /
`last-reviewed → null` frontmatter edit was swept into this commit. The status
transition is Commit 3's job, done by tool, not by hand here.)

### Commit 2 — decision record + expedited-log entry

Append this block verbatim to `decisions/log.md`:

```
## DEC-000060 — LEXICON.md brought into metadata in-scope set by owner override
Date: 2026-08-07
Decision: The single-line additive edit naming `LEXICON.md` in the in-scope set
of `policies/document-metadata-policy.md` is agreed without a review cycle, on
owner authority. That document is agreed and its in-scope set is an enforcement
rule, so the doc-only cycle's condition 3 would otherwise force a full review
cycle; the owner overrides condition 3 for this revision only. This does not
create a general owner-flip route for enforcement-rule documents.
Context: The edit is additive — it brings a governed definitional document under
enforcement it already claims via its frontmatter — so it cannot blind
enforcement of itself. `bin/check-frontmatter --all` was verified green with
LEXICON in scope. A full multi-agent gate is disproportionate to a one-line
additive scope change.
```

Append this line verbatim to `reviews/expedited-log.md`, under its `## Entries`
list, substituting **SHA1** (Commit 1's full SHA):

```
- 2026-08-07 — policies/document-metadata-policy.md @ SHA1 — LEXICON.md added to in-scope set; owner override of doc-only condition 3, no review cycle (DEC-000060)
```

Commit both files together.

### Commit 3 — self-verifying flip

Run, substituting **SHA1**:

```
python3 bin/flip-agreed policies/document-metadata-policy.md --review "reviews/expedited-log.md @ SHA1" --status agreed
```

`flip-agreed` performs the frontmatter-only status/`last-reviewed` transition and
self-verifies. If it refuses for any reason, STOP and surface the diagnostic — do
**not** hand-edit frontmatter to satisfy it.

## Verify

`python3 bin/check-frontmatter --all` must exit 0.

## Ship

Push `lexicon-in-scope-2026-08-07`. Open a PR titled
`LEXICON.md into metadata in-scope set (DEC-000060, owner override)`.
STOP. **Do not merge** — Dave reviews the diff and merges.

## Report

Report what was done, not what this directive said: the three commit SHAs, the
`check-frontmatter` exit status, and the PR URL. On any instruction that cannot
be executed as written, or any concurrent change to the working tree, STOP and
surface it rather than improvising (`skills/directive-dispatch.md`, executor
obligations).
