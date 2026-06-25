---
name: star-audit
description: "Audit STAR responses in the candidate's interview-prep documents against his STAR construction conventions before delivery. Use this skill whenever an interview-prep document (recruiter screen, behavioural panel, executive panel) containing STAR responses or a speaking-notes addendum is about to be saved to Interview Prep/ or presented as the final output of a prep session. Also use when [Candidate First Name] says 'audit the STARs', 'check the STAR structure', 'are these STARs right', or 'run the STAR check'. The audit is mechanical (~30–60 sec) and catches the most common prep failure modes: an Action written as a what-list instead of a how-mechanism, numbered-list structure instead of flowing 5.8-style prose, missing or unbolded principle lines, and spoken responses without a drop list of at least 20 seconds of cuttable runway."
---

# STAR Audit — interview-prep verification skill

Codifies the STAR construction conventions of `Project_Instructions.md` (rev 2026-06-12). Wave 2 verification skill of the framework.

This skill mechanically audits every STAR response in an interview-prep document. It exists because the STAR disciplines are the most-often-eroded content rules under context pressure: a reshape or tightening pass quietly flattens a HOW into a what-list, or drops the bolded principle lines that are the load-bearing structure [Candidate First Name] holds in memory under panel pressure.

---

## When to invoke

- **Default trigger:** before saving any interview-prep document or speaking-notes addendum containing STAR responses to `[Workspace Folder Path]/Interview Prep/`, and after any content reshape or tightening pass that touched STAR text.
- **Explicit triggers:** "audit the STARs", "check the STAR structure", "run the STAR check", "are the principle lines intact".
- **Skip when:** the document is a practicalities-only deliverable (e.g. a short recruiter Q&A with no STAR content).

## Inputs the skill needs

1. **The prep document text** (or file path) — the brief, the addendum, or both.
2. **The interview format** (recruiter screen / behavioural panel / executive panel) — determines whether drop lists are mandatory (they are for any spoken response).

## Audit checks — run all six per STAR

Load `references/star-rules.md` for the full rule definitions, then check each STAR response:

1. **Why/How/What structure.** Situation + Task present and framed as *why* the work was needed; Action present and framed as *how* (mechanism, sequencing, judgement call); Result present with metrics. Flag any Action that reads as a bare what-list ("did X, did Y, did Z" with no mechanism or judgement).
2. **5.8-style prose.** The Action is flowing prose, **not a numbered list**. Each HOW move is followed by an embedded "why this worked" principle. Flag numbered/bulleted Actions as High severity — they read as a checklist, not an executive thinker.
3. **Bolded principle lines.** Embedded principle lines are bolded; the response ends on a crisp closing principle, bolded. Flag missing bolding (Medium) and a missing closing principle (High).
4. **Drop list present.** Every spoken STAR carries an on-the-fly drop list naming specific sentences with per-cut time savings.
5. **Drop-list runway ≥ 20 seconds.** Sum the stated savings; flag below 20 sec (Medium).
6. **Closing principles never in the drop list.** Flag any drop-list entry that names a closing principle line or any bolded principle (High — those are the structural lands the panel remembers).

## Output format

A per-STAR table (STAR ID / checks passed / findings with severity and exact-quote evidence / recommended fix), then a one-line verdict: **Pass** or **Amend before delivery** (any High finding). Gate behaviour: High findings block delivery; Medium and Low are advisory — [Candidate First Name] decides.
