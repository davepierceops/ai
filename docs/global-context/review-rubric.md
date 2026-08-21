---
status: draft
last-reviewed: null
audience: [spec-reviewer-agent, chief-of-staff, human]
---

# Review Rubric — Fiducial Assembly, Pass 1 (prose)

Criteria every non-code file in this repository is examined against. A file
passes when it satisfies all ten or is retired. Findings cite the criterion
number.

1. **Bundles are the product.** The file is written to be read inside a
   generated bundle, by an agent that has never seen the repository. Nothing
   in it assumes the reader can open another file.

2. **`audience:` is the selector.** The file carries `audience:` with at least
   one value from the known set, and `order:` where its position in a bundle
   matters.

3. **No references to other files by path.** If the file needs something
   another file states, it states it. A path-shaped reference is a defect.

4. **Core states it → remove it here.** The file does not restate a rule that
   Core or the Decision Layer already states.

5. **Agent instruction, not authoring principle.** Every rule is an instruction
   to the agent reading it. A rule for the person writing instructions belongs
   in the instruction-writing criteria, not here.

6. **Instructions, not rationale.** Rules are stated; arguments for them are
   cut. "Never X" restatements of a stated rule and trailing justifications
   are cut.

7. **Session kind is explicit.** The file is for decision sessions, execution
   sessions, or both, and says nothing only the other kind needs.

8. **Tiers, not model names; route and model, not track.** Model selection
   speaks in tiers. A directive states route and model. Track does not appear.

9. **Filenames are `<descriptor>-<timestamp>`.** Any filename the file
   prescribes or generates follows the convention. No random strings, hashes,
   or UUIDs.

10. **The file earns its place or is retired.** It lands in at least one
    bundle and contributes something no other file in that bundle states.
    A file that fails this is removed, not fixed.
