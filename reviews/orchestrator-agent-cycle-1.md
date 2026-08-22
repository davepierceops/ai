# Review: roles/orchestrator-agent.md — cycle 1

Verdict: changes-required
Reviewed: `roles/orchestrator-agent.md` @ `ed926db`
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (66 lines) against `docs/global-context/review-rubric.md` @ `ed926db`, all ten criteria, criterion 10 answered first. Because the file is `status: superseded` and retires this pass, the review's working question is narrower than a full gate: for each obligation the file states, does it survive somewhere else, and if not, where is its home. Criterion 4 judged against the current text of `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md`, all @ `ed926db`.
Cross-checked: `roles/chief-of-staff.md` §Decomposition and handoff, §Dispatching a package, §Constraints (the named successor, line by line against this file's Responsibilities, Required outputs, Dave's role, Constraints, and Non-goals); `docs/global-context/core.md` §Vocabulary (Directive, Directive file, Instruction, Companion document, Execution block) and the three-layer paragraph; `LEXICON.md` §Retired terms (Prompt, Dispatch, Sync block, Track) and §Spec state (Tranche); `operating-model.md` §Responsibilities, §Change flow, §Change package; `docs/global-context/decision-layer.md`; `skills/directive-dispatch.md` (Purpose and the three requirements, as the candidate home for the residue); `policies/document-metadata-policy.md` §Conditional fields (`superseded-by:`) and §Scope; `reviews/chief-of-staff-cycle-4.md` (the standing reason this file was left unconformed).
Not inspected: `skills/directive-dispatch.md` against its own rubric criteria — it is a later cycle and the baton records it as due for a rename and rewrite, so it is read here only to establish whether the residue in O2 already lands there; `MANIFEST.md:134,149,154`, `docs/packages/package-b-migration-plan.md`, `docs/packages/package-b-spec.md`, and `OPEN-ITEMS.md`, all of which name this file or the `orchestrator-agent` audience value — they are outside this cycle's scope and their repointing is not reported here; whether `bin/bundle --list` currently emits `orchestrator-agent` — no generator run was performed, and the claim in O4 rests on the frontmatter alone.
Findings: 5 — 2 blocking, 2 non-blocking, 1 observation
Dave should inspect: O2. It is the only thing in this file that dies with it. Everything else the Chief of Staff already says; two lines do not, and they specify what a per-package directive must contain. If they land nowhere, the retirement quietly drops the rule that a directive carries the package's acceptance criteria and the boundaries the executor must not cross.

## Criterion 10, first and explicitly

**retire.**

The file is already `status: superseded` with `superseded-by:
roles/chief-of-staff.md`, and the directive for this cycle settles that it
retires now. The question this review answers is not whether, but what is lost.

Obligation by obligation, against `roles/chief-of-staff.md` @ `ed926db`:

| This file | Survives in |
| --- | --- |
| `:25` read the agreed PRD and TRD | `chief-of-staff.md:92-93` ("Read the agreed PRD and TRD in full") |
| `:26-27` identify discrete change packages — the smallest independently executable units | `chief-of-staff.md:96-97` ("smallest independently executable units, in dependency order") |
| `:28` sequence the packages in dependency order | `chief-of-staff.md:96-97` |
| `:29` surface cross-package dependencies or sequencing constraints | `chief-of-staff.md:100-102` (the decomposition doc carries "sequencing rationale, dependency map") |
| `:31` which context files to load | **obsolete** — bundle composition; `audience:` selects what an agent receives |
| `:32` which role(s) to invoke | **obsolete** — same; the role slug *is* the audience value |
| `:33` acceptance criteria the package must satisfy | **nowhere** — see O2 |
| `:34` boundaries the agent must not cross | **nowhere** — see O2 |
| `:35-36` flag spec ambiguity that would force an agent to decide rather than escalate | `chief-of-staff.md:98-99`, near-verbatim |
| `:40` ordered list with sequencing rationale | `chief-of-staff.md:100-102` |
| `:42` dependency map | `chief-of-staff.md:100-102` |
| `:43` spec ambiguities flagged for Dave | `chief-of-staff.md:100-102` ("flagged ambiguities and resolutions") |
| `:47-49` Dave approves before work begins; may reorder, merge, split, drop | `chief-of-staff.md:103-104`, near-verbatim |
| `:53` operates in chat only; does not execute | `core.md` §Vocabulary (decision session); `operating-model.md` §Responsibilities ("It operates as a decision session, not an execution session") |
| `:54` does not modify spec documents | `chief-of-staff.md:150-151` |
| `:55-56` does not make architecture decisions; escalates | `chief-of-staff.md:152-153`, near-verbatim |
| `:57-58` prompts it produces are drafts; Dave owns the final one | `core.md:15` rule 2; `chief-of-staff.md:46-47`, `:149` |
| `:62-66` Non-goals (execute, review or test, assess risk, agree) | `chief-of-staff.md:152-153` |

Two lines survive nowhere. Everything else is either carried by the successor,
carried by Core or the operating model, or made obsolete by bundle composition.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — `:31-32` instruct the agent to choose which context files to load, which is what the bundle compiler now does; the rule presumes a reader who can open the repository |
| 2 | `audience:` is the selector | fail — O4; `[orchestrator-agent, human]` keeps a retired role as a live, compilable audience value |
| 3 | No references to other files by path | pass — the file cites no path in its body; `superseded-by:` at `:5` is a required conditional field, not a body reference |
| 4 | Core states it → remove it here | fail — O3; and `:53`, `:57-58`, `:62-66` restate Core and the operating model |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | pass — the file states lists and stops; it is the cleanest of the five on this criterion |
| 7 | Session kind is explicit | fail — O3; `:12` and `:53` say "in chat" and "not inside a Claude Code session", which is the vendor-shaped form of the distinction Core states as decision session / execution session |
| 8 | Tiers, not model names; route and model, not track | fail — O3; six uses of the retired *prompt* and seven vendor tokens in 66 lines, the densest concentration in this cycle |
| 9 | Filenames `<descriptor>-<timestamp>` | not applicable — the file prescribes no filename |
| 10 | Earns its place | fail — retire, see above |

## O1 — blocking
Claim: Every obligation in the file except two is already carried by `roles/chief-of-staff.md`, Core, or the operating model, so the file contributes nothing to any bundle.
Location: `roles/orchestrator-agent.md:10-66` (the whole body)
Evidence: Verified by running and by reading. The line-by-line mapping is the table above, established by reading both files whole at `ed926db`. Two pairs are near-verbatim: `:35-36` "flag any ambiguity in the spec that would require an agent to decide rather than escalate — resolve with Dave before handing off" against `chief-of-staff.md:98-99` "Flag any spec ambiguity that would force an agent to decide rather than escalate; resolve with Dave first"; and `:48` "Dave may reorder, merge, split, or drop packages" against `chief-of-staff.md:104` "he may reorder, merge, split, or drop." `grep -n "superseded" roles/orchestrator-agent.md` confirms `status: superseded` at `:2` and `superseded-by: roles/chief-of-staff.md` at `:5`, so the supersession is already recorded in frontmatter; what has not happened is the deletion.
Consequence: Criterion 10. While the file remains in the tree with a valid `audience:` value, a bundle for `orchestrator-agent` still compiles (O4), and what it compiles is a second, older, vendor-worded specification of the Chief of Staff's decomposition job — including two rules the successor deliberately dropped (`:31-32`, obsoleted by bundle composition). An agent receiving it would be told to choose its own context files, which is the one thing a bundle-compiled agent structurally cannot do.
Fix: `git rm roles/orchestrator-agent.md`. Before that commit lands, resolve O2 and O5.
Related: O2, O4, O5

## O2 — blocking
Claim: Two lines specify what a per-package directive must contain, and neither `roles/chief-of-staff.md` nor Core nor `skills/directive-dispatch.md` states them; they die with the file.
Location: `roles/orchestrator-agent.md:33-34`
Evidence: Verified by running. The two lines are "- acceptance criteria the package must satisfy" and "- boundaries the agent must not cross", both sub-items of `:30`. Searched for each obligation in the successor and the foundation: `chief-of-staff.md:142-145` is the whole of what it says about handing a package over — "A package is dispatched per `skills/directive-dispatch.md`, and the decomposition doc — not the spec — is the source the directive derives from" — which names the source, not the contents. `chief-of-staff.md:116-117` mentions acceptance criteria only to exclude them: "ACs are a separate execution-time input, not part of what the decomp pins" — an acknowledgement that they arrive at execution time, with no rule that the directive carries them. `core.md` §Vocabulary defines a **Directive** as "one line stating route (fresh or existing session) and model tier, then the execution block as a paste block" and an **Instruction** as "one direction within a directive file" — structure, not required contents. `operating-model.md` §Change flow step 2 requires ACs to exist for a unit of work but says nothing about their transport. No file states that a directive must carry the boundaries the executor may not cross.
Consequence: Retiring the file drops two rules with no successor. The concrete failure: a Chief of Staff drafts a package directive that names the decomposition doc and the route and model, and omits the acceptance criteria — because nothing requires them — so the execution session builds to the package description rather than to written ACs, which is the red-gate precondition in `operating-model.md` step 4. The boundaries line is the sharper loss: it is the only statement anywhere that a directive must tell the executor what it may not do, and the operating model's Escalation section covers when to escalate, not what is out of bounds.
Fix: Carry both lines into `skills/directive-dispatch.md` as required contents of a package directive, phrased as instructions: "A package directive states the acceptance criteria the package must satisfy, and the boundaries the execution session must not cross." That file owns the directive's shape, which is the same division A2 settled for review artifacts — the skill owns the artifact's shape, the role states what it decides. `skills/directive-dispatch.md` is not in this cycle's scope, so this is named as a dependency of the retirement, not as a finding against that file. If Dave prefers the rule to sit with the drafter rather than the transport, the alternative home is `roles/chief-of-staff.md:142-145`.
Related: O1

## O3 — non-blocking
Claim: Six uses of the retired term *prompt*, seven vendor tokens, and the session-kind distinction stated in vendor terms.
Location: `roles/orchestrator-agent.md:11`, `:12`, `:30`, `:41`, `:47`, `:49`, `:57`, `:58`, `:63`
Evidence: Verified by running. `grep -on 'prompts\?' roles/orchestrator-agent.md` returns six hits: `:11`, `:30`, `:41`, `:49`, and `:57` (×2). `grep -on 'Claude Code' roles/orchestrator-agent.md` returns seven: `:11`, `:12`, `:30`, `:41`, `:47`, `:58`, `:63`. `LEXICON.md` §Retired terms routes *prompt* to its replacements, and the sense used here — "the Claude Code prompt for each package" — is the first one listed: "**What a decision session hands an execution session** — a *directive*." `core.md` states the layers as "**decision** — chat; **execution** — an LLM agent session; **shell**", against `:12` "in chat, not inside a Claude Code session" and `:53` "operates in chat only".
Consequence: Criteria 4, 7, and 8. `reviews/chief-of-staff-cycle-4.md` already recorded this cluster and the reason it was left alone: "a frozen document is a record of what a superseded role said, and conforming it would make it a worse record without making anything truer… it is the largest unconformed cluster left in `roles/`, and a later sweep should find the reason rather than re-derive it." That reasoning holds and this finding does not overturn it — the count is recorded because the directive asks for it, and because deletion resolves it more completely than conformance would.
Fix: None as edits. The retirement removes all thirteen tokens. Do not conform the file first; that would produce a status-transition-plus-content-edit commit on a document about to be deleted.
Related: O1

## O4 — non-blocking
Claim: `audience: [orchestrator-agent, human]` keeps a retired role as a live audience value.
Location: `roles/orchestrator-agent.md:4`
Evidence: Verified by reading `policies/document-metadata-policy.md:91-93`: "`audience:` list of roles that consume this document. Values are `roles/` file slugs plus two reserved values: `all-roles` and `human`." `orchestrator-agent` is a `roles/` file slug for exactly as long as `roles/orchestrator-agent.md` exists. The baton records that "`bin/bundle --list` emits every audience value in use." This file is the only one in the tree that still carries the value: `grep -rn "orchestrator-agent" --include='*.md' .` returns it in frontmatter here, in `roles/chief-of-staff.md:10` as a path (O5), and otherwise only in `docs/`, `reviews/`, and `MANIFEST.md`, all outside this cycle's scope.
Consequence: Criterion 2. A retired role remains selectable — an operator running the generator for `orchestrator-agent` gets a bundle, and the bundle is the superseded document (O1). The audience list is meant to be the inventory of who can receive context, and it currently lists a role that no longer exists.
Fix: Subsumed by O1 — deleting the file removes the slug, and the value ceases to be valid by the metadata policy's own definition.
Related: O1

## O5 — observation
Claim: `roles/chief-of-staff.md:9-10` cites this file by path, so deleting it without editing that line leaves the successor citing a deleted path.
Location: `roles/orchestrator-agent.md` — whole file; the external reference is `roles/chief-of-staff.md:9-10`
Evidence: Verified by running. `grep -n "orchestrator-agent" roles/chief-of-staff.md` returns `:10`: "`roles/orchestrator-agent.md` is `superseded` and frozen," preceded at `:9` by "Supersedes the Orchestrator Agent (Q3c)". `roles/chief-of-staff.md` is `status: agreed`, so an edit to it carries the revision-lifecycle consequence recorded as C11 in `reviews/chief-of-staff-cycle-5.md`.
Consequence: Core rule 13 — a changed fact changes everywhere it appears. The successor's opening sentence explains its own provenance by pointing at a file that will not exist, and the sentence is not merely stale but self-defeating: its content is "the other file is frozen," which is meaningless once the other file is gone. This is recorded as an observation against this file because the edit belongs to `roles/chief-of-staff.md`, where it is finding C10, not here.
Fix: In the same change package as the deletion, replace `roles/chief-of-staff.md:9-10` with "Short form: **`cos`**." and nothing further. Files outside this cycle's scope that also name this path are known and deliberately not reported here.
Related: O1
