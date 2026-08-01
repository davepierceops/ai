"""AC-CO-*: `bin/cycle-open` — directive skeleton + reviewed-revision bundle.

Contract: `docs/packages/package-a-spec.md` §3.6. The directive format is the
one in `skills/spec-review-cycle.md`; the SHAs are read from real git history,
never invented.
"""

from __future__ import annotations

import datetime
import re
import unittest

from tests.helpers import (
    agreed_doc,
    base_env,
    commit,
    context_set_doc,
    git,
    head_sha,
    make_home,
    make_repo,
    porcelain,
    read,
    run_cli,
    write,
)

DOC_A = "policies/alpha.md"
DOC_B = "policies/beta.md"
DIRECTIVE_7 = "docs/cycles/cycle-7-directive.md"
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
EM_DASH = "—"


class CycleOpenTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        write(self.repo, DOC_A, agreed_doc(body="\n# Alpha\n\nAlpha content v1.\n"))
        self.sha_a = commit(self.repo, "add alpha", env=self.env)
        write(self.repo, DOC_B, agreed_doc(body="\n# Beta\n\nBeta content v1.\n"))
        self.sha_b = commit(self.repo, "add beta", env=self.env)

    def open_cycle(self, *args):
        return run_cli("cycle-open", *args, cwd=self.repo, env=self.env)

    def directive(self, relpath=DIRECTIVE_7):
        self.assertTrue(
            (self.repo / relpath).is_file(),
            "no directive written at %s; worktree: %r"
            % (relpath, porcelain(self.repo, env=self.env)),
        )
        return read(self.repo, relpath)

    def bundle_file(self, relpath):
        self.assertTrue(
            (self.repo / relpath).is_file(),
            "no bundle artifact at %s; worktree: %r"
            % (relpath, porcelain(self.repo, env=self.env)),
        )
        return read(self.repo, relpath)


class TestDirectivePlacement(CycleOpenTestCase):
    def test_co1_cycle_number_names_the_directive(self):
        """AC-CO-1: `--cycle N` writes `docs/cycles/cycle-<N>-directive.md`."""
        rc, out, err = self.open_cycle("--cycle", "7", "--title", "Streamlining", DOC_A)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue((self.repo / DIRECTIVE_7).is_file(), porcelain(self.repo, env=self.env))

    def test_co1_slug_names_the_directive(self):
        """AC-CO-1: `--name SLUG` writes `docs/cycles/<SLUG>-directive.md`."""
        rc, out, err = self.open_cycle("--name", "streamlining", "--title", "T", DOC_A)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue((self.repo / "docs/cycles/streamlining-directive.md").is_file())

    def test_co1_neither_selector_is_a_usage_error(self):
        """AC-CO-1: exactly one of `--cycle`/`--name` is required (exit 2)."""
        rc, out, err = self.open_cycle(DOC_A)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_co1_both_selectors_is_a_usage_error(self):
        """AC-CO-1: `--cycle` and `--name` together is a usage error (exit 2)."""
        rc, out, err = self.open_cycle("--cycle", "7", "--name", "x", DOC_A)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_co2_refuses_to_overwrite_an_existing_directive(self):
        """AC-CO-2: an existing directive is never clobbered (exit 3)."""
        write(self.repo, DIRECTIVE_7, "# Cycle 7 Directive %s existing\n" % EM_DASH)
        commit(self.repo, "add directive", env=self.env)

        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A)
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("existing", self.directive())


class TestDirectiveContent(CycleOpenTestCase):
    def setUp(self):
        super().setUp()
        self.rc, self.out, self.err = self.open_cycle(
            "--cycle", "7", "--title", "Streamlining", "--date", "2026-08-01", DOC_A, DOC_B
        )

    def test_co3_heading_date_and_scope_list(self):
        """AC-CO-3: heading, `Date:` line, and `Documents in scope:` list."""
        self.assertEqual(self.rc, 0, "stdout=%r stderr=%r" % (self.out, self.err))
        text = self.directive()
        self.assertIn("# Cycle 7 Directive %s Streamlining" % EM_DASH, text)
        self.assertIn("Date: 2026-08-01", text)
        self.assertIn("Documents in scope:", text)
        self.assertRegex(text, r"- %s @ [0-9a-f]{40}" % re.escape(DOC_A))
        self.assertRegex(text, r"- %s @ [0-9a-f]{40}" % re.escape(DOC_B))

    def test_co3_required_sections_are_present(self):
        """AC-CO-3: Decisions, Deferred / out of scope, and Execution notes."""
        self.assertEqual(self.rc, 0, "stdout=%r stderr=%r" % (self.out, self.err))
        text = self.directive()
        self.assertIn("## Decisions", text)
        self.assertIn("## Deferred / out of scope", text)
        self.assertIn("## Execution notes", text)

    def test_co3_decisions_section_carries_a_commented_placeholder(self):
        """AC-CO-3: one commented placeholder decision entry with its three fields."""
        self.assertEqual(self.rc, 0, "stdout=%r stderr=%r" % (self.out, self.err))
        text = self.directive()
        section = text.split("## Decisions", 1)[1].split("## Deferred", 1)[0]
        self.assertIn("<!--", section)
        self.assertIn("Finding:", section)
        self.assertIn("Resolution:", section)
        self.assertIn("Dictated wording:", section)

    def test_co4_shas_are_full_and_come_from_git(self):
        """AC-CO-4: each recorded SHA is the full last-touching commit id."""
        self.assertEqual(self.rc, 0, "stdout=%r stderr=%r" % (self.out, self.err))
        text = self.directive()
        recorded = dict(re.findall(r"- (\S+\.md) @ ([0-9a-f]+)", text))
        self.assertEqual(recorded.get(DOC_A), self.sha_a)
        self.assertEqual(recorded.get(DOC_B), self.sha_b)
        for sha in recorded.values():
            self.assertRegex(sha, FULL_SHA_RE)


class TestPreconditions(CycleOpenTestCase):
    def test_co5_refuses_a_dirty_document(self):
        """AC-CO-5: uncommitted edits make the recorded SHA a lie (exit 3)."""
        write(self.repo, DOC_A, agreed_doc(body="\n# Alpha\n\nDirty edit.\n"))

        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A)
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertFalse((self.repo / DIRECTIVE_7).exists())

    def test_co5_allow_dirty_downgrades_to_a_warning(self):
        """AC-CO-5: `--allow-dirty` warns and proceeds."""
        write(self.repo, DOC_A, agreed_doc(body="\n# Alpha\n\nDirty edit.\n"))

        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "--allow-dirty", DOC_A
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("WARN", out + err)
        self.assertTrue((self.repo / DIRECTIVE_7).is_file())

    def test_co6_refuses_an_untracked_path(self):
        """AC-CO-6: an untracked document has no reviewed SHA (exit 1)."""
        write(self.repo, "policies/untracked.md", agreed_doc())

        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "policies/untracked.md"
        )
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("policies/untracked.md", out + err)

    def test_co6_refuses_a_nonexistent_path(self):
        """AC-CO-6: a path that does not exist is named and refused (exit 1)."""
        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "policies/never-existed.md"
        )
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("policies/never-existed.md", out + err)


class TestBundleEmission(CycleOpenTestCase):
    def test_co7_default_output_directory_and_flattened_names(self):
        """AC-CO-7: default `--out` is `.cycle-bundles/<directive-stem>/`."""
        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A, DOC_B)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        outdir = self.repo / ".cycle-bundles" / "cycle-7-directive"
        self.assertTrue(outdir.is_dir(), "missing %s" % outdir)
        self.assertTrue((outdir / "policies__alpha.md").is_file())
        self.assertTrue((outdir / "policies__beta.md").is_file())

    def test_co7_bundle_carries_the_reviewed_revision_not_the_worktree(self):
        """AC-CO-7: bundle content is `git show <sha>:<path>`, not the worktree."""
        write(self.repo, DOC_A, agreed_doc(body="\n# Alpha\n\nWORKTREE ONLY.\n"))

        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "--allow-dirty", DOC_A
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        bundled = self.bundle_file(".cycle-bundles/cycle-7-directive/policies__alpha.md")
        self.assertIn("Alpha content v1.", bundled)
        self.assertNotIn("WORKTREE ONLY", bundled)

    def test_co7_bundle_txt_lists_paths_shas_and_the_directive(self):
        """AC-CO-7: `BUNDLE.txt` lists `<path> @ <sha>` plus the directive path."""
        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A, DOC_B)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        manifest = self.bundle_file(".cycle-bundles/cycle-7-directive/BUNDLE.txt")
        self.assertIn("%s @ %s" % (DOC_A, self.sha_a), manifest)
        self.assertIn("%s @ %s" % (DOC_B, self.sha_b), manifest)
        self.assertIn(DIRECTIVE_7, manifest)

    def test_co7_out_flag_redirects_the_bundle(self):
        """AC-CO-7: `--out DIR` places the bundle where asked."""
        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "--out", "uploads", DOC_A
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue((self.repo / "uploads" / "policies__alpha.md").is_file())
        self.assertTrue((self.repo / "uploads" / "BUNDLE.txt").is_file())

    def test_co8_warns_when_the_bundle_directory_is_not_ignored(self):
        """AC-CO-8: an untracked-but-not-ignored bundle dir gets a WARN, still writes."""
        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("WARN", out + err)
        self.assertTrue((self.repo / ".cycle-bundles/cycle-7-directive").is_dir())

    def test_co8_no_warning_when_the_bundle_directory_is_ignored(self):
        """AC-CO-8: a gitignored bundle directory is not warned about."""
        write(self.repo, ".gitignore", ".cycle-bundles/\n")
        commit(self.repo, "ignore bundles", env=self.env)

        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("Documents in scope:", self.directive())
        self.assertNotIn("WARN", out + err)


class TestBundleExpansion(CycleOpenTestCase):
    def setUp(self):
        super().setUp()
        write(
            self.repo,
            "context-sets/entry.md",
            context_set_doc("entry", depends_on=["leaf"]),
        )
        write(self.repo, "context-sets/leaf.md", context_set_doc("leaf"))
        commit(self.repo, "add context sets", env=self.env)

    def test_co9_bundle_entry_expands_the_closure(self):
        """AC-CO-9: `--bundle ENTRY` pulls in the entry's reference closure."""
        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "--bundle", "entry"
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        text = self.directive()
        self.assertIn("context-sets/entry.md", text)
        self.assertIn("context-sets/leaf.md", text)

    def test_co9_union_with_explicit_paths_is_deduplicated_and_stable(self):
        """AC-CO-9: explicit PATHs union with the closure, no duplicates."""
        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T",
            "--bundle", "entry", "context-sets/leaf.md", DOC_A,
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        text = self.directive()
        scope_lines = [
            l for l in text.splitlines() if re.match(r"^- \S+\.md @ [0-9a-f]{40}$", l)
        ]
        paths = [l.split(" @ ")[0][2:] for l in scope_lines]
        self.assertEqual(len(paths), len(set(paths)), "duplicate entries: %r" % paths)
        self.assertIn("context-sets/leaf.md", paths)
        self.assertIn(DOC_A, paths)


class TestDateAndSideEffects(CycleOpenTestCase):
    def test_co10_date_flag_fixes_the_date_line(self):
        """AC-CO-10: `--date` makes the directive deterministic."""
        rc, out, err = self.open_cycle(
            "--cycle", "7", "--title", "T", "--date", "2020-02-29", DOC_A
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("Date: 2020-02-29", self.directive())

    def test_co10_default_date_is_today(self):
        """AC-CO-10: with no `--date`, today's local date is used."""
        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("Date: %s" % datetime.date.today().isoformat(), self.directive())

    def test_co11_does_not_stage_or_commit(self):
        """AC-CO-11: the tool never touches the index or creates a commit."""
        before_head = head_sha(self.repo, env=self.env)

        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A, DOC_B)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("Documents in scope:", self.directive())
        self.assertEqual(head_sha(self.repo, env=self.env), before_head)
        staged = git(
            self.repo, "diff", "--cached", "--name-only", env=self.env, check=True
        )[1]
        self.assertEqual(staged.strip(), "")

    def test_co11_modifies_no_document(self):
        """AC-CO-11: only the directive and the bundle directory appear."""
        rc, out, err = self.open_cycle("--cycle", "7", "--title", "T", DOC_A, DOC_B)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

        self.assertIn("Documents in scope:", self.directive())
        status = porcelain(self.repo, env=self.env)
        modified = [l for l in status.splitlines() if not l.startswith("??")]
        self.assertEqual(modified, [], "documents were modified: %r" % status)
        self.assertIn("Alpha content v1.", read(self.repo, DOC_A))


if __name__ == "__main__":
    unittest.main()
