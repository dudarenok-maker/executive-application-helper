# Executive Application Helper — Template Package (v0.6.5)

**Estimated read time:** 7 minutes

A reusable, Claude-driven framework for preparing high-quality executive job applications and interview preparation. This template gives you a structured evidence bank, a voice baseline, a document production pipeline, three verification gates and operating instructions — pre-wired to be filled in and run inside Anthropic's Cowork mode (or any Claude project with file access).

Once populated, the framework produces tailored cover letters, statements of claims, targeted pitches and recruiter responses in a single session — with coverage analysis, resume tailoring and evidence-bank maintenance built into every run.

---

## 1. Executive summary

| What you get | What it does |
|---|---|
| **`Project_Instructions.md`** | The operating brain (V6 dispatcher, ~20 KB). Drives Claude every session: gating, index→row retrieval, channel length bands, drafting, gates, maintenance. |
| **`Writing_Voice_and_Style_Guide.md`** | Your tone-and-style baseline, including opener rotation and the mandatory voice audit. |
| **`Resume_Master.md`** | **The** single source of truth for career history and metrics. One file; variants live in its front-matter. |
| **`Examples_Master.md` + section files A, B1–B6, C, D/E** | Your evidence bank — modular, indexed, retrieved on demand. |
| **`Examples_Section_5_*` indexes + `Matrix_Rows/`** | Role-family archetypes: a slim index per family, full prescriptions in per-row files. |
| **`Pipeline/`** | Working `.md → HTML → PDF` build for the resume and letters, under one design system. |
| **`skills/`** | Three composite verification gates (draft / prep / bank) plus the voice and coverage skills. |
| **Changelogs + git** | Audit trail, staleness control, and full state recovery. |
| **Setup orchestrator** | A paste-in prompt that drives Claude to interview you and populate everything here. |

**To get to a working setup:** read this file, then paste the contents of `01_SETUP_ORCHESTRATOR.md` into a fresh Cowork session. Claude guides you from there.

---

## 2. Prerequisites

- **A Claude product with project and file access** — Cowork mode (recommended), Claude.ai with Projects, or equivalent. The framework relies on Claude reading and editing files in a workspace folder.
- **Your raw career material** — current resume, three to five samples of your own writing (emails, LinkedIn posts, articles, briefing notes), three to five strong achievements with scope, action and outcome.
- **`git`** — the workspace becomes a repository at setup. This is the framework's entire safety model; there is no fallback.
- **Python 3.10+ with `weasyprint`, `jinja2`, `markdown`, `pyyaml`**, plus `pandoc`, for the document pipeline. Optional at first: you can draft in Markdown before wiring up PDF output.
- **About 90 minutes for setup** — split across one to three sessions if needed.

---

## 3. What this framework does well

- **Evidence-led applications.** Every claim traces back to a real example with scope, action and outcome.
- **Retrieval that stays cheap.** Slim family indexes plus per-row detail files mean a session loads the one archetype it matched, not a whole family matrix.
- **Reusability.** Once the bank is populated, every application reuses and sharpens it rather than rebuilding.
- **Honesty discipline.** A watch-outs register, earned one caught overclaim at a time, gates every draft.
- **Gates, not vibes.** Three composite gates each require a written verification checklist with evidence per row — the checks most often skipped under pressure are the ones made mechanical.
- **One resume, many variants.** A single source file with named variants, a 2-page mode, and a real build pipeline.
- **A review loop that ends in your words.** Letters are delivered as an editable `.docx` first; your edits fold back into the source before the final PDF, and recurring patterns fold into the voice guide.
- **Maintenance baked in.** Every session ends with the bank refreshed, the changelog appended, and a commit.

## 4. What this framework does not do

- It does not invent achievements, metrics or motivations. Everything comes from material you provide.
- It does not replace your judgement. Claude drafts; you read every word and sign.
- It does not do the discovery for you. Output quality scales with the depth of evidence you load in.

---

## 5. Recommended setup flow

The orchestrator (`01_SETUP_ORCHESTRATOR.md`) walks you through five phases.

| Phase | Goal | Files populated | Time |
|---|---|---|---|
| **1 — Foundations** | Identity, roles, capability domains, git repository, contact details. | `Resume_Master.md`, `Project_Instructions.md` (personalised), `.gitignore`, baseline commit | 20–25 min |
| **2 — Voice and style** | Establish your written and spoken voice from samples. | `Writing_Voice_and_Style_Guide.md`, `Interview_Voice_and_Style_Guide.md` | 20–30 min |
| **3 — Evidence bank** | Three to five strong achievements per capability domain; positioning blocks; the first family index and row files. | `Examples_Section_*` files, `Examples_Master.md`, `Matrix_Rows/` | 30–40 min initially |
| **4 — Gates and skills** | Package and install the three composite gates plus the voice and coverage skills. | `skills/*` | 10–15 min |
| **5 — Pipeline** | Wire up document production and prove one build end to end. | `Pipeline/` | 15–20 min |

Phases 2, 3 and 5 deepen with use. Every application produces new framings, metrics and entries that fold back in at the maintenance step.

---

## 6. How to use the package after setup

1. **Move the populated files** out of `_Template` into the workspace root of your project. `_Template` stays as the master reference for future setups.
2. **Copy `Project_Instructions.md` into your project's instructions field.** This is what makes Claude behave like an executive recruitment consultant every session.
3. **Install the skills** (Phase 4). Until they are installed, the gates run as prose checklists rather than invoked skills — workable, but easier to skip.
4. **Run an application.** Drop the role materials. Claude gates on materials, runs the pre-drafting assessment, drafts, audits voice, runs the draft gate, gives you an editable review copy, produces the final PDF after your edits, analyses coverage, suggests resume tailoring, maintains the bank, and commits.

See `02_HOW_TO_USE_AFTER_SETUP.md` for operating notes.

---

## 7. Folder contents

| File | Purpose |
|---|---|
| `00_README.md` | This file. Entry point. |
| `01_SETUP_ORCHESTRATOR.md` | Paste-in prompt that drives Claude-guided population of all files. |
| `02_HOW_TO_USE_AFTER_SETUP.md` | Operating notes for running the framework once set up. |
| `Project_Instructions.md` | Generic, de-personalised V6 operating instructions. |
| `Writing_Voice_and_Style_Guide.md` | Skeleton voice-and-style guide, with opener rotation and the voice audit. |
| `Interview_Voice_and_Style_Guide.md` | Spoken-delivery companion guide. |
| `Interview_Prep_Template.md` | The twelve-section prep-document structure, including the research half (company context, operating entities, panel research, structural-reality analysis) and the panel-room half (decision-instrument executive summary, cross-artefact consistency, attribution, coaching-note elements). |
| `Resume_Master.md` | Single-source resume skeleton in the Pipeline's format, with variants. |
| `Examples_Master.md` | Evidence-bank operating layer: protocol, entry format, vocabulary, master index, family pointers. |
| `Examples_Section_5_INDEX_TEMPLATE.md` | Copy-me skeleton for a role-family index file. |
| `Matrix_Rows/README.md`, `Matrix_Rows/_ROW_TEMPLATE.md` | Row-file format, second-occurrence policy, copy-me row skeleton. |
| `Examples_Section_A_Positioning.md` | Skeleton positioning blocks. |
| `Examples_Section_B1.md` – `B6.md` | Skeleton capability-domain evidence files (renameable per your career). |
| `Examples_Section_C_Templates.md` | Re-usable drafting templates. |
| `Examples_Section_D_E_Personal_Maintenance.md` | Optional personal content + maintenance protocol notes. |
| `Pipeline/` | Working build system: `build.py`, `brand.css`, HTML templates, README. |
| `skills/` | `draft-gate`, `prep-gate`, `bank-gate`, `candidate-voice`, `coverage-audit`. |
| `gitignore.template` | Starter `.gitignore` plus the git setup and recovery commands. |
| `Evidence_Bank_Changelog.md` / `Project_Instructions_Changelog.md` | Starter changelogs with the 2–4-line entry protocol. |
| `Template_Changelog.md` | Change history for **this template package**. |

---

## 8. Maintaining and contributing back

This template is designed to evolve. If you find improvements during real use — sharper prompts, better gating rules, additional capability domains, new archetypes — capture them in your own copy and consider sharing them back.

The framework this was extracted from has a rule baked into its own instructions (Step 5): whenever the live framework changes structurally, the template package is updated in the same session, with a matching entry in `Template_Changelog.md`.

---

## 9. Source of this template

Extracted from a working executive application framework run inside Anthropic's Cowork mode. All personal content has been removed; the structural logic, retrieval protocol, drafting workflow, gate discipline, production pipeline and maintenance rules are preserved in full.

`Template_Changelog.md` records the structural reasoning behind each version — including what was retired and why, which is usually the more useful half.
