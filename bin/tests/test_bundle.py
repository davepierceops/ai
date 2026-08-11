"""AC-BN-*: `bin/bundle` — reference closure over entry-point context-sets.

Contract: `docs/packages/package-a-spec.md` §3.7.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re
import unittest

from tests.helpers import (
    REPO_ROOT,
    agreed_doc,
    base_env,
    bracket_codes,
    commit,
    context_set_doc,
    make_home,
    make_repo,
    run_cli,
    temp_dir,
    write,
)


ROOT = "context-sets/root.md"
MID = "context-sets/mid.md"
LEAF = "context-sets/leaf.md"
REFERENCED = "policies/referenced.md"
DEEP = "policies/deep.md"


class BundleTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        # root --depends-on--> mid --depends-on--> leaf
        # root --body-ref-----> policies/referenced.md --body-ref--> policies/deep.md
        write(
            self.repo,
            ROOT,
            context_set_doc(
                "root",
                depends_on=["mid"],
                body="\n# Root\n\nSee `%s` for the rules.\n" % REFERENCED,
            ),
        )
        write(self.repo, MID, context_set_doc("mid", depends_on=["leaf"]))
        write(self.repo, LEAF, context_set_doc("leaf"))
        write(
            self.repo,
            REFERENCED,
            agreed_doc(body="\n# Referenced\n\nDerives from `%s`.\n" % DEEP),
        )
        write(self.repo, DEEP, agreed_doc(body="\n# Deep\n\nLeaf policy.\n"))
        commit(self.repo, "seed closure", env=self.env)

    def bundle(self, *args, cwd=None):
        return run_cli("bundle", *args, cwd=cwd or self.repo, env=self.env)

    def paths(self, *args):
        rc, out, err = self.bundle(*args)
        return rc, [l for l in out.splitlines() if l.strip()], err


class TestClosure(BundleTestCase):
    def test_bn1_depends_on_edges_are_followed_transitively(self):
        """AC-BN-1: `depends-on` resolves to `context-sets/<name>.md`, transitively."""
        rc, paths, err = self.paths("root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn(MID, paths)
        self.assertIn(LEAF, paths)

    def test_bn1_body_references_are_followed_transitively(self):
        """AC-BN-1: backticked repo-relative `*.md` paths are closure edges too."""
        rc, paths, err = self.paths("root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn(REFERENCED, paths)
        self.assertIn(DEEP, paths)

    def test_bn1_a_repo_relative_path_is_a_valid_entry(self):
        """AC-BN-1: an ENTRY may be a path as well as a context-set name."""
        rc, paths, err = self.paths(REFERENCED)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertEqual(paths[:1], [REFERENCED])
        self.assertIn(DEEP, paths)

    def test_bn2_output_is_breadth_first_lexicographic_and_deduplicated(self):
        """AC-BN-2: deterministic BFS order, entry points first, no duplicates."""
        rc, paths, err = self.paths("root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertEqual(paths, [ROOT, MID, REFERENCED, LEAF, DEEP])
        self.assertEqual(len(paths), len(set(paths)))

    def test_bn2_multiple_entry_points_come_first_in_argument_order(self):
        """AC-BN-2: entry points precede everything they reach."""
        rc, paths, err = self.paths("root", "leaf")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertEqual(paths[:2], [ROOT, LEAF])
        self.assertEqual(len(paths), len(set(paths)))

    def test_bn3_reference_cycles_terminate(self):
        """AC-BN-3: a mutual `depends-on` pair yields two entries, not a hang."""
        write(self.repo, "context-sets/cyc-a.md", context_set_doc("cyc-a", depends_on=["cyc-b"]))
        write(self.repo, "context-sets/cyc-b.md", context_set_doc("cyc-b", depends_on=["cyc-a"]))
        commit(self.repo, "add cycle", env=self.env)

        rc, paths, err = self.paths("cyc-a")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertEqual(paths, ["context-sets/cyc-a.md", "context-sets/cyc-b.md"])

    def test_bn4_max_depth_zero_yields_only_entry_points(self):
        """AC-BN-4: `--max-depth 0` truncates to the entry points."""
        rc, paths, err = self.paths("--max-depth", "0", "root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertEqual(paths, [ROOT])

    def test_bn4_max_depth_one_yields_direct_references_only(self):
        """AC-BN-4: `--max-depth 1` stops after the entry's direct references."""
        rc, paths, err = self.paths("--max-depth", "1", "root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertEqual(paths, [ROOT, MID, REFERENCED])


class TestDanglingReferences(BundleTestCase):
    def setUp(self):
        super().setUp()
        write(
            self.repo,
            "context-sets/dangler.md",
            context_set_doc("dangler", depends_on=["no-such-context-set"]),
        )
        commit(self.repo, "add dangler", env=self.env)

    def test_bn5_dangling_depends_on_warns_and_is_omitted(self):
        """AC-BN-5: an unresolvable `depends-on` warns and drops out of the closure."""
        rc, paths, err = self.paths("dangler")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("dangling-reference", bracket_codes(err))
        self.assertIn("WARN", err)
        self.assertEqual(paths, ["context-sets/dangler.md"])

    def test_bn5_strict_makes_a_dangling_reference_fatal(self):
        """AC-BN-5: `--strict` turns the warning into exit 1."""
        rc, out, err = self.bundle("--strict", "dangler")
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("dangling-reference", bracket_codes(err))

    def test_bn6_backticked_non_files_are_silently_ignored(self):
        """AC-BN-6: only declared `depends-on` edges are strict."""
        write(
            self.repo,
            "context-sets/noisy.md",
            context_set_doc(
                "noisy",
                body=(
                    "\n# Noisy\n\nSet `status: agreed` and see `somewhere/absent.md` "
                    "plus `bin/check-frontmatter`.\n"
                ),
            ),
        )
        commit(self.repo, "add noisy", env=self.env)

        rc, out, err = self.bundle("--strict", "noisy")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertNotIn("dangling-reference", bracket_codes(err))
        self.assertEqual(
            [l for l in out.splitlines() if l.strip()], ["context-sets/noisy.md"]
        )


class TestOutputFormats(BundleTestCase):
    def test_bn7_list_format_prints_paths_and_nothing_else(self):
        """AC-BN-7: `--format list` is one repo-relative path per line on stdout."""
        rc, out, err = self.bundle("--format", "list", "root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        lines = out.splitlines()
        self.assertEqual(lines, [ROOT, MID, REFERENCED, LEAF, DEEP])
        for line in lines:
            self.assertFalse(line.startswith(" "), "unexpected annotation: %r" % line)

    def test_bn7_json_format_carries_path_depth_and_via(self):
        """AC-BN-7: `--format json` emits objects with path, depth, and via."""
        rc, out, err = self.bundle("--format", "json", "root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertTrue(
            out.strip().startswith("["), "not a JSON array: %r" % out[:120]
        )
        data = json.loads(out)
        self.assertIsInstance(data, list)
        by_path = {entry["path"]: entry for entry in data}
        self.assertEqual(by_path[ROOT]["depth"], 0)
        self.assertIsNone(by_path[ROOT]["via"])
        self.assertEqual(by_path[MID]["depth"], 1)
        self.assertEqual(by_path[MID]["via"], ROOT)
        self.assertEqual(by_path[DEEP]["depth"], 2)
        self.assertEqual(by_path[DEEP]["via"], REFERENCED)

    def test_bn7_concat_format_separates_documents_with_path_and_sha(self):
        """AC-BN-7: `--format concat` precedes each document with `===== path @ sha =====`."""
        rc, out, err = self.bundle("--format", "concat", "root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertRegex(out, r"===== %s @ [0-9a-f]{7,40} =====" % re.escape(ROOT))
        self.assertRegex(out, r"===== %s @ [0-9a-f]{7,40} =====" % re.escape(LEAF))
        self.assertIn("# Root", out)
        self.assertIn("# Deep", out)

    def test_bn8_why_annotates_referrer_and_depth(self):
        """AC-BN-8: `--why` adds `  <- <referrer> (depth N)` to list output."""
        rc, out, err = self.bundle("--why", "root")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("  <- %s (depth 1)" % ROOT, out)
        self.assertIn("  <- %s (depth 2)" % REFERENCED, out)

    def test_bn9_unresolvable_entry_exits_two_naming_it(self):
        """AC-BN-9: an ENTRY that resolves to no file is a usage error."""
        rc, out, err = self.bundle("no-such-entry")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("no-such-entry", out + err)


class TestAgainstThisRepository(unittest.TestCase):
    """AC-BN-10 runs against the real methodology repo. Read-only."""

    def setUp(self):
        self.env = base_env(methodology_home=REPO_ROOT)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=REPO_ROOT, env=self.env)

    def test_bn10_bundle_base_yields_exactly_itself(self):
        """AC-BN-10(a): `bundle base` yields exactly `context-sets/base.md`.

        Tightened from `assertIn` to `assertEqual` when §3.7 was revised:
        `base.md` declares `depends-on: []` and cites no documents, so a
        closure returning anything more is over-collecting.
        """
        rc, out, err = self.bundle("base")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(
            [l for l in out.splitlines() if l.strip()], ["context-sets/base.md"]
        )

    def test_bn10_transitive_body_references_are_followed_in_this_repo(self):
        """AC-BN-10: `policies/source-of-truth-policy.md` is reachable from `operating-model.md`.

        The spec's regression anchor. Note that it is asserted from
        `operating-model.md`, which is where that reference actually lives;
        `context-sets/base.md` declares `depends-on: []` and cites no
        documents, so nothing is reachable from `base` alone.
        """
        rc, out, err = self.bundle("operating-model.md")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        paths = out.splitlines()
        self.assertIn("operating-model.md", paths)
        self.assertIn("policies/source-of-truth-policy.md", paths)


# ---------------------------------------------------------------- AC-BN-11..15: --write mode

WRITE_STAMP_PATTERN = r"\d{4}-\d{2}-\d{2}-\d{4}"


def write_name_re(entry_stem):
    """Regex for the `--write` filename convention (AC-BN-13), built from a
    literal `<entry>` stem rather than hardcoded to any one fixture entry."""
    return re.compile(
        r"^%s-context-bundle-%s\.md$" % (re.escape(entry_stem), WRITE_STAMP_PATTERN)
    )


def find_write_files(out_dir):
    """Every `<entry>-context-bundle-<stamp>.md` file directly under `out_dir`."""
    return sorted(pathlib.Path(out_dir).glob("*-context-bundle-*.md"))


class TestWriteMode(BundleTestCase):
    def out_dir(self, prefix="bundle-write-out-"):
        return temp_dir(self, prefix)

    def test_bn12_default_out_dir_is_home_downloads(self):
        """AC-BN-12: `--write` with no `--out` writes under `$HOME/Downloads`."""
        write_home = temp_dir(self, "bundle-write-home-")
        env = base_env(methodology_home=self.home, home=write_home)
        rc, out, err = run_cli("bundle", "root", "--write", cwd=self.repo, env=env)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        downloads = write_home / "Downloads"
        files = find_write_files(downloads)
        self.assertEqual(
            len(files), 1, "expected exactly one file in %s, found %r" % (downloads, files)
        )
        self.assertRegex(files[0].name, write_name_re("root"))

    def test_bn14_out_dir_is_created_with_mkdir_p_semantics(self):
        """AC-BN-14: a missing, multi-level `--out DIR` is created once rendering
        succeeds, matching AC-BM-1's `bundle-methodology` semantics."""
        parent = self.out_dir("bundle-write-parent-")
        nested = parent / "a" / "b" / "c"
        self.assertFalse(nested.exists())
        rc, out, err = self.bundle("root", "--write", "--out", nested)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        files = find_write_files(nested)
        self.assertEqual(
            len(files), 1, "expected exactly one file in %s, found %r" % (nested, files)
        )

    def test_bn13_stamp_format_matches_bundle_methodology_convention(self):
        """AC-BN-13: the stamp is `%Y-%m-%d-%H%M`, local time — same as
        `bin/bundle-methodology`'s."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle("root", "--write", "--out", out_dir)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        files = find_write_files(out_dir)
        self.assertEqual(len(files), 1, "stdout=%r stderr=%r" % (out, err))
        name = files[0].name
        self.assertRegex(name, write_name_re("root"))
        stamp = name[len("root-context-bundle-") : -len(".md")]
        # Raises ValueError (failing the test) if the stamp isn't exactly
        # %Y-%m-%d-%H%M.
        datetime.datetime.strptime(stamp, "%Y-%m-%d-%H%M")

    def test_bn13_entry_stem_for_a_context_set_name_entry(self):
        """AC-BN-13: `bundle root --write` names the file `root-context-bundle-...`
        (the entry is a context-set name)."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle("root", "--write", "--out", out_dir)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        files = find_write_files(out_dir)
        self.assertEqual(len(files), 1, "stdout=%r stderr=%r" % (out, err))
        self.assertRegex(files[0].name, write_name_re("root"))

    def test_bn13_entry_stem_for_a_repo_relative_path_entry(self):
        """AC-BN-13: `bundle context-sets/leaf.md --write` names the file
        `leaf-context-bundle-...` (the entry is a repo-relative path; the stem
        is the resolved path's basename with `.md` stripped)."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle(LEAF, "--write", "--out", out_dir)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        files = find_write_files(out_dir)
        self.assertEqual(len(files), 1, "stdout=%r stderr=%r" % (out, err))
        self.assertRegex(files[0].name, write_name_re("leaf"))

    def test_bn11_more_than_one_entry_is_a_usage_error_and_writes_nothing(self):
        """AC-BN-11: `--write` combined with more than one `ENTRY` exits 2 and
        writes nothing."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle("root", "leaf", "--write", "--out", out_dir)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(find_write_files(out_dir), [])

    def test_bn11_explicit_non_concat_format_is_a_usage_error_and_writes_nothing(self):
        """AC-BN-11: `--write` combined with an explicit `--format` other than
        `concat` (e.g. `json`) exits 2 and writes nothing."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle("root", "--write", "--format", "json", "--out", out_dir)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(find_write_files(out_dir), [])

    def test_bn11_explicit_concat_format_is_redundant_but_permitted(self):
        """AC-BN-11: `--write --format concat` is explicit but matches the
        implied form, so it succeeds like plain `--write`."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle("root", "--write", "--format", "concat", "--out", out_dir)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(find_write_files(out_dir)), 1)

    def test_bn12_out_without_write_is_a_usage_error(self):
        """AC-BN-12: `--out DIR` supplied without `--write` is a usage error,
        and the directory is never created."""
        parent = self.out_dir("bundle-write-unused-")
        target = parent / "unused-out"
        self.assertFalse(target.exists())
        rc, out, err = self.bundle("root", "--out", target)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertFalse(target.exists())

    def test_bn14_unresolvable_entry_creates_no_out_dir_and_no_file(self):
        """AC-BN-14: a resolution failure (the existing AC-BN-9 error) happens
        before rendering completes, so it creates no `--out DIR` and leaves no
        file, anywhere."""
        parent = self.out_dir("bundle-write-fail-parent-")
        out_dir = parent / "does-not-exist-yet"
        self.assertFalse(out_dir.exists())
        rc, out, err = self.bundle("no-such-entry", "--write", "--out", out_dir)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertFalse(
            out_dir.exists(), "AC-BN-14: --out dir was created despite the failure"
        )
        self.assertEqual(
            find_write_files(parent),
            [],
            "AC-BN-14: a bundle file was written despite the failure",
        )

    def test_bn15_success_prints_exactly_one_wrote_line_with_a_valid_path(self):
        """AC-BN-15: on success, stdout is exactly one `wrote <absolute path>`
        line and nothing else, and the file it names is the rendered concat
        bundle."""
        out_dir = self.out_dir()
        rc, out, err = self.bundle("root", "--write", "--out", out_dir)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        lines = out.splitlines()
        self.assertEqual(
            len(lines), 1, "expected exactly one stdout line, got %r" % (lines,)
        )
        m = re.match(r"^wrote (/.*)$", lines[0])
        self.assertIsNotNone(m, "unexpected stdout line: %r" % lines[0])
        written_path = pathlib.Path(m.group(1))
        self.assertTrue(written_path.is_absolute(), "%s is not absolute" % written_path)
        self.assertTrue(written_path.exists(), "%s does not exist" % written_path)
        content = written_path.read_text(encoding="utf-8")
        self.assertRegex(content, r"===== %s @ [0-9a-f]{7,40} =====" % re.escape(ROOT))

    def test_bn7_format_list_and_json_still_work_when_write_is_absent(self):
        """Regression guard: adding `--write`/`--out` to the parser must not
        disturb explicit `--format list`/`--format json` when `--write` is
        absent (AC-BN-7, unaffected by §3.7.1)."""
        rc, out, err = self.bundle("--format", "list", "root")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(
            [l for l in out.splitlines() if l.strip()], [ROOT, MID, REFERENCED, LEAF, DEEP]
        )

        rc, out, err = self.bundle("--format", "json", "root")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        data = json.loads(out)
        self.assertIsInstance(data, list)
        self.assertTrue(any(entry["path"] == ROOT for entry in data))


if __name__ == "__main__":
    unittest.main()
