---
name: bank-gate
description: "Run the consolidated session-close verification gate at the end of ANY session that touched evidence-bank files, Matrix_Rows/ files, the project instructions or a changelog — git commit discipline, mount-cache coherence cross-check on every changed file, watch-out cross-reference resolution, and the personal-context discretion boundary — in a single invocation with one consolidated report. Use at session close after bank edits, before the maintenance report, whenever git status is not clean, or when the candidate says 'close out the session', 'check the bank', 'integrity check', 'run the bank gate', 'did anything personal leak', or 'make sure I didn't break anything'. Replaces the retired bank-integrity-check, snapshot-check and personal-context-discretion-check skills under the git-based safety model. Blocking: uncommitted bank changes, coherence mismatches, broken cross-references and any personal-context propagation all block session close; propagation must be reversed in-session, never parked."
---

# Bank Gate — consolidated session-close verification skill

> **Setup note:** This is a template skeleton. Set the workspace path at the top of `references/check-script.sh`, and replace `[Candidate Name]` / `[Candidate First Name]` / `[Workspace Folder Path]` throughout. The gate assumes the workspace is a git repository — if `git init` has not been run, do that first (see the project instructions, Git discipline).

One invocation, four checks, one report. This gate replaces the retired integrity stack (`snapshot-check`, `bank-integrity-check`, `personal-context-discretion-check`) under the git-based safety model.

Two of the three retired skills were made redundant by git: snapshots and end-of-file / line-count integrity axes are both answered better by `git diff` and `git checkout` than by a folder of dated copies. Two things git does **not** solve survive into this gate: a **semantic** cross-reference (a matrix row naming a watch-out sub-variant that does not exist) is a perfectly valid commit, and a **mount-cache** incoherence can hand the shell a stale view of a file that a later rewrite then persists as a truncation. Those are Checks 3 and 2.

## MANDATORY — emit the verification checklist table

This gate is not run until its checklist is **written down**. Load `references/checklist.md` and **emit that table in full**: one row per item, each with an explicit verdict **and the evidence that produced it**. **A row that cannot be evidenced is `UNVERIFIED`, and `UNVERIFIED` is treated as a FAIL.**

**Required row count — 7 + 2F + N:**

| Block | Rows |
|:--|:--|
| Check 1 — git commit discipline | 3 (rows 1.1–1.3) |
| Check 2 — mount-cache coherence | **2 × F** (`F` = bank / changelog files changed this session; **two rows per file**) |
| Check 3 — watch-out cross-references | **N** (one row per distinct reference found; if none, one row recording the command and its empty output) |
| Check 4 — personal-context discretion | 4 (rows 4.1–4.4) — emitted every session, `N-A` with a reason where nothing sensitive surfaced |

**Total required = 7 + 2F + N. Minimum 8.**

**Self-audit line — emit it immediately before the gate verdict, every time:**

> `Checklist rows emitted: [X]. Rows required: 7 + 2F + N = [Y]. Match: [yes/no].`

### Anti-patterns (each is a gate failure)

- "Committed and clean" with no commit hash and no `git status` output.
- One coherence row per file instead of two — the two rows catch different failures (a file still in flux vs a steadily stale cache), and collapsing them hides one of them.
- Reporting Check 3 as "no broken references" without the sweep command and its output.
- Omitting Check 4 because nothing sensitive came up. `N-A` with a stated reason is the correct verdict, not silence.
- Parking a discretion finding as a follow-up. Propagation is reversed in the session that created it.

---

## When to invoke

- **Default trigger:** at session close, whenever any tracked file was touched — an evidence-bank file, a `Matrix_Rows/` file, the project instructions, or a changelog. Run it **before** writing the maintenance report, so the commit hash and verdict can go into that report.
- **Explicit triggers:** "close out the session", "check the bank", "integrity check", "run the bank gate", "did anything personal leak", "make sure I didn't break anything".
- **Also run** whenever `git status` is not clean at any point you expected it to be.

## Inputs the gate needs

1. The list of files changed this session (and what changed in each).
2. Whether any sensitive personal context surfaced during the session, and for which named deliverable.
3. The watch-outs register (for Check 3's target headings).

## Fastest path — Checks 1–3 by script

`references/check-script.sh` runs the mechanical parts: git status and the last commit, the coherence probe on changed files, and the cross-reference sweep. Run it, read the output, then complete Check 4 by hand. The script reports; it does not decide — the verdicts are still written into the checklist with their evidence.

## Check 1 — Git commit discipline

The working tree is clean at close, and every change made this session is in a commit whose message says **what changed and why**. Under the git-based model, the commit message carries the narrative that changelog entries used to carry — changelog entries are now 2–4 lines, so a thin commit message loses the reasoning permanently.

Evidence: the commit hash, the message's first line, and `git status --porcelain` output (empty). **A dirty tree blocks the close.** Untracked files that should be ignored are a `.gitignore` fix, not an exception.

## Check 2 — Mount-cache coherence cross-check (changed files)

For every bank file, changelog or instructions file changed this session, **two** rows:

1. **Cross-tool agreement.** The shell's view (size, hash, last line) matches the Read-tool view. A mismatch means the shell view is stale — trust the Read tool and re-write via the shell.
2. **Stability across two reads.** The same shell probe, repeated a second apart, returns identical results. A file still settling gives two different answers, and writing back the first one truncates it.

Both rows are needed because they fail differently: row 1 catches a steadily stale cache, row 2 catches a write still in flight. **A mismatch on either blocks the close.**

If the workspace is on a local disk with no mount or sync layer, both rows are `N-A` with that reason stated once — but state it, rather than skipping the rows.

## Check 3 — Watch-out cross-reference axis

The one axis of the old three-axis integrity check that git does not replace. Sweep every matrix row file and family index for references to watch-out sub-variants, then confirm each referenced ID exists as a heading in the register. A row that prescribes a watch-out that no longer exists sends the draft gate looking for a rule that cannot be found — and the sweep silently comes back clean.

One row per distinct reference found. **A dangling reference blocks the close** and is fixed in-session: either restore the missing heading or correct the reference.

## Check 4 — Personal-context discretion (always manual, always blocking)

Load `references/discretion-rules.md`. Sensitive personal information shared for a specific deliverable is bounded to that deliverable. Four rows, every session:

| Row | Question |
|---|---|
| 4.1 | Did sensitive personal context surface this session? (If no: `N-A`, reason stated, rows 4.2–4.4 also `N-A`.) |
| 4.2 | Was it used **only** in the named deliverable it was shared for? |
| 4.3 | Did any of it reach the evidence bank, a matrix row, a changelog, memory, or a staged future deliverable? |
| 4.4 | Was it committed to git? (Git makes propagation durable — this row is why the check runs before the commit, not after.) |

**Any propagation blocks the close and is reversed in-session.** Not noted as a follow-up, not parked in the changelog — removed, and the removal verified.

---

## Consolidated report format

```
## Bank gate — session close [YYYY-MM-DD]

### 1. Git commit discipline — [PASS / BLOCK]
Commit [hash] — "[message first line]" · git status: [clean / N files dirty]

### 2. Coherence cross-check — [PASS / BLOCK]
(two rows per changed file)

### 3. Watch-out cross-references — [PASS / BLOCK]
(sweep command + output; one row per distinct reference)

### 4. Personal-context discretion — [CLEAN / N-A — none surfaced / BLOCK: propagation found]

### Verification checklist (MANDATORY — emit in full, 7 + 2F + N rows)
| # | Check | How verified (command / quote / count) | Result | Verdict |

### Self-audit
Checklist rows emitted: [X]. Rows required: 7 + 2F + N = [Y]. Match: [yes/no].

### Gate verdict
[CLOSE / BLOCKED (name the blocking finding)]
```
