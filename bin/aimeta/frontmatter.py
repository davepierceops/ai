"""Frontmatter dialect: parse, render, validate.

STUB — interface contract only. Behaviour is deliberately inert so that the
pre-implementation test run is a *behavioural* red-gate (tests fail on wrong
answers, not on a missing module). See
`context-sets/spec-and-change-discipline.md`.

Contract: `docs/packages/package-a-spec.md` §3.1.
"""

from __future__ import annotations

STATUSES = {"draft", "in-review", "agreed", "superseded", "deprecated"}
EXCLUDED_FIELDS = {"version", "last-modified", "author", "changelog"}
RESERVED_AUDIENCE = {"all-roles", "human"}
FIELD_ORDER = ["status", "last-reviewed", "audience", "superseded-by"]
LAST_REVIEWED_RE = r"^reviews/\S+\.md @ [0-9a-f]{7,40}$"

FENCE = "---"


class Finding:
    """A single structural or policy finding about a document."""

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __repr__(self):
        return "Finding(code=%r, message=%r)" % (self.code, self.message)

    def __eq__(self, other):
        return (
            isinstance(other, Finding)
            and self.code == other.code
            and self.message == other.message
        )

    def __hash__(self):
        return hash((self.code, self.message))


class Document:
    """A parsed document: frontmatter fields plus the body after the fence."""

    def __init__(self, fields=None, body="", has_frontmatter=False, errors=None):
        self.fields = dict(fields or {})
        self.body = body
        self.has_frontmatter = has_frontmatter
        self.errors = list(errors or [])

    def __repr__(self):
        return "Document(has_frontmatter=%r, fields=%r, body_len=%d)" % (
            self.has_frontmatter,
            self.fields,
            len(self.body),
        )


def parse_text(text):
    """Parse document text into a Document. Never raises on malformed input."""
    # STUB: claims every document is frontmatter-free.
    return Document(fields={}, body=text, has_frontmatter=False, errors=[])


def render(doc):
    """Serialize a Document back to text, canonicalizing field order."""
    # STUB: drops the frontmatter entirely.
    return doc.body


def with_fields(doc, updates):
    """Return a new Document with `updates` applied to its fields."""
    # STUB: returns the input unchanged.
    return doc


def validate(doc, path=None, role_slugs=None, grandfathered=False):
    """Return policy findings for a document. Empty list means compliant."""
    # STUB: accepts everything.
    return []
