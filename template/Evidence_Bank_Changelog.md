---
title: Evidence Bank Changelog
owner: [Candidate Name]
paired_files: Examples_Master.md; Examples_Section_A_Positioning.md; Examples_Section_B1.md; Examples_Section_B2.md; Examples_Section_B3.md; Examples_Section_B4.md; Examples_Section_B5.md; Examples_Section_B6.md; Examples_Section_C_Templates.md; Examples_Section_D_E_Personal_Maintenance.md
format: Reverse-chronological. Most recent entries at the top.
last_updated: [YYYY-MM-DD]
---

# Evidence Bank Changelog

This file is the authoritative change history for the evidence bank. The bank is split across `Examples_Master.md` (the operating layer) and the companion section files (the entry bodies). Every update to any of those files must be paired with an entry here in the same session. If no changelog entry is added, the change is considered draft only.

## Integrity model — git, not weekly splits

Earlier versions of this framework split this file weekly into dated archives, on the theory that a smaller live file limits the damage from a racing or partial write. **That is retired.** The workspace is a git repository; every state of this file since the baseline commit is recoverable with `git checkout`, which is strictly better than an archive folder and requires no discipline to maintain.

What replaced it:

- **Commit at every session close** that touched this file. The commit message carries **what changed and why** — the narrative that entries used to carry.
- **Entries are 2–4 lines.** One per discrete change, newest first. If an entry is running long, the extra material belongs in the commit message.
- **Rebuild structurally with a script that slices existing text verbatim**, and write the whole file — never edit a long append-only file in place. This one rule survived the move to git, because it prevents the damage rather than recovering from it.
- **Where the workspace is a mounted or synced folder**, read this file with the file/editor tool and write it only from the shell, cross-checking size and last line before any rewrite. The shell can serve a stale view of a host-side write, and writing that view back truncates the file. This is the failure mode that motivated the weekly split in the first place; git recovers from it, and the read/write discipline prevents it.

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

Entries are **2–4 lines: what changed, and why.** Session narrative lives in the commit message, not here — a changelog that reconstructs the session is a changelog nobody re-reads.

```
### YYYY-MM-DD — [short descriptor]
- **Change:** [What changed — file + entry ID, e.g. `Examples_Section_B4.md` B4-2 re-tiered to Primary.]
- **Why:** [What triggered it — a role, a gate finding, a staleness trigger.]
- **Commit:** [hash]
```

Longer form is available where a change genuinely needs it (a restructure, a retirement with consequences), but it is the exception. The test: if a future reader would understand the change from the entry plus `git show <hash>`, the entry is long enough.

*[Integrity note — 2026-05-29: this "Entry template" block was reconstructed after an in-place-editor truncation lost the original during the v0.4.4 session; the field set was inferred from the "Change types" list above and the live `Evidence_Bank_Changelog.md` template. The "Staleness triggers" section above it was restored verbatim from a pre-truncation read. Logged per Convention 15 — structural edits must use a Python rebuild, not the in-place editor.]*

---
