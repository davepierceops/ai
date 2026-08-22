# Review: policies/remote-write-verification-policy.md — cycle 6

Verdict: changes-required
Reviewed: policies/remote-write-verification-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent (execution session, frontier tier)
Date: 2026-08-22
Scope: the whole file, 183 lines, against all ten rubric criteria at docs/global-context/review-rubric.md @ 2a722bb.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/verification-boundary-policy.md, policies/commit-and-change-control-policy.md, skills/spec-review-cycle.md, skills/directive-dispatch.md (existence only), decisions/log.md DEC-000080, OPEN-ITEMS.md — all @ 2a722bb.
Not inspected: bin/ implementations; the body of skills/directive-dispatch.md (its own cycle); the four policies not in this cycle's scope; roles/; specs/, engagements/, writing/, vendors/ bodies; prior review artifacts other than the cycle-5 pointer below.
Findings: 10 — 7 blocking, 2 non-blocking, 1 observation
Prior cycle: reviews/remote-write-verification-policy-cycle-5.md
Dave should inspect: RW-1 (the file is `status: agreed` in frontmatter and says "Nothing here is agreed" in its last line — one of the two is wrong, and which is a decision only he makes) and the criterion-10 disposition below, which cuts the file to about a quarter of its length and raises a merge-into-Core alternative.

## Criterion 10 first — disposition

**Retain-with-changes** — reduced to Rule 3, Rule 4, and the known gap.

The file lands in the `all-roles` bundle. Core rule 12 now states most of it:
"A tool's success response is a claim. Confirm the correct content landed
before reporting it. Read current state before retrying a write that appeared
to fail. If you cannot read it back, report only what the operator reported."
That is Rule 1, Rule 2, and the "Where the agent cannot read its own write
back" paragraph, in three sentences. Criterion 4 removes all three from here.

Two things survive that Core does not state and should not carry:

- **Rule 3** — that the repository's own log, not the tool's response and not
  the agent's recollection, is the authority on what landed, and that a SHA is
  read from it rather than invented.
- **Rule 4** — the two-consecutive-qualifying-failures detector, with its
  qualifying/not-qualifying taxonomy and its counting rules. `decisions/log.md`
  DEC-000080 records the decision to keep it for what it detects. It is roughly
  twenty lines of operational taxonomy; Core is fifty-four lines of standing
  rule and would be the wrong home.

The **known gap** — landing is verified, content is not — survives as the
boundary statement on the two rules.

Everything else goes: the failure-mode essay, the Scope section, the
Relationship-to-existing-rules section, Placement, and Status of this draft.
That is 183 lines to roughly 45.

**The merge-into alternative, for Dave.** If Rule 4's taxonomy were compressed
to its trigger and its action — two qualifying transport failures in a row means
stop and establish state — the residue would fit in Core beside rule 12, and
this file would retire. That trades the taxonomy (which is what makes the
detector unambiguous in the moment) for one fewer file. Recommend against, but
it is a real option and the criterion-10 answer changes if he takes it.

## Criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — RW-4, RW-5, RW-9 |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`; no `order:`, and position does not carry meaning here |
| 3 | No references to other files by path | fail — RW-5, 18 path references |
| 4 | Core states it → remove it here | fail — RW-2 |
| 5 | Agent instruction, not authoring principle | fail — RW-6 |
| 6 | Instructions, not rationale | fail — RW-6, RW-9 |
| 7 | Session kind is explicit | fail — RW-8 |
| 8 | Tiers, not model names; route and model, not track | fail — RW-3 (retired "track"), RW-7 (vendor names); no model names |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — the file prescribes no generated filename |
| 10 | The file earns its place or is retired | retain-with-changes, as above |

## RW-1 — blocking
Claim: The frontmatter says `status: agreed`; the file's last sentence says "Nothing here is agreed."
Location: policies/remote-write-verification-policy.md:2 and :183
Evidence: Verified by reading. Frontmatter line 2 is `status: agreed` with `last-reviewed: reviews/expedited-log.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3`; line 183 reads "Nothing here is agreed." `git log -1 -- policies/remote-write-verification-policy.md` → 0bea63d, "docs(policies/remote-write-verification-policy.md): status -> agreed" — the flip landed and the closing sentence was not swept with it. This is also the only one of the four policies in this cycle not carrying `status: draft`, against the baton's record that everything stays `draft` through Pass 1.
Consequence: Core rule 9 — two sources disagree about the governing status of a canonical document. An agent reading the bundle cannot tell whether this policy binds it. Core rule 13 is the rule that was missed: a changed fact changes everywhere it appears.
Fix: Delete :183 as part of deleting the Status-of-this-draft section (RW-6). Whether the frontmatter stays `agreed` through Pass 1 or reverts to `draft` with the rest is Dave's call — the directive forbids a status flip in this cycle, so this is recorded, not acted on.

## RW-2 — blocking
Claim: Rule 1, Rule 2, and the "Where the agent cannot read its own write back" paragraph restate Core rule 12.
Location: policies/remote-write-verification-policy.md:31-38 (Rule 1), :40-45 (Rule 2), :108-114 (cannot-read-back)
Evidence: Verified by reading docs/global-context/core.md at 2a722bb. Rule 12: "A tool's success response is a claim. Confirm the correct content landed before reporting it. Read current state before retrying a write that appeared to fail. If you cannot read it back, report only what the operator reported." Sentence one is Rule 1 here; sentence two is Rule 2 here; sentence three is :108-114 here. :37-38 additionally restates Core rules 5-7 ("an unverified claim from a tool is still an unverified claim") and does so by pointing at `context-sets/base.md`, which is deleted (RW-4).
Consequence: Core loads first in every bundle and cannot be waived. Three restatements of it, one of them justified by a dead pointer, in a file loaded immediately after.
Fix: Delete :31-45 and :108-114. Renumber the surviving rules. The section heading becomes the two rules Core does not state.
Related: RW-4

## RW-3 — blocking
Claim: Retired terms — "dispatch" and "track" — appear twelve times.
Location: policies/remote-write-verification-policy.md:57, :100, :106, :174 (prose "dispatch"); :56, :83, :102, :128, :178 (the filename `skills/directive-dispatch.md`); :175, :179, :181 (prose "track")
Evidence: Verified by running a case-insensitive grep for the four retired terms over the file. LEXICON.md states the replacements: dispatch → "hand the directive to an execution session," or "direct"; track → a directive states route and model tier, there is no third part. The three "track" uses at :175, :179, :181 are the retired sense ("the retired delivery track," "that track," "the track language"), not the exempt tracker/tracking sense. "tracker" at :139 and "tracked" at :145 are the exempt sense and are not counted. This is the file the directive expected to carry the most Track A / Track B residue; the residue that remains is generic "track," not the lettered form.
Consequence: LEXICON's touch rule requires any file edited for another reason to be conformed. This file is being edited; the terms must go with the edit.
Fix: :57, :100, :106 and :174-181 all fall inside sections deleted by RW-2, RW-6, and RW-9. Of the five filename occurrences, four fall inside deleted sections; the one at :83 is inside Rule 4 and should be cut with the rest of :78-87 per RW-9, leaving Rule 4 as its trigger, its taxonomy, its counting rules, and its action.

## RW-4 — blocking
Claim: Three references to files that do not exist.
Location: policies/remote-write-verification-policy.md:37 and :160-161 (`context-sets/base.md`, and "base.md"); :167 (`vendors/claude-code/mcp-write-verification.md`)
Evidence: Verified by running `git log --oneline --diff-filter=D -1 -- context-sets/base.md` → deleted in 40b5ffe ("Pass 1 cycle 12 revision"); `test -e vendors/claude-code/mcp-write-verification.md` → false, and `ls vendors/claude-code` returns only `environment-config.md`. :37 and :160 are the two lines the baton at docs/batons/baton-20260822T153848.md names. :161 continues :160 with a bare "base.md" and :167 is an additional one the baton does not list.
Consequence: :160-163 is worse than a dead pointer — it is an open question ("whether the underlying principle should also appear in `context-sets/base.md`") whose subject no longer exists, so the question reads as live work when it is closed.
Fix: :37 goes with RW-2. :149-163 (Placement) and :165-183 (Status of this draft) go with RW-6, taking :160-161 and :167 with them. See RW-10 for why the open question at :155-163 is closed, not merely relocated.
Related: RW-2, RW-6, RW-10

## RW-5 — blocking
Claim: Eighteen path-shaped references to other files.
Location: policies/remote-write-verification-policy.md:37, :56, :81, :83, :102, :118, :128, :137, :145, :149, :150, :152, :160, :161, :167, :170, :173, :178, :180
Evidence: Verified by running a path-shaped-token extraction over the body (frontmatter excluded): `skills/directive-dispatch.md` ×5, `context-sets/base.md` ×2 plus a bare "base.md" ×1, `OPEN-ITEMS.md` ×2, `docs/cycles/*-directive.md` ×3, `skills/spec-review-cycle.md` ×1, `decisions/log.md` ×1, `vendors/README.md` ×1, `vendors/claude-code/` ×1, `vendors/claude-code/mcp-write-verification.md` ×1.
Consequence: The densest path-reference load of the four policies in this cycle — roughly one per ten lines. The bundle reader can follow none of them, and three lead nowhere even for a reader with the repository.
Fix: Sixteen disappear with the RW-2, RW-6, and RW-9 deletions. Two must be restated rather than dropped: `decisions/log.md` DEC-000080 at :81, which is the authority for keeping Rule 4 — state that the detector is kept for what it detects, without the citation; and `OPEN-ITEMS.md` at :145, where the known gap is tracked — state that closing the gap is open work, without the path.

## RW-6 — blocking
Claim: Two sections — Placement and Status of this draft — are authoring and revision history addressed to whoever maintains the document, not instructions to the agent reading it.
Location: policies/remote-write-verification-policy.md:147-163 (Placement), :165-183 (Status of this draft); also :25-27 (how the discipline was learned)
Evidence: Verified by reading. Placement argues why the file is a policy rather than a vendors/ document and revisits a decision already made. Status of this draft is a five-revision changelog naming four directive files by path and dating each change. :25-27 states that the discipline "was learned across three sessions and lived only in chat history."
Consequence: Criterion 5 and criterion 6 both fail. Thirty-seven lines of the file — a fifth of it — instruct nobody. Git carries revision history; the bundle reader gets it as loaded context and cannot act on any of it.
Fix: Delete :25-27, :147-163, and :165-183.
Related: RW-1, RW-4

## RW-7 — blocking
Claim: Vendor names appear three times.
Location: policies/remote-write-verification-policy.md:91 ("The GitHub MCP tools"), :150 (`vendors/claude-code/`), :167 (`vendors/claude-code/mcp-write-verification.md`)
Evidence: Verified by running a case-insensitive grep for vendor and model names over the file. No model names found. The file's own :152-153 invokes the vendors/ swap test — "would swapping vendors leave the sentence true?" — and then names a vendor twice in the same section.
Consequence: The Scope section's whole claim is that nothing here depends on a particular transport, and it opens by naming one.
Fix: :150 and :167 go with RW-6. :91-95 collapses to the one sentence the section actually needs, with no transport named: the rules govern any tool-mediated remote mutation, because the failure is that a response is a claim about a write rather than evidence of one.

## RW-8 — non-blocking
Claim: The file does not state which session kind it is for.
Location: policies/remote-write-verification-policy.md:1-7
Evidence: Verified by reading; no session-kind statement. `policies/verification-boundary-policy.md:9-10`, a peer policy through Pass 1, opens with one.
Consequence: The rules govern both kinds, but a decision session reading Rule 3 ("Where a local clone exists") cannot tell whether the rule assumes it holds one. Core states a decision session may hold a clone, so the answer is yes — but the file leaves it to be inferred.
Fix: Open with the session-kind line: this policy governs both session kinds.

## RW-9 — non-blocking
Claim: The Relationship-to-existing-rules section, the Scope section's dispatch paragraph, and Rule 4's closing paragraph are entirely about other documents and about what this policy no longer covers.
Location: policies/remote-write-verification-policy.md:78-87 (Rule 4 closing), :100-106 (Scope, "What this policy no longer governs: dispatch"), :116-130 (Relationship to existing rules)
Evidence: Verified by reading. :100-106 states what the policy does *not* govern. :116-130 summarises `skills/spec-review-cycle.md` and `skills/directive-dispatch.md`. :78-87 explains that Rule 4 "opens onto nothing else" and that "there is no alternative route for it to select."
Consequence: Twenty-eight lines that state no rule. The reader who has only the bundle cannot verify any of the summarised claims, and a negative-scope statement is only meaningful to someone who remembers the removed scope.
Fix: Delete all three spans. Rule 4 keeps :59-77 — the trigger, the two lists, and the counting rules — and its action stays in the rule's own text.
Related: RW-3

## RW-10 — observation
Claim: The open question at :155-163 is closed, not open.
Location: policies/remote-write-verification-policy.md:155-163
Evidence: Verified by reading. The question is whether the principle "A write through an unreliable transport is not evidence that the write landed. Verify before reporting, and read state before retrying" should also appear in `context-sets/base.md` "beside the evidence vocabulary, where it is always loaded." Two things have happened since: base.md was deleted in 40b5ffe, and Core rule 12 states the principle in the file that is always loaded first.
Consequence: Left as written, the question invites an executor to promote a rule that has already been promoted, into a file that no longer exists.
Fix: Deleted by RW-6. Recorded here so the closure is on the record rather than lost with the section.
Related: RW-2, RW-4
