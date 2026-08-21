---
status: draft
last-reviewed: null
audience: [assistant, cartographer, skeptic, human]
order: 10
---

# Working With Dave

This file is for execution sessions within an engagement.

## Who you are working with

Dave: 30-year infrastructure/SRE veteran, former director. On a client
engagement he is onsite, hands on the client's keyboard, under time pressure.

## Infra verification ladder

For infra changes, in ascending order:

- **plan-verified** — a dry run (terraform plan or equivalent) shows the
  intended delta and nothing else
- **apply-verified** — the change was applied somewhere real and the resources
  exist as intended
- **serving-verified** — the resulting system demonstrably does its job, not
  merely exists
- **delta-verified** — post-change measurement shows the expected improvement
  against a pre-change measurement

Plan output does not prove apply behavior; apply success does not prove the
system serves.

## Client guardrail — not negotiable, not overridable

You have zero write access to the client's cloud and systems. Dave (or the
client's own CI) moves the levers; you produce what he runs.
