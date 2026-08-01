"""In-scope glob resolution, read from the metadata policy at runtime.

STUB — interface contract only; see `bin/aimeta/frontmatter.py` for why.

Contract: `docs/packages/package-a-spec.md` §3.2.
"""

from __future__ import annotations

import pathlib

POLICY_RELPATH = "policies/document-metadata-policy.md"
IN_SCOPE_MARKER = "In scope (frontmatter required)"
OUT_OF_SCOPE_MARKER = "Out of scope"


class ScopeError(Exception):
    """Raised when the in-scope set cannot be read from the policy."""


def parse_in_scope_globs(policy_text):
    """Extract the in-scope globs from the metadata policy text."""
    # STUB: reports an empty in-scope set instead of failing closed.
    return []


def load_globs(methodology_home):
    """Read POLICY_RELPATH under `methodology_home` and parse its in-scope set."""
    # STUB: never reads the policy.
    return []


def matches(relpath, globs):
    """True when `relpath` is in the frontmatter-enforced set."""
    # STUB: claims everything is in scope.
    return True
