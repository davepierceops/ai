"""AC-MG-*: `bin/migrate-frontmatter` — the F2 legacy-header transform.

Contract: `docs/packages/package-a-spec.md` §3.8. Package A only builds and
tests this; Package B runs it. The transform is mechanical and
status-preserving by design: every judgment field stays `TODO`.
"""

from __future__ import annotations

import re
import unittest

from tests.helpers import (
    agreed_doc,
    base_env,
    commit,
    context_set_doc,
    git,
    head_sha,
    legacy_doc,
    make_home,
    make_repo,
    plan_block,
    read,
    run_cli,
    write,
)

LEGACY_STABLE = "policies/legacy-stable.md"
LEGACY_DRAFT = "policies/legacy-draft.md"
LEGACY_IN_REVIEW = "policies/legacy-in-review.md"
NO_STATUS = "policies/no-status.md"
COMPOSED = "context-sets/composed.md"
ALREADY_VALID = "policies/already-valid.md"

LEGACY_STABLE_TEXT = (
    "# Legacy Stable\n"
    "\n"
    "Status: stable\n"
    "\n"
    "Prose paragraph one.\n"
    "\n"
    "Prose paragraph two.\n"
)


def body_after_status_removal(original):
    """The body the transform should leave: the `Status:` line gone, one
    doubled blank line collapsed, everything else byte-identical."""
    lines = original.splitlines(keepends=True)
    idx = next(i for i, line in enumerate(lines) if line.startswith("Status:"))
    del lines[idx]
    if (
        0 < idx < len(lines)
        and lines[idx].strip() == ""
        and lines[idx - 1].strip() == ""
    ):
        del lines[idx]
    return "".join(lines)


def split_frontmatter(text):
    """(frontmatter_block, body) for a rendered document."""
    if not text.startswith("---\n"):
        return "", text
    rest = text[4:]
    head, _, body = rest.partition("\n---\n")
    return head, body


class MigrateTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        write(self.repo, LEGACY_STABLE, LEGACY_STABLE_TEXT)
        write(self.repo, LEGACY_DRAFT, legacy_doc("Legacy Draft", "draft"))
        write(self.repo, LEGACY_IN_REVIEW, legacy_doc("Legacy In Review", "in-review"))
        write(self.repo, NO_STATUS, "# No Status Line\n\nJust prose.\n")
        write(self.repo, COMPOSED, context_set_doc("composed", status_word="stable"))
        write(self.repo, ALREADY_VALID, agreed_doc())
        write(self.repo, "docs/notes.md", "# Out of scope\n\nStatus: whatever\n")
        commit(self.repo, "seed legacy docs", env=self.env)

        self.doc_paths = [
            LEGACY_STABLE,
            LEGACY_DRAFT,
            LEGACY_IN_REVIEW,
            NO_STATUS,
            COMPOSED,
            ALREADY_VALID,
            "docs/notes.md",
        ]

    def migrate(self, *args):
        return run_cli("migrate-frontmatter", *args, cwd=self.repo, env=self.env)

    def plan_text(self):
        rc, out, err = self.migrate("--plan")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        return out

    def block_for(self, plan, path):
        blocks = re.split(r"(?m)^## ", plan)
        for block in blocks:
            if block.startswith("`%s`" % path):
                return block
        raise AssertionError("no plan block for %s in:\n%s" % (path, plan))

    def doc_snapshot(self):
        return {p: read(self.repo, p) for p in self.doc_paths}

    def write_plan(self, relpath, *blocks):
        write(self.repo, relpath, "\n".join(blocks))
        return relpath


class TestPlan(MigrateTestCase):
    def test_mg1_one_block_per_in_scope_document_in_sorted_path_order(self):
        """AC-MG-1: `--plan` emits a backticked H2 per in-scope `.md`, sorted."""
        plan = self.plan_text()
        headings = re.findall(r"(?m)^## `(.+?)`\s*$", plan)
        expected = sorted(
            [LEGACY_STABLE, LEGACY_DRAFT, LEGACY_IN_REVIEW, NO_STATUS, COMPOSED, ALREADY_VALID]
        )
        self.assertEqual(headings, expected)

    def test_mg1_out_of_scope_documents_are_not_planned(self):
        """AC-MG-1: only the in-scope set appears in the plan."""
        plan = self.plan_text()
        self.assertIn("## `%s`" % LEGACY_STABLE, plan)
        self.assertNotIn("docs/notes.md", plan)

    def test_mg1_out_flag_writes_the_plan_to_a_file(self):
        """AC-MG-1: `--out FILE` redirects the plan; stdout stays clean."""
        rc, out, err = self.migrate("--plan", "--out", "migration-plan.md")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(
            (self.repo / "migration-plan.md").is_file(), "no plan file written"
        )
        written = read(self.repo, "migration-plan.md")
        self.assertIn("## `%s`" % LEGACY_STABLE, written)

    def test_mg2_legacy_status_line_records_number_and_verbatim_text(self):
        """AC-MG-2: the 1-based line number and the verbatim line are recorded."""
        plan = self.plan_text()
        block = self.block_for(plan, LEGACY_STABLE)
        self.assertRegex(block, r"legacy-status-line:\s*3\s+`Status: stable`")

    def test_mg2_detects_the_status_line_below_existing_frontmatter(self):
        """AC-MG-2: detection is over the body, after the H1, not the raw file top."""
        plan = self.plan_text()
        block = self.block_for(plan, COMPOSED)
        self.assertRegex(block, r"legacy-status-line:\s*10\s+`Status: stable`")

    def test_mg2_a_status_line_far_below_the_h1_is_not_detected(self):
        """AC-MG-2: the search window is the first 20 lines after the H1."""
        filler = "\n".join("Paragraph %d." % i for i in range(30))
        write(
            self.repo,
            "policies/far-status.md",
            "# Far Status\n\n%s\n\nStatus: stable\n" % filler,
        )
        commit(self.repo, "add far status doc", env=self.env)

        block = self.block_for(self.plan_text(), "policies/far-status.md")
        self.assertNotIn("`Status: stable`", block)

    def test_mg3_status_mapping_is_preserving_where_the_policy_defines_it(self):
        """AC-MG-3: `draft` -> `draft` and `in-review` -> `in-review`."""
        plan = self.plan_text()
        self.assertRegex(self.block_for(plan, LEGACY_DRAFT), r"(?m)^- status: draft\s*$")
        self.assertRegex(
            self.block_for(plan, LEGACY_IN_REVIEW), r"(?m)^- status: in-review\s*$"
        )

    def test_mg3_unmapped_legacy_values_become_todo_with_a_reason(self):
        """AC-MG-3: `stable` has no policy mapping, so it becomes TODO."""
        block = self.block_for(self.plan_text(), LEGACY_STABLE)
        self.assertRegex(block, r"(?m)^- status: TODO\b")
        self.assertIn("stable", block)

    def test_mg3_absent_legacy_status_becomes_todo(self):
        """AC-MG-3: no legacy line at all is still a TODO, never a guess."""
        block = self.block_for(self.plan_text(), NO_STATUS)
        self.assertRegex(block, r"(?m)^- status: TODO\b")

    def test_mg3_never_guesses_agreed(self):
        """AC-MG-3: the transform never proposes `agreed` for a legacy document."""
        plan = self.plan_text()
        for path in [LEGACY_STABLE, LEGACY_DRAFT, LEGACY_IN_REVIEW, NO_STATUS, COMPOSED]:
            block = self.block_for(plan, path)
            self.assertNotRegex(
                block, r"(?m)^- status: agreed\s*$", "%s was guessed as agreed" % path
            )

    def test_mg4_audience_is_always_todo(self):
        """AC-MG-4: `audience` is the judgment field and is never inferred."""
        plan = self.plan_text()
        for path in [LEGACY_STABLE, LEGACY_DRAFT, LEGACY_IN_REVIEW, NO_STATUS, COMPOSED]:
            block = self.block_for(plan, path)
            self.assertRegex(
                block, r"(?m)^- audience: TODO\s*$", "%s: %r" % (path, block)
            )

    def test_mg5_complete_documents_are_skipped_with_no_todos(self):
        """AC-MG-5: an already-valid document plans as `action: skip`."""
        block = self.block_for(self.plan_text(), ALREADY_VALID)
        self.assertRegex(block, r"(?m)^- action: skip\s*$")
        self.assertNotIn("TODO", block)

    def test_mg6_plan_writes_no_changes_to_any_document(self):
        """AC-MG-6: `--plan` is read-only over the document set."""
        before = self.doc_snapshot()
        rc, out, err = self.migrate("--plan")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        # Precondition: a plan that was never produced trivially writes nothing.
        self.assertIn("## `%s`" % LEGACY_STABLE, out)
        self.assertEqual(self.doc_snapshot(), before)


class TestApplyGuards(MigrateTestCase):
    def test_mg7_refuses_a_plan_with_unresolved_todos(self):
        """AC-MG-7: `--apply` refuses (exit 3) and names every undecided path."""
        plan = self.write_plan(
            "plan.md",
            plan_block(
                LEGACY_STABLE, status="TODO", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(
                LEGACY_DRAFT, status="draft", last_reviewed="null",
                audience="TODO", grandfather="no",
            ),
            plan_block(
                NO_STATUS, status="draft", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
        )
        before = self.doc_snapshot()

        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(LEGACY_STABLE, out + err)
        self.assertIn(LEGACY_DRAFT, out + err)
        self.assertNotIn(NO_STATUS, out + err)
        self.assertEqual(self.doc_snapshot(), before)

    def test_mg8_apply_is_all_or_nothing(self):
        """AC-MG-8: one invalid result means nothing at all is written (exit 1)."""
        plan = self.write_plan(
            "plan.md",
            plan_block(
                LEGACY_STABLE, status="draft", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(
                LEGACY_DRAFT, status="draft", last_reviewed="null",
                audience="[not-a-real-role]", grandfather="no",
            ),
        )
        before = self.doc_snapshot()

        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(LEGACY_DRAFT, out + err)
        self.assertEqual(
            self.doc_snapshot(), before, "a partial write escaped the all-or-nothing rule"
        )


class TestApplyTransform(MigrateTestCase):
    def valid_plan(self, *paths):
        blocks = []
        for path in paths:
            blocks.append(
                plan_block(
                    path,
                    status="draft",
                    last_reviewed="null",
                    audience="[all-roles]",
                    grandfather="no",
                )
            )
        return self.write_plan("plan.md", *blocks)

    def test_mg9_inserts_frontmatter_and_deletes_the_legacy_line(self):
        """AC-MG-9: a document with no frontmatter gains a block and loses `Status:`."""
        plan = self.valid_plan(LEGACY_STABLE)
        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

        text = read(self.repo, LEGACY_STABLE)
        self.assertTrue(text.startswith("---\n"), "frontmatter not at the very top")
        head, body = split_frontmatter(text)
        self.assertIn("status: draft", head)
        self.assertIn("audience: [all-roles]", head)
        self.assertNotIn("Status: stable", text)

    def test_mg9_remaining_body_is_byte_identical_apart_from_the_deletion(self):
        """AC-MG-9: only the `Status:` line and one doubled blank line disappear."""
        plan = self.valid_plan(LEGACY_STABLE)
        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

        _, body = split_frontmatter(read(self.repo, LEGACY_STABLE))
        self.assertEqual(
            body.lstrip("\n"), body_after_status_removal(LEGACY_STABLE_TEXT)
        )

    def test_mg10_merges_into_existing_frontmatter_preserving_its_keys(self):
        """AC-MG-10: composition fields survive; lifecycle fields are merged in."""
        plan = self.valid_plan(COMPOSED)
        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

        text = read(self.repo, COMPOSED)
        head, body = split_frontmatter(text)
        self.assertIn("context-set: composed", head)
        self.assertIn("purpose: Purpose of composed.", head)
        self.assertIn("include-when: When composed applies.", head)
        self.assertIn("depends-on: []", head)
        self.assertIn("status: draft", head)
        self.assertIn("last-reviewed: null", head)
        self.assertNotIn("Status: stable", body)

    def test_mg10_does_not_produce_a_second_frontmatter_block(self):
        """AC-MG-10: the merge is into the existing block, not a new one."""
        plan = self.valid_plan(COMPOSED)
        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        text = read(self.repo, COMPOSED)
        self.assertIn("status: draft", text)
        self.assertEqual(text.count("\n---\n"), 1, "two frontmatter blocks: %r" % text[:300])

    def test_mg11_dry_run_prints_a_diff_and_writes_nothing(self):
        """AC-MG-11: `--apply --dry-run` is a preview only."""
        plan = self.valid_plan(LEGACY_STABLE, COMPOSED)
        before = self.doc_snapshot()

        rc, out, err = self.migrate("--apply", plan, "--dry-run")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("@@", out)
        self.assertIn("-Status: stable", out)
        self.assertIn(LEGACY_STABLE, out)
        self.assertIn(COMPOSED, out)
        self.assertEqual(self.doc_snapshot(), before)

    def test_mg12_apply_never_stages_or_commits(self):
        """AC-MG-12: the transform leaves the change in the worktree for review."""
        plan = self.valid_plan(LEGACY_STABLE)
        before_head = head_sha(self.repo, env=self.env)

        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(head_sha(self.repo, env=self.env), before_head)
        staged = git(
            self.repo, "diff", "--cached", "--name-only", env=self.env, check=True
        )[1]
        self.assertEqual(staged.strip(), "")
        unstaged = git(
            self.repo, "diff", "--name-only", env=self.env, check=True
        )[1]
        self.assertIn(LEGACY_STABLE, unstaged)

    def test_mg13_migrated_set_passes_check_frontmatter(self):
        """AC-MG-13: after `--apply`, `check-frontmatter --all` is clean."""
        plan = self.write_plan(
            "plan.md",
            plan_block(
                LEGACY_STABLE, status="draft", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(
                LEGACY_DRAFT, status="draft", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(
                LEGACY_IN_REVIEW, status="in-review", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(
                NO_STATUS, status="draft", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(
                COMPOSED, status="draft", last_reviewed="null",
                audience="[all-roles]", grandfather="no",
            ),
            plan_block(ALREADY_VALID, action="skip"),
        )

        rc, out, err = self.migrate("--apply", plan)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        # Precondition: the documents must actually have been migrated, or a
        # clean check-frontmatter run says nothing about the transform.
        for path in [LEGACY_STABLE, LEGACY_DRAFT, LEGACY_IN_REVIEW, NO_STATUS]:
            self.assertTrue(
                read(self.repo, path).startswith("---\n"),
                "%s was not migrated" % path,
            )

        check_rc, check_out, check_err = run_cli(
            "check-frontmatter", "--all", cwd=self.repo, env=self.env
        )
        self.assertEqual(
            check_rc, 0, "migrated set still has findings: %r" % (check_err or check_out)
        )


class TestUsage(MigrateTestCase):
    def test_mg1_requires_exactly_one_mode(self):
        """AC-MG-1: neither or both of `--plan`/`--apply` is a usage error (2)."""
        rc, out, err = self.migrate()
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))


if __name__ == "__main__":
    unittest.main()
