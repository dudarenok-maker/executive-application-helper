# Watch-outs sweep checklist

> **Setup note:** This file is the only genuinely candidate-specific part of `draft-gate`. It is a **flat, greppable list** of every named watch-out in the register — `Examples_Master.md` Section 7, or `Examples_Section_7_Watchouts.md` once the register outgrows the Master file and is split out — so the sweep does not depend on holding a long register in working memory. Regenerate it whenever the register gains an entry.

A new framework starts with an almost-empty register, and that is correct: **every entry should be earned.** A watch-out is added when a real overclaim is caught — in a draft, in a gate finding, or in feedback after an interview. A register populated speculatively at setup fills with rules nobody believes and the sweep degrades into ritual.

## Structure to maintain

```markdown
## Always-applicable honesty boundaries
- [ID] [Short name] — forbidden claim: "[the exact phrasing that overclaims]".
      Compliant alternative: "[the phrasing the bank supports]".
      Search patterns: "[pattern1]", "[pattern2]"

## Role-family / sector sub-variants
- [ID] [Family or sector] — applies when: [the trigger].
      Required framing: [what the draft must do].
      Search patterns: "[pattern1]", "[pattern2]"

## Framing discipline
- [ID] [Rule] — e.g. lead with the substance of what was built, not the label of the technology.
      Search patterns: "[pattern1]"

## Evidence recency
- [ID] [Claim family] — flag whenever a figure older than [N] months is used as current.
      Search patterns: "[pattern1]"
```

Each entry needs its **search patterns** written out. That is what makes the sweep mechanical: the gate's evidence cell is either an exact quote from the draft or `no match found for pattern "<pattern>"`, and the second half is impossible to produce honestly without a pattern to name.

## Sweep order

1. Always-applicable boundaries — every draft, every time, no exceptions.
2. Sub-variants matching the role family or sector of this brief.
3. Sub-variants the matched row's `Notes / Distinct from` section names explicitly.
4. Framing discipline.
5. Evidence recency.

With no matched row, run every sub-variant. A false positive costs one line of report; a missed overclaim costs the application, and occasionally the relationship with the recruiter who forwarded it.

## Scoring

| Score | Meaning | Effect |
|---|---|---|
| **High** | A direct or indirect breach of a named honesty boundary | **Blocks delivery** |
| **Medium** | A framing breach, or a mandatory discipline the row requires and the draft omits | Advisory — recommend the rewrite |
| **Low** | A recency flag, or a contextual near-miss worth knowing about | Surface for awareness |

Anything the register does not name is raised as a **"Watch-out candidate"**, never as a finding — and if the candidate agrees it is real, it becomes a register entry in the same session. That is how the register grows: one caught overclaim at a time.
