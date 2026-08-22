# Review: boundaries/mocked-boundaries.md — cycle 1

Verdict: changes-required
Disposition (criterion 10): **merge-into `policies/verification-boundary-policy.md`** — one sentence survives; the rest is deleted
Reviewed: `boundaries/mocked-boundaries.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11b)
Date: 2026-08-21
Scope: the whole document, all ten rubric criteria, judged as a bundle member. Criterion 4 judged against `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md` at the same SHA. Criterion 10 judged by computing the reference closure with `bin/bundle` from all six context-set entry points, then diffing this file's every section against the closure members that state the same rules — `policies/verification-boundary-policy.md`, `context-sets/testing-and-verification.md`, `context-sets/base.md` — including a key-by-key comparison of the two YAML declaration examples.
Cross-checked: `policies/verification-boundary-policy.md`, `context-sets/testing-and-verification.md`, `context-sets/base.md`, `boundaries/live-integration-boundaries.md`, `operating-model.md`, `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `docs/global-context/review-rubric.md`, `policies/document-metadata-policy.md`, `policies/release-readiness-policy.md`
Not inspected: `policies/testing-policy.md`, `roles/**`, `skills/boundary-audit.md`, `skills/**` generally, `.claude/**`, `vendors/`, `specs/`, `engagements/`, and `bin/` other than `bin/bundle`. No mock or MSW handler was exercised — the YAML examples were compared as text and never validated against a schema or a consumer, because none exists in this repo. Whether any tooling reads either key set was not checked beyond a grep; if something does, B1's fix direction changes and that dependency would need to be found first.
Findings: 4 blocking, 3 non-blocking, 1 observation
Prior cycle: none — first artifact for this document
Dave should inspect: B1 — two incompatible YAML schemas for one declaration, in one bundle, in a file that names the other as authoritative. That is the finding that decides the disposition; everything else here is duplication.

## Criterion pass

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — B2 (the operative rule is delegated to a file the bundle reader cannot open) |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`, both reserved values (`policies/document-metadata-policy.md:95-96`); no `order:` needed |
| 3 | No references to other files by path | fail — B2 (1 reference) |
| 4 | Core states it → remove it here | fail — N1 (1 restated rule) |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | fail — N3 (§Policy line 15) |
| 7 | Session kind is explicit | fail — B4 |
| 8 | Tiers, not model names; route and model, not track | fail — B1, N2 (1 vendor name, 0 model names, 1 occurrence of a retired term) |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no filename; `external.geocoding` is a boundary name, not a file |
| 10 | The file earns its place or is retired | **merge-into `policies/verification-boundary-policy.md`** — see below |

## Criterion 10 — merge-into `policies/verification-boundary-policy.md`

It lands in a bundle. **Verified by running** `python3 bin/bundle <entry> --format list` for all six context-set entry points: the file appears in all six closures, resolved at depth 3 via `OPEN-ITEMS.md` (**verified by running** `python3 bin/bundle base --format list --why`). As with `boundaries/live-integration-boundaries.md`, no policy, context set, role, or skill cites it — a grep of the corpus for the path returns only `OPEN-ITEMS.md:661`, `docs/cycles/doc-review-2026-08-02-directive.md:29`, `docs/research/methodology-scan-phase2-findings.md`, and prior review artifacts.

It contributes nothing that no other file in that closure states, with one sentence excepted:

| Section here | Already stated in the same bundle |
| --- | --- |
| §Summary (definition of a mocked boundary) | `policies/verification-boundary-policy.md:13,17`; `context-sets/testing-and-verification.md:37-59` §Mock-verified |
| §Policy, first line (*"mocks must not create hidden confidence"*) | `context-sets/base.md:100-108` §Mock rule; `policies/verification-boundary-policy.md:21` (*"Agents must not let tests imply broader confidence than they actually support"*) |
| §Policy, blockquote (*"a claim about our side of the contract"*) | **not stated elsewhere** — `context-sets/base.md:102` and `context-sets/testing-and-verification.md:23` both say *"A mock is a claim with a deferred proof"*, which does not say *which side* is unproven |
| §Common mocked boundaries (13 bullets) | `policies/verification-boundary-policy.md:70-89` §Boundary types (15 bullets) — a superset; every bullet here appears there |
| §Required declaration (6 fields) | `policies/verification-boundary-policy.md:32-44` §Boundary declaration (9 fields) — and this file names that section as authoritative, then states fewer fields than it |
| §Example (YAML) | `policies/verification-boundary-policy.md:46-68` — the same geocoding example under a different, incompatible key set (B1) |

**The residue is one sentence** — the contract framing at line 19 — and it belongs in `policies/verification-boundary-policy.md` §Core rule, where it sharpens a rule already stated. The remainder is a subset, a divergent restatement, or a contradiction. Under rubric criterion 10 a file in that condition *"is removed, not fixed"*; the disposition is recorded as merge-into rather than retire only because that one sentence is worth carrying across, and the executor should not lose it by deleting the file outright.

## B1 — blocking
Claim: the §Example YAML uses a different key set from the declaration schema this file names as authoritative, so the bundle carries two incompatible schemas for one artifact.
Location: `boundaries/mocked-boundaries.md:45-64`, against `policies/verification-boundary-policy.md:46-68`
Evidence: **Verified by running** a grep for top-level YAML keys in both blocks. This file: `boundary`, `production_surface`, `mocked_by`, `verified_by_mock`, `not_verified_by_mock`, `deferred_to`, `release_status`. The policy: `boundary`, `production_surface`, `representation`, `verification_class`, `verified_claims`, `unverified_claims`, `deferred_verification`, `release_impact`. Two keys match; five differ; the policy carries `verification_class`, which has no counterpart here at all. Both examples model the same geocoding boundary — this file names it `external.geocoding`, the policy `stadia.geocoding` — and both use the same MSW mechanism, so the divergence is in the schema, not the subject.
Consequence: an agent instructed at line 40 to *"declare it using the boundary declaration schema in `policies/verification-boundary-policy.md`"* and then handed a worked example in a different schema, in the same file, has two sources that disagree. Core rule 9 makes this a surface-and-stop, not a pick-one — so the intended cheap path (copy the example) is the path that produces a declaration the named schema rejects, and the safe path is an escalation. A declaration written from this example carries no `verification_class`, which is the field `policies/verification-boundary-policy.md:91-103` §Required status labels exists to populate.
Fix: delete the block at lines 45-64. One worked example, in the file that owns the schema, is the whole fix. Do not reconcile the keys — a second copy of a worked example is the defect, whatever its keys say.
Related: B2, B3

## B2 — blocking
Claim: the file's operative rule is delegated to another file by path, so it does not survive the trip into a bundle.
Location: `boundaries/mocked-boundaries.md:38-43`
Evidence: **Verified by running** a grep for backticked paths over the file — one hit, `` `policies/verification-boundary-policy.md` ``, at line 41, inside the sentence that states the file's only requirement: *"For each material mocked boundary, declare it using the boundary declaration schema in `policies/verification-boundary-policy.md`."*
Consequence: this is a criterion 1 failure before it is a criterion 3 one. The section does not restate the schema — it points at it and then gives an *"At minimum"* list of six fields that is not the schema either. An agent reading only what this section gives it declares a boundary against six fields; `policies/verification-boundary-policy.md:34-44` requires nine, and the three missing are `boundary name`, `verification class`, and `owner or trigger for follow-up`. So the shortfall is not hypothetical: the "at minimum" list is below the minimum the cited schema sets.
Fix: delete lines 38-43. The requirement is already stated at `policies/verification-boundary-policy.md:17` (*"must have a declared verification boundary"*) and its field list is there in full.
Related: B1, B3

## B3 — blocking
Claim: §Common mocked boundaries is a strict subset of `policies/verification-boundary-policy.md` §Boundary types, in the same bundle.
Location: `boundaries/mocked-boundaries.md:21-36`
Evidence: **Verified by reading** both lists at `7310937` and matching bullet to bullet. All thirteen bullets here — HTTP APIs, browser APIs, time, geolocation, storage, authentication, authorization, map/tile providers, service workers, network status, generated test data, third-party response fixtures, SLO monitoring — appear at `policies/verification-boundary-policy.md:72-89`, which carries fifteen and adds jsdom replacing a real browser, local development config, and local environment variables replacing deployed secrets.
Consequence: an agent using this list to decide whether a boundary is material misses three types the policy names, two of which — local dev config and local env vars standing in for deployed config — are exactly the class that produces a green suite against a broken deployment. Unlike B1 this is not a contradiction, so a careful reader loses nothing; the reader who stops at the shorter list does.
Fix: delete lines 21-36.
Related: B1, B2

## B4 — blocking
Claim: the file does not state which session kind it is for.
Location: `boundaries/mocked-boundaries.md:1-5`
Evidence: **Verified by reading** the frontmatter against `docs/global-context/core.md:37-38` and rubric criterion 7.
Consequence: the same defect as its three siblings — content selected into execution-session bundles by `audience: [all-roles, human]` with no statement of which kind acts on it. Here the answer is genuinely both (an executor writes the mock; a decision session weighs the gap at release), which is a permitted answer under criterion 7 and still has to be said.
Fix: on the merge this resolves at `policies/verification-boundary-policy.md`, which must state it. If the merge is rejected, state it here in one line.

## N1 — non-blocking
Claim: the SLO and error-budget bullet restates `operating-model.md` §Change package item 7.
Location: `boundaries/mocked-boundaries.md:35-36`
Evidence: **Verified by running** `grep -rn "error budget" --include='*.md'` over `boundaries/`, `context-sets/`, `policies/`, `operating-model.md`, `specs/`. This file: *"SLO monitoring and error budget tracking (targets defined but no production signal in place)"*. `operating-model.md:155`: *"SLO status and error budget consumption for affected Top K user journeys"*. `policies/verification-boundary-policy.md:89` states the same as a boundary type: *"SLO targets and error budget state not yet connected to production monitoring"*.
Consequence: minor — the three agree. The cost is Core rule 13 maintenance across ten files carrying the claim.
Fix: covered by the B3 deletion.
Related: N2

## N2 — non-blocking
Claim: the retired term *track* appears once, as "tracking", and a vendor library name appears once.
Location: `boundaries/mocked-boundaries.md:35` (tracking) and `:50` (MSW)
Evidence: **Verified by running** a case-insensitive grep for `dispatch|sync block|track|prompt` over the file — one hit, *"error budget tracking"* — and a grep for vendor and model names — one hit, *"MSW handler in unit/component tests"*. `LEXICON.md:69-70` retires *Track* with the scope *"A directive states route and model tier; there is no third part"*; rubric criterion 8 states it without qualification.
Consequence: the *track* hit is the SRE term of art, not the directive third part — the same naming collision as the approval-**prompt** carve-out at `LEXICON.md:59-61`, and renaming it would break a phrase eight other governed files use. The MSW hit is a real criterion 8 defect: it names one JavaScript mocking library in a document that governs every project, so an agent in a non-JS project reads a mechanism it cannot use. Note the same name appears at `policies/verification-boundary-policy.md:51`, which is outside this cycle's scope and should be swept when that file is reviewed.
Fix: both fall out of the B1 and B3 deletions. If `LEXICON.md` is to be read literally on *track*, give it the carve-out sentence *Prompt* already has — outside this cycle.
Related: N1, B1

## N3 — non-blocking
Claim: §Policy's first line is rationale, not a rule.
Location: `boundaries/mocked-boundaries.md:15`
Evidence: **Verified by reading**: *"Mocks are acceptable, but they must not create hidden confidence."* The first clause grants permission nobody withheld; the second is the argument for the declaration requirement stated below it. `policies/verification-boundary-policy.md:21` states the same as an actual prohibition: *"Agents must not let tests imply broader confidence than they actually support."*
Consequence: minor. It reads as a rule and selects no behavior, so an agent that satisfies it has done nothing.
Fix: delete line 15, keep line 19 (the blockquote), and carry that one sentence into `policies/verification-boundary-policy.md` §Core rule per the disposition.

## O1 — observation
Claim: no governing document references this file, so its bundle membership depends on `OPEN-ITEMS.md`.
Location: `boundaries/mocked-boundaries.md` (whole file)
Evidence: **Verified by running** `python3 bin/bundle base --format list --why` — resolved at depth 3 via `OPEN-ITEMS.md` — and a grep of the corpus for the path, which returns no policy, context set, role, or skill.
Consequence: same as recorded for `boundaries/live-integration-boundaries.md`: the file leaves every bundle silently if that one backlog reference goes, and no tool reports it. Moot under the merge disposition; stated so the check is run if the merge is rejected.
