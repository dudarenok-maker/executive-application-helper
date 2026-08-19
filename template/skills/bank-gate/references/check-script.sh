#!/usr/bin/env bash
#
# bank-gate — mechanical helper for Checks 1-3.
#
#   bash check-script.sh "/path/to/workspace"
#
# Runs the parts of the session-close gate a machine can do:
#   Check 1  git commit discipline  — status, HEAD, message
#   Check 2  mount-cache coherence  — two probes per changed file
#   Check 3  cross-reference axis   — every watch-out reference resolves
#
# Check 4 (personal-context discretion) is deliberately NOT here. It requires
# judgement about what was shared and for which deliverable, and a script that
# appeared to run it would make it easy to stop thinking about it.
#
# The script REPORTS. It does not decide. Every verdict still goes into the
# gate's checklist table with the evidence pasted from this output.
#
# Exit codes: 0 all pass / 1 dirty tree / 2 coherence / 3 cross-reference / 4 multiple / 99 bad dir

set -uo pipefail

# ---------------------------------------------------------------------------
# SETUP: set this to your workspace root, or pass it as $1.
# ---------------------------------------------------------------------------
BANK_DIR="${1:-[Workspace Folder Path]}"

# Files whose cross-references are swept in Check 3. Adjust to your file names.
REGISTER="Examples_Master.md"                   # SETUP: the file holding the watch-outs register
                                                # (switch to Examples_Section_7_Watchouts.md if you split it out)
REF_PATTERN='Section 7\.[0-9]+(\.[0-9]+)*'      # the reference form used in rows

cd "$BANK_DIR" 2>/dev/null || { echo "FATAL: cannot cd to $BANK_DIR"; exit 99; }

fail_git=0; fail_coh=0; fail_ref=0

echo "==========================================================="
echo " bank-gate mechanical checks — $(date +%F) — $BANK_DIR"
echo "==========================================================="

# ---------------------------------------------------------------------------
# Check 1 — git commit discipline
# ---------------------------------------------------------------------------
echo
echo "--- Check 1: git commit discipline ---"
if [ ! -d .git ]; then
  echo "FATAL: no git repository at $BANK_DIR. Run 'git init' — see the project"
  echo "       instructions, Git discipline. The gate cannot pass without it."
  exit 99
fi

echo "[1.1] git status --porcelain:"
STATUS="$(git status --porcelain)"
if [ -z "$STATUS" ]; then
  echo "      (empty — clean)"
else
  echo "$STATUS" | sed 's/^/      /'
  echo "      *** DIRTY TREE — Check 1.1 FAILS. Commit before close. ***"
  fail_git=1
fi

echo "[1.2] HEAD:"
git log -1 --format='      %h  %ad  %s' --date=short
echo "[1.2] files in HEAD:"
git show --stat --format='' HEAD | sed 's/^/      /'
echo "[1.3] message first line — judge what+why by eye:"
git log -1 --format='      %s'

# ---------------------------------------------------------------------------
# Check 2 — mount-cache coherence, two probes per changed file
# ---------------------------------------------------------------------------
echo
echo "--- Check 2: mount-cache coherence (changed files) ---"
echo "NOTE: this script reads through the shell. If the workspace is a mounted or"
echo "      synced folder, the shell can serve a STALE view. Probe 1 below catches a"
echo "      write still in flight; only a cross-check against the Read tool catches a"
echo "      steadily-stale cache. Row <n>.1 of the checklist is that cross-check and"
echo "      CANNOT be produced by this script — do it by hand."

CHANGED="$(git show --stat --format='' --name-only HEAD 2>/dev/null; git diff --name-only)"
CHANGED="$(echo "$CHANGED" | grep -E '\.md$' | sort -u)"

if [ -z "$CHANGED" ]; then
  echo "      no markdown files changed — Check 2 is N-A (state the reason in the checklist)"
else
  for f in $CHANGED; do
    [ -f "$f" ] || continue
    s1=$(wc -c < "$f"); h1=$(sha256sum "$f" | cut -c1-16); l1=$(tail -1 "$f")
    sleep 1
    s2=$(wc -c < "$f"); h2=$(sha256sum "$f" | cut -c1-16); l2=$(tail -1 "$f")
    if [ "$s1" = "$s2" ] && [ "$h1" = "$h2" ]; then
      echo "      [stable] $f  ${s1}B  sha:${h1}"
      echo "               last line: ${l1:0:70}"
    else
      echo "      [IN FLUX] $f  ${s1}B/${s2}B  sha:${h1}/${h2}  *** Check 2 FAILS ***"
      fail_coh=1
    fi
  done
  echo "      -> now cross-check each size/last-line above against the Read tool."
fi

# ---------------------------------------------------------------------------
# Check 3 — watch-out cross-reference axis
# ---------------------------------------------------------------------------
echo
echo "--- Check 3: watch-out cross-references ---"
if [ ! -f "$REGISTER" ]; then
  echo "      register '$REGISTER' not found — set REGISTER at the top of this script"
  fail_ref=1
else
  REFS="$(grep -rhoE "$REF_PATTERN" Matrix_Rows/ Examples_Section_5_*.md 2>/dev/null | sort -u)"
  if [ -z "$REFS" ]; then
    echo "      grep found no references (this is itself the evidence for the single"
    echo "      Check 3 row — paste this line, do not omit the row)"
  else
    for r in $REFS; do
      id="${r#Section }"
      if grep -qE "^#+ *${id}" "$REGISTER"; then
        echo "      [ok]      $r -> heading found in $REGISTER"
      else
        echo "      [DANGLING] $r -> NO heading in $REGISTER  *** Check 3 FAILS ***"
        fail_ref=1
      fi
    done
  fi
fi

# ---------------------------------------------------------------------------
echo
echo "--- Check 4: personal-context discretion ---"
echo "      NOT AUTOMATED. Four rows, by hand, every session — see"
echo "      references/discretion-rules.md and the SKILL.md checklist."
echo

n=$((fail_git + fail_coh + fail_ref))
if [ "$n" -eq 0 ]; then echo "RESULT: mechanical checks 1-3 PASS. Complete Check 4 by hand."; exit 0
elif [ "$n" -gt 1 ]; then echo "RESULT: MULTIPLE FAILURES — close is blocked."; exit 4
elif [ "$fail_git" -eq 1 ]; then echo "RESULT: git discipline FAILED — close is blocked."; exit 1
elif [ "$fail_coh" -eq 1 ]; then echo "RESULT: coherence FAILED — close is blocked."; exit 2
else echo "RESULT: cross-reference FAILED — close is blocked."; exit 3
fi
