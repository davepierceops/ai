"""AC-EL-*: the cited SHA must appear in an entry in the expedited log.

Contract: `OPEN-ITEMS.md`, "The expedited path's log entry is unenforced —
`flip-agreed` checks existence, not content". Those ACs are the spec; the
`AC-EL-` prefix is local to this suite because the work is dispatched from the
tracker entry rather than from `docs/packages/package-a-spec.md`.

- **AC-EL-1** `flip-agreed --review` resolves the cited SHA against the target
  artifact's *contents* when that artifact is the expedited log, and fails
  closed when the SHA is absent.
- **AC-EL-2** Abbreviation is normalized through `git rev-parse` before
  comparison: an abbreviated pointer against a full-length entry is the same
  SHA and a different string, and either side may be the abbreviated one.
- **AC-EL-3** A non-log artifact keeps today's existence-only behaviour.
- **AC-EL-4** `check-frontmatter` reports the same condition over the whole
  in-scope set.

Real git throughout, per the suite's standing constraint: the rule is about
whether a SHA *resolves*, which a mocked git cannot answer.
"""

from __future__ import annotations

import unittest

from tests.helpers import (
    agreed_doc,
    base_env,
    bracket_codes,
    commit,
    commit_count,
    in_review_doc,
    make_home,
    make_repo,
    no_traceback,
    run_cli,
    write,
)

TARGET = "policies/sample-policy.md"
LOG = "reviews/expedited-log.md"
OTHER_REVIEW = "reviews/sample-review.md"
BODY = "\n# Sample Policy\n\nThe body that must not change.\n"

LOG_HEADER = (
    "# Expedited Review Log\n"
    "\n"
    "One line per expedited agreement. Format:\n"
    "\n"
    "`- <YYYY-MM-DD> — <document path> @ <sha> — <what changed>`\n"
    "\n"
    "## Entries\n"
    "\n"
)

EMPTY_LOG = LOG_HEADER + "<!-- none yet; the first expedited agreement appends here -->\n"


def log_with(*shas):
    """The log with one well-formed entry per SHA."""
    entries = "".join(
        "- 2026-08-02 — %s @ %s — one clause about what changed\n" % (TARGET, sha)
        for sha in shas
    )
    return LOG_HEADER + entries


class ExpeditedLogTestCase(unittest.TestCase):
    """Shared fixture: a repo with two commits, so two real SHAs exist."""

    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        write(self.repo, TARGET, in_review_doc(body=BODY))
        write(self.repo, LOG, EMPTY_LOG)
        write(self.repo, OTHER_REVIEW, "# Review of the sample policy\n\nFindings: none.\n")
        self.reviewed_sha = commit(self.repo, "seed", env=self.env)

        write(self.repo, "notes.md", "An unrelated commit, to give the repo a second SHA.\n")
        self.other_sha = commit(self.repo, "unrelated", env=self.env)

    # ------------------------------------------------------------- helpers

    def set_log(self, text):
        write(self.repo, LOG, text)
        return commit(self.repo, "log", env=self.env)

    def flip(self, *args):
        return run_cli("flip-agreed", *args, cwd=self.repo, env=self.env)

    def flip_with(self, pointer):
        return self.flip(TARGET, "--review", pointer)

    def check(self, *args):
        return run_cli("check-frontmatter", *args, cwd=self.repo, env=self.env)

    def set_agreed_pointer(self, pointer):
        """Put the target document at `agreed` with `pointer`, without the tool."""
        write(self.repo, TARGET, agreed_doc(body=BODY, review=pointer))
        return commit(self.repo, "hand-written agreement", env=self.env)


class FlipAgreedLogCheckTests(ExpeditedLogTestCase):
    """AC-EL-1 / AC-EL-2 / AC-EL-3 at the flip."""

    def test_refuses_a_pointer_the_log_does_not_name(self):
        """AC-EL-1: the exact sequence from the tracker entry — step 3 skipped."""
        before = commit_count(self.repo, env=self.env)
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha))
        self.assertEqual(code, 1, err)
        self.assertEqual(commit_count(self.repo, env=self.env), before)
        self.assertTrue(no_traceback(out, err))

    def test_accepts_a_pointer_the_log_names(self):
        """AC-EL-1: the same flip succeeds once the entry exists."""
        self.set_log(log_with(self.reviewed_sha))
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha))
        self.assertEqual(code, 0, err)

    def test_an_entry_for_another_commit_does_not_satisfy_the_pointer(self):
        """AC-EL-1: the *cited* SHA has to be there, not merely some SHA."""
        self.set_log(log_with(self.other_sha))
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha))
        self.assertEqual(code, 1, err)
        self.assertTrue(no_traceback(out, err))

    def test_abbreviated_pointer_matches_a_full_length_entry(self):
        """AC-EL-2: same SHA, different string — normalize, do not string-compare."""
        self.set_log(log_with(self.reviewed_sha))
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha[:7]))
        self.assertEqual(code, 0, err)

    def test_full_pointer_matches_an_abbreviated_entry(self):
        """AC-EL-2: normalization has to run on both sides, not just the pointer."""
        self.set_log(log_with(self.reviewed_sha[:8]))
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha))
        self.assertEqual(code, 0, err)

    def test_a_missing_log_still_fails_closed(self):
        """AC-EL-1: the artifact-existence check keeps its precedence."""
        (self.repo / LOG).unlink()
        commit(self.repo, "remove the log", env=self.env)
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha))
        self.assertEqual(code, 1, err)
        self.assertTrue(no_traceback(out, err))

    def test_a_non_log_artifact_keeps_existence_only_behaviour(self):
        """AC-EL-3: `reviews/sample-review.md` names no SHA and is still accepted."""
        code, out, err = self.flip_with("%s @ %s" % (OTHER_REVIEW, self.reviewed_sha))
        self.assertEqual(code, 0, err)

    def test_prose_mentioning_the_sha_outside_an_entry_does_not_count(self):
        """AC-EL-1: an entry is a log entry, not any occurrence of the string."""
        self.set_log(
            LOG_HEADER
            + "Once %s is agreed this section will hold its entry.\n" % self.reviewed_sha
        )
        code, out, err = self.flip_with("%s @ %s" % (LOG, self.reviewed_sha))
        self.assertEqual(code, 1, err)
        self.assertTrue(no_traceback(out, err))


class CheckFrontmatterLogCheckTests(ExpeditedLogTestCase):
    """AC-EL-4: the same condition, over the in-scope set rather than at the flip."""

    def test_all_reports_a_pointer_the_log_does_not_name(self):
        self.set_agreed_pointer("%s @ %s" % (LOG, self.reviewed_sha))
        code, out, err = self.check("--all")
        self.assertEqual(code, 1, err)
        self.assertIn("expedited-sha-not-in-log", bracket_codes(err))
        self.assertTrue(no_traceback(out, err))

    def test_all_passes_once_the_log_names_the_sha(self):
        self.set_agreed_pointer("%s @ %s" % (LOG, self.reviewed_sha))
        self.set_log(log_with(self.reviewed_sha))
        code, out, err = self.check("--all")
        self.assertEqual(code, 0, err)

    def test_all_normalizes_abbreviation_before_comparing(self):
        self.set_agreed_pointer("%s @ %s" % (LOG, self.reviewed_sha[:7]))
        self.set_log(log_with(self.reviewed_sha))
        code, out, err = self.check("--all")
        self.assertEqual(code, 0, err)

    def test_path_mode_reports_it_too(self):
        self.set_agreed_pointer("%s @ %s" % (LOG, self.reviewed_sha))
        code, out, err = self.check(TARGET)
        self.assertEqual(code, 1, err)
        self.assertIn("expedited-sha-not-in-log", bracket_codes(err))

    def test_a_non_log_pointer_is_left_alone(self):
        """AC-EL-3's other half: nothing new is asserted about other artifacts."""
        self.set_agreed_pointer("%s @ %s" % (OTHER_REVIEW, self.reviewed_sha))
        code, out, err = self.check("--all")
        self.assertEqual(code, 0, err)

    def test_a_pointer_citing_an_unresolvable_sha_fails_closed(self):
        """A SHA git cannot resolve cannot be shown to be in the log."""
        self.set_agreed_pointer("%s @ %s" % (LOG, "0" * 40))
        self.set_log(log_with(self.reviewed_sha))
        code, out, err = self.check("--all")
        self.assertEqual(code, 1, err)
        self.assertTrue(no_traceback(out, err))

    def test_a_null_pointer_is_unaffected(self):
        """Only a pointer at the log is in question; the fixture doc has none."""
        code, out, err = self.check("--all")
        self.assertEqual(code, 0, err)


if __name__ == "__main__":
    unittest.main()
