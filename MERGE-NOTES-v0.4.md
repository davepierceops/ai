# Merge Notes: v0.4

## Scope

Merged two artifacts:

- **The operating model** (this tree, v0.3 / collab2): the AI-native, evidence-first model with roles, verification boundaries, policies, skills, and adapters.
- **The methodology spine** (Dave's original `methodology.md`): spec-first, test-driven development with a human verification gate.

The operating model was kept as the chassis because it is more mature and
already satisfies three of Dave's original requirements: modular context-sets,
paste-only-what's-needed loading, and provider independence (the adapter /
vendor-tooling-boundary model). The methodology's spec discipline and
composition ergonomics were bolted into it.

## Decisions Dave made

1. **Release gate: two-tier (option c), fired at the release decision.** Routine
   changes flow to release on evidence; the consequential class requires an
   explicit human go/no-go at the **release decision** (not at commit).
   Commit/deploy/release mapping is deferred to each project's TRD. Resolves the
   conflict between the methodology's "every commit needs approval" and the
   operating model's "humans don't gate on reading code" by separating two axes:
   the control surface (spec/tests/o11y, agentic code review) and the release
   gate (human go/no-go on evidence).
2. **Test Designer / Coder separation: separated.** For a unit of work these are
   always different agents. Overrides the operating model's prior "the same
   model may fill multiple roles" where it concerned these two.
3. **Standing TRD: kept.** The TRD remains the durable technical anchor, with
   the per-change architecture summary sitting between it and Issues. Not
   dissolved into context-sets + boundaries.

## Changes made

### Added
- `specs/prd-template.md`, `specs/trd-template.md` — the canonical spec spine.
- `policies/source-of-truth-policy.md` — PRD → TRD → ACs → architecture summary → Issues; conflicts are a hard stop.
- `policies/commit-and-change-control-policy.md` — two-tier gate, red-gate, separation rule.
- `context-sets/spec-and-change-discipline.md` — canonical sequence, red-gate, operating habits.

### Revised
- `operating-model.md` — spec-first summary, source-of-truth section, spec-first change flow mapped to roles, release gate, red-then-green definition of done.
- `roles/architect-agent.md` — TRD authorship + per-change architecture summary.
- `roles/test-designer-agent.md`, `roles/coder-agent.md` — separation imposed.
- `context-sets/ai-native-engineering.md` — separation made mandatory.
- `context-sets/*` — composition front-matter (`include-when`, `depends-on`).
- `README.md`, `MANIFEST.md` — document map, principles, bundles, v0.4 changelog.
- `CLAUDE.md`, `AGENTS.md` — spec-first reading, separation, and gate (kept thin).

### Carried over unchanged
All policies, skills, boundary docs, and the production-grade and base context
sets carried over intact; the strongest part of the source model — the
Skeptic/Risk role and the verification-boundary apparatus — was preserved as-is.

## Open items for Dave

- The (c) gate is provisional ("provisionally I'll answer (c)"). The
  consequential-change list in `commit-and-change-control-policy.md` is the
  concrete proposal; confirm or adjust the boundary of that class.
- Two earlier roles questions are now largely answered by structure but not
  explicitly ratified: whether Reviewer sign-off is a gate or advisory, and
  per-file vs single-file role granularity (the source model uses per-file).
- Nothing here has been committed. This set is a draft for Dave's verification.
