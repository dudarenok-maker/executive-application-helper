#!/usr/bin/env bash
#
# Bank integrity check - EXTENDED scope (V5 Convention 14, scope-extension 2026-05-29)
#
# Canonical, scope-extended source for the bank-integrity-check skill. The installed
# skill dir is read-only from the Cowork session, so this staged copy is what should be
# folded into the skill package's references/check-script.sh on next reinstall. Until
# then, run it manually:
#
#   bash _resources/bank-integrity-check_extended_2026-05-29.sh "/path/to/[Workspace Folder Path]"
#
# What changed vs the installed v1 (V5.0):
#   - Axis 1 (EOF) now also covers the two changelogs and the current weekly
#     Evidence_Bank_Changelog archive. Project_Instructions_V*.md is NOT in the EOF
#     axis (it ends with prose, not the --- separator).
#   - Axis 3 (line-count) now also covers the two changelogs (already covered V*).
#   - Axis 3 reads only the _resources root and ignores *TRUNCATED* backups.
#
# Exit codes: 0 all pass / 1 EOF / 2 cross-ref / 3 line-count / 4 multiple / 99 bad dir

set -uo pipefail

# *** Discipline D6 — COHERENCE CAVEAT ***
#   This script reads through the shell. If the workspace is a mounted or synced folder,
#   a file changed by the host-side editor tools may not be coherently visible to a shell
#   read — the shell can serve a STALE, wrong-length view. A PASS here means only that the
#   *shell view* is intact. Always pair with a file-tool (Read) cross-check of the changelog
#   tail. The Axis 0 probe below catches in-flux staleness but NOT a steadily-stale cache.
#
BANK_DIR="${1:-$HOME/[Workspace Folder Path]}"
RESOURCES_DIR="$BANK_DIR/_resources"

if [ ! -d "$BANK_DIR" ]; then
  echo "ERROR: BANK_DIR does not exist."
  exit 99
fi

axis1_fail=0; axis2_fail=0; axis3_fail=0

echo "=== Bank integrity check (V5 Convention 14 - EXTENDED 2026-05-29) ==="
echo "Bank dir: $BANK_DIR"
echo
echo "--- Axis 0 (advisory): mounted-folder stability probe (discipline D6) ---"
cl="$BANK_DIR/Evidence_Bank_Changelog.md"
if [ -f "$cl" ]; then
  h1=$(sha256sum "$cl" | cut -d" " -f1); sleep 1; h2=$(sha256sum "$cl" | cut -d" " -f1)
  if [ "$h1" = "$h2" ]; then echo "STABLE across two reads 1s apart (sha $h1)."; 
  else echo "*** UNSTABLE — folder cache in flux; do NOT write the file back. Re-read via the file (Read) tool. ***"; fi
  tail -c 5 "$cl" | grep -q -- "---" && echo "changelog EOF: ends ---" || echo "*** changelog EOF: NOT ending in --- ***"
fi
echo "REMINDER: a PASS = shell view intact; cross-check the changelog tail with the file (Read) tool (D6)."
echo

# EOF axis extra files: changelogs + current weekly archive (NOT V*, which ends in prose)
EOF_EXTRA=()
for f in "$BANK_DIR"/Project_Instructions_Changelog.md "$BANK_DIR"/Evidence_Bank_Changelog.md; do
  [ -e "$f" ] && EOF_EXTRA+=("$f")
done
latest_weekly=$(ls -1 "$BANK_DIR"/Archive/Evidence_Bank_Changelog_20*_to_*.md 2>/dev/null | sort | tail -1)
[ -n "$latest_weekly" ] && EOF_EXTRA+=("$latest_weekly")

echo "--- Axis 1: End-of-file integrity ---"
for f in "$BANK_DIR"/Examples_*.md "${EOF_EXTRA[@]}"; do
  [ -e "$f" ] || continue
  last_nonempty=$(awk 'NF' "$f" | tail -1)
  if [ "$last_nonempty" != "---" ]; then
    echo "FAIL: $(basename "$f")"
    awk 'NF' "$f" | tail -3 | sed 's/^/    /'
    axis1_fail=1
  fi
done
[ "$axis1_fail" -eq 0 ] && echo "PASS - all checked files end with ---."
echo

echo "--- Axis 2: Cross-reference integrity ---"
S7_FILE="$BANK_DIR/Examples_Section_7_Watchouts.md"
if [ ! -e "$S7_FILE" ]; then
  echo "FAIL: Section 7 file not found."; axis2_fail=1
else
  mapfile -t refs < <(grep -hoE 'Section 7\.1\.[0-9]+' "$BANK_DIR"/Examples_Section_5_*.md 2>/dev/null | sort -u)
  for ref in "${refs[@]}"; do
    stripped="${ref#Section }"
    if ! grep -qE "^#{2,4} (Section )?${stripped}([^0-9]|$)" "$S7_FILE"; then
      echo "FAIL: $ref referenced in matrix files but missing as a heading in Section 7."; axis2_fail=1
    fi
  done
  [ "$axis2_fail" -eq 0 ] && [ "${#refs[@]}" -gt 0 ] && echo "PASS - all ${#refs[@]} Section 7.1.x references resolve."
fi
echo

echo "--- Axis 3: Line-count sanity ---"
if [ ! -d "$RESOURCES_DIR" ]; then
  echo "SKIP - no _resources/."
else
  any_suspect=0
  for live_file in "$BANK_DIR"/Examples_*.md "$BANK_DIR"/Project_Instructions_V*.md "$BANK_DIR"/Project_Instructions_Changelog.md "$BANK_DIR"/Evidence_Bank_Changelog.md; do
    [ -e "$live_file" ] || continue
    fname=$(basename "$live_file" .md)
    latest_backup=$(find "$RESOURCES_DIR" -maxdepth 1 -name "${fname}_backup_*.md" ! -name "*TRUNCATED*" 2>/dev/null | sort | tail -1)
    if [ -n "$latest_backup" ]; then
      diff=$(( $(wc -l < "$latest_backup") - $(wc -l < "$live_file") ))
      if [ "$diff" -gt 50 ]; then
        echo "SUSPECT: $fname dropped $diff lines vs $(basename "$latest_backup") - verify against changelog (deliberate restructure = pass)."
        any_suspect=1
      fi
    fi
  done
  [ "$any_suspect" -eq 0 ] && echo "PASS - no file dropped >50 lines vs latest good backup." || axis3_fail=1
fi
echo

total_fails=$((axis1_fail + axis2_fail + axis3_fail))
echo "=== Verdict ==="
if [ "$total_fails" -eq 0 ]; then
  echo "ALL-PASS - bank integrity clear at session close."
  exit 0
fi
echo "REVIEW - check each flagged axis. Axis 3 SUSPECTs may be legitimate restructures recorded in the changelog."
echo "Flagged: $axis1_fail (EOF) $axis2_fail (cross-ref) $axis3_fail (line-count)"
[ "$total_fails" -gt 1 ] && exit 4
[ "$axis1_fail" -eq 1 ] && exit 1
[ "$axis2_fail" -eq 1 ] && exit 2
[ "$axis3_fail" -eq 1 ] && exit 3
