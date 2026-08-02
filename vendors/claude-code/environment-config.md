---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# Claude Code — Environment Configuration

The canonical `settings.json` posture for a repo where Claude Code acts as the
agent-runner.

**This document records the intended posture. It is not the posture the
committed file currently carries — see "Divergence" below.**

## The principle this implements

> Gate only on actual human judgment.

Every gate below is either a **structural** guarantee (something the agent
cannot do, whatever it decides) or a **credential** boundary (something the
agent cannot read). Neither is a prompt asking a human to approve a mechanical
step. Prompts are spent on judgment; structure carries everything else.

## Posture

### Sandbox

```json
"sandbox": { "enabled": true, "autoAllowBashIfSandboxed": true }
```

Commands run inside a filesystem and network sandbox. Because the sandbox
bounds the blast radius, bash commands inside it do not each need an approval
prompt — the structure replaces the prompt. That trade is the whole design,
and it only holds while the next line holds.

```json
"allowUnsandboxedCommands": false
```

**Strict.** No escape hatch. A configuration that auto-allows sandboxed
commands *and* permits unsandboxed ones has auto-allowed everything. This
setting is what makes `autoAllowBashIfSandboxed` safe rather than
decorative — the two must be read together, and neither should be changed
alone.

### Credential denies

Read access denied to, at minimum:

- `~/.ssh/**`
- `~/.aws/credentials`
- `.env`

Credentials are not a judgment call and are not prompt-worthy. There is no
task in scope for which an agent reading a private key is the right answer, so
the correct control is a deny, not an ask.

### Network allowlist

Outbound network access is allowlisted rather than open. The working set is
the hosts the job actually needs — package registries, the API endpoint, the
git forge, and whatever hosts the current task legitimately reaches.

An allowlist is a structural gate on exfiltration. It does not depend on the
agent behaving well.

### Push

```json
"ask": []
```

`git push` is **allowed**, not asked (Q1a/D1).

The reasoning is the gating principle applied honestly: an approval prompt on
`git push` was never a human judgment. Nobody read the diff at that prompt.
It was a reflex click, and a gate that is always approved is not a gate — it
is a tax that trains the habit of dismissing gates.

What actually protects the branch is **branch protection**: no force-push, no
deletion (`policies/project-setup-requirements.md`). That is structural, it
holds regardless of what any agent decides, and it is the gate that replaced
the prompt.

Force-push stays denied locally as well, as defense in depth:

```json
"deny": ["Bash(git push --force*)"]
```

### Notification hook

A `Notification` hook fires when the session needs attention. With mechanical
prompts removed, the remaining interrupts are the ones that carry judgment —
so they should actually reach the human rather than wait on someone watching a
terminal.

## Divergence from the committed file

As of 2026-08-02, `.claude/settings.json` at `main` carries:

```json
{ "permissions": { "defaultMode": "acceptEdits",
  "ask": ["Bash(git push *)"],
  "deny": ["Bash(git push --force*)", "Bash(rm -rf *)",
           "Read(.env)", "Read(~/.ssh/**)"] } }
```

It differs from the posture above on five points: `git push` is **asked, not
allowed**; there is no `sandbox` block; no `allowUnsandboxedCommands`; no
`~/.aws/credentials` deny; no network allowlist; no notification hook.
(`.claude/settings.local.json` — untracked, local-only — does enable the
sandbox, so an individual clone may already be closer to this posture than the
committed file is.)

**The committed file was deliberately not edited when this document was
drafted.** The directive that produced this draft directed a document, not a
configuration change, and flipping the push permission is the operative half
of a decision that has not reached `agreed` in any governed document. Aligning
the file is a separate, deliberate change.

Until then this document describes a target, and the repo does not match it.

## Scope boundary

`.claude/**` is an **adapter** — explicitly out of scope in
`policies/document-metadata-policy.md`, and subject to
`operating-model.md`'s rule that tool-specific files "should not be the sole
location of durable policy."

So: the *principle* (gate only on actual human judgment) belongs in the core
doc set and does not currently have a home there — see the W2 findings. The
*settings strings* belong here. This document is not a substitute for
canonicalizing the principle.

## Status of this draft

Drafted 2026-08-02 per the doc-review directive
(`docs/cycles/doc-review-2026-08-02-directive.md`, W3.2) executing Q1b.
Nothing here is agreed.
