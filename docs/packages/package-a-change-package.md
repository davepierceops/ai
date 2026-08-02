# Change Package — Package A: Frontmatter & Cycle Tooling

Directive: `docs/cycles/streamlining-directive.md` (F1 + F4, plus F2's transform).
Spec and ACs: `docs/packages/package-a-spec.md`.
Branch: `package-a-tooling`. Commits `434e592` → `d6d2f70`.

**Release recommendation: ship to `main`, do not install the hook.**
**Tier: consequential. Human go/no-go required.**

---

## 1. Intent

Replace hand-executed methodology ceremony with scripts that are cheap to run
and that verify their own claims:

- **F1** — frontmatter status flips stop being hand-edits. `bin/flip-agreed`
  performs a status transition in a commit that proves it touched nothing but
  frontmatter; a pre-commit hook performs the `agreed → in-review` flip when an
  agreed document's content is edited.
- **F4** — cycle opening stops being manual SHA bookkeeping. `bin/cycle-open`
  reads reviewed SHAs from git, writes the directive skeleton, and emits the
  reviewed revisions as an upload bundle. `bin/bundle` computes the reference
  closure from entry-point context-sets.
- **F2 (transform only)** — `bin/migrate-frontmatter`, split into a mechanical
  `--plan` step and an `--apply` step. Package B consumes it.

Scripts live canonically in `/ai/bin/` and are never copied into project repos;
projects install a thin shim. Repo root comes from the invoking repo, and the
in-scope globs are read from the metadata policy at runtime rather than baked
into code.

## 2. Acceptance criteria

98 ACs in spec §3–§4, plus 21 added at the review gates (§8). All are behavioural.
Every AC has at least one test except the two named in §7 as unverified.

## 3. Implementation summary

Nine new executables and modules under `bin/`, Python 3 stdlib only, ~2,400
lines: `aimeta/{frontmatter,scope,repo,cli,closure}.py` and the CLIs
`check-frontmatter`, `flip-agreed`, `cycle-open`, `bundle`,
`migrate-frontmatter`, `install-hooks`, plus the POSIX-sh pre-commit shim.

`aimeta/cli.py` and `aimeta/closure.py` were not in the original file layout.
Both were accepted at the Reviewer gate and §2.3 was amended: AC-CO-9 requires
`cycle-open` and `bundle` to share *one* closure implementation, and six CLIs
otherwise duplicate the exit-code and diagnostic contract.

## 4. Test plan and results

**321 tests, 321 passing, 0 errors.** Real git throughout — `git init`
repositories, real commits, the real index, real installed hooks. **There is no
mocked git layer anywhere in the suite.**

Role separation held for the whole package: the Architect wrote the spec and
the deliberately-inert interface stubs; an independent Test Designer wrote every
test; a separate Coder wrote every line of implementation. The Coder never
edited a test, and the Test Designer never edited production code — verified by
diff at each round, not asserted.

| Stage | Commit | Evidence |
| --- | --- | --- |
| Red-gate | `434e592` | 232 tests, **222 failures, 0 errors**, every failure an `AssertionError` — a behavioural red against stubs, not a missing-module red |
| Implementation | `ea21174` | 232/232 green |
| Fix round 1 | `e1741ca` | 305/305 green after 73 tests added for the gate findings |
| Fix round 2 | `d6d2f70` | 321/321 green |

## 5. Review findings

Both gates ran twice. **This is the part of the package that matters most.**

The implementation reached a **fully green 232-test suite** — independently
authored, mock-free, exercising real git — and both gates then failed it on
**seven defects, three of them data-integrity**. The suite was not weak. Its
*aperture* was narrow: one git verb (`git commit -m`), one repo shape, one
encoding (UTF-8/LF), one environment. Every defect sat just outside it.

| Defect | Consequence | Status |
| --- | --- | --- |
| **B1** | Hook transcoded non-UTF-8 bytes in the index (`0xE9` → `U+FFFD`), then crashed *after* the mutation; `--no-verify` committed the corruption | closed, re-verified |
| **B2** | `git commit -- <path>` left the real index stale; two hook-approved commits landed `status: agreed` with a stale `last-reviewed` on an edited body | closed, re-verified |
| **B3** | Conflicted merge flipped documents agreed on the merged branch, nulling `last-reviewed` | closed, re-verified |
| **F2** | `flip-agreed` committed a hook-injected body change at exit 0 while claiming frontmatter-only | closed |
| **F3** | `grandfather: yes` never recorded, so migrated docs failed the check immediately after — landing on Package B | closed |
| **F4** | `cycle-open --out` wrote outside the repo | closed |
| **S1** | The *fix* for B2 re-opened B2: a failed mirror downgraded to a NOTE at exit 0 | closed, re-verified |

Two further findings came from the **Coder's own disclosure** rather than from
either gate — S1's root cause and the `index.lock` version coupling. Asking the
implementer "where is your fix narrower than the defect?" produced findings a
green run could not.

**The `index.lock` decision.** The B2 fix writes into `.git/index.lock`, which
git installs after the hook. The orchestrator initially recommended refusing
pathspec commits instead. The Reviewer disproved that by instrumenting git:
`lsof` shows **no open file descriptor** on the lock during the hook, so the
fd-versus-path race that would make this dangerous does not exist, and
`update-index` against a malformed lock refuses rather than writing garbage. The
mechanism stays; refusing would have imposed a certain cost on an everyday
workflow and trained `--no-verify`, the habit this package exists to remove.

## 6. Verification boundaries

- **Mock-verified:** nothing.
- **Contract-verified:** the frontmatter dialect, the metadata policy's field
  rules, in-scope glob extraction — against the policy text as the contract.
- **Live-verified:** hook installation and firing; index mutation; commit
  shaping; plain, pathspec, `-a`, `--amend` and conflicted-merge commits;
  non-UTF-8 documents *as blocked*; linked worktrees; split index; the shim
  under a minimal `PATH` and `LC_ALL=C`. In throwaway repositories **shaped
  like this one — not in this repo.**
- **Unverified:** any project repo other than this one; merge, rebase,
  cherry-pick and revert, which bypass pre-commit entirely; *processing* a
  non-UTF-8 document; CRLF documents; **any git version other than 2.54.0**;
  Linux, Windows, case-sensitive filesystems; concurrent git processes.
- **Deferred verification:** the `wne-crm` shim install, sequenced after
  Package A by the directive.

**Version-pinned assumption.** AC-CF-16's mirror depends on git's
partial-commit lock protocol, which is **undocumented**, verified on **git
2.54.0 only**. If a future git wrote the lock after the hook, the mirror would
be silently discarded and B2 would return — and unlike every other failure mode
here, that variant is *not* detectable from inside the hook. This is a standing
re-verification obligation before the hook is installed anywhere. The durable
alternative is a `post-commit` companion needing no undocumented behaviour.

**SLO / error budget:** not applicable. No production journeys, no telemetry
surface, no deployed service.

## 7. Known gaps

**Unverified branches (2).** `flip-agreed`'s post-commit exit-4 path, which
fires only when its own commit disagrees with what it staged — unreachable from
outside the process, kept to a single comparison, verifiable by reading. And
`AC-CF-20` auto-skips on a case-sensitive filesystem, so a Linux run showing one
skip is expected.

**Enforcement escapes, accepted and disclosed.** Each is a deliberate act that
prints a diagnostic, and none is reachable by ordinary work:
`MERGE_HEAD` present; a staged symlink at an in-scope path; a HEAD version that
is not valid UTF-8; merge/rebase/cherry-pick/revert; `--no-verify`.

**A gap the fix did not close.** AC-CF-23 warns when the glob set matches
*nothing*. Verified: a single typo'd glob among several that still match is
**silent in hook mode**, and that is the more likely failure. Per-glob warnings
exist in `--all` and were deliberately kept out of `--staged`, where they would
fire constantly in project repos that legitimately match only `specs/**`.
Mitigation: run `check-frontmatter --all` after any edit to the metadata
policy's Scope section. The AC was scoped to the rarer case; that was an
orchestrator error, recorded rather than quietly widened.

**Seven further follow-ups** in spec §8.7: trivia misattribution inside block
lists; the undecodable-HEAD bypass; `--all` following symlinks; `relpath_of`
resolving symlinks before scope matching; the disposition file written after the
documents; `concat` dropping an undecodable body; `| head` exiting 120.
`migrate-frontmatter --out` remains CWD-relative and now disagrees with
`cycle-open --out` — a spec/code inconsistency, unpinned by tests, left rather
than changed unpinned behaviour.

## 8. Operational notes

**The hook is deliberately NOT installed in this repo.** Measured today:
**34 of 38 in-scope documents fail, 46 findings** (28 `missing-frontmatter`,
5 `missing-status`, 6 `missing-audience`, 6 `missing-last-reviewed`,
1 `invalid-status`). Installing now would block nearly every commit. Install is
Package B's step, after the migration lands.

This also matters because `--no-verify` disables the *entire* hook for a commit,
suspending the flip as well as the legacy check. A long interim between A and B
would train exactly the habit the hook exists to remove.

**Correction to a claim carried in the agent reports.** The Test Designer's
later reports state that seven spec observations (S1–S7) "still stand." They do
not — all seven were resolved in spec §8 before the fix rounds. The agent was
reporting from memory of the pre-edit spec rather than re-reading it.

**A process error, recorded.** Commit `e1741ca` landed while a hard gate was
still running, with "suite 305 green" in its subject — self-certifying before
the gate returned, and leaving the gate reviewing a moving tree. Production code
happened not to change, so that gate's evidence held. The correct pattern is to
hold the commit until the gate reports, or to tag the reviewed tree.

## 9. Human gate

**Required.** New executable tooling that mutates the git index unattended in
developers' repositories, resting on an undocumented git behaviour verified on a
single git version. Both gates independently called for it.

Blocked until a go: merging `package-a-tooling` to `main`.
Not in this package regardless: installing the hook here, and the `wne-crm`
shim.

## 10. Decisions for Dave

1. **Merge to `main`?** The package is green, both gates are satisfied, and it
   changes no agreed document and installs nothing.
2. **Package B timing.** The interim between A and B is where the `--no-verify`
   habit forms. Sequencing B next is the recommendation.
3. **Sibling-`ai/` vs `$AI_METHODOLOGY_HOME` as the primary documented install.**
   Git GUIs, IDEs and Xcode do not inherit a shell profile, so the env var will
   be unset and every commit from those clients fails closed with a clear
   message. This is a decision about who commits from what tool, and it gates
   the deferred `wne-crm` shim install.
