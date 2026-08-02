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
    DOCUMENTED_EXIT_CODES,
    agreed_doc,
    base_env,
    blob_bytes,
    bracket_codes,
    commit,
    disposition_doc,
    draft_doc,
    filesystem_is_case_insensitive,
    frontmatter_block,
    git,
    make_home,
    make_repo,
    no_traceback,
    policy_without,
    read,
    read_bytes,
    run_cli,
    show,
    snapshot_tree,
    stage,
    temp_dir,
    write,
    write_bytes,
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
        # The doomed file gets its own body so it cannot pair with any added
        # path under git's default rename detection. Nothing is added in this
        # scenario today, so this is defensive: it keeps the deletion reported
        # as `D` if this fixture ever grows a new file.
        write(
            self.repo,
            "policies/doomed.md",
            agreed_doc(body="\n# Doomed\n\n" + "about to be deleted\n" * 40),
        )
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


# ---------------------------------------------------------------------------
# §8 — gate findings. Everything below is an addition or amendment from the
# Reviewer and Skeptic/Risk gates (spec §8), covering ground the original
# suite's aperture missed: one git verb, one repo shape, one encoding.
# ---------------------------------------------------------------------------


#: An `agreed` frontmatter block as raw ASCII bytes, so a fixture can carry a
#: body that is deliberately not valid UTF-8.
AGREED_HEAD_BYTES = (
    b"---\n"
    b"status: agreed\n"
    b"last-reviewed: reviews/sample-review.md @ abc1234\n"
    b"audience: [all-roles]\n"
    b"superseded-by: null\n"
    b"---\n"
)
#: 0xE9 is `e` acute in latin-1 and an illegal standalone byte in UTF-8.
LATIN1_V1 = AGREED_HEAD_BYTES + b"\n# Caf\xe9 Policy\n\noriginal body\n"
LATIN1_V2 = AGREED_HEAD_BYTES + b"\n# Caf\xe9 Policy\n\nedited body\n"
REPLACEMENT_CHAR = b"\xef\xbf\xbd"

LATIN_TARGET = "policies/latin1-policy.md"


class TestNonUtf8Documents(CheckFrontmatterTestCase):
    """AC-CF-14: bytes in, bytes out. No transcoding, ever."""

    def seed_latin1(self):
        write_bytes(self.repo, LATIN_TARGET, LATIN1_V1)
        commit(self.repo, "seed latin-1 policy", env=self.env)
        write_bytes(self.repo, LATIN_TARGET, LATIN1_V2)
        stage(self.repo, LATIN_TARGET, env=self.env)

    def test_cf14_undecodable_document_is_reported_and_blocks_the_commit(self):
        """AC-CF-14: a non-UTF-8 staged document is `[undecodable]` and exits 1."""
        self.seed_latin1()

        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("undecodable", bracket_codes(err))
        self.assertIn(LATIN_TARGET, err)

    def test_cf14_index_blob_is_byte_identical_before_and_after(self):
        """AC-CF-14: the run must not rewrite the index blob of an undecodable doc."""
        self.seed_latin1()
        before = blob_bytes(self.repo, ":" + LATIN_TARGET, env=self.env)
        self.assertEqual(before, LATIN1_V2, "fixture did not stage the raw bytes")

        self.check("--staged")

        after = blob_bytes(self.repo, ":" + LATIN_TARGET, env=self.env)
        self.assertEqual(after, before, "the index blob was transcoded or rewritten")

    def test_cf14_no_replacement_characters_reach_the_index(self):
        """AC-CF-14: U+FFFD must never appear in a blob written by the tool."""
        self.seed_latin1()

        self.check("--staged")

        after = blob_bytes(self.repo, ":" + LATIN_TARGET, env=self.env)
        self.assertNotIn(
            REPLACEMENT_CHAR, after, "a lossy decode/re-encode round trip corrupted the blob"
        )
        self.assertIn(b"\xe9", after, "the original latin-1 byte was lost")

    def test_cf14_worktree_file_is_byte_identical_before_and_after(self):
        """AC-CF-14: the worktree copy is left exactly as the developer wrote it."""
        self.seed_latin1()
        before = read_bytes(self.repo, LATIN_TARGET)

        self.check("--staged")

        self.assertEqual(read_bytes(self.repo, LATIN_TARGET), before)

    def test_cf14_committing_after_the_block_preserves_the_bytes(self):
        """AC-CF-14: the documented `--no-verify` override must not commit corruption."""
        self.seed_latin1()

        self.check("--staged")
        git(self.repo, "commit", "-q", "--no-verify", "-m", "latin1", env=self.env, check=True)

        committed = blob_bytes(self.repo, "HEAD:" + LATIN_TARGET, env=self.env)
        self.assertEqual(committed, LATIN1_V2)


class TestValidateBeforeMutating(CheckFrontmatterTestCase):
    """AC-CF-15: findings are computed on the would-be-flipped content first."""

    def stage_edit_with_findings(self):
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)
        # A content edit (so the flip would fire) that is also invalid (so the
        # run must block). The tool must decide before it writes anything.
        write(
            self.repo,
            TARGET,
            frontmatter_block(
                status="agreed",
                last_reviewed="reviews/sample-review.md @ abc1234",
                audience=["not-a-real-role"],
                superseded_by=None,
            )
            + BODY_V2,
        )
        stage(self.repo, TARGET, env=self.env)

    def test_cf15_findings_block_the_run(self):
        """AC-CF-15: an invalid staged document still exits 1."""
        self.stage_edit_with_findings()
        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invalid-audience", bracket_codes(err))

    def test_cf15_index_is_untouched_when_findings_exist(self):
        """AC-CF-15: a blocked run leaves the index exactly as the developer staged it."""
        self.stage_edit_with_findings()
        before = self.index_blob()

        self.check("--staged")

        self.assertEqual(self.index_blob(), before, "the index was mutated despite findings")
        self.assertIn("status: agreed", self.index_blob())

    def test_cf15_worktree_is_untouched_when_findings_exist(self):
        """AC-CF-15: a blocked commit must not leave the working tree edited."""
        self.stage_edit_with_findings()
        before = read(self.repo, TARGET)

        self.check("--staged")

        self.assertEqual(read(self.repo, TARGET), before, "the worktree was mutated despite findings")

    def test_cf15_no_verify_after_a_block_commits_what_the_developer_staged(self):
        """AC-CF-15: the override commits the developer's content, not the tool's rewrite."""
        self.stage_edit_with_findings()
        staged_before = self.index_blob()

        self.check("--staged")
        git(self.repo, "commit", "-q", "--no-verify", "-m", "override", env=self.env, check=True)

        self.assertEqual(self.head_blob(), staged_before)


class HookedRepoTestCase(CheckFrontmatterTestCase):
    """A repo with the managed pre-commit hook actually installed."""

    def setUp(self):
        super().setUp()
        rc, out, err = run_cli("install-hooks", cwd=self.repo, env=self.env)
        self.assertEqual(rc, 0, "install-hooks failed: stdout=%r stderr=%r" % (out, err))
        self.assertTrue((self.repo / ".git" / "hooks" / "pre-commit").is_file())


class TestTemporaryIndexCommit(HookedRepoTestCase):
    """AC-CF-16: `git commit -- <path>` runs the hook against a temporary index."""

    def setUp(self):
        super().setUp()
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)
        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)

    def pathspec_commit(self, message="pathspec commit"):
        return git(self.repo, "commit", "-m", message, "--", TARGET, env=self.env)

    def test_cf16_pathspec_commit_records_the_flip(self):
        """AC-CF-16: the commit itself is still correct."""
        rc, out, err = self.pathspec_commit()
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: in-review", self.head_blob())

    def test_cf16_real_index_does_not_keep_the_pre_flip_blob(self):
        """AC-CF-16: the real index must not be left holding the stale `agreed` blob."""
        rc, out, err = self.pathspec_commit()
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))

        self.assertIn(
            "status: in-review",
            self.index_blob(),
            "the real index kept the pre-flip blob after a pathspec commit",
        )

    def test_cf16_status_reports_no_change_the_user_did_not_make(self):
        """AC-CF-16: `git status` must be clean, as it is for a pathspec commit with no hook."""
        rc, out, err = self.pathspec_commit()
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))

        status = git(self.repo, "status", "--short", env=self.env, check=True)[1]
        self.assertEqual(
            status.strip(), "", "the hook left a staged/unstaged change the user never made"
        )

    def test_cf16_two_commits_cannot_launder_an_edit_back_to_agreed(self):
        """AC-CF-16: the end state after a pathspec commit plus an ordinary one.

        The reported defect: the stale real index made the second commit look
        like a pure status transition, so AC-CF-5's exemption applied and the
        edited body landed as `agreed` with its old review pointer.
        """
        rc, out, err = self.pathspec_commit()
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))

        # Whether this second commit succeeds or reports "nothing to commit" is
        # not the point; the end state is.
        git(self.repo, "commit", "-m", "second", env=self.env)

        final = self.head_blob()
        self.assertIn("Edited body.", final, "fixture lost the content edit")
        self.assertIn(
            "status: in-review",
            final,
            "an edited body ended up committed as `agreed` across two hook-approved commits",
        )


class TestTemporaryIndexGuard(HookedRepoTestCase):
    """AC-CF-16, the "and only when" half: never clobber unrelated staged state.

    `git commit -a` builds its temporary index from the *worktree*, so when a
    partially-staged file is present the blob the hook flips is not the blob
    the real index holds. Mirroring the flip there would destroy staged work
    the user never offered to this commit.
    """

    BODY_V3 = "\n# Sample Policy\n\nWorktree-only third revision.\n"

    def setUp(self):
        super().setUp()
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        commit(self.repo, "seed", env=self.env)

        write(self.repo, TARGET, agreed_doc(body=BODY_V2))
        stage(self.repo, TARGET, env=self.env)          # real index  = v2
        write(self.repo, TARGET, agreed_doc(body=self.BODY_V3))  # worktree = v3

        self.real_index_before = self.index_blob()
        self.assertIn("Edited body.", self.real_index_before, "fixture: index should hold v2")

    def test_cf16_commit_a_reports_that_the_real_index_was_left_alone(self):
        """AC-CF-16: the guard fires and says so when the real index differs."""
        rc, out, err = git(self.repo, "commit", "-a", "-m", "commit -a", env=self.env)
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))
        self.assertIn("real-index-untouched", bracket_codes(out + err))

    def test_cf16_commit_a_records_the_flip_and_leaves_a_clean_tree(self):
        """AC-CF-16: `git commit -a` still commits the flip, and `git status` is clean."""
        rc, out, err = git(self.repo, "commit", "-a", "-m", "commit -a", env=self.env)
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))

        committed = self.head_blob()
        self.assertIn("status: in-review", committed)
        self.assertIn("Worktree-only third revision.", committed)
        status = git(self.repo, "status", "--short", env=self.env, check=True)[1]
        self.assertEqual(status.strip(), "", "the tree was left dirty: %r" % status)

    def temp_index_env(self):
        """An env whose `$GIT_INDEX_FILE` is a scratch index, exactly as git does."""
        index = temp_dir(self, "aimeta-tmpindex-") / "index"
        env = dict(self.env)
        env["GIT_INDEX_FILE"] = str(index)
        # Build the temporary index the way `git commit -a` does: start from
        # HEAD, then add the worktree content.
        git(self.repo, "read-tree", "HEAD", env=env, check=True)
        git(self.repo, "add", "--", TARGET, env=env, check=True)
        return env

    def test_cf16_flip_lands_in_the_temporary_index(self):
        """AC-CF-16: the commit-bound index is still flipped when the guard declines."""
        env = self.temp_index_env()

        rc, out, err = self.check("--staged", env=env)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

        staged = show(self.repo, ":" + TARGET, env=env)
        self.assertIn("status: in-review", staged)
        self.assertIn("Worktree-only third revision.", staged)

    def test_cf16_real_index_keeps_the_unrelated_staged_blob(self):
        """AC-CF-16: staged work the user did not offer to this commit survives."""
        env = self.temp_index_env()

        self.check("--staged", env=env)

        self.assertEqual(
            self.index_blob(),
            self.real_index_before,
            "the flip clobbered unrelated staged state in the real index",
        )
        self.assertIn("status: agreed", self.index_blob())


class TestMergeCommits(HookedRepoTestCase):
    """AC-CF-17: a merge's difference against its first parent is not an edit."""

    BRANCH_REVIEW = "reviews/branch-review.md @ bbb2222"

    def setUp(self):
        super().setUp()
        # `notes.txt` is out of scope and exists only to force the conflict that
        # makes git stop and hand the merge commit to `git commit` (and so to
        # the pre-commit hook) with MERGE_HEAD present.
        write(self.repo, TARGET, agreed_doc(body=BODY_V1))
        write(self.repo, "notes.txt", "main\n")
        commit(self.repo, "seed", env=self.env)

        git(self.repo, "checkout", "-q", "-b", "feature", env=self.env, check=True)
        write(
            self.repo,
            TARGET,
            agreed_doc(body=BODY_V2, review=self.BRANCH_REVIEW),
        )
        write(self.repo, "notes.txt", "branch\n")
        commit(self.repo, "reviewed and agreed on the branch", env=self.env)

        git(self.repo, "checkout", "-q", "main", env=self.env, check=True)
        write(self.repo, "notes.txt", "main second\n")
        commit(self.repo, "diverge on main", env=self.env)

        rc, _, _ = git(self.repo, "merge", "feature", env=self.env)
        self.assertNotEqual(rc, 0, "fixture expected a conflicted merge")
        write(self.repo, "notes.txt", "resolved\n")
        stage(self.repo, "notes.txt", env=self.env)
        self.assertTrue(
            (self.repo / ".git" / "MERGE_HEAD").is_file(), "fixture expected MERGE_HEAD"
        )

    def test_cf17_merge_commit_does_not_flip(self):
        """AC-CF-17: with MERGE_HEAD present, no flip occurs."""
        rc, out, err = git(self.repo, "commit", "-m", "merge feature", env=self.env)
        self.assertEqual(rc, 0, "merge commit failed: stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: agreed", self.head_blob())

    def test_cf17_merge_preserves_the_review_pointer_agreed_on_the_branch(self):
        """AC-CF-17: the durable record of which review agreed the doc survives."""
        rc, out, err = git(self.repo, "commit", "-m", "merge feature", env=self.env)
        self.assertEqual(rc, 0, "merge commit failed: stdout=%r stderr=%r" % (out, err))
        committed = self.head_blob()
        self.assertIn("last-reviewed: %s" % self.BRANCH_REVIEW, committed)
        self.assertNotIn("last-reviewed: null", committed)

    def test_cf17_merge_prints_a_note_naming_why(self):
        """AC-CF-17: the tool says it skipped the flip rather than silently doing so."""
        rc, out, err = git(self.repo, "commit", "-m", "merge feature", env=self.env)
        self.assertEqual(rc, 0, "merge commit failed: stdout=%r stderr=%r" % (out, err))
        self.assertIn("NOTE", out + err)


class TestStagedRename(CheckFrontmatterTestCase):
    """AC-CF-18: a rename compares against the OLD path at HEAD."""

    OLD = "policies/old-doc.md"
    NEW = "policies/new-doc.md"
    LONG_V1 = "\n# Doc\n\n" + "".join("stable paragraph %d.\n\n" % i for i in range(30))
    LONG_V2 = LONG_V1 + "One appended line of new content.\n"

    def setUp(self):
        super().setUp()
        write(self.repo, self.OLD, agreed_doc(body=self.LONG_V1))
        commit(self.repo, "seed", env=self.env)

        git(self.repo, "mv", self.OLD, self.NEW, env=self.env, check=True)
        write(self.repo, self.NEW, agreed_doc(body=self.LONG_V2))
        stage(self.repo, self.NEW, env=self.env)

        status = git(
            self.repo, "diff", "--cached", "--name-status", "HEAD", env=self.env, check=True
        )[1]
        self.assertTrue(
            status.startswith("R"), "fixture expected a rename, git said: %r" % status
        )

    def test_cf18_rename_plus_edit_still_flips(self):
        """AC-CF-18: renaming an agreed doc while editing it is not a bypass."""
        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "status: in-review",
            self.index_blob(self.NEW),
            "rename-and-edit slipped past the flip",
        )

    def test_cf18_pure_rename_without_an_edit_is_not_flipped(self):
        """AC-CF-18: a rename that does not change the body is still exempt."""
        git(self.repo, "checkout", "-q", "HEAD", "--", ".", env=self.env, check=False)
        git(self.repo, "reset", "-q", "--hard", "HEAD", env=self.env, check=True)
        git(self.repo, "mv", self.OLD, self.NEW, env=self.env, check=True)

        rc, out, err = self.check("--staged")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("status: agreed", self.index_blob(self.NEW))


class TestScopeVisibility(CheckFrontmatterTestCase):
    """AC-CF-19: enforcing nothing must not look like enforcing everything."""

    def test_cf19_all_reports_how_many_files_matched(self):
        """AC-CF-19: `--all` prints a NOTE stating the in-scope match count."""
        write(self.repo, "policies/a.md", agreed_doc())
        write(self.repo, "policies/b.md", agreed_doc())
        write(self.repo, "README.md", agreed_doc())
        commit(self.repo, "seed three in-scope files", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        note_lines = [l for l in err.splitlines() if l.startswith("NOTE")]
        self.assertTrue(note_lines, "no NOTE line; stderr=%r" % err)
        self.assertTrue(
            any("3" in l for l in note_lines),
            "no NOTE stated the match count of 3: %r" % note_lines,
        )

    def test_cf19_globs_matching_nothing_are_warned_about(self):
        """AC-CF-19: a configured glob that matches no path gets a WARN."""
        write(self.repo, "policies/a.md", agreed_doc())
        commit(self.repo, "seed only policies", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        warn_lines = [l for l in err.splitlines() if l.startswith("WARN")]
        self.assertTrue(warn_lines, "no WARN for unmatched globs; stderr=%r" % err)
        joined = "\n".join(warn_lines)
        for unmatched in ["roles/**", "skills/**", "boundaries/**"]:
            self.assertIn(unmatched, joined)
        self.assertNotIn("policies/**", joined, "a glob that did match was warned about")

    def test_cf19_a_repo_matching_nothing_is_distinguishable_from_a_clean_one(self):
        """AC-CF-19: zero matches must not present as a silent all-clear."""
        write(self.repo, "docs/notes.md", "# Out of scope\n")
        commit(self.repo, "seed nothing in scope", env=self.env)

        rc, out, err = self.check("--all")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("WARN", err)
        note_lines = [l for l in err.splitlines() if l.startswith("NOTE")]
        self.assertTrue(
            any("0" in l for l in note_lines), "nothing said zero files matched: %r" % err
        )


class TestPathResolution(CheckFrontmatterTestCase):
    """AC-CF-20: a mis-cased path argument must not be a false all-clear."""

    def setUp(self):
        super().setUp()
        if not filesystem_is_case_insensitive(self.repo):
            self.skipTest("filesystem is case-sensitive; AC-CF-20 is not reachable here")

    def test_cf20_mis_cased_path_is_resolved_to_its_real_case(self):
        """AC-CF-20: `Policies/x.md` is checked, not silently skipped as out of scope."""
        write(self.repo, "policies/bad.md", "# In scope, no frontmatter\n")
        commit(self.repo, "seed", env=self.env)

        rc, out, err = self.check("Policies/bad.md")
        self.assertEqual(
            rc, 1, "mis-cased path exited %s silently; stdout=%r stderr=%r" % (rc, out, err)
        )
        self.assertIn("missing-frontmatter", bracket_codes(err))


class TestStagedSymlinks(CheckFrontmatterTestCase):
    """AC-CF-21: a symlink's blob is a path, not a document."""

    LINK = "policies/link.md"

    def setUp(self):
        super().setUp()
        self.outside = temp_dir(self, "aimeta-outside-")
        self.victim = self.outside / "victim.md"
        self.victim.write_text("# Outside the repo\n\nMust not be written through.\n")
        self.victim_before = self.victim.read_text()

        write(self.repo, "policies/real.md", agreed_doc())
        commit(self.repo, "seed", env=self.env)

        (self.repo / "policies" / "link.md").symlink_to(self.victim)
        stage(self.repo, self.LINK, env=self.env)

    def test_cf21_staged_symlink_is_reported(self):
        """AC-CF-21: the symlink is named in the diagnostics rather than passed over."""
        rc, out, err = self.check("--staged")
        self.assertIn(self.LINK, out + err)
        self.assertIn(rc, DOCUMENTED_EXIT_CODES)
        self.assertTrue(no_traceback(out, err))

    def test_cf21_staged_symlink_is_not_reported_as_a_broken_document(self):
        """AC-CF-21: reporting `missing-frontmatter` on a symlink is the defect."""
        rc, out, err = self.check("--staged")
        link_lines = [l for l in err.splitlines() if self.LINK in l]
        self.assertTrue(link_lines, "the symlink was not reported at all; stderr=%r" % err)
        self.assertNotIn(
            "missing-frontmatter",
            bracket_codes("\n".join(link_lines)),
            "a symlink was misreported as a document with no frontmatter",
        )

    def test_cf21_symlink_is_skipped_not_followed(self):
        """AC-CF-21: nothing is written through the link, inside or outside the repo."""
        self.check("--staged")

        self.assertTrue(
            (self.repo / self.LINK).is_symlink(), "the symlink was replaced by a regular file"
        )
        self.assertEqual(
            self.victim.read_text(), self.victim_before, "the tool wrote outside the repo"
        )


if __name__ == "__main__":
    unittest.main()
