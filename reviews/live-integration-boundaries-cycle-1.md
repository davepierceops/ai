# Review: boundaries/live-integration-boundaries.md — cycle 1

Verdict: changes-required
Disposition (criterion 10): **merge-into `policies/verification-boundary-policy.md`**
Reviewed: `boundaries/live-integration-boundaries.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11b)
Date: 2026-08-21
Scope: the whole document, all ten rubric criteria, judged as a bundle member. Criterion 4 judged against `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, and `operating-model.md` at the same SHA. Criterion 10 judged by computing the reference closure with `bin/bundle` from all six context-set entry points, then reading every closure member that states the same rules — principally `context-sets/testing-and-verification.md` and `policies/verification-boundary-policy.md` — and diffing their lists against this file's section by section.
Cross-checked: `context-sets/testing-and-verification.md`, `policies/verification-boundary-policy.md`, `context-sets/base.md`, `operating-model.md`, `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `LEXICON.md`, `docs/global-context/review-rubric.md`, `policies/document-metadata-policy.md`, `boundaries/mocked-boundaries.md`, `context-sets/production-grade-software.md`, `policies/release-readiness-policy.md`
Not inspected: `policies/testing-policy.md`, `specs/trd-template.md` beyond the two `error budget` hits, `roles/**`, `skills/**`, `.claude/**`, `vendors/`, `bin/` other than `bin/bundle`, and `engagements/`. The seven required-documentation fields were not tested against any real live boundary — no project in this repo declares one, so whether the field set is sufficient in practice is unverified and cannot be verified here. I did not attempt the merge, so the claim that the residue fits `policies/verification-boundary-policy.md` without disturbing it is inferred from reading that file's structure, not demonstrated by a draft. Whether Dave wants `boundaries/` to survive as a directory at all is his call and is not settled here.
Findings: 4 blocking, 2 non-blocking, 1 observation
Prior cycle: none — first artifact for this document
Dave should inspect: the criterion-10 call. This is a merge, not a retirement — two required-documentation fields and the risk-based cadence framing are real and have no other home — but taking it, together with the same call on `boundaries/mocked-boundaries.md`, leaves `boundaries/` holding two files.

## Criterion pass

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | pass — the file is self-contained; nothing in it requires opening another file |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`, both reserved values (`policies/document-metadata-policy.md:95-96`); no `order:` needed |
| 3 | No references to other files by path | pass — 0 path-shaped references |
| 4 | Core states it → remove it here | fail — N1 (1 restated rule, at 2 locations) |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | pass |
| 7 | Session kind is explicit | fail — B4 |
| 8 | Tiers, not model names; route and model, not track | fail — N2 (0 vendor names, 0 model names, 2 occurrences of a retired term) |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no filename |
| 10 | The file earns its place or is retired | **merge-into `policies/verification-boundary-policy.md`** — see below |

## Criterion 10 — merge-into `policies/verification-boundary-policy.md`

It lands in a bundle. **Verified by running** `python3 bin/bundle <entry> --format list` for all six context-set entry points: the file appears in all six closures. But its only inbound edge is incidental — **verified by running** `python3 bin/bundle base --format list --why`, which resolves it at depth 4 via `REVIEW-v0.4.md`, a v0.4 review-notes document whose line 163 lists it in a carried-forward table. A grep of the corpus for backticked references to the path returns `REVIEW-v0.4.md`, `docs/cycles/cycle-2-directive.md`, `docs/packages/package-b-migration-plan.md`, `docs/research/methodology-scan-phase2-findings.md`, and one prior review artifact. **No policy, context set, role, or skill cites this file.** It is in every bundle because a scratch document happens to mention it.

It does not contribute enough that no other file in that closure states. Section by section, against the two closure members that cover the same ground:

| Section here | Already stated in the same bundle |
| --- | --- |
| §Summary (definition of a live integration boundary) | `policies/verification-boundary-policy.md:13` defines a verification boundary; `context-sets/testing-and-verification.md:82-100` §Live-verified defines the live case |
| §Policy (explicit verification when material to user-visible behavior or release risk) | `policies/verification-boundary-policy.md:17`, `:107-112`, `:166-175` |
| §Examples (13 bullets) | `context-sets/testing-and-verification.md:182-198` §Boundary-sensitive areas (13 bullets) and `policies/verification-boundary-policy.md:70-89` §Boundary types (15 bullets) |
| §Live verification is useful for (7 bullets) | `context-sets/testing-and-verification.md:86-93` §Live-verified → Useful for (6 bullets) |
| §Live verification is not for (4 bullets) | `context-sets/testing-and-verification.md:95-100` §Does not prove, and `:238` §Anti-patterns (*"adding live tests to every unit run"*) |
| §Required documentation (7 fields) | `policies/verification-boundary-policy.md:32-44` §Boundary declaration (9 fields) — 5 of the 7 map directly |
| §Recommended cadence (4 bullets) | `policies/verification-boundary-policy.md:141-152` §CI and automation expectations (manually before release / dedicated CI job / on a schedule / after deploy as synthetic monitoring) |

**The residue is two things**, and both are one line each: the declaration fields **cadence** and **failure response**, which `policies/verification-boundary-policy.md` §Boundary declaration does not carry (it has `owner or trigger for follow-up`, which is neither); and the framing that cadence is chosen by **risk**, which that policy's §CI and automation expectations lists mechanisms for without saying how to pick among them. Add those to §Boundary declaration and §CI and automation expectations respectively, and delete this file.

## B1 — blocking
Claim: §Examples and §Live verification is useful for / is not for duplicate `context-sets/testing-and-verification.md`, which lands in the same bundle, and the two copies have diverged.
Location: `boundaries/live-integration-boundaries.md:17-48`
Evidence: **Verified by reading** both files in full at `7310937` and comparing bullet by bullet. §Examples lists *external APIs, map/tile providers, auth providers, hosted databases, email providers, payment providers, analytics/telemetry providers, browser-only rendering, PWA/service worker, production environment variables, domain/CORS restrictions, quotas and billing state, SLO monitoring*. `context-sets/testing-and-verification.md:184-198` lists *external APIs, auth and authorization, environment variables, browser-only behavior, maps/tiles/geolocation/rendering, service workers and PWA offline, payment/email/notification/messaging, storage and persistence, time/timers/scheduling, rate limits/quotas/billing, SLO targets and error budget state, security and privacy controls*. Neither is a subset: this file has hosted databases, analytics/telemetry, and domain/CORS; the context set has storage, time, and security/privacy.
Consequence: an agent asked "is this a boundary-sensitive dependency?" gets two non-identical lists in one bundle and no rule for which governs. Under Core rule 9 it must surface the disagreement rather than resolve it, so the duplication converts a routine judgment into an escalation. Concretely: a change touching **storage** is boundary-sensitive under the context set and absent from this file's list; a change touching **CORS** is the reverse.
Fix: delete lines 17-48. The union of the two lists belongs in one place — `context-sets/testing-and-verification.md` §Boundary-sensitive areas, which is the more complete of the two — and any item this file has that it lacks moves there.
Related: B2, B3

## B2 — blocking
Claim: §Required documentation states a second, shorter field set for a boundary declaration than the schema `policies/verification-boundary-policy.md` defines, in the same bundle.
Location: `boundaries/live-integration-boundaries.md:50-60`
Evidence: **Verified by running** a grep for the declaration headings in both files, then reading both. This file requires seven fields: dependency, production behavior, verification method, required environment/config, cadence, release requirement, failure response. `policies/verification-boundary-policy.md:34-44` requires nine: boundary name, production surface, representation mechanism, verification class, verified claims, unverified claims, deferred verification path, release impact, owner or trigger for follow-up. Four of that policy's nine — verification class, verified claims, unverified claims, deferred verification path — have **no counterpart here**, and `boundaries/mocked-boundaries.md:38-43` states a third field set again.
Consequence: three field sets for one artifact reach an agent in one bundle. An agent that documents a live boundary using this file's seven fields produces a declaration missing *what was verified* and *what was not* — the two fields the whole verification-boundary model exists to capture (`policies/verification-boundary-policy.md:21-29`). The gap is not cosmetic: the resulting declaration cannot answer questions 2 and 3 of that policy's own six.
Fix: delete lines 50-60 and add **cadence** and **failure response** to `policies/verification-boundary-policy.md` §Boundary declaration, which is the only content here that set lacks.
Related: B1, B3

## B3 — blocking
Claim: §Recommended cadence restates `policies/verification-boundary-policy.md` §CI and automation expectations.
Location: `boundaries/live-integration-boundaries.md:62-71`
Evidence: **Verified by reading** both. This file: *before release for critical user-visible integrations / scheduled synthetic checks / manual checklist for low-frequency or hard-to-automate behavior / production monitoring for behavior that can drift after deployment*. `policies/verification-boundary-policy.md:145-150`: *manually before release / in a dedicated CI job / on a schedule / after deploy as synthetic monitoring*. Four bullets each, three of them the same mechanisms.
Consequence: the third copy of the same guidance in one bundle, and the one genuinely distinct idea here — that the cadence is chosen by **risk**, stated in three words at line 64 — is buried under the restatement and would be lost if the section were simply deleted.
Fix: delete lines 62-71, and add the risk-based selection rule to `policies/verification-boundary-policy.md` §CI and automation expectations: the cadence follows the risk of the boundary, not a fixed schedule.
Related: B1, B2

## B4 — blocking
Claim: the file does not state which session kind it is for.
Location: `boundaries/live-integration-boundaries.md:1-5`
Evidence: **Verified by reading** the frontmatter — `status`, `last-reviewed`, `audience`, nothing more — against `docs/global-context/core.md:37-38` and rubric criterion 7.
Consequence: the file carries content for both kinds without saying so: §Live verification is useful for / is not for is execution-session material, and §Recommended cadence and §Policy (*"material to... release risk"*) are release-judgment material a decision session acts on. An execution session receives the cadence guidance and has no directive to which it applies.
Fix: on the merge, the question resolves itself — `policies/verification-boundary-policy.md` is the file that must state its session kind. If the merge is rejected, state it here in one line.

## N1 — non-blocking
Claim: the SLO and error-budget bullets restate `operating-model.md` §Change package item 7.
Location: `boundaries/live-integration-boundaries.md:31` and `:70-71`
Evidence: **Verified by running** `grep -rn "error budget" --include='*.md'` over `boundaries/`, `context-sets/`, `policies/`, `operating-model.md`, `specs/`. Line 31: *"SLO monitoring and error budget tracking against Top K user journey targets"*. `operating-model.md:155` (change package item 7): *"SLO status and error budget consumption for affected Top K user journeys"*. The grep returns the same claim in eight further files, including `policies/release-readiness-policy.md` and `context-sets/testing-and-verification.md:134-143`, all in the same bundle.
Consequence: minor here — the two statements agree. The cost is Core rule 13: a change to the Top K / error-budget model has ten places to find.
Fix: delete both, covered by the B1 and B3 deletions. Non-blocking because nothing is contradicted.
Related: B1, B3, N2

## N2 — non-blocking
Claim: the retired term *track* appears twice, as "tracking".
Location: `boundaries/live-integration-boundaries.md:31` and `:70-71`
Evidence: **Verified by running** a case-insensitive grep for `dispatch|sync block|track|prompt` over the file — two hits, both *"error budget tracking"*. Read against `LEXICON.md:69-70`, which retires *Track* with the scope *"A directive states route and model tier; there is no third part"*, and against rubric criterion 8, whose wording is unqualified: *"Track does not appear."*
Consequence: this is a naming collision, not the retired sense. Neither hit is a directive third part; both are the SRE term of art, the same shape as the approval-**prompt** carve-out `LEXICON.md:59-61` states explicitly for the other retired word. Recorded because the directive requires every use to be reported, and marked non-blocking because renaming *error budget tracking* would break a phrase eight other governed files use.
Fix: no edit here. If Dave wants criterion 8 read literally, the honest resolution is at `LEXICON.md` — give *Track* the same explicit carve-out sentence *Prompt* already has, naming error-budget and SLO tracking. That change is outside this cycle's scope.
Related: N1

## O1 — observation
Claim: no governing document references this file, so its bundle membership depends on a scratch document.
Location: `boundaries/live-integration-boundaries.md` (whole file)
Evidence: **Verified by running** `python3 bin/bundle base --format list --why`, which resolves the file at depth 4 via `REVIEW-v0.4.md`; and a grep of the corpus for the path, which returns only `REVIEW-v0.4.md:163`, `docs/cycles/cycle-2-directive.md:61`, `docs/packages/package-b-migration-plan.md:19`, `docs/research/methodology-scan-phase2-findings.md:545`, and `reviews/document-metadata-policy-cycle-5.md:9`.
Consequence: if `REVIEW-v0.4.md` is ever retired or its table de-backticked, the file silently leaves every bundle — no tool reports it, because `bin/bundle --strict` only fails on dangling `depends-on`, not on a document dropping out of the closure. Recorded as an observation because the merge disposition makes it moot; it is stated so the same check gets run on the other boundary files if the merge is rejected.
