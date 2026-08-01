"""Git and repository helpers. Repo root always comes from the invoking repo.

Contract: `docs/packages/package-a-spec.md` §3.3.
"""

from __future__ import annotations

import os
import pathlib
import re
import subprocess

DISPOSITION_PATH = "reviews/frontmatter-disposition.md"
HOME_ENV_VAR = "AI_METHODOLOGY_HOME"
HOME_SENTINEL = "bin/check-frontmatter"

_BACKTICKED = re.compile(r"`([^`]+)`")

#: The SHA of git's empty tree, used as the diff base before the first commit.
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"


class GitError(Exception):
    """A git invocation failed."""


def run(args, cwd=None, stdin=None):
    """Run git, returning `(returncode, stdout_bytes, stderr_text)`.

    Output is captured as bytes and decoded explicitly, so document content
    read out of git survives byte for byte.
    """
    try:
        proc = subprocess.run(
            ["git"] + [str(a) for a in args],
            cwd=str(cwd) if cwd is not None else None,
            input=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as exc:
        raise GitError("cannot run git in %s: %s" % (cwd, exc))
    return proc.returncode, proc.stdout, proc.stderr.decode("utf-8", "replace")


def git(*args, cwd=None, check=True):
    """Run git and return stripped stdout. Raises GitError on non-zero exit."""
    code, out, err = run(list(args), cwd=cwd)
    if check and code != 0:
        raise GitError("git %s failed: %s" % (" ".join(str(a) for a in args), err.strip()))
    return out.decode("utf-8", "replace").strip()


def repo_root(start=None):
    """Top level of the repo containing `start` (default: cwd)."""
    start = pathlib.Path(start) if start is not None else pathlib.Path.cwd()
    return pathlib.Path(git("rev-parse", "--show-toplevel", cwd=start))


def _is_home(candidate):
    if candidate is None:
        return False
    sentinel = pathlib.Path(candidate) / HOME_SENTINEL
    return sentinel.is_file() and os.access(str(sentinel), os.X_OK)


def methodology_home(root):
    """Locate the /ai clone: env var, then self-hosted repo, then sibling `ai`."""
    root = pathlib.Path(root)
    env_home = os.environ.get(HOME_ENV_VAR)
    for candidate in [
        pathlib.Path(env_home) if env_home else None,
        root,
        root.parent / "ai",
    ]:
        if _is_home(candidate):
            return pathlib.Path(candidate)
    raise LookupError(
        "cannot locate the ai methodology home. Set %s to your /ai clone, or "
        "clone it as a sibling directory named `ai` next to %s."
        % (HOME_ENV_VAR, root)
    )


def last_commit_sha(root, relpath):
    """Full SHA of the last commit touching `relpath`, or None if untracked."""
    code, out, _ = run(["log", "-1", "--format=%H", "--", str(relpath)], cwd=root)
    if code != 0:
        return None
    sha = out.decode("utf-8", "replace").strip()
    return sha or None


def file_at_rev(root, rev, relpath):
    """Content of `relpath` at `rev` (`:` for the index), or None if absent."""
    spec = "%s%s" % (rev, relpath) if str(rev).endswith(":") else "%s:%s" % (rev, relpath)
    code, out, _ = run(["show", spec], cwd=root)
    if code != 0:
        return None
    return out.decode("utf-8", "replace")


def staged_entries(root):
    """[(status letter, relpath)] for the staged set."""
    code, _, _ = run(["rev-parse", "--verify", "--quiet", "HEAD"], cwd=root)
    base = "HEAD" if code == 0 else EMPTY_TREE
    out = git("diff", "--cached", "--name-status", "-z", base, cwd=root)
    tokens = [t for t in out.split("\0") if t != ""]
    entries = []
    index = 0
    while index < len(tokens):
        letter = tokens[index][0]
        index += 1
        if letter in ("R", "C"):
            # old path, then new path; the new path is the one that matters.
            index += 1
            if index < len(tokens):
                entries.append((letter, tokens[index]))
                index += 1
        elif index < len(tokens):
            entries.append((letter, tokens[index]))
            index += 1
    return entries


def role_slugs(root, home=None):
    """Set of `roles/*.md` basenames, from the invoking repo or the home clone."""
    for base in [pathlib.Path(root), pathlib.Path(home) if home else None]:
        if base is None:
            continue
        roles = base / "roles"
        if roles.is_dir():
            return {p.stem for p in roles.glob("*.md")}
    return set()


def disposition_paths(root):
    """Paths named in the grandfather disposition list, or an empty set."""
    listing = pathlib.Path(root) / DISPOSITION_PATH
    if not listing.is_file():
        return set()
    return {
        value
        for value in _BACKTICKED.findall(listing.read_text())
        if value.endswith(".md")
    }
