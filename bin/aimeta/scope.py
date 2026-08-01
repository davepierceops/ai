"""In-scope glob resolution, read from the metadata policy at runtime.

The globs are never baked into code: they are extracted from the metadata
policy's Scope section, so a policy edit changes enforcement. Extraction
fails closed (`ScopeError`) rather than falling back to a built-in list — a
silent fallback would let a policy edit stop being enforced without anyone
noticing.

Contract: `docs/packages/package-a-spec.md` §3.2.
"""

from __future__ import annotations

import fnmatch
import pathlib
import re

POLICY_RELPATH = "policies/document-metadata-policy.md"
IN_SCOPE_MARKER = "In scope (frontmatter required)"
OUT_OF_SCOPE_MARKER = "Out of scope"

_BACKTICKED = re.compile(r"`([^`]+)`")


class ScopeError(Exception):
    """Raised when the in-scope set cannot be read from the policy."""


def parse_in_scope_globs(policy_text):
    """Extract the in-scope globs from the metadata policy text."""
    lines = policy_text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if IN_SCOPE_MARKER in line:
            start = index + 1
            break
    if start is None:
        raise ScopeError(
            "no %r section in the metadata policy; refusing to guess the in-scope set"
            % IN_SCOPE_MARKER
        )

    globs = []
    for line in lines[start:]:
        if OUT_OF_SCOPE_MARKER in line:
            break
        if line.strip().startswith("-"):
            globs.extend(_BACKTICKED.findall(line))
    if not globs:
        raise ScopeError(
            "the %r section names no backticked entries; refusing to guess"
            % IN_SCOPE_MARKER
        )
    return globs


def load_globs(methodology_home):
    """Read POLICY_RELPATH under `methodology_home` and parse its in-scope set."""
    policy = pathlib.Path(methodology_home) / POLICY_RELPATH
    try:
        text = policy.read_text()
    except OSError as exc:
        raise ScopeError("cannot read %s: %s" % (policy, exc))
    return parse_in_scope_globs(text)


def matches(relpath, globs):
    """True when `relpath` is in the frontmatter-enforced set.

    Only markdown is ever in scope: frontmatter is a markdown convention.
    """
    relpath = str(relpath).replace("\\", "/")
    if not relpath.endswith(".md"):
        return False
    for glob in globs:
        if glob.endswith("/**"):
            if relpath.startswith(glob[:-2]):
                return True
        elif fnmatch.fnmatchcase(relpath, glob):
            return True
    return False
