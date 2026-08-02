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
    DOCUMENTED_EXIT_CODES,
    ascii_env,
    write_bytes,
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


# ---------------------------------------------------------------------------
# §8 — gate findings.
# ---------------------------------------------------------------------------


#: A valid `agreed` document whose body is not valid UTF-8 (0xE9 is latin-1).
LATIN1_DOC = (
    b"---\n"
    b"status: agreed\n"
    b"last-reviewed: reviews/r.md @ abc1234\n"
    b"audience: [all-roles]\n"
    b"superseded-by: null\n"
    b"---\n"
    b"\n# Caf\xe9 Policy\n\nbody\n"
)
EM_DASH_DOC = (
    "---\n"
    "status: draft\n"
    "last-reviewed: null\n"
    "audience: [all-roles]\n"
    "superseded-by: null\n"
    "---\n"
    "\n# Dashed \u2014 Policy\n\nProse with an em-dash \u2014 like this one.\n"
)
#: A context set that is *valid* under the metadata policy as well as carrying
#: composition fields, so it can sit in an in-scope tree without failing a
#: `--all` scan. `context_set_doc()` deliberately omits lifecycle fields
#: (test_mg4/test_mg5 depend on that), so this is built here instead.
EM_DASH_CONTEXT_SET = (
    "---\n"
    "context-set: base\n"
    "purpose: Entry point for the bundle smoke run \u2014 with an em-dash.\n"
    "include-when: Always.\n"
    "depends-on: []\n"
    "status: draft\n"
    "last-reviewed: null\n"
    "audience: [all-roles]\n"
    "superseded-by: null\n"
    "---\n"
    "\n# Context Set: Base\n\nProse with an em-dash \u2014 here too.\n"
)


class TestNoTracebacks(unittest.TestCase):
    """AC-X-6: every uncaught exception becomes a diagnostic and an exit code."""

    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        # These tests run whole-repo scans, so every seeded document affects the
        # outcome. `ok.md` is valid and exists only so the scan has something
        # readable; `latin1.md` is the one deliberately broken document, and it
        # is broken in exactly the way this class is about.
        write(self.repo, "policies/ok.md", agreed_doc())
        write_bytes(self.repo, "policies/latin1.md", LATIN1_DOC)
        commit(self.repo, "seed a non-utf-8 in-scope document", env=self.env)

    def assert_clean_failure(self, name, *args):
        rc, out, err = run_cli(name, *args, cwd=self.repo, env=self.env)
        self.assertTrue(
            no_traceback(out, err),
            "%s %s emitted a traceback:\n%s" % (name, " ".join(args), err),
        )
        self.assertIn(
            rc,
            DOCUMENTED_EXIT_CODES,
            "%s %s exited %s; stderr=%r" % (name, " ".join(args), rc, err),
        )
        return rc, out, err

    def test_x6_check_frontmatter_all_over_a_non_utf8_document(self):
        """AC-X-6: `check-frontmatter --all` must not raise UnicodeDecodeError."""
        self.assert_clean_failure("check-frontmatter", "--all")

    def test_x6_check_frontmatter_path_over_a_non_utf8_document(self):
        """AC-X-6: `check-frontmatter PATH` must not raise UnicodeDecodeError."""
        self.assert_clean_failure("check-frontmatter", "policies/latin1.md")

    def test_x6_migrate_frontmatter_plan_over_a_non_utf8_document(self):
        """AC-X-6: `migrate-frontmatter --plan` must not raise UnicodeDecodeError."""
        self.assert_clean_failure("migrate-frontmatter", "--plan")

    def test_x6_every_cli_survives_a_non_utf8_document_in_the_repo(self):
        """AC-X-6: no CLI tracebacks with an undecodable document present."""
        for name in CLI_NAMES:
            with self.subTest(cli=name):
                self.assert_clean_failure(name, *CLI_MINIMAL_ARGS[name])

    def test_x6_undecodable_document_is_named(self):
        """AC-X-6: the diagnostic identifies which document could not be read."""
        rc, out, err = self.assert_clean_failure("check-frontmatter", "--all")
        self.assertIn("policies/latin1.md", out + err)


class TestExplicitEncoding(unittest.TestCase):
    """AC-X-7: every read and write names UTF-8 rather than trusting the platform.

    A hook spawned by a GUI client can easily run under `LC_ALL=C`, where the
    default resolves to ASCII — and this repo is full of em-dashes.
    """

    ENCODED_CALLS = {"open", "read_text", "write_text"}

    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        # Every document seeded here is in scope, so every one of them affects
        # a `--all` scan. Both carry valid lifecycle frontmatter *and* an
        # em-dash, which is the only property this class is about.
        write(self.repo, "policies/dashed.md", EM_DASH_DOC)
        write(self.repo, "context-sets/base.md", EM_DASH_CONTEXT_SET)
        commit(self.repo, "seed em-dash documents", env=base_env())

    def unencoded_calls(self, path):
        """`(lineno, callee)` for text I/O calls that do not pass `encoding=`."""
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        offenders = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name):
                name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                name = node.func.attr
            else:
                continue
            if name not in self.ENCODED_CALLS:
                continue
            if any(kw.arg == "encoding" for kw in node.keywords):
                continue
            offenders.append((node.lineno, name))
        return offenders

    def test_x7_no_production_text_io_relies_on_the_platform_default(self):
        """AC-X-7: every `open`/`read_text`/`write_text` passes `encoding=`."""
        offenders = []
        for path in production_files():
            for lineno, name in self.unencoded_calls(path):
                offenders.append("%s:%d %s() without encoding=" % (path.name, lineno, name))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_x7_check_frontmatter_works_under_an_ascii_default_encoding(self):
        """AC-X-7: an em-dash document validates cleanly under `LC_ALL=C`."""
        env = ascii_env(methodology_home=self.home)
        rc, out, err = run_cli("check-frontmatter", "--all", cwd=self.repo, env=env)
        self.assertTrue(no_traceback(out, err), "traceback under LC_ALL=C:\n%s" % err)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

    def test_x7_migrate_frontmatter_works_under_an_ascii_default_encoding(self):
        """AC-X-7: `--plan` reads em-dash documents under `LC_ALL=C`."""
        env = ascii_env(methodology_home=self.home)
        rc, out, err = run_cli("migrate-frontmatter", "--plan", cwd=self.repo, env=env)
        self.assertTrue(no_traceback(out, err), "traceback under LC_ALL=C:\n%s" % err)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

    def test_x7_every_cli_survives_an_ascii_default_encoding(self):
        """AC-X-7: no CLI depends on the platform default text encoding."""
        env = ascii_env(methodology_home=self.home)
        for name in CLI_NAMES:
            with self.subTest(cli=name):
                rc, out, err = run_cli(
                    name, *CLI_MINIMAL_ARGS[name], cwd=self.repo, env=env
                )
                self.assertTrue(
                    no_traceback(out, err), "%s tracebacked under LC_ALL=C:\n%s" % (name, err)
                )
                self.assertIn(rc, DOCUMENTED_EXIT_CODES, "%s exited %s" % (name, rc))


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
