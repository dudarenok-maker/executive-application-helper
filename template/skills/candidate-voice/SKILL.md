---
name: candidate-voice
description: "Apply the candidate's executive voice and style — written or spoken — or audit existing material against it. Use this skill any time you are (a) drafting, rewriting, sharpening or reviewing prose the candidate will send or sign (emails, cover letters, statements of claims, briefings); (b) preparing for or rehearsing an interview the candidate will sit (recruiter screens, behavioural panels, executive panels — including STAR-style prep documents and opening scripts); (c) generating an interview-prep document using the framework's twelve-section template; or (d) running the MANDATORY pre-delivery voice audit that must precede the draft gate on every application document. Also use when the candidate asks to 'make this sharper / more like me / in my voice' or for a critique, audit or tone review of any writing. Default to invoking this skill rather than freelancing on voice, tone or interview-prep structure."
---

# Candidate Voice — written voice, spoken voice, prep structure, and the voice audit

> **Setup note:** This is a template skeleton. At setup, populate the three reference files from the candidate's completed style guides (Setup Orchestrator Phase 2 produces them), and replace `[Candidate Name]` / `[Candidate First Name]` throughout. Rename the skill if you prefer (e.g. `jane-voice`) — update the `name:` field and every reference to it in `Project_Instructions.md`.

This skill is the canonical home for the candidate's voice and structural templates. Four modes.

## Mode 1 — Writing voice (APPLY)

For any written deliverable the candidate will sign. Load `references/style-guide.md` and apply it as the style baseline: tone register, sentence rhythm, banned constructions, evidence-first discipline, fit-acknowledgment style.

## Mode 2 — Interview voice (spoken delivery)

For spoken-response drafting and rehearsal. Load `references/interview-style-guide.md`. It carries voice consistency from the writing guide plus spoken-delivery adjustments: pause markers, spoken cadence, drop lists, and timing at the candidate's **actual measured** words-per-minute.

## Mode 3 — Interview-prep structure

For generating a prep document. Load `references/interview-prep-template.md` — the canonical twelve-section structure (front-matter; executive summary as a decision instrument; company context; operating entities; panel and individual research; structural-reality analysis; opening script; likely-questions table; STAR responses; practicalities; calibrated questions for the panel; sources), plus the two cross-cutting disciplines: **§R research disciplines** (the confidence ladder, source-authority ranking, inference labelling, handling markers, per-round hygiene) and **§X cross-artefact consistency** (reconcile every spoken answer against everything already submitted for the role). The research sections sit **before** the scripts deliberately — a pack that writes the scripts first has written them without the research.

## Mode 4 — VOICE AUDIT (mandatory before every draft gate)

**This mode is not optional and does not wait to be asked.** Every application document runs through it after drafting and **before** `draft-gate`. The gate's Check 0 is blocking: if the audit has not run and its findings have not been folded in, the gate stops and sends you back here.

Why it sits ahead of the gate rather than inside it: the gate's other checks are about compliance — length, overclaim, prescription. The audit is about whether the document reads as though a person wrote it. A draft can pass every compliance check and still be recognisably machine-made, and the reader who spots that stops reading for content and starts reading for tells.

Audit the near-final draft against these, each with **evidence** — a count, an exact quote, or the pattern searched with a null result:

| # | Check | What "pass" looks like |
|---|---|---|
| 1 | **Opener rotation** | The opening move is not the one used in the previous letter — and not the same move used twice in a row to the same recruiter. Rotate among the sanctioned openers (see the style guide). |
| 2 | **Em-dash discipline** | Within the cap **and not zero.** Zero em-dashes usually means colons are carrying every rhythmic beat, which is the same machine tell wearing a different hat. |
| 3 | **Word-echo** | No distinctive word repeated across paragraphs. Function words don't count; a striking noun or verb repeated three times does. |
| 4 | **Sentence-rhythm spikes** | At least one short sentence against long neighbours. Flat multi-sentence runs of similar length are the strongest single tell. |
| 5 | **Low-probability phrase** | At least one phrase a language model would not have reached for first. Quote it. |
| 6 | **Wit or warmth** | One moment of it, somewhere. Executive register is not the same as affectless. |
| 7 | **Banned filler** | None of the style guide's banned constructions. Name the patterns searched. |
| 8 | **Bolded lead-ins** | Present, consistent, and punctuated per the style guide. |
| 9 | **English variant** | Consistent throughout. Search the usual suspects (`-ize`, `-yze`, `-or`/`-our`). |

**Fold every finding into the draft before any output file is produced.** A draft with an open voice finding is not final, whatever else has passed.

### The edit loop — the highest-value input this skill ever gets

The candidate's own edits to a review `.docx` are the single best source of voice signal the framework receives: they are the delta between what was generated and what the person would actually say. At the maintenance step, look at those edits as a set rather than one at a time. When the same correction appears twice, it is no longer a preference — it is a rule, and it belongs in `references/style-guide.md`.

## Reference files

| File | Populate from |
|---|---|
| `references/style-guide.md` | The candidate's Writing Voice and Style Guide (Setup Phase 2) |
| `references/interview-style-guide.md` | The candidate's Interview Voice and Style Guide |
| `references/interview-prep-template.md` | The framework's Interview Prep Template, calibrated to the candidate |

Keep this skill as the **single source of truth** for voice content. If stub pointer files exist at the workspace root for discoverability, they must point here — never carry divergent copies.
