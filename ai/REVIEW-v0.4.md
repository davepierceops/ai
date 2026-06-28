# Review: v0.4

Status: in-review

## How to use this document

This is a tiered review, mirroring the project's own two-tier gate rather than
reading all 37 documents line by line (which is the "human as compiler"
anti-pattern this framework warns against).

1. Read the **consequential spine** (Section C, marked *spine*) carefully —
   these are the files where being wrong propagates everywhere.
2. Use the **findings** (Section A) to steer attention while you read.
3. **Scan** the carried-over files (Section C, marked *carried*); spot-check
   rather than proofread.
4. Record approvals in the tracker (Section C) as you go.

**Caveat:** these findings were produced by the same party that wrote the merge.
That makes this a pre-filter, not the independent Skeptic/Risk review the
framework calls for. It steers your reading; it does not certify the set.

---

## A. Findings

Severity uses the project's own vocabulary: *blocking* / *needs Dave decision* /
*deferrable* / *not material*.

No blocking findings. No dangling internal links — every backtick-referenced
path resolves to a real file.

### Needs Dave decision

**A1. [RESOLVED] Vocabulary blurred two axes and two actors.** What looked like
two overlapping lists to merge was really ambiguous language. Two *axes* were
conflated — the **control surface** (how humans control: spec/tests/o11y, not
human code review) and the **release gate** (whether a human gives go/no-go
before users see a change) — and within the first, two *actors* were blurred:
*human* vs *agentic* code review. Resolved by rewording, not merging:
README #5 now names the control surface and says code review is agentic
(Reviewer, Skeptic/Risk) feeding human-decided recommendations; README #10 and
the gate policy now frame the gate as the **release decision**;
`human-review-boundary.md`'s inspection list is relabeled the *exception path*,
explicitly distinct from the release gate. The two lists never needed merging —
they describe different axes and now say so.

**A2. [NARROWED] Gate framing ratified; consequential-class membership still
open.** Dave ratified the gate model: two-tier, fired at the **release
decision**, with commit/deploy/release mapping deferred to each project's TRD.
What remains open is only the *membership* of the consequential class — the list
in `commit-and-change-control-policy.md` (auth, schema/migrations,
security/privacy, irreversible, public-facing, verification boundary, core
architecture) is the proposal. *Decision:* confirm or adjust that list.

**A3. [RESOLVED] Versioning split into two concepts.** Per-doc version numbers
were trying to signal both "is this current" and "how settled is this doc," and
answered neither. Resolved (option 3): a single **tree version** is declared once
in `MANIFEST.md` and echoed in `README.md`; per-document `Status` lines now carry
a maturity word only (`draft` / `in-review` / `stable` / `placeholder`), no
competing number. Project specs (PRD/TRD skeletons) keep real version numbers, as
those artifacts version independently.

**A8. "Meaningful change" is an undefined load-bearing threshold.** The phrase
gates ceremony across the framework (release-readiness, change packages, "for
meaningful changes…") but is never defined anywhere. It is the load-bearing
version of the vague-conditional concern. *Decision:* define "meaningful change"
once and reference it, or draw a second light line (trivial vs meaningful)
alongside the routine-vs-consequential line in A1/A2. Adjacent to A1/A2.

### Deferrable (clear fixes; I can apply on your say-so)

**A4. `testing-policy.md` is silent on the red-gate.** It says to write the test
plan "before implementation" but never states the confirm-tests-fail-first rule,
even though that rule now lives in three other files. The testing policy is
exactly where a reader expects it. *Fix:* add a red-gate sentence + cross-ref.

**A5. Architect missing from a separation list.** `ai-native-engineering.md`
"Team model" lists seven roles including Architect, but its "Separation of
concerns" enumeration names only five (no Architect, no PM). Since the Architect
was just elevated to TRD author, its absence is a small inconsistency. *Fix:*
add the Architect line.

**A6. `MERGE-NOTES-v0.4.md` references `methodology.md`,** which isn't in the
tree (it was the source input). A cold reader will look for it and not find it.
*Fix:* mark it "(source input, not included)" or drop the filename.

### Not material (note only)

**A7. Stale activation/era copy in carried-over files.** `base.md` ends with a
"## Next" rollout list ("apply to all active work…"), and `REVIEW-NOTES-v0.2/v0.3`
contain "next likely review targets" that read as live TODOs but are historical.
Harmless, but a cold reader could mistake them for current instructions. Optional
cleanup: archive the review notes or stamp them "historical."

---

## B. What was checked

- Every internal path reference against the real file list — all resolve.
- The canonical spec chain stated in four places (source-of-truth-policy,
  operating-model, README principles, TRD diagram) — all four match.
- The Test Designer / Coder separation across the three files it touches —
  consistent.
- The two "close-look" lists (A1) — the main coordination gap.
- The red-gate's presence across files (A4) — the main coverage gap.

Not checked (out of scope for a pre-filter): whether the framework *as a whole*
is the right model — that's your call, not a consistency question.

---

## C. Review tracker

Tier: *spine* = read carefully; *changed* = new or revised in v0.4, review the
substance; *carried* = carried over intact, scan/spot-check.

### Entry & overview — read first

| ✓ | File | Tier | Notes |
|---|------|------|-------|
| [x] | `CLAUDE.md` | changed | adapter / entry point; **approved** — cut vague "role-specific review when appropriate" line |
| [x] | `ai/README.md` | spine | **approved**; #5/#10 rewritten; tree-version convention (A3 resolved) |
| [x] | `ai/operating-model.md` | spine | **approved** (ship); source-of-truth, 9-step flow, release gate, DoD, flags |
| [ ] | `ai/context-sets/base.md` | spine | root context; see A7 (Next section) |

### Consequential spine — read carefully

| ✓ | File | Tier | Notes |
|---|------|------|-------|
| [ ] | `ai/specs/trd-template.md` | spine | foundation; standing-vs-per-change line (you said yes) |
| [ ] | `ai/specs/prd-template.md` | spine | product spec above TRD |
| [ ] | `ai/policies/source-of-truth-policy.md` | spine | canonical chain + hard stop |
| [ ] | `ai/policies/commit-and-change-control-policy.md` | spine | the (c) gate — see A1, A2 |
| [ ] | `ai/context-sets/spec-and-change-discipline.md` | spine | sequence, red-gate, habits |

### Changed in v0.4 — review the substance

| ✓ | File | Tier | Notes |
|---|------|------|-------|
| [ ] | `ai/roles/architect-agent.md` | changed | gained TRD + per-change summary |
| [ ] | `ai/roles/test-designer-agent.md` | changed | separation imposed |
| [ ] | `ai/roles/coder-agent.md` | changed | separation imposed |
| [ ] | `ai/context-sets/ai-native-engineering.md` | changed | separation mandatory; see A5 |
| [ ] | `ai/MANIFEST.md` | changed | v0.4 changelog + bundles |
| [ ] | `ai/MERGE-NOTES-v0.4.md` | changed | decision record; see A6 |

### Carried over — scan / spot-check

| ✓ | File | Tier | Notes |
|---|------|------|-------|
| [ ] | `ai/roles/pm-em-owner.md` | carried | |
| [ ] | `ai/roles/reviewer-agent.md` | carried | |
| [ ] | `ai/roles/skeptic-risk-agent.md` | carried | strongest doc in the set |
| [ ] | `ai/roles/release-manager-agent.md` | carried | |
| [ ] | `ai/context-sets/production-grade-software.md` | carried | |
| [ ] | `ai/context-sets/testing-and-verification.md` | carried | |
| [ ] | `ai/policies/testing-policy.md` | carried | see A4 (red-gate gap) |
| [ ] | `ai/policies/verification-boundary-policy.md` | carried | |
| [ ] | `ai/policies/agent-review-policy.md` | carried | |
| [ ] | `ai/policies/release-readiness-policy.md` | carried | |
| [ ] | `ai/boundaries/human-review-boundary.md` | carried | see A1 |
| [ ] | `ai/boundaries/mocked-boundaries.md` | carried | |
| [ ] | `ai/boundaries/live-integration-boundaries.md` | carried | |
| [ ] | `ai/boundaries/vendor-tooling-boundary.md` | carried | |
| [ ] | `ai/skills/boundary-audit.md` | carried | |
| [ ] | `ai/skills/evidence-review.md` | carried | |
| [ ] | `ai/skills/release-readiness-review.md` | carried | |
| [ ] | `ai/skills/change-package-creation.md` | carried | |
| [ ] | `ai/skills/test-plan-review.md` | carried | |
| [ ] | `AGENTS.md` | changed | adapter; spec-first + gate lines |
| [ ] | `.claude/agents/README.md` | carried | placeholder |
| [ ] | `.claude/skills/README.md` | carried | placeholder |

---

## D. Sign-off

- [ ] Spine reviewed and approved
- [ ] Needs-decision findings (A1–A3) resolved
- [ ] Deferrable fixes (A4–A6) applied or explicitly deferred
- [ ] Tree approved as v0.4
