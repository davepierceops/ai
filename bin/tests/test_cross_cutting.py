"""AC-X-*: cross-cutting acceptance criteria over the whole of `bin/`.

Contract: `docs/packages/package-a-spec.md` §4.

The static scans (AC-X-1, AC-X-2) deliberately cover **production files only**
— every file directly under `bin/` plus `bin/aimeta/*.py`. `bin/tests/` is
excluded on purpose: the test suite legitimately references the repository
root (it has to know where the fixtures and the scripts under test live), and
it is not shipped as part of the tool.
"""

from __future__ import annotations

import ast
import sys
import unittest

from tests.helpers import (
    BIN_DIR,
    CLI_MINIMAL_ARGS,
    CLI_NAMES,
    REPO_ROOT,
    agreed_doc,
    base_env,
    commit,
    context_set_doc,
    in_review_doc,
    make_home,
    make_repo,
    no_traceback,
    run_cli,
    snapshot_tree,
    temp_dir,
    write,
)


def production_files():
    """Every shipped file under `bin/` — CLIs and the `aimeta` package."""
    files = [
        p
        for p in sorted(BIN_DIR.iterdir())
        if p.is_file() and not p.name.startswith(".")
    ]
    files += sorted((BIN_DIR / "aimeta").glob("*.py"))
    return files


class TestNoAbsolutePaths(unittest.TestCase):
    #: Absolute-path prefixes that would tie a script to one machine or repo.
    FORBIDDEN = ["/Users/", "/home/", "/root/", str(REPO_ROOT)]

    def test_x1_no_production_file_hardcodes_a_repo_or_home_path(self):
        """AC-X-1: no file under `bin/` names a specific repository or user home."""
        offenders = []
        for path in production_files():
            text = path.read_text(errors="replace")
            for needle in self.FORBIDDEN:
                if needle in text:
                    offenders.append("%s contains %r" % (path.name, needle))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_x1_no_production_file_uses_a_tilde_home_reference(self):
        """AC-X-1: `~/`-rooted paths are equally machine-specific."""
        offenders = [
            path.name for path in production_files() if "~/" in path.read_text(errors="replace")
        ]
        self.assertEqual(offenders, [])


class TestStdlibOnly(unittest.TestCase):
    LOCAL_MODULES = {"aimeta"}

    def imported_top_level_modules(self, path):
        tree = ast.parse(path.read_text(), filename=str(path))
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    names.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.level == 0 and node.module:
                    names.add(node.module.split(".")[0])
        return names

    def test_x2_every_import_is_stdlib_or_local(self):
        """AC-X-2: no script imports a third-party module."""
        allowed = set(sys.stdlib_module_names) | self.LOCAL_MODULES
        offenders = []
        for path in production_files():
            for name in sorted(self.imported_top_level_modules(path)):
                if name not in allowed:
                    offenders.append("%s imports %s" % (path.name, name))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_x2_every_production_file_parses_as_python(self):
        """AC-X-2: the scan is meaningful only if every file actually parses."""
        for path in production_files():
            with self.subTest(path=path.name):
                ast.parse(path.read_text(), filename=str(path))


class TestCliSurface(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        write(self.repo, "policies/sample.md", agreed_doc())
        commit(self.repo, "seed", env=self.env)

    def test_x3_every_cli_supports_help_and_exits_zero(self):
        """AC-X-3: `--help` exits 0 on every CLI."""
        for name in CLI_NAMES:
            with self.subTest(cli=name):
                rc, out, err = run_cli(name, "--help", cwd=self.repo, env=self.env)
                self.assertEqual(rc, 0, "%s --help: stderr=%r" % (name, err))
                self.assertIn("usage", (out + err).lower())

    def test_x4_every_cli_fails_cleanly_outside_a_git_repository(self):
        """AC-X-4: outside a repo, exit 2 or 3 with no traceback."""
        outside = temp_dir(self, "aimeta-not-a-repo-")
        for name in CLI_NAMES:
            with self.subTest(cli=name):
                rc, out, err = run_cli(
                    name, *CLI_MINIMAL_ARGS[name], cwd=outside, env=self.env
                )
                self.assertIn(
                    rc, (2, 3), "%s: rc=%s stdout=%r stderr=%r" % (name, rc, out, err)
                )
                self.assertTrue(
                    no_traceback(out, err), "%s raised a traceback: %s" % (name, err)
                )
                self.assertTrue((out + err).strip(), "%s failed silently" % name)


class TestWriteContainment(unittest.TestCase):
    def setUp(self):
        self.sandbox = temp_dir(self, "aimeta-sandbox-")
        self.repo = make_repo(self, name="proj", parent=self.sandbox)
        self.home = make_home(self, parent=self.sandbox, name="home")
        self.env = base_env(methodology_home=self.home)

        write(self.repo, "policies/sample.md", in_review_doc())
        write(self.repo, "reviews/r.md", "# Review\n\nNo findings.\n")
        write(self.repo, "context-sets/entry.md", context_set_doc("entry"))
        self.sha = commit(self.repo, "seed", env=self.env)

    def test_x5_no_tool_writes_outside_the_invoking_repo(self):
        """AC-X-5: every CLI confines its writes to the repo it was invoked in."""
        skip = [self.repo, self.home / "bin"]
        before = snapshot_tree(self.sandbox, skip=skip)

        invocations = [
            ("check-frontmatter", ["--all"]),
            ("bundle", ["entry"]),
            ("migrate-frontmatter", ["--plan"]),
            ("cycle-open", ["--cycle", "1", "--title", "T", "policies/sample.md"]),
            (
                "flip-agreed",
                [
                    "policies/sample.md",
                    "--review",
                    "reviews/r.md @ %s" % self.sha[:7],
                    "--no-commit",
                ],
            ),
            ("install-hooks", []),
        ]
        for name, args in invocations:
            run_cli(name, *args, cwd=self.repo, env=self.env)

        after = snapshot_tree(self.sandbox, skip=skip)
        self.assertEqual(
            after, before, "a tool wrote outside the invoking repo"
        )

    def test_x5_tools_do_write_inside_the_invoking_repo(self):
        """AC-X-5: containment is not vacuous — the tools do produce output."""
        rc, out, err = run_cli(
            "cycle-open",
            "--cycle",
            "1",
            "--title",
            "T",
            "policies/sample.md",
            cwd=self.repo,
            env=self.env,
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue((self.repo / "docs/cycles/cycle-1-directive.md").is_file())


if __name__ == "__main__":
    unittest.main()
