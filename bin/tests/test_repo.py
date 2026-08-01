"""AC-RP-*: git and repository helpers.

Contract: `docs/packages/package-a-spec.md` §3.3. Every test here runs against
a real repository created with `git init` — there is no mocked git layer
(spec §5).
"""

from __future__ import annotations

import os
import unittest
from unittest import mock

from aimeta import repo as R

from tests.helpers import (
    agreed_doc,
    base_env,
    commit,
    disposition_doc,
    git,
    make_home,
    make_repo,
    role_doc,
    stage,
    temp_dir,
    write,
)


class RepoTestCase(unittest.TestCase):
    """Runs each test under a scrubbed environment.

    `aimeta.repo` shells out to git in-process, so the *test process* env has
    to be isolated too: no inherited `AI_METHODOLOGY_HOME`, no global or
    system git config, no global hooks.
    """

    def setUp(self):
        patcher = mock.patch.dict(os.environ, base_env(), clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)


class TestRepoRoot(RepoTestCase):
    def test_rp1_returns_the_top_level_of_the_containing_repo(self):
        """AC-RP-1: repo_root resolves upward to the repo top level."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        commit(root, "init")
        nested = root / "policies"
        self.assertEqual(R.repo_root(start=nested).resolve(), root.resolve())

    def test_rp1_returns_the_root_when_started_at_the_root(self):
        """AC-RP-1: starting at the root returns the root itself."""
        root = make_repo(self)
        write(root, "README.md", agreed_doc())
        commit(root, "init")
        self.assertEqual(R.repo_root(start=root).resolve(), root.resolve())

    def test_rp1_raises_outside_a_repository(self):
        """AC-RP-1: repo_root raises when there is no repo above the start path."""
        outside = temp_dir(self, "aimeta-not-a-repo-")
        with self.assertRaises(R.GitError):
            R.repo_root(start=outside)


class TestMethodologyHome(RepoTestCase):
    def test_rp2_env_var_wins(self):
        """AC-RP-2: `$AI_METHODOLOGY_HOME` is consulted first."""
        parent = temp_dir(self, "aimeta-layout-")
        root = make_repo(self, parent=parent)
        write(root, "bin/check-frontmatter", "#!/bin/sh\n")
        os.chmod(root / "bin" / "check-frontmatter", 0o755)
        home = make_home(self)
        with mock.patch.dict(os.environ, {"AI_METHODOLOGY_HOME": str(home)}):
            self.assertEqual(R.methodology_home(root).resolve(), home.resolve())

    def test_rp2_self_hosted_repo_is_the_second_candidate(self):
        """AC-RP-2: a repo carrying `bin/check-frontmatter` is its own home."""
        parent = temp_dir(self, "aimeta-layout-")
        root = make_repo(self, parent=parent)
        write(root, "bin/check-frontmatter", "#!/bin/sh\n")
        os.chmod(root / "bin" / "check-frontmatter", 0o755)
        self.assertEqual(R.methodology_home(root).resolve(), root.resolve())

    def test_rp2_sibling_ai_directory_is_the_third_candidate(self):
        """AC-RP-2: `<parent-of-repo-root>/ai` is the last candidate."""
        parent = temp_dir(self, "aimeta-layout-")
        root = make_repo(self, name="project", parent=parent)
        sibling = make_home(self, parent=parent, name="ai")
        self.assertEqual(R.methodology_home(root).resolve(), sibling.resolve())

    def test_rp2_invalid_env_var_falls_through(self):
        """AC-RP-2: a set-but-invalid env var falls through, it does not fail."""
        parent = temp_dir(self, "aimeta-layout-")
        root = make_repo(self, name="project", parent=parent)
        sibling = make_home(self, parent=parent, name="ai")
        bogus = temp_dir(self, "aimeta-bogus-home-")
        with mock.patch.dict(os.environ, {"AI_METHODOLOGY_HOME": str(bogus)}):
            self.assertEqual(R.methodology_home(root).resolve(), sibling.resolve())

    def test_rp2_raises_lookuperror_naming_the_fixes(self):
        """AC-RP-2: with no candidate, it raises LookupError naming the env var."""
        parent = temp_dir(self, "aimeta-layout-")
        root = make_repo(self, name="project", parent=parent)
        with self.assertRaises(LookupError) as ctx:
            R.methodology_home(root)
        self.assertIn("AI_METHODOLOGY_HOME", str(ctx.exception))


class TestLastCommitSha(RepoTestCase):
    def test_rp3_returns_the_full_sha_of_the_last_touching_commit(self):
        """AC-RP-3: the SHA is the full 40-char id of the last commit on the path."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        first = commit(root, "add a")
        sha = R.last_commit_sha(root, "policies/a.md")
        self.assertEqual(sha, first)
        self.assertEqual(len(sha), 40)

    def test_rp3_is_unaffected_by_commits_touching_other_paths(self):
        """AC-RP-3: an unrelated later commit does not change the path's SHA."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        first = commit(root, "add a")
        write(root, "policies/b.md", agreed_doc())
        commit(root, "add b")
        self.assertEqual(R.last_commit_sha(root, "policies/a.md"), first)

    def test_rp3_tracks_the_most_recent_touching_commit(self):
        """AC-RP-3: editing the path moves its recorded SHA forward."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        first = commit(root, "add a")
        write(root, "policies/a.md", agreed_doc(body="\n# Sample\n\nEdited.\n"))
        second = commit(root, "edit a")
        self.assertNotEqual(first, second)
        self.assertEqual(R.last_commit_sha(root, "policies/a.md"), second)

    def test_rp3_returns_none_for_an_untracked_path(self):
        """AC-RP-3: an untracked path has no commit SHA."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        commit(root, "add a")
        write(root, "policies/untracked.md", agreed_doc())
        self.assertIsNone(R.last_commit_sha(root, "policies/untracked.md"))


class TestFileAtRev(RepoTestCase):
    def test_rp4_reads_content_at_a_revision(self):
        """AC-RP-4: content is read at the named revision, not the worktree."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\nversion one\n"))
        first = commit(root, "v1")
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\nversion two\n"))
        commit(root, "v2")
        at_first = R.file_at_rev(root, first, "policies/a.md")
        at_head = R.file_at_rev(root, "HEAD", "policies/a.md")
        self.assertIsNotNone(at_first, "no content read at %s" % first)
        self.assertIsNotNone(at_head, "no content read at HEAD")
        self.assertIn("version one", at_first)
        self.assertIn("version two", at_head)

    def test_rp4_returns_none_when_absent_at_that_revision(self):
        """AC-RP-4: an absent path returns None rather than raising."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        first = commit(root, "v1")
        write(root, "policies/b.md", agreed_doc())
        commit(root, "v2")
        self.assertIsNone(R.file_at_rev(root, first, "policies/b.md"))
        self.assertIsNone(R.file_at_rev(root, "HEAD", "policies/never-existed.md"))

    def test_rp4_index_notation_reads_the_staged_blob(self):
        """AC-RP-4: `rev=":"` reads the staged blob, distinct from HEAD."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\ncommitted\n"))
        commit(root, "v1")
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\nstaged\n"))
        stage(root, "policies/a.md")
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\nworktree\n"))
        staged = R.file_at_rev(root, ":", "policies/a.md")
        committed = R.file_at_rev(root, "HEAD", "policies/a.md")
        self.assertIsNotNone(staged, "no staged blob read")
        self.assertIsNotNone(committed, "no committed blob read")
        self.assertIn("staged", staged)
        self.assertNotIn("worktree", staged)
        self.assertIn("committed", committed)


class TestStagedEntries(RepoTestCase):
    def test_rp5_reports_added_modified_and_deleted(self):
        """AC-RP-5: staged adds, modifications, and deletions carry A/M/D."""
        root = make_repo(self)
        # The deleted and added blobs must be *dissimilar*, not merely
        # differently named: git's rename detection is on by default, and a
        # staged delete/add pair of similar content is correctly reported as a
        # single `R` (which is what AC-RP-5's rename case asserts). Identical
        # bodies here would test rename detection, not add/delete reporting.
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\noriginal\n"))
        write(
            root,
            "policies/gone.md",
            agreed_doc(body="\n# Gone\n\n" + "content that is about to be deleted\n" * 40),
        )
        commit(root, "init")

        write(root, "policies/a.md", agreed_doc(body="\n# A\n\nedited\n"))
        write(
            root,
            "policies/new.md",
            agreed_doc(body="\n# New\n\n" + "an entirely unrelated new document\n" * 40),
        )
        git(root, "rm", "-q", "--", "policies/gone.md", check=True)
        stage(root, "policies/a.md", "policies/new.md")

        entries = dict((path, letter) for letter, path in R.staged_entries(root))
        self.assertEqual(entries.get("policies/a.md"), "M")
        self.assertEqual(entries.get("policies/new.md"), "A")
        self.assertEqual(entries.get("policies/gone.md"), "D")

    def test_rp5_reports_renames_as_r_with_the_new_path(self):
        """AC-RP-5: a staged rename is reported as `R` carrying the new path."""
        root = make_repo(self)
        write(root, "policies/old-name.md", agreed_doc(body="\n# A\n\n" + "x\n" * 40))
        commit(root, "init")
        git(root, "mv", "policies/old-name.md", "policies/new-name.md", check=True)

        entries = R.staged_entries(root)
        paths = [path for _, path in entries]
        self.assertIn("policies/new-name.md", paths)
        letter = dict((p, l) for l, p in entries)["policies/new-name.md"]
        self.assertEqual(letter, "R")

    def test_rp5_works_before_the_first_commit(self):
        """AC-RP-5: with no HEAD, the staged set is diffed against the empty tree."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        stage(root, "policies/a.md")
        self.assertEqual(R.staged_entries(root), [("A", "policies/a.md")])

    def test_rp5_is_empty_when_nothing_is_staged(self):
        """AC-RP-5: a clean index yields an empty list."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        commit(root, "init")
        self.assertEqual(R.staged_entries(root), [])

    def test_rp5_ignores_unstaged_worktree_edits(self):
        """AC-RP-5: only the index is reported, never the worktree."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        commit(root, "init")
        write(root, "policies/a.md", agreed_doc(body="\n# A\n\nunstaged\n"))
        self.assertEqual(R.staged_entries(root), [])


class TestRoleSlugs(RepoTestCase):
    def test_rp6_reads_the_invoking_repo_when_it_has_roles(self):
        """AC-RP-6: role slugs come from the invoking repo's `roles/`."""
        root = make_repo(self)
        for slug in ["coder-agent", "reviewer-agent"]:
            write(root, "roles/%s.md" % slug, role_doc(slug))
        commit(root, "init")
        home = make_home(self, roles=("someone-else",))
        self.assertEqual(R.role_slugs(root, home), {"coder-agent", "reviewer-agent"})

    def test_rp6_falls_back_to_the_methodology_home(self):
        """AC-RP-6: with no `roles/` in the repo, the home clone supplies them."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        commit(root, "init")
        home = make_home(self, roles=("coder-agent", "architect-agent"))
        self.assertEqual(R.role_slugs(root, home), {"coder-agent", "architect-agent"})

    def test_rp6_slugs_are_basenames_without_extension(self):
        """AC-RP-6: non-`.md` files in `roles/` are not slugs."""
        root = make_repo(self)
        write(root, "roles/coder-agent.md", role_doc("coder-agent"))
        write(root, "roles/notes.txt", "not a role\n")
        commit(root, "init")
        home = make_home(self)
        self.assertEqual(R.role_slugs(root, home), {"coder-agent"})


class TestDispositionPaths(RepoTestCase):
    def test_rp7_parses_backticked_md_paths(self):
        """AC-RP-7: every backticked `*.md` path in the disposition list is returned."""
        root = make_repo(self)
        write(
            root,
            R.DISPOSITION_PATH,
            disposition_doc(["policies/a.md", "roles/coder-agent.md"]),
        )
        commit(root, "init")
        self.assertEqual(
            R.disposition_paths(root), {"policies/a.md", "roles/coder-agent.md"}
        )

    def test_rp7_ignores_backticked_non_md_strings(self):
        """AC-RP-7: only `*.md` paths are collected."""
        root = make_repo(self)
        write(
            root,
            R.DISPOSITION_PATH,
            "# Disposition\n\n- `policies/a.md`\n- `status: agreed`\n- `bin/foo`\n",
        )
        commit(root, "init")
        self.assertEqual(R.disposition_paths(root), {"policies/a.md"})

    def test_rp7_empty_set_when_the_list_does_not_exist(self):
        """AC-RP-7: with no disposition list, the grandfather clause does not apply."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        commit(root, "init")
        self.assertEqual(R.disposition_paths(root), set())

    def test_rp7_disposition_path_constant(self):
        """AC-RP-7: the disposition list lives at the documented path."""
        self.assertEqual(R.DISPOSITION_PATH, "reviews/frontmatter-disposition.md")


class TestGitHelper(RepoTestCase):
    def test_rp1_git_returns_stripped_stdout(self):
        """AC-RP-1: `git()` returns stripped stdout for a successful invocation."""
        root = make_repo(self)
        write(root, "policies/a.md", agreed_doc())
        sha = commit(root, "init")
        self.assertEqual(R.git("rev-parse", "HEAD", cwd=root), sha)

    def test_rp1_git_raises_giterror_on_failure(self):
        """AC-RP-1: a non-zero git exit raises GitError."""
        root = make_repo(self)
        with self.assertRaises(R.GitError):
            R.git("rev-parse", "--verify", "definitely-not-a-ref", cwd=root)


if __name__ == "__main__":
    unittest.main()
