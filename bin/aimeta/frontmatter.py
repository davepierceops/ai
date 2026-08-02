"""Frontmatter dialect: parse, render, validate.

The dialect is a documented subset of YAML (see
`docs/packages/package-a-spec.md` §3.1), parsed by hand so the tooling can
produce policy-shaped error codes and stay stdlib-only.

Contract: `docs/packages/package-a-spec.md` §3.1.
"""

from __future__ import annotations

import re

STATUSES = {"draft", "in-review", "agreed", "superseded", "deprecated"}
EXCLUDED_FIELDS = {"version", "last-modified", "author", "changelog"}
RESERVED_AUDIENCE = {"all-roles", "human"}
FIELD_ORDER = ["status", "last-reviewed", "audience", "superseded-by"]
LAST_REVIEWED_RE = r"^reviews/\S+\.md @ [0-9a-f]{7,40}$"

FENCE = "---"

_ITEM_RE = re.compile(r"^\s*-\s+(.*)$")


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
    """A parsed document: frontmatter fields plus the body after the fence.

    `leading` maps a key to the comment and blank lines written immediately
    above it, and `trailing` holds those after the last key. Per AC-FM-17 that
    trivia binds to the key below it and travels with that key when `render`
    reorders the block, so an unattended rewrite cannot delete authored text.
    """

    def __init__(
        self, fields=None, body="", has_frontmatter=False, errors=None,
        leading=None, trailing=None,
    ):
        self.fields = dict(fields or {})
        self.body = body
        self.has_frontmatter = has_frontmatter
        self.errors = list(errors or [])
        self.leading = {key: list(value) for key, value in (leading or {}).items()}
        self.trailing = list(trailing or [])

    def __repr__(self):
        return "Document(has_frontmatter=%r, fields=%r, body_len=%d)" % (
            self.has_frontmatter,
            self.fields,
            len(self.body),
        )


def parse_scalar(raw):
    """A scalar value: matching outer quotes are stripped, nothing else."""
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ("'", '"'):
        return raw[1:-1]
    return raw


def parse_value(raw):
    """Parse one frontmatter value per the dialect."""
    raw = raw.strip()
    if raw == "" or raw == "null":
        return None
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    return parse_scalar(raw)


def parse_text(text):
    """Parse document text into a Document. Never raises on malformed input.

    A document has frontmatter iff its first line is exactly `---` *and* a
    closing `---` line exists. An unclosed block is reported as a finding and
    the whole text is kept as the body, so no caller can destroy content it
    could not parse.
    """
    if not text.startswith(FENCE + "\n") and text.rstrip("\n") != FENCE:
        return Document(fields={}, body=text, has_frontmatter=False)

    lines = text.split("\n")
    close = None
    for index in range(1, len(lines)):
        if lines[index] == FENCE:
            close = index
            break
    if close is None:
        return Document(
            fields={},
            body=text,
            has_frontmatter=False,
            errors=[
                Finding(
                    "unclosed-frontmatter",
                    "frontmatter opens with `---` but is never closed",
                )
            ],
        )

    fields = {}
    errors = []
    leading = {}
    pending = []
    last_key = None
    for raw_line in lines[1:close]:
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            pending.append(raw_line)
            continue
        item = _ITEM_RE.match(raw_line)
        if item is not None:
            if last_key is None:
                errors.append(
                    Finding(
                        "malformed-frontmatter",
                        "list item with no preceding key: %r" % raw_line,
                    )
                )
            elif fields[last_key] is None or isinstance(fields[last_key], list):
                if not isinstance(fields[last_key], list):
                    fields[last_key] = []
                fields[last_key].append(parse_scalar(item.group(1).strip()))
            else:
                # AC-FM-18: the scalar is kept and the ambiguity is reported,
                # rather than the scalar being silently replaced by a list.
                errors.append(
                    Finding(
                        "malformed-frontmatter",
                        "list item %r follows scalar value %r for key %r"
                        % (raw_line, fields[last_key], last_key),
                    )
                )
            continue
        if ":" in raw_line:
            key, _, value = raw_line.partition(":")
            key = key.strip()
            if key:
                if key in fields:
                    errors.append(
                        Finding("duplicate-key", "key %r appears more than once" % key)
                    )
                fields[key] = parse_value(value)
                leading[key] = pending
                pending = []
                last_key = key
                continue
        errors.append(
            Finding("malformed-frontmatter", "cannot parse line: %r" % raw_line)
        )

    body = "\n".join(lines[close + 1 :])
    return Document(
        fields=fields,
        body=body,
        has_frontmatter=True,
        errors=errors,
        leading=leading,
        trailing=pending,
    )


def _render_value(value):
    if value is None:
        return "null"
    if isinstance(value, (list, tuple)):
        return "[%s]" % ", ".join(str(item) for item in value)
    return str(value)


def render(doc):
    """Serialize a Document back to text, canonicalizing field order."""
    if not doc.has_frontmatter:
        return doc.body
    ordered = [key for key in FIELD_ORDER if key in doc.fields]
    ordered += [key for key in doc.fields if key not in FIELD_ORDER]
    lines = [FENCE]
    for key in ordered:
        lines.extend(doc.leading.get(key, []))
        lines.append("%s: %s" % (key, _render_value(doc.fields[key])))
    lines.extend(doc.trailing)
    lines.append(FENCE)
    return "\n".join(lines) + "\n" + doc.body


def with_fields(doc, updates):
    """Return a new Document with `updates` applied to its fields."""
    fields = dict(doc.fields)
    for key, value in updates.items():
        fields[key] = value
    return Document(
        fields=fields,
        body=doc.body,
        has_frontmatter=doc.has_frontmatter,
        errors=list(doc.errors),
        leading=doc.leading,
        trailing=doc.trailing,
    )


def _audience_values(value):
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]


def validate(doc, *, path=None, role_slugs=None, grandfathered=False):
    """Return policy findings for a document. Empty list means compliant.

    Structural parse findings live on `doc.errors`; callers that want both
    report `doc.errors + validate(doc, ...)`.
    """
    findings = []
    if not doc.has_frontmatter:
        return [Finding("missing-frontmatter", "no YAML frontmatter block")]

    known_roles = set(role_slugs or ())
    fields = doc.fields

    status = fields.get("status")
    if "status" not in fields or status is None:
        findings.append(Finding("missing-status", "`status` is required"))
    elif status not in STATUSES:
        findings.append(
            Finding(
                "invalid-status",
                "status %r is not one of %s" % (status, ", ".join(sorted(STATUSES))),
            )
        )

    review = fields.get("last-reviewed")
    if "last-reviewed" not in fields:
        findings.append(
            Finding("missing-last-reviewed", "`last-reviewed` is required (null is allowed)")
        )
    elif review is not None:
        if not isinstance(review, str) or not re.match(LAST_REVIEWED_RE, review):
            findings.append(
                Finding(
                    "invalid-last-reviewed",
                    "last-reviewed %r is not `<reviews/path.md> @ <sha>`" % (review,),
                )
            )

    if status == "agreed" and review is None and not grandfathered:
        findings.append(
            Finding(
                "agreed-without-review",
                "status: agreed requires a non-null last-reviewed",
            )
        )

    if "audience" not in fields or fields.get("audience") is None:
        findings.append(Finding("missing-audience", "`audience` is required"))
    elif isinstance(fields["audience"], (list, tuple)) and not fields["audience"]:
        findings.append(Finding("empty-audience", "`audience` may not be empty"))
    else:
        for value in _audience_values(fields["audience"]):
            if value not in RESERVED_AUDIENCE and value not in known_roles:
                findings.append(
                    Finding(
                        "invalid-audience",
                        "audience value %r is neither a reserved value nor a role slug"
                        % (value,),
                    )
                )

    pointer = fields.get("superseded-by")
    if status == "superseded" and pointer is None:
        findings.append(
            Finding("superseded-without-pointer", "status: superseded requires superseded-by")
        )
    if pointer is not None and status != "superseded":
        findings.append(
            Finding(
                "superseded-by-without-status",
                "superseded-by is set but status is %r" % (status,),
            )
        )

    for key in fields:
        if key in EXCLUDED_FIELDS:
            findings.append(
                Finding("excluded-field", "field %r is derivable from git and excluded" % key)
            )

    return findings
