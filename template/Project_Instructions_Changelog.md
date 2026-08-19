---
title: Project Instructions Changelog
owner: [Candidate Name]
paired_files: Project_Instructions.md
format: Reverse-chronological. Most recent entries at the top.
last_updated: [YYYY-MM-DD]
---

# Project Instructions Changelog

Authoritative change history for the Cowork project instructions used in the Executive Application Helper framework. Every update to the live instructions must be paired with an entry here in the same session. This file sits alongside `Evidence_Bank_Changelog.md`, which tracks changes to the evidence bank.

## How to use this log

- One entry per change, in reverse-chronological order (newest first).
- Each entry must capture: date, version transition, sections touched, type of change, rationale, and outcome where measurable.
- Group sub-changes under a single date heading when they were made in one session.
- Do not rewrite history. If an earlier entry is found to be incorrect, add a new entry referring back to it rather than editing the original.

## Change types

- **Major** — structural or scope change (new rule, new workflow, new canonical file).
- **Minor** — behavioural refinement or additional guidance within an existing rule.
- **Editorial** — tightening, deduplication or formatting change with no behavioural impact.

## Entry template

Entries are **2–4 lines: what changed, and why.** Rationale and session narrative live in the commit message — this file is an index of changes, not a record of reasoning.

```
### YYYY-MM-DD — [short descriptor] — [VX.Y → VX.Z]
- **Change:** [What changed in the instructions.]
- **Why:** [What triggered it.]
- **Commit:** [hash]
```

On any version change, do exactly two things: update the single **Current version** line in `Project_Instructions.md`, and append an entry here. Never accumulate per-version banners in the instructions file itself — history belongs in this log and in git.

---

# Changelog

> **Setup note:** The first entry is typically the initial setup of the framework — recording the date, the source template version used, the populated files and any gaps. Append future entries newest-first.

