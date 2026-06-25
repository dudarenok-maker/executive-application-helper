---
name: bank-integrity-check
description: "Run a three-axis integrity check on the framework's evidence-bank files at the end of any session that touched the bank — Examples_Master.md, the Section 4/5/6/7 files, any Examples_Section_A/B/C/D companion file — plus the append-only files that actually truncate in practice: both changelogs (evidence-bank changelog + current weekly archive, instructions changelog) and the Project_Instructions file. Use at post-draft maintenance (STEP 4) before the maintenance report, OR when the candidate says 'check the bank', 'integrity check', or 'make sure I didn't break anything'. Mechanical (~30–60 sec via bash + grep); catches three failure modes that otherwise go undetected for weeks: end-of-file truncation, cross-reference breakage, and silent line-count drops."
---

# Bank Integrity Check — three-axis verification skill

> **Setup note:** This is a template skeleton. `references/check-script.sh` carries the mechanical check — set the workspace path at the top. The check codifies the framework's Convention 14 (integrity check before session close) and pairs with Convention 13 (pre-edit snapshots in `_resources/`).

## When to invoke

- **Default trigger:** at the end of STEP 4 if any evidence-bank file was modified this session — before producing the maintenance report.
- **Explicit triggers:** "check the bank", "integrity check", "verify the bank", "make sure I didn't break anything".
- Not needed when no bank file was touched.

## The three axes

1. **End-of-file integrity.** Every touched file ends with `---` after its terminal section — not mid-row, mid-cell or mid-paragraph. Scope: `Examples_*.md`, both changelogs, the current weekly changelog archive. (The Project_Instructions file is checked by line count but not EOF — it ends with prose.)
2. **Cross-reference integrity.** Every Section 7.1.x sub-variant named in any matrix-row `Notes / Distinct from` column exists as a heading in `Examples_Section_7_Watchouts.md`.
3. **Line-count sanity.** No touched file is non-trivially shorter than its most recent good backup in `_resources/` (a drop of more than ~50 lines without a deliberate restructure signals truncation). Ignore `*TRUNCATED*` backups when choosing the comparison anchor.

## On failure

**Halt the session close.** Restore from the latest good pre-edit snapshot in `_resources/` (per the snapshot-check skill and `RESTORE_INDEX.md`), re-apply the intended change, re-run. Integrity failures are always actionable — advisory mode does not apply to this skill.

## Coherence caveat — a PASS can reflect a STALE view (discipline D6)

This script reads through the shell. If the workspace is a mounted or synced folder, a file changed by the host-side editor tools may not be coherently visible to a shell read, so the shell can serve a **stale, wrong-length** view. A PASS therefore means only that the *shell view* is intact — not the host file. **Always pair a PASS with a file-tool (Read) cross-check** of the changelog tail. The bundled script prints an **Axis 0 (advisory) stability probe** first (two reads 1 s apart); it catches in-flux staleness but **not** a steadily-stale cache — only the cross-tool check does.

## Output

Per-file, per-axis table (pass/fail with detail), then verdict: **all-pass** or **HALT — restore from [named snapshot]**. Include the output in the STEP 4 maintenance report.
