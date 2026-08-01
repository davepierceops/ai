"""Shared plumbing for the aimeta command-line tools.

Exit codes are the contract (`docs/packages/package-a-spec.md` §2.4), and all
human-readable diagnostics go to stderr (§6, D2) so stdout stays reserved for
machine-consumable output.
"""

from __future__ import annotations

import os
import pathlib
import sys

from . import repo, scope

EXIT_OK = 0
EXIT_POLICY = 1
EXIT_USAGE = 2
EXIT_PRECONDITION = 3
EXIT_SELF_VERIFY = 4


class ToolError(Exception):
    """A diagnostic plus the exit code the CLI should return."""

    def __init__(self, message, code=EXIT_USAGE):
        Exception.__init__(self, message)
        self.message = message
        self.code = code


def err(line):
    """One human-readable diagnostic line, on stderr."""
    print(line, file=sys.stderr)


def diagnostic(severity, path, code, message):
    err("%s %s: [%s] %s" % (severity, path, code, message))


class Context:
    """The invoking repo plus everything derived from the methodology home."""

    def __init__(self, root, home, globs, role_slugs, disposition):
        self.root = root
        self.home = home
        self.globs = globs
        self.role_slugs = role_slugs
        self.disposition = disposition

    def grandfathered(self, relpath):
        return relpath in self.disposition

    def in_scope(self, relpath):
        return scope.matches(relpath, self.globs)


def load_root(start=None):
    """The invoking repo's top level, or a clean usage error outside a repo."""
    try:
        return repo.repo_root(start)
    except repo.GitError as exc:
        raise ToolError("not inside a git repository: %s" % exc, EXIT_USAGE)


def load_context(start=None):
    """Resolve the invoking repo, the methodology home, and the in-scope set."""
    root = load_root(start)
    try:
        home = repo.methodology_home(root)
    except LookupError as exc:
        raise ToolError(str(exc), EXIT_USAGE)
    try:
        globs = scope.load_globs(home)
    except scope.ScopeError as exc:
        raise ToolError(
            "cannot read the in-scope set from the metadata policy: %s" % exc,
            EXIT_PRECONDITION,
        )
    return Context(
        root=root,
        home=home,
        globs=globs,
        role_slugs=repo.role_slugs(root, home),
        disposition=repo.disposition_paths(root),
    )


def relpath_of(root, argument):
    """Normalize a command-line path to a repo-relative, slash-separated path."""
    path = pathlib.Path(argument)
    if not path.is_absolute():
        path = pathlib.Path.cwd() / path
    try:
        rel = os.path.relpath(str(path.resolve()), str(pathlib.Path(root).resolve()))
    except ValueError as exc:
        raise ToolError("%s is outside the repository: %s" % (argument, exc), EXIT_POLICY)
    rel = rel.replace(os.sep, "/")
    if rel == ".." or rel.startswith("../"):
        raise ToolError("%s is outside the repository" % argument, EXIT_POLICY)
    return rel


def in_scope_files(ctx):
    """Every in-scope document in the invoking repo's working tree, sorted."""
    found = []
    for dirpath, dirnames, filenames in os.walk(str(ctx.root)):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), str(ctx.root))
            rel = rel.replace(os.sep, "/")
            if ctx.in_scope(rel):
                found.append(rel)
    return sorted(found)


def report(findings, path):
    """Print one `ERROR <path>: [code] <message>` line per finding."""
    for finding in findings:
        diagnostic("ERROR", path, finding.code, finding.message)


def run(main_func, argv=None):
    """Invoke a CLI main, turning ToolError into a diagnostic and an exit code."""
    try:
        return main_func(argv)
    except ToolError as exc:
        err("ERROR: %s" % exc.message)
        return exc.code
    except repo.GitError as exc:
        err("ERROR: %s" % exc)
        return EXIT_PRECONDITION
    except BrokenPipeError:
        return EXIT_OK
