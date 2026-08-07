# Cycle 10 Triage Directive — document-metadata-policy.md doc-only route

Date: 2026-08-06
Reviewed: `reviews/document-metadata-policy-cycle-10.md` — verdict `changes-required` (4 blocking, 5 non-blocking, 1 observation)
Governing decisions (per `context-sets/base.md` consult-and-cite): `DEC-000010` (the route), `DEC-000030` (gate-doc exclusion in condition 3)

Documents in scope:
- `policies/document-metadata-policy.md` @ `fca43091fff78275b1d65b60aa9c80d0c9e9089f` (stays `in-review`)
- `roles/spec-reviewer-agent.md` @ `0135043` (`draft` — plain commit, no flip)
- `reviews/expedited-log.md` @ `0135043` (out of frontmatter scope — no flip)

## Decisions

### B1 — accept
Finding: No `specs/` exclusion; a co-authored PRD/TRD reaches `agreed` bypassing the Spec Reviewer gate.
Resolution: Add a fifth eligibility condition mirroring the expedited path's condition 4; retitle the list and update any "four" references to "five".
Dictated wording (new condition 5):
> **Not under `specs/`.** Spec agreement is gated by the Spec Reviewer Agent (`roles/spec-reviewer-agent.md`); this route neither reaches that gate nor overrides it.

### B2 — accept
Finding: "consistency sweep" (condition 4) is defined nowhere in the repo.
Resolution: Define it at first use in the section.
Dictated wording:
> A **consistency sweep** checks the document — and the documents it cross-references and that reference it — for any value or cross-reference the change has made stale. It extends the within-document consistency check `context-sets/spec-and-change-discipline.md` already requires to the document's neighbours, because a change to one document routinely falsifies a claim in another. The co-authoring agent runs it before sign-off; "at least one" means the most recent sweep post-dates the final edit. Completion is attested by Dave's sign-off, not a separate artifact.

### B3 — accept
Finding: Route is silent on multi-document agreements; `DEC-000030` retained multi-file freedom.
Resolution: State that a doc-only agreement may cover more than one in-scope document, and specify recording: the content commit may touch multiple in-scope documents; the log takes one entry per document; each document's `last-reviewed` cites the same content SHA; a separate frontmatter-only flip lands per document (`flip-agreed` touches exactly one path per commit).

### B4 — accept
Finding: The section falsifies `roles/spec-reviewer-agent.md`'s "one bounded exception" claim.
Resolution: Amend `roles/spec-reviewer-agent.md` lines 34-36 to name both exceptions (expedited path and doc-only cycle) and their bounds. `draft` → plain commit, no flip. Sibling sweep already done — `README.md`, `operating-model.md`, `boundaries/human-review-boundary.md` do not carry the claim; no edit there.

### N1 — accept
Finding: `### The record` and the expedited log describe themselves as "expedited"-only; the entry format assumes a revision.
Resolution: Generalize "Each expedited agreement…" → "Each expedited or doc-only agreement…" in `### The record` and in the `reviews/expedited-log.md` header. Add a clause that for a new document the entry's summary states what the document is rather than what changed.

### N2 — accept
Finding: `DEC-000010`'s "Dave asks for the cycle" condition is absent from the conditions.
Resolution: Fold "Dave asks for this route" into condition 4. No `DEC-000010` narrowing.

### N3 — modify
Finding: Section cites neither decision ID (`base.md` consult-and-cite) and names the route two ways.
Resolution: The reviewer's "cite the IDs in the section" is **not adopted** — `document-metadata-policy.md` is portable, and this repo's local `DEC-` IDs break when it travels to project repos. Do **not** add `DEC-` IDs to the section body; the consult-and-cite obligation is satisfied at the change level (this directive and the execution commit name `DEC-000010`/`DEC-000030`). Naming: settle on "doc-only cycle" throughout — retitle `## Doc-only agreement` → `## Doc-only cycle` and use that term in prose.

### N4 — accept
Finding: Route says "any format" but presumes a frontmatter-carrying doc; out-of-scope docs can't complete the sequence.
Resolution: Add a clause restricting the route to documents in the frontmatter in-scope set, since `agreed` is a frontmatter state and out-of-scope documents have no status to reach.

### N5 — accept
Finding: "co-authoring *is* the read a reviewer would perform" overstates; no enforcement-can't-see counterpart.
Resolution: Rewrite the sentence to name the trade in `DEC-000030`'s terms — co-authoring supplies the read, not an independent reader, which is why condition 3 excludes the documents that define the routes to `agreed`. Add a one-line counterpart to the expedited path's "enforcement checks none of this and cannot…" candour.

### O1 — accept
Finding: Expedited's "necessary, not sufficient" + self-exclusion clause not restated.
Resolution: Add a parity clause — the conditions are necessary, not sufficient, and a document may exclude its own revisions from this route.

## Deferred / out of scope
- Decoupling `specs/` templates (`specs/prd-template.md`, `specs/trd-template.md`) from the `specs/` gate to make co-authored templates doc-only-eligible — a deliberate future decision with its own decision-log entry. Raised under B1.

## Execution notes
- Verify the working tree matches reviewed SHA `fca4309` for `document-metadata-policy.md` (or contains it in history with no intervening edits to that doc) before editing.
- `document-metadata-policy.md` stays `in-review`; do **not** flip it to `agreed`. Re-gate (cycle 11) precedes any flip.
- After edits land, the document returns to the Spec Reviewer for the cycle 11 re-gate.
