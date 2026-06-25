---
name: watchouts-sweep
description: "Cross-check a drafted application document (cover letter, statement of claims, targeted pitch, recruiter response, screening-question response) against the candidate's watch-outs register (Examples_Section_7_Watchouts.md) before delivery. Use whenever a draft is about to be saved to Submissions/ or presented as the final output of an application-drafting session. Also use when the candidate asks to 'sweep this for watchouts', 'check this for overclaim', or 'verify this against Section 7'. The sweep is mechanical (~30–60 sec) and catches the most common executive-application failure mode: an overclaim that the register would have caught."
---

# Watchouts Sweep — Section 7 verification skill

> **Setup note:** This is a template skeleton. The sweep runs against the watch-outs register your framework accumulates in `Examples_Section_7_Watchouts.md`. The register starts thin — every entry is added after a real overclaim is caught (that is the discipline that makes it valuable). The skill needs no per-candidate editing beyond placeholders.

## When to invoke

- **Default trigger:** before saving any drafted `.docx` to `[Workspace Folder Path]/Submissions/`, before delivering any screening-question response, and before any final application document is presented to the candidate.
- **Explicit triggers:** "sweep this for watchouts", "check for overclaim", "verify against Section 7".
- **Skip when:** the draft is an intermediate iteration under active review (sweep at the end, not every revision).

## Inputs

1. **The draft text** (inline or file path).
2. **The matched matrix row ID** — its `Notes / Distinct from` column names the specific 7.1.x sub-variants that apply. If unknown, infer the role family and sweep against family-wide watch-outs plus all named sub-variants.
3. **The role context** (organisation, sector, role title) — for domain-specific watch-outs.

## Method

1. **Load the register** — read `Examples_Section_7_Watchouts.md` in full: 7.1 experience-limits table and sub-variants, 7.2 framing discipline, 7.3 evidence-recency flags.
2. **Filter to applicable watch-outs** using the matched row and role context. Universal honesty boundaries in the 7.1 table always apply.
3. **Sweep the draft** — for each applicable watch-out, search the draft for breaching claims: scope inflation, temporal-qualifier loss ("first" without "at the time"), attribution drift (organisation-level outcomes claimed as personal), stale metrics (7.3).
4. **Score each finding** High / Medium / Low with exact-quote evidence and a register-compliant alternative wording.

## Output and gate behaviour

Findings list (severity / exact quote / breached watch-out / recommended rewording), then verdict. **High-severity findings block delivery until amended; Medium and Low are advisory** — the candidate decides. (Run advisory-only for the first two weeks of a new setup while the register is young, then flip High to blocking.)
