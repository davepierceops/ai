# Review: policies/remote-write-verification-policy.md — cycle 3

Verdict: ready-with-findings
Reviewed: `policies/remote-write-verification-policy.md` @ `582fb6f`
Reviewer: self-review (autonomous, this directive)
Date: 2026-08-09
Scope: the new Rule 4, the two revised Scope paragraphs, the rewritten
Relationship to existing rules, and the Status of this draft note. Checked
against `docs/cycles/friction-refactor-2026-08-09-directive.md` D1.2 and D1.3,
and against `decisions/log.md` `DEC-000080`, whose keep-reason Rule 4 must
preserve.
Cross-checked: `skills/directive-dispatch.md` (Purpose; §3 Track; Executor
obligations), `skills/spec-review-cycle.md` (Hard constraints),
`decisions/log.md` `DEC-000080`, `DEC-000130`, `OPEN-ITEMS.md` ("Promote the
write-verification principle into `context-sets/base.md`"; "MCP write
verification must cover content").
Not inspected: Rules 1–3 and the Known gap section, unchanged this cycle;
whether Rule 4's counting rules behave correctly under a real contention event —
no failure was reproduced, and the rules are carried over verbatim from the text
that survived cycles 1–3 of `skills/directive-dispatch.md`.
Findings: 1 non-blocking
Prior cycle: `reviews/remote-write-verification-policy-cycle-2.md`

## N1 — non-blocking
Claim: Rule 4 is a detection rule in a policy whose title, purpose, and three
other rules are about *verification*, and it is the only rule that prescribes no
verification.
Location: `policies/remote-write-verification-policy.md`, "### 4. Two
consecutive qualifying failures is a fact about the environment"
Evidence: Verified by reading the document against its own framing at `582fb6f`.
"The failure mode" section defines the policy's subject as a write that succeeds
on the server and fails to report success; Rules 1–3 each say what to read back.
Rule 4 says to stop counting and start diagnosing, which is a different verb.
Consequence: A reader looking for the detector will not think to look here, which
is the discoverability problem `OPEN-ITEMS.md` records for skills without a
`description`. Against that: the rule's qualifying list is entirely
transport-failure conditions, which is exactly this document's subject matter,
and the alternatives considered were worse — `skills/directive-dispatch.md` no
longer has a mediated transport in its path at all, and `context-sets/base.md` is
pre-empted by an open item.
Fix: None taken. If the placement proves wrong in use, the rule moves as a unit —
it has no dependencies on Rules 1–3 beyond the Rule 2 cross-reference. The
judgment call and its alternatives are recorded at
`docs/cycles/friction-refactor-2026-08-09-decisions.md` D2 for Dave to overturn.
