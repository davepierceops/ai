"""AC-BM-*: `bin/bundle-methodology` — regenerate the methodology-context-bundle.

Contract: `docs/packages/bundle-methodology-spec.md` §6 (AC-BM-1..9) and §7 (the
byte-exact concrete rendering). The golden-oracle strategy is §8: this suite
transcribes `decisions/log.md` `DEC-000140`'s interim generation procedure
into a test helper (`dec140_render`, parameterized on the file-set list and
the output path, never on `~/code/`) and diffs the real CLI's output against
it, rather than against a second hand-written expectation that could itself
drift from the recorded reference behavior.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import unittest

from aimeta import frontmatter as fm

from tests.helpers import (
    REPO_ROOT,
    base_env,
    commit,
    git,
    head_sha,
    make_home,
    make_repo,
    porcelain,
    run_cli,
    temp_dir,
    write,
)


# ---------------------------------------------------------------- fixed spine

SPINE = [
    "context-sets/spec-and-change-discipline.md",
    "operating-model.md",
    "roles/chief-of-staff.md",
    "policies/commit-and-change-control-policy.md",
]


def spine_content(path):
    """Minimal, unique placeholder content — the spec only requires the six
    spine paths to exist and be committed at known paths (§4)."""
    return "# %s\n\nPlaceholder content for `%s`.\n" % (path, path)


# ---------------------------------------------------------------- skill fixtures

SKILL_ALPHA = (
    "---\n"
    "status: agreed\n"
    "last-reviewed: reviews/sample-review.md @ abc1234\n"
    "audience: [all-roles, coder-agent]\n"
    "superseded-by: null\n"
    "---\n"
    "\n# Alpha Skill\n\nMatches the file-set rule via inline `all-roles`.\n"
)

SKILL_GAMMA = (
    "---\n"
    "status: agreed\n"
    "last-reviewed: reviews/sample-review.md @ abc1234\n"
    "audience:\n"
    "- chief-of-staff\n"
    "superseded-by: null\n"
    "---\n"
    "\n# Gamma Skill\n\nMatches the file-set rule via block-list `chief-of-staff`.\n"
)

SKILL_BETA = (
    "---\n"
    "status: agreed\n"
    "last-reviewed: reviews/sample-review.md @ abc1234\n"
    "audience: [coder-agent]\n"
    "superseded-by: null\n"
    "---\n"
    "\n# Beta Skill\n\nNeither `all-roles` nor `chief-of-staff`: excluded.\n"
)

SKILL_DELTA = (
    "# Delta Skill\n\nNo frontmatter at all, so no `audience` field: excluded.\n"
)

SKILL_FIXTURES = {
    "skills/alpha-role.md": SKILL_ALPHA,
    "skills/beta-excluded.md": SKILL_BETA,
    "skills/gamma-chief-of-staff.md": SKILL_GAMMA,
    "skills/delta-no-audience.md": SKILL_DELTA,
}

# Lexicographic order among the fixtures above, per AC-BM-4.
EXPECTED_MATCHING_SKILLS = ["skills/alpha-role.md", "skills/gamma-chief-of-staff.md"]
EXPECTED_FILE_SET = SPINE + EXPECTED_MATCHING_SKILLS


# ---------------------------------------------------------------- misc helpers

BUNDLE_NAME_RE = re.compile(r"^methodology-context-bundle-\d{4}-\d{2}-\d{2}-\d{4}\.md$")
GENERATED_LINE_RE = re.compile(r"^- Generated: .*$", re.M)
LIST_ENTRY_RE = re.compile(r"^  (\d+)\. (\S+) \(blob ([0-9a-f]{4,40})\)$", re.M)


def normalize_generated(text):
    """Strip the `Generated:` line so two runs can be compared byte-for-byte."""
    return GENERATED_LINE_RE.sub("- Generated: <normalized>", text)


def find_bundle_files(out_dir):
    return sorted(pathlib.Path(out_dir).glob("methodology-context-bundle-*.md"))


def parse_file_list(bundle_text):
    """`{path: short_sha}` from the numbered file list (AC-BM-4)."""
    return {path: sha for _, path, sha in LIST_ENTRY_RE.findall(bundle_text)}


def audience_values(doc_text):
    doc = fm.parse_text(doc_text)
    value = doc.fields.get("audience")
    if value is None:
        return set()
    if isinstance(value, (list, tuple)):
        return set(value)
    return {value}


def expected_skill_paths(repo):
    """Independent recomputation of §4's rule, via the real frontmatter dialect
    (`aimeta.frontmatter.parse_text`), not a hand-rolled regex — so this stays
    honest about both the inline `[a, b]` and block `- item` forms."""
    skills_dir = pathlib.Path(repo) / "skills"
    matches = []
    for path in sorted(skills_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if audience_values(text) & {"all-roles", "chief-of-staff"}:
            matches.append("skills/%s" % path.name)
    return matches


def dec140_render(repo, files, stamp, env=None):
    """`DEC-000140`'s interim generation procedure, transcribed verbatim from
    `decisions/log.md`, parameterized only on the file-set list and the
    generation stamp (never hardcoded to `~/code/`, and never recomputing the
    audience-selection rule itself — the caller supplies `files`, exactly as
    `docs/packages/bundle-methodology-spec.md` §8 describes the golden-oracle
    strategy: "parameterized only on the file-set list and the output path").

    Same algorithm as the recorded procedure: `git rev-parse HEAD`, a
    `git rev-parse --short HEAD:<path>` per file, the same header lines, the
    same numbered list, the same `<!-- FILE n/N -->` separator blocks, and the
    same `rstrip("\\n")` body normalization. Bodies are read from the fixture
    repo's worktree (not from the git blob), exactly as the recorded procedure
    does — safe here because every fixture commits before rendering.
    """
    env = env or base_env()

    def sh(*args):
        return subprocess.check_output(
            ["git", *args], cwd=str(repo), env=env
        ).decode()

    repo_sha = sh("rev-parse", "HEAD").strip()

    def blob(path):
        return sh("rev-parse", "--short", "HEAD:%s" % path).strip()

    file_count = len(files)
    bar = "<!-- " + "=" * 60 + " -->"
    out = [
        "# methodology-context-bundle\n",
        "**Derived artifact — do not edit.** Regenerate from davepierceops/ai; "
        "the repo is canonical.\n",
        "- Source: davepierceops/ai @ %s" % repo_sha,
        "- Generated: %s" % stamp,
        "- File set: fixed decision-layer spine + every skills/*.md whose "
        "audience includes all-roles or chief-of-staff (rule; Dave "
        "2026-08-07).\n",
    ]
    out += [
        "  %d. %s (blob %s)" % (i, path, blob(path))
        for i, path in enumerate(files, 1)
    ]
    out.append("")
    for i, path in enumerate(files, 1):
        body = (pathlib.Path(repo) / path).read_text(encoding="utf-8")
        out += [
            "",
            bar,
            "<!-- FILE %d/%d: %s @ %s -->" % (i, file_count, path, blob(path)),
            bar,
            "",
            body.rstrip("\n"),
            "",
        ]
    return "\n".join(out) + "\n"


def load_spec_section_7_rendering():
    """The literal byte-exact rendering from §7, extracted from the spec doc
    itself (not retyped), so a future edit to that fixture cannot silently
    drift from what this suite checks against."""
    spec_path = REPO_ROOT / "docs/packages/bundle-methodology-spec.md"
    text = spec_path.read_text(encoding="utf-8")
    marker = "the byte-exact output is:\n\n```\n"
    start = text.index(marker) + len(marker)
    end = text.index("\n```\n", start) + 1  # keep the trailing newline
    return text[start:end]


# ---------------------------------------------------------------- base fixture


class BundleMethodologyTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        for path in SPINE:
            write(self.repo, path, spine_content(path))
        for path, text in SKILL_FIXTURES.items():
            write(self.repo, path, text)
        commit(self.repo, "seed fixture tree", env=self.env)

    def run_bm(self, *args, cwd=None):
        return run_cli("bundle-methodology", *args, cwd=cwd or self.repo, env=self.env)

    def out_dir(self):
        return temp_dir(self, "bundle-methodology-out-")

    def write_one(self, out_dir=None):
        """Run the CLI once and return `(rc, out, err, bundle_path_or_None)`."""
        out_dir = out_dir or self.out_dir()
        rc, out, err = self.run_bm("--out", out_dir)
        files = find_bundle_files(out_dir)
        return rc, out, err, (files[0] if files else None)


# ---------------------------------------------------------------- AC-BM-1


class TestFileNaming(BundleMethodologyTestCase):
    def test_bm1_writes_exactly_one_correctly_named_file(self):
        """AC-BM-1: one `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md` in `--out DIR`."""
        out_dir = self.out_dir()
        rc, out, err = self.run_bm("--out", out_dir)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        written = find_bundle_files(out_dir)
        self.assertEqual(
            len(written), 1, "expected exactly one bundle file, found %r" % written
        )
        self.assertRegex(written[0].name, BUNDLE_NAME_RE)

    def test_bm1_out_dir_is_created_with_mkdir_p_semantics(self):
        """AC-BM-1: a missing, multi-level `--out DIR` is created, not an error."""
        parent = self.out_dir()
        nested = parent / "a" / "b" / "c"
        self.assertFalse(nested.exists())
        rc, out, err = self.run_bm("--out", nested)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(find_bundle_files(nested)), 1)

    def test_bm1_relative_out_dir_resolves_against_invoking_cwd(self):
        """AC-BM-1/§2: a repo-relative `--out` resolves against the invoking cwd."""
        rc, out, err = self.run_bm("--out", "bundle-out", cwd=self.repo)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(find_bundle_files(self.repo / "bundle-out")), 1)

    def test_bm1_explicit_out_tilde_is_expanded(self):
        """AC-BM-1/§2: `--out ~/x` is tilde-expanded against the invoking
        user's home directory, not treated as a literal `~` directory
        created under the invoking cwd."""
        write_home = temp_dir(self, "bundle-methodology-tilde-home-")
        env = base_env(methodology_home=self.home, home=write_home)
        rc, out, err = run_cli(
            "bundle-methodology", "--out", "~/tilde-out", cwd=self.repo, env=env
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        expected_dir = write_home / "tilde-out"
        files = find_bundle_files(expected_dir)
        self.assertEqual(
            len(files), 1, "expected exactly one file in %s, found %r" % (expected_dir, files)
        )
        literal_tilde = self.repo / "~"
        self.assertFalse(
            literal_tilde.exists(), "a literal '~' directory was created under cwd"
        )


# ---------------------------------------------------------------- AC-BM-2..5: golden oracle


class TestGoldenOracle(BundleMethodologyTestCase):
    def test_bm2_bm3_bm4_bm5_output_byte_matches_the_dec140_oracle(self):
        """AC-BM-2/3/4/5: header, file set, numbered list, and separators all
        byte-match `DEC-000140`'s procedure (transcribed, not re-derived),
        modulo the `Generated:` line (§8)."""
        files = SPINE + expected_skill_paths(self.repo)
        self.assertEqual(
            files, EXPECTED_FILE_SET, "fixture drifted from the expected file set"
        )

        oracle = dec140_render(self.repo, files, stamp="oracle-stamp", env=self.env)

        rc, out, err, bundle_path = self.write_one()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIsNotNone(bundle_path, "no bundle file written; stderr=%r" % err)
        actual = bundle_path.read_text(encoding="utf-8")

        self.assertEqual(
            normalize_generated(actual),
            normalize_generated(oracle),
            "CLI output does not byte-match the DEC-000140 oracle",
        )

    def test_bm3_file_set_is_the_spine_plus_matching_skills_in_order(self):
        """AC-BM-3: spine first (§4 order), then matching skills, lexicographic."""
        rc, out, err, bundle_path = self.write_one()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        entries = parse_file_list(bundle_path.read_text(encoding="utf-8"))
        self.assertEqual(list(entries.keys()), EXPECTED_FILE_SET)

    def test_bm3_excluded_skills_are_absent_from_the_file_list(self):
        """AC-BM-3: a skill matching neither `all-roles` nor `chief-of-staff`,
        or carrying no frontmatter at all, is excluded."""
        rc, out, err, bundle_path = self.write_one()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        entries = parse_file_list(bundle_path.read_text(encoding="utf-8"))
        self.assertNotIn("skills/beta-excluded.md", entries)
        self.assertNotIn("skills/delta-no-audience.md", entries)

    def test_bm3_a_new_matching_skill_is_picked_up_on_the_next_run_no_code_change(self):
        """AC-BM-3: the file set is computed every run, never a hardcoded list —
        add a skill between two runs and the list changes accordingly."""
        rc1, out1, err1, bundle1 = self.write_one()
        self.assertEqual(rc1, 0, "stdout=%r stderr=%r" % (out1, err1))
        before = parse_file_list(bundle1.read_text(encoding="utf-8"))
        self.assertNotIn("skills/epsilon-new.md", before)

        write(
            self.repo,
            "skills/epsilon-new.md",
            "---\n"
            "status: agreed\n"
            "last-reviewed: reviews/sample-review.md @ abc1234\n"
            "audience: [all-roles]\n"
            "superseded-by: null\n"
            "---\n"
            "\n# Epsilon Skill\n\nAdded between two runs.\n",
        )
        commit(self.repo, "add a new matching skill", env=self.env)

        rc2, out2, err2, bundle2 = self.write_one()
        self.assertEqual(rc2, 0, "stdout=%r stderr=%r" % (out2, err2))
        after = parse_file_list(bundle2.read_text(encoding="utf-8"))
        self.assertIn("skills/epsilon-new.md", after)
        self.assertNotEqual(before, after)

    def test_bm3_an_audience_edit_changes_the_computed_set_no_code_change(self):
        """AC-BM-3: editing an existing skill's `audience` changes the set too."""
        rc1, out1, err1, bundle1 = self.write_one()
        self.assertEqual(rc1, 0, "stdout=%r stderr=%r" % (out1, err1))
        before = parse_file_list(bundle1.read_text(encoding="utf-8"))
        self.assertNotIn("skills/beta-excluded.md", before)

        write(
            self.repo,
            "skills/beta-excluded.md",
            SKILL_BETA.replace("audience: [coder-agent]", "audience: [coder-agent, all-roles]"),
        )
        commit(self.repo, "widen beta's audience", env=self.env)

        rc2, out2, err2, bundle2 = self.write_one()
        self.assertEqual(rc2, 0, "stdout=%r stderr=%r" % (out2, err2))
        after = parse_file_list(bundle2.read_text(encoding="utf-8"))
        self.assertIn("skills/beta-excluded.md", after)


class TestOracleHelperFidelity(unittest.TestCase):
    """Sanity check on `dec140_render` itself, independent of the CLI: it must
    reproduce §7's literal, independently-verified byte-exact rendering when
    fed the same two-file input (with real git SHAs substituted for the
    spec's illustrative `abc123fullsha` / `e1e2e3f` / `a1b2c3d` placeholders,
    which are not valid git hashes and so cannot be reproduced verbatim by a
    real repo). This does not exercise `bin/bundle-methodology` and is
    expected to pass before that script exists — it is evidence the oracle
    used by `TestGoldenOracle` is itself faithful to `DEC-000140`.
    """

    def test_dec140_render_matches_spec_section_7_with_real_shas_substituted(self):
        home = make_home(self)
        repo = make_repo(self)
        env = base_env(methodology_home=home)
        write(repo, "context-sets/base.md", "file a\ncontent\n")
        write(repo, "skills/x.md", "file b content, no trailing newline")
        commit(repo, "seed section 7 fixture", env=env)

        repo_sha = head_sha(repo, env=env)
        base_blob = git(repo, "rev-parse", "--short", "HEAD:context-sets/base.md", env=env, check=True)[1].strip()
        x_blob = git(repo, "rev-parse", "--short", "HEAD:skills/x.md", env=env, check=True)[1].strip()

        actual = dec140_render(
            repo, ["context-sets/base.md", "skills/x.md"], stamp="2026-08-09-1200", env=env
        )

        expected = (
            load_spec_section_7_rendering()
            .replace("abc123fullsha", repo_sha)
            .replace("e1e2e3f", base_blob)
            .replace("a1b2c3d", x_blob)
        )
        self.assertEqual(actual, expected)


# ---------------------------------------------------------------- AC-BM-6/7


class TestShaSourcing(BundleMethodologyTestCase):
    def test_bm6_changing_one_spine_files_content_changes_only_its_sha(self):
        """AC-BM-6: every SHA is computed against `HEAD` at run time; a content
        change to one file changes only that file's blob SHA."""
        rc1, out1, err1, bundle1 = self.write_one()
        self.assertEqual(rc1, 0, "stdout=%r stderr=%r" % (out1, err1))
        before = parse_file_list(bundle1.read_text(encoding="utf-8"))

        write(self.repo, "operating-model.md", spine_content("operating-model.md") + "more.\n")
        commit(self.repo, "edit operating-model.md", env=self.env)

        rc2, out2, err2, bundle2 = self.write_one()
        self.assertEqual(rc2, 0, "stdout=%r stderr=%r" % (out2, err2))
        after = parse_file_list(bundle2.read_text(encoding="utf-8"))

        self.assertEqual(set(before.keys()), set(after.keys()))
        self.assertNotEqual(before["operating-model.md"], after["operating-model.md"])
        for path in before:
            if path == "operating-model.md":
                continue
            self.assertEqual(
                before[path], after[path], "unrelated SHA for %s changed" % path
            )

    def test_bm7_two_runs_against_the_same_head_are_byte_identical(self):
        """AC-BM-7: deterministic given HEAD and the fixture tree, modulo `Generated:`."""
        rc1, out1, err1, bundle1 = self.write_one()
        self.assertEqual(rc1, 0, "stdout=%r stderr=%r" % (out1, err1))
        rc2, out2, err2, bundle2 = self.write_one()
        self.assertEqual(rc2, 0, "stdout=%r stderr=%r" % (out2, err2))

        self.assertEqual(
            normalize_generated(bundle1.read_text(encoding="utf-8")),
            normalize_generated(bundle2.read_text(encoding="utf-8")),
        )


# ---------------------------------------------------------------- AC-BM-8


class TestNoSideEffects(BundleMethodologyTestCase):
    def test_bm8_repo_git_status_is_unchanged_by_a_run(self):
        """AC-BM-8: a run writes only the bundle file; the fixture repo's git
        status is unchanged (`--out` outside the repo)."""
        before = porcelain(self.repo, env=self.env)
        self.assertEqual(before, "", "fixture repo was not clean before the run")

        rc, out, err, bundle_path = self.write_one()
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIsNotNone(bundle_path)

        after = porcelain(self.repo, env=self.env)
        self.assertEqual(before, after)


# ---------------------------------------------------------------- AC-BM-9


class TestMissingSpinePath(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

    def run_bm(self, *args, cwd=None):
        return run_cli("bundle-methodology", *args, cwd=cwd or self.repo, env=self.env)

    def test_bm9_missing_spine_path_at_head_is_a_hard_failure(self):
        """AC-BM-9: a spine path absent at `HEAD` exits 3, naming the path."""
        missing = "roles/chief-of-staff.md"
        for path in SPINE:
            if path == missing:
                continue
            write(self.repo, path, spine_content(path))
        commit(self.repo, "seed tree missing a spine path", env=self.env)

        out_dir = temp_dir(self, "bundle-methodology-out-")
        rc, out, err = self.run_bm("--out", out_dir)

        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(missing, out + err)
        self.assertEqual(
            len(find_bundle_files(out_dir)), 0, "a partial bundle was written"
        )

    def test_bm9_uncommitted_matching_skill_at_head_is_a_hard_failure(self):
        """AC-BM-9: a `skills/*.md` path the rule selected, but that is only in
        the worktree (uncommitted add, ahead of `HEAD`), exits 3, naming it."""
        for path in SPINE:
            write(self.repo, path, spine_content(path))
        commit(self.repo, "seed full spine", env=self.env)

        uncommitted = "skills/uncommitted-match.md"
        write(
            self.repo,
            uncommitted,
            "---\n"
            "status: agreed\n"
            "last-reviewed: reviews/sample-review.md @ abc1234\n"
            "audience: [all-roles]\n"
            "superseded-by: null\n"
            "---\n"
            "\n# Uncommitted Skill\n\nSelected by the rule, absent at HEAD.\n",
        )
        # Deliberately not committed: the worktree is ahead of HEAD.

        out_dir = temp_dir(self, "bundle-methodology-out-")
        rc, out, err = self.run_bm("--out", out_dir)

        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(uncommitted, out + err)
        self.assertEqual(
            len(find_bundle_files(out_dir)), 0, "a partial bundle was written"
        )


if __name__ == "__main__":
    unittest.main()
