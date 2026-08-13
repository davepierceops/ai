---
status: draft
audience: [editor, section-writer, human]
purpose: Criteria for Dave's public-facing published prose. The governing instrument for the Editor role and the instruction set every section-writing session receives.
---

# Public Prose Criteria

## Scope

Public-facing prose published on the open internet under Dave's byline —
articles, blog posts, and similar. Nothing else: methodology documents,
operator-facing reports, and internal writing are governed elsewhere or not
yet at all.

## Trust model — every word is reviewed

Dave's engineering methodology (`davepierceops/ai`) deliberately removes
human line-by-line review of agent output; this work inverts that. Dave
reviews every word before publication. Agents draft under direction; nothing
publishes on agent judgment. The human gate is not the release decision — it
is every sentence.

## Purpose and audience

Readers: adopters, peers, potential clients. Goal now: establish thought
leadership. Goal later: drive adoption, expected to become primary when the
SRE-focused methodology work is public. Revisit the register when that shift
happens.

## Voice and register

- Dave's voice, singular. Not a house style, not a persona — the test is
  "reads as Dave."
- Baseline: dry, technical, wry.
- More expansive and explanatory than the methodology register — public prose
  walks the reader through reasoning the repo docs compress away.
- Persuasive, flowery, or poetic passages are permitted as occasional
  flourish, never as the constant mode.

## Claims taxonomy

Every claim in a piece belongs to one of four tiers, and the writing makes the
tier legible to the reader:

1. **Relayed** — someone else's claim, passed along. Attributed as such.
2. **Demonstrated** — Dave's evidence constitutes proof: hypothesis, test,
   result. The piece can show the work.
3. **Inferred** — grounded in experience, observation, or data below the bar
   for proof. Marked as inference.
4. **Opinion** — flagged clearest of all.

This is the public-facing translation of the evidence vocabulary in
`davepierceops/ai` (`context-sets/base.md`). Tier-blurring — an opinion
dressed as an inference, an inference dressed as proof — is a defect.

## Terminology

- Define and use the methodology's own terms (the governed vocabulary in
  `davepierceops/ai`, `LEXICON.md`); build the public vocabulary
  deliberately.
- When an industry-standard term exists for a concept the methodology names
  differently, flag the mismatch and decide — the resolution may flow back
  into `LEXICON.md`.

## Profanity

Rare, and each use earns its place. Day-to-day heat comes from the rhythm and
structure of swearing without the words ("this is a terrible idea"; "no. no no
no."). The justification-ledger pass in the Editor workflow (`roles/editor.md`)
enforces this mechanically: every profanity ships with its stated reason,
reviewed by Dave before publication.

## Naming

Anonymize by default, in both directions — criticized practices are named,
companies/products/people are not; praise is likewise sparing with names.
Name only when there is a clear, articulable benefit in that instance, and
state the benefit when proposing it.

**Exception — attribution is mandatory.** When the author of a piece of work
(an idea, a technique, a phrase, a finding) is known, credit them. Always,
unless the work is literally trivial. Anonymize-by-default governs targets
and examples; it never licenses taking credit by omission.

## Structure

- Length and structure are per-piece decisions, not criteria — revisit only
  if problems recur.
- Standing convention: summary sections are labeled **TL;DR**.

## Continuity

Build across pieces is allowed, but every piece lands clean for a cold
reader. No piece reads as unannounced episode four. Exception: an explicitly
declared series ("part 2 of N," stated upfront) may assume its predecessors.

## Discoverability

In scope, reluctantly. Titles descriptive-searchable over clever; key terms
appear early; structure skimmable. **When discoverability and readability
conflict, readability wins.** The register is untouchable — the wry survives
SEO.

## Repo citation

When a piece discusses a methodology mechanism, link the canonical document
in the public repo (`davepierceops/ai`) as the authoritative artifact.

## Venue and portability

Canonical home: Dave's own site (pending; LinkedIn interim). Until settled:
write venue-independent prose with no platform-specific formatting
dependencies. Once the site exists it is canonical and everything else is a
cross-post.

## Disclosure

Site-level, stated once, in register — LLMs listed among the writing tools
alongside the dictionary and the public school education, with the closing
commitment: Dave personally reads and stands behind every published word,
including those that started in an LLM. No per-piece disclosure.

## AI prose-smell — named defect class

Enforced adversarially in its own editing pass. The tell list is open;
add tells as they are noticed. Current entries:

- "load-bearing"
- em-dash cascades
- "it's not X, it's Y" constructions
- triadic sentence rhythm as default cadence
- hedge-then-assert patterns
- re-stating the thesis at every section opening
- summary sentences that add nothing ("This matters because...")

A tell appearing in a draft is not a crisis; a tell surviving the purge pass
is a defect.
