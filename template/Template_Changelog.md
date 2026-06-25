---
title: Template Package Changelog
scope: Tracks structural changes to the Executive Application Helper template package itself (this `_Template/` folder)
format: Reverse-chronological. Most recent entries at the top.
last_updated: 2026-06-25 (v0.5.6 — mirror-sync to instructions V5.6: new discipline D6 (Read-tool/shell coherence) + bank-integrity-check Axis 0 stability probe. Prior: v0.5.5 — mirror-sync to instructions V5.5 (version-history banners removed from the live instructions file; no template skeleton content changed). Prior: v0.5.4 — skill-based architecture: 11 skill skeletons in skills/, verification-gates wiring, Setup Phase 4, public GitHub distribution (MIT). Prior same day: PDF output disciplines for annotated prep documents added to the Interview Prep skeleton — v0.4.6. Prior: 2026-05-29 — Data-integrity & resilience disciplines section added — v0.4.5)
---

# Template Package Changelog

This file tracks structural changes to the **template package** — the de-personalised, reusable scaffold in `_Template/` that anyone can use to set up an executive application framework of their own. It is distinct from `Evidence_Bank_Changelog.md` (which tracks the candidate's evidence) and `Project_Instructions_Changelog.md` (which tracks changes to the candidate's live operating instructions).

The maintenance protocol is: whenever a structural change is made to the live framework that would also benefit other users of this package, mirror the change into `_Template/` and append an entry here. Personal content stays in the live files; only structural patterns flow back into the template.

## How to use this log

- One entry per change, in reverse-chronological order (newest first).
- Each entry must capture: date, version transition, files in `_Template/` touched, type of change, rationale, and what a downstream user of the template would notice.
- Group sub-changes under a single date heading when made in one session.
- Do not rewrite history. If an earlier entry is found to be incorrect, add a new entry referring back to it rather than editing the original.

## Change types

- **Major** — new file, new section, new mandatory rule, structural shift in entry format, change to setup flow.
- **Minor** — refinement to placeholder language, additional structural commentary, sharper guidance in skeletons.
- **Editorial** — typo, formatting, deduplication.

## Versioning

The template version **mirrors the candidate's live project-instructions version**: instructions `VX.Y` maps to template `v0.X.Y` (so instructions V5.4 → template **v0.5.4**; a future V6.0 → **v0.6.0**, V6.1 → v0.6.1, and so on). This keeps the published package and the operating instructions legible against each other at a glance. The leading `0.` marks the package as pre-1.0 (still evolving); it rolls to `1.x` only if the framework is ever declared stable for outside users independent of the candidate's own line.

- **The MINOR digit tracks the instructions MAJOR** (V5.x → v0.5.x).
- **The PATCH digit tracks the instructions MINOR** (V5.4 → v0.5.4).
- **A template-only fix** that corresponds to no instructions change takes the next free patch and notes "template-only" in its entry.
- **An instructions-only change** (e.g. housekeeping in the live instructions that does not touch the template skeleton) still advances the template version to keep the mirror in lockstep; its entry notes "mirror-sync — no skeleton content changed."

(Adopted 2026-06-12, retro-applied from v0.5.0 → v0.5.4 to mirror instructions V5.4. Prior history v0.1.0 → v0.4.6 predates the mirror rule and is left as-is.)

## Entry template

```
### YYYY-MM-DD — [short descriptor] — [vX.Y.Z → vX.Y.Z]

- **Type:** Major / Minor / Editorial
- **Files touched:** e.g. `_Template/Project_Instructions.md`; `_Template/Examples_Master.md`
- **Change:** One or two sentences on what changed.
- **Reason:** What in the live framework triggered the update.
- **Downstream impact:** What a user with an existing setup would need to do (or whether nothing is required).
```

---

# Changelog

### 2026-06-25 — Mirror-sync to instructions V5.6 — v0.5.5 → v0.5.6

- **Type:** Structural — new resilience discipline + skill-skeleton update.
- **Change:** Mirrored instructions Convention 18 into the template as **discipline D6** (Read-tool / shell coherence for changelogs and append-only files), added a pointer from D4, and updated the `bank-integrity-check` skill skeleton — header coherence caveat plus an **Axis 0** mounted-folder stability probe ahead of the three integrity axes.
- **Reason:** Root-cause finding (2026-06-25): on a mounted/synced workspace, a host-side editor write can be served stale to a shell read, and writing that view back truncates the file. This was the cause of a recurring changelog-truncation cycle that the rebuild-whole rule (D3) alone did not stop. De-personalised for any user's environment.
- **Files touched:** `Project_Instructions.md` (D6 + D4 pointer); `skills/bank-integrity-check/references/check-script.sh` (Axis 0 + caveat); `skills/bank-integrity-check/SKILL.md` (coherence section); `Template_Changelog.md` (this entry); `README.md` (version bump).

### 2026-06-12 — Mirror-sync to instructions V5.5 — v0.5.4 → v0.5.5

- **Type:** Editorial (mirror-sync; no template skeleton content changed).
- **Files touched (`_Template/`):** `Template_Changelog.md` (this entry; front-matter bumped to v0.5.5; Versioning section gains the instructions-only-change clause). No other skeleton file changed.
- **Mirrors live change:** instructions V5.4 → V5.5 — the V5.0–V5.4 version-history banners were removed from the top of the live `Project_Instructions_V5.md` and replaced with a one-line current-version pointer to the changelog (history belongs in the changelog, not the always-loaded instructions). The template's instructions skeleton already used a setup-note header with no banner stack, so there was nothing to remove there.
- **Why the version still moved:** under the mirror rule (instructions `VX.Y` ↔ template `v0.X.Y`) the template version advances in lockstep even when a change is instructions-only, so the two numbers stay legible against each other. See the Versioning section.
- **What a downstream user notices:** nothing in the skeleton changes; the package is re-tagged v0.5.5 to match instructions V5.5.

### 2026-06-12 — Skill-based architecture: eleven de-personalised skill skeletons, verification-gates wiring, Setup Phase 4, public GitHub distribution; version line re-aligned to mirror instructions — v0.4.6 → v0.5.4

- **Type:** Major (new `skills/` folder with 11 skill skeletons; new mandatory-wiring section in the Project Instructions skeleton; new setup phase; new distribution channel).
- **Files touched (`_Template/`):** `skills/` (new — `candidate-voice`, `watchouts-sweep`, `length-check`, `bank-integrity-check`, `matrix-row-traceability`, `coverage-audit`, `star-audit`, `pace-audit`, `capability-mapping-check`, `snapshot-check`, `personal-context-discretion-check`; each SKILL.md + references where applicable; all de-personalised with `[Candidate Name]` / `[Candidate First Name]` / `[Workspace Folder Path]` placeholders); `Project_Instructions.md` (note at the top of Canonical files; new "Verification skills (v0.5.4 skill-based architecture)" section before STEP 5, with the full skill table, gate behaviours and run-mode guidance); `01_SETUP_ORCHESTRATOR.md` (new Phase 4 — populate, de-placeholder, package and install the skills; verify triggering); `Template_Changelog.md` (this entry; front-matter bumped to v0.5.4).
- **Mirrors live change:** live framework V5.0 → V5.4 — voice consolidation into a reference skill, three Wave 1 verification skills (advisory → gate after a two-week review), and the V5.4 Wave 2 + Wave 3 build-out completing all ten verification disciplines as skills.
- **Also fixed:** the v0.4.5 and v0.4.6 entries had been inserted inside the "Entry template" code fence rather than under `# Changelog`; both moved to their correct position (content unchanged).
- **Distribution:** the template package is now also published as the `executive-application-helper` GitHub repository (MIT licence). Structural changes mirrored here should also be committed to the repo working copy.
- **What a downstream user notices:** the package now ships enforcement, not just discipline — eleven installable skills, a setup phase that wires them, and a public repo to pull updates from.
- **Version-line re-alignment:** the template version now mirrors the live instructions version (`VX.Y` → `v0.X.Y`); this release is numbered **v0.5.4** to match instructions V5.4 (it would have been v0.5.0 under the old independent line). See the Versioning section for the rule.

### 2026-06-12 — PDF output disciplines for annotated prep documents added to the Interview Prep skeleton (v0.4.5 → v0.4.6)

- **Files touched (`_Template/`):** `Interview_Prep_Template.md` — new "PDF output for annotated prep documents" section added before "Maintenance and reuse"; `Template_Changelog.md` (this entry).
- **Type:** Minor (additive — one new section; no existing content changed, no ordering shift).
- **Change:** Documented three reusable PDF-output disciplines for prep documents converted via `pandoc --pdf-engine=xelatex`: (1) paired Markdown + PDF with reproducible YAML page geometry; (2) proportional pipe-table separator dashes (size columns by content, not equally); (3) landscape rotation for wide tables via raw-`{=latex}` blocks (a bare `\begin{landscape}` pair makes pandoc swallow the markdown table and the `#` header column breaks the build).
- **Rationale:** Mirrors Convention 17 (landscape rotation) and the existing proportional-dash discipline from the live framework, surfaced in a recruiter-screen-prep session where a wide five-column likely-questions table was rotated to landscape for easier annotation. The template previously carried no PDF-output guidance, so the section also folds in the paired-output and proportional-dash essentials to stand on its own.
- **What a downstream user notices:** the Interview Prep skeleton now tells them how to produce a clean, annotation-friendly PDF — including how to rotate a wide table to landscape without breaking the build.

### 2026-05-29 — Data-integrity & resilience disciplines section added to the Project Instructions skeleton (v0.4.4 → v0.4.5)

- **Type:** Major (new always-relevant disciplines section in the template's `Project_Instructions.md`).
- **Files touched (`_Template/`):** `Project_Instructions.md` (new "# Data-integrity and resilience disciplines" section inserted before STEP 5 — snapshot-before-structural-edit; `_resources/` retention + `*TRUNCATED*` quarantine + `RESTORE_INDEX.md`; rebuild-whole-never-in-place; three-axis integrity check at session close; changelog split/roll-over for the evidence-bank changelog (weekly) and the instructions changelog (by version)); `Template_Changelog.md` (this entry; `last_updated` bumped to v0.4.5).
- **Mirrors live change:** `Project_Instructions_V5.md` V5.1 → V5.2 (Convention 13 retention rule, Convention 14 scope-widening, Convention 15 applied to instructions/changelog files, Convention 16 extended to the instructions changelog) plus the rebuilt, scope-extended `bank-integrity-check` skill.
- **What a downstream user notices:** the template now ships with the full data-integrity discipline set, de-personalised — a new setup inherits the truncation-resilience guardrails without having to rediscover them through its own data-loss incident.
- **Rationale:** these disciplines were written across the live framework after repeated tail-truncations of large append-only files; they are the most transferable safety pattern in the framework and belong in every copy of it.

### 2026-05-29 — Changelog weekly-split + file-resilience discipline added to the Evidence Bank Changelog skeleton — v0.4.3 → v0.4.4

- **Type:** Minor (non-breaking addition to the `Evidence_Bank_Changelog.md` skeleton; safe to adopt incrementally; no change to setup flow or entry format).
- **Files touched:** `_Template/Evidence_Bank_Changelog.md` (new "File-size resilience — weekly split" section added after the intro).
- **Change:** Added a recommended discipline for keeping the changelog from truncating once it grows: live file holds the current ISO week only; completed weeks move to immutable `Archive/Evidence_Bank_Changelog_[Mon]_to_[Sun].md` files; roll-over at the first session of each new week; structural rebuilds done with a verbatim-slicing script rather than the in-place editor. Framed as "adopt once the live file exceeds a few hundred lines" so small setups stay simple.
- **Rationale:** Mirrors a live-framework change made the same day after the candidate's monolithic changelog repeatedly lost its tail to racing writes and in-place-editor truncation. Any downstream user whose changelog grows will hit the same failure mode, so the prevention belongs in the template.
- **Downstream user notices:** new guidance section in the changelog skeleton explaining when and how to split the log weekly; no action required until their own log grows large.

### 2026-05-19 — Duplicate-submission check section added between Mandatory gating step and Lightweight initiation protocol — v0.4.2 → v0.4.3

- **Type:** Minor (additive — new gating-style check inserted between the existing Mandatory gating step and the Lightweight initiation protocol; no change to existing rules; non-breaking for downstream users on v0.4.x).
- **Files touched in `_Template/`:**
  - **`Project_Instructions.md`** — new `## Duplicate-submission check` section inserted between `## Mandatory gating step before drafting` and `## Lightweight initiation protocol`; one-paragraph "Order of operations — strict" preface added to `## Lightweight initiation protocol`; one bullet added at top of `## Pre-drafting assessment` requiring the duplicate-check outcome be recorded.
  - **`Template_Changelog.md`** — this entry; front-matter `last_updated` refreshed to v0.4.3.
- **What a downstream user notices:** Claude (or the equivalent assistant) now runs a three-step duplicate-detection sequence (Glob `Submissions/`; Grep evidence-bank changelog; Grep evidence-bank master file) at the start of every new role kickoff. If a prior submission is detected at high confidence (same organisation + same/synonymous role title), Claude stops, surfaces the prior submission's date and file location, and asks the user to choose between four canonical options (Refresh / Re-send unchanged / Full fresh redraft / Stand down) before any framing or pack-fetch questions are asked. Medium-confidence near-matches are surfaced in the pre-drafting assessment as context without blocking. The check eliminates wasted-effort kickoffs when roles are reposted across platforms.
- **Rationale:** A live-framework user surfaced the gap when a Seek listing was reposted and they kicked off a fresh session without noticing the role had already been responded to six days earlier. The full retrieval-first protocol + clarifying-question round were run before the duplicate was detected mid-session. The fix is to add a check that runs before the Lightweight initiation protocol opens its single clarifying round. Reusable for any framework user — duplicate role advertisements across Seek / LinkedIn / recruiter sites are a common pattern.
- **Migration note for downstream users on v0.4.2:** Re-paste the updated `_Template/Project_Instructions.md` into your live project settings (or copy the new `## Duplicate-submission check` section, "Order of operations — strict" paragraph and Pre-drafting assessment bullet manually). No data migration required; no breaking changes to existing entries, files or templates.

### 2026-05-11 — STEP 4 changelog template reference generalised to point to the changelog's own self-documenting spec — v0.4.1 → v0.4.2

- **Type:** Minor (single-paragraph edit to template STEP 4 part 3; mirrors the live framework's V4.1 → V4.2 minor bump).
- **Files touched:**
  - **`_Template/Project_Instructions.md`** — STEP 4 part 3 rewritten. Removes the partial template reference; replaces with a description of what a disciplined evidence-bank changelog enforces (one entry per change; structured template with typical 8 fields; no reconstruction; no parking; explicit file/entry naming; reverse-chronological); points downstream users to make their own changelog self-documenting (rules + template + anti-patterns at the top of the file). Slightly generalised vs the live V4.2 wording — the template doesn't reference the live archive path (since downstream users won't have that archive); instead frames the self-documenting principle as a design recommendation.
- **Change:** Mirror the live framework's V4.2 minor bump into the template package. Generalises the language so downstream users adopting the template see the principle ("changelog should be self-documenting") rather than a copy-paste of Mikhail's specific 8-field template. Downstream users can adopt the same 8 fields, choose a smaller subset that suits their cadence, or extend with additional fields — the template gives the principle and the typical baseline.
- **Reason:** Mikhail 2026-05-11 promoted the live framework to V4.2 ("STEP 4 changelog template reference updated for disciplined 8-field template + self-documenting spec pointer + archive reference"). Per Step 5 (Template package maintenance), structural changes that benefit downstream users are mirrored into `_Template/` in the same session.
- **Downstream impact:** This is a **Minor** version bump (v0.4.1 → v0.4.2). The change is **fully additive** — existing setups using v0.4.1 continue to work without modification. To adopt v0.4.2, a downstream user re-pastes the updated template Project_Instructions.md into their live project config and (recommended) restructures their `Evidence_Bank_Changelog.md` to be self-documenting (codifying their entry template + maintenance rules at the top of the file). Without the self-documenting changelog, the instructions still work — Claude will use whatever entry format the downstream user chooses to apply.

### 2026-05-11 — Quick-start triggers section mirrored into template for mobile-friendly kickoff vocabulary — v0.4.0 → v0.4.1

- **Type:** Minor (additive — new section at top of `_Template/Project_Instructions.md` mirrored from live V4.1; no change to existing template workflow rules).
- **Files touched:**
  - **`_Template/Project_Instructions.md`** — Quick-start triggers section inserted as the first top-level section, above `## Role`. Three tables (application drafting kickoffs / interview prep kickoffs / cross-workflow and follow-up kickoffs) plus natural language alternatives and a disambiguation rule. All instances of `Mikhail` replaced with `[Candidate First Name]` placeholder; otherwise structurally identical to live V4.1.
- **Change:** Mirror the live framework's V4.0 → V4.1 minor bump into the template package. The Quick-start triggers vocabulary is a general-purpose kickoff pattern that benefits any downstream user of the template — drop URL alone = Cover Letter (default); drop URL + one keyword = named deliverable. Both workflows supported.
- **Reason:** Mikhail 2026-05-11 chose Option B (codify the trigger vocabulary in the project instructions). Per Step 5 (Template package maintenance), structural additions that benefit downstream users are mirrored into `_Template/` in the same session.
- **Downstream impact:** This is a **Minor** version bump (v0.4.0 → v0.4.1) and is **fully additive** — existing setups using v0.4.0 continue to work without modification. To adopt v0.4.1, a downstream user can either (a) re-paste the updated template Project_Instructions.md into their live project config, or (b) ignore the Quick-start triggers section entirely; in the latter case Claude will continue to handle kickoffs via the Lightweight initiation protocol, which already supports the same behaviour through auto-extract + AskUserQuestion rounds — the Quick-start triggers section is an optimisation, not a new mandatory rule.

### 2026-05-11 — Matrix-based retrieval flow mirrored into template; STEP 4 references updated to decision matrices — v0.3.0 → v0.4.0

- **Type:** Major (mirrors the live framework's V3.5 → V4.0 promotion: matrix-based retrieval flow + STAR interview prep workflow integration).
- **Files touched:**
  - **`_Template/Project_Instructions.md`** — `Mandatory retrieval-first protocol` rewritten for matrix flow. New 9-step sequence (was 6): load Master → identify role family → open matched family's Section 5 decision matrix → pattern-match brief against `Pattern` column → matched row delivers all attributes → extend with Section 4 master index as needed → cross-check Section 7 → load only companion files from row's `Companion` column → for interview prep load Interview Voice/Style + Template → cross-check Section 6. Section 5.8 cross-family hybrid awareness added. Maintenance discipline added (new patterns go directly into the appropriate matrix in the same session).
  - **`_Template/Project_Instructions.md`** — STEP 4 (Post-draft maintenance) references updated. "Section 5 (Role-family recipes)" → "Section 5 (role-family decision matrices, including any new matrix row)". "amend a role-family recipe reference if appropriate" → "amend the relevant matrix row (or add a new row) if appropriate".
- **Change:** Mirror the live framework's V4.0 retrieval-flow change into the template package. The matrix-based flow is a fundamentally different retrieval surface (matrix pattern-match instead of prose recipe scan) that any downstream user of the template should adopt when they set up Section 5 with decision matrices instead of prose recipes.
- **Reason:** Mikhail 2026-05-11 promoted the live framework to V4.0 ("STAR interview prep + matrix-based retrieval flow consolidated"). Per Step 5 (Template package maintenance), structural changes that benefit downstream users are mirrored into `_Template/` in the same session.
- **Downstream impact:** This is a **Major** version bump (v0.3.x → v0.4.0). The change is **structurally additive** for downstream users — existing setups using v0.3.x with prose recipes in Section 5 continue to work, but the template's `Mandatory retrieval-first protocol` now describes the matrix flow. Downstream users adopting v0.4.0 will need to: (a) restructure their Section 5 in `Examples_Master.md` from prose recipes into per-role-family decision matrices (with one row per archetype, columns for ID / Pattern / Tested with / Positioning / Body stacks / Template-Length / Fit-ack / AI register / Companion / Notes); (b) add a Section 5.8 for cross-family hybrid archetypes; (c) update their Section 0 Quick-start retrieval protocol to reflect the matrix flow. The `_Template/Examples_Master.md` skeleton itself has **not yet been updated** with example matrix structure — it still has the v0.3.x prose-recipe skeleton. **Pending follow-up** (deferred per the V4.0 changelog note): update `_Template/Examples_Master.md` to provide an example matrix structure (with placeholder rows and column legend) so downstream users have a clear pattern to follow.

### 2026-05-11 — STAR-style interview preparation added as a parallel workflow — v0.2.1 → v0.3.0

- **Type:** Major (two new canonical files; restructured Document types in `Project_Instructions.md`; Section 0 retrieval protocol in `Examples_Master.md` updated for dual workflow).
- **Files touched:**
  - **`_Template/Interview_Voice_and_Style_Guide.md`** (new) — spoken-delivery style guide skeleton. Part 1 prompts the candidate to mirror Voice principles from the Writing Voice guide with explicit calibration for the interview room. Part 2 captures the generic style adjustments for spoken delivery (sentence length, pacing at ~140–160 wpm, pause discipline with explicit markers, em-dashes as audible pauses, three-beat structure compressed inside STAR). Includes word-count targets by interview format and STAR component, tone-by-format guidance for three interview formats, and common-question-type approach guidance. Most structural content is generic and can stay as-is for downstream users; the candidate-specific work is in Part 1 (voice principles) and the placeholder name in the title.
  - **`_Template/Interview_Prep_Template.md`** (new) — canonical eight-section structure for prep documents (front-matter, executive summary, opening script, likely questions table, pre-prepared STAR responses, practicalities cheat sheet, candidate questions, sources). Each section documented with purpose, required components, format and example. Includes STAR word-count targets per interview format, honest-framing variation for lived-experience or hard-gap questions, format-specific section-emphasis variations (recruiter screen / behavioural panel / executive panel), and maintenance/reuse guidance. Almost entirely generic — placeholder name in the title plus `[Workspace Folder Path]` in the output-location convention.
  - **`_Template/Project_Instructions.md`** — `Document types` section restructured into two named workflows: *Application drafting* (existing five document types) and *Interview preparation* (three new formats: recruiter screen, behavioural panel, executive panel). New section explicitly notes that interview prep bypasses STEPs 2–3 but retains STEP 4-equivalent post-prep maintenance. New output-naming convention and output-location convention codified. `Canonical files and loading rules` table extended with two new rows for the new files; existing `Writing_Voice_and_Style_Guide.md` row updated to clarify it loads for interview prep too. `Examples_Master.md` row note added that the bank serves both workflows.
  - **`_Template/Examples_Master.md`** — Section 0 (Quick-start retrieval protocol) updated to note the dual workflow at the top. New Step 8 added to the protocol: "For interview prep, also load `Interview_Voice_and_Style_Guide.md` and `Interview_Prep_Template.md`." Closing paragraph extended to note that both workflows feed back into the same evidence-bank changelog.
- **Change:** Codify STAR-style interview preparation as a formal supported workflow alongside application drafting in the template package. The candidate framework has been used for interview prep in practice; this brings the template package up to match.
- **Reason:** The live framework was extended on 2026-05-11 to formalise interview-prep as a documented workflow. Two new canonical files (`Mike_Dudarenok_Interview_Voice_and_Style_Guide.md` and `Mike_Dudarenok_Interview_Prep_Template.md`) were created in the live workspace, the live `Project_Instructions_Updated_V3.md` was restructured to register the new workflow, and the live `Examples_Master.md` Section 0 was updated to note the dual retrieval protocol. The same structural changes are mirrored into `_Template/` here so the package stays useful for future setups.
- **Downstream impact:** This is a **Major** version bump (v0.2.x → v0.3.0) but the change is **additive** rather than breaking. Existing setups using the template continue to work for application drafting without modification. To adopt interview-prep support, a downstream user needs to: (a) copy the two new template files into their workspace and personalise the title/name placeholders, (b) apply the Document types restructure and Canonical files extension to their own `Project_Instructions.md` (and paste the updated version into their Cowork project config), and (c) apply the Section 0 update to their `Examples_Master.md`. The evidence bank itself does not need any changes — the same entries serve both workflows. The Setup Orchestrator (`_Template/01_SETUP_ORCHESTRATOR.md`) should be updated in a follow-up pass to walk new users through interview-prep setup; that update is deferred until the live workflow has been tested across multiple interview formats.

### 2026-05-08 — Seek screening-question 1,000-character per-question hard limit codified — v0.2.0 → v0.2.1

- **Type:** Minor (refinement to existing length rule; no new section, no scope change).
- **Files touched:** `_Template/Project_Instructions.md` — Lightweight initiation protocol's auto-extract list extended with a Seek-specific signal item that surfaces screening questions as a deliverable; STEP 1 — Draft the application document → Length section extended with the new Seek screening-question rule (1,000 characters maximum per question, plain-text formatting, per-answer character-count verification before delivery, trimming approach when an answer needs more than 1,000 characters of evidence, and the `[Candidate Name] - [Title] - [Company Name] - Screening Questions.md` filename convention in `[Workspace Folder Path]/Submissions/`).
- **Change:** Codify the Seek apply-flow's hard 1,000-character per-screening-question limit as a permanent length rule in the template package, applied to every Seek-advertised role automatically, regardless of whether the brief restates the limit. Mirrors an equivalent change made to the live framework (V3.3 → V3.4) on the same date.
- **Reason:** Mirrors a structural refinement made to the live framework on 2026-05-08 after the first Seek-advertised role in the bank that surfaced screening questions (INIT Group Australia Managing Director cover letter session) was drafted without the limit applied — initial answers ranged 1,015 to 1,758 characters and required a re-trim pass. The limit is a Seek platform constraint rather than a per-role one, so codifying it once in the template package prevents the correction loop on every future Seek role for any downstream user.
- **Downstream impact:** Non-breaking. Existing template users adopting v0.2.1 will produce Seek-compliant screening-question deliverables by default the first time a Seek brief is run. Setup populations from earlier template versions can adopt the change in-flight by appending the new Seek-specific bullet to the auto-extract list and the new Seek length-rule bullet to the Length section per the live diff. Patch-style version bump to **v0.2.1** because this is a behavioural refinement to existing wording (length rule) rather than a structural addition.

### 2026-04-28 — Lightweight initiation protocol added; Rule 1 clarified — v0.1.1 → v0.2.0

- **Type:** Major (new section, new rule, change to gating logic)
- **Files touched:** `_Template/Project_Instructions.md` — Rule 1 of the Mandatory gating step amended; new "Lightweight initiation protocol" section inserted between Mandatory gating step and Pre-drafting assessment, with three sub-sections (auto-extract / ask-only / batching rule; Defaults when fields are unstated; How to ask).
- **Change:** Codified a lightweight kickoff path so a candidate can initiate a session by dropping a single URL or attachment with no other framing. The new section instructs the assistant to (a) auto-extract everything inferable from the materials before asking anything, (b) ask only what genuinely cannot be inferred, (c) batch all clarifying questions into a single multi-choice prompt, and (d) cap clarifying rounds at one — any subsequent evidence gaps that surface during drafting are captured as next-step items in the post-draft maintenance report, not as another mid-session question round. A defaults block locks in document type (Cover Letter), length (per Step 1 defaults), tone (executive, per the Style Guide), output format (`.docx` from the configured Word template, saved to `Submissions/`), and spelling (as configured in the Style Guide). Rule 1 amended to make explicit that a single URL or single attachment is sufficient to clear the gate.
- **Reason:** Mirrors a structural change made to the live framework on 2026-04-28 (V3.2 → V3.3). The candidate asked to make session kickoff as lightweight as possible — ideally a one-link or one-attachment drop — to enable initiation from mobile without typing a full prompt. Codifying the path makes the lightweight kickoff reliable rather than dependent on the assistant's own judgement.
- **Downstream impact:** Non-breaking. Existing template users adopting v0.2.0 will get mobile-friendly kickoff behaviour by default — bare URL or attachment drops will resolve to a clean drafting path with one round of multi-choice taps. Setup populations from earlier template versions can adopt the change in-flight by appending the new "Lightweight initiation protocol" section to their `Project_Instructions.md` and amending Rule 1 per the live diff. Minor version bumped to **v0.2.0** because this is a structural addition (new section, new rule) rather than a refinement to existing wording.

### 2026-04-28 — STEP 3 presentation format — one mini-table per suggestion — v0.1.0 → v0.1.1

- **Type:** Minor
- **Files touched:** `_Template/Project_Instructions.md` (STEP 3 — Resume tailoring recommendations: new "Presentation format — one mini-table per suggestion" sub-section appended).
- **Change:** Added explicit instruction that each resume suggestion must be presented as its own labelled subsection (`### Suggested change N — [topic]`) followed by a two-column `Field` / `Content` mini-table with four rows (Current wording, Proposed wording, Reason for change, Likely benefit). Replaces the previous implicit format where multiple suggestions could be presented as rows in a single combined table. Also requires bold highlighting of new/strengthened language inside Proposed wording, and a closing one-line judgement on whether a full rewrite is warranted.
- **Reason:** Mirrors a structural refinement made to the live framework after candidate feedback during the KBR Senior Manager IT cover-letter session, 2026-04-28. The per-suggestion mini-table format proved materially easier to scan than the combined-table format, especially when proposed wording ran to several sentences.
- **Downstream impact:** Non-breaking. Existing template users adopting v0.1.1 will produce more skim-friendly Step 3 outputs by default. No migration required for in-flight setups; the change applies the next time Step 3 is run.

### 2026-04-28 — Initial template extraction — v0.1.0

- **Type:** Major
- **Files touched:** All files in `_Template/`:
  - `00_README.md` — entry point and setup overview
  - `01_SETUP_ORCHESTRATOR.md` — paste-in prompt for Claude-guided population
  - `02_HOW_TO_USE_AFTER_SETUP.md` — operating notes post-setup
  - `Project_Instructions.md` — de-personalised V3.1 of the live operating instructions, with `[Candidate Name]`, `[Candidate First Name]`, `[Workspace Folder Path]` and `[Word Template Filename]` placeholders
  - `Writing_Voice_and_Style_Guide.md` — skeleton with structural commentary; eight Voice and eight Style principle slots; brevity-mode optional Part 3
  - `Resume.md` — section-headed skeleton with prompts for what each section should contain
  - `Examples_Master.md` — full-structure skeleton; Sections 0–7 preserved; Section 4 master index, Section 5 role-family recipes, Section 6 signature metrics and Section 7 watch-outs are empty stubs
  - `Examples_Section_A_Positioning.md` — skeleton with structural guidance for A1–A12 positioning blocks
  - `Examples_Section_B1.md` to `Examples_Section_B6.md` — six capability-domain skeletons with default headings and renaming guidance
  - `Examples_Section_C_Templates.md` — C1–C6 templates with structural prose preserved and worked-exemplar slots marked as "to be populated"
  - `Examples_Section_D_E_Personal_Maintenance.md` — D1 personal-content skeleton; E1–E3 maintenance notes (largely portable verbatim)
*[Integrity note — 2026-05-29: the tail of this 2026-04-28 "Initial template extraction — v0.1.0" entry (the final file-list bullet(s) and the entry's Type/Change/Reason closing) was lost to a file truncation surfaced during the v0.4.4 session. Not recoverable from backup (no git, no snapshot). The file list above is substantially complete. Logged per Convention 15 — structural edits use a Python rebuild, not the in-place editor.]*

---
