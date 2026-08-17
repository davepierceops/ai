---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Client Credentials

## The rule

Agents have **zero write access** to the client's cloud and production
systems. Reading configs, logs, metrics, code, and CI output is the agents'
world; moving levers is the humans'.

Mutations flow exclusively through pull requests applied by humans or by the
client's own CI under the client's own gates.

## Carve-outs

If a discovery task strictly requires a write capability (for example, a
diagnostic that cannot run read-only), the carve-out must be:

- **named** — the exact capability, not a broader role
- **scoped** — the narrowest resource set that serves the need
- **justified** — why discovery cannot proceed without it
- **granted** — by Dave only, with client sign-off
- **expiring** — removed when the need ends
- **registered** — listed in the table below before use

| Capability | Scope | Justification | Granted | Expires |
|---|---|---|---|---|
| (none) | | | | |

## Secrets

Client secret values never enter agent context. Agents may reference that a
secret exists and where it is stored; they never read, echo, or transform its
value.

## Override status

Unlike ceremony (`override-log-policy.md`), this policy is **not overridable
in the field**. Changing it means editing this document, reviewed like any
canonical document. The asymmetry is deliberate: process is negotiable, blast
radius is not.
