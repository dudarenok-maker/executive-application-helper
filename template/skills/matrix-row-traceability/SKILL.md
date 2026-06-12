---
name: matrix-row-traceability
description: "Confirm that a drafted application document actually follows the prescription of its matched evidence-bank matrix row — every B-ID in the row's body stack is reflected in the draft, the dominant A-ID positioning leads, the template and length band match, and the fit-acknowledgment style and AI register are honoured. Use this skill at Step 1 close on any application-drafting session where a matrix row was matched (cite by ID), alongside length-check and watchouts-sweep. Also use when [Candidate First Name] asks 'did we follow the row', 'trace the draft to the matrix', or 'is this on-prescription'. Catches prescription drift: a draft that silently swapped the row's tested body stack for ad-hoc evidence selection, losing the calibration the row encodes."
---

# Matrix Row Traceability — prescription verification skill

Codifies the matched-row mechanism of `Project_Instructions.md` (Mandatory retrieval-first protocol, steps 3–4; rev 2026-06-12). Wave 3 verification skill of the framework.

The matrix rows encode tested calibrations — which positioning leads, which body stack lands, which template and length band fit the archetype. A draft that drifts from the matched row without a documented reason quietly discards that calibration. This skill makes the drift visible.

---

## When to invoke

- **Default trigger:** at Step 1 close, after `length-check` and `watchouts-sweep`, before the draft is delivered — on any session where a matrix row was matched.
- **Explicit triggers:** "did we follow the row", "trace the draft to the matrix", "is this on-prescription".
- **Skip when:** the session ran on a documented no-clean-match basis (closest-analogue noted in the pre-drafting assessment) — then trace against the analogue row and note the documented deviations.

## Inputs the skill needs

1. **The final draft text** (or file path).
2. **The matched matrix row ID** and its full row from the relevant `Examples_Section_5_*.md` file (positioning A-IDs with dominant flag, body stacks grouped by paragraph, template + length band, fit-acknowledgment style, AI register, companion files).
3. **The pre-drafting assessment** (for any documented deviations agreed before drafting).

## Checks — run all six

Load `references/traceability-method.md`, then:

1. **Body-stack reflection.** Every B-ID in the row's body stack appears in the draft as substantive content (not a passing mention). List any absent B-ID and any substituted entry.
2. **A-ID dominance.** The row's dominant positioning block leads the draft's framing; secondary A-IDs support, not compete.
3. **Template + length band.** The draft used the row's prescribed template (C1–C6) and sits inside the row's length band (cross-checked with `length-check` output, not recounted).
4. **Fit-acknowledgment style.** Honest-gap framing follows the row's prescribed style (e.g. direct acknowledgment vs adjacent-strength bridge).
5. **AI register.** The draft's AI positioning matches the row's register (e.g. hands-on builder vs governance-led).
6. **Documented deviations.** Every deviation from 1–5 is either documented in the pre-drafting assessment or flagged now as undocumented drift.

## Output format

A six-check table (check / on-prescription / deviation / documented?), then verdict: **On-prescription**, **Documented deviations only**, or **Undocumented drift — review** (advisory: [Candidate First Name] decides whether the drift is an improvement to fold back into the row at STEP 4, or a regression to fix). Undocumented drift that *is* an improvement must be recorded against the matrix row in the same session — that is the row-calibration loop.
