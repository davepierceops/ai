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

## Lifecycle: governed and enforced

`policies/document-metadata-policy.md` lists `vendors/**` in its in-scope
set as of `ef4438b`, so:

- the pre-commit hook checks these files
- their frontmatter is enforced on the same terms as everywhere else in the
  in-scope set, not written by hand and verified by nobody
- the `status` field on a document here means what it means anywhere else

Documents here carried frontmatter from the start, which is why bringing the
directory into scope was a one-line policy edit rather than a migration.

That settles the lifecycle half of Q1b. The taxonomy half — "does the doc set
need an environment-config class?" — is **not answered here**. The v1
requirement was a usable, expandable answer, not the final taxonomy.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.2) executing Q1b.
Nothing here is agreed.
