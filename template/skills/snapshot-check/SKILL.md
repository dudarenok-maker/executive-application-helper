---
name: snapshot-check
description: "Verify — BEFORE any structural edit to the candidate's evidence-bank, project-instructions or changelog files — that a Convention 13 pre-edit snapshot exists in _resources/ under the dated naming convention, and that the _resources/ retention discipline (keep 3 most-recent good backups, _archive/ for older, _quarantine/ for truncated, RESTORE_INDEX.md current) holds. Use this skill at the START of any session step that will add or move a matrix row, change entry format, restructure a Section file or Examples_Master.md, restructure Project_Instructions_V*.md or either changelog, or run a multi-edit Python script across the bank. Also use when [Candidate First Name] says 'check the snapshots', 'is there a backup', or 'verify the restore index'. This is a blocking gate, not advisory: a structural edit without a pre-edit snapshot is unrecoverable if it truncates."
---

# Snapshot Check — Convention 13 pre-edit gate skill

Codifies Convention 13 (pre-major-edit snapshot + retention rule) of `Project_Instructions.md` (rev 2026-06-12). Wave 3 verification skill of the framework.

The 2026-05-28 Section 7 reconstruction recovered from a 2026-05-11 backup only because that backup happened to exist. This gate makes the snapshot a checked precondition rather than a remembered discipline. **It blocks the edit if the snapshot is missing.**

---

## When to invoke

**Before** any session step that will:

- (a) add or move a matrix row in any `Examples_Section_5_*.md` file;
- (b) modify the entry format used in any A / B / C / D section file;
- (c) restructure `Examples_Section_4_Master_Index.md`, any `Examples_Section_5_*.md`, `Examples_Section_6_Signature_Metrics.md`, `Examples_Section_7_Watchouts.md` or `Examples_Master.md`;
- (d) restructure `Project_Instructions_V*.md` or either changelog (Convention 15 scope);
- (e) apply a multi-edit Python script across the bank.

**Trivial edits are exempt** — single proof-point amendment, single tag tweak, changelog appends, prose copy-edits inside an existing entry.

## Checks — run all four

Load `references/snapshot-rules.md`, then:

1. **Snapshot exists.** For every file about to be edited, a same-day snapshot exists in `_resources/` named `[Original_filename]_backup_YYYY-MM-DD_pre-{kebab-descriptor}.md` and its descriptor names *this* structural change. If missing → **STOP: take the snapshot now, then proceed.** (The fix is one `cp`; the gate exists so it cannot be skipped, not to create ceremony.)
2. **Snapshot is good.** The snapshot is byte-identical to the current file (verbatim copy taken before any edit). A snapshot shorter than the live file is itself suspect — quarantine and retake.
3. **Retention discipline holds** for the touched base files: at most the 3 most-recent good backups in `_resources/` root; older in `_resources/_archive/`; any `*TRUNCATED*` file in `_resources/_quarantine/` (never a restore source).
4. **`RESTORE_INDEX.md` is current** — it names the known-good latest backup for every touched base file. The newest backup *by timestamp* is not necessarily the newest *good* one.

## Output format

A per-file table (file / snapshot found / good / retention OK / index OK), then verdict: **Proceed** or **Blocked — [action]**. Blocked is resolved in-session (take snapshot, fix retention, update index), then re-run.
