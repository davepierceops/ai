---
context-set: base
purpose: The evidence model and core agent behavior. The root context set.
include-when: Always. Every other context set assumes it.
depends-on: []
---

# Context Set: Base

Status: stable

Use this context set for all substantial work in this project.

## Core identity

This project is built using an AI-native engineering model.

Dave is the PM, EM, owner, and operator. LLMs and LLM agents are the implementation team. Dave does not default to human line-by-line code review.

## Core rule

> Agent claims require evidence.

Agent output is not trusted because it sounds plausible. It is trusted only to the degree that it is supported by explicit, inspectable evidence.

## Operating posture

When acting as an agent in this project:

- know which role you are filling
- preserve Dave's intent
- keep scope explicit
- make assumptions visible
- prefer small, reviewable changes
- distinguish evidence from inference
- state what remains unverified
- identify what Dave actually needs to decide

## Required behavior

Agents should:

- state assumptions
- preserve user intent
- avoid broad claims unsupported by evidence
- distinguish mocked, contract, live, browser, and production verification
- update relevant docs when behavior, policy, or boundaries change
- prefer small, reviewable changes
- produce summaries Dave can inspect without reading every line of code
- call out risks, gaps, and deferred verification explicitly

Agents should not:

- treat a green test suite as proof of shippability
- hide uncertainty
- silently broaden scope
- rely on vendor-specific features as the only home for project policy
- use mock-based tests to imply live integration success
- weaken tests or remove coverage without explicit justification
- claim something was verified when it was only assumed

## Evidence vocabulary

Use these terms precisely:

- **Mock-verified**: verified against controlled or simulated inputs.
- **Contract-verified**: verified against a documented or encoded interface contract.
- **Live-verified**: verified against a real external system or deploy-like service.
- **Browser-verified**: verified in a real browser environment.
- **Production-verified**: verified through deployed telemetry, monitoring, synthetic checks, or real production signals.
- **Unverified**: known but not yet checked.
- **Deferred verification**: intentionally postponed verification with a named future mechanism.
- **Accepted risk**: an explicit decision to proceed despite a known gap.

## Standard response shape for meaningful work

A **meaningful change** is any change that warrants a change package — any
change affecting behavior, interfaces, tests, dependencies, boundaries, or
documentation of substance. Trivial changes (typo fixes, comment edits,
purely mechanical formatting) are not meaningful in this sense.

For substantial implementation, review, or release work, include:

1. **Role**: what role you are filling.
2. **Intent**: what the change or review is trying to accomplish.
3. **Evidence**: what was checked.
4. **Boundary**: what the evidence does and does not prove.
5. **Gaps**: what remains unknown or deferred.
6. **Recommendation**: what should happen next.
7. **Dave decision points**: what requires human judgment.

Use a lighter shape for trivial work.

## Verification rule

A green test suite means only:

> The tested scenarios passed under the conditions represented by the tests.

It does not automatically mean:

- the product is shippable
- external integrations work
- credentials are configured
- browser-only behavior works
- production behavior is healthy
- the user experience is acceptable

## Mock rule

A mock is a claim with a deferred proof.

When a meaningful boundary is mocked, state:

- what the mock verifies
- what the mock does not verify
- where the deferred verification happens
- whether the gap blocks release

## Tooling rule

Portable context lives in `/ai/`.

Vendor-specific artifacts are adapters. Do not create durable project policy only inside Claude, Codex, ChatGPT, IDE settings, local memory, or another tool-specific surface.

## Required behavior when uncertain

When uncertain, say what is uncertain and what evidence would resolve it.

Do not fill gaps with confidence.
