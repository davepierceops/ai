# Doc-Set Review — Question List (Draft)

Seeded from the permissions/autonomy conversation, 2026-08-02. Inputs for the
post-streamlining doc review, not decisions. Status: discussion draft, ungoverned.

**Pin lifted 2026-08-02**: this list is now the input to the active doc
review. All questions worked; see per-item decisions below. Q4 bundle
regeneration is the first execution item and gates on the streamlining
changes being landed on `main`.

---

## Q1 — Canonicalizing the permissions/autonomy work

Splits into three distinct questions:

**Q1a — The principle.** "Reduce human-gating to the actual human judgment;
gate only on that." An operating-model statement. Canonicalizes cleanly —
question is placement and wording, not whether.

**Q1b — The mechanics.** settings.json contents, sandbox config, notification
hooks. This is *environment config* — a document class the doc set does not
currently have. Policies govern documents; nothing governs tooling state.
Question: does the doc set need an environment-config class, and what governs
its lifecycle?

Complication: the methodology should stay mostly vendor-agnostic, and these
configs are mostly vendor-specific — they describe how one vendor's tool
(Claude Code) acts as the agent-runner (better word needed). Candidate shape:
a directory per supported vendor (e.g. `vendors/claude-code/`), with the
vendor-agnostic principle staying in the core doc set and only the config
artifacts living vendor-side. Deliberately deferring most of this thought —
the v1 requirement is a usable answer that is flexible/expandable, not the
final taxonomy.

**Q1c — Out-of-repo state.** Branch protection lives in GitHub's config, not
in git. Direction: a short, well-documented set of startup assumptions is
acceptable ("GitHub must be configured in the following way"). No
self-bootstrapping script for v1. Constraint: the list stays short by design —
if it grows to ~20 items, that is a signal the approach is wrong, not a reason
for a longer list. Decided: this document and the per-project frontmatter
enforcement item (currently in `OPEN-ITEMS.md`) are the same document — one
"project setup / adoption requirements" doc covering everything that must be
true when a project adopts the methodology.

---

## Q2 — Dispatch discipline for Claude Code directives

Three requirements per dispatch:

1. Route: fresh instance vs. instance with existing context (explicit each time)
2. Model: selected per quality/cost assumptions (mechanism undefined;
   hard-coding acceptable for v1)
3. Artifact: directive as `<naming-schema>.md`, committed and pushed, with
   relative-path@sha paste block for the target session

**Proposed shape: a skill plus a script, where the script is the enforcement.**
Per the F4 lesson, discipline belongs in tooling. A `bin/dispatch` that takes a
directive file, refuses to emit the paste block until the file is committed and
pushed, and stamps the SHA into the block makes the discipline impossible to
skip. The skill doc describes what the script enforces.

Decided 2026-08-02: shape accepted; **script deferred** (BACKLOG entry when
this list is processed). The discipline continues manually — seven cycles
without a slip means the failure mode is theoretical for now. Skill doc can
proceed without the script.

Open sub-questions:
- Directive naming schema: does not exist yet; needs definition
- Model-selection table: needs a home — likely a config file the script reads,
  so hard-coded-for-now is one edit from not

---

## Q3 — Orchestrator role: rename and redefine

Desired: proactive state-gathering, next-step determination, deep
workflow-preference context, minimal keystrokes and especially mousing.

**Underlying question first: where does current state live?** "What's in
flight" is currently scattered across OPEN-ITEMS.md, standing obligations in
chat summaries, and Dave's head. A proactive orchestrator is only as good as
its state sources.

- Q3a — **Decided: yes**, with a binding constraint: no maintained artifact
  that could be derived (the TREE.txt / MANIFEST-duplicate-register principle).
  The state surface must be *computed* — a defined read-sequence or a generated
  view over existing sources (OPEN-ITEMS → recent commits → pending gates) —
  never a hand-updated register that duplicates state living elsewhere. If it
  requires a human or agent to remember to update it, it is the wrong design.
  Follow-on, agreed: the read-sequence should be scripted (`bin/state` or
  similar) so state-gathering is a cheap render at session start rather than
  the agent reading source files raw. Deferred — BACKLOG entry alongside
  `bin/dispatch` when this list is processed.
- Q3b — **Decided:** the role assesses state and proposes next steps
  immediately upon invocation, unprompted — run `bin/state` (or the manual
  read-sequence until it exists), render current state, propose the next step.
  No open question remains; this is behavior spec for the role doc.
- Q3c — **Decided: chief-of-staff** (`cos`). TLA not obviously reserved in
  relevant lexicons. Replaces "orchestrator." Candidate for the "agent-runner"
  rename in Q1b as well — decide whether they are the same term when the role
  doc is written.

---

## Additional questions (Claude-proposed)

- **Q4 — Bundle regeneration. Decided: yes.** F4 landed the reference-closure
  scripts; the 7-file `BUNDLE_chat` predates them. First production use of the
  closure scripts, so first run carries a verification step: diff the computed
  closure against the known-good 7-file list before adopting. Superset → works,
  and caught files the hand-picked list missed. Missing one of the 7 → script
  bug, or a load-bearing file nothing references (a real finding either way).
  Exact match → hand-picked list verified closed. Sequencing: run against
  post-streamlining HEAD, after the in-flight session lands. Executes before
  the pin lifts (sole carve-out, per header).
- **Q5 — MCP-verification discipline. Decided: yes, canonicalize.**
  Fetch-back before reporting a commit as landed; HEAD-read before retrying a
  timed-out write. Hard-won across three sessions, currently living only in
  chat history — the named memory-dependence anti-pattern. Placement (skill vs.
  policy) and vendor-specificity (this is GitHub-MCP behavior, so possibly
  `vendors/`-adjacent per Q1b) resolved at doc-review time.
- **Q6 — Blast radius on existing docs. Resolved: reframed as the first work
  item *of* the doc review, not a question for it.** Audit existing agreed
  docs against this artifact's decisions; contradictions become findings and
  enter through a spec-review cycle — no second door. Likely blast radius for
  scoping: `commit-and-change-control-policy` (ask-on-push assumption),
  possibly `spec-and-change-discipline` and `operating-model` where they
  describe the permission posture.
- **Q7 — Role-scoped credentials. Decided: backlog-bound, not review-bound.**
  Fine-grained PATs per role (implementation agents push branches; merge
  rights stay elsewhere). One line in `BACKLOG-v2.md` when this list is
  processed, alongside `bin/dispatch` and `bin/state`. Not part of the doc
  review's working scope; out of mind until deliberately pulled.

---

*More expected. This list grows before it shrinks.*
