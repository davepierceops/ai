"""AC-FM-*: the frontmatter dialect — parse, render, validate.

Contract: `docs/packages/package-a-spec.md` §3.1. These are pure unit tests;
no git and no filesystem are involved.
"""

from __future__ import annotations

import unittest

from aimeta import frontmatter as fm

from tests.helpers import agreed_doc, code_set, codes, frontmatter_block


ROLE_SLUGS = {"coder-agent", "test-designer-agent", "reviewer-agent"}


def validate(text, path="policies/sample.md", role_slugs=None, grandfathered=False):
    doc = fm.parse_text(text)
    return fm.validate(
        doc,
        path=path,
        role_slugs=ROLE_SLUGS if role_slugs is None else role_slugs,
        grandfathered=grandfathered,
    )


class TestParse(unittest.TestCase):
    def test_fm1_parses_fields_and_exact_body(self):
        """AC-FM-1: frontmatter is detected; body is the text after the fence."""
        text = (
            "---\n"
            "status: draft\n"
            "last-reviewed: null\n"
            "audience: [all-roles]\n"
            "---\n"
            "\n# Title\n\nBody line.\n"
        )
        doc = fm.parse_text(text)
        self.assertTrue(doc.has_frontmatter)
        self.assertEqual(doc.fields.get("status"), "draft")
        self.assertIsNone(doc.fields.get("last-reviewed"))
        self.assertEqual(doc.fields.get("audience"), ["all-roles"])
        # Only the newline ending the closing fence is consumed.
        self.assertEqual(doc.body, "\n# Title\n\nBody line.\n")

    def test_fm1_field_insertion_order_is_preserved(self):
        """AC-FM-1: `fields` is insertion-ordered as the document had them."""
        text = "---\naudience: [human]\nstatus: draft\nzz: 1\n---\nbody\n"
        doc = fm.parse_text(text)
        self.assertEqual(list(doc.fields.keys()), ["audience", "status", "zz"])

    def test_fm1_trailing_content_after_fence_is_not_stripped(self):
        """AC-FM-1: nothing beyond the fence newline is stripped from the body."""
        text = "---\nstatus: draft\n---\n\n\nleading blanks kept\n\n"
        doc = fm.parse_text(text)
        self.assertEqual(doc.body, "\n\nleading blanks kept\n\n")

    def test_fm2_no_frontmatter(self):
        """AC-FM-2: no leading fence means no frontmatter and an intact body."""
        text = "# Title\n\nStatus: stable\n\nBody.\n"
        doc = fm.parse_text(text)
        self.assertFalse(doc.has_frontmatter)
        self.assertEqual(doc.fields, {})
        self.assertEqual(doc.body, text)

    def test_fm2_fence_not_on_first_line_is_not_frontmatter(self):
        """AC-FM-2: the fence only counts as the exact first line."""
        text = "\n---\nstatus: draft\n---\nbody\n"
        doc = fm.parse_text(text)
        self.assertFalse(doc.has_frontmatter)
        self.assertEqual(doc.body, text)

    def test_fm3_unclosed_frontmatter_is_a_finding_not_an_exception(self):
        """AC-FM-3: an unclosed block yields `unclosed-frontmatter`, no raise."""
        text = "---\nstatus: draft\naudience: [human]\n"
        doc = fm.parse_text(text)
        self.assertIn("unclosed-frontmatter", code_set(doc.errors))


class TestValueDialect(unittest.TestCase):
    def test_fm4_null_and_empty_become_none(self):
        """AC-FM-4: `null` and an empty value both parse to None."""
        doc = fm.parse_text("---\na: null\nb:\n---\nbody\n")
        self.assertIn("a", doc.fields)
        self.assertIn("b", doc.fields)
        self.assertIsNone(doc.fields["a"])
        self.assertIsNone(doc.fields["b"])

    def test_fm4_inline_list(self):
        """AC-FM-4: `[a, b]` parses to a list of strings."""
        doc = fm.parse_text("---\naudience: [all-roles, coder-agent]\n---\nbody\n")
        self.assertEqual(doc.fields.get("audience"), ["all-roles", "coder-agent"])

    def test_fm4_empty_inline_list(self):
        """AC-FM-4: `[]` parses to an empty list, not None."""
        doc = fm.parse_text("---\ndepends-on: []\n---\nbody\n")
        self.assertEqual(doc.fields.get("depends-on"), [])

    def test_fm4_block_list_continuation(self):
        """AC-FM-4: `- item` lines continue the preceding key as a list."""
        doc = fm.parse_text("---\naudience:\n- all-roles\n- human\n---\nbody\n")
        self.assertEqual(doc.fields.get("audience"), ["all-roles", "human"])

    def test_fm4_quoted_scalar_loses_exactly_its_outer_quotes(self):
        """AC-FM-4: matching outer quotes are stripped; inner ones survive."""
        doc = fm.parse_text(
            "---\n"
            'a: "quoted"\n'
            "b: 'single'\n"
            'c: "he said \'hi\'"\n'
            "---\nbody\n"
        )
        self.assertEqual(doc.fields.get("a"), "quoted")
        self.assertEqual(doc.fields.get("b"), "single")
        self.assertEqual(doc.fields.get("c"), "he said 'hi'")

    def test_fm4_mismatched_quotes_are_verbatim(self):
        """AC-FM-4: non-matching quotes are not a quoted scalar."""
        doc = fm.parse_text("---\na: \"unbalanced'\n---\nbody\n")
        self.assertEqual(doc.fields.get("a"), "\"unbalanced'")

    def test_fm4_review_pointer_is_verbatim_string(self):
        """AC-FM-4: `reviews/x.md @ abc1234` parses as that verbatim string."""
        doc = fm.parse_text("---\nlast-reviewed: reviews/x.md @ abc1234\n---\nbody\n")
        self.assertEqual(doc.fields.get("last-reviewed"), "reviews/x.md @ abc1234")

    def test_fm4_blank_and_comment_lines_are_ignored(self):
        """AC-FM-4: blank lines and `#` comments inside the block are inert."""
        doc = fm.parse_text("---\n\n# a comment\nstatus: draft\n---\nbody\n")
        self.assertEqual(list(doc.fields.keys()), ["status"])
        self.assertEqual(codes(doc.errors), [])


class TestStructuralFindings(unittest.TestCase):
    def test_fm5_duplicate_key(self):
        """AC-FM-5: a repeated key produces `duplicate-key`."""
        doc = fm.parse_text("---\nstatus: draft\nstatus: agreed\n---\nbody\n")
        self.assertIn("duplicate-key", code_set(doc.errors))

    def test_fm5_malformed_line(self):
        """AC-FM-5: a line that is neither `key: value` nor `- item` is malformed."""
        doc = fm.parse_text("---\nstatus: draft\nthis is not a field\n---\nbody\n")
        self.assertIn("malformed-frontmatter", code_set(doc.errors))

    def test_fm5_leading_dash_without_a_preceding_key_is_malformed(self):
        """AC-FM-5: a `- item` with no preceding key is malformed."""
        doc = fm.parse_text("---\n- orphan\nstatus: draft\n---\nbody\n")
        self.assertIn("malformed-frontmatter", code_set(doc.errors))

    def test_fm5_wellformed_block_has_no_structural_findings(self):
        """AC-FM-5: a well-formed block produces no structural findings."""
        doc = fm.parse_text(agreed_doc())
        self.assertEqual(codes(doc.errors), [])


class TestRender(unittest.TestCase):
    SAMPLES = [
        agreed_doc(),
        "---\nstatus: draft\n---\n",
        "---\nstatus: draft\n---\n\n\nbody with blanks\n\n",
        "---\ncontext-set: base\ndepends-on: []\n---\n\n# Context Set\n\nProse.\n",
        "no frontmatter at all\n",
        "---\nstatus: draft\n---\ntrailing without newline",
    ]

    def test_fm6_body_survives_a_parse_render_parse_round_trip(self):
        """AC-FM-6: render preserves the body byte for byte."""
        for text in self.SAMPLES:
            with self.subTest(text=text[:40]):
                once = fm.parse_text(text)
                # Precondition: a round trip over a document that was never
                # recognised as having frontmatter would prove nothing.
                self.assertEqual(once.has_frontmatter, text.startswith("---\n"))
                twice = fm.parse_text(fm.render(once))
                self.assertEqual(twice.body, once.body)

    def test_fm6_fields_survive_a_render_round_trip(self):
        """AC-FM-6: a render round trip is field-preserving as well as body-preserving."""
        doc = fm.parse_text(agreed_doc())
        self.assertEqual(doc.fields.get("status"), "agreed")
        again = fm.parse_text(fm.render(doc))
        self.assertEqual(again.fields, doc.fields)

    def test_fm7_known_fields_render_in_field_order(self):
        """AC-FM-7: FIELD_ORDER fields come first, in that order."""
        text = (
            "---\n"
            "superseded-by: null\n"
            "audience: [all-roles]\n"
            "last-reviewed: null\n"
            "status: draft\n"
            "---\nbody\n"
        )
        rendered = fm.render(fm.parse_text(text))
        keys = [
            line.split(":", 1)[0]
            for line in rendered.splitlines()[1:]
            if line and line != "---" and ":" in line
        ]
        self.assertEqual(keys[: len(fm.FIELD_ORDER)], fm.FIELD_ORDER)

    def test_fm7_unknown_fields_follow_in_original_relative_order(self):
        """AC-FM-7: unknown fields render after the known ones, order preserved."""
        text = (
            "---\n"
            "zeta: 1\n"
            "status: draft\n"
            "alpha: 2\n"
            "---\nbody\n"
        )
        rendered = fm.render(fm.parse_text(text))
        self.assertLess(rendered.index("status:"), rendered.index("zeta:"))
        self.assertLess(rendered.index("zeta:"), rendered.index("alpha:"))

    def test_fm7_none_renders_as_null_and_lists_render_inline(self):
        """AC-FM-7: None renders as `null`; a list renders as `[a, b]`."""
        doc = fm.parse_text("---\nstatus: draft\nsuperseded-by: null\naudience:\n- a\n- b\n---\nbody\n")
        rendered = fm.render(doc)
        self.assertIn("superseded-by: null", rendered)
        self.assertIn("audience: [a, b]", rendered)

    def test_fm7_composition_fields_survive_round_trip(self):
        """AC-FM-7: context-set composition fields are unknown but preserved."""
        text = (
            "---\n"
            "context-set: base\n"
            "purpose: The evidence model.\n"
            "include-when: Always.\n"
            "depends-on: [spec-and-change-discipline]\n"
            "---\n\n# Context Set: Base\n"
        )
        again = fm.parse_text(fm.render(fm.parse_text(text)))
        self.assertEqual(again.fields.get("context-set"), "base")
        self.assertEqual(again.fields.get("purpose"), "The evidence model.")
        self.assertEqual(again.fields.get("include-when"), "Always.")
        self.assertEqual(again.fields.get("depends-on"), ["spec-and-change-discipline"])


class TestWithFields(unittest.TestCase):
    def test_fm8_returns_a_new_document_and_applies_updates(self):
        """AC-FM-8: `with_fields` returns a new Document carrying the updates."""
        doc = fm.parse_text(agreed_doc())
        updated = fm.with_fields(doc, {"status": "in-review"})
        self.assertIsNot(updated, doc)
        self.assertEqual(updated.fields.get("status"), "in-review")

    def test_fm8_original_is_not_mutated(self):
        """AC-FM-8: the input Document is left untouched."""
        doc = fm.parse_text(agreed_doc())
        before = dict(doc.fields)
        fm.with_fields(doc, {"status": "in-review", "last-reviewed": None})
        self.assertEqual(doc.fields, before)

    def test_fm8_none_sets_null_rather_than_deleting(self):
        """AC-FM-8: a key mapped to None is set to null, not removed."""
        doc = fm.parse_text(agreed_doc())
        updated = fm.with_fields(doc, {"last-reviewed": None})
        self.assertIn("last-reviewed", updated.fields)
        self.assertIsNone(updated.fields["last-reviewed"])

    def test_fm8_body_is_carried_through(self):
        """AC-FM-8: `with_fields` changes fields only, never the body."""
        doc = fm.parse_text(agreed_doc())
        updated = fm.with_fields(doc, {"status": "in-review"})
        self.assertEqual(updated.body, doc.body)


class TestCommentAndBlankPreservation(unittest.TestCase):
    """AC-FM-17 (§8): `render` must not silently delete authored content.

    The dialect admits `#` comments and `parse_text` accepts them, but nothing
    round-tripped them — so an unattended index mutation deleted a comment
    explaining why a document's `audience` must not change.
    """

    #: Key order already matches FIELD_ORDER, so "position relative to the
    #: surrounding keys" is unambiguous here and does not collide with
    #: AC-FM-7's canonical ordering. See the note in the final report.
    ANNOTATED = (
        "---\n"
        "status: agreed\n"
        "last-reviewed: reviews/x.md @ abc1234\n"
        "# audience is fixed by the charter; do not change\n"
        "audience: [all-roles]\n"
        "\n"
        "superseded-by: null\n"
        "---\n"
        "\n# Annotated\n\nBody.\n"
    )
    COMMENT = "# audience is fixed by the charter; do not change"

    def test_fm17_comment_lines_survive_render(self):
        """AC-FM-17: a `#` comment inside the block is preserved by `render`."""
        rendered = fm.render(fm.parse_text(self.ANNOTATED))
        self.assertIn(self.COMMENT, rendered)

    def test_fm17_comment_keeps_its_position_relative_to_surrounding_keys(self):
        """AC-FM-17: the comment still sits between `last-reviewed` and `audience`."""
        rendered = fm.render(fm.parse_text(self.ANNOTATED))
        self.assertIn(self.COMMENT, rendered)
        self.assertLess(rendered.index("last-reviewed:"), rendered.index(self.COMMENT))
        self.assertLess(rendered.index(self.COMMENT), rendered.index("audience:"))

    def test_fm17_blank_lines_inside_the_block_survive_render(self):
        """AC-FM-17: blank lines inside the frontmatter block are preserved."""
        rendered = fm.render(fm.parse_text(self.ANNOTATED))
        head = rendered.split("---\n", 2)[1]
        self.assertIn("\n\n", head, "the blank line inside the block was dropped")

    def test_fm17_comments_survive_with_fields_and_render(self):
        """AC-FM-17: the flip path (`with_fields` then `render`) preserves comments."""
        doc = fm.parse_text(self.ANNOTATED)
        flipped = fm.with_fields(doc, {"status": "in-review", "last-reviewed": None})
        rendered = fm.render(flipped)
        self.assertIn("status: in-review", rendered)
        self.assertIn(self.COMMENT, rendered)

    def test_fm17_annotated_document_round_trips(self):
        """AC-FM-17: parse/render/parse is stable for an annotated document."""
        once = fm.render(fm.parse_text(self.ANNOTATED))
        twice = fm.render(fm.parse_text(once))
        self.assertEqual(twice, once)

    def test_fm18_block_item_after_a_scalar_key_is_malformed(self):
        """AC-FM-18: a `- item` following a scalar value is `malformed-frontmatter`."""
        text = (
            "---\n"
            "status: draft\n"
            "audience: all-roles\n"
            "- coder-agent\n"
            "---\nbody\n"
        )
        doc = fm.parse_text(text)
        self.assertIn("malformed-frontmatter", code_set(doc.errors))

    def test_fm18_scalar_is_not_silently_discarded(self):
        """AC-FM-18: the scalar value must not vanish in favour of the list."""
        text = (
            "---\n"
            "status: draft\n"
            "audience: all-roles\n"
            "- coder-agent\n"
            "---\nbody\n"
        )
        doc = fm.parse_text(text)
        self.assertIn(
            "all-roles",
            repr(doc.fields.get("audience")),
            "the scalar `all-roles` was discarded rather than reported",
        )

    def test_fm18_a_genuine_block_list_is_still_accepted(self):
        """AC-FM-18: `key:` with no scalar followed by `- item` remains valid."""
        doc = fm.parse_text("---\nstatus: draft\naudience:\n- all-roles\n---\nbody\n")
        self.assertNotIn("malformed-frontmatter", code_set(doc.errors))
        self.assertEqual(doc.fields.get("audience"), ["all-roles"])


class TestValidate(unittest.TestCase):
    def test_fm9_missing_frontmatter(self):
        """AC-FM-9: a document with no frontmatter yields `missing-frontmatter`."""
        self.assertIn("missing-frontmatter", code_set(validate("# Title\n\nProse.\n")))

    def test_fm10_missing_status_when_absent(self):
        """AC-FM-10: an absent `status` yields `missing-status`."""
        text = frontmatter_block(audience=["all-roles"]) + "\nbody\n"
        self.assertIn("missing-status", code_set(validate(text)))

    def test_fm10_missing_status_when_null(self):
        """AC-FM-10: a null `status` yields `missing-status`."""
        text = frontmatter_block(status=None, audience=["all-roles"]) + "\nbody\n"
        self.assertIn("missing-status", code_set(validate(text)))

    def test_fm10_invalid_status(self):
        """AC-FM-10: a status outside STATUSES yields `invalid-status`."""
        text = (
            frontmatter_block(status="stable", last_reviewed=None, audience=["all-roles"])
            + "\nbody\n"
        )
        found = code_set(validate(text))
        self.assertIn("invalid-status", found)
        self.assertNotIn("missing-status", found)

    def test_fm11_missing_last_reviewed_only_when_key_absent(self):
        """AC-FM-11: absence is a finding; an explicit null is permitted."""
        absent = frontmatter_block(status="draft", audience=["all-roles"]) + "\nbody\n"
        self.assertIn("missing-last-reviewed", code_set(validate(absent)))

        explicit_null = (
            frontmatter_block(status="draft", last_reviewed=None, audience=["all-roles"])
            + "\nbody\n"
        )
        self.assertNotIn("missing-last-reviewed", code_set(validate(explicit_null)))

    def test_fm11_invalid_last_reviewed_format(self):
        """AC-FM-11: a non-null value not matching LAST_REVIEWED_RE is invalid."""
        for bad in ["2026-01-01", "reviews/x.md @ zzz", "reviews/x.md@abc1234", "abc1234"]:
            with self.subTest(value=bad):
                text = (
                    frontmatter_block(
                        status="draft", last_reviewed=bad, audience=["all-roles"]
                    )
                    + "\nbody\n"
                )
                self.assertIn("invalid-last-reviewed", code_set(validate(text)))

    def test_fm11_valid_last_reviewed_format_is_accepted(self):
        """AC-FM-11: a well-formed review pointer produces no finding."""
        text = (
            frontmatter_block(
                status="draft",
                last_reviewed="reviews/document-metadata-policy-cycle-4.md @ ea6b44e",
                audience=["all-roles"],
            )
            + "\nbody\n"
        )
        self.assertNotIn("invalid-last-reviewed", code_set(validate(text)))

    def test_fm12_agreed_without_review(self):
        """AC-FM-12: `agreed` with a null review record is a finding."""
        text = (
            frontmatter_block(status="agreed", last_reviewed=None, audience=["all-roles"])
            + "\nbody\n"
        )
        self.assertIn("agreed-without-review", code_set(validate(text)))

    def test_fm12_grandfathered_suppresses_the_finding(self):
        """AC-FM-12: `grandfathered=True` suppresses `agreed-without-review`."""
        text = (
            frontmatter_block(status="agreed", last_reviewed=None, audience=["all-roles"])
            + "\nbody\n"
        )
        self.assertNotIn(
            "agreed-without-review", code_set(validate(text, grandfathered=True))
        )

    def test_fm13_missing_and_empty_audience(self):
        """AC-FM-13: absent/null audience is `missing-audience`; `[]` is `empty-audience`."""
        absent = frontmatter_block(status="draft", last_reviewed=None) + "\nbody\n"
        self.assertIn("missing-audience", code_set(validate(absent)))

        null_value = (
            frontmatter_block(status="draft", last_reviewed=None, audience=None) + "\nbody\n"
        )
        self.assertIn("missing-audience", code_set(validate(null_value)))

        empty = "---\nstatus: draft\nlast-reviewed: null\naudience: []\n---\nbody\n"
        found = code_set(validate(empty))
        self.assertIn("empty-audience", found)
        self.assertNotIn("missing-audience", found)

    def test_fm13_invalid_audience_one_finding_per_value_naming_it(self):
        """AC-FM-13: each bad audience value gets its own finding, naming the value."""
        text = (
            "---\nstatus: draft\nlast-reviewed: null\n"
            "audience: [all-roles, not-a-role, also-bogus]\n---\nbody\n"
        )
        findings = validate(text)
        invalid = [f for f in findings if f.code == "invalid-audience"]
        self.assertEqual(len(invalid), 2)
        joined = " ".join(f.message for f in invalid)
        self.assertIn("not-a-role", joined)
        self.assertIn("also-bogus", joined)

    def test_fm13_reserved_and_role_slug_values_are_accepted(self):
        """AC-FM-13: RESERVED_AUDIENCE plus known role slugs validate clean."""
        text = (
            "---\nstatus: draft\nlast-reviewed: null\n"
            "audience: [all-roles, human, coder-agent]\n---\nbody\n"
        )
        self.assertNotIn("invalid-audience", code_set(validate(text)))

    def test_fm13_bare_string_audience_is_a_one_element_list(self):
        """AC-FM-13: a bare string audience is treated as a one-element list."""
        good = "---\nstatus: draft\nlast-reviewed: null\naudience: all-roles\n---\nbody\n"
        found = code_set(validate(good))
        self.assertNotIn("invalid-audience", found)
        self.assertNotIn("missing-audience", found)

        bad = "---\nstatus: draft\nlast-reviewed: null\naudience: not-a-role\n---\nbody\n"
        self.assertIn("invalid-audience", code_set(validate(bad)))

    def test_fm14_superseded_without_pointer(self):
        """AC-FM-14: `superseded` with no successor pointer is a finding."""
        null_pointer = (
            frontmatter_block(
                status="superseded",
                last_reviewed=None,
                audience=["all-roles"],
                superseded_by=None,
            )
            + "\nbody\n"
        )
        self.assertIn("superseded-without-pointer", code_set(validate(null_pointer)))

        absent_pointer = (
            frontmatter_block(
                status="superseded", last_reviewed=None, audience=["all-roles"]
            )
            + "\nbody\n"
        )
        self.assertIn("superseded-without-pointer", code_set(validate(absent_pointer)))

    def test_fm14_pointer_without_superseded_status(self):
        """AC-FM-14: a non-null `superseded-by` on a non-superseded doc is a finding."""
        text = (
            frontmatter_block(
                status="draft",
                last_reviewed=None,
                audience=["all-roles"],
                superseded_by="policies/other.md",
            )
            + "\nbody\n"
        )
        self.assertIn("superseded-by-without-status", code_set(validate(text)))

    def test_fm14_null_pointer_on_non_superseded_doc_is_permitted(self):
        """AC-FM-14: `superseded-by: null` on a draft is not a finding (null == absent)."""
        text = (
            frontmatter_block(
                status="draft", last_reviewed=None, audience=["all-roles"], superseded_by=None
            )
            + "\nbody\n"
        )
        found = code_set(validate(text))
        self.assertNotIn("superseded-by-without-status", found)
        self.assertNotIn("superseded-without-pointer", found)

    def test_fm15_excluded_fields_one_finding_each(self):
        """AC-FM-15: every EXCLUDED_FIELDS key yields its own `excluded-field`."""
        text = (
            "---\nstatus: draft\nlast-reviewed: null\naudience: [all-roles]\n"
            "version: 3\nauthor: Dave\n---\nbody\n"
        )
        findings = validate(text)
        excluded = [f for f in findings if f.code == "excluded-field"]
        self.assertEqual(len(excluded), 2)
        joined = " ".join(f.message for f in excluded)
        self.assertIn("version", joined)
        self.assertIn("author", joined)

    def test_fm16_fully_valid_agreed_document_has_no_findings(self):
        """AC-FM-16: a compliant agreed document yields zero findings."""
        text = agreed_doc()
        doc = fm.parse_text(text)
        # Precondition: the document must actually be recognised as frontmatter
        # -- "zero findings" on an unparsed document would be vacuous.
        self.assertTrue(doc.has_frontmatter)
        self.assertEqual(doc.fields.get("status"), "agreed")
        self.assertEqual(
            fm.validate(doc, path="policies/sample.md", role_slugs=ROLE_SLUGS), []
        )

    def test_fm16_constants_match_the_policy(self):
        """AC-FM-16: the module constants encode the policy's field vocabulary."""
        self.assertEqual(
            fm.STATUSES, {"draft", "in-review", "agreed", "superseded", "deprecated"}
        )
        self.assertEqual(
            fm.EXCLUDED_FIELDS, {"version", "last-modified", "author", "changelog"}
        )
        self.assertEqual(fm.RESERVED_AUDIENCE, {"all-roles", "human"})
        self.assertEqual(
            fm.FIELD_ORDER, ["status", "last-reviewed", "audience", "superseded-by"]
        )


if __name__ == "__main__":
    unittest.main()
