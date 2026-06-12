# Executive Application Helper — Template Package

**Estimated read time:** 6 minutes

A reusable, Claude-driven framework for preparing high-quality executive job applications. This template gives you a structured evidence bank, a tone-and-style baseline, drafting templates and operating instructions — pre-wired to be filled in and run inside Anthropic's Cowork mode (or any Claude project).

Once populated, the framework lets you produce tailored cover letters, statements of claims, targeted pitches and recruiter responses in a single Cowork session — with coverage analysis, resume tailoring and evidence-bank maintenance built into every run.

---

## 1. Executive summary

| What you get | What it does |
|---|---|
| **`Project_Instructions.md`** | The operating brain. Drives Claude's behaviour every session: gating, retrieval, drafting, coverage analysis, resume tailoring, evidence-bank maintenance. |
| **`Writing_Voice_and_Style_Guide.md`** | Your tone-and-style baseline. Read by Claude before every write. |
| **`Resume.md`** | Your factual grounding. Loaded every session. |
| **`Examples_Master.md` + section files A, B1–B6, C, D/E** | Your evidence bank — modular, indexed, retrieved on demand. |
| **`Evidence_Bank_Changelog.md` / `Project_Instructions_Changelog.md`** | Audit trail and staleness control. |
| **Setup orchestrator** | A paste-in prompt that drives Claude to interview you and populate everything in this folder. |

**To get to a working setup:** read this file, then paste the contents of `01_SETUP_ORCHESTRATOR.md` into a fresh Cowork session. Claude will guide you from there.

---

## 2. Prerequisites

You need:

- **A Claude product with project / file access** — Cowork mode (recommended), Claude.ai with Projects, or equivalent. The framework relies on Claude being able to read and edit files in a workspace folder.
- **Your raw career material** — current resume, three to five samples of your own writing (emails, LinkedIn posts, articles, briefing notes), three to five strong career achievements with scope, action and outcome.
- **A Word template** (optional but recommended) — your preferred letterhead `.docx` for cover letters. The framework will use it as the base for every formatted output.
- **About 60–90 minutes for setup** — split across one to three sessions if needed.

---

## 3. What this framework does well

- **Evidence-led applications.** Forces every claim back to a real example with scope, action and outcome.
- **Reusability.** Once your evidence bank is populated, every future application reuses and refines it rather than rebuilding from scratch.
- **Honesty discipline.** Built-in watch-outs prevent overclaiming. Staleness checks keep proof points current.
- **Coverage analysis.** Every draft comes with a section-by-section map against the role materials so you can see what was addressed, partially addressed or missed.
- **Resume tailoring.** Side-by-side suggestions for sharpening your resume against each specific role, without a full rewrite.
- **Maintenance baked in.** Every session ends with the evidence bank refreshed, the changelog updated, and any new framings captured for next time.

## 4. What this framework does not do

- It does not invent achievements, metrics or motivations. Everything that ends up in your applications comes from material you provide.
- It does not replace your judgement. Claude drafts; you decide.
- It does not do the discovery for you. The quality of your applications scales with the quality and depth of evidence you load in.

---

## 5. Recommended setup flow

The framework is designed to be set up in three phases. The orchestrator (`01_SETUP_ORCHESTRATOR.md`) walks you through them.

| Phase | Goal | Files populated | Time |
|---|---|---|---|
| **Phase 1 — Foundations** | Capture identity, current role, contact details. Confirm capability domains. | `Resume.md` (skeleton populated), `Project_Instructions.md` (personalised), Word template path confirmed | 15–20 min |
| **Phase 2 — Voice and style** | Establish your writing voice from samples. | `Writing_Voice_and_Style_Guide.md` | 20–30 min |
| **Phase 3 — Evidence bank** | Capture three to five strong achievements per capability domain. Build positioning blocks (Section A) and capability evidence (Sections B1–B6). | All `Examples_Section_*.md` files plus `Examples_Master.md` index | 30–40 min initially; deepens with every application |

After Phase 3, the framework is ready to draft real applications. Phases 2 and 3 can be deepened iteratively — every application you run produces new framings, metrics and entries that get folded back in via the maintenance step.

---

## 6. How to use the package after setup

Once the canonical files are populated:

1. **Move the populated files** out of `_Template` and into the workspace root of your Cowork project (or your equivalent Claude project folder). The `_Template` folder stays as the master reference for future setups.
2. **Copy the contents of `Project_Instructions.md` into your Cowork project's instructions field** (or equivalent system-prompt location). This is what makes Claude behave like an executive recruitment consultant in every session.
3. **Run an application.** Provide the role materials (advertisement, position description, candidate information pack, recruiter brief). Claude will gate on materials, run the pre-drafting assessment, draft, analyse coverage, suggest resume edits, and maintain the evidence bank — all in one pass.

See `02_HOW_TO_USE_AFTER_SETUP.md` for operating notes.

---

## 7. Folder contents

| File | Purpose |
|---|---|
| `00_README.md` | This file. Entry point. |
| `01_SETUP_ORCHESTRATOR.md` | Paste-in prompt that drives Claude-guided population of all files. |
| `02_HOW_TO_USE_AFTER_SETUP.md` | Operating notes for running the framework once set up. |
| `Project_Instructions.md` | Generic, de-personalised operating instructions. |
| `Writing_Voice_and_Style_Guide.md` | Skeleton voice-and-style guide with structural commentary. |
| `Resume.md` | Skeleton resume with section prompts. |
| `Examples_Master.md` | Skeleton evidence-bank master file with full structure preserved. |
| `Examples_Section_A_Positioning.md` | Skeleton positioning blocks. |
| `Examples_Section_B1.md` to `Examples_Section_B6.md` | Skeleton capability-domain evidence files (renameable per your career). |
| `Examples_Section_C_Templates.md` | Re-usable drafting templates (cover letter, SoC, pitch, recruiter response). |
| `Examples_Section_D_E_Personal_Maintenance.md` | Optional personal content + maintenance protocol notes. |
| `Evidence_Bank_Changelog.md` | Empty starter changelog with template entry. |
| `Project_Instructions_Changelog.md` | Empty starter changelog with template entry. |
| `Template_Changelog.md` | Change history for **this template package**. |

---

## 8. Maintaining and contributing back

This template is designed to evolve. If you find improvements during real use — sharper prompts, better gating rules, additional capability domains, new role-family recipes — capture them in your own copy and consider sharing them back to whoever shared the template with you.

The original maintainer of the live project this template was extracted from has a rule baked into their `Project_Instructions` that whenever the live framework changes structurally, this template package is updated in the same session, with a matching entry in `Template_Changelog.md`.

---

## 9. Source of this template

This template was extracted from a working executive application framework run inside Anthropic's Cowork mode. All personal content has been removed; the structural logic, retrieval protocol, drafting workflow, watch-out discipline and maintenance rules have been preserved in full.

If you have questions about how a specific rule is intended to work, the `Template_Changelog.md` records the structural reasoning behind each version of the template.
