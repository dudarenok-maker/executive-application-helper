# Bank gate — mandatory verification checklist

The **emit-in-full** checklist for `bank-gate`. Every invocation reproduces this table with the evidence column filled from actual command output and a verdict on every row.

**Verdict vocabulary:** `PASS` / `FAIL` / `UNVERIFIED` / `N-A`. `UNVERIFIED` counts as a FAIL. `N-A` must state its reason.

**Evidence rules:** every row in this gate is evidenced by **command output** — a hash, a `git status` result, a byte count, a sweep result. Prose assurance is `UNVERIFIED`.

---

## Required row count

| Block | Rows | Notes |
|:--|:--|:--|
| Check 1 — git commit discipline | **3** (fixed) | 1.1–1.3 |
| Check 2 — mount-cache coherence | **2 × F** | `F` = number of bank / changelog / instructions files changed this session. **Two rows per changed file** — a single row per file collapses two different failure modes (a write still in flight vs a steadily stale cache). |
| Check 3 — watch-out cross-references | **N** | `N` = distinct references found by the sweep. If the sweep finds none, emit **one** row recording the command and its empty output (`N = 1`). |
| Check 4 — personal-context discretion | **4** (fixed) | 4.1–4.4; emitted every session, `N-A` with a reason when nothing sensitive surfaced |

**Required total = 7 + 2F + N. Minimum 8.**

## Check 1 — git commit discipline

| # | Check | Evidence required |
|:--|:--|:--|
| 1.1 | Working tree clean at close | `git status --porcelain` output (empty), pasted |
| 1.2 | This session's changes are committed | The commit hash and `git show --stat <hash>` file list |
| 1.3 | Commit message carries what + why | The message's first line, quoted |

Row 1.3 is not a formality. Changelog entries are 2–4 lines under this model, so the reasoning behind a change lives in the commit message and nowhere else. "Update bank" as a message is a `FAIL`.

## Check 2 — mount-cache coherence (two rows per changed file)

| # | Check | Evidence required |
|:--|:--|:--|
| 2.n.1 | Shell view matches the Read-tool view for `<file>` | Byte size and last line from each, side by side |
| 2.n.2 | Shell probe stable across two reads one second apart for `<file>` | Both probe results |

`N-A` is legitimate only where the workspace has no mount or sync layer — state that reason once and apply it to every row.

## Check 3 — watch-out cross-reference axis (one row per distinct reference)

| # | Check | Evidence required |
|:--|:--|:--|
| 3.1 … 3.N | Reference `<ID>` resolves to a heading in the register | The grep command and its output, showing both the reference and the target heading |

If the sweep finds no references at all, emit one row with the command and its empty output. An empty result is a finding; an omitted row is a gap.

## Check 4 — personal-context discretion (always manual, always blocking)

| # | Check | Evidence required |
|:--|:--|:--|
| 4.1 | Did sensitive personal context surface this session? | Yes, with the deliverable named — or `N-A` with the reason |
| 4.2 | Used only in the deliverable it was shared for | The deliverable named, and the files it appears in |
| 4.3 | No propagation to the bank, a matrix row, a changelog, memory, or a staged deliverable | The grep patterns searched and their results |
| 4.4 | Not committed to git | `git log -p` or `git show` search result for the pattern |

Row 4.4 exists because git makes propagation durable in a way that a stray file edit is not — which is why this check runs **before** the commit, not after it.

---

## Anti-patterns — each is a gate failure

1. "Committed and clean" with no hash and no `git status` output.
2. One coherence row per file instead of two.
3. Check 3 reported as "no broken references" with no command and no output.
4. Check 4 omitted because nothing sensitive came up — `N-A` with a reason is the verdict, not silence.
5. A discretion finding parked as a follow-up. It is reversed in the session that created it, and the reversal is verified.
