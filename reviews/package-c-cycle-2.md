# Review: Package C (staged, 9 files) — cycle 2

*Authored by the Spec Reviewer agent in the gate session, 2026-08-01;
committed by the orchestrator, lightly copy-edited — all fields and all
evidence lines preserved. (Contrast cycle 1, which was heavily condensed; its
header says so.) This is the first artifact written in the review schema that
Package C introduces.*

Verdict: changes-required
Reviewed: staged index at `d778813` + 9 staged changes, including the `TREE.txt`
deletion and the `docs/packages/package-c-change-package.md` addition
Reviewer: Spec Reviewer Agent (gate review; not the drafting instance; same
instance as cycle 1)
Date: 2026-08-01
Scope: all eight cycle-1 blocking fixes checked for correctness rather than
presence; all nine non-blocking fixes checked; the four new/changed files not in
cycle 1 reviewed in full; the `TREE.txt` deletion checked for orphaned
references; `bin/bundle` exercised against the supersession condition the fix
introduced.
Cross-checked: `docs/cycles/streamlining-directive.md`,
`policies/document-metadata-policy.md`, `policies/source-of-truth-policy.md`,
`roles/spec-reviewer-agent.md`, `policies/agent-review-policy.md`,
`docs/cycles/cycle-2-directive.md`, `context-sets/*.md` frontmatter,
`bin/bundle`, `bin/check-frontmatter`.
Not inspected: `bin/aimeta/closure.py` internals (bundle was tested
behaviourally); Package A/B acceptance criteria; F6/Package D; whether the
`human-gate` degraded-mode clause works against a real GitHub outage —
untestable here, MCP GitHub is not configured in this session.
Findings: 1 blocking, 5 non-blocking, 3 observations
Prior cycle: `reviews/package-c-cycle-1.md`
Dave should inspect: B1 only. It is the one item where a cycle-1 fix made
things worse rather than better, and resolving it requires a decision (are the
bundles permanent?), not a rewording.

## B1 — blocking
Claim: The concrete `bin/bundle` supersession condition introduced to fix
cycle-1 N3 is unsatisfiable, and MANIFEST now asserts it as achievable.
Location: `MANIFEST.md` bundles section; `OPEN-ITEMS.md`, same condition
restated.
Evidence: Verified by running, bracketed on both sides. Unbounded closure from
`spec-and-change-discipline` returns **50 paths** spanning the whole repo —
`OPEN-ITEMS.md`, `MERGE-NOTES-v0.4.md`, `.claude/agents/README.md`,
`reviews/document-metadata-policy-cycle-1.md`, and `MANIFEST.md` itself; all six
context-sets. The "Spec chat" bundle is three. At `--max-depth 1` it yields two
context-sets, missing `ai-native-engineering`. No depth yields three. Root cause
verified by reading frontmatter: every context-set declares `depends-on: [base]`
and nothing else, so the graph is star-shaped and closure cannot distinguish one
bundle from another at any depth. The distinguishing information lives in the
prose `include-when:` field — curatorial judgment, not a reference.
Consequence: Three layers. (a) MANIFEST states as settled a condition the repo
cannot meet — the register defect I was asked to watch for, introduced by a fix
rather than surviving one. (b) The hold is worse than before: "trusted in
practice" was vague but honest; this is precise and false, so a future agent who
runs the check reasonably concludes `bin/bundle` is broken. (c) **The directive
is wrong here, and I am naming it rather than reinterpreting it.** The
streamlining directive defers "`bin/bundle` superseding MANIFEST bundle
definitions — after F4 lands and closure output is trusted," which assumes
reference-closure can replace curated bundles. It cannot.
Fix: Decide the substantive question first — the bundles look permanent, not
pending. Then either state that (MANIFEST holds a curated artifact no derivation
replaces; `bin/bundle` is complementary; drop the supersession framing and the
"candidate for removal" line), or restate the condition as something bundle can
actually be measured against, recording the depth and restriction. Note the
directive-level correction in the change package so F7's premise is not carried
forward silently.

## N1 — non-blocking
Claim: The `COLLAB-STATE.md` fix struck the decision but left the tree-version
declaration nine lines above it.
Location: `COLLAB-STATE.md:5`.
Evidence: Verified by reading after staging. Line 14 is correctly struck and
marked SUPERSEDED; line 5 is untouched. Cycle-1 N1 cited both.
Consequence: The file opens by declaring a tree version, then nine lines later
declares that tree versions do not exist — a smaller version of the README
defect this package exists to close, in the same file opened to close it.
Fix: Strike the version token or extend the SUPERSEDED note to cover the header.
Related: cycle-1 N1.

## N2 — non-blocking
Claim: The B8 mapping table covers the role doc's outputs but only two of
`agent-review-policy`'s seven, and creates a name collision.
Location: `skills/spec-review-cycle.md`, "What this schema governs".
Evidence: Verified by reading both. The policy requires seven outputs;
**Required follow-ups** and **Recommendation** have no row.
Consequence: `Recommendation` means the overall ship call in the policy and the
per-finding fix in the schema — one word, two things, no row saying which. The
residual of exactly the ambiguity B8 was raised to remove.
Fix: Add two rows; consider renaming the entry field to `Fix:` to kill the
homonym outright.

## N3 — non-blocking
Claim: The `TREE.txt` residual is tracked, but not under a heading anyone would
find it by.
Location: `OPEN-ITEMS.md`, nested inside the `bin/bundle` item.
Evidence: Verified by reading. `OPEN-ITEMS.md` is organised by `##` heading; a
reader or agent scanning headings for `TREE.txt` or for the agreed policy gets
nothing.
Consequence: The stated purpose was that the hold be visible from outside
MANIFEST. Nested under a heading about context-set bundles, it is visible only
to someone already reading about bundles — and if B1 resolves by deleting that
item, the note goes with it.
Fix: Promote to its own `##` item naming the agreed document and Package D.

## N4 — non-blocking
Claim: The F7 deviation is recorded twice, in a file whose thesis is that a
second copy drifts.
Location: `MANIFEST.md` parenthetical and change package §5.
Evidence: Verified by reading both. My cycle-1 B5 recommendation was to amend
the opening claim **and** record the deviation in the change package; the
executor did both plus an in-file note.
Consequence: Minor and self-aware, but it makes MANIFEST's second paragraph a
permanent footnote about a 2026 directive.
Fix: Trim the in-file note to a clause; leave the full account in §5. Separately
a reflow left a short orphan line — cosmetic.

## N5 — non-blocking
Claim: The package's own gate review is not in `reviews/`, so its central
evidence claim cannot be verified from the repo.
Location: change package §3 and §7; `reviews/` holds four files, none for
Package C.
Evidence: Verified by running `git status --short` and listing `reviews/`.
Consequence: The claim is true — I wrote cycle 1 in the schema — but nothing in
the repo evidences it. The schema landing in this very package says review
artifacts live in `reviews/`. Shipping it alongside a review that exists only in
a chat transcript is the weakest link in an otherwise well-evidenced package.
Fix: Commit both cycles. Cycle 1 predates the schema and should be committed as
written, per the schema's own no-retrofit rule.

## O1 — observation
Claim: Leaving `TREE.txt` in the agreed policy's out-of-scope list is right, and
it is inert as claimed.
Evidence: Verified by running — `check-frontmatter --all` after deletion: exit
0, 38 matched, no warning. Verified by reading `bin/tests/test_scope.py` that
the out-of-scope list is genuinely parsed from the policy, so the behaviour is
tested, not incidental.
Consequence: Endorsed without reservation. Spending a full cycle against the
only agreed document on a cosmetic mention would be the ceremony this package
exists to reduce.

## O2 — observation
Claim: Leaving the two Package A/B open items is right, but the reasoning does
not extend to leaving them factually wrong.
Evidence: Both still end "Blocked on the policy reaching `agreed`" — the policy
is agreed, the hook is live, the migration shipped.
Consequence: The scope argument covers *closing*; it does not cover a live
tracker asserting a blocker that no longer exists. A and B are finished, so
nobody will revisit — the items become permanent misinformation by default
rather than by decision.
Fix: Name both in the change package as an explicit handoff. Zero scope stretch;
`OPEN-ITEMS.md` stays untouched.

## O3 — observation
Claim: All eight blocking fixes are correct, not merely present, and three are
better than what I asked for.
Evidence: Verified by reading each against its cycle-1 finding.
Consequence: B3 ties the ask to "absence of a response is not a go" in the text
itself, which explains why the line cannot be dropped again. B4 names the change
package as interim holder, which I did not ask for and which closes the gap I
would have found next. B7's enum is right and the schema explains *why* `agreed`
is refused, making the constraint durable rather than arbitrary. The `Related:`
field earned its place immediately — N1 uses it.

## Schema feedback — second use

**Better.** The `Scope` / `Cross-checked` / `Not inspected` split fixed the
worst thing about cycle 1. `Not inspected` with "nothing is a claim, not a
default" changed my behaviour, not just my formatting — it made me state that I
could not test the GitHub degraded mode, which I would otherwise have quietly
omitted. `Dave should inspect` in the header is the highest-value amendment:
cycle 1 buried it after 250 lines; here it sits at line 12 where it will be
read.

**Worse.** The header is now 10 fields, and for a genuinely clean pass six are
`none` or boilerplate. The clean case got measurably more expensive, in tension
with "keeping the cheap case cheap." Consider marking `Cross-checked`,
`Prior cycle`, and `Related` omit-if-none.

**Ordering by weight worked but exposed a gap.** With one blocking finding it
was free. The schema still has one bucket for "the file asserts something false"
and "a sentence is imprecise". If a third user reports the same friction, a
`Severity:` qualifier inside `blocking` is worth the field.

**The no-retrofit rule immediately did real work.** It gave a clean answer for
N5: commit cycle 1 as written rather than rewriting it. Without that clause I
would have been tempted to retrofit — exactly the drift the clause names.

**The mapping table changed how I wrote.** Everything went into a field; this
artifact has no free-text section outside this block, where cycle 1 needed two.
