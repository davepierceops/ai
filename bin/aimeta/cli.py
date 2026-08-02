"""Shared plumbing for the aimeta command-line tools.

Exit codes are the contract (`docs/packages/package-a-spec.md` §2.4), and all
human-readable diagnostics go to stderr (§6, D2) so stdout stays reserved for
machine-consumable output.
"""

from __future__ import annotations

import os
import pathlib
import sys

from . import frontmatter, repo, scope

EXIT_OK = 0
EXIT_POLICY = 1
EXIT_USAGE = 2
EXIT_PRECONDITION = 3
EXIT_SELF_VERIFY = 4

ENCODING = "utf-8"


def configure_streams():
    """Pin stdout/stderr to UTF-8 regardless of the ambient locale (AC-X-7).

    A hook spawned by a GUI client can run under `LC_ALL=C`, where the platform
    default is ASCII and a single em-dash would otherwise abort the run.
    """
    for stream, errors in ((sys.stdout, "strict"), (sys.stderr, "replace")):
        try:
            stream.reconfigure(encoding=ENCODING, errors=errors)
        except (AttributeError, OSError, ValueError):  # pragma: no cover
            pass


configure_streams()


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


def real_case(root, relpath):
    """`relpath` with each component corrected to the case on disk (AC-CF-20).

    On a case-insensitive filesystem `Policies/x.md` opens the file but does
    not match the `policies/**` glob, so scope matching silently passes over a
    real document. Resolution is per component because only the filesystem
    knows the true spelling.
    """
    current = pathlib.Path(root)
    parts = []
    for part in relpath.split("/"):
        if not (current / part).exists():
            return "/".join(parts + relpath.split("/")[len(parts):])
        try:
            names = os.listdir(str(current))
        except OSError:
            names = []
        if part not in names:
            folded = [name for name in names if name.lower() == part.lower()]
            part = folded[0] if folded else part
        parts.append(part)
        current = current / part
    return "/".join(parts)


def relpath_of(root, argument, code=EXIT_POLICY):
    """Normalize a command-line path to a repo-relative, slash-separated path."""
    path = pathlib.Path(argument)
    if not path.is_absolute():
        path = pathlib.Path.cwd() / path
    try:
        rel = os.path.relpath(str(path.resolve()), str(pathlib.Path(root).resolve()))
    except ValueError as exc:
        raise ToolError("%s is outside the repository: %s" % (argument, exc), code)
    rel = rel.replace(os.sep, "/")
    if rel == ".." or rel.startswith("../"):
        raise ToolError("%s is outside the repository" % argument, code)
    return real_case(root, rel)


def read_document(path):
    """Read a document as UTF-8. Returns `(text, finding)`; one is always None."""
    try:
        return pathlib.Path(path).read_bytes().decode(ENCODING), None
    except UnicodeDecodeError as exc:
        return None, frontmatter.Finding(
            "undecodable", "not valid UTF-8 (%s); refusing to guess an encoding" % exc
        )
    except OSError as exc:
        return None, frontmatter.Finding("unreadable", "cannot read the file: %s" % exc)


def decode_blob(blob):
    """Decode a git blob strictly. Returns `(text, finding)`."""
    try:
        return blob.decode(ENCODING), None
    except UnicodeDecodeError as exc:
        return None, frontmatter.Finding(
            "undecodable", "not valid UTF-8 (%s); refusing to guess an encoding" % exc
        )


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


def unmatched_globs(ctx, relpaths):
    """Configured globs that match nothing in this repo (AC-CF-19)."""
    return [
        glob
        for glob in ctx.globs
        if not any(scope.matches(relpath, [glob]) for relpath in relpaths)
    ]


def report_scope(ctx, relpaths):
    """State what the in-scope set actually matched, so silence is informative."""
    err(
        "NOTE in-scope: [scope-summary] %d file(s) matched, from %d configured glob(s)"
        % (len(relpaths), len(ctx.globs))
    )
    for glob in unmatched_globs(ctx, relpaths):
        diagnostic(
            "WARN",
            glob,
            "unmatched-glob",
            "this in-scope glob matches no path in this repo, so it enforces nothing",
        )


def report(findings, path):
    """Print one `ERROR <path>: [code] <message>` line per finding."""
    for finding in findings:
        diagnostic("ERROR", path, finding.code, finding.message)


def run(main_func, argv=None):
    """Invoke a CLI main, turning any exception into a diagnostic and an exit code.

    AC-X-6: no CLI ever emits a traceback. The catch-all is a backstop, not the
    handling — conditions with a meaningful code (an undecodable document, a
    refused precondition) are reported where they are detected.
    """
    try:
        return main_func(argv)
    except ToolError as exc:
        err("ERROR: %s" % exc.message)
        return exc.code
    except repo.GitError as exc:
        err("ERROR: %s" % exc)
        return EXIT_PRECONDITION
    except BrokenPipeError:
        # A consumer that closes early (`| head`) still reaches the
        # interpreter's own final flush, which reports exit 120 regardless of
        # what is done here. Recorded as a known gap rather than worked around.
        return EXIT_OK
    except Exception as exc:  # noqa: BLE001 - deliberate: no traceback ever escapes
        err("ERROR: [internal-error] %s: %s" % (type(exc).__name__, exc))
        return EXIT_PRECONDITION
