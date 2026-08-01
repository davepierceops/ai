"""Shared fixtures and helpers for the Package A test suite.

Design constraints (see `docs/packages/package-a-spec.md` §5):

- **No mocked git.** Every git interaction in this suite runs against a real
  repository created with `git init` in a throwaway temp directory.
- **Isolated environment.** Subprocesses never inherit the developer's
  `AI_METHODOLOGY_HOME`, global git config, or global hooks.
- **Stdlib only.**

This module is test scaffolding, not production code: it is the one place in
`bin/` that is allowed to know where the methodology repo lives, and AC-X-1's
absolute-path scan deliberately excludes `bin/tests/`.
"""

from __future__ import annotations

import atexit
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

# bin/tests/helpers.py -> bin/tests -> bin -> <repo root>. Derived, never
# hardcoded, so the suite moves with the repo.
TESTS_DIR = pathlib.Path(__file__).resolve().parent
BIN_DIR = TESTS_DIR.parent
REPO_ROOT = BIN_DIR.parent

POLICY_RELPATH = "policies/document-metadata-policy.md"
DISPOSITION_RELPATH = "reviews/frontmatter-disposition.md"

CLI_NAMES = [
    "check-frontmatter",
    "flip-agreed",
    "cycle-open",
    "bundle",
    "migrate-frontmatter",
    "install-hooks",
]

#: Minimal argv that gets each CLI past argparse, for tests that only care
#: about environmental preconditions (e.g. AC-X-4, "run outside a repo").
CLI_MINIMAL_ARGS = {
    "check-frontmatter": ["--all"],
    "flip-agreed": ["policies/x.md", "--review", "reviews/r.md @ abc1234"],
    "cycle-open": ["--cycle", "1"],
    "bundle": ["base"],
    "migrate-frontmatter": ["--plan"],
    "install-hooks": [],
}

REAL_POLICY_TEXT = (REPO_ROOT / POLICY_RELPATH).read_text()

DEFAULT_ROLE_SLUGS = (
    "coder-agent",
    "test-designer-agent",
    "reviewer-agent",
    "architect-agent",
)

_SESSION_HOME = None


# ---------------------------------------------------------------- temp dirs


def _session_home():
    """A process-wide throwaway `$HOME`, so global git config cannot leak in."""
    global _SESSION_HOME
    if _SESSION_HOME is None:
        _SESSION_HOME = tempfile.mkdtemp(prefix="aimeta-session-home-")
        atexit.register(shutil.rmtree, _SESSION_HOME, ignore_errors=True)
    return _SESSION_HOME


def temp_dir(case, prefix="aimeta-"):
    """Create a temp directory and register its removal with `case`."""
    path = pathlib.Path(tempfile.mkdtemp(prefix=prefix))
    case.addCleanup(shutil.rmtree, str(path), ignore_errors=True)
    return path


# ---------------------------------------------------------------- environment


def base_env(methodology_home=None, home=None, **overrides):
    """A subprocess environment scrubbed of anything that could skew results.

    Drops every inherited `GIT_*` var and `AI_METHODOLOGY_HOME`; pins `HOME`
    to a throwaway dir; disables system and global git config so the
    developer's `core.hooksPath` or identity cannot influence a test.
    """
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.pop("AI_METHODOLOGY_HOME", None)
    env["HOME"] = str(home or _session_home())
    env["GIT_CONFIG_NOSYSTEM"] = "1"
    env["GIT_CONFIG_GLOBAL"] = os.devnull
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["LC_ALL"] = "C"
    if methodology_home is not None:
        env["AI_METHODOLOGY_HOME"] = str(methodology_home)
    for key, value in overrides.items():
        if value is None:
            env.pop(key, None)
        else:
            env[key] = str(value)
    return env


# ---------------------------------------------------------------- git plumbing


def git(repo, *args, env=None, check=False, timeout=60):
    """Run git in `repo`. Returns `(returncode, stdout, stderr)`."""
    proc = subprocess.run(
        ["git", *[str(a) for a in args]],
        cwd=str(repo),
        env=env or base_env(),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if check and proc.returncode != 0:
        raise AssertionError(
            "git %s failed in %s: %s" % (" ".join(map(str, args)), repo, proc.stderr)
        )
    return proc.returncode, proc.stdout, proc.stderr


def make_repo(case, name="proj", parent=None, env=None):
    """A real, empty git repo on branch `main`, with a local identity.

    `parent` lets a test control the repo's *sibling* directory layout, which
    AC-RP-2's `<parent>/ai` fallback needs.
    """
    parent = pathlib.Path(parent) if parent is not None else temp_dir(case, "aimeta-work-")
    root = parent / name
    root.mkdir(parents=True, exist_ok=True)
    env = env or base_env()
    git(root, "init", "-q", "-b", "main", env=env, check=True)
    git(root, "config", "user.email", "tests@example.invalid", env=env, check=True)
    git(root, "config", "user.name", "AI Methodology Tests", env=env, check=True)
    git(root, "config", "commit.gpgsign", "false", env=env, check=True)
    return root


def write(repo, relpath, text):
    """Write `text` to `repo/relpath`, creating parent directories."""
    path = pathlib.Path(repo) / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def read(repo, relpath):
    """Read `repo/relpath` as text."""
    return (pathlib.Path(repo) / relpath).read_text()


def stage(repo, *paths, env=None):
    """`git add` the given paths (or everything when none are given)."""
    env = env or base_env()
    args = ["add", "--"] + list(paths) if paths else ["add", "-A"]
    git(repo, *args, env=env, check=True)


def commit(repo, message, *paths, env=None):
    """Stage `paths` (or everything) and commit. Returns the full SHA."""
    env = env or base_env()
    stage(repo, *paths, env=env)
    git(repo, "commit", "-q", "--no-verify", "-m", message, env=env, check=True)
    return git(repo, "rev-parse", "HEAD", env=env, check=True)[1].strip()


def head_sha(repo, env=None):
    return git(repo, "rev-parse", "HEAD", env=env or base_env(), check=True)[1].strip()


def show(repo, rev_and_path, env=None):
    """`git show <rev>:<path>` — e.g. `show(r, ":policies/x.md")` for the index."""
    rc, out, err = git(repo, "show", rev_and_path, env=env or base_env())
    if rc != 0:
        raise AssertionError("git show %s failed: %s" % (rev_and_path, err))
    return out


def commit_paths(repo, rev="HEAD", env=None):
    """Sorted list of paths touched by a commit."""
    rc, out, err = git(
        repo,
        "show",
        "--pretty=format:",
        "--name-only",
        rev,
        env=env or base_env(),
        check=True,
    )
    return sorted(p for p in out.splitlines() if p.strip())


def commit_count(repo, env=None):
    rc, out, _ = git(repo, "rev-list", "--count", "HEAD", env=env or base_env())
    return int(out.strip()) if rc == 0 else 0


def porcelain(repo, env=None):
    return git(repo, "status", "--porcelain", env=env or base_env(), check=True)[1]


# ---------------------------------------------------------------- methodology home


def make_home(case, policy_text=None, roles=DEFAULT_ROLE_SLUGS, parent=None, name="ai"):
    """A temp methodology home: a policy, roles, and a `bin/` symlink.

    `bin/` is a **symlink to the real `bin/`**, so the scripts exercised are
    the ones under test, while `policies/document-metadata-policy.md` is a
    copy this test can vary (AC-CF-13).
    """
    parent = pathlib.Path(parent) if parent is not None else temp_dir(case, "aimeta-home-")
    home = parent / name
    home.mkdir(parents=True, exist_ok=True)
    write(home, POLICY_RELPATH, REAL_POLICY_TEXT if policy_text is None else policy_text)
    for slug in roles:
        write(home, "roles/%s.md" % slug, role_doc(slug))
    link = home / "bin"
    if not link.exists():
        link.symlink_to(BIN_DIR, target_is_directory=True)
    return home


def policy_without(marker_glob, policy_text=None):
    """The real policy text with one in-scope bullet removed (AC-CF-13)."""
    text = REAL_POLICY_TEXT if policy_text is None else policy_text
    return "\n".join(
        line for line in text.splitlines() if line.strip() != "- `%s`" % marker_glob
    ) + "\n"


# ---------------------------------------------------------------- CLI invocation


def run_cli(name, *args, cwd, env=None, methodology_home=None, timeout=90, script_dir=None):
    """Invoke `bin/<name>` as a subprocess through its own shebang.

    CLI behaviour is tested across the process boundary because exit codes are
    part of the contract (spec §2.4).
    """
    script = pathlib.Path(script_dir or BIN_DIR) / name
    proc = subprocess.run(
        [str(script), *[str(a) for a in args]],
        cwd=str(cwd),
        env=env if env is not None else base_env(methodology_home=methodology_home),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return proc.returncode, proc.stdout, proc.stderr


# ---------------------------------------------------------------- assertions


BRACKET_CODE_RE = re.compile(r"\[([a-z][a-z0-9-]*)\]")


def bracket_codes(text):
    """Every bracketed `[code]` in a diagnostic stream.

    Tests assert on codes, never on English wording, so that rewording a
    message does not break the suite.
    """
    return BRACKET_CODE_RE.findall(text or "")


def codes(findings):
    """Codes of a `list[Finding]`, in order."""
    return [f.code for f in findings]


def code_set(findings):
    return set(codes(findings))


def no_traceback(*streams):
    return not any("Traceback (most recent call last)" in (s or "") for s in streams)


def snapshot_tree(root, skip=()):
    """`{relpath: (size, mtime_ns, sha-ish content)}` for a directory tree."""
    root = pathlib.Path(root)
    skip = [pathlib.Path(s).resolve() for s in skip]
    out = {}
    for path in sorted(root.rglob("*")):
        try:
            resolved = path.resolve()
        except OSError:
            continue
        if any(resolved == s or s in resolved.parents for s in skip):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        st = path.stat()
        out[str(path.relative_to(root))] = (st.st_size, st.st_mtime_ns)
    return out


# ---------------------------------------------------------------- doc fixtures


def frontmatter_block(**fields):
    lines = ["---"]
    for key, value in fields.items():
        key = key.replace("_", "-")
        if value is None:
            lines.append("%s: null" % key)
        elif isinstance(value, (list, tuple)):
            lines.append("%s: [%s]" % (key, ", ".join(str(v) for v in value)))
        else:
            lines.append("%s: %s" % (key, value))
    lines.append("---")
    return "\n".join(lines) + "\n"


DEFAULT_BODY = "\n# Sample Document\n\nOriginal body text.\n"
REVIEW_POINTER = "reviews/sample-review.md @ abc1234"


def agreed_doc(body=DEFAULT_BODY, review=REVIEW_POINTER, audience=("all-roles",)):
    """A fully valid `agreed` document (AC-FM-16's shape)."""
    return (
        frontmatter_block(
            status="agreed",
            last_reviewed=review,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def draft_doc(body=DEFAULT_BODY, audience=("all-roles",)):
    return (
        frontmatter_block(
            status="draft",
            last_reviewed=None,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def in_review_doc(body=DEFAULT_BODY, audience=("all-roles",)):
    return (
        frontmatter_block(
            status="in-review",
            last_reviewed=None,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def legacy_doc(title="Legacy Document", status_word="stable", body_extra=""):
    """A pre-frontmatter document carrying a body `Status:` line."""
    return "# %s\n\nStatus: %s\n\nSome legacy prose.\n%s" % (title, status_word, body_extra)


def context_set_doc(name, depends_on=(), body=None, status_word=None):
    """A context set carrying composition frontmatter and no lifecycle fields."""
    head = frontmatter_block(
        context_set=name,
        purpose="Purpose of %s." % name,
        include_when="When %s applies." % name,
        depends_on=list(depends_on),
    )
    if body is None:
        body = "\n# Context Set: %s\n\nProse.\n" % name
    if status_word:
        body = "\n# Context Set: %s\n\nStatus: %s\n\nProse.\n" % (name, status_word)
    return head + body


def role_doc(slug):
    return agreed_doc(body="\n# Role: %s\n\nRole prose.\n" % slug)


def disposition_doc(paths):
    lines = ["# Frontmatter grandfather disposition", ""]
    lines += ["- `%s` — agreed before policy adoption" % p for p in paths]
    return "\n".join(lines) + "\n"


def plan_block(path, action="migrate", **fields):
    """One `migrate-frontmatter --plan` block (spec §3.8 format)."""
    lines = ["## `%s`" % path, "- action: %s" % action]
    for key, value in fields.items():
        lines.append("- %s: %s" % (key.replace("_", "-"), value))
    return "\n".join(lines) + "\n"
