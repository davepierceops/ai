# Review: policies/decision-log-policy.md — cycle 1

Verdict: changes-required
Reviewed: policies/decision-log-policy.md @ 2a722bba17a42e65709dda5fb169acee3f1eaaa0
Reviewer: Spec Reviewer Agent
Date: 2026-08-22
Scope: the whole file (72 lines), against docs/global-context/review-rubric.md @ 2a722bb, all ten criteria.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md (all @ 2a722bb); policies/document-metadata-policy.md, policies/agent-review-policy.md, policies/testing-policy.md for cross-policy duplication.
Not inspected: decisions/log.md itself (the log's contents, as against the policy governing it); bin/ tooling behaviour against this policy; the C1a source material referenced at line 71, which I could not locate in the repository.
Findings: 5 — 2 blocking, 2 non-blocking, 1 observation
Dave should inspect: L2. Removing the Consult obligation section deletes this file's only statement of *why* the log gets read; the obligation survives as decision-layer rule 10, but only decision sessions receive that file, so the rule stops reaching execution sessions. That reach change is a decision, not an edit.

## Criterion 10, first and explicitly

**retain-with-changes.**

The entry format, the DEC-NNNNNN identifier scheme, the step-of-ten assignment
rule, the collision-resolution rule, and append-only supersession are stated
nowhere else in the repository. No other in-scope file defines them, and a
bundle that omits this file leaves an agent unable to append a well-formed
entry. The file earns its place. What it carries beyond that — the consult
obligation — is decision-layer rule 10 and belongs there.

## The ten criteria

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — L4 (`C1a` is unresolvable from a bundle) |
| 2 | `audience:` is the selector | pass — `[all-roles, human]`; no `order:`, and position does not matter for this file |
| 3 | No path references | fail — L1, L3. `decisions/log.md` (19, 67) is exempt: it is the artifact this policy governs, not a deferral of content to another file |
| 4 | Core states it → remove it here | fail — L2 |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | fail — L5 |
| 7 | Session kind explicit | fail — L5 covers the rationale; session kind is separately absent, folded into L2's fix |
| 8 | Tiers, not model names | pass — no model name, no tier claim, no use of the retired *track* |
| 9 | Filenames `<descriptor>-<timestamp>` | pass — the file prescribes `decisions/log.md`, a stated convention naming the file, which criterion 9 permits |
| 10 | Earns its place | pass, with changes — see above |

## L1 — blocking
Claim: The Consult obligation section instructs the reader to add a line to `context-sets/base.md`, a file that no longer exists.
Location: policies/decision-log-policy.md:64-65
Evidence: Verified by running. `git cat-file -e 2a722bb:context-sets/base.md` → "path does not exist in 2a722bb"; `git log --diff-filter=D -- context-sets/base.md` → deleted in 40b5ffe, "Pass 1 cycle 12 revision: context-sets and boundaries (6 deleted, 4 retained, 5 merge targets) (#98)". `ls context-sets/` returns three files, none named base.md.
Consequence: The sentence "This line is added to `context-sets/base.md` required behavior" is an instruction with no executable target. An agent that follows it stops, or invents a destination. The block-quoted obligation beneath it is left with no stated home, so the rule reads as pending insertion into a file that was deleted ten cycles ago — the policy describes its own enforcement as not-yet-done when in fact the obligation landed as decision-layer rule 10.
Fix: Delete lines 62-72 entire, per L2. If any part is retained instead, the destination sentence must name the surviving home rather than `context-sets/base.md`.
Related: L2

## L2 — blocking
Claim: The Consult obligation section restates decision-layer rule 10.
Location: policies/decision-log-policy.md:62-72
Evidence: Verified by reading both texts at 2a722bb. decision-layer.md:29 reads "**Check the decision log before you govern something it already governs.** Before recommending or encoding anything an existing decision may govern, read the decision log and cite the governing entry by ID." decision-log-policy.md:67-69 reads "consult the project's decision log (`decisions/log.md`) before recommending or encoding anything an existing decision may govern, and cite the governing entry by ID". The two are the same rule in near-identical wording; the baton confirms the placement — "Decision-log consultation is decision-layer rule 10."
Consequence: Criterion 4 defect. Two homes for one obligation is the drift condition this repo exists to prevent: a later cycle that narrows the rule in the decision layer leaves this policy asserting the wider version, and an agent reading a bundle carrying both has no rule for which governs. The duplication is also self-defeating here, since the policy states the obligation as *not yet added* (L1) while the decision layer already carries it as live.
Fix: Delete lines 62-72. The rule's single home is decision-layer rule 10. Note the reach consequence flagged in "Dave should inspect": the decision layer is not delivered to execution sessions, so deleting this section removes the obligation from execution-session bundles. If execution sessions must also consult the log, that is a decision-layer or Core change, not a reason to keep the restatement here.
Related: L1

## L3 — non-blocking
Claim: The methodology repository is named as `davepierceops/ai`; it is `davepierceops/fiducial`.
Location: policies/decision-log-policy.md:20
Evidence: Verified by running. `git config --get remote.origin.url` → `https://github.com/davepierceops/fiducial.git`. The baton records the same staleness in the generator — "`bin/bundle-methodology` stamps `davepierceops/ai` and no age; Pass 2" — which is a separate occurrence in `bin/` and out of this scope; this one is in an in-scope document and is not excluded by the directive's step 6.
Consequence: An agent reading this in a bundle is told the methodology decisions live in a repository that does not exist under that name. Where the reader has access to both, it resolves to the wrong log; where it does not, the sentence is simply false and undermines the one thing the section is asserting — that there is exactly one place a methodology decision resolves to.
Fix: Replace `davepierceops/ai` with `davepierceops/fiducial`, or drop the parenthetical entirely — "The methodology repo keeps its own, for methodology decisions" carries the rule without a repository name, and the name is the part that goes stale.

## L4 — non-blocking
Claim: The closing sentence cites "the C1a misses", a finding identifier with no definition in the file or anywhere a bundle reader can reach.
Location: policies/decision-log-policy.md:71
Evidence: Verified by running. `grep -rn "C1a"` across the repository returns this line and no definition; the identifier is not in LEXICON.md, decisions/, or reviews/. Inferred by reading: it is a finding id from a review cycle that predates the current artifact set.
Consequence: Criterion 1 defect. The sentence is the file's justification for the obligation, and its load-bearing term resolves to nothing for an agent that has never seen the repository. A reader cannot evaluate the claim, act on it, or tell whether it is still true.
Fix: Delete the sentence. It falls with lines 62-72 under L2; if any part of that section survives, the sentence goes regardless — it is rationale (criterion 6) resting on an unresolvable reference (criterion 1).
Related: L2

## L5 — observation
Claim: Three passages are rationale or deferred-future notes rather than instructions, and the file does not state which session kind it addresses.
Location: policies/decision-log-policy.md:46-52 (collision-resolution reasoning), 59-60 (the parenthetical "If that reverse lookup ever gets tedious, a `Superseded-by:` back-reference is the obvious addition — not built now"), 41 ("a 'who' field would be noise, so there is none"); session kind absent throughout.
Evidence: Inferred by reading against criteria 6 and 7. Distinguished from the collision *rule* at 47-49, which is an instruction and stays.
Consequence: Criterion 6 and 7. Modest here — the file is 72 lines and the rationale is a small fraction of it, so this does not put the file over an attention budget the way it does in policies/document-metadata-policy.md. The session-kind omission is the sharper half: appending to the log is decision-session work, consulting it is both, and the file says neither, so an execution session cannot tell whether the append procedure is addressed to it.
Fix: Cut 59-60 and the trailing clause at 41; compress 50-52 to the rule without its justification. Add one line under the title naming the session kind, on the pattern of context-sets/testing-and-verification.md:11 ("Rules for execution sessions.").
