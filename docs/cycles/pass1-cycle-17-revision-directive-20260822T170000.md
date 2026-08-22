# Directive — Pass 1, Cycle 17: revision of the policies (cycles 16a/16b)

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Coder, executing reviewer dispositions

Base: origin/main @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0.
Review artifacts: branches p1-cycle-16a-review @ 457714bd1e80fa87d6ace7838819e8f8621c37dc and p1-cycle-16b-review @ 1ff30fe335e72f3d21b45aeb571f417cf3d313dc. Merge both into the working branch first; they touch only reviews/.
Foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, docs/global-context/review-rubric.md.

## Rules for every edit

- Every finding below is applied as its artifact's Fix states unless this directive says otherwise. Read the artifact before editing the file.
- No pointers. Where a Fix says "reference" or "point at", state the rule in the file's own words or delete the sentence. The only paths that stay are normative data a policy operates on (scope globs, the log path, the expedited-log filename).
- Retired terms (dispatch, sync block, track, prompt) are removed on touch per LEXICON; count them in the report.
- Vendor names become "the forge", "the tracker", or are deleted; "human-gate tracker issue" is the term.
- Each retained policy opens with one line naming the session kind it governs.
- Every "Status of this draft", "Discharge note", "Placement", and revision-history section is deleted.
- Files through Pass 1 (operating-model, LEXICON, context-sets/testing-and-verification, policies/verification-boundary-policy) are edited only where named below, minimally.

## Dispositions

### policies/commit-and-change-control-policy.md — retain-with-changes
Apply CC-3 through CC-12. CC-1: this file's consequential-class list is canonical; in operating-model.md "Release gate", replace the inline enumeration with the sentence that the consequential class is the list this policy states. Report in one line any item that was only in operating-model's version. CC-2: the four-item branch-protection set moves to project-setup-requirements (below); here, keep one sentence that branch protection is the structural gate the push posture rests on. CC-13: this file is the single home for the human-gate requirement; no edit here, the other files are handled below or in their own cycles.

### policies/remote-write-verification-policy.md — retain-with-changes
Apply RW-2 through RW-10. Result is rules 3 and 4 (renumbered 1 and 2), the known-gap boundary statement, and the session-kind line. RW-1: flip frontmatter to status: draft, last-reviewed: null; delete the closing sentence. RW-5: state the two retained facts (detector kept for what it detects; closing the gap is open work) without citations.

### policies/project-setup-requirements.md — retain-with-changes
Apply PS-1 through PS-8. PS-1: requirement 1 becomes the full four-item set from commit-and-change-control (no force-push, no branch deletion, changes land via pull request, bypass disallowed including for administrators). PS-2: state requirements 2–4 in full; for requirement 2 name the in-scope set rule rather than the metadata policy. PS-4: drop the bin/ tool names or mark them as this repo's instance.

### policies/release-readiness-policy.md — retain-with-changes (Dave overrides the reviewer's merge)
The file shrinks to: the session-kind line, the definition of release-ready, and the statement that the release decision is gated per the commit-and-change-control policy's two tiers. Apply RR-3, RR-5, RR-6, RR-7 as deletions. RR-2: delete the release-package list here; roles/release-manager-agent.md keeps it and gains the one sentence that the package is assembled from the change package, not written fresh. RR-4: see LEXICON below; this file's known-gap section is deleted and the definition uses the LEXICON labels. RR-6: in roles/release-manager-agent.md replace "GitHub issue" with "tracker issue"; no other edit to that role.

### policies/decision-log-policy.md — retain-with-changes
Apply L1 through L5. L2: delete the Consult obligation section; the single home is decision-layer rule 10 and the reach narrowing to decision sessions is intended. L3: drop the repository name.

### policies/agent-review-policy.md — merge into roles/reviewer-agent.md, then delete
Apply A1: carry the Prohibited review patterns list and the sentence on stating what was and was not checked into roles/reviewer-agent.md; carry nothing else; delete the file. A2: the review artifact schema in skills/spec-review-cycle.md owns the output shape; delete the list here; role documents are trimmed in their own cycle. A5: in skills/spec-review-cycle.md, re-point the "What this schema governs" table and its note from policies/agent-review-policy.md to roles/reviewer-agent.md — that edit only, no other change to that skill.

### policies/testing-policy.md — merge into context-sets/testing-and-verification.md, then delete
Apply T1 through T8. T2: add "failure cases" as item 11 of the test-plan list in the merge target. T3: the broken-test sentence, the seven-level ladder, and the coverage rule land per T3's placement. T7: levels 4–7 name the evidence class each produces; do not redefine the classes. T8: fold the three additive items into operating-model.md's change package as sub-items of Test results. Delete the file.

### LEXICON.md — one edit
Add the release-impact vocabulary beside the evidence classes: blocking, deferred, accepted-risk, not-material, with the definitions from policies/verification-boundary-policy.md:104-109. "Requires Dave decision" is not a label; a gap awaiting his judgment is blocking. In verification-boundary-policy.md, replace the label definitions at :104-109 with the sentence that the labels are defined in the lexicon; keep the discharge conditions.

### policies/document-metadata-policy.md — not in this cycle
Cycle 18. Do not touch.

## Verification

1. bin/check-frontmatter --all passes.
2. bin/bundle-methodology runs clean with the two deleted files gone.
3. grep the seven touched policies, the two roles, the skill, the context set, LEXICON, and operating-model for: the four retired terms; GitHub, MCP, Claude; every path-shaped reference — list each survivor with its justification or remove it.
4. Every file in scope, in full, once more against the rubric's criteria 1, 3, 4, and 6 before committing.

## Output

Commit on p1-cycle-17-revision, push, open a pull request against main titled "Pass 1 cycle 17 revision: policies (16a/16b)". Do not merge. The PR body lists, per file, which findings were applied as written and which were not, with one line each for the latter.

## Report shape

One line per file: path, action (edited / deleted / merged-into), findings applied / findings varied. Then: the CC-1 discrepancy line; the retired-term count removed; any surviving path reference with its reason. Then branch, SHA, PR number.
