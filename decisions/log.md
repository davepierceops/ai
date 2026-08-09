# Decision Log — davepierceops/ai

Append-only record of methodology decisions, per
`policies/decision-log-policy.md`. Newest last. Entries are never edited or
deleted; a reversal is a new entry whose `Supersedes:` names the old ID.

## DEC-000010 — Doc-only cycle is a sanctioned route to `agreed`
Date: 2026-08-06
Decision: A co-authored methodology/governance document may reach `status:
agreed` through the doc-only cycle — authored or edited together in the artifact
pane, at least one consistency sweep, and Dave's verbal sign-off — recorded as an
entry in `reviews/expedited-log.md`, with `last-reviewed` citing the log and the
reviewed SHA.
Context: Entry conditions — the document is methodology/governance prose (any
format, not a program meant to run); it is co-authored in the artifact pane;
Dave asks for the cycle and agrees. The metadata policy previously sanctioned
only the full reviewer cycle and the expedited path, neither of which fits a
co-authored, multi-section, or new prose document.

## DEC-000020 — Doc-only cycle overrides metadata-policy route-to-`agreed` limits
Date: 2026-08-06
Decision: The doc-only cycle overrides the expedited-path eligibility conditions
in `policies/document-metadata-policy.md` (the ≤10-line body cap, the single
in-scope-file rule, and the gate/enforcement-doc exclusion) wherever they would
block a co-authored, signed-off document from reaching `agreed`. Dave is the
final arbiter of policy; this ruling governs over the metadata-policy text until
that text is amended to describe the doc-only route.
Context: `policies/decision-log-policy.md` is a new multi-section policy, so it
fails the expedited eligibility conditions, yet it was co-authored and signed
off under the doc-only cycle. `bin/flip-agreed` enforces only a frontmatter-only
transition and that the cited SHA resolves to a log entry — not the eligibility
conditions — so this agreement lands cleanly. Amending the metadata-policy prose
is queued as follow-up.

## DEC-000030 — Doc-only cycle excludes review-regime documents; they keep independent review
Date: 2026-08-06
Decision: Narrows DEC-000020. The doc-only cycle still overrides the expedited
path's ≤10-line body cap and single-in-scope-file rule for co-authored
documents, but it does not override the gate/enforcement-doc exclusion.
Documents that state a gate, a hard stop, or an enforcement rule governing how
work is reviewed, agreed, or released — the class defined in
`policies/document-metadata-policy.md`, "Expedited return to `agreed`",
condition 3 — reach `agreed` only through the full reviewer-gated cycle
(`skills/spec-review-cycle.md`), even when co-authored. The doc-only cycle's
verbal sign-off is not sufficient for that class.
Context: DEC-000020 overrode the gate-doc exclusion alongside the size and
single-file limits, which was too broad. The doc-only cycle trades away
independent review, and the one class where independence is load-bearing is the
set of documents that define the routes to `agreed`: a self-serving change there
would propagate to every future agreement with only its author having read it.
Prompted by the pending `document-metadata-policy.md` amendment, which under
this entry routes through the full cycle. This does not unwind the agreement of
`policies/decision-log-policy.md` under DEC-000020 — that document states a
working-practice obligation (consult the log), not a route to `agreed`, so it
falls outside the class this entry protects. Size and multi-file freedom are
retained for all other co-authored prose.
Supersedes: DEC-000020

## DEC-000040 — Doc-only cycle is single-document; multi-file override withdrawn
Date: 2026-08-06
Decision: Supersedes DEC-000030. The doc-only cycle overrides the expedited
path's ≤10-line body cap for co-authored documents — a co-authored document may
be any size — but does not override the single-in-scope-file rule: a doc-only
agreement covers exactly one in-scope document, as the expedited path does.
Several documents co-authored in one session are agreed as separate, sequential
agreements. The gate/enforcement-doc exclusion carried by DEC-000030 stands
unchanged: documents that state a gate, a hard stop, or an enforcement rule
governing how work is reviewed, agreed, or released reach `agreed` only through
the full reviewer-gated cycle, even when co-authored.
Context: DEC-000030 also overrode the single-file rule, letting one content
commit agree multiple documents under one shared content SHA. The cycle-11
re-gate of `document-metadata-policy.md` (finding B1) found the shared SHA
defeats the single-entry pointer resolution `### The record` relies on —
`bin/flip-agreed` / `bin/aimeta/expedited.py` match a `last-reviewed` pointer on
SHA alone, so document B's pointer is satisfied by document A's entry: a false
claim of review in the one case the SHA is deliberately shared. Rather than make
the checker path-aware (a `bin/` change), the single-file rule is restored; size
freedom is retained.
Supersedes: DEC-000030

## DEC-000050 — decision-log-policy.md sits outside the gate-document class
Date: 2026-08-06
Decision: `policies/decision-log-policy.md` is not a gate/enforcement document in
the sense of the doc-only cycle's condition 3 — it states a working-practice
obligation (consult the log), not a route to `agreed` or a gate over how work is
reviewed, agreed, or released. Its revisions are eligible for the doc-only cycle
when co-authored, and its agreement under DEC-000020 stands.
Context: DEC-000030 recorded this carve-out; DEC-000040 superseded DEC-000030 and
carried the gate-doc exclusion forward but not this classification, so under the
decision log's whole-entry supersession rule the carve-out went dead. This entry
restates it as a live decision. Not a supersession — DEC-000040 remains fully in
force; this adds back only the dropped classification.

## DEC-000060 — LEXICON.md brought into metadata in-scope set by owner override
Date: 2026-08-07
Decision: The single-line additive edit naming `LEXICON.md` in the in-scope set
of `policies/document-metadata-policy.md` is agreed without a review cycle, on
owner authority. That document is agreed and its in-scope set is an enforcement
rule, so the doc-only cycle's condition 3 would otherwise force a full review
cycle; the owner overrides condition 3 for this revision only. This does not
create a general owner-flip route for enforcement-rule documents.
Context: The edit is additive — it brings a governed definitional document under
enforcement it already claims via its frontmatter — so it cannot blind
enforcement of itself. `bin/check-frontmatter --all` was verified green with
LEXICON in scope. A full multi-agent gate is disproportionate to a one-line
additive scope change.

## DEC-000070 — ACs are an execution-time input, not pinned by the decomposition doc
Date: 2026-08-07
Decision: The tranche decomposition doc pins the PRD/TRD SHAs it derives from; acceptance criteria are consumed at package execution time and are not part of what the decomp pins. Staleness-check strictness (block vs. flag on spec movement past the pin) is left unsettled, to be learned by doing.
Context: Raised while adding a spec-drift guard to roles/chief-of-staff.md. The decomp is a derived artifact and can drift from canonical specs; pinning the PRD/TRD SHA gives a staleness signal. ACs sit between agreed spec and execution and are better re-read live than pinned into a derived doc that later work references in place of the spec.

## DEC-000080 — Flakiness-workaround directives retained; Track B auto-propose trigger kept as contention detector
Date: 2026-08-07
Decision: An audit of the "special MCP-handling" directives — remote-write
verification, the spec-review-cycle small-writes rule, remote/sync hygiene, and
the Track B auto-propose-after-two-failures trigger — removes none of them. The
trigger is retained specifically as a contention detector: its two-failure fire
is how contention between concurrent Claude Desktop chats gets noticed, and that
diagnostic value holds independent of whether the underlying cause is random
flakiness or contention.
Context: GitHub MCP is not fixed; the real failure mode is concurrent-Desktop
contention, which Track B sidesteps. An audit (per the global-retro-inbox
2026-08-04 entry) tested whether any directive existed only to work around
now-nonexistent flakiness and found none: remote-write verification is
transport-general evidence discipline, and the spec-review-cycle small-writes
rule rests on the decision/execution layer boundary. The trigger was nearly cut
as cruft this session before Dave noted it had already surfaced an accidental
contention event once; skills/directive-dispatch.md frames it only as a Track B
on-ramp, so its keep-reason is recorded here.

## DEC-000090 — Track B carries the sync step in the echoed line; the sync block is Track A only
Date: 2026-08-08
Decision: `LEXICON.md`'s `Sync block` is narrowed to precede every **Track A**
execution block, not every execution block. Track B has no sync block: it carries
the sync step in the echoed dispatch line, and what that line asks for is a
working-tree-current check in the same clone — HEAD at the echoed SHA, no
uncommitted edits to the files in scope — not a remote fetch. The alternative
direction, restoring a sync command block to the Track B sequence, is rejected.
Context: Trivium cycle-1 gate, `reviews/LEXICON-cycle-1.md` B1 ≡
`reviews/directive-dispatch-cycle-1.md` B1 — two canonical documents disagreed
with no tiebreak, `81bd2de` having dropped the standalone Track B sync block. The
tracks differ for a reason worth stating: Track B is same-machine and
commit-not-push, so the executor runs in the clone that already holds the
unpushed commit. A Track A remote fetch has no remote to fetch the directive from
and could check out a tree lacking it. This closes `OPEN-ITEMS.md`'s "Sync as a
skill rather than a step inside every directive", whose proposed phrasing the
tree had already adopted ahead of its own analysis. It does **not** decide that
item's broader proposal — sync as a role-held skill so directives carry no
version-control mechanics — which is untouched and reopens on its own if wanted.

## DEC-000100 — The shell-termination rule is stated by effect, not by enumeration
Date: 2026-08-08
Decision: `skills/command-blocks.md`'s interactive-shell rule and its conformance
criterion are stated by effect — no construct that can terminate the shell the
block is pasted into — with `exit`, `exec`, `logout`, `|| { …; exit; }`, and
`set -e` named as known instances and adopting projects directed to add their
own. `skills/directive-dispatch.md`'s restatement of the same enumeration is
replaced by a pointer to that criterion, so the rule lives in one document and
cannot drift.
Context: `reviews/command-blocks-cycle-1.md` B1 ≡
`reviews/directive-dispatch-cycle-1.md` B2. `set -e` ends an interactive shell on
the next failing command exactly as `exit` does (verified by running under both
`bash -i` and `zsh -i`), and is the idiomatic opening line of a careful block —
so the enumeration that `ed7d904` added passed the construct the rule exists to
stop. Choosing effect over enumeration also settles the document against itself:
the copy-control rule at the same file already used the "known instance, not the
rule" pattern, so the document held two patterns for the same kind of rule. No
prior decision governs the enumeration — it entered in `ed7d904` with no entry —
so this reverses nothing.

## DEC-000110 — Reviewer-gated cycle directives fix route and model by class; track is required
Date: 2026-08-08
Decision: A reviewer-gated cycle directive states its **track** and its execution
block per directive, and takes **route** (fresh) and **model** (Opus 5) as fixed
by its class, stated once in `skills/spec-review-cycle.md` rather than restated
per cycle. This is a bounded exception to `skills/directive-dispatch.md`'s
all-four-every-time rule, mirrored there and in `LEXICON.md`'s `Directive`
definition so the general statement admits it rather than contradicting it.
Context: `reviews/spec-review-cycle-cycle-1.md` B1 ≡ `reviews/LEXICON-cycle-1.md`
N1. The cycle-directive format required none of route/model/track and licensed
the omission ("Everything else as needed"), while two other canonical documents
called each unstated part a defect. Route and model genuinely do not vary for
this class — one conversation per cycle with execution in a fresh session, and
directive execution over canonical documents is the row the model table already
decides — so restating them per directive adds no information. Track does vary,
so it is carried. The matching change to `bin/cycle-open`'s generated skeleton
(`:116`) is deliberately **not** in this doc cycle: it is a code change needing
acceptance criteria, tests, and a red gate, filed as its own package. Until it
ships, the author hand-adds Track, as this cycle's own directive did.

## DEC-000120 — The command-block remote rule is rewritten; `origin` was never the hazard
Date: 2026-08-08
Decision: `skills/command-blocks.md`'s "Name remotes explicitly; do not rely on
the `origin` alias" rule is replaced rather than enforced. The rule now targets
the real hazard: a sync or remote command in a pasted block names its remote and
ref explicitly, does not lean on branch-upstream configuration, and has its exit
status checked before anything downstream acts on the tree it produced. `origin`
is a valid explicit remote name and using it is fine. The false rationale — that
an auth failure surfaces as missing work rather than as an auth error — is
removed. A seventh conformance criterion is added for the rewritten rule.
Context: `reviews/command-blocks-cycle-1.md` B2 reported the rule as the one body
rule with no conformance criterion. On inspection the rule itself was unsound:
`origin` is a remote *name*, not a protocol, and a `git fetch`/`push` that cannot
authenticate exits non-zero rather than returning empty results silently. It
entered in a bulk drafting commit (`c4baefe`) with no decision or incident behind
it. Adding a criterion would have hardened an incorrect rule. The criterion
question was left to ride with the rewrite; the criterion is added because the
finding's underlying gap — a body rule invisible to the checklist a reviewer
actually runs down — survives the rewrite, and the rewritten rule is per-block
and mechanically checkable, which is the shape the other criteria have.

## DEC-000130 — Remote-write Rule 3 is about provenance; SHA abbreviation is out of its scope
Date: 2026-08-08
Decision: `policies/remote-write-verification-policy.md` Rule 3 drops "Never
abbreviate a SHA that will be used as a pointer" and keeps the provenance rule
(state SHAs read from git; never invent one), with a pointer to
`skills/directive-dispatch.md`, which carries the narrow, correctly-scoped
abbreviation rule for dispatch blocks. Complementary: the policy's Scope now
reaches the case where the agent cannot read its own write back — Track B —
where verification is the operator's and the agent reports only what the operator
reported.
Context: `reviews/remote-write-verification-policy-cycle-1.md` B1 and N1. The
abbreviation clause contradicted `policies/document-metadata-policy.md`, which is
`agreed` and contemplates abbreviated `last-reviewed` pointers, and
`bin/aimeta/expedited.py`, which is shipped specifically to normalize them
through `git rev-parse`. A draft policy contradicting an agreed one is the
serious direction: an agent holding both cannot tell which to satisfy. Rule 3's
surrounding sentences are about provenance, so the clause read as a scoping slip
rather than a disagreement, and it is dropped rather than promoted — widening it
would have been an edit to an agreed policy and to shipped tooling, and belongs
in a cycle over those.

## DEC-000140 — methodology-context-bundle: filename format, file-set rule, interim generation procedure, script deferred to tooling tranche
Date: 2026-08-08
Decision: The uploaded chat-context bundle is named
`methodology-context-bundle-<YYYY-MM-DD-HHMM>.md` — timestamped deliberately,
overriding the no-derived-metadata-in-filenames default, for project-view
version visibility (Dave). File set: the fixed decision-layer spine
(`context-sets/base.md`, `context-sets/spec-and-change-discipline.md`,
`context-sets/collab-workflow.md`, `operating-model.md`,
`roles/chief-of-staff.md`, `policies/commit-and-change-control-policy.md`) plus
every `skills/*.md` whose `audience` frontmatter contains `all-roles` or
`chief-of-staff`. The bundle pins `Source: @ <repo HEAD>` and a per-file blob
short-SHA (each file's own blob, `git rev-parse --short HEAD:<path>` — not the
repo HEAD), with `<!-- FILE n/N: path @ sha -->` separators. Building
`bin/bundle-methodology` is folded into the tooling tranche alongside the
drift-audit `bin/` check (`docs/global-retro-inbox.md`) — not built as its own
package. Until it exists, regenerate with the procedure below, which computes
the file set from the audience rule (not a hardcoded list) so a skill's
audience change or a new skill is picked up automatically.

Context: this filename format and a working generator were reached 2026-08-08
(chat "AI retro: Methodology bugs") but recorded only as an aspiration in
`docs/global-retro-inbox.md` — "should be a script." The decision and the
artifact went nowhere durable, and were re-derived from scratch the same day,
the second regen opening with "there is no generator." That re-derivation is
the drift the log exists to stop; hence this entry carries the runnable
procedure, not just a pointer.

Interim generation procedure — run from the `ai` clone root on a synced `main`;
writes the timestamped bundle to `~/code/`:

```
python3 - <<'PY'
import subprocess, glob, re, os, datetime
sh=lambda *a: subprocess.check_output(a).decode()
repo=sh("git","rev-parse","HEAD").strip()
blob=lambda p: sh("git","rev-parse","--short","HEAD:%s"%p).strip()
stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
spine=["context-sets/base.md","context-sets/spec-and-change-discipline.md",
 "context-sets/collab-workflow.md","operating-model.md",
 "roles/chief-of-staff.md","policies/commit-and-change-control-policy.md"]
def aud(p):
    m=re.search(r'^audience:\s*\[([^\]]*)\]',open(p,encoding="utf-8").read(),re.M)
    return {x.strip() for x in m.group(1).split(",")} if m else set()
skills=sorted(p for p in glob.glob("skills/*.md") if aud(p)&{"all-roles","chief-of-staff"})
files=spine+skills; N=len(files); bar="<!-- "+"="*60+" -->"
o=["# methodology-context-bundle\n",
 "**Derived artifact — do not edit.** Regenerate from davepierceops/ai; the repo is canonical.\n",
 "- Source: davepierceops/ai @ %s"%repo, "- Generated: %s"%stamp,
 "- File set: fixed decision-layer spine + every skills/*.md whose audience includes all-roles or chief-of-staff (rule; Dave 2026-08-07).\n"]
o+=["  %d. %s (blob %s)"%(i,p,blob(p)) for i,p in enumerate(files,1)]; o.append("")
for i,p in enumerate(files,1):
    o+=["",bar,"<!-- FILE %d/%d: %s @ %s -->"%(i,N,p,blob(p)),bar,"",open(p,encoding="utf-8").read().rstrip("\n"),""]
dest=os.path.expanduser("~/code/methodology-context-bundle-%s.md"%stamp)
open(dest,"w",encoding="utf-8").write("\n".join(o)+"\n")
print("WROTE",dest,"| source",repo[:7],"| files",N)
PY
```

Then upload the written file to each project's Context and delete the prior
bundle (uploads are per-project; same-name re-upload does not propagate across
projects).

## DEC-000150 — Reviewer-gated cycle directives state all four; fresh and Opus 5 are defaults, not fixed by class
Date: 2026-08-08
Decision: A reviewer-gated cycle directive states **all four** dispatch
requirements — route, model, track, and the execution block — like every other
dispatch. Route *fresh* and model *Opus 5* are the class **defaults**: stated per
directive and overridable. This reverses the route/model half of `DEC-000110`.
Its other half is carried forward unchanged and restated here so it stays live
under whole-entry supersession: **track is required per directive**, because it
genuinely varies. The carve-out is removed from `skills/spec-review-cycle.md`
(Cycle directive format), `skills/directive-dispatch.md` (Use when, The four
requirements), and `LEXICON.md` (`Directive`).
Context: owner override (Dave), per
`docs/cycles/trivium-gate-cycle-2-directive.md` R1, after `DEC-000110` had landed
agreed. The finding `DEC-000110` answered
(`reviews/spec-review-cycle-cycle-1.md` B1 ≡ `reviews/LEXICON-cycle-1.md` N1) is
still answered, by the other route that review named: with all four stated,
nothing is omitted, so `skills/directive-dispatch.md`'s "an unstated part is a
defect" is satisfied by statement rather than by exemption. That review called it
the smaller change and the one not requiring a new exception class. Restating the
track half is deliberate — `policies/decision-log-policy.md` supersedes whole
entries, which is how `DEC-000030`'s carve-out went dead under `DEC-000040`, and
a half-reversal expressed as a pointer to a superseded entry would repeat it.
Consequence for tooling: `bin/cycle-open` (TP-1) must emit Route, Model, and
Track, not Track alone; the Track-only PR is superseded and held.
Supersedes: DEC-000110
