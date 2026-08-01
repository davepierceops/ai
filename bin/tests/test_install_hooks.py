"""AC-IH-*: `bin/install-hooks` and the pre-commit shim.

Contract: `docs/packages/package-a-spec.md` §3.9. AC-IH-7 is the end-to-end
proof: a real `git commit` in a throwaway repo with the hook installed, with
assertions on what actually landed in the commit.
"""

from __future__ import annotations

import os
import stat
import unittest

from tests.helpers import (
    agreed_doc,
    base_env,
    commit,
    draft_doc,
    frontmatter_block,
    git,
    make_home,
    make_repo,
    run_cli,
    show,
    snapshot_tree,
    stage,
    write,
)

MANAGED_MARKER = "# >>> ai-methodology frontmatter hook (managed) >>>"
BODY_V1 = "\n# Sample Policy\n\nOriginal body.\n"
BODY_V2 = "\n# Sample Policy\n\nEdited body.\n"


class InstallHooksTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

    def install(self, *args, cwd=None):
        return run_cli("install-hooks", *args, cwd=cwd or self.repo, env=self.env)

    def hook_path(self, repo=None):
        return (repo or self.repo) / ".git" / "hooks" / "pre-commit"

    def hook_text(self, name="pre-commit", repo=None):
        path = (repo or self.repo) / ".git" / "hooks" / name
        self.assertTrue(path.is_file(), "no hook file at %s" % path)
        return path.read_text()


class TestInstallation(InstallHooksTestCase):
    def test_ih1_writes_an_executable_pre_commit_hook(self):
        """AC-IH-1: an executable `pre-commit` lands in the repo's hooks dir."""
        rc, out, err = self.install()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        hook = self.hook_path()
        self.assertTrue(hook.is_file(), "no hook at %s" % hook)
        self.assertTrue(
            hook.stat().st_mode & stat.S_IXUSR, "hook is not executable: %o" % hook.stat().st_mode
        )

    def test_ih1_honours_core_hooks_path(self):
        """AC-IH-1: a configured `core.hooksPath` wins over the default location."""
        custom = self.repo / "githooks"
        custom.mkdir()
        git(self.repo, "config", "core.hooksPath", str(custom), env=self.env, check=True)

        rc, out, err = self.install()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue((custom / "pre-commit").is_file(), "hook not in core.hooksPath")
        self.assertFalse(self.hook_path().exists(), "hook also written to the default dir")

    def test_ih1_repo_flag_targets_another_repository(self):
        """AC-IH-1: `--repo DIR` installs into that repo, not the cwd's."""
        other = make_repo(self, name="other")
        rc, out, err = self.install("--repo", str(other))
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(self.hook_path(other).is_file())

    def test_ih2_shim_carries_the_managed_marker(self):
        """AC-IH-2: the shim is identifiable as managed."""
        rc, out, err = self.install()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(MANAGED_MARKER, self.hook_text())

    def test_ih2_shim_resolves_the_home_and_execs_check_frontmatter(self):
        """AC-IH-2: the shim follows the §2.1 discovery order and execs the checker."""
        rc, out, err = self.install()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        shim = self.hook_text()
        self.assertIn("AI_METHODOLOGY_HOME", shim)
        self.assertIn("bin/check-frontmatter", shim)
        self.assertIn("--staged", shim)
        self.assertIn("exec", shim)

    def test_ih3_reinstalling_over_a_managed_hook_is_idempotent(self):
        """AC-IH-3: a second install replaces the shim, exit 0, no backup."""
        self.assertEqual(self.install()[0], 0)
        first = self.hook_text()

        rc, out, err = self.install()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(self.hook_text(), first)
        self.assertFalse((self.repo / ".git/hooks/pre-commit.bak").exists())

    def test_ih4_refuses_an_unmanaged_hook(self):
        """AC-IH-4: an existing unmanaged `pre-commit` is never clobbered (exit 3)."""
        write(self.repo, ".git/hooks/pre-commit", "#!/bin/sh\necho mine\n")
        os.chmod(self.hook_path(), 0o755)

        rc, out, err = self.install()
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("echo mine", self.hook_text())

    def test_ih4_force_backs_up_before_replacing(self):
        """AC-IH-4: `--force` moves the old hook aside to `pre-commit.bak`."""
        write(self.repo, ".git/hooks/pre-commit", "#!/bin/sh\necho mine\n")
        os.chmod(self.hook_path(), 0o755)

        rc, out, err = self.install("--force")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("echo mine", self.hook_text("pre-commit.bak"))
        self.assertIn(MANAGED_MARKER, self.hook_text())

    def test_ih5_print_writes_to_stdout_and_touches_nothing(self):
        """AC-IH-5: `--print` emits the shim without installing it."""
        before = snapshot_tree(self.repo)

        rc, out, err = self.install("--print")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(MANAGED_MARKER, out)
        self.assertFalse(self.hook_path().exists())
        self.assertEqual(snapshot_tree(self.repo), before)

    def test_ih6_shim_contains_no_absolute_repo_paths(self):
        """AC-IH-6: the shim is portable — no machine-specific absolute paths."""
        rc, out, err = self.install("--print")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(MANAGED_MARKER, out, "no shim was printed")
        for needle in ["/Users/", "/home/", str(self.repo), str(self.home)]:
            self.assertNotIn(needle, out, "shim leaks %r" % needle)


class TestEndToEndHook(InstallHooksTestCase):
    """AC-IH-7: real git, real hook, real commits."""

    def setUp(self):
        super().setUp()
        write(self.repo, "policies/edited.md", agreed_doc(body=BODY_V1))
        write(self.repo, "policies/transitioned.md", agreed_doc(body=BODY_V1))
        write(self.repo, "policies/badaudience.md", draft_doc())
        commit(self.repo, "seed", env=self.env)
        rc, out, err = self.install()
        self.assertEqual(rc, 0, "install failed: %r %r" % (out, err))

    def do_commit(self, message):
        # Precondition for every AC-IH-7 assertion: the hook must exist, or
        # "the commit behaved" is a statement about plain git, not the hook.
        self.assertTrue(self.hook_path().is_file(), "no pre-commit hook installed")
        return git(self.repo, "commit", "-q", "-m", message, env=self.env)

    def test_ih7_content_edit_is_flipped_in_the_resulting_commit(self):
        """AC-IH-7: committing a content edit to an agreed doc records `in-review`."""
        write(self.repo, "policies/edited.md", agreed_doc(body=BODY_V2))
        stage(self.repo, "policies/edited.md", env=self.env)

        rc, out, err = self.do_commit("edit the agreed doc")
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))

        committed = show(self.repo, "HEAD:policies/edited.md", env=self.env)
        self.assertIn("status: in-review", committed)
        self.assertIn("last-reviewed: null", committed)
        self.assertIn("Edited body.", committed)

    def test_ih7_frontmatter_only_change_keeps_its_status(self):
        """AC-IH-7: a status-transition-shaped commit is not flipped by the hook."""
        write(
            self.repo,
            "policies/transitioned.md",
            agreed_doc(body=BODY_V1, audience=("all-roles", "human")),
        )
        stage(self.repo, "policies/transitioned.md", env=self.env)

        rc, out, err = self.do_commit("frontmatter-only change")
        self.assertEqual(rc, 0, "commit failed: stdout=%r stderr=%r" % (out, err))

        committed = show(self.repo, "HEAD:policies/transitioned.md", env=self.env)
        self.assertIn("status: agreed", committed)
        self.assertIn("audience: [all-roles, human]", committed)

    def test_ih7_invalid_audience_blocks_the_commit(self):
        """AC-IH-7: an invalid `audience` value fails the commit with non-zero git exit."""
        write(
            self.repo,
            "policies/badaudience.md",
            frontmatter_block(
                status="draft", last_reviewed=None, audience=["not-a-real-role"],
                superseded_by=None,
            )
            + BODY_V1,
        )
        stage(self.repo, "policies/badaudience.md", env=self.env)
        head_before = git(self.repo, "rev-parse", "HEAD", env=self.env, check=True)[1]

        rc, out, err = self.do_commit("introduce a bad audience")
        self.assertNotEqual(rc, 0, "commit should have been blocked: %r %r" % (out, err))
        head_after = git(self.repo, "rev-parse", "HEAD", env=self.env, check=True)[1]
        self.assertEqual(head_after, head_before)

    def test_ih7_no_verify_is_the_documented_override(self):
        """AC-IH-7: `--no-verify` still lets a blocked commit through (spec §6 risk 1)."""
        write(self.repo, "policies/legacy.md", "# Legacy doc with no frontmatter\n")
        stage(self.repo, "policies/legacy.md", env=self.env)

        rc, out, err = git(
            self.repo, "commit", "-q", "--no-verify", "-m", "legacy", env=self.env
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))


if __name__ == "__main__":
    unittest.main()
