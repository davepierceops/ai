"""AC-CF-*: `bin/check-frontmatter` — validator and pre-commit hook engine.

Contract: `docs/packages/package-a-spec.md` §3.4.

This is the highest-risk surface in the package: `--staged` mode *mutates the
git index*, so a bug here corrupts a commit rather than merely failing it
(spec §6, risk 2). AC-CF-4 through AC-CF-12 therefore assert on the actual
index blob (`git show :<path>`) and on the worktree file separately.

All CLI behaviour is exercised across the process boundary because exit codes
are part of the contract (spec §2.4).
"""

from __future__ import annotations

import unittest

from tests.helpers import (
    agreed_doc,
    base_env,
    bracket_codes,
    commit,
    disposition_doc,
    draft_doc,
    frontmatter_block,
    git,
    make_home,
    make_repo,
    policy_without,
    read,
    run_cli,
    show,
    snapshot_tree,
    stage,
    write,
)

BODY_V1 = "\n# Sample Policy\n\nOriginal body.\n"
BODY_V2 = "\n# Sample Policy\n\nEdited body.\n"
BODY_V3 = "\n# Sample Policy\n\nWorktree-only body.\n"

TARGET = "policies/sample-policy.md"


class CheckFrontmatterTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

    def check(self, *args, env=None):
        return run_cli(
            "check-frontmatter", *args, cwd=self.repo, env=env or self.env
        )

    def index_blob(self, relpath=TARGET):
        return show(self.repo, ":" + relpath, env=self.env)

    def head_blob(self, relpath=TARGET):
        return show(self.repo, "HEAD:" + relpath, env=self.env)

    def seed_agreed(self, relpath=TARGET, body=BODY_V1):
        write(self.repo, relpath, agreed_doc(body=body))
        return commit(self.repo, "seed %s" % relpath, env=self.env)


class TestDefaultMode(CheckFrontmatterTestCase):
    def test_cf1_valid_in_scope_files_are_silent_and_exit_zero(self):
        """AC-CF-1: a compliant in-scope set produces no findings and exits 0."""
        self.seed_agreed()
        write(self.repo, "roles/coder-agent.md", agreed_doc())
        commit(self.repo, "add role", env=self.env)

        rc, out, err = self.check()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertNotIn("ERROR", out + err)

    def test_cf1_findings_print_one_error_line_each_and_exit_one(self):
        """AC-CF-1: one `ERROR <path>: [code] ...` line per finding, exit 1."""
        write(
            self.repo,
            TARGET,
            frontmatter_block(
                status="stable", last_reviewed=None, audience=["not-a-role"]
            )
            + BODY_V1,
        )
        commit(self.repo, "add bad doc", env=self.env)

        rc, out, err = self.check()
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        error_lines = [l for l in err.splitlines() if l.startswith("ERROR ")]
        self.assertGreaterEqual(len(error_lines), 2)
        for line in error_lines:
            self.assertIn(TARGET, line)
            self.assertTrue(bracket_codes(line), "no [code] in %r" % line)
        found = set(bracket_codes(err))
        self.assertIn("invalid-status", found)
        self.assertIn("invalid-audience", found)

    def test_cf1_default_with_no_arguments_checks_everything(self):
        """AC-CF-1: no arguments and no flags behaves as `--all`."""
        self.seed_agreed()
        write(self.repo, "roles/bad-role.md", "# No frontmatter here\n")
        commit(self.repo, "add bad role", env=self.env)

        rc, out, err = self.check()
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("missing-frontmatter", bracket_codes(err))
        self.assertIn("roles/bad-role.md", err)

    def test_cf1_all_flag_scans_the_whole_repo(self):
        """AC-CF-1: `--all` validates every in-scope file, not just one."""
        write(self.repo, "policies/a.md", agreed_doc())
        write(self.repo, "context-sets/b.md", "# No frontmatter\n")
        write(self.repo, "boundaries/c.md", "# No frontmatter either\n")
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 1)
        self.assertIn("context-sets/b.md", err)
        self.assertIn("boundaries/c.md", err)

    def test_cf1_named_paths_limit_the_check(self):
        """AC-CF-1: naming a path checks only that path."""
        write(self.repo, "policies/good.md", agreed_doc())
        write(self.repo, "policies/bad.md", "# No frontmatter\n")
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("policies/good.md")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertNotIn("policies/bad.md", out + err)

    def test_cf2_out_of_scope_paths_are_ignored_even_when_named(self):
        """AC-CF-2: a named out-of-scope path is skipped while in-scope ones are not."""
        write(self.repo, "docs/cycles/x.md", "# Tracker doc, no frontmatter\n")
        write(self.repo, "MANIFEST.md", "# Manifest, no frontmatter\n")
        write(self.repo, "policies/bad.md", "# In scope, no frontmatter\n")
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("docs/cycles/x.md", "MANIFEST.md", "policies/bad.md")
        # Exit 1 comes from the in-scope file only; the other two are skipped.
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("policies/bad.md", err)
        self.assertNotIn("docs/cycles/x.md", err)
        self.assertNotIn("MANIFEST.md", err)

    def test_cf2_out_of_scope_files_are_not_reported_by_all(self):
        """AC-CF-2: `--all` never reaches out-of-scope documents."""
        self.seed_agreed()
        write(self.repo, "OPEN-ITEMS.md", "# Open items, no frontmatter\n")
        write(self.repo, "reviews/some-review.md", "# Review artifact\n")
        write(self.repo, "policies/bad.md", "# In scope, no frontmatter\n")
        commit(self.repo, "seed trackers", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("policies/bad.md", err)
        self.assertNotIn("OPEN-ITEMS.md", out + err)
        self.assertNotIn("reviews/some-review.md", out + err)

    def test_cf3_default_mode_writes_nothing(self):
        """AC-CF-3: default mode never mutates a file, even with findings."""
        write(self.repo, TARGET, frontmatter_block(status="stable") + BODY_V1)
        write(self.repo, "roles/coder-agent.md", agreed_doc())
        commit(self.repo, "seed", env=self.env)

        before = snapshot_tree(self.repo, skip=[self.repo / ".git"])
        rc, out, err = self.check("--all")
        after = snapshot_tree(self.repo, skip=[self.repo / ".git"])

        self.assertEqual(rc, 1, "expected findings; stdout=%r stderr=%r" % (out, err))
        self.assertEqual(before, after)
        self.assertIn("status: stable", read(self.repo, TARGET))


class TestStagedFlip(CheckFrontmatterTestCase):
    def test_cf4_content_edit_to_an_agreed_doc_is_flipped_in_the_index(self):
        """AC-CF-4: an agreed doc with a staged body edit is flipped in the index."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        staged = self.index_blob()

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: in-review", staged)
        self.assertNotIn("status: agreed", staged)
        self.assertIn("last-reviewed: null", staged)

    def test_cf4_flip_leaves_every_other_field_and_the_body_untouched(self):
        """AC-CF-4: only `status` and `last-reviewed` change during a flip."""
        write(
            self.repo,
            TARGET,
            agreed_doc(body=BODY_V1, audience=("all-roles", "human")),
        )
        commit(self.repo, "seed", env=self.env)
        write(
            self.repo,
            TARGET,
            agreed_doc(body=BODY_V2, audience=("all-roles", "human")),
        )
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        staged = self.index_blob()

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: in-review", staged)
        self.assertIn("audience: [all-roles, human]", staged)
        self.assertIn("superseded-by: null", staged)
        self.assertTrue(
            staged.endswith(BODY_V2), "staged body was altered: %r" % staged[-80:]
        )

    def test_cf4_flip_is_announced(self):
        """AC-CF-4: the flip prints a FLIPPED line naming the path."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        self.assertIn("FLIPPED", out + err)
        self.assertIn(TARGET, out + err)

    def test_cf4_the_flip_lands_in_the_resulting_commit(self):
        """AC-CF-4: committing after the flip records `in-review`, not `agreed`."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        git(self.repo, "commit", "-q", "--no-verify", "-m", "edit", env=self.env, check=True)
        self.assertIn("status: in-review", self.head_blob())

    def test_cf5_frontmatter_only_change_is_never_flipped(self):
        """AC-CF-5: a status-transition-shaped change is exempt from the flip.

        A second, content-edited file is staged alongside so the "not flipped"
        assertion cannot pass merely because the tool did nothing.
        """
        write(self.repo, TARGET, agreed_doc(body=BODY_V1, audience=("all-roles",)))
        write(self.repo, "policies/edited.md", agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)

        write(
            self.repo, TARGET, agreed_doc(body=BODY_V1, audience=("all-roles", "human"))
        )
        write(self.repo, "policies/edited.md", agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, "policies/edited.md", env=self.env)

        rc, out, err = self.check("--staged")
        staged = self.index_blob()

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: agreed", staged)
        self.assertNotIn("in-review", staged)
        self.assertIn(
            "status: in-review",
            show(self.repo, ":policies/edited.md", env=self.env),
            "the content-edited companion was not flipped, so this test proves nothing",
        )

    def test_cf5_flip_agreed_style_transition_commit_survives_the_hook(self):
        """AC-CF-5: promoting in-review -> agreed is not undone by the hook."""
        write(self.repo, TARGET, draft_doc(body=BODY_V1))
        commit(self.repo, "seed draft", env=self.env)
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: agreed", self.index_blob())

    def test_cf6_non_agreed_staged_status_is_never_flipped(self):
        """AC-CF-6: the staged status governs; a draft is left alone.

        Staged alongside a genuine flip candidate, so a no-op cannot pass.
        """
        self.seed_agreed()
        write(self.repo, "policies/edited.md", agreed_doc(body=BODY_V1))
        commit(self.repo, "seed companion", env=self.env)

        write(self.repo, TARGET, draft_doc(body=BODY_V2))
        write(self.repo, "policies/edited.md", agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, "policies/edited.md", env=self.env)

        rc, out, err = self.check("--staged")
        staged = self.index_blob()

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: draft", staged)
        self.assertIn(
            "status: in-review",
            show(self.repo, ":policies/edited.md", env=self.env),
            "the companion was not flipped, so this test proves nothing",
        )

    def test_cf7_new_file_is_not_flipped_but_is_validated(self):
        """AC-CF-7: an added file is never flipped; `agreed` + null review fails."""
        write(self.repo, "policies/existing.md", agreed_doc())
        commit(self.repo, "seed", env=self.env)

        write(
            self.repo,
            "policies/brand-new.md",
            frontmatter_block(
                status="agreed", last_reviewed=None, audience=["all-roles"],
                superseded_by=None,
            )
            + BODY_V1,
        )
        stage(self.repo, "policies/brand-new.md", env=self.env)

        rc, out, err = self.check("--staged")
        staged = show(self.repo, ":policies/brand-new.md", env=self.env)

        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("agreed-without-review", bracket_codes(err))
        self.assertIn("status: agreed", staged)
        self.assertNotIn("FLIPPED", out + err)

    def test_cf8_staged_deletions_are_skipped(self):
        """AC-CF-8: a staged deletion is never read or reported (AC-CF-4 too)."""
        write(self.repo, "policies/doomed.md", agreed_doc(body=BODY_V1))
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)

        git(self.repo, "rm", "-q", "--", "policies/doomed.md", env=self.env, check=True)
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertNotIn("policies/doomed.md", out + err)
        # The other staged path was still processed, so "no output" is not
        # vacuously true here.
        self.assertIn("status: in-review", self.index_blob())


class TestStagedWorktreeInteraction(CheckFrontmatterTestCase):
    def test_cf9_worktree_is_rewritten_when_it_matches_the_staged_content(self):
        """AC-CF-9: a fully staged file has its worktree copy flipped too."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        worktree = read(self.repo, TARGET)

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: in-review", worktree)
        self.assertIn("last-reviewed: null", worktree)

    def test_cf9_partial_staging_flips_the_index_and_leaves_the_worktree_alone(self):
        """AC-CF-9: with worktree != index, only the index is flipped."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)
        worktree_text = agreed_doc(body=BODY_V3)
        write(self.repo, TARGET, worktree_text)

        rc, out, err = self.check("--staged")

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        staged = self.index_blob()
        self.assertIn("status: in-review", staged)
        self.assertTrue(staged.endswith(BODY_V2), "staged body was clobbered")
        # The worktree must be byte-identical to what the developer left there.
        self.assertEqual(read(self.repo, TARGET), worktree_text)

    def test_cf9_partial_staging_prints_a_note_about_the_worktree(self):
        """AC-CF-9: a NOTE warns that the worktree copy still claims `agreed`."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)
        write(self.repo, TARGET, agreed_doc(body=BODY_V3))

        rc, out, err = self.check("--staged")
        self.assertIn("NOTE", out + err)
        self.assertIn(TARGET, out + err)

    def test_cf10_no_flip_mutates_neither_index_nor_worktree(self):
        """AC-CF-10: `--staged --no-flip` validates the index without mutating."""
        self.seed_agreed()
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

        index_before = self.index_blob()
        worktree_before = read(self.repo, TARGET)
        tree_before = snapshot_tree(self.repo, skip=[self.repo / ".git"])

        rc, out, err = self.check("--staged", "--no-flip")

        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(self.index_blob(), index_before)
        self.assertIn("status: agreed", self.index_blob())
        self.assertEqual(read(self.repo, TARGET), worktree_before)
        self.assertEqual(snapshot_tree(self.repo, skip=[self.repo / ".git"]), tree_before)
        self.assertNotIn("FLIPPED", out + err)

    def test_cf10_no_flip_still_reports_findings(self):
        """AC-CF-10: `--no-flip` is validate-only, not check-nothing."""
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)
        write(
            self.repo,
            TARGET,
            frontmatter_block(
                status="agreed", last_reviewed=None, audience=["all-roles"]
            )
            + BODY_V2,
        )
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged", "--no-flip")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("agreed-without-review", bracket_codes(err))
        self.assertIn("status: agreed", self.index_blob())


class TestStagedValidation(CheckFrontmatterTestCase):
    def test_cf11_findings_block_the_commit_with_exit_one(self):
        """AC-CF-11: validation findings in `--staged` mode exit 1."""
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)
        write(
            self.repo,
            TARGET,
            agreed_doc(body=BODY_V2, audience=("not-a-real-role",)),
        )
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invalid-audience", bracket_codes(err))

    def test_cf11_message_names_the_deliberate_override(self):
        """AC-CF-11: the blocking message names `git commit --no-verify`."""
        write(self.repo, TARGET, "# Legacy doc with no frontmatter\n")
        stage(self.repo, TARGET, env=self.env)

        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("--no-verify", out + err)

    def test_cf12_grandfathered_file_passes_and_an_unlisted_one_fails(self):
        """AC-CF-12: the disposition list decides who may be agreed with null review."""
        grandfathered = frontmatter_block(
            status="agreed", last_reviewed=None, audience=["all-roles"], superseded_by=None
        ) + BODY_V1
        write(self.repo, "policies/old.md", grandfathered)
        write(self.repo, "policies/new.md", grandfathered)
        write(
            self.repo,
            "reviews/frontmatter-disposition.md",
            disposition_doc(["policies/old.md"]),
        )
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        offending = [
            l for l in err.splitlines() if "agreed-without-review" in l
        ]
        self.assertEqual(len(offending), 1, "stderr=%r" % err)
        self.assertIn("policies/new.md", offending[0])
        self.assertNotIn("policies/old.md", err)

    def test_cf12_without_a_disposition_list_the_clause_does_not_apply(self):
        """AC-CF-12: no disposition list means normal rules govern."""
        write(
            self.repo,
            "policies/old.md",
            frontmatter_block(
                status="agreed", last_reviewed=None, audience=["all-roles"],
                superseded_by=None,
            )
            + BODY_V1,
        )
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("agreed-without-review", bracket_codes(err))


class TestPolicyDrivenScope(CheckFrontmatterTestCase):
    def test_cf13_in_scope_set_comes_from_the_policy_at_runtime(self):
        """AC-CF-13: dropping `skills/**` from the policy stops enforcement there."""
        write(self.repo, "skills/x.md", "# A skill with no frontmatter\n")
        write(self.repo, "policies/ok.md", agreed_doc())
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 1, "expected skills/x.md to be reported; stderr=%r" % err)
        self.assertIn("skills/x.md", err)

        narrowed = make_home(self, policy_text=policy_without("skills/**"))
        rc2, out2, err2 = self.check(
            "--all", env=base_env(methodology_home=narrowed)
        )
        self.assertEqual(rc2, 0, "stdout=%r stderr=%r" % (out2, err2))
        self.assertNotIn("skills/x.md", out2 + err2)

    def test_cf13_globs_matching_nothing_are_inert(self):
        """AC-CF-13: a repo that matches only some globs is still valid, exit 0."""
        write(self.repo, "specs/prd.md", agreed_doc())
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))


class TestUsage(CheckFrontmatterTestCase):
    def test_cf1_staged_with_paths_is_a_usage_error(self):
        """AC-CF-1: `--staged` takes no paths (spec §2.4 exit 2)."""
        rc, out, err = self.check("--staged", "policies/x.md")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))


if __name__ == "__main__":
    unittest.main()
