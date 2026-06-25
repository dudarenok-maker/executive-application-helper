# Snapshot and retention rules — canonical reference (rev 2026-06-12, codifies the framework Convention 13)

## Naming convention

`[Original_filename]_backup_YYYY-MM-DD_pre-{short-descriptor}.md`

- `{short-descriptor}` is kebab-case and names the structural change ahead (e.g. `pre-section7-reconstruction`, `pre-matrix-row-cartology`, `pre-entry-format-shift`).
- The snapshot is a **verbatim copy** — same content, dated filename. It is the rollback point if the edit truncates the file, corrupts structure, or fails a Convention 14 integrity check.

## What requires a snapshot

Structural changes only: new/moved matrix rows; entry-format changes; restructures of the master index, any Section 5.x matrix, Section 6, Section 7, or `Examples_Master.md`; restructures of `Project_Instructions_V*.md` or either changelog; any multi-edit Python script across the bank.

Exempt: single proof-point amendments, tag tweaks, changelog appends, prose copy-edits inside an existing entry.

## Retention discipline 

- Keep at most the **three most-recent good backups per base file** in the `_resources/` root.
- Move older good backups to `_resources/_archive/`.
- Move any truncated backup to `_resources/_quarantine/` — a `*TRUNCATED*` file must **never** be a restore source.
- `_resources/RESTORE_INDEX.md` names the known-good latest backup per base file. Keep it current whenever backups are added, archived or quarantined: the newest backup *by timestamp* is not necessarily the newest *good* one (a truncated snapshot taken just before an incident is newer but unusable).

## Quick mechanical check (bash)

```bash
cd "[workspace]/_resources"
# snapshots for today's touched files
ls *backup_$(date +%F)* 2>/dev/null
# byte-identical check (run per file before the edit)
cmp "../[file]" "[file]_backup_$(date +%F)_pre-[descriptor].md" && echo GOOD
# retention: count backups per base file in root (should be ≤3)
ls *backup* | sed 's/_backup_.*//' | sort | uniq -c
```

## Gate behaviour

This skill is a **blocking gate** (advisory mode does not apply — Convention 13/14 failures are always actionable). Resolution is in-session and cheap: take the snapshot, fix retention, update the index, re-run.
