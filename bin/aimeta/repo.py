"""Git and repository helpers. Repo root always comes from the invoking repo.

STUB — interface contract only; see `bin/aimeta/frontmatter.py` for why.

Contract: `docs/packages/package-a-spec.md` §3.3.
"""

from __future__ import annotations

import pathlib

DISPOSITION_PATH = "reviews/frontmatter-disposition.md"
HOME_ENV_VAR = "AI_METHODOLOGY_HOME"
HOME_SENTINEL = "bin/check-frontmatter"


class GitError(Exception):
    """A git invocation failed."""


def git(*args, **kwargs):
    """Run git and return stripped stdout. Raises GitError on non-zero exit."""
    # STUB
    return ""


def repo_root(start=None):
    """Top level of the repo containing `start` (default: cwd)."""
    # STUB: pretends the cwd is always a repo root.
    return pathlib.Path(start or ".").resolve()


def methodology_home(root):
    """Locate the /ai clone: env var, then self-hosted repo, then sibling `ai`."""
    # STUB: always claims the invoking repo is the methodology home.
    return pathlib.Path(root)


def last_commit_sha(root, relpath):
    """Full SHA of the last commit touching `relpath`, or None if untracked."""
    # STUB
    return None


def file_at_rev(root, rev, relpath):
    """Content of `relpath` at `rev` (`:` for the index), or None if absent."""
    # STUB
    return None


def staged_entries(root):
    """[(status letter, relpath)] for the staged set."""
    # STUB
    return []


def role_slugs(root, home=None):
    """Set of `roles/*.md` basenames, from the invoking repo or the home clone."""
    # STUB
    return set()


def disposition_paths(root):
    """Paths named in the grandfather disposition list, or an empty set."""
    # STUB: claims every document is grandfathered.
    return {"*"}
