"""Reference closure over documents, shared by `bin/bundle` and `bin/cycle-open`.

Edges are (a) `depends-on:` frontmatter entries resolved to
`context-sets/<name>.md` and (b) backticked repo-relative `*.md` paths in the
body that exist as files in the repo. Only declared `depends-on` edges are
strict: a backticked string that is not a repo file is prose, not a broken
reference.

Contract: `docs/packages/package-a-spec.md` §3.7.
"""

from __future__ import annotations

import re

from . import cli, frontmatter

BACKTICKED = re.compile(r"`([^`]+)`")


def resolve_entry(root, entry):
    """An ENTRY is a repo-relative path or a context-set name."""
    for candidate in [entry, "context-sets/%s.md" % entry]:
        if (root / candidate).is_file():
            return candidate
    raise cli.ToolError("cannot resolve entry %r to a file" % entry, cli.EXIT_USAGE)


def references(root, relpath, dangling):
    """Outgoing edges from `relpath`, in discovery order."""
    doc = frontmatter.parse_text((root / relpath).read_text())
    edges = []
    depends = doc.fields.get("depends-on") or []
    if isinstance(depends, str):
        depends = [depends]
    for name in depends:
        target = name if name.endswith(".md") else "context-sets/%s.md" % name
        if (root / target).is_file():
            edges.append(target)
        else:
            dangling.append((relpath, target))
            cli.diagnostic(
                "WARN",
                relpath,
                "dangling-reference",
                "depends-on %r resolves to %s, which is not a file" % (name, target),
            )
    for value in BACKTICKED.findall(doc.body):
        if value.endswith(".md") and (root / value).is_file():
            edges.append(value)
    return edges


def walk(root, entries, max_depth=None, dangling=None):
    """Breadth-first by depth, ties broken lexicographically, no duplicates.

    Returns `[{"path": ..., "depth": ..., "via": ...}]` with the entry points
    first, in argument order, each carrying `via: None`.
    """
    dangling = [] if dangling is None else dangling
    walked = []
    seen = set()
    frontier = []
    for entry in entries:
        if entry not in seen:
            seen.add(entry)
            frontier.append(entry)
            walked.append({"path": entry, "depth": 0, "via": None})

    depth = 0
    while frontier and (max_depth is None or depth < max_depth):
        depth += 1
        discovered = {}
        for path in frontier:
            for target in references(root, path, dangling):
                if target not in seen and target not in discovered:
                    discovered[target] = path
        frontier = sorted(discovered)
        for target in frontier:
            seen.add(target)
            walked.append({"path": target, "depth": depth, "via": discovered[target]})
    return walked
