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


def run(args, cwd=None, stdin=None, env=None):
    """Run git, returning `(returncode, stdout_bytes, stderr_text)`.

    Output is captured as bytes and never decoded on the caller's behalf, so
    document content read out of git survives byte for byte (AC-CF-14).
    `env`, when given, is overlaid on the inherited environment — that is how
    the hook reaches the *real* index while running against a temporary one.
    """
    if env is not None:
        merged = dict(os.environ)
        merged.update(env)
        env = merged
    try:
        proc = subprocess.run(
            ["git"] + [str(a) for a in args],
            cwd=str(cwd) if cwd is not None else None,
            input=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
    except OSError as exc:
        raise GitError("cannot run git in %s: %s" % (cwd, exc))
    return proc.returncode, proc.stdout, proc.stderr.decode("utf-8", "replace")


def git(*args, cwd=None, check=True, env=None):
    """Run git and return stripped stdout. Raises GitError on non-zero exit."""
    code, out, err = run(list(args), cwd=cwd, env=env)
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


def blob_at_rev(root, rev, relpath):
    """Raw bytes of `relpath` at `rev` (`:` for the index), or None if absent.

    Bytes, never text: the flip path must not transcode a document it cannot
    decode (AC-CF-14).
    """
    spec = "%s%s" % (rev, relpath) if str(rev).endswith(":") else "%s:%s" % (rev, relpath)
    code, out, _ = run(["cat-file", "blob", spec], cwd=root)
    if code != 0:
        return None
    return out


def short_blob_sha(root, rev, relpath):
    """Short SHA of `relpath`'s own blob at `rev` (`:` for the index), or None.

    This is the file's own content hash (`git rev-parse --short <rev>:<path>`),
    never the commit SHA at `rev` — callers that want the commit SHA already
    have `git rev-parse <rev>` or `last_commit_sha` for that.
    """
    spec = "%s%s" % (rev, relpath) if str(rev).endswith(":") else "%s:%s" % (rev, relpath)
    code, out, _ = run(["rev-parse", "--short", spec], cwd=root)
    if code != 0:
        return None
    return out.decode("utf-8", "replace").strip()


def file_at_rev(root, rev, relpath):
    """Content of `relpath` at `rev` (`:` for the index), or None if absent.

    Decoding is **strict**: a `UnicodeDecodeError` here is a real condition the
    caller must report, not something to paper over with replacement
    characters. Callers that may meet non-UTF-8 content use `blob_at_rev`.
    """
    blob = blob_at_rev(root, rev, relpath)
    if blob is None:
        return None
    return blob.decode("utf-8")


def index_entry(root, relpath, env=None):
    """`(mode, sha)` for the staged entry, or `(None, None)` when absent."""
    entry = git("ls-files", "--stage", "--", relpath, cwd=root, env=env)
    if not entry:
        return None, None
    parts = entry.split()
    return parts[0], parts[1]


def real_index_path(root):
    """The repository's own index file, even when `$GIT_INDEX_FILE` overrides it.

    Derived from the git directory rather than `rev-parse --git-path index`,
    which honours `$GIT_INDEX_FILE` and so answers with the temporary index
    inside a hook — exactly the case this function exists to detect.
    """
    return os.path.abspath(
        os.path.join(git("rev-parse", "--absolute-git-dir", cwd=root), "index")
    )


def using_temporary_index(root):
    """True when git handed us a temporary index, as `git commit -- <path>` does."""
    override = os.environ.get("GIT_INDEX_FILE")
    if not override:
        return False
    return os.path.abspath(os.path.join(str(root), override)) != real_index_path(root)


def installable_index_path(root):
    """The file that will *be* the repository index once this command finishes.

    A pathspec commit holds `index.lock` for the whole hook, so the real index
    cannot be written directly — but git installs that lock file as the index
    when it finishes, and git has already written the pre-hook index into it
    and closed it (verified with `lsof`: no open descriptor survives into the
    hook, so there is no fd-versus-path race). Updating it is therefore the
    only way a pre-commit hook can keep the real index honest.

    **This depends on undocumented git ordering, verified on git 2.54.0 only.**
    It degrades safely with respect to *corruption* — `git update-index`
    refuses a malformed lock rather than writing garbage, and the blast radius
    is the post-commit index, never history. It does **not** degrade safely
    with respect to *enforcement*: if a future git wrote the lock after the
    hook instead, the mirror would be silently discarded and defect B2 would
    return. That is why every failure of this path is loud and blocking
    (AC-CF-22) rather than a warning, and why the assumption carries a standing
    re-verification obligation (spec §8.6).
    """
    index = real_index_path(root)
    pending = index + ".lock"
    return pending if os.path.exists(pending) else index


def merge_in_progress(root):
    """True when `MERGE_HEAD` exists — the commit being made is a merge."""
    return os.path.isfile(
        os.path.join(str(root), git("rev-parse", "--git-path", "MERGE_HEAD", cwd=root))
    )


def staged_rename_sources(root):
    """`{new_path: old_path}` for staged renames and copies."""
    code, _, _ = run(["rev-parse", "--verify", "--quiet", "HEAD"], cwd=root)
    base = "HEAD" if code == 0 else EMPTY_TREE
    out = git("diff", "--cached", "--name-status", "-z", base, cwd=root)
    tokens = [t for t in out.split("\0") if t != ""]
    sources = {}
    index = 0
    while index < len(tokens):
        letter = tokens[index][0]
        index += 1
        if letter in ("R", "C"):
            if index + 1 < len(tokens):
                sources[tokens[index + 1]] = tokens[index]
            index += 2
        else:
            index += 1
    return sources


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
        for value in _BACKTICKED.findall(listing.read_text(encoding="utf-8"))
        if value.endswith(".md")
    }
