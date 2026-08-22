# Directive — Pass 1, Cycle 20: revision of the roles (cycles 19a/19b)

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Coder, executing reviewer dispositions

Base: origin/main @ ab7f08de (after #112).
Review artifacts, all on main: reviews/chief-of-staff-cycle-5.md, spec-reviewer-agent-cycle-3.md, context-quality-reviewer-cycle-1.md, pm-em-owner-cycle-1.md, orchestrator-agent-cycle-1.md, architect-agent-cycle-1.md, coder-agent-cycle-1.md, test-designer-agent-cycle-1.md, reviewer-agent-cycle-1.md, skeptic-risk-agent-cycle-1.md, release-manager-agent-cycle-1.md. Read each before editing its file.
Foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, docs/global-context/review-rubric.md.

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

## Rules for every edit

- Every finding is applied as its artifact's Fix states unless this directive says otherwise.
- No pointers. State the rule or delete the sentence; the only paths that stay are in chief-of-staff's read-sequence, which needs targets.
- Retired terms are removed on touch; count them in the report. Vendor names: "tracker issue", "forge", or deleted. No model names.
- Each retained role opens with one line naming the session kind it runs in.
- A role document states what the role inspects and decides. Output-shape lists (review outputs, test plans, release packages, response shapes) have one home elsewhere; delete them here per finding A2.
- Gap and risk labels are LEXICON's four: blocking, deferred, accepted-risk, not-material. No role keeps a "needs Dave decision" category.
- Files through Pass 1 are edited only where named below, minimally.

## Dispositions

### roles/chief-of-staff.md — retain-with-changes
Apply C1 through C11. C1: the mid-delta rule as the Fix words it. C11: status draft, last-reviewed null (not in-review — all governed files sit at draft through Pass 1). Additionally, from orchestrator finding O2: under the decomposition-and-handoff section, add "A package directive states the acceptance criteria the package must satisfy, and the boundaries the execution session must not cross."

### roles/spec-reviewer-agent.md — retain-with-changes
Apply S1 through S8. S3's dependent edit to operating-model.md:91-92 is applied. S9: this role gates specs and canonical documents; add one sentence ceding corpus-wide instruction-file review to the Context Quality Reviewer. Additionally: this role no longer restates the rubric's existence; Pass 1 directives from cycle 21 name the Context Quality Reviewer.

### roles/context-quality-reviewer.md — retain-with-changes (Dave overrides the merge)
Rewrite as the role that reviews governed instruction documents — Core, the decision layer, LEXICON, operating-model, policies, roles, skills, context-sets, boundaries, specs templates, engagements, writing — against the rubric. Content: session kind (execution; returns a review artifact per the artifact schema), scope as stated, what it inspects, what it decides (verdict and findings; never agreement), what it cedes to the Spec Reviewer (PRD/TRD and acceptance criteria). Apply X2's retained-file alternative, X3, X5's retained-file alternative, X6's retained-file alternative. Do not restate any criterion. Target: under 40 lines.
X4: add criterion 11 to docs/global-context/review-rubric.md with the wording in X4's Fix. Set review-rubric.md's audience: to [context-quality-reviewer, human].

### roles/pm-em-owner.md — merge into operating-model.md, then delete
Apply P1 through P6 as written.

### roles/orchestrator-agent.md — retire
Apply O1, O3, O4, O5. O2 lands in chief-of-staff as above, not in skills/directive-dispatch.md.

### roles/architect-agent.md — retain-with-changes
Apply AR-1 through AR-8. AR-2: "tracker issue".

### roles/coder-agent.md — retain-with-changes
Apply CO-1 through CO-7. The file is thin by design; it retains because it is the sole definition of its audience value.

### roles/test-designer-agent.md — retain-with-changes
Apply TD-1 through TD-8. TD-1: the context set owns the test-plan shape; carry "behaviors under test" and "known out-of-scope cases" into context-sets/testing-and-verification.md's list if not already covered by an existing item, and report which.

### roles/reviewer-agent.md — retain-with-changes
Apply RV-1 through RV-7. RV-1's dependent edit: in skills/spec-review-cycle.md, drop the second sentence of the Fix-versus-Recommendation note, keeping "Note the entry field is Fix, not Recommendation." That edit only.

### roles/skeptic-risk-agent.md — retain-with-changes
Apply SK-1 through SK-9. SK-1: LEXICON's four labels; the "Needs Dave decision" examples become blocking examples. SK-3: the Skeptic does not emit a ship recommendation; its output is findings and their labels.

### roles/release-manager-agent.md — retain-with-changes
Apply RM-1 through RM-7. RM-1: the release-package list stays here; skills/release-readiness-review.md's Procedure becomes the method of assembly and its Output drops the duplicated vocabulary — that edit only to that skill. RM-2: keep the "assembled from the change package" sentence and add that user-visible behavior and rollback/mitigation path are release-only items the Release Manager supplies.

## Verification

1. bin/check-frontmatter --all passes; bin/bundle --list (or bin/bundle-methodology if bundle is absent) runs clean with orchestrator-agent and pm-em-owner gone, and no audience: value anywhere names either slug.
2. grep all touched files for: the four retired terms; GitHub, MCP, Claude; "Needs Dave decision" and "requires Dave decision"; path-shaped references outside chief-of-staff's read-sequence — list each survivor with its reason or remove it.
3. Each retained role, in full, against rubric criteria
