---
name: coverage-audit
description: "Generate the STEP 2 coverage analysis for a drafted application document — mapping the draft against every section of the source materials (candidate information pack, position description, advertisement, selection criteria, recruiter requests, 'About You' / 'Key Accountabilities' / 'Capabilities' sections) and marking each Addressed / Partially Addressed / Not Addressed with the supporting evidence-bank entry IDs. Use this skill immediately after any application draft is finalised (cover letter, statement of claims, targeted pitch, selection criteria response, recruiter response) — STEP 2 is mandatory for every application-drafting session. Also use when [Candidate First Name] asks 'how well does this cover the PD', 'coverage analysis', 'what did we miss', or 'map the draft to the criteria'. Produces the Step 2 deliverable tables directly."
---

# Coverage Audit — STEP 2 verification skill

Codifies STEP 2 (coverage analysis) of `Project_Instructions.md` (rev 2026-06-12). Wave 3 verification skill of the framework.

This skill produces the supplementary analysis showing how well the drafted response addresses the source materials. It runs after the draft is final (post `length-check` and `watchouts-sweep`), because coverage is assessed against delivered text, not an intermediate draft.

---

## When to invoke

- **Default trigger:** after STEP 1 closes on any application-drafting session — coverage analysis is mandatory, not optional.
- **Explicit triggers:** "coverage analysis", "how well does this cover the PD", "what did we miss", "map the draft to the criteria".
- **Not applicable** to interview prep (STEP 2 is an application-drafting step).

## Inputs the skill needs

1. **The final draft text** (or file path in `Submissions/`).
2. **All source materials provided this session** — candidate information pack, position description, advertisement, recruiter requests, selection criteria.
3. **The evidence-bank entry IDs used** in the draft (from the Step 1 traceability list).

## Method

Load `references/coverage-method.md`, then:

1. **Enumerate the assessable sections** across all provided materials: selection criteria; "About You" / "What We Are Looking For"; "Key Accountabilities"; "Key Challenges"; "Capabilities"; recruiter-specific requests; any equivalent section.
2. **Map each section to the draft.** Mark **Addressed / Partially Addressed / Not Addressed**; cite the draft passage and the supporting evidence-bank entry ID(s).
3. **Surface the risk list:** important requirements not strongly evidenced; areas where further examples would improve the application; wording in the draft that needs strengthening or sharpening.
4. **Feed STEP 4:** any gap that traces to missing bank evidence (rather than drafting choice) is named as a candidate evidence-bank capture for the post-draft maintenance report.

## Output format

The STEP 2 deliverable: one table per source document (Section / Status / How covered + entry IDs / Gap or risk), followed by the consolidated risk list and the bank-gap candidates. Advisory by nature — coverage gaps inform the candidate's submit/strengthen decision; they do not block delivery.
