---
title: Evidence Bank Changelog
owner: [Candidate Name]
paired_files: Examples_Master.md; Examples_Section_A_Positioning.md; Examples_Section_B1.md; Examples_Section_B2.md; Examples_Section_B3.md; Examples_Section_B4.md; Examples_Section_B5.md; Examples_Section_B6.md; Examples_Section_C_Templates.md; Examples_Section_D_E_Personal_Maintenance.md
format: Reverse-chronological. Most recent entries at the top.
last_updated: [YYYY-MM-DD]
---

# Evidence Bank Changelog

This file is the authoritative change history for the evidence bank. The bank is split across `Examples_Master.md` (the operating layer) and the companion section files (the entry bodies). Every update to any of those files must be paired with an entry here in the same session. If no changelog entry is added, the change is considered draft only.

## File-size resilience — weekly split (recommended once the log grows)

A single long, frequently-appended changelog is vulnerable to **tail-truncation** — from racing writes (more than one session touching it) or from in-place-editor partial writes. To bound the damage, keep this live file small:

- **Live file holds the current ISO week only** (Monday–Sunday), plus a short "Archived changelog files" index in the frontmatter mapping each past period to its archive file.
- **Completed weeks move to immutable archives** named `Archive/Evidence_Bank_Changelog_[YYYY-MM-DD-Mon]_to_[YYYY-MM-DD-Sun].md`. Never append to an archive.
- **Roll-over trigger:** at the first session of a new ISO week, before appending the new entry, move the previous week's entries into a new dated archive file, add a row to the index, then append to the now-empty current week.
- **Always rebuild structurally with a script that slices existing text verbatim**, not the in-place editor — the in-place editor is the most common cause of silent tail-truncation.

Adopt this once the live file exceeds a few hundred lines; below that, a single file is fine.

## How to use this log

- One entry per change, in reverse-chronological order (newest first).
- Each entry must capture: date, section(s) touched, type of change, rationale, and source.
- Group sub-changes under a single date heading when they were made in one session.
- Do not rewrite history. If an earlier entry is found to be incorrect, add a new entry referring back to it rather than editing the original.

## Change types

- **Add** — new entry, new section, or new template.
- **Amend** — existing entry strengthened, reframed, retagged, or re-tiered.
- **Retire** — entry removed from active use (kept here for audit, flagged as retired in the source file or excised entirely).
- **Source update** — new proof point, metric or evidence added to an existing entry.
- **Tag update** — role-family, capability, sector or anchor-org tag corrected or extended.
- **Cross-reference update** — "See also" links adjusted.

## Staleness triggers

Rebuild or amend an entry when any of the following apply:

- Role context changes materially (new role, expanded remit, change in seniority).
- A proof point is now more than 24 months old without refresh.
- A metric is superseded by a stronger figure.
- An application cycle reveals that an existing example under-delivered or read weakly against role requirements.
- A new organisation enters the anchor set.

## Entry template

```
### YYYY-MM-DD — [short descriptor of the change]

- **Type:** Add / Amend / Retire / Source update / Tag update / Cross-reference update
- **Section(s) touched:** [file + entry ID, e.g. `Examples_Section_B4.md` — B4-2]
- **Change:** [one or two sentences on what changed; point to the entry for the content rather than restating it]
- **Reason:** [what triggered the change — a role, an application cycle, or one of the staleness triggers above]
- **Source:** [where the new evidence or framing came from]
```

*[Integrity note — 2026-05-29: this "Entry template" block was reconstructed after an in-place-editor truncation lost the original during the v0.4.4 session; the field set was inferred from the "Change types" list above and the live `Evidence_Bank_Changelog.md` template. The "Staleness triggers" section above it was restored verbatim from a pre-truncation read. Logged per Convention 15 — structural edits must use a Python rebuild, not the in-place editor.]*

---
