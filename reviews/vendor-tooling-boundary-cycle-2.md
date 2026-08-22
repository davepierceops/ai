# Review: boundaries/vendor-tooling-boundary.md — cycle 2

Verdict: changes-required
Disposition (criterion 10): **retain-with-changes** — on a narrow margin; see below
Reviewed: `boundaries/vendor-tooling-boundary.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11b)
Date: 2026-08-21
Scope: the whole document, all ten rubric criteria, judged as a bundle member. Cycle 1 was scoped to a single word and explicitly did not open a full gate (`reviews/vendor-tooling-boundary-cycle-1.md`, Not inspected); this is the first full gate over the file. Criterion 4 judged against `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md` at the same SHA. Criterion 10 judged by computing the reference closure with `bin/bundle` from all six context-set entry points and reading every closure member that states the portable/adapter rule.
Cross-checked: `operating-model.md`, `context-sets/base.md`, `policies/source-of-truth-policy.md`, `vendors/README.md`, `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `docs/global-context/review-rubric.md`, `policies/document-metadata-policy.md`, `AGENTS.md`, `CLAUDE.md`, `reviews/vendor-tooling-boundary-cycle-1.md`
Not inspected: `vendors/claude-code/` and `.claude/**` were not read, so the §Examples bullets were checked for path shape and vendor naming only — whether `.claude/agents/` and `.claude/skills/` still hold what line 24-25 says they hold is unverified. `roles/**`, `skills/**`, `specs/`, `engagements/`, `bin/` other than `bin/bundle`, and `docs/research/methodology-scan-phase2-findings.md` beyond the four lines that cite this file. No adopting project or second vendor was exercised, so the swap-the-vendor test at `vendors/README.md:31-32` was applied by reading, not by running. Whether the five-step discipline is followed in practice is not evidenced anywhere in the repo and was not checked.
Findings: 4 blocking, 2 non-blocking, 1 observation
Prior cycle: `reviews/vendor-tooling-boundary-cycle-1.md`
Dave should inspect: the criterion-10 call. Taking B1 through B3 deletes four of the file's six sections, leaving the five-step §Required discipline and little else. That is enough to earn a place under criterion 10, but it is close — and `policies/source-of-truth-policy.md:25-28` already carries the rule and already points here, so merge-into that policy is a defensible alternative if you would rather hold fewer files.

## Criterion pass

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — B2 |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`, both reserved values (`policies/document-metadata-policy.md:95-96`); no `order:` needed |
| 3 | No references to other files by path | fail — B2 (6 path-shaped references) |
| 4 | Core states it → remove it here | fail — B1 (3 restated rules across 2 sections) |
| 5 | Agent instruction, not authoring principle | pass — §Required discipline is addressed to the agent creating the artifact |
| 6 | Instructions, not rationale | fail — B3, N1 |
| 7 | Session kind is explicit | fail — B4 |
| 8 | Tiers, not model names; route and model, not track | fail — N2 (3 vendor names, 7 occurrences over 5 lines; 0 model names, 0 retired terms) |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the filenames named are stated conventions (`CLAUDE.md`, `AGENTS.md`), which criterion 9 permits |
| 10 | The file earns its place or is retired | **retain-with-changes** — see below |

## Criterion 10 — retain-with-changes

It lands in a bundle. **Verified by running** `python3 bin/bundle <entry> --format list` for all six context-set entry points: the file appears in all six closures. It is reached from a governing document — `policies/source-of-truth-policy.md:28` cites it by path — and not only from scratch, which distinguishes it from `boundaries/live-integration-boundaries.md` and `boundaries/mocked-boundaries.md`.

Its **rule** contributes nothing new. *"No durable operating principle should live only inside a vendor-specific tool"* is stated four further times in the same closure: `operating-model.md:201` (*"Tool-specific files may adapt these rules but should not be the sole location of durable policy"*), `operating-model.md:79` (Agents must not — *"store durable policy only in vendor-specific tooling"*), `context-sets/base.md:110-114` §Tooling rule, and `policies/source-of-truth-policy.md:25-28`. `vendors/README.md:31-32` adds the operational test (*"if swapping vendors would delete the sentence, it belongs here"*), which this file lacks.

What contributes something no other file states is the **five-step §Required discipline** at lines 40-48 — identify the portable source, keep the adapter short, add no new durable policy in the adapter, update the portable source first, note intentional deviations. **Verified by running** a grep for each step's substance across the closure: step 4, *update the portable source first*, is the sequencing rule, and it appears nowhere else; the other four state the rule as a procedure an agent follows when it is about to write an adapter, which is the form none of the four restatements take. That is a real contribution and it is why the disposition is retain rather than merge.

It is a narrow margin, and the alternative is worth stating plainly: after B1-B3, what remains is a title, one rule sentence, and five steps. `policies/source-of-truth-policy.md` already holds the portable/adapter split, is already the file that points here, and would absorb the five steps without strain. The reason to keep this file separate is that the steps are a procedure and that policy is a hierarchy of authority — different jobs. Dave decides.

## B1 — blocking
Claim: §Summary lines 13 and §Policy restate the portable/adapter rule that `operating-model.md` states twice.
Location: `boundaries/vendor-tooling-boundary.md:13`, `:17`, `:19`
Evidence: **Verified by reading** all four at `7310937`. Line 13: *"These tools are execution backends, not the source of truth."* Line 17: *"No durable operating principle should live only inside a vendor-specific tool."* Line 19: *"The portable `/ai/` documents are authoritative. Vendor-specific files are adapters."* Against `operating-model.md:199-201`: *"These portable operating documents are the source of truth for project operating guidance. Tool-specific files may adapt these rules but should not be the sole location of durable policy."* And `operating-model.md:79`, under Agents must not: *"store durable policy only in vendor-specific tooling."* Three statements here, two there, plus `context-sets/base.md:110-114` and `policies/source-of-truth-policy.md:25-28` in the same bundle — five files, seven statements of one rule.
Consequence: seven copies arrive in one bundle. Under Core rule 13 every one is a maintenance obligation, and the copies are not identical — `operating-model.md:201` says adapters *"should not"* be the sole location, this file says *"no durable operating principle should"*, and `operating-model.md:79` states it as a flat prohibition. An agent looking for whether the rule is advisory or absolute finds all three registers and no tiebreak.
Fix: cut lines 13 and 19; keep line 17 as the file's single statement of the rule, since the §Required discipline that earns the file its place has to say what it is disciplining. The two `operating-model.md` statements should be reduced to one when that file is next open, which is outside this cycle.
Related: B3, N1

## B2 — blocking
Claim: six path-shaped references, and one of them carries the rule.
Location: `boundaries/vendor-tooling-boundary.md:19` (`/ai/`), `:23` (`CLAUDE.md`), `:24` (`.claude/agents/`), `:25` (`.claude/skills/`), `:26` (`AGENTS.md`), `:27` (`/ai/`)
Evidence: **Verified by running** a grep for backticked strings over the file — six hits, listed above. Line 19 is the load-bearing one: *"The portable `/ai/` documents are authoritative"* states the rule by naming a directory, so an agent reading the bundle is told authority lives at a path it cannot see and cannot enumerate. Lines 23-27 are the §Examples list, five bullets each naming a file or directory.
Consequence: for line 19, the rule does not survive the trip into a bundle — the reader learns that something called `/ai/` is authoritative without learning what is in it, and the bundle it is holding *is* that content, unlabelled. For lines 23-27, the reader is handed five adapter locations it cannot open, so the examples teach nothing it can act on; they are also the file's entire vendor-name exposure (N2).
Fix: delete §Examples (lines 21-27) in full. Reword line 19 out of existence per B1, so the rule is carried by line 17, which names no path. Note that `policies/source-of-truth-policy.md:25-28` states the same rule and names the same paths, so the same sweep is due there.
Related: B1, N2

## B3 — blocking
Claim: §Risks is rationale — six reasons the rule exists, no instruction.
Location: `boundaries/vendor-tooling-boundary.md:29-38`
Evidence: **Verified by reading**: *"Vendor-specific tooling can create: lock-in / hidden policy drift / stale duplicated instructions / inconsistent agent behavior across tools / difficult migration to other models / unclear source of truth."* Every bullet is a consequence of violating the rule stated at line 17. Rubric criterion 6 requires that arguments for a stated rule be cut.
Consequence: ten lines of a file whose earned content is five steps are spent arguing for a rule the reader has already been given and cannot dispute. In a bundle where `operating-model.md`, `context-sets/base.md`, and `policies/source-of-truth-policy.md` all state the same rule, the argument for it is the least useful thing present.
Fix: delete lines 29-38.
Related: B1, N1

## B4 — blocking
Claim: the file does not state which session kind it is for.
Location: `boundaries/vendor-tooling-boundary.md:1-5`
Evidence: **Verified by reading** the frontmatter — `status`, `last-reviewed`, `audience`, nothing naming a session kind — against `docs/global-context/core.md:37-38` and rubric criterion 7.
Consequence: the same defect as its three siblings. Here the honest answer is both: an execution session writing an adapter follows the five steps against a working tree, and a decision session deciding where a new rule lives applies the same test. Criterion 7 permits *both*; it does not permit silence.
Fix: state it in one line under the title — this file governs both session kinds.

## N1 — non-blocking
Claim: §Core principle is an aphorism, and it introduces a fifth formulation of the source-of-truth hierarchy that does not match the one `policies/source-of-truth-policy.md` states.
Location: `boundaries/vendor-tooling-boundary.md:50-52`
Evidence: **Verified by reading** both. This file: *"Context Sets are the constitution. Vendor artifacts are deployment targets."* `policies/source-of-truth-policy.md:14-28` states the canonical order as PRD → TRD → acceptance criteria → architecture summary → Issues, with the `/ai/` operating-model documents (*"context-sets, policies, roles, skills, boundaries"*) canonical for *how the project is run*. Context sets are one of five kinds in that second group, not the constitution over the whole.
Consequence: read literally, the line elevates `context-sets/` above `policies/`, `roles/`, `skills/`, and `boundaries/` — including over the file it appears in. Nothing in the repo acts on that, which is why this is non-blocking rather than a contradiction finding, but it is a sentence that would be cited if someone needed a hierarchy and reached for the memorable line.
Fix: delete lines 50-52.
Related: B1, B3

## N2 — non-blocking
Claim: three vendor names, seven occurrences over five lines; no model names and no retired terms.
Location: `boundaries/vendor-tooling-boundary.md:11` (Claude Code, Codex, ChatGPT), `:23` (`CLAUDE.md`), `:24` (Claude subagents), `:25` (Claude skills), `:27` (Codex)
Evidence: **Verified by running** a case-insensitive grep for vendor and model names over the file — hits on lines 11, 23, 24, 25, 27 — seven occurrences of three vendors — and a grep for `dispatch|sync block|track|prompt`, which returns nothing, confirming cycle 1's single-word fix held.
Consequence: the tension is real and worth stating rather than ruling on mechanically: a boundary document *about* vendor tooling naming vendors is not the same defect as a directive naming a model. But the names do no work. The rule at line 17 says *"a vendor-specific tool"* and needs no examples; the names appear only in §Summary's illustrative list and §Examples, both of which B2 deletes for a different reason. `vendors/README.md` is the file that may name vendors — it exists to hold *"vendor-specific configuration artifacts and vendor-specific mechanics"* (`:16-18`) — and it is in the same bundle.
Fix: falls out of the B2 deletion, plus rewording line 11 to *"vendor-specific AI tooling — agent frameworks, skills, hooks, memory files, IDE integrations"*, dropping the three product names. Non-blocking because no reader is misled; the names are illustrative and accurate.
Related: B2

## O1 — observation
Claim: the file has no `order:`, and unlike its siblings its position may actually matter.
Location: `boundaries/vendor-tooling-boundary.md:1-5`
Evidence: **Verified by running** a sweep of `order:` values across the corpus: `docs/global-context/core.md` 0, `docs/global-context/decision-layer.md` 1, `LEXICON.md` 2, `operating-model.md` 3; no boundary file carries one.
Consequence: none demonstrable, which is why this is an observation. The reason to note it: after the cuts, this file's content is a procedure that presupposes the rule stated in `operating-model.md` §Relationship to tools, and a bundle that placed the procedure first would read oddly. I cannot show that any generated bundle does so — `bin/bundle` emits in walk order, not `order:` order, and I did not trace how a consumer applies the field.
