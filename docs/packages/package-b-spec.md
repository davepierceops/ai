# Package B — Frontmatter Migration and Hook Self-Hosting: Spec and ACs

Source directive: `docs/cycles/streamlining-directive.md` (F2), plus two
requirements folded in at Package A's release decision (Dave, 2026-08-01).

Depends on Package A (`bin/`, merged at `9fdf9c6`).

## 1. Intent

Make this repo compliant with `policies/document-metadata-policy.md`, then turn
the hook on. Three things, in order:

1. **Migrate** every in-scope document to YAML frontmatter, status-preserving,
   using `bin/migrate-frontmatter`.
2. **Change the shim's resolution order** to sibling-directory-first, per Dave's
   decision at the Package A gate.
3. **Install the hook in this repo** — the first install anywhere — after
   re-verifying the `index.lock` mechanism on the installed git.

Order matters: installing before migrating would block nearly every commit
(34 of 38 documents currently fail, 46 findings).

## 2. Measured starting state

`bin/migrate-frontmatter --plan` and `bin/check-frontmatter --all`, run against
`ab8392a`:

- **38 in-scope documents.** 34 to migrate, 4 already compliant
  (`policies/document-metadata-policy.md`, `skills/conversation-retro.md`,
  `specs/prd-template.md`, `specs/trd-template.md`) — these plan as
  `action: skip`.
- **46 findings:** 28 `missing-frontmatter`, 6 `missing-audience`, 6
  `missing-last-reviewed`, 5 `missing-status`, 1 `invalid-status`.
- **Two migration classes**, not one: 28 documents with no frontmatter and a
  legacy `Status:` line, and 6 context-sets that already carry *composition*
  frontmatter (`context-set`, `purpose`, `include-when`, `depends-on`) plus a
  legacy body `Status:` line and no lifecycle fields. The directive names only
  the first class; the transform handles both (AC-MG-9 and AC-MG-10).
- **Two documents need a human decision**, and only two:
  - `context-sets/base.md` carries `Status: stable`, which has no target in the
    policy's status set. The transform refuses to guess and plans `TODO`.
  - `context-sets/spec-and-change-discipline.md` carries **two** status
    declarations: a frontmatter `status: draft v0.1` and a body `Status: draft`.
    The frontmatter value is invalid twice over — not in the status set, and it
    embeds a version number, which the policy lists as an excluded field. The
    transform takes the body value and overwrites it. No decision needed; noted
    because it is the concrete case for why duplicate state drifts.
- Every other document maps mechanically: `draft` → `draft`, 33 of them.

## 3. The judgment fields

`status` and `grandfather` resolve to one decision (§3.1). `audience` is 34
decisions unless a rule is agreed, so §3.2 proposes a rule.

### 3.1 `status` for `context-sets/base.md`, and the disposition list

The policy's grandfather clause exists for exactly this moment: documents agreed
before the policy existed may migrate as `agreed` with `last-reviewed: null`,
*if* the repo records a one-time disposition list naming them. If no list
exists, the clause does not apply.

- **AC-B-1** The disposition decision is Dave's and is recorded in the change
  package. The default the executor proposes, absent a different instruction, is
  **`status: draft` for `base.md` and no disposition list at all** — because
  nothing in this repo has been through a review cycle that produced a review
  artifact except `document-metadata-policy.md`, which is already `agreed` and
  already points at one. Migrating anything else as `agreed` would assert a
  review that did not happen, and an empty grandfather list is the honest
  outcome. `stable` was a maturity word from a superseded convention, not an
  agreement.
- **AC-B-2** If Dave instead directs that some documents migrate as `agreed`,
  `bin/migrate-frontmatter --apply` writes them into
  `reviews/frontmatter-disposition.md` (AC-MG-14), and the change package
  declares that location as the adoption record the policy requires.

### 3.2 `audience` — a rule, not 34 choices

Proposed rule, to be agreed as a whole at the batch gate:

| Class | `audience` | Reasoning |
| --- | --- | --- |
| `README.md`, `operating-model.md`, `policies/**`, `context-sets/**`, `boundaries/**` | `[all-roles, human]` | These bind every role. Narrowing them would let a role skip a rule that governs it. |
| `roles/<slug>.md` | `[<slug>, orchestrator-agent, human]` | The role itself, the orchestrator that assigns it, and Dave. |
| `skills/<name>.md` | the roles that execute the procedure, plus `human` | Per-skill, listed in §3.3. |
| `specs/**` | already compliant — not migrated | — |

- **AC-B-3** Every migrated document's `audience` follows the rule above, and
  the change package states the rule so a future reader can apply it to a new
  document without re-deriving it.
- **AC-B-4** Every `audience` value is either a reserved value (`all-roles`,
  `human`) or a slug of an existing `roles/*.md` file. Enforcement rejects
  anything else, so a typo fails the batch rather than shipping.

### 3.3 Per-skill audiences

| Skill | `audience` |
| --- | --- |
| `boundary-audit` | `[reviewer-agent, skeptic-risk-agent, release-manager-agent, human]` |
| `change-package-creation` | `[coder-agent, release-manager-agent, orchestrator-agent, human]` |
| `evidence-review` | `[reviewer-agent, skeptic-risk-agent, release-manager-agent, human]` |
| `release-readiness-review` | `[release-manager-agent, skeptic-risk-agent, human]` |
| `spec-review-cycle` | `[spec-reviewer-agent, architect-agent, orchestrator-agent, human]` |
| `test-plan-review` | `[test-designer-agent, reviewer-agent, human]` |

## 4. Migration execution

- **AC-B-5** The migration is performed by `bin/migrate-frontmatter --apply`,
  not by hand. Hand-editing 34 documents is the failure mode the tool exists to
  remove, and it would not be reviewable as a batch.
- **AC-B-6** The applied result changes **only** frontmatter and the deletion of
  the legacy `Status:` line. Verification is mechanical, not visual: for every
  migrated document, the body after the frontmatter block is byte-identical to
  the pre-migration body minus that one line (and one collapsed blank line).
  A diff that touches prose fails the batch.
- **AC-B-7** After `--apply`, `bin/check-frontmatter --all` reports **zero
  findings** across all 38 in-scope documents (AC-MG-13).
- **AC-B-8** The 4 `action: skip` documents are byte-identical before and after.
- **AC-B-9** The migration lands as one commit, separate from the shim change
  and separate from the hook install, so each is independently revertible.

## 5. Shim resolution order (Dave's decision, Package A gate)

**Decision as given:** sibling-directory convention (`../ai`) is primary;
`$AI_METHODOLOGY_HOME` is the documented override for nonstandard layouts.
Rationale: the env var is unset in GUI clients (Xcode, GUI git tools), so
env-var-primary means commits fail closed with no visible reason — and mystery
enforcement failures are precisely the overhead class this initiative removes.
The sibling convention matches the actual side-by-side clone layout and needs
zero configuration.

- **AC-B-10** The shim resolves the methodology home in this order:
  1. a sibling directory named `ai` (`<parent-of-repo-root>/ai`),
  2. the invoking repo itself, when it contains `bin/check-frontmatter` (the
     self-hosted methodology repo),
  3. `$AI_METHODOLOGY_HOME`, when set and valid.

  *(Note the inversion: `$AI_METHODOLOGY_HOME` moves from first to last. It
  remains a true override in the sense that it is honoured when the earlier
  candidates do not resolve — but a set-and-valid env var no longer silently
  wins over a sibling clone. If a layout needs the env var to take precedence,
  that is a further decision, not something to assume here.)*
- **AC-B-11** `aimeta.repo.methodology_home` resolves in the same order as the
  shim. Two different orders in two places is a defect by construction.
- **AC-B-12** When no candidate resolves, the error **names both resolution
  paths and the fix** — the expected sibling location and the env-var override —
  in the shim's own `ERROR:` form, exiting with a documented code. A developer
  who has never read this spec must be able to fix it from the message alone.
- **AC-B-13** Existing ACs that pin the old order are amended rather than
  deleted: AC-RP-2 and AC-IH-2 now assert the §5 order. `docs/packages/package-a-spec.md`
  §2.1 is corrected in the same commit, so the two specs never disagree.

## 6. Hook install and the standing obligation

- **AC-B-14** Before the hook is installed, the `index.lock` mechanism is
  re-verified **on the git version actually installed on this machine**, and the
  result is recorded in the change package with the version string. Package A
  verified it on git 2.54.0 only, and the mechanism depends on git's
  undocumented partial-commit lock protocol. This is the first install anywhere,
  so this is the first time the obligation falls due.
- **AC-B-15** The re-verification is behavioural, not a version comparison: run
  the AC-CF-16 and AC-CF-22 suites, and confirm by direct observation that
  `.git/index.lock` exists and is populated before the hook runs during a
  pathspec commit. A version string alone proves nothing.
- **AC-B-16** If re-verification fails, the install stops and the finding goes
  to Dave. The migration still stands on its own; the hook is what waits.
- **AC-B-17** The hook is installed via `bin/install-hooks`, not by hand, and
  the installed file carries the managed marker so `--uninstall` can remove it.
- **AC-B-18** After install, a real end-to-end check in this repo: a content
  edit to an `agreed` document flips to `in-review` in the resulting commit; a
  frontmatter-only change does not; and `bin/flip-agreed` still produces a
  clean one-path commit with the hook live.
- **AC-B-19** Rollback is documented in the change package and verified once:
  `bin/install-hooks --uninstall` returns the repo to no-hook state.

## 7. Out of scope

- The `wne-crm` shim install. Dave's decision 3 unblocks it with no further
  design decision, but it is a separate change in a separate repo.
- Every follow-up in `package-a-spec.md` §8.7, and the AC-CF-23 gap now tracked
  in `OPEN-ITEMS.md`.
- Package C (ceremony policy edits) and Package D (the F6 routing change).

## 8. Known risks

1. **The migration touches 34 documents at once.** That is the point — one batch
   gate rather than 34 review cycles — but it means a transform defect lands
   everywhere simultaneously. AC-B-6's mechanical body-identity check is the
   control, and `--apply` is all-or-nothing (AC-MG-8), so a partial write is not
   a possible outcome.
2. **Migrating as `draft` is a claim too.** Every document will assert
   `status: draft` with `last-reviewed: null`. That is accurate today and it is
   the honest starting point, but it also means the repo's own methodology
   documents are, by their own metadata, not agreed. Package C and later cycles
   are how they earn `agreed`.
3. **Turning the hook on changes the cost of every future commit** in this repo.
   That is intended. The AC-CF-23 gap means a typo in the metadata policy's
   Scope section can silently narrow enforcement; the mitigation is running
   `check-frontmatter --all` after any Scope edit.
