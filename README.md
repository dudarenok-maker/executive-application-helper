# Executive Application Helper

A complete, battle-tested framework for running senior-executive job applications and interview preparation as a Claude project — with an evidence bank, matrix-based retrieval, verification skills that gate quality mechanically, and data-integrity disciplines earned the hard way.

Built and iterated across months of real executive applications (CIO / CTO / COO / CDO / SES and equivalent roles). Every rule in this framework exists because something went wrong without it.

## What it does

**Two workflows, one evidence base:**

- **Application drafting** — drop a job URL or attachment into a Claude project and get a tailored cover letter, statement of claims, pitch, or selection-criteria response in the candidate's own voice, built from a structured evidence bank, gated by length and overclaim checks before delivery.
- **Interview preparation** — recruiter screens, behavioural panels, and executive panels: eight-section prep documents with STAR responses written for spoken delivery, honest timing audits at the candidate's real speaking pace, and capability mapping for framework-scored (e.g. APS SES) panels.

**The machinery underneath:**

- **Evidence bank** — a structured, tagged library of the candidate's proof points, positioning blocks, and ready-made templates, with a master index and per-role-family decision matrices that prescribe exactly which evidence stack fits which role archetype.
- **Eleven verification skills** (`skills/`) — mechanical pass/fail gates for overclaim (watch-outs sweep), length and platform character limits, matrix-row traceability, coverage analysis, STAR structure, speaking pace, capability mapping, pre-edit snapshots, file integrity, and personal-context privacy boundaries.
- **Data-integrity disciplines** — snapshot-before-edit, three-axis integrity checks, changelog splitting, and quarantine rules that keep a long-running, append-heavy workspace from silently corrupting.

## Quick start

1. **Clone or download** this repository.
2. **Copy the `template/` folder** into a fresh folder on your machine — this becomes your workspace.
3. **Open a Cowork session** (Claude desktop) pointed at that folder and paste the contents of `template/01_SETUP_ORCHESTRATOR.md` into the chat. Claude walks you through four setup phases: foundations, voice and style, evidence bank, and skill installation.
4. **Paste the populated `template/Project_Instructions.md`** into your Claude project's instructions field.
5. Drop a job ad URL into the project. That's it — the default action is a tailored cover letter.

## Repository layout

| Path | What it is |
|---|---|
| `template/` | The de-personalised framework: project instructions, setup orchestrator, evidence-bank skeletons, voice-guide templates, changelog scaffolds |
| `template/skills/` | Eleven de-personalised skill skeletons (SKILL.md + references) — populate, package as `.skill`, and install per Setup Phase 4 |
| `template/Template_Changelog.md` | Version history of the framework package (current: v0.5.0) |
| `LICENSE` | MIT |
| `CONTRIBUTING.md` | How to propose improvements |

## Requirements

- Claude desktop app with Cowork mode (for setup and file-producing sessions), or any Claude project for drafting-only use.
- For PDF interview-prep output: `pandoc` with `xelatex` (optional — Markdown output works without it).

## Design principles

1. **Evidence before prose.** Nothing is claimed that the bank can't support; the watch-outs register records every framing that once went too far.
2. **Ordering is sacred.** Duplicate-check → gating → initiation → drafting → verification → maintenance. Skills implement content; the project instructions own the sequence.
3. **Gates, not vibes.** The checks most often skipped under pressure are the ones enforced mechanically.
4. **Everything leaves a trail.** Changelogs for the bank, the instructions, and the template itself; snapshots before structural edits; integrity checks before close.

## Provenance and licence

Extracted and de-personalised from a live framework maintained by Mikhail Dudarenok. MIT licence — use it, adapt it, ship your own version. Attribution appreciated, not required.
