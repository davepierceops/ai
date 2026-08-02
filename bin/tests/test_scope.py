"""AC-SC-*: the in-scope glob set, read from the metadata policy at runtime.

Contract: `docs/packages/package-a-spec.md` §3.2. The policy text itself is the
contract here (spec §5, "contract-verified"), so AC-SC-1 asserts against the
real `policies/document-metadata-policy.md`.
"""

from __future__ import annotations

import unittest

from aimeta import scope

from tests.helpers import REAL_POLICY_TEXT, make_home, policy_without


EXPECTED_GLOBS = [
    "policies/**",
    "roles/**",
    "context-sets/**",
    "boundaries/**",
    "skills/**",
    "specs/**",
    "vendors/**",
    "operating-model.md",
    "README.md",
]


class TestParseInScopeGlobs(unittest.TestCase):
    def test_sc1_extracts_the_in_scope_list_in_document_order(self):
        """AC-SC-1: the current policy yields exactly the nine in-scope globs."""
        self.assertEqual(scope.parse_in_scope_globs(REAL_POLICY_TEXT), EXPECTED_GLOBS)

    def test_sc1_stops_at_the_out_of_scope_marker(self):
        """AC-SC-1: out-of-scope backticked entries are not collected."""
        globs = scope.parse_in_scope_globs(REAL_POLICY_TEXT)
        for out_of_scope in ["MANIFEST.md", "OPEN-ITEMS.md", "CLAUDE.md", ".claude/**"]:
            self.assertNotIn(out_of_scope, globs)

    def test_sc1_load_globs_reads_the_policy_from_the_methodology_home(self):
        """AC-SC-1: `load_globs` sources the same set from a home directory."""
        home = make_home(self)
        self.assertEqual(scope.load_globs(home), EXPECTED_GLOBS)

    def test_sc1_load_globs_reflects_an_edited_policy(self):
        """AC-SC-1: the glob set is read at runtime, not baked in."""
        home = make_home(self, policy_text=policy_without("skills/**"))
        globs = scope.load_globs(home)
        self.assertNotIn("skills/**", globs)
        self.assertIn("policies/**", globs)

    def test_sc2_missing_section_fails_closed(self):
        """AC-SC-2: an absent in-scope section raises ScopeError, no fallback."""
        text = "# Policy\n\n## Scope\n\nSome prose with no marker.\n"
        with self.assertRaises(scope.ScopeError):
            scope.parse_in_scope_globs(text)

    def test_sc2_section_with_no_backticked_entries_fails_closed(self):
        """AC-SC-2: a marker with no backticked entries raises ScopeError."""
        text = (
            "# Policy\n\n**In scope (frontmatter required):**\n\n"
            "- everything, obviously\n\n**Out of scope:**\n\n- `MANIFEST.md`\n"
        )
        with self.assertRaises(scope.ScopeError):
            scope.parse_in_scope_globs(text)

    def test_sc2_load_globs_raises_when_the_policy_file_is_absent(self):
        """AC-SC-2: a home without the policy fails closed rather than defaulting."""
        home = make_home(self)
        (home / "policies" / "document-metadata-policy.md").unlink()
        with self.assertRaises(Exception) as ctx:
            scope.load_globs(home)
        self.assertNotIsInstance(ctx.exception, AssertionError)


class TestMatches(unittest.TestCase):
    def setUp(self):
        self.globs = list(EXPECTED_GLOBS)

    def test_sc3_directory_globs_match_at_any_depth(self):
        """AC-SC-3: `dir/**` means any path under `dir/`, at any depth."""
        for path in [
            "policies/document-metadata-policy.md",
            "policies/nested/deeper/thing.md",
            "context-sets/base.md",
            "specs/prd-template.md",
        ]:
            with self.subTest(path=path):
                self.assertTrue(scope.matches(path, self.globs))

    def test_sc3_directory_glob_does_not_match_the_bare_directory_name(self):
        """AC-SC-3: `policies/**` matches paths *under* the directory."""
        self.assertFalse(scope.matches("policies", self.globs))

    def test_sc3_non_directory_globs_are_fnmatch_over_the_whole_path(self):
        """AC-SC-3: a plain entry matches the whole relative path only."""
        self.assertTrue(scope.matches("operating-model.md", self.globs))
        self.assertTrue(scope.matches("README.md", self.globs))
        self.assertFalse(scope.matches("docs/README.md", self.globs))
        self.assertFalse(scope.matches("sub/operating-model.md", self.globs))

    def test_sc4_only_markdown_is_ever_in_scope(self):
        """AC-SC-4: a non-`.md` file under an in-scope prefix is out of scope."""
        for path in [
            "policies/x.txt",
            "policies/notes.yaml",
            "context-sets/diagram.png",
            "specs/schema.json",
        ]:
            with self.subTest(path=path):
                self.assertFalse(scope.matches(path, self.globs))

    def test_sc5_paths_outside_every_glob_are_out_of_scope(self):
        """AC-SC-5: tracker, review, and adapter documents are never in scope."""
        for path in [
            "MANIFEST.md",
            "OPEN-ITEMS.md",
            "docs/cycles/x.md",
            "reviews/x.md",
            "CLAUDE.md",
            ".claude/skills/README.md",
            "AGENTS.md",
            "docs/packages/package-a-spec.md",
        ]:
            with self.subTest(path=path):
                self.assertFalse(scope.matches(path, self.globs))

    def test_sc5_an_empty_glob_set_matches_nothing(self):
        """AC-SC-5: with no globs, nothing is in scope (inert, not universal)."""
        self.assertFalse(scope.matches("policies/x.md", []))


if __name__ == "__main__":
    unittest.main()
