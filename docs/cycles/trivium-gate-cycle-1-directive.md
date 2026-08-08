# Trivium Gate — Cycle 1 Directive — davepierceops/ai

Date: 2026-08-08
Route: fresh — self-contained; a fresh Claude Code session, no triage context.
Model: Opus 5 — directive execution over canonical documents.
Track: A (MCP) recommended; B if operator-invoked. *(Route/Model stated explicitly
here because the bounded-exception that lets cycle directives omit them lands in
this same cycle — see D3. Track is hand-added pending the `bin/cycle-open` package.)*

Documents in scope (all @ `81bd2de55e2a7c5838882bb5b7768abc7ccf8238`):
- `LEXICON.md`
- `skills/command-blocks.md`
- `skills/directive-dispatch.md`
- `skills/spec-review-cycle.md`
- `policies/remote-write-verification-policy.md`

Reviewer findings (origin/main): `reviews/{LEXICON,command-blocks,directive-dispatch,spec-review-cycle,remote-write-verification-policy}-cycle-1.md`.
18 raw findings; 3 cross-filed pairs merged → 15 decisions below (D1–D7 blocking, D8–D14 non-blocking, D15 observation).

---

## Decisions

### D1 (LEXICON B1 ≡ directive-dispatch B1) — modify
Finding: LEXICON's `Sync block` says a sync block precedes *every* execution block; directive-dispatch's Track B has none (folded into the echoed line). Two canonical docs, no tiebreak.
Resolution: Direction (a) — narrow to Track A.
- `LEXICON.md` (`Sync block` def, ~`:105-106`): change "Precedes every execution block in a dispatch." to state it precedes every **Track A** execution block; in Track B the sync step is carried by the echoed dispatch line, not a separate block.
- `skills/directive-dispatch.md` Track B mechanics: state that Track B carries the sync step in the echoed line and *why the tracks differ* — Track B is same-machine, commit-not-push (`:185-190`), so the executor runs in the clone that already holds the local unpushed commit; a Track A remote fetch does not apply and could pull a tree lacking the directive. Pin down what "sync" means in the Track B echoed line: a working-tree-current check in that same clone, **not** a remote fetch. (This dissolves the "a bare 'sync' can't name a remote" concern — Track B does no remote sync.)
- Wording note: state this using the corrected framing from D5 (fail-loudly / unverified-remote), not the "name the remote or work goes missing" rationale D5 removes.
- `OPEN-ITEMS.md:901` ("Sync as a skill rather than a step…"): close it, recording that this cycle's direction-(a) decision resolves it (Track B carries sync in the echoed line; same-machine semantics). Do not leave it "Not analysed" while the tree ships its proposal.

### D2 (command-blocks B1 ≡ directive-dispatch B2) — accept
Finding: `set -e` terminates an interactive shell on the next failure exactly as `exit` does, but is absent from the shell-termination enumeration (command-blocks rule `:51-55` + criterion 6 `:70-72`); directive-dispatch `:176-180` restates the same enumeration and inherits the gap.
Resolution:
- `skills/command-blocks.md`: restate the rule (`:51-55`) and criterion 6 (`:70-72`) **by effect** — "no construct that can terminate the shell it is pasted into" — naming `exit`, `exec`, `logout`, `|| { …; exit; }`, and `set -e` as known instances, directing adopting projects to add their own. This mirrors the "known instance, not the rule" pattern the copy-control rule (`:39-42`) already uses, so the document stops holding two patterns for the same kind of rule.
- `skills/directive-dispatch.md:176-180`: replace the restated enumeration with a pointer — e.g. "Guards fall through; they never terminate the shell. See `skills/command-blocks.md`, criterion 6." The rule then lives in one place and cannot drift.
Note: no DEC governs the current enumeration (it entered in `ed7d904` with no decision entry), so the by-effect restatement reverses nothing.

### D3 (spec-review-cycle B1 ≡ LEXICON N1) — modify
Finding: The cycle-directive format requires none of route/model/track and licenses the omission ("Everything else as needed"); directive-dispatch calls each unstated part a defect and says its rules reach this file; `bin/cycle-open:116` bakes the omission into the generated skeleton.
Resolution: Bounded exception.
- `skills/spec-review-cycle.md` (Cycle directive format `:101-130`): carry **Track** as a required field. State that Route and Model are **fixed-by-class** for reviewer-gated cycle directives — Route: fresh (one conversation per cycle; fresh execution session); Model: Opus 5 (directive execution over canonical documents) — stated once with a pointer to `skills/directive-dispatch.md` §2/§1, not restated per directive.
- Mirror the carve-out at `skills/directive-dispatch.md:21-24` and `LEXICON.md:64-66` (`Directive` def) so the "all four, every time" statement admits the bounded exception rather than contradicting it.
- `bin/cycle-open` skeleton change is **out of scope for this directive** — see Deferred §T1. Interim: the author hand-adds Track to cycle directives (as done on this one).

### D4 (LEXICON B2) — accept
Finding: The warrant for the layer-2 `execute` rule cites `roles/orchestrator-agent.md` as "describes executing change packages as its work," but that file says the Orchestrator does *not* execute (`:15`, `:63`).
Resolution: `LEXICON.md:38-41` — replace the backwards `orchestrator-agent` citation with `roles/chief-of-staff.md` (the agreed supersessor), which uses "execution" for layer-2 Claude Code work ("execution belongs to Claude Code"). Keep the `skills/spec-review-cycle.md` citation as the second live example.

### D5 (command-blocks B2) — modify
Finding: The "name remotes explicitly; do not rely on the `origin` alias" rule (`:27-30`) has no conformance criterion — but on inspection the rule itself is unsound: `origin` is a remote *name*, not a protocol; a `git fetch`/`push` that can't authenticate fails loudly (non-zero exit), it does not silently return empty results. The rule entered in a bulk drafting commit (`c4baefe`) with no decision or incident behind it.
Resolution: **Rewrite the rule, do not add a criterion to enforce it.** Lightweight version:
- `skills/command-blocks.md:27-30`: replace with a rule targeting the real hazard — a sync/remote command in a pasted block states its remote **and ref** explicitly, does not rely on branch-upstream config, and fails loudly (checked exit) on a bad sync. `origin` remains a valid explicit remote name used correctly. Remove the false "auth failure surfaces as missing work rather than an auth error" rationale.
- The conformance-criterion question (whether the rewritten rule warrants a checklist line — e.g. "sync commands state remote+ref and check exit status") rides with the rewrite draft; decide it there, not as a separate finding.

### D6 (spec-review-cycle B2) — accept
Finding: `skills/spec-review-cycle.md:57` heading "Directive (handoff artifact)" is the exact `handoff` misuse `LEXICON.md:122-123` names by line and `OPEN-ITEMS.md:775-791` tracks as "needs a cycle." This is that cycle.
Resolution: Three-record reconciliation, one change:
- `skills/spec-review-cycle.md:57`: `### 2. Directive (handoff artifact)` → `### 2. Directive`.
- `LEXICON.md:122-123`: strike the "Known misuse to correct: …" paragraph — the misuse is gone.
- `OPEN-ITEMS.md:775-791`: close/strike the entry — its "what's needed" is done.

### D7 (remote-write B1) — modify
Finding: Rule 3's clause "Never abbreviate a SHA that will be used as a pointer" (`:53-54`) contradicts the **agreed** `document-metadata-policy.md` (which permits abbreviated `last-reviewed` pointers) and `bin/aimeta/expedited.py` (which normalizes them via `rev-parse`).
Resolution: (b) drop-and-point.
- `policies/remote-write-verification-policy.md` Rule 3 (`:53-54`): remove the abbreviation clause; keep the two provenance sentences ("State SHAs read from git… never invent one"). Rule 3 stays about provenance (git log is the source of record), which is its actual subject.
- Add a one-line pointer to `skills/directive-dispatch.md:92-93`, which already carries the narrow, correctly-scoped "never abbreviate a pointer SHA" rule for dispatch blocks.

### D8 (command-blocks N1) — accept
Finding: "Evidence" is load-bearing in criterion 4 and undefined; the Track B pre-flight `ls` reads both ways under it.
Resolution: `skills/command-blocks.md:21-25` — scope "evidence" to output that is cited later or leaves the session, as against output consumed in-the-moment by the person running the block. State where the pre-flight `ls` block is defined (`skills/directive-dispatch.md`) that its listing is the exempt (in-the-moment) kind.

### D9 (directive-dispatch N1) — accept
Finding: The `bin/dispatch` deferral rests on a stale "seven cycles" count (entered 2026-08-02, never recounted) presented as current evidence.
Resolution: `skills/directive-dispatch.md:272-284` — drop the count; rest the deferral on the two named build triggers plus the expiry condition alone.

### D10 (directive-dispatch N2) — accept
Finding: The Track B relocate/append blocks assume the pasting shell's cwd is the clone root; neither states nor checks it.
Resolution: `skills/directive-dispatch.md` (`:156-165`, `:208-219`) — state the assumed working directory (run from the clone root) in the prose around the blocks. Prose only: a structural guard would need the *expected* clone path, which the block does not carry generically; a bare "am I in a repo" check misses the wrong-clone case this finding names.

### D11 (directive-dispatch N3) — accept
Finding: The two-failure trigger's keep-reason (contention detector, `DEC-000080`) is absent from the skill, which frames the trigger only as a Track B on-ramp — the reading under which `DEC-000080` records it was nearly cut.
Resolution: `skills/directive-dispatch.md` — one clause at `:63-64` naming the contention-detector value and citing `DEC-000080`; one clause at `:57-60` adding concurrent-session contention to the conditions Track B addresses. Does not move the decision record; makes the skill point at it.

### D12 (spec-review-cycle N1) — accept
Finding: The reviews/ filename convention (`<stem>-cycle-<n>.md`) that `last-reviewed` points at is unwritten; the stem rule self-collides on this document (`spec-review-cycle-cycle-1`).
Resolution: `skills/spec-review-cycle.md` (`### What this schema governs`) — state the convention: `reviews/<document stem>-cycle-<n>.md`, stem = basename without extension; say what to do when the stem already ends in `-cycle` or a digit.

### D13 (spec-review-cycle N2) — accept in principle, **defer**
Finding: The review schema has no shape for a check that was run and passed; this review carried five unschema'd "checks that passed" lists because of it.
Resolution: Deferred to a dedicated schema-revision cycle together with `OPEN-ITEMS.md:547` items 1–4 (same fourth-use feedback round, not gate findings on these docs). **No edit in this directive.** See Deferred §T2.

### D14 (remote-write N1) — accept
Finding: The policy's Scope and "Relationship to existing rules" do not reach the Track B write path (local clone `mv`/`add`/`commit`), whose verification rule lives only in a skill.
Resolution: `policies/remote-write-verification-policy.md` — add a Scope clause for the case where the agent cannot read back its write: verification is the operator's, and the agent reports only what the operator reported. Cite `skills/directive-dispatch.md` in "Relationship to existing rules" alongside `skills/spec-review-cycle.md`. Complements D7.

### D15 (LEXICON O1) — accept
Finding: Two open-work lines in LEXICON lack `OPEN-ITEMS.md` pointers.
Resolution: `:122-123` is struck by D6. For the remaining line `:125-126` ("A handoff into another *decision* session has no term yet. Naming it is open work."), add the `OPEN-ITEMS.md:794` anchor.

---

## Deferred / out of scope

- **§T1 — `bin/cycle-open` Track field (from D3).** The skeleton generator (`:116`) must emit the Track field. This is a code change (acceptance criteria, tests, red-gate), filed as its own coded package — **not** in this doc-cycle. Track it in `OPEN-ITEMS.md`/`BACKLOG-v2.md`. Interim: authors hand-add Track to cycle directives.
- **§T2 — review-artifact schema revision (from D13).** A shape for verified-and-held checks, taken together with `OPEN-ITEMS.md:547` items 1–4. Dedicated schema cycle.
- **§T3 — whole-doc LEXICON-conformance sweep (touch rule / AI-12).** Whether agreeing these five requires conforming each *whole* document to the lexicon, versus the targeted conformance the findings touch, is unsettled and gates on Dave. Disposition (2026-08-08): **targeted suffices for this gate**; a whole-doc sweep is its own reviewed pass, not folded into this directive.
- **Housekeeping (not a gate finding):** `OPEN-ITEMS.md:747` ("LEXICON.md frontmatter unenforced") is stale — DEC-000060 landed and `bin/check-frontmatter --all` exits 0 over 47 files. Strike when convenient; outside this cycle's scope.

---

## Execution notes

- **STOP conditions pin to `81bd2de`**, not the head of the branch this directive lands on.
- **Targeted edits only.** No whole-document lexicon-conformance sweep in this pass (see §T3). Conform lexicon terms within the sections actually edited.
- **Permitted outside the five in-scope docs:** `OPEN-ITEMS.md` (`:901` close per D1; `:775-791` close per D6; `:794` anchor per D15) and `decisions/log.md` (append-only DEC entries, below). No other files.
- **Append DEC entries** for the substantive calls — D1 (Track-B sync direction), D2 (by-effect enumeration), D3 (bounded exception + tool split), D5 (origin-rule rewrite), D7 (Rule 3 scoping) — as marker-guarded `cat >>` appends to `decisions/log.md` (skip if the marker heading is already present; `rm` the source after). One DEC or a grouped entry, per the executor's judgment on granularity.
- **Cross-file consistency** is required within: D1 (LEXICON + directive-dispatch + OPEN-ITEMS), D2 (command-blocks + directive-dispatch), D6 (spec-review-cycle + LEXICON + OPEN-ITEMS), D7 (remote-write + directive-dispatch pointer), D15 (LEXICON + OPEN-ITEMS). Where a value or claim is changed, update every instance across the whole document before finishing.
- **Executor obligations:** report what was done, not what the directive said; an instruction that cannot be executed as written → stop and surface, no improvisation on canonical documents; concurrent tree mutation (files this session did not change moving, HEAD moving, index lock) → stop and surface.
- On completion: commit referencing the cycle, push, and surface the diff for Dave's review (spec-review-cycle §4). Documents then go back to the reviewer for the gate re-check; no `status` flip here.
