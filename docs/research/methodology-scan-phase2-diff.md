---
status: draft
last-reviewed: null
audience: [research-agent, human]
purpose: Diff the external practice catalog against the project methodology, grade adoption-worthiness, and sort findings into gap / contradiction / convergence as inputs to a spec-review cycle. Phase 2 of the scan.
depends-on: []
---

# Directive: External Methodology Scan — Phase 2 (Diff and Grade)

## Intent

Diff the external practice catalog against this project's methodology. For each
catalogued practice, determine its relationship to the methodology and grade its
adoption-worthiness against the rubric below. Output is a findings set packaged
as input to a spec-review cycle.

Phase 2 assesses and recommends. It does not decide adoption and does not edit
methodology documents — adoption is Dave's, and any change enters through the
normal cycle.

## Inputs

- The external practices: `methodology-scan-catalog.md` and
  `methodology-scan-catalog-gap.md`.
- The methodology corpus: the governed documents of `davepierceops/ai`.

## Not blind

Phase 1 was blind to the methodology. This phase requires it. Load the corpus;
the prior blindness constraint does not apply.

## Rubric — adoption-worthiness

This rubric is authored from the problem and fixed before grading begins. It is
not tuned to the catalogued practices, and it grades a practice on its own
merits and fit to the problem — never on whether the practice resembles what the
methodology already does.

Grade each practice on four axes, low / medium / high, each with a one-line
reason:

1. **Problem relevance** — does a spec-first, LLM-assisted workflow actually have
   the failure mode this practice addresses? If no: out of scope — record as
   no-action, do not grade further.
2. **Mechanism concreteness** — is there a specific, adoptable mechanism, or only
   an aspiration? A goal with no mechanism is not adoptable.
3. **Source strength** — how well-evidenced is the practice in its own tradition?
   Carry the catalog's source type and quality forward; a weak or vendor-content
   source scores low here regardless of the idea's appeal.
4. **Adoption cost** — cheap and additive, or a deep structural change? High cost
   is not disqualifying; it is information for sequencing.

Score is independent of bucket. A practice that contradicts a methodology choice
can still score high, and a high-scoring contradiction is a priority finding.

## Buckets — relationship to the methodology

Classify each practice into exactly one:

- **Gap** — the methodology holds no position on the problem this practice
  addresses. An unfilled slot.
- **Contradiction** — a serious external practice does the opposite of a
  deliberate methodology choice. Not adopted here; surfaced for Dave to
  re-litigate against the practice's strongest case.
- **Convergence** — the practice shares a mechanism with an existing methodology
  position that was arrived at independently.
- **No-action** — out of scope (failed problem-relevance), or a duplicate of a
  position already fully held.

### Evidence discipline

Every classification cites the methodology:

- Convergence, contradiction, and any "already covered" claim name the
  methodology document and section that holds the position, by path — and the
  decision-log ID where one governs.
- State whether the methodology's coverage is **equivalent** to the external
  practice or merely **adjacent**. Adjacent-but-not-equivalent is a **partial
  gap**, not "already covered." Do not collapse it. An unsupported "already
  covered" is not permitted.
- Convergence requires a shared **mechanism**, not shared vocabulary. Term
  overlap without mechanism overlap is not convergence.
- A contradiction names the specific methodology decision it opposes and states
  the external practice's case at its strongest, so re-litigation runs against a
  real argument rather than a strawman.

## Finding schema

```markdown
## <catalog-id> — <practice name>
Bucket: gap | contradiction | convergence | no-action
Methodology position: <path[:section], decision-log ID if any — or "none" for a gap>
Coverage: equivalent | adjacent (partial gap) | none | n/a
Scores: relevance <l/m/h> · mechanism <l/m/h> · source <l/m/h> · cost <l/m/h>
Case: <gap: what it would add. contradiction: the external practice's strongest
  case and the choice it opposes. convergence: the shared mechanism and the
  independent position it confirms.>
Cycle input: <the specific proposed change, phrased as an input to a spec-review
  cycle — not a decision>
```

## Processing and checkpoints

- Work the catalog in batches; by tradition is fine. Write findings
  incrementally rather than holding the whole set to the end.
- Checkpoint the findings file after each batch.
- Do not edit any methodology document. The findings file is the only output.

## Output

- Write findings to `./methodology-scan-phase2-findings.md`.
- Within each bucket, order by adoption-worthiness, high scores first.
  High-scoring contradictions lead the document.
- End with a summary: counts per bucket; the highest-value handful across all
  buckets; any practice whose classification was genuinely ambiguous — flag it
  for Dave rather than force a bucket.

## Dispatch

- **Route:** fresh session.
- **Model floor:** Opus. This is judgment over canonical documents where a wrong
  call is expensive and hard to detect — the top row of the dispatch table. Not
  Sonnet.
- **Corpus present, not isolated:** unlike Phase 1, run this where the full
  methodology corpus is available — the repo clone — with both catalogs present.
- **Landing:** the executor writes the findings file into the working tree and
  stops. Dave reviews the git diff and commits — the diff is the human control
  surface. No push required until the remote returns.
- **Attended posture:** confirm the first batch checkpoint before stepping away.
  The findings feed a spec-review cycle; read them as cycle inputs, not
  conclusions.
