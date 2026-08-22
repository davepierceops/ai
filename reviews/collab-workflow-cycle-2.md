# Review: context-sets/collab-workflow.md — cycle 2

Verdict: changes-required
Reviewed: `context-sets/collab-workflow.md` @ `7310937`
Reviewer: Spec Reviewer Agent (Pass 1, cycle 11a)
Date: 2026-08-21
Scope: the whole file — frontmatter and all three body sections — against all
ten criteria of `docs/global-context/review-rubric.md` @ `7310937`. Cycle 1 was
a narrow self-review of the C2 touch-rule edit and explicitly not a first full
gate; this is that gate. Criterion 4 judged line-by-line against
`docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, and `operating-model.md` @ `7310937`, and additionally against
`context-sets/spec-and-change-discipline.md` @ `7310937`, which duplicates one
of this file's three sections near-verbatim. Mechanical sweeps run (verified by
running `grep`): retired terms, vendor and model names, path-shaped references.
`bin/bundle-methodology`, `decisions/log.md` `DEC-000140`, and `CLAUDE.md` read
to establish retirement cost.
Cross-checked: `docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `operating-model.md`, `context-sets/spec-and-change-discipline.md`,
`context-sets/base.md`, `bin/bundle-methodology`, `decisions/log.md`, `CLAUDE.md`,
`git remote -v`
Not inspected: `skills/spec-review-cycle.md` §Use when was read for the schema
and filename convention only; whether it fully states the two-mode distinction
this file's L19–21 draws was **not** verified, and C2's fix depends on that. The
existence and current state of a `davepierceops/ai` repository was not checked
(C7 reports only what `git remote -v` shows for the repository this file is
in). No claim is made about `OPEN-ITEMS.md`'s contents.
Findings: 9 — 5 blocking, 2 non-blocking, 2 observations
Prior cycle: `reviews/collab-workflow-cycle-1.md`
Dave should inspect: C1's retirement is blocked behind a decision you own —
`DEC-000140` fixes this file into the `bin/bundle-methodology` spine, so
retiring it amends a decision. And C4 surfaces a live contradiction between this
file and Decision Layer rule 9 about whether `OPEN-ITEMS.md` should exist at
all; that is a judgment call, not a drafting error.

## Criterion 10 — disposition

**retire.**

The file has three sections and each is stated elsewhere in the same bundle:

- **Document review** (L17–32) is Decision Layer rule 10, plus a vendor-specific
  UI description. Rule 10 @ `7310937` reads: "The thing under review is an
  artifact, separate from the discussion of it. One document at a time. 'Ship'
  or 'done' advances exactly one step." That is this section's entire operative
  content (C2).
- **Authorship** (L34–42) is `context-sets/spec-and-change-discipline.md:160-165`
  near-verbatim, and Core rule 2 underneath both (C3).
- **Session handoff** (L44–54) is `OPEN-ITEMS.md` — duplicated at
  `context-sets/spec-and-change-discipline.md:173-184` and in tension with
  Decision Layer rule 9 (C4) — plus the baton, which is Core §Vocabulary (C5),
  plus a stale repository name (C7).

Nothing survives. This is not a file that needs cutting down; there is no
residue to cut down to.

**Cost of the retirement, and why it is not merely a document edit.** The file
is named in four places:

1. `bin/bundle-methodology:28` — the hard-coded `SPINE` list. `render()` raises
   `cli.ToolError` (exit 3) on a missing blob, so this fails loudly, which is
   the good case.
2. `decisions/log.md` `DEC-000140` (L240–242) — the spine is fixed *by decision*,
   not just by code. Retiring the file amends a landed decision.
3. `CLAUDE.md` — the adapter's "Collaborative document review" section names
   this file as "the portable source of truth for how Dave and agents
   collaborate during document authorship and review" and says "The rules there
   apply in full." Retiring the file without editing `CLAUDE.md` leaves the
   adapter pointing at nothing.
4. `context-sets/spec-and-change-discipline.md:106` — a `bin/bundle` in-body
   edge.

The `CLAUDE.md` pointer is the one that bites: it does not fail loudly, and it
is the sentence that made this file load-bearing in the first place. Its
replacement is Decision Layer rule 10 — but the Decision Layer is
`audience: [all-decision-roles, human]` and `CLAUDE.md` currently reaches this
material through `context-sets/`, so the repoint is a real edit, not a
find-and-replace.

## Criteria 1–9 — summary

| # | Criterion | Result |
| --- | --- | --- |
| 1 | Bundles are the product | fail — C2, C5, C6, C7 |
| 2 | `audience:` is the selector | fail — C8 |
| 3 | No path references | fail — C5, C6 |
| 4 | Core states it → remove it here | fail — C2, C3, C4, C5 |
| 5 | Agent instruction, not authoring principle | pass |
| 6 | Instructions, not rationale | pass |
| 7 | Session kind is explicit | fail — C8 |
| 8 | Tiers, not model names | fail — C2 |
| 9 | Filenames are `<descriptor>-<timestamp>` | pass — `OPEN-ITEMS.md` is a convention-named file, which criterion 9 permits |

## Counts (instruction 4)

- **Rules restated from Core / Decision Layer / LEXICON / operating-model:** 8
  across 3 of 3 body sections. By section: Document review 3 (Decision Layer
  rule 10 ×3 clauses) plus Core rule 2; Authorship 2 (Core rule 2,
  `operating-model.md` §Release gate two-tier); Session handoff 2 (Core
  §Vocabulary §Baton, Core rule 4). Plus 2 sections duplicated from
  `context-sets/spec-and-change-discipline.md` rather than from the foundation.
- **Path-shaped references:** 5 — `skills/spec-review-cycle.md` (L20),
  `context-sets/spec-and-change-discipline.md` (L42), `OPEN-ITEMS.md` (L47),
  `LEXICON.md` (L51), `davepierceops/ai` (L53, a repository rather than a file
  path, counted here because it is the same class of unreachable-from-a-bundle
  reference).
- **Vendor and model names:** 1 — "Claude" (L32). The artifact-pane / left-pane
  / right-pane description at L20 and L25–26 is vendor-specific without naming
  the vendor.
- **Retired terms:** 1 — "tracked" (L46). See C9 for why this one is reported
  differently from the others.

## C1 — blocking
Claim: The file does not earn its place; all three of its sections are stated
elsewhere in the same bundle and no residue survives.
Location: `context-sets/collab-workflow.md` (whole file)
Evidence: Verified by reading — each section mapped against the four foundation
files and `context-sets/spec-and-change-discipline.md` @ `7310937`; the mapping
is enumerated in C2–C5. Verified by running: `grep` sweeps for retired terms,
vendor names, and path-shaped references; `git remote -v` for C7;
`grep -n SPINE bin/bundle-methodology` and `grep -n DEC-000140 decisions/log.md`
for the retirement cost.
Consequence: Beyond the bundle budget, the specific harm is that `CLAUDE.md`
designates this file as the source of truth for document collaboration while
Decision Layer rule 10 states the same rules more tersely and with more
authority. A reader following `CLAUDE.md` lands on the derived copy and takes it
as canonical; a reader given the Decision Layer takes that as canonical; the two
have already drifted, in that this file's L26–31 adds a four-step
"mark complete, load the next, begin the review — all in one response"
sequencing that rule 10 does not have.
Fix: Retire the file. Execute the four repoints listed in the criterion-10
disposition above. Take the L29–31 multi-document sequencing into Decision Layer
rule 10 first, if it is wanted — it is the one clause in the file that is
neither a duplicate nor a defect, and it would be lost otherwise.

## C2 — blocking
Claim: §Document review restates Decision Layer rule 10 and adds a
vendor-specific UI description that a bundled agent cannot act on.
Location: `context-sets/collab-workflow.md:17-32`
Evidence: Verified by reading. This file L24–31: "Put the document under review
into an artifact (right pane); discuss in chat (left pane). One document at a
time. Do not advance to the next document until Dave signals done. In a
multi-document review, when Dave says 'ship', 'done', or equivalent: mark the
current document complete, load the next document into the artifact, and begin
the review." Decision Layer rule 10 @ `7310937`: "**The thing under review is an
artifact, separate from the discussion of it.** One document at a time. 'Ship'
or 'done' advances exactly one step." L32 ("Claude drafts edits; Dave approves
in the artifact before anything is locked") is Core rule 2.
Consequence: The rule is stated twice, and the copy here is expressed as
two-pane geometry. An agent in any surface without a right pane — every
execution session, and any decision session outside that one product — is given
an instruction it cannot execute, which puts it into Core rule 11 over a
presentation detail. Rule 10's phrasing is surface-independent and says the same
thing.
Fix: Delete L17–32. Carry L29–31's multi-document sequencing into Decision Layer
rule 10 if it is wanted; drop the pane geometry and the vendor name entirely.
Related: C1

## C3 — blocking
Claim: §Authorship duplicates `context-sets/spec-and-change-discipline.md:160-165`
near-verbatim.
Location: `context-sets/collab-workflow.md:36-42`
Evidence: Verified by reading, both @ `7310937`. This file: "Agents dispose of
routine changes; Dave disposes of judgment calls. Agents draft, review, and
merge the routine class on evidence, without asking. What returns to Dave is the
release decision for the consequential class and the agreement of any canonical
document. Drafts are produced for his agreement, not for his line-by-line
verification." `context-sets/spec-and-change-discipline.md:160-165`: identical
except for one inserted clause ("— specs and methodology documents alike") and
its trailing `boundaries/human-review-boundary.md` citation.
Consequence: The same paragraph in two context sets, both `audience: [all-roles,
human]`, both reachable from `base`. They have already drifted by one clause. A
reader who notices cannot tell whether the missing clause here is a deliberate
narrowing or an oversight, and Core rule 9 forbids resolving it by taking the
longer one.
Fix: Delete L34–42. The paragraph is retained at
`context-sets/spec-and-change-discipline.md:160-165`, which is where its
cross-references already live. The closing pointer at L40–42 ("For operating
habits governing how questions are asked … see
`context-sets/spec-and-change-discipline.md`") goes with it.
Related: C1

## C4 — blocking
Claim: The `OPEN-ITEMS.md` bullet is duplicated in
`context-sets/spec-and-change-discipline.md`, and both contradict Decision Layer
rule 9.
Location: `context-sets/collab-workflow.md:46-47`
Evidence: Verified by reading. This file: "Open items, deferred decisions, and
outstanding fixes are tracked in `OPEN-ITEMS.md` and flushed at the end of each
work session." `context-sets/spec-and-change-discipline.md:173-184` states the
same obligation with four named checkpoints. Decision Layer rule 9 @ `7310937`:
"**State is computed, never maintained.** Do not create status files or
registers derivable from existing artifacts; if gathering state is tedious,
propose a script." Verified by running: `ls OPEN-ITEMS.md` resolves — the file
exists.
Consequence: This is a genuine conflict, not a duplication. `OPEN-ITEMS.md` is a
maintained register of open items. Decision Layer rule 9 prohibits creating
maintained registers where the state is derivable, and rule 9 is a Decision
Layer rule, so it does not resolve by Core's precedence clause. An agent given
both is told to maintain a register and told not to maintain registers. Core
rule 9 then requires it to surface the disagreement rather than pick one —
correct behaviour, but it will happen on every session that reads both.
Fix: Not a drafting fix. Either open items are *not* derivable from existing
artifacts, in which case Decision Layer rule 9 needs a stated carve-out naming
`OPEN-ITEMS.md`; or they are, in which case the register should go and rule 9's
"propose a script" applies. Dave's call. Whichever way it goes, the statement
belongs in one file — `context-sets/spec-and-change-discipline.md`'s version is
the fuller one — and this bullet is deleted regardless.
Related: C1, C3

## C5 — blocking
Claim: The baton bullet restates Core §Vocabulary and reaches for `LEXICON.md`
by path to do it.
Location: `context-sets/collab-workflow.md:48-52`
Evidence: Verified by reading. This file: "travels as a **baton**, the artifact
one decision session hands its successor (`LEXICON.md`). A baton is not a
directive: it goes to another decision session, never to an execution session."
`docs/global-context/core.md:54` @ `7310937`: "**Baton** — the artifact a
decision session hands its successor decision session: the package of unfinished
responsibility — state, open questions, decisions in flight — that lets the
receiver continue without the conversation that produced it. A baton passes
between decision sessions only; a directive hands work to an execution session.
The two never blur." Both clauses of this file's version are in Core's.
Consequence: Core carries `order: 0` and `audience: [all-roles, human]`, so it
is the first file in every bundle this one appears in. The definition is read,
then read again eighty lines later in weaker form, with a parenthetical pointing
at a third file the reader was not necessarily given. Note also that the
parenthetical cites `LEXICON.md`, but the definition is in Core — `grep` over
`LEXICON.md` @ `7310937` finds "baton" only inside the `Prompt` retirement
entry, not as a term of its own. The citation is wrong as well as forbidden.
Fix: Delete L48–52.
Related: C1

## C6 — non-blocking
Claim: Two more path-shaped references.
Location: `context-sets/collab-workflow.md:20,42`
Evidence: Verified by running — `grep` returns `skills/spec-review-cycle.md`
(L20) and `context-sets/spec-and-change-discipline.md` (L42); `ls` confirms both
resolve, so these are live `bin/bundle` edges, not dangling references.
Consequence: Criterion 3. L20 is the load-bearing one: the two-mode distinction
it draws — interactive co-authoring versus reviewer-gated cycle, and
"documents do not go into artifacts in that mode" — is stated *only* by pointing
at another file. An agent given this file alone knows a second mode exists and
nothing about it.
Fix: Both go with the file under C1. But L20's two-mode distinction must be
confirmed present in `skills/spec-review-cycle.md` before deletion — that
verification was not run here (see Not inspected). If it is not there, it is the
second clause besides L29–31 that has to be rehomed rather than dropped.
Related: C1, C2

## C7 — non-blocking
Claim: The session-state bullet names a repository that does not match this
repository's remote.
Location: `context-sets/collab-workflow.md:53-54`
Evidence: Verified by running. The file says "Session state is committed to the
`davepierceops/ai` repository." `git remote -v` @ `7310937` returns
`https://github.com/davepierceops/fiducial.git` for both fetch and push. Verified
by reading: `davepierceops/ai` appears elsewhere in the tree only in historical
records — `docs/cycles/` directives, `docs/research/` findings,
`docs/global-retro-inbox.md` — where a past name is correct. This is the only
live governing document asserting it. Whether `davepierceops/ai` still resolves
was not checked; GitHub redirects renamed repositories, so it may well work and
still be wrong.
Consequence: A governing document names the wrong repository. The instruction
still functions today by redirect, which is worse than a clean break — it will
keep working until it silently does not, and Core rule 13 ("a changed fact
changes everywhere it appears") was not applied at the rename.
Fix: Goes with the file under C1. The residual rule — "Do not rely on chat
history as the sole record of decisions made" — is Core rule 4 and needs no new
home. Separately, and outside this cycle's scope: `git grep -n 'davepierceops/ai'`
should be run across the tree and each hit classified as historical record
(leave) or live assertion (fix).

## C8 — observation
Claim: No `order:`, and no session kind stated, in a file that is entirely
decision-session material.
Location: `context-sets/collab-workflow.md:1-9`
Evidence: Verified by reading. `audience: [all-roles, human]` — both reserved
values, valid — but the whole file governs decision sessions: reviewing
documents with Dave in a two-pane surface, Dave disposing of judgment calls,
handing a baton to a successor decision session. No execution-session rule
appears in it. `docs/global-context/decision-layer.md:4` carries
`audience: [all-decision-roles, human]` and `:10` states "Execution sessions
never receive this file" — the correct pattern for this content.
Consequence: Criterion 2 and criterion 7 together. `audience: [all-roles]` puts
decision-session-only material into execution bundles, which is exactly the
selection error the Decision Layer's audience value exists to prevent.
Fix: Dissolves with the file under C1 — and the fact that its correct audience
is the Decision Layer's is further evidence that the Decision Layer is where its
surviving clauses belong.
Related: C1, C2

## C9 — observation
Claim: A retired term appears, in a sense `LEXICON.md` does not carve out.
Location: `context-sets/collab-workflow.md:46`
Evidence: Verified by running — `grep -niE '\btracked\b'` returns L46: "Open
items … are tracked in `OPEN-ITEMS.md`." `LEXICON.md:69-70` @ `7310937`:
"**Track** — retired 2026-08-21. A directive states route and model tier; there
is no third part."
Consequence: The retirement as written is bare — it gives the reason (the
directive's third part) but states no scope, so on a literal reading the
ordinary verb "keep a list of" is also retired. That literal reading is almost
certainly not intended: `operating-model.md:143` ("stale flags are tracked as
debt") and `:155` ("error budget consumption") use it the same way, in a
document already through Pass 1. The defect is in the retirement entry, not
here.
Fix: `LEXICON.md`'s `Track` entry needs the carve-out its `Prompt` entry already
models — "*Not covered by this retirement:* … a different word in a different
domain, and it keeps its ordinary meaning." Without it, three Pass-1 documents
are in technical violation and every future sweep re-raises them. This bullet is
deleted under C4 either way, so no edit is owed here.
Related: C4
