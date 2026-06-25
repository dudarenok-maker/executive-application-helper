---
name: capability-mapping-check
description: "Verify that a panel brief for an SES or equivalent senior role contains a complete capability mapping section before delivery — all framework capability groups mapped per question, Strong/Adequate/Watch ratings on every cell, a named pivot story for every Watch, an overall coverage matrix, a values/behaviours cross-frame, and the cumulative-impression reminder. Use this skill whenever a panel or executive-panel brief for an APS SES role (or a state-government / board-level equivalent scored against a formal capability framework such as the ILS) is about to be saved to Interview Prep/ or delivered. Also use when [Candidate First Name] asks 'check the capability mapping', 'is the ILS coverage complete', or 'run the mapping check'. The check is mechanical (~30–60 sec) and catches the panel-prep failure mode where coverage thins on one capability and no pivot story exists when the panel probes it."
---

# Capability Mapping Check — SES panel-prep verification skill

Codifies the "Panel interview prep — SES and equivalent senior roles" capability mapping convention of `Project_Instructions.md` (rev 2026-06-12). Wave 2 verification skill of the framework.

For SES and equivalent roles the panel scores against a formal capability framework — typically the APS ILS for SES roles, plus organisation-specific values frameworks. The brief must demonstrate *conscious* coverage; this skill verifies the demonstration is complete.

---

## When to invoke

- **Default trigger:** before delivering any behavioural-panel or executive-panel brief where the role is APS SES Band 1/2 or a state/board equivalent scored against a named capability framework. Not required for recruiter screens.
- **Explicit triggers:** "check the capability mapping", "is the ILS coverage complete", "run the mapping check", "where does coverage thin".
- **Re-run** when final questions arrive (~24h out) and Section A tailored responses replace the generic STARs — the mapping must reflect the responses [Candidate First Name] will actually give.

## Inputs the skill needs

1. **The panel brief** (text or file path).
2. **The applicable framework(s)** — e.g. APS ILS SES Band 1 five groups; agency values; conduct codes (APS Values, DRIVE, agency-specific).
3. **The confirmed or likely questions** the mapping is built against.

## The six required components

Load `references/mapping-checklist.md`, then verify each is present and complete:

1. **Capability groups reference list** — the framework's groups stated (ILS SES Band 1: Shapes strategic thinking; Achieves results; Cultivates productive working relationships; Exemplifies personal drive and integrity; Communicates with influence).
2. **Per-question capability mapping** — a table per question showing every capability tested, where the response covers it, and a **Strong / Adequate / Watch** rating on every cell. Flag unrated cells.
3. **Overall coverage matrix** — capabilities × questions, at-a-glance.
4. **Watch pivot plan** — every Watch names a specific pivot story (with underlying STAR ID) and the trigger phrases to listen for. A Watch without a pivot story is a High finding.
5. **Values and behaviours coverage summary** — cross-frame matrix of agency values / conduct codes / APS Values per question.
6. **"One thing to remember on the day"** — the cumulative-impression reminder (the panel scores the cumulative impression, not each question in isolation; trust the matrix).

Also verify, for ≤30-minute panels: Section 6 questions-back constrained to **2 primary + 3 backup** with swap guidance.

## Output format

A six-component checklist (present / incomplete / missing, with what's missing), the list of Watch capabilities and their pivot status, and a verdict: **Pass** or **Amend before delivery** (missing component or unpivoted Watch = High). High findings block delivery in gate mode.
