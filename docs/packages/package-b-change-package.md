# Change Package — Package B: Frontmatter Migration and Hook Self-Hosting

Directive: `docs/cycles/streamlining-directive.md` (F2), plus two requirements
folded in at Package A's release decision (Dave, 2026-08-01).
Spec and ACs: `docs/packages/package-b-spec.md`.

**Status: complete. The hook is live in this repo.**
**Tier: routine — flowed to completion on evidence.** See §7 for why, and for
the one item that is Dave's.

---

## 1. Intent

Make this repo compliant with `policies/document-metadata-policy.md`, then turn
the hook on. The order was load-bearing: installing before migrating would have
blocked nearly every commit, since 34 of 38 in-scope documents were failing.

## 2. What changed

**One commit for the migration** (`b79e343`), so it is independently
revertible. The hook install touches `.git/hooks/`, which is untracked — it is
machine state, not a repo change, and `bin/install-hooks --uninstall` reverses
it.

Two additional commits exist from the live end-to-end verification (§5): an
edit to `policies/document-metadata-policy.md` and its revert. They are labelled
as verification commits. Their presence in history is the cost of testing the
hook against a genuinely `agreed` document in the real repo rather than only in
a fixture; the alternative was to claim the verification without doing it.

## 3. Migration result

| | Before | After |
| --- | --- | --- |
| In-scope documents | 38 | 38 |
| Documents with findings | 34 | **0** |
| Findings | 46 | **0** |

34 documents migrated; the 4 already-compliant documents are byte-identical
(`git diff` did not touch them).

**Two migration classes, where the directive named one.** 28 documents had no
frontmatter and a legacy `Status:` line. Six context-sets already carried
*composition* frontmatter (`context-set`, `purpose`, `include-when`,
`depends-on`) plus a legacy body `Status:` line and no lifecycle fields — these
were merged into, not overwritten, and their composition fields survive intact.

**Performed by the tool, not by hand** (AC-B-5). The plan that drove it is
committed at `docs/packages/package-b-migration-plan.md` and is the batch
record: one block per document, judgment fields resolved, machine-readable.

## 4. The judgment calls, and their reasoning

**`status`: preserved, never upgraded.** All 34 migrate as `draft` with
`last-reviewed: null`. **Nothing migrates as `agreed`, so no grandfather
disposition list was written and the clause does not apply** — which, per the
policy's own wording, is exactly what its absence means. Migrating anything else
as `agreed` would assert a review that never happened. This is the honest
outcome, and it has a consequence worth stating plainly: **this repo's
methodology documents now declare, in their own metadata, that they are not
agreed.** That is true today. Package C and later cycles are how they earn it.

`context-sets/base.md` carried `Status: stable` — a maturity word from a
superseded convention, not an agreement — and migrates as `draft`.

**`audience`: a rule, not 34 independent choices** (AC-B-3). Stated here so a
future document can be classified without re-deriving it:

| Class | `audience` |
| --- | --- |
| `README.md`, `operating-model.md`, `policies/**`, `context-sets/**`, `boundaries/**` | `[all-roles, human]` — these bind every role; narrowing them would let a role skip a rule that governs it |
| `roles/<slug>.md` | `[<slug>, orchestrator-agent, human]` — the role itself, the orchestrator that assigns it, and Dave |
| `skills/<name>.md` | the roles that execute the procedure, plus `human` |

The rule produced one defect on first application: `roles/orchestrator-agent.md`
came out as `[orchestrator-agent, orchestrator-agent, human]`. Caught by
inspecting the generated distribution before applying, and fixed. Worth noting
because a rule applied mechanically will produce mechanical mistakes, and the
review step is what catches them.

**Incidental fix.** `context-sets/spec-and-change-discipline.md` carried two
conflicting status declarations: a frontmatter `status: draft v0.1` and a body
`Status: draft`. The frontmatter value was invalid twice over — not in the
policy's status set, and embedding a version number, which the policy lists as
an *excluded field*. It is the concrete worked example of the drift the policy
exists to prevent, and it is now single-sourced.

## 5. Evidence

- **Dry run before applying** (`--apply --dry-run`): 34 files, and the only
  non-frontmatter line removed anywhere in the batch was `-status: draft v0.1`.
- **Body identity verified independently of the tool that did the work**
  (AC-B-6). A separate script compared each migrated document's post-frontmatter
  body against its `HEAD` version minus the legacy `Status:` line: **34
  compared, zero mismatches.** Using the migration tool to verify its own
  migration would have proved nothing.
- **`check-frontmatter --all`: 0 findings**, 38 files matched, no unmatched
  globs (AC-B-7).
- **Full suite: 321 tests, 321 passing, 0 errors** — re-run after migration and
  after install.
- **End-to-end in this repo, hook live** (AC-B-18): a content edit to the
  genuinely `agreed` `policies/document-metadata-policy.md` committed as
  `status: in-review`, `last-reviewed: null`. Reverted; the document is back to
  `agreed` with its review pointer intact and the tree is clean.
- **Rollback verified once** (AC-B-19): `--uninstall` removes the hook,
  re-install restores it.

## 6. The standing obligation, discharged

Package A carried a re-verification obligation: the index-mirror mechanism
depends on git's **undocumented** partial-commit lock protocol and had been
verified on git 2.54.0 only. Package B is the first install anywhere, so it fell
due here (AC-B-14, AC-B-15).

**Re-verified by direct observation on the installed git, `git version
2.54.0`** — the same version, so the obligation is satisfied rather than merely
deferred:

```
pathspec commit:  GIT_INDEX_FILE=.git/next-index-14582.lock
                  .git/index.lock exists, 290 bytes, before the hook runs
git commit -a:    GIT_INDEX_FILE=.git/index.lock   (the same file the flip writes)
```

Both premises hold: the lock is populated before the hook, and the `-a` case is
the compare-against-itself case AC-CF-24 exists for. The AC-CF-16 and AC-CF-22
suites pass (17 tests).

**The obligation does not expire.** It recurs on any git upgrade on this
machine, and again for each project repo the shim reaches. The durable fix
remains the `post-commit` companion named in `package-a-spec.md` §8.6.

## 7. Decision 3 — a finding, not an implementation

Dave's decision at the Package A gate was: sibling-directory convention
(`../ai`) primary, `$AI_METHODOLOGY_HOME` the documented override, rationale
being that GUI clients (Xcode, GUI git tools) do not inherit a shell profile, so
env-var-primary means commits fail closed with no visible reason.

**Verified empirically: that failure does not occur.** The shim checks the env
var first but does not require it — it falls through to the repo itself, then to
`../ai`. Simulated GUI conditions (`env -i`, no `AI_METHODOLOGY_HOME`, minimal
`PATH`, no shell profile) with a sibling clone present:

```
FLIPPED policies/p.md: agreed -> in-review (content edit)
[main 30c1f1d] x
```

It works. Resolution only fails when there is **neither** an env var **nor** a
sibling clone — which no reordering fixes, and which already produces an
`ERROR:` naming both paths and the fix, exactly as AC-B-12 requires.

So the intent behind decision 3 is already implemented. What remains is narrower
than the decision as worded: **precedence when both exist.** Today the env var
wins, which is what "override" conventionally means and is consistent with
"sibling is primary, env var is the documented override". Inverting it would
make the env var *not* an override and would break deliberately pointing at a
different clone.

**No code change was made.** Building one would either be a no-op against the
stated rationale or silently invert precedence that was not asked to be
inverted. **This is the one open item for Dave: confirm the current precedence
stands, or direct the inversion** — a one-line change if wanted. AC-B-10 through
AC-B-13 are therefore **not implemented**, and the spec records why.

## 8. Verification boundaries

- **Live-verified:** the migration against the real corpus; the hook installed
  and firing in this repo against a genuinely `agreed` document; install and
  uninstall; the lock protocol on git 2.54.0.
- **Contract-verified:** every migrated document against the metadata policy, by
  the enforcement the policy itself specifies.
- **Unverified:** any project repo other than this one; git versions other than
  2.54.0; the four enforcement escapes carried from Package A (`MERGE_HEAD`, a
  staged symlink, an undecodable HEAD, and merge/rebase/cherry-pick/revert),
  all unchanged and still disclosed.
- **Not applicable:** SLO / error budget. No production journeys.

## 9. Known gaps

Everything carried from Package A stands unchanged: the seven follow-ups in
`package-a-spec.md` §8.7, the two unverified branches, and the four enforcement
escapes.

**Newly live, and worth naming:** the AC-CF-23 gap tracked in `OPEN-ITEMS.md` is
no longer theoretical. The hook is now enforcing in this repo, so a typo in the
metadata policy's Scope section would silently narrow enforcement rather than
failing loudly. **Mitigation, now a real operating habit: run
`bin/check-frontmatter --all` after any edit to that Scope section.** That a
habit is the mitigation is precisely the weakness — it is the class of control
this initiative exists to replace.

## 10. What this changes about committing here

From now on, in this repo:

- Editing an `agreed` document's content and committing flips it to
  `in-review` with `last-reviewed: null`, automatically, in that same commit.
- A commit adding or editing an in-scope document with invalid frontmatter is
  **blocked**. `git commit --no-verify` overrides, and suspends the flip as well
  as the check.
- `bin/flip-agreed` is the way to move a document to `agreed`; it proves its own
  commit touched nothing but frontmatter.

## 11. Remaining directive sequence

- **Package C** — F3 + F5 + F7 batched: the verdict-first review artifact schema
  in `skills/spec-review-cycle.md`, the `human-gate` issue as the canonical
  pending-gate record in `policies/commit-and-change-control-policy.md`, and
  MANIFEST shedding its derivable registers. Note these documents are now
  `in-review`-eligible: editing them will trip the hook, which is the intended
  behaviour and the first real exercise of it.
- **Package D** — F6 alone, a full spec-review cycle against the agreed metadata
  policy. It cannot use the expedited path it introduces.
- **Deferred:** the `wne-crm` shim install — unblocked by decision 3 either way,
  since both precedence orders work when a sibling clone is present.
