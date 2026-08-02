"""Shared library for the /ai methodology tooling.

Canonical home: `/ai/bin/aimeta`. Never copied into project repos — project
repos install a thin pre-commit shim that execs the scripts from the local /ai
clone. See `docs/packages/package-a-spec.md` §2.1.

Standard library only.
"""

__all__ = ["frontmatter", "scope", "repo", "cli"]
