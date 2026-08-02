---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Vendor Directories

## The convention

One directory per supported vendor: `vendors/<vendor>/`. Currently:
`vendors/claude-code/`.

## What belongs here

**Vendor-specific configuration artifacts and vendor-specific mechanics.**
The concrete shape of one tool's settings file, the failure modes of one
tool's transport, the exact permission strings one tool understands.

## What does not

**Operating principles.** Those stay in the core doc set —
`policies/`, `context-sets/`, `boundaries/`, `roles/`, `skills/` — and stay
vendor-agnostic.

The split follows `operating-model.md`: "Tool-specific files may adapt these
rules but should not be the sole location of durable policy," and README
principle #7: "Vendor-specific agent systems are implementation details, not
the source of truth."

The test: if swapping vendors would delete the sentence, it belongs here. If
swapping vendors would leave it true, it belongs in the core doc set.

## The lifecycle question is open

`policies/document-metadata-policy.md` does not list `vendors/**` in its
in-scope set, so:

- the pre-commit hook does not check these files
- their frontmatter is written by hand and verified by nobody
- per that policy's agent-behavior rules, a document with no governed status
  is not clearly loadable as governing context

Documents here carry frontmatter anyway, so that extending the in-scope set
later is a one-line policy edit rather than a migration. **But the frontmatter
currently means less here than it does elsewhere, and that should not be
mistaken for governance.**

This is precisely the open question in Q1b — "does the doc set need an
environment-config class, and what governs its lifecycle?" — and it is
**not answered here**. The v1 requirement was a usable, expandable answer,
not the final taxonomy.

Extending `policies/document-metadata-policy.md` to cover `vendors/**` is a
revision to an `agreed` document and must go through a spec-review cycle. It
was not done as part of this draft.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.2) executing Q1b.
Nothing here is agreed.
