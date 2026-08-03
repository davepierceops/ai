# Manifest

This file holds one thing git and the metadata policy cannot derive: the
context-set bundle definitions. Everything else it used to carry has been
removed, because a second copy of a derivable fact drifts and then lies — the
canonical-vs-derived principle in `policies/source-of-truth-policy.md`, applied
to this file.

The former assembly notes carried nothing git does not; see
`docs/packages/package-c-change-package.md` §5.

## What is no longer here, and where it lives instead

**The file registry.** This file used to list every source-of-truth document.
That list is now derived: the in-scope set is the glob list in
`policies/document-metadata-policy.md` ("In scope (frontmatter required)"),
and `bin/check-frontmatter --all` reports how many paths that glob set
currently matches. A hand-maintained registry could only ever be a stale mirror
of the filesystem — and it was: four files were registered retroactively in
v0.5 after going missing.

**Document versions and status.** Governed by
`policies/document-metadata-policy.md`. The version of a document at reference
time is the SHA of the last commit touching it. There is no repo-wide version
number and no per-document version numbers. In-scope documents carry YAML
frontmatter (`status`, `last-reviewed`, `audience`), enforced by a pre-commit
hook. Instantiated project PRDs/TRDs live in project repos and adopt the same
schema, standing up their own enforcement at project setup.

**The changelog.** Git history is the changelog. The version sections below are
frozen: see the tombstone.

## Context-set bundles

Paste only the sets a chat needs. `base` is always included.

- **Spec chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering`
- **Implementation chat:** `base` + `spec-and-change-discipline` + `ai-native-engineering` + `testing-and-verification`
- **Release / risk chat:** `base` + `testing-and-verification` + `production-grade-software`
- **Everything:** all context-sets.

These are hand-maintained, and they are the reason this file exists.

The directive that produced this rewrite deferred "`bin/bundle` superseding
MANIFEST bundle definitions — after F4 lands and closure output is trusted."
That deferral rests on a false premise and is withdrawn.

`bin/bundle` computes a **reference closure**: what a document cites,
transitively. A bundle is a **curated judgment**: what a conversation needs.
Those are different questions, and **no reference closure reproduces a curated
bundle.** Measured against "Spec chat" (`base` + `spec-and-change-discipline` +
`ai-native-engineering`): the unbounded closure from `spec-and-change-discipline`
returns every context-set, plus trackers, historical artifacts, and this file;
at `--max-depth 1` it returns two context-sets and misses
`ai-native-engineering`. **No depth returns three** — the context-set count goes
2, 4, 6.

The cause is structural, and it is **two failures in opposite directions**.
`bin/bundle` walks two graphs. The `depends-on` graph is too *sparse* to reach a
bundle's other members: every context-set declares `depends-on: [base]` and
nothing else, so it is a star. The in-body citation graph is too *dense* and not
curatorial: `ai-native-engineering` is reached only at depth 2, and not through
`depends-on` at all — it arrives as a citation inside
`policies/commit-and-change-control-policy.md`, alongside twenty-odd unrelated
paths. Overshoot in one graph, undershoot in the other; no depth lands on three.

What distinguishes the bundles lives in each set's prose `include-when:` field,
which is editorial judgment, not a reference.

So the two are **complementary, not successive**. Use `bin/bundle` to answer
"what does this document cite, and did I miss something?" Use the lists above
to answer "what do I paste into this chat?"

**What is not foreclosed.** These lists could become derivable if bundle
membership were declared as *data* — a `bundles:` frontmatter key, or a small
`bundles.yaml` — which relocates the judgment without removing it. That is a
different change from closure computation, and it has not been proposed or
costed. Enriching `depends-on` to fake it is **rejected on two grounds**: "a
spec chat also wants the AI-native set" is co-selection, not dependency, so
encoding it there would corrupt the field for every other consumer,
`bin/bundle` included — and it would not even work, since the in-body walk
overshoots regardless of how good the `depends-on` edges get. If
membership-as-data is ever built, these lists become a second copy of a
derivable fact and should move — the same principle that emptied the rest of
this file.

---

## Tombstone — frozen version history

**The sections below are historical record, not a live convention.** They were
written when this repo declared a tree version and maintained a changelog. Both
practices ended: git history is the changelog, and the git SHA is the version.

Nothing is appended here again. They are kept because they explain decisions
whose reasoning is not otherwise recoverable — why the specs, the two-tier
release gate, and the Test Designer/Coder split arrived when they did — and
deleting them would lose that. Read them as archaeology, and treat any file
list, status word, or version number inside them as expired.

### v0.2 changes

- Revised `operating-model.md` for stronger trust model, standard change flow, definition of done, and escalation rules.
- Revised `context-sets/base.md` for sharper agent behavior, response shape, mock rule, and tooling rule.

### v0.3 changes

- Revised `context-sets/testing-and-verification.md` to define verification classes, confidence ledgers, test-plan requirements, and anti-patterns.
- Revised `policies/verification-boundary-policy.md` with boundary declaration schema, status labels, triggers, and release impact labels.
- Revised `roles/skeptic-risk-agent.md` into an operational review role with checklists, severity categories, and output template.

### v0.4 changes (methodology merge)

Merged the spec-first / test-driven methodology spine into this operating model.

- Added `specs/` with PRD and TRD templates. The TRD is the standing technical spec; the per-change architecture summary (Architect) sits between the TRD and Issues.
- Added `policies/source-of-truth-policy.md`: PRD → TRD → ACs → architecture summary → Issues; Issues are derived; conflicts are a hard stop.
- Added `policies/commit-and-change-control-policy.md`: two-tier release gate (routine flows to release on evidence; consequential requires explicit human go/no-go at the release decision) plus the red-gate and Test Designer/Coder separation.
- Added `context-sets/spec-and-change-discipline.md`: canonical sequence, red-gate, and operating habits (one question at a time, document consistency, loose-end tracking).
- Imposed Test Designer / Coder separation in `roles/test-designer-agent.md`, `roles/coder-agent.md`, and `context-sets/ai-native-engineering.md`.
- Gave the Architect role TRD authorship and the per-change architecture summary in `roles/architect-agent.md`.
- Revised `operating-model.md`: spec-first summary, source-of-truth section, spec-first change flow with role mapping, release gate, and red-then-green definition of done.
- Added composition front-matter (`include-when`, `depends-on`) to all context-sets and the bundles below.

### v0.5 changes

- Added `skills/spec-review-cycle.md`: reviewer-gated spec review cycles run
  chat-for-triage, Claude Code-for-execution. Cycle directives (with reviewed
  commit SHAs) are the handoff artifact; full documents never round-trip
  through chat.
- Linked the skill from `operating-model.md` change-flow step 1 and from
  `context-sets/collab-workflow.md` (mode distinction).
- Retroactive registration of files predating this commit and missing from
  this manifest: `roles/orchestrator-agent.md`, `roles/context-quality-reviewer.md`,
  `roles/spec-reviewer-agent.md`, `context-sets/collab-workflow.md`.
- Regenerated `TREE.txt` (was stale: pre-flattening paths, missing newer files).

### Post-v0.5 changes (SHA-versioned per document-metadata-policy)

- Added `policies/document-metadata-policy.md`: YAML frontmatter schema,
  git-SHA versioning, revision lifecycle, and agent build-gating rules.
  Removed the repo-wide `Tree version` declaration from this file — the
  version headings above are historical record, not a live convention.
- Added `skills/conversation-retro.md` (draft): per-conversation
  retrospective skill. Retros are per-project tracker-class artifacts
  (`retros/` in project repos, no lifecycle frontmatter); methodology
  changes they surface enter via spec-review cycles only.
- Added `roles/chief-of-staff.md` (draft): supersedes
  `roles/orchestrator-agent.md` (now `superseded`), carrying the
  decomposition/handoff responsibility redesigned around state assessment,
  pre-staging, and tranches. Repointed the audience field of 11 role/skill
  docs, `README.md`'s role-loading guidance, `context-sets/ai-native-engineering.md`'s
  team model, and `OPEN-ITEMS.md`'s live what's-needed entry from
  `orchestrator-agent` to `chief-of-staff`.
