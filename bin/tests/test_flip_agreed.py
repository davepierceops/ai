"""AC-FA-*: `bin/flip-agreed` — self-verifying, frontmatter-only status commits.

Contract: `docs/packages/package-a-spec.md` §3.5. Real git throughout: the
point of this tool is the *shape of the commit it produces*, so the assertions
are on committed trees and on which paths a commit touched.
"""

from __future__ import annotations

import unittest

from tests.helpers import (
    agreed_doc,
    base_env,
    bracket_codes,
    commit,
    commit_count,
    commit_paths,
    frontmatter_block,
    git,
    in_review_doc,
    make_home,
    make_repo,
    porcelain,
    run_cli,
    show,
    stage,
    write,
)

TARGET = "policies/sample-policy.md"
REVIEW = "reviews/sample-review.md"
BODY = "\n# Sample Policy\n\nThe body that must not change.\n"


class FlipAgreedTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        write(self.repo, TARGET, in_review_doc(body=BODY))
        write(self.repo, REVIEW, "# Review of the sample policy\n\nFindings: none.\n")
        write(self.repo, "policies/other.md", agreed_doc())
        self.base_sha = commit(self.repo, "seed", env=self.env)
        self.short_sha = self.base_sha[:7]
        self.review_value = "%s @ %s" % (REVIEW, self.short_sha)
        self.commits_before = commit_count(self.repo, env=self.env)

    def flip(self, *args):
        return run_cli("flip-agreed", *args, cwd=self.repo, env=self.env)

    def flip_target(self, *extra):
        return self.flip(TARGET, "--review", self.review_value, *extra)

    def head_doc(self, relpath=TARGET):
        return show(self.repo, "HEAD:" + relpath, env=self.env)

    def assert_no_new_commit(self):
        self.assertEqual(commit_count(self.repo, env=self.env), self.commits_before)


class TestHappyPath(FlipAgreedTestCase):
    def test_fa1_sets_status_and_review_pointer(self):
        """AC-FA-1: in-review -> agreed with the supplied review pointer."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        committed = self.head_doc()
        self.assertIn("status: agreed", committed)
        self.assertIn("last-reviewed: %s" % self.review_value, committed)

    def test_fa1_leaves_other_fields_and_the_body_untouched(self):
        """AC-FA-1: nothing but `status` and `last-reviewed` moves."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        committed = self.head_doc()
        self.assertIn("status: agreed", committed)
        self.assertIn("audience: [all-roles]", committed)
        self.assertIn("superseded-by: null", committed)
        self.assertTrue(committed.endswith(BODY), "body changed: %r" % committed[-80:])

    def test_fa1_creates_exactly_one_commit_touching_exactly_one_file(self):
        """AC-FA-1: one commit, one path."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(commit_count(self.repo, env=self.env), self.commits_before + 1)
        self.assertEqual(commit_paths(self.repo, env=self.env), [TARGET])

    def test_fa1_leaves_a_clean_worktree(self):
        """AC-FA-1: the flip is fully committed, nothing left staged or dirty."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(commit_count(self.repo, env=self.env), self.commits_before + 1)
        self.assertEqual(porcelain(self.repo, env=self.env).strip(), "")


class TestSelfVerification(FlipAgreedTestCase):
    def test_fa2_content_difference_aborts_with_exit_four(self):
        """AC-FA-2: a body difference against HEAD is a self-verification failure."""
        write(self.repo, TARGET, in_review_doc(body="\n# Sample Policy\n\nSmuggled.\n"))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.flip_target()
        self.assertEqual(rc, 4, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("frontmatter-only-violation", bracket_codes(out + err))

    def test_fa2_no_commit_is_created_on_a_violation(self):
        """AC-FA-2: the violating flip is not committed."""
        write(self.repo, TARGET, in_review_doc(body="\n# Sample Policy\n\nSmuggled.\n"))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.flip_target()
        self.assertEqual(rc, 4, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()
        self.assertIn("status: in-review", self.head_doc())


class TestPreconditions(FlipAgreedTestCase):
    def test_fa3_refuses_when_other_changes_are_staged(self):
        """AC-FA-3: unrelated staged work would be swept into the commit."""
        write(self.repo, "policies/other.md", agreed_doc(body="\n# Other\n\nedited\n"))
        stage(self.repo, "policies/other.md", env=self.env)

        rc, out, err = self.flip_target()
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()

    def test_fa4_refuses_when_the_target_has_unstaged_body_edits(self):
        """AC-FA-4: a dirty target would make the frontmatter-only claim false."""
        write(self.repo, TARGET, in_review_doc(body="\n# Sample Policy\n\nDirty.\n"))

        rc, out, err = self.flip_target()
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()


class TestArgumentValidation(FlipAgreedTestCase):
    def test_fa5_review_is_required_for_agreed(self):
        """AC-FA-5: `--status agreed` without `--review` is a usage error (2)."""
        rc, out, err = self.flip(TARGET)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()

    def test_fa5_review_value_must_match_the_documented_format(self):
        """AC-FA-5: a malformed review pointer is a validation failure (1)."""
        for bad in ["2026-01-01", "reviews/sample-review.md@abc1234", "just-a-sha"]:
            with self.subTest(value=bad):
                rc, out, err = self.flip(TARGET, "--review", bad)
                self.assertEqual(rc, 1, "value=%r stdout=%r stderr=%r" % (bad, out, err))
        self.assert_no_new_commit()

    def test_fa5_review_artifact_must_exist(self):
        """AC-FA-5: a review pointer naming a missing artifact fails (1)."""
        rc, out, err = self.flip(
            TARGET, "--review", "reviews/never-written.md @ %s" % self.short_sha
        )
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("reviews/never-written.md", out + err)
        self.assert_no_new_commit()

    def test_fa5_sha_must_resolve_to_a_commit(self):
        """AC-FA-5: a well-formed but unresolvable SHA fails (1)."""
        rc, out, err = self.flip(TARGET, "--review", "%s @ 0000000" % REVIEW)
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()

    def test_fa6_superseded_requires_a_successor(self):
        """AC-FA-6: `--status superseded` without `--superseded-by` is usage (2)."""
        rc, out, err = self.flip(TARGET, "--status", "superseded")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()

    def test_fa6_superseded_writes_the_successor_pointer(self):
        """AC-FA-6: the successor path lands in `superseded-by`."""
        rc, out, err = self.flip(
            TARGET, "--status", "superseded", "--superseded-by", "policies/other.md"
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        committed = self.head_doc()
        self.assertIn("status: superseded", committed)
        self.assertIn("superseded-by: policies/other.md", committed)

    def test_fa6_deprecated_is_accepted_without_a_review(self):
        """AC-FA-6: `--status deprecated` needs no review pointer."""
        rc, out, err = self.flip(TARGET, "--status", "deprecated")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: deprecated", self.head_doc())

    def test_fa6_a_non_transition_status_is_rejected(self):
        """AC-FA-6: only the three status transitions are permitted."""
        rc, out, err = self.flip(TARGET, "--status", "draft")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()

    def test_fa7_pre_existing_findings_abort_the_flip(self):
        """AC-FA-7: an invalid document is not silently promoted to agreed."""
        write(
            self.repo,
            TARGET,
            frontmatter_block(
                status="in-review", last_reviewed=None, audience=["not-a-role"],
                superseded_by=None,
            )
            + BODY,
        )
        commit(self.repo, "make it invalid", env=self.env)
        self.commits_before = commit_count(self.repo, env=self.env)

        rc, out, err = self.flip_target()
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invalid-audience", bracket_codes(out + err))
        self.assert_no_new_commit()

    def test_fa8_refuses_an_out_of_scope_path(self):
        """AC-FA-8: out-of-scope documents have no lifecycle to flip (1)."""
        write(self.repo, "docs/notes.md", in_review_doc(body=BODY))
        commit(self.repo, "add out-of-scope doc", env=self.env)
        self.commits_before = commit_count(self.repo, env=self.env)

        rc, out, err = self.flip("docs/notes.md", "--review", self.review_value)
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("docs/notes.md", out + err)
        self.assert_no_new_commit()

    def test_fa8_refuses_a_missing_file(self):
        """AC-FA-8: a non-existent target fails, naming it (1)."""
        rc, out, err = self.flip(
            "policies/absent.md", "--review", self.review_value
        )
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("policies/absent.md", out + err)
        self.assert_no_new_commit()

    def test_fa8_refuses_a_document_without_frontmatter(self):
        """AC-FA-8: a legacy document cannot be flipped (1)."""
        write(self.repo, "policies/legacy.md", "# Legacy\n\nStatus: stable\n")
        commit(self.repo, "add legacy", env=self.env)
        self.commits_before = commit_count(self.repo, env=self.env)

        rc, out, err = self.flip("policies/legacy.md", "--review", self.review_value)
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("missing-frontmatter", bracket_codes(out + err))
        self.assert_no_new_commit()


class TestNoCommitAndMessages(FlipAgreedTestCase):
    def test_fa9_no_commit_stages_without_committing(self):
        """AC-FA-9: `--no-commit` leaves the flip staged, exit 0."""
        rc, out, err = self.flip_target("--no-commit")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assert_no_new_commit()
        staged = show(self.repo, ":" + TARGET, env=self.env)
        self.assertIn("status: agreed", staged)
        self.assertIn("last-reviewed: %s" % self.review_value, staged)

    def test_fa10_default_commit_subject(self):
        """AC-FA-10: the default subject is `docs(<relpath>): status -> <status>`."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        subject = git(
            self.repo, "log", "-1", "--pretty=%s", env=self.env, check=True
        )[1].strip()
        self.assertEqual(subject, "docs(%s): status -> agreed" % TARGET)

    def test_fa10_commit_body_carries_the_review_pointer(self):
        """AC-FA-10: the review pointer appears on a commit body line."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        body = git(self.repo, "log", "-1", "--pretty=%b", env=self.env, check=True)[1]
        self.assertIn(self.review_value, body)

    def test_fa10_message_overrides_the_subject(self):
        """AC-FA-10: `--message` replaces the subject line."""
        rc, out, err = self.flip_target("--message", "docs: agree the sample policy")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        subject = git(
            self.repo, "log", "-1", "--pretty=%s", env=self.env, check=True
        )[1].strip()
        self.assertEqual(subject, "docs: agree the sample policy")


class TestPostCommitVerification(FlipAgreedTestCase):
    def test_fa11_committed_file_revalidates_and_head_touches_one_path(self):
        """AC-FA-11: post-commit re-verification passes on the happy path."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(commit_paths(self.repo, env=self.env), [TARGET])

        check_rc, check_out, check_err = run_cli(
            "check-frontmatter", TARGET, cwd=self.repo, env=self.env
        )
        self.assertEqual(
            check_rc, 0, "committed file did not revalidate: %r" % check_err
        )

    def test_fa11_does_not_rewrite_history(self):
        """AC-FA-11: the tool never amends or rewrites an existing commit."""
        rc, out, err = self.flip_target()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        parent = git(
            self.repo, "rev-parse", "HEAD~1", env=self.env, check=True
        )[1].strip()
        self.assertEqual(parent, self.base_sha)


if __name__ == "__main__":
    unittest.main()
