"""The expedited log's content rule: a cited SHA must be named by an entry.

Contract: `OPEN-ITEMS.md`, "The expedited path's log entry is unenforced —
`flip-agreed` checks existence, not content", and the rule it points at in
`policies/document-metadata-policy.md` ("The record").

Why this is not part of `frontmatter.validate`: the rule is not a fact about
the document. Deciding it needs the log's contents and needs git to resolve an
abbreviation, and `frontmatter` is deliberately pure and stdlib-only so the
dialect can be reasoned about without a repository.

**Fail closed everywhere.** Every branch that cannot *prove* the SHA is named
by an entry reports — an unreadable log, an unresolvable SHA, an entry whose
SHA git does not recognize. The failure this exists to stop is a pointer that
silently claims a review nobody did, so an ambiguous answer has to cost a
diagnostic rather than a pass.
"""

from __future__ import annotations

import re

from . import frontmatter, repo

#: The one artifact whose *contents* are checked. Named here rather than
#: derived, on the same design as `repo.DISPOSITION_PATH`: the policy states
#: the path literally, and parsing prose for it would add a failure mode
#: without adding a fact.
LOG_PATH = "reviews/expedited-log.md"

#: A SHA as it appears in an entry: after the `@` separator the log's format
#: line defines. Anchoring on `@` is what keeps a SHA mentioned in the header
#: prose from counting as an entry.
_ENTRY_SHA_RE = re.compile(r"@\s+([0-9a-f]{7,40})\b")

_LIST_ITEM_PREFIXES = ("-", "*")


def is_log(artifact):
    """True when this review pointer targets the expedited log."""
    return artifact == LOG_PATH


def split_pointer(review):
    """`(artifact, sha)` from a `<reviews/path.md> @ <sha>` pointer."""
    artifact, _, sha = review.partition(" @ ")
    return artifact, sha


def resolve(root, sha):
    """Full SHA of the commit `sha` names, or None when git does not know it."""
    code, out, _ = repo.run(
        ["rev-parse", "--verify", "--quiet", "%s^{commit}" % sha], cwd=root
    )
    if code != 0:
        return None
    resolved = out.decode("ascii", "replace").strip()
    return resolved or None


def entry_shas(text):
    """Every SHA named by a log *entry*, in order.

    An entry is a Markdown list item, per the format the log documents. The
    header prose and the format template are not entries, and a SHA that only
    appears there does not satisfy a pointer.
    """
    found = []
    for line in text.splitlines():
        if not line.lstrip().startswith(_LIST_ITEM_PREFIXES):
            continue
        found.extend(_ENTRY_SHA_RE.findall(line))
    return found


def names_sha(root, log_text, sha):
    """True when an entry in `log_text` names the same commit as `sha`.

    Comparison is between *resolved* SHAs on both sides, per the policy: an
    abbreviated pointer against a full-length entry is the same SHA and a
    different string, and either side may be the abbreviated one.
    """
    target = resolve(root, sha)
    if target is None:
        return False
    return any(resolve(root, candidate) == target for candidate in entry_shas(log_text))


def read_log(root):
    """`(text, finding)` for the log; one is always None."""
    path = root / LOG_PATH
    if not path.is_file():
        return None, frontmatter.Finding(
            "expedited-log-missing",
            "last-reviewed cites %s, which does not exist" % LOG_PATH,
        )
    try:
        return path.read_bytes().decode("utf-8"), None
    except (OSError, UnicodeDecodeError) as exc:
        return None, frontmatter.Finding(
            "expedited-log-unreadable",
            "cannot read %s to confirm the cited SHA: %s" % (LOG_PATH, exc),
        )


def check_pointer(root, review):
    """Findings for one `last-reviewed` pointer. Empty list means it holds.

    A pointer at any other artifact is not this rule's business and returns
    nothing — existence-only behaviour there is unchanged.
    """
    artifact, sha = split_pointer(review)
    if not is_log(artifact):
        return []
    log_text, finding = read_log(root)
    if finding is not None:
        return [finding]
    if resolve(root, sha) is None:
        return [
            frontmatter.Finding(
                "expedited-sha-unresolvable",
                "last-reviewed cites %s, which does not resolve to a commit, so it "
                "cannot be matched against %s" % (sha, LOG_PATH),
            )
        ]
    if not names_sha(root, log_text, sha):
        return [
            frontmatter.Finding(
                "expedited-sha-not-in-log",
                "no entry in %s names %s; a pointer to a SHA the log does not name "
                "is a false claim of review" % (LOG_PATH, sha),
            )
        ]
    return []


def check_document(root, doc):
    """Findings for a parsed document's `last-reviewed`, if it has one."""
    review = doc.fields.get("last-reviewed")
    if not isinstance(review, str):
        return []
    return check_pointer(root, review)
