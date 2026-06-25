---
name: personal-context-discretion-check
description: "Verify at session close that any sensitive personal context [Candidate Name] shared during the session (health, medical history, family circumstances, or anything on the sensitive-personal-information list) was used ONLY in the named deliverable it was shared for, with his explicit consent, and was NOT propagated to the evidence bank, the memory system, or staged for any future deliverable. Use this skill at the close of any session in which sensitive personal context surfaced — interview prep with lived-experience questions is the canonical case. Also use when [Candidate First Name] asks 'check the discretion rule', 'did anything personal leak', or 'verify the personal-context boundary'. This is a blocking check: a propagation finding must be reversed before session close, not noted for later."
---

# Personal Context Discretion Check — session-close boundary skill

Codifies the Personal context discretion convention  of `Project_Instructions.md` (rev 2026-06-12). Wave 3 verification skill of the framework.

Sensitive personal context is one-time and bounded to the deliverable it was shared for. Calibration standard: a sensitive health-history detail used in one named panel brief with explicit direction, and deliberately not propagated to `Examples_Section_D_E_Personal_Maintenance.md` or any memory file. This skill makes that discipline a checked gate at session close.

---

## When to invoke

- **Default trigger:** at session close (immediately before the STEP 4 maintenance report, or before the post-prep report for interview-prep sessions) whenever sensitive personal context surfaced during the session.
- **Explicit triggers:** "check the discretion rule", "did anything personal leak", "verify the personal-context boundary".
- **Skip when:** no sensitive personal context surfaced this session (state that explicitly in the close-out if the session was prep for a lived-experience-adjacent role).

## What counts as sensitive

Health and medical history, mental-health details, family circumstances, protected attributes, and anything on the system sensitive-personal-information list. When in doubt, treat as sensitive.

## Checks — run all four

Load `references/discretion-rules.md`, then:

1. **Consent scope.** The context was used only in the named deliverable [Candidate First Name] shared it for, and his explicit consent for that use exists in this session's record.
2. **Bank boundary.** No evidence-bank file touched this session carries the context — no entry, no proof point, no caution row, no changelog narrative detail. (Grep the session's touched files for the context's key terms.)
3. **Memory boundary.** No memory file or memory entry created or amended this session carries the context.
4. **Forward-staging boundary.** No note, draft, template, or "for next time" artefact stages the context for a future deliverable. Re-surfacing in future requires the candidate's explicit direction at that session's kickoff — nothing this session may pre-commit it.

## Output format

A four-check table (boundary / clean / finding with file + line), then verdict: **Clean** or **Propagation found — reverse before close**. Gate behaviour: blocking — a finding is reversed in-session (remove the content, re-run), never parked as a follow-up. If the changelog must record that prep touched personal context at all, it records the fact category only (e.g. "lived-experience response prepared"), never the substance.
