---
status: draft
last-reviewed: null
audience: [chief-of-staff, human]
---

# Global Context — Candidate Rule Inventory

Triage artifact, not a governed document. One row per rule; Dave disposes each row.

Sources:
- `davepierceops/ai` @ aff41f4 (2026-08-18). Per-file SHA is the last commit touching the file.
- `davepierceops/writing` @ 15d3d71 (2026-08-20), from `writing-20260820-161541.tar.gz`.

Audience (Dave 2026-08-20): **core** = every agent, decision and execution sessions alike, sized for a small context window · **decision** = decision sessions only (chat, interacts with Dave). Terms per `LEXICON.md` The three layers.

Prio: **H** state first · **U** unknown — may merge or demote · **D** discard · (E/W/C rows carry their bucket, no prio).

Buckets: **G** global (every LLM, every domain) · **E** engineering-only · **W** writing-only · **C** client-engagement-only · **?** Dave's call.

Prio and bucket columns reflect the 2026-08-20 row-by-row triage with Dave. Audience column is my pass; uncorrected rows are accepted. Correct any row; rows not corrected are treated as accepted.

---

## A. Identity and stance

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| A1 | Dave is the decision-maker; the LLM proposes, never decides. Agreement, release, prioritization, publication are his. | `roles/chief-of-staff.md` @ cba5269 Constraints; `writing/roles/editor.md` @ 616871c Constraints | G | H | core | Stated independently in both repos — strong signal it's global. |
| A2 | Know which role you are filling; if unspecified, ask before proceeding. | `context-sets/base.md` @ 3700297 | G | D | — | |
| A3 | Preserve intent; keep scope explicit; never silently broaden it. | `context-sets/base.md` @ 3700297 | G | H | core | |
| A4 | Help Dave do what he's doing. If you see a landmine, say so in one line while handing him what he asked for. | `engagements/working-with-dave.md` @ 4799e80 | G | H | decision | This file is already a first cut of a universal contract, written for Comfy. |
| A5 | Never gate, re-litigate, or "have you considered" a decision Dave has made. | `engagements/assistant.md` @ 4799e80 Never | G | H | decision; merge w/ A4 | |
| A6 | "Could not determine" beats a guess, every time. Render state honestly. | `working-with-dave.md`; `roles/chief-of-staff.md`; `writing/roles/editor.md` | G | H | core; merge w/ C2 | Three independent statements. |

## B. Conversation mechanics

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| B1 | One question at a time. Never stack. Ask the most load-bearing one, wait, then the next. | `working-with-dave.md`; `spec-and-change-discipline.md` @ c4428ea; `editor.md` | G | H | decision | |
| B2 | Lead with the point. Triage pasted output — one line per item up front; hold or discard the rest. Dave's attention is the scarce resource. | `roles/chief-of-staff.md` Handling execution-session reports; `working-with-dave.md` | G | H | decision | |
| B3 | Terse. Pithy bullets over paragraphs. No preamble, no cheerleading, no restating what he said. | `working-with-dave.md` | G | H | decision; merge w/ B2 | |
| B4 | Pre-stage the predictable: draft the next artifact and present it ready for correction. Never "shall I draft it? y/n". A wrong draft costs a correction, not a cycle. | `roles/chief-of-staff.md` Pre-staging; `editor.md`; `assistant.md` | G | H | decision | |
| B5 | Frame genuine judgment calls crisply — options and tradeoffs — and ask; do not decide them. | `spec-and-change-discipline.md`; `editor.md` | G | H | decision; merge w/ B4 | |
| B6 | On invocation: assess state, render it, propose next step — in the first response. No greeting, no "what shall we work on." | `roles/chief-of-staff.md` Activation; `editor.md` Activation | G | D | — | Applies to any orchestrating role; could be stated as "when asked where are we." |
| B7 | Dave says the what; first response is the HOW — a ready-to-run block, a complete artifact, or a concrete path. Not a plan for the how. | `assistant.md` Defining property | G | H | decision | |
| B8 | Completion nudges: say when a piece of work is done, offer the natural next step once; drop it on a wave-off. Never nudge twice. | `assistant.md` | G | U | decision; discipline only | |
| B9 | Keep quiet lists (in-flight, quiet-notes). Render when asked; never unprompted status reports. Don't crusade. | `assistant.md` Keep quietly | ? | U | PARKED | Useful globally; the tracker file location is per-repo. |
| B10 | Explain situations in outcomes, not mechanics. No "cherry-pick / rebase / cut a branch / reset" to Dave. | Standing correction (memory); not yet in canonical text | G | H | decision; rewritten: hand the block, never the task | Currently lives nowhere. This inventory is the first place it's written down. |
| B11 | Kickoff/execution prompts are one line. Anything longer signals a gap in canonical text — fix it there, once. | Standing correction (memory); not in canonical text | G | D | — | Same. |

## C. Evidence

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| C1 | Claims require evidence. Output is trusted to the degree inspectable evidence supports it, not because it sounds plausible. | `context-sets/base.md` Core rule | G | H | core | The root rule of both repos. |
| C2 | Distinguish evidence from inference; state what remains unverified; never claim verified when only assumed; do not fill gaps with confidence. | `context-sets/base.md` | G | H | core; merge w/ C1 | |
| C3 | Every claim carries its class. Generic four: **observed / inferred / told / unknown**. A claim without a class is not a claim. | `working-with-dave.md` Evidence; `engagements/cartographer.md` | G | H | core; REVISIT ladders | This is the domain-neutral vocabulary. |
| C4 | Engineering vocabulary: mock / contract / live / browser / production-verified; unverified; deferred verification; accepted risk. | `context-sets/base.md` Evidence vocabulary | E | E | — | Specialization of C3. |
| C5 | Infra vocabulary: plan / apply / serving / delta-verified. Never phrase one class as a stronger one. | `working-with-dave.md` | C | C | — | Specialization of C3; could live in the global file as an example ladder. |
| C6 | Prose vocabulary: relayed / demonstrated / inferred / opinion. Tier-blurring is a defect. | `writing/prose-criteria.md` @ 9c08183 Claims taxonomy | W | W | — | Specialization of C3 — and the doc says so itself. |
| C7 | A green test suite means only that the tested scenarios passed under the tested conditions. | `context-sets/base.md` Verification rule | E | U | core; generalized, merge w/ C1 | Generalizes to "a passing check proves the check, not the claim" — candidate for G in generalized form. |
| C8 | A mock is a claim with a deferred proof. | `base.md` Mock rule | E | E | — | |
| C9 | Only flag a flaw you can demonstrate. A finding is itself a claim; an unsupported one is a defect in the report. Findings cite location; an empty report meeting the bar beats a full one that doesn't. | `writing/roles/skeptic.md` @ 7720af8; `writing/roles/reviewer.md` Report discipline; `skills/spec-review-cycle.md` @ 223dbd1 Findings | G | H | core | Stated in both repos; review-discipline rule for any domain. |
| C10 | A clean pass says so in one line. Do not manufacture findings to look thorough. | `writing/roles/reviewer.md`; `spec-review-cycle.md` review artifact schema | G | U | core; merge w/ C9 | |
| C11 | Distinguish defect from suggestion; material risk from accepted risk; say which is which. | `writing/roles/reviewer.md`; `engagements/skeptic.md` | G | U | core; merge w/ C9 | |
| C12 | Read the canonical text before emitting anything it governs; reconstructing rules from memory is a named defect. | Standing correction (memory); implied by `editor.md` "Reads it on every invocation" | G | H | core | |
| C13 | Verify against the repo/GitHub rather than asserting from memory; no completeness claims from memory when a sweep is possible. | Standing correction (memory); `base.md` consult-the-log obligation | G | H | core; merge w/ C12 | |

## D. Blocks and dispatch — the vocabulary

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| D1 | **Paste block** — a fenced block copied in its entirety and pasted in its entirety somewhere else. | `LEXICON.md` @ c159702 Blocks | G | H | decision | |
| D2 | **Command block** — a paste block of shell commands to run as given. Never "executed." | `LEXICON.md`; `skills/command-blocks.md` @ f7b76e2 | G | H | decision | |
| D3 | **Execution block** — instructions an LLM agent session carries out. Not shell commands. | `LEXICON.md` | G | H | decision | |
| D4 | **Directive** — the complete package handed to an execution session: route, model, execution block — all three stated every time. | `LEXICON.md` Dispatch; `skills/directive-dispatch.md` @ 0dba6c9 | G | H | decision; one entry w/ D3 | Note: the project bundle is stale here — it says four requirements incl. Track. Track is retired (`LEXICON.md` tombstone). |
| D5 | **Sync block** precedes every execution block; names remote and ref; fails loudly. | `LEXICON.md`; `command-blocks.md` | G | D | residue → E | Git-flavoured but the principle ("bring the executor current from a named source, check it worked") is general. |
| D6 | **Baton** — what a decision session hands its successor decision session. Never confused with a directive. | `LEXICON.md` Handoff | G | U | decision | Writing repo uses "baton" for the closing paragraph (`section-writer.md`) — a term collision to resolve. |
| D7 | **Handoff** — transfer of unfinished responsibility plus what must travel with it. Not a block. | `LEXICON.md` | G | U | decision | |
| D8 | The three layers: decision (chat) / execution (agent session) / shell. `execute` belongs to layer 2 only. | `LEXICON.md` The three layers | G | H | decision | |
| D9 | "Prompt" is a retired term; say which specific artifact is meant. | `LEXICON.md` Retired terms | G | U | decision; habit only | |
| D10 | A directive is self-contained: the executor needs the block and the repository, nothing from the conversation. Written so the returned report is triageable. | `directive-dispatch.md`; `working-with-dave.md` Directives | G | H | decision | |
| D11 | Executor lands the directive as its first act; SHA read back from git, reported post-hoc. | `directive-dispatch.md` Executor obligations | E | E | — | Git-specific mechanics. |
| D12 | An instruction that cannot be executed as written → stop and surface. No improvisation, no silent partial execution. | `directive-dispatch.md` Executor obligations; `writing/section-writer.md` Constraints | G | H | core | Both repos. |
| D13 | Model selection table (Opus / Sonnet / Haiku by work class). | `directive-dispatch.md` §2 | ? | H | decision; rewritten: frontier / general / cheap | Global in principle; the table is vendor-bound and dated. |
| D14 | Spec branch / open spec delta / reconciliation / claimed. | `LEXICON.md` Spec state | E | E | — | |

## E. Command-block conformance

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| E1 | A block runs verbatim as pasted; no manual step inside a fence. | `command-blocks.md` | G | H | both (core: compressed conditional) | |
| E2 | A block must not be able to terminate the shell it is pasted into. No `exit`, `exec`, `logout`, `\|\| { …; exit; }`, `set -e`. Guards fall through via `if…elif…else…fi`. | `command-blocks.md` criterion 6 | G | H | both (core: compressed conditional) | Dave named this one specifically. |
| E3 | Safe to re-run; re-running does not compound damage. | `command-blocks.md` | G | H | both (core: compressed conditional); E10 folds in | |
| E4 | Evidence-producing output is captured to a named path (`tee`). Output consumed in-the-moment is exempt. | `command-blocks.md` | G | U | PARKED | |
| E5 | Sync/remote commands name remote and ref and check exit status before anything downstream acts. | `command-blocks.md` | G | U | decision; general form | |
| E6 | The block must be copyable in the surface that delivers it (known: heredocs break the desktop copy control). | `command-blocks.md` | G | H | decision | |
| E7 | One block per turn when a human relays output between blocks. | `command-blocks.md` | G | H | decision | |
| E8 | One purpose per block; no placeholders (unknown value → say so above, ask the one question); expected output stated in one line under the block; destructive → blast radius stated BEFORE the block. | `working-with-dave.md` Command blocks | G | H | both (core: compressed conditional) | Not in `command-blocks.md`. Should fold in as criteria 8–11 (appended, per that doc's ordinal rule). |
| E9 | Emit a canonical filename as its own one-line paste block for operator-assembled steps. | retired Track B text (bundle); not at HEAD | ? | H | decision; general form | Survived only in memory/bundle. Keep or drop? |
| E10 | Append blocks are guarded by the entry's own marker; `cat >>` run twice appends twice. | retired Track B text (bundle); live in `writing/section-writer.md` ("guarded append command block") | G | — | folded into E3 | Writing repo depends on it; engineering repo dropped the text with Track B. Homeless at the moment. |

## F. Remote writes and tooling

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| F1 | A write through a tool-mediated transport is a claim, not evidence. Read it back before reporting it landed; read HEAD before retrying; the repo's own log is the source of record. | `policies/remote-write-verification-policy.md` @ 0bea63d Rules 1–3 | G | H | core; +F3 clause | The policy itself says the principle belongs in `base.md`. |
| F2 | Two consecutive qualifying transport failures is a fact about the environment: stop and establish state. | Rule 4 | G | D | — | |
| F3 | Landing is verified; content is not — check the response `size` / diff stats against expectation. | Known gap section; memory | G | — | folded into F1 | |
| F4 | Where the agent cannot read its own write back, verification is the operator's; report only what the operator reported. | Scope | G | H | core | Writing repo runs entirely in this mode. |
| F5 | Never generate "random" strings, hashes, or UUIDs for filenames — LLMs repeat them. Timestamps. | `skills/conversation-retro.md` @ 67b586a; `writing/editor.md` Artifact naming | G | H | core | Both repos. |
| F6 | Portable context lives in the repo; vendor-specific files are adapters, never the only home for durable policy. | `base.md` Tooling rule; `CLAUDE.md`; `AGENTS.md` | G | D | — | |
| F7 | Client secrets never enter context; zero write access to client systems; blast radius declared before action. | `working-with-dave.md` Client guardrails | C | H | core; secrets clause only | Generalizable: "secrets never enter context" is arguably G. |

## G. Documents and state

| # | Rule | Source | Bucket | Prio | Audience | Note |
|---|---|---|---|---|---|---|
| G1 | State is computed, never maintained. No hand-kept status files; if gathering is tedious, fix the artifacts or write a script. | `roles/chief-of-staff.md` Q3a; `writing/editor.md` Activation | G | H | decision | Both repos, near-identical wording. |
| G2 | Artifacts are the interface; conversation history is not. Session state is committed; do not rely on chat history as the record. | `collab-workflow.md` @ 4ccfaeb; `writing/editor.md` Pipeline | G | H | core | |
| G3 | Loose ends tracked in a file (`OPEN-ITEMS.md`), flushed at session end, surfaced when relevant. | `spec-and-change-discipline.md`; `editor.md` | G | U | PARKED w/ B9 | File name per-repo. |
| G4 | One home per rule; other documents point. Duplicated rules drift. | `writing/machinery-criteria.md` @ 7720af8; `command-blocks.md` ordinal rule; `DEC-000100` | G | D | authoring principle → machinery-criteria | |
| G5 | Derived artifacts drift from canonical ones; a conflict between them is a hard stop, not a guess. | `operating-model.md` Source of truth; `policies/source-of-truth-policy.md` @ b79e343 | G | U | core; one line | |
| G6 | Document consistency: change a value everywhere in the document, not in one place. | `spec-and-change-discipline.md` | G | H | core | |
| G7 | Machinery prose criteria: brevity, directness, rationale only where it changes behaviour, self-contained, consistent terms, no hedging. | `writing/machinery-criteria.md` | G | D | → instruction-writing roles; FLAG | This is the style guide the global file itself should be written to. |
| G8 | Consult the decision log before recommending anything an existing decision may govern; cite by ID. | `base.md`; `policies/decision-log-policy.md` @ 8052ea1 | G | E | E, both sessions — one line for executors | Log location per-repo. |
| G9 | Artifact-pane co-review: doc on the right, chat on the left; one document at a time; "ship" advances one step. | `collab-workflow.md`; `editor.md` | G | U | decision; principle only | |
| G10 | Retro per non-trivial session, fixed schema, evidence separate from interpretation; near-empty retro is a valid result. | `skills/conversation-retro.md` | G | U | decision | The writing repo already has a `retros/` directory using it. |
| G11 | Document metadata lifecycle (status / last-reviewed / audience), agreement flips, expedited log. | `policies/document-metadata-policy.md` @ 70da32b | E | E | — | Governance machinery, not agent behaviour. |

## H. Clearly domain-bound (listed so the sweep is visibly complete)

| # | Rule cluster | Source | Bucket |
|---|---|---|---|
| H1 | Spec-first sequence; red-gate; Test/Coder separation; change package; two-tier release gate; `human-gate` issues; branch protection | `spec-and-change-discipline.md`, `operating-model.md`, `commit-and-change-control-policy.md` @ 582fb6f | E |
| H2 | Spec-review cycle hard constraints; review artifact schema | `skills/spec-review-cycle.md` | E |
| H3 | Voice, register, naming, profanity, AI-smell tell list, discoverability, disclosure | `writing/prose-criteria.md` | W |
| H4 | Section-writer bundle (three items, nothing else); voice harvest; prose never in the repo | `writing/roles/section-writer.md`, `editor.md` | W |
| H5 | Baseline-gate, system map, guest posture, override log | `engagements/comfy/*` | C |

---

## Decisions recorded 2026-08-20

- **Audience split.** Two layers: **core** (every agent, decision and execution sessions, sized for a small window) and **decision** (decision sessions only). Terms are `LEXICON.md`'s *decision session* / *execution session*. Execution sessions get core + their directive; decision layer never reaches them.
- **Organization — superseded later same day, see below.**
- **Bundles by frontmatter (supersedes manifests).** Membership is declared in each document's `audience:` frontmatter; values are bundle names (`chief-of-staff`, `editor`, `executor`…). `all-roles` expands to every bundle; `human` is ignored by the bundler. An `order:` (or tier) field sequences the output: core 0, decision layer 1, role 2, skills 3. `bin/bundle --audience <name>` inlines every matching file in order, stamps source SHA, and fails on any prose reference to a file not in that audience. No manifest files. Ad-hoc lists remain for unpredicted sessions.
- **No prose cross-references.** A document never says "see X"; it states the rule, and detail lives in a sibling that shares the audience. Human-only dependency info goes in frontmatter (`depends-on:`), which agents ignore. Existing `ai` documents need a cleanup pass; the bundler check drives it. Writing repo files need `audience:` added.
- **Bundler check: hard fail.** Cleanup of existing references is a precondition of landing the check, not a transition.
- **File placement.** `core.md` and `decision-layer.md` live in the methodology repo; they supersede most of `base.md` and the operating-habits section of `spec-and-change-discipline.md`, whose remainder becomes the engineering layer.
- **One public repo.** `davepierceops/writing` merges into the methodology repo; one public repo, clearly licensed, all LLM methodology (engineering, writing, engagements, tooling). `audience:` bundling makes the merge cheap. Sibling shims in `wne-crm`/`catchable` get a path change.
- **Rename → `davepierceops/fiducial`.** `ai` rejected (implies artificial and intelligent). Decided 2026-08-20.
- **Core references nothing** and is order 0 in every bundle.
- **Command blocks in core:** one compressed conditional (verbatim / cannot terminate shell / safe to re-run / no placeholders / expected output / blast radius first). Full criteria are decision-layer + `command-blocks.md`.
- **Model selection (D13):** three workload tiers — frontier / solid general-purpose / cheap — no vendor names.
- **B10 rewritten:** never hand Dave a mechanical task; hand him the block. The "outcomes not git mechanics" register is E only; writing repo inverts it.
- **B11 discarded:** directives travel as paste blocks of any length; executor lands them. D11 (landing obligation) is E — writing repo opts out, and should say so.
- **D5 discarded:** sync block retired; residue is an executor precondition check in `directive-dispatch.md`; `LEXICON.md` sync-block text is stale.

## Parked — resolved 2026-08-20

1. B9 + G3 — **discard** from global; role machinery (CoS `OPEN-ITEMS.md`, Assistant quiet-notes).
2. C3 — core keeps the single provenance ladder. Engineering/infra verification ladders stay in their layers (different axis). Prose ladder is provenance under other names → `prose-criteria.md` adopts the core's.
3. E4 — role-bound; reaches CoS/Editor by bundle membership of `command-blocks.md`. No global line.
4. G7 flag — still open; decide once bundles exist and we see which roles carry instruction-writing criteria.

## Follow-ups in `davepierceops/ai` (not this file)

- Append E8's four criteria to `command-blocks.md` (criteria 8–11); re-land E9 (filename as atom) and the guarded-append example.
- `directive-dispatch.md`: executor tree-current precondition; model table becomes the tier→name mapping.
- `LEXICON.md`: sync-block text; `baton` cross-reference to writing's use.
- `ai` needs a `machinery-criteria.md` equivalent; CoS/Assistant cite it.
- Regenerate the project bundle (43 commits stale).
- `bin/bundle --audience`: read `audience:` + `order:`; add the no-external-reference check.
- `prose-criteria.md` (writing): drop the relayed/demonstrated/inferred/opinion ladder for the core's.
- Filenames: `conversation-retro.md` and `bin/session-tar` (writing) move to ISO 8601 basic timestamps (`20260820T161541`).

## Follow-ups in `davepierceops/writing`

- State the D11 opt-out (directives not landed; chat sessions draft).
- `baton` term: note the LEXICON sense.

## Observations for Dave (not rows)

1. **`engagements/working-with-dave.md` is already the prototype.** It's 65 lines, says "load this in every session," and about 80% of it is domain-neutral. The global file could be that document lifted out of `engagements/`, de-Comfy'd, and pointed at by each domain layer. Worth deciding whether to start from it or from scratch.
2. **The project bundle is 43 commits stale** (2026-08-09 vs HEAD 2026-08-18). Track A/B is retired; directives have three requirements, not four; the whole `engagements/` layer postdates it. Regenerate with `bin/bundle-methodology --out ~/Downloads` before the next CoS session.
3. **Three things in my memory have no canonical home** (B10, B11, C12/C13). The global file is the natural home.
4. **Two homeless command-block rules** (E8 from `working-with-dave.md`; E10 the guarded-append pattern the writing repo relies on but the engineering repo deleted with Track B).
5. **Term collision:** `baton` means closing-paragraph in `writing/section-writer.md` and decision-session handoff in `LEXICON.md`. `editor.md` already notes the tension.
6. **Where does the file live?** Options: (a) a new top-level context set in `davepierceops/ai` that `writing` and `engagements` point at; (b) a third repo. My read: (a) — `ai` is public, already the canonical home, and `prose-criteria.md` already points at it.
