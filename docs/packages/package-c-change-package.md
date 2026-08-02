# Change Package — Package C: Ceremony Reduction (F3 + F5 + F7)

Directive: `docs/cycles/streamlining-directive.md` — F3, F5, F7, batched into
one review cycle on the shared rationale of ceremony reduction with no routing
change (Execution sequence item 3).

**Tier: routine.** No routing change, no code, no agreed document edited. F7
required this package because of MANIFEST's registry role; it is produced for
that reason, not because a gate is pending.

---

## 1. Intent

Three documents were carrying obligations that cost more than they returned:

- **F3** — review artifacts had no schema, so a clean pass cost as much to
  write as a substantive one. A review format expensive to write is a review
  that gets skipped.
- **F5** — a pending gate had to be stated twice, in chat and in a GitHub
  issue. Two copies of the same evidence drift, and the chat copy does not
  survive the conversation.
- **F7** — `MANIFEST.md` maintained a file registry and a changelog that git
  and the metadata policy already derive. Both had already drifted.

## 2. What changed

| File | Change |
| --- | --- |
| `skills/spec-review-cycle.md` | **F3.** Adds "Review artifact schema": verdict-first header, structured finding entries, prose permitted but not default. |
| `policies/commit-and-change-control-policy.md` | **F5.** The `human-gate` issue becomes the canonical pending-gate record; chat reduces to one line plus an explicit ask. |
| `MANIFEST.md` | **F7.** Sheds the file registry and the changelog obligation; history frozen under a tombstone; bundle definitions retained with a concrete supersession condition. |
| `README.md` | Removes the stale `Tree version: v0.4` block. See §4 — this is a conformance fix, not scope creep. |
| `AGENTS.md` | Adapter contradicted the revised F5 policy. See §5. |
| `COLLAB-STATE.md` | Marks decision A3 superseded in place. |
| `TREE.txt` | **Deleted.** See §6. |
| `OPEN-ITEMS.md` | Closes the MANIFEST version item; opens the `bin/bundle` supersession item. |

## 3. Review

One gate review, by an independent Spec Reviewer agent, against the directive
and the agreed metadata policy. **Verdict: `changes-required` — 8 blocking, 9
non-blocking, 3 observations.** Every blocking finding is fixed; the material
ones:

- **The `human-gate` issue had no degraded mode.** F5 as first drafted made the
  issue the sole canonical record with no path when GitHub is unreachable —
  and the directive authorising this work was itself delivered as a file
  *because MCP GitHub was unavailable that session*. The policy now states the
  fallback: the chat statement carries the full body, and the change does not
  release until the issue exists.
- **F5 had dropped the explicit ask.** The old text required asking for a
  go/no-go; the rewrite reduced chat to a notification. The section still ends
  "Absence of a response is not a go" — which only holds if someone was asked.
  Restored.
- **`AGENTS.md` still carried the superseded two-step procedure.** Under
  `policies/source-of-truth-policy.md` an adapter contradicting a policy is a
  **hard stop**. The change would have shipped one. This is the same defect
  class the executor caught in README, one file over, and missed.
- **The verdict word `agreed` was the wrong word.** `agreed` is the repo's
  standing verb for a decision only Dave makes, and
  `roles/spec-reviewer-agent.md` forbids the reviewer from making it. The enum
  is now `ready | ready-with-findings | changes-required`. The reviewer hit this
  "in the first five seconds of writing."
- **The schema conflicted with two documents that already specify review
  outputs.** It now states that it governs the *artifact* while the role doc and
  the review policy govern the *review*, with a field mapping, and adds the
  `Dave should inspect` field that `policies/agent-review-policy.md` requires.
- **The findings template hardcoded `Findings: none`.** Followed literally,
  every review with findings would declare it has none, directly above its
  findings. The first mechanical user of the schema would have produced a
  self-contradicting document.

## 4. The README fix — stronger grounds than first claimed

The executor added `README.md` to the package as a consequence of F7 and asked
the gate to rule on whether that was scope creep. The gate's answer was that it
was not discretionary but **mandatory**, on grounds the executor had not found:

`policies/document-metadata-policy.md` — the only `agreed` document in the repo
— requires that removing the `Tree version` line land in the same change package
as the agreement, "the repo never holds both conventions as canonical." Commit
`0230e11` removed MANIFEST's line and left README's, which claimed the tree
version was "the single source for what's current." **The repo has been in
violation of that clause since, and two review cycles passed over the package
without catching it.**

Recorded because the lesson is not about README: a conformance clause was
written, agreed, reviewed twice, and silently broken by the change that was
supposed to satisfy it.

## 5. Deviations from the directive, recorded rather than silent

**F7 said MANIFEST retains "bundle definitions and assembly notes."** The
assembly notes were a single line — "Generated initial document set." — carrying
nothing git does not. They are not retained. MANIFEST says so in place.

**The directive's deferred `bin/bundle` supersession item is withdrawn, on a
false premise.** This is a correction to the directive itself, not to its
execution, and it is the most substantive thing in this package.

The directive deferred "`bin/bundle` superseding MANIFEST bundle definitions —
after F4 lands and closure output is trusted." F4 landed. The premise does not
survive contact with the tool. Measured against "Spec chat" (`base` +
`spec-and-change-discipline` + `ai-native-engineering`):

Measured at `d778813` + the Package C working tree:

| invocation | result |
| --- | --- |
| unbounded closure from `spec-and-change-discipline` | **53 paths**, all 6 context-sets, plus `OPEN-ITEMS.md` and `MANIFEST.md` itself |
| `--max-depth 1` | 2 context-sets — misses `ai-native-engineering` |
| any depth | never 3 |

That path count is a **dated measurement and lives only here.** It does not
appear in MANIFEST or `OPEN-ITEMS.md`, for reasons §6 explains — it moved twice
during this package.

The cause is **two failures in opposite directions**, and this is a correction
of record: cycles 2 and 3 attributed it to the `depends-on` graph alone ("the
graph is a star"), which is half the mechanism. `bin/bundle` walks two graphs.
`depends-on` is too *sparse* — every context-set points only at `base`. In-body
citations are too *dense* and not curatorial — `ai-native-engineering` is
reached only at depth 2, and not via `depends-on` at all; it arrives as a
citation inside `policies/commit-and-change-control-policy.md`. Context-set
count by depth: 2, 4, 6.

The omission mattered: the partial version points at a repair that does not
work. A reader told the cause is a sparse `depends-on` graph would reasonably
try enriching it — and with the full mechanism stated, that route fails on its
own terms before the co-selection argument is even needed. The reviewer
identified this as their own error from cycle 2, adopted here in good faith and
propagated into five files.

`bin/bundle` computes what a document *cites*; a bundle is a judgment about
what a conversation *needs*, and that judgment lives in the prose
`include-when:` field. **The two are complementary, not successive.** MANIFEST and `OPEN-ITEMS.md` now say so, and MANIFEST's
self-description as a temporary file awaiting automation is removed.

Found by the gate, in the fix to its own earlier finding: cycle 1 flagged the
supersession condition as unactionable, the executor replaced it with a
*concrete* condition, and cycle 2 found the concrete condition unsatisfiable.
The vague version was at least honest.

**`AC-B-10`–`AC-B-13` remain unimplemented** from Package B, per Dave's
confirmation that current shim precedence stands.

## 6. `TREE.txt`, deleted

Not named by F7, but the gate found that cycle 2 **explicitly deferred it to
"the next checkpoint,"** and the MANIFEST rewrite is that checkpoint. It fired
without honouring the deferral.

Measured: 49 entries against 91 tracked files, missing all of `bin/`, `docs/`,
`reviews/`, and two documents added in July. It is `git ls-files` with a
maintenance obligation and no maintainer — the exact class F7 removes. Deleting
it rather than regenerating it is the only outcome consistent with F7's own
reasoning.

**One stale mention is deliberately left.** `policies/document-metadata-policy.md`
lists `TREE.txt` in its out-of-scope set. That document is `agreed`, so
correcting a cosmetic mention would trigger a full review cycle. The mention is
inert — an out-of-scope list naming a nonexistent file excludes nothing. It is
tracked in `OPEN-ITEMS.md` to ride the next cycle that opens that document for a
substantive reason, and it is a worked example of the cost F6 (Package D) exists
to reduce.

## 7. Evidence

- `bin/check-frontmatter --all`: **0 findings**, 38 files matched.
- The two edited in-scope documents are `draft`, so the hook correctly did not
  flip them. Verified: status unchanged on both.
- **The F3 schema was dogfooded before it landed.** The gate review was written
  in it, as its first user, and reported back where it fought. Four defects came
  out of that alone — the verdict-word collision, the hardcoded `Findings:
  none`, `Scope:` being too small for a cross-document review (now split into
  `Scope` / `Cross-checked` / `Not inspected`), and the missing `Dave should
  inspect` field. A schema reviewed only by reading would have shipped all four.

## 8. Known gaps

- The schema's `Related:` field and the instruction to order `blocking` entries
  by weight came from the reviewer's usage feedback; neither has been exercised
  by a second user yet.
- `bin/bundle` supersession is now conditioned concretely but the comparison has
  not been run.
- Adapters (`CLAUDE.md`, `.claude/**`) were checked for the F5 contradiction;
  `CLAUDE.md` never carried the two-step text. `.claude/agents/README.md` and
  `.claude/skills/README.md` still carry `Status: placeholder` lines, outside
  frontmatter scope by design and left alone.

## 8b. The rule this package produced

Three gate passes over the same nine files produced one finding general enough
to outlive the package, and it came from a defect the executor introduced while
fixing a defect the gate had found:

> **A derived measurement may live in a dated record — a change package, a
> review artifact, a commit message — but not in canonical text.** Canonical
> text has no date; the measurement does.

The worked example: cycle 1 found the `bin/bundle` supersession condition
unactionable ("trusted in practice" — no criterion, no owner). The executor
replaced it with a *concrete* condition. Cycle 2 found the concrete condition
unsatisfiable, and noted the vague version had at least been honest. The
executor then wrote the measured closure count — 51 paths — into MANIFEST,
`OPEN-ITEMS.md`, and this file. Cycle 3 measured **53**.

It moved because of a fix made in this same package: trimming MANIFEST's
parenthetical to cite `§5` of this document added a citation, which pulled two
more documents into the closure. `MANIFEST.md` is *inside* the closure it was
reporting. The number drifted before the commit, in the paragraph arguing that a
copied derivable fact drifts and then lies.

This is the same principle F7 applied to the file registry, one level down —
and the reason it had to be rediscovered is that F7 removed a *list* and nobody
noticed a *count* is the same kind of thing. Two other instances in this
package: this document counted `TREE.txt`'s lines while deleting `TREE.txt`, and
a review artifact quoted a count that the act of committing it changed.

Related corrections of record: cycle 1's B6 says `TREE.txt` had "48 listed";
the actual count was 49. That figure is left standing inside the reviewer's
artifact — correcting a reviewer's arithmetic inside their own document would
make it the executor's document — and is corrected here instead.

## 9. Handoff — debt this package deliberately did not touch

Two `OPEN-ITEMS.md` entries are **factually wrong and are not Package C's to
close**: "Build this repo's frontmatter-enforcement hook" and "Migrate existing
docs to YAML frontmatter". Both still end "Blocked on the policy reaching
`agreed`". The policy is agreed, the hook is live, and the migration shipped in
Package B.

Closing another package's items inside this one is the scope habit that produced
the `TREE.txt` miss in the first place, so the entries are untouched. But the
scope argument covers *closing* — it does not license leaving a live tracker
asserting a blocker that no longer exists, and since A and B are finished nobody
will revisit them by default. Recorded here so the debt has a carrier: **whoever
next opens `OPEN-ITEMS.md` for a substantive reason should strike both.**

## 10. Remaining sequence

**Package D** — F6 alone, a full spec-review cycle against the agreed
`policies/document-metadata-policy.md`. It cannot use the expedited path it
introduces. It is also now the natural home for the inert `TREE.txt` mention in
§6, since it opens that document anyway.
