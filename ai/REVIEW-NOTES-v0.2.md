# Review Notes: v0.2

## Scope

Reviewed and revised:

- `ai/operating-model.md`
- `ai/context-sets/base.md`

## Findings

v0.1 had the correct conceptual spine:

- Dave as PM/EM/operator
- agents as implementation team
- human code review intentionally not the default control
- evidence replacing default diff review
- mocked boundaries as explicit confidence boundaries

The main weakness was that the documents were still somewhat abstract. They needed clearer behavioral instructions for agents and a stronger connection between the operating model and day-to-day change flow.

## Changes made

### `ai/operating-model.md`

Strengthened:

- trust model
- core operating rule
- agent must/must-not behavior
- standard change flow
- definition of done
- escalation to Dave
- relationship to vendor tooling
- production-grade standard

### `ai/context-sets/base.md`

Strengthened:

- core evidence rule
- operating posture
- standard response shape for meaningful work
- verification rule
- mock rule
- tooling rule
- accepted-risk vocabulary

## Editorial judgment

These two files now better serve as the root instructions for the rest of the tree.

The next likely review targets are:

1. `ai/context-sets/testing-and-verification.md`
2. `ai/policies/verification-boundary-policy.md`
3. `ai/roles/skeptic-risk-agent.md`

Those three files should become the strongest enforcement path for the original mocked-boundary insight.
