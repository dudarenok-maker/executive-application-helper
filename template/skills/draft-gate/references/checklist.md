# Draft gate — mandatory verification checklist

This is the **emit-in-full** checklist for `draft-gate`. Every invocation reproduces this table in the report, with the evidence column filled from the actual draft and a verdict on every row.

**Verdict vocabulary:** `PASS` / `FAIL` / `UNVERIFIED` / `N-A`.
- `UNVERIFIED` = the check was not actually run, or the evidence cannot be produced. **`UNVERIFIED` counts as a FAIL for blocking purposes** — it never rolls up into "clear".
- `N-A` is legitimate only where the skill itself scopes the check out (e.g. a sub-variant whose role family does not match). `N-A` **must state the reason** in the evidence column.

**Evidence rules (a verdict with no evidence is `UNVERIFIED`):**
- A length row must carry the **actual number** (words or characters) and the band it was compared to.
- A watch-out row must carry either the **exact quote from the draft** that was inspected, or `no match found for pattern "<the pattern actually searched>"`.
- A traceability row must name the **B-ID / A-ID / row ID** and **where in the draft** it appears (paragraph number or exact quote).
- A voice row must carry a **count, an exact quote, or the pattern searched with a null result**.
- A criteria-structure row must carry the **criterion as the advertisement words it** alongside the
  draft heading or draft sentence inspected — a verdict quoting only the draft has not run the
  comparison, because the comparison is against the advertisement.
- "Checked", "looks fine", "confirmed" and "no issues" are **not evidence**.

---

## Required row count

| Block | Rows | Notes |
|:--|:--|:--|
| Check 0 — voice-audit precondition | **10** (fixed) | 0.1–0.10 |
| Check 1 — length | **L** (variable) | **One row per document section or per screening answer.** A single summary row for several answers is a gate failure. `L ≥ 1`. |
| Check 2 — watch-outs | **13** (fixed) | 2.1–2.13. Adjust the fixed count to match your own register's structure and keep it fixed thereafter — a variable watch-out count is how sweeps quietly shrink. |
| Check 3 — traceability | **6** (fixed) | 3.1–3.6 |
| Check 4 — criteria-response structure | **C** (conditional) | **11** (4.1–4.11) when the document type is a Selection Criteria Response; otherwise **1** — a single `N-A` row naming the actual document type. Eleven `N-A` rows is a gate failure. |

**Required total = 29 + L + C.** Minimum possible = **31**. Check 4 is **additional to** the
29 + L formula, not a re-slice of it.

---

## Check 0 — voice-audit precondition (blocking; reported BEFORE any other verdict)

| # | Check | Evidence required |
|:--|:--|:--|
| 0.1 | The voice audit ran on **this** draft in **this** session and every finding was folded in | The audit date and the count of findings folded, or `BLOCKED — voice audit missing` |
| 0.2 | Opener pattern rotated — not the previous letter's opener | Exact quote of this draft's opening sentence **and** the previous letter's opener (or the file compared against) |
| 0.3 | Em-dash count within cap **and not zero** | The actual count and the cap it was compared to |
| 0.4 | No word-echo — no distinctive word repeated across paragraphs | The most-repeated distinctive word and its count |
| 0.5 | Sentence-rhythm spikes present; no flat multi-sentence runs | The sentence word-length sequence for the longest run, or the shortest and longest sentence counts |
| 0.6 | At least one low-probability phrase | The exact phrase, quoted |
| 0.7 | At least one wit or warmth moment | The exact sentence, quoted |
| 0.8 | No banned filler | The filler patterns searched, each with its result |
| 0.9 | Bolded lead-ins intact (and punctuated per the style guide) | Count of bolded lead-ins vs paragraph count, plus one quoted lead-in |
| 0.10 | Correct English variant throughout | The spelling patterns searched (e.g. `-ize`, `-yze`, `organization`) with results |

## Check 1 — length (one row per section / per screening answer)

| # | Check | Evidence required |
|:--|:--|:--|
| 1.1 … 1.L | Section / screening answer `<name or Q number>` within its band | **Actual count** (words for letters, characters for screening answers and criteria), the band applied, and the **source of the band** (brief-stated limit / row `Template / Length` / channel band). For screening answers: the count is post-markdown-strip, and any markdown found is its own finding in the Result cell. |

**One row per screening answer is mandatory** — "all answers under the limit" without per-answer counts is a gate failure, because passing on average is not passing per question.

## Check 2 — watch-outs sweep

> **Setup note:** the row list below is a **shape**, not content. Populate it from your own Section 7 register: one row per named honesty boundary, one row per sub-variant family, one row for framing discipline, one row for evidence recency. Keep the count fixed once set.

| # | Check | Evidence required |
|:--|:--|:--|
| 2.1 – 2.n | `[Named honesty boundary from the register]` | Exact draft quote inspected, or `no match found for pattern "<pattern>"` |
| 2.n+1 | `[Sub-variant family — role-family or sector specific]` | Which sub-variant(s) applied and why (role family named), then a quote or null result per applied sub-variant; `N-A` requires the role family named |
| 2.12 | Framing discipline (including any AI framing rules) | Quote of every claim inspected, or a null result |
| 2.13 | Evidence recency | Each dated claim quoted with its year, or a null result |

Every finding row also carries its **score** in the Result cell: `High` (blocks) / `Medium` (advisory) / `Low` (awareness). State the register's revision date once, in the report header.

## Check 3 — matrix-row traceability

| # | Check | Evidence required |
|:--|:--|:--|
| 3.1 | Body-stack reflection | **Every B-ID in the row's stack listed individually**, each mapped to a draft paragraph number or quote with `reflected / thin / absent`; substitutions named |
| 3.2 | A-ID dominance | The dominant A-ID named, plus the quote from the opening third that carries its framing |
| 3.3 | Template and length band | The template ID used and the band, cross-referenced to the Check 1 row that carries the count (**do not recount**) |
| 3.4 | Fit-acknowledgment style | The row's prescribed style named, plus the draft quote implementing it (or an explicit "absent") |
| 3.5 | AI register | The row's register named, plus the draft quote carrying the AI claim |
| 3.6 | Deviation accounting | Each deviation from 3.1–3.5 listed with `documented in pre-drafting assessment` (quoted) or `undocumented drift` |

---

## Check 4 — Selection Criteria Response structure (conditional; 11 rows or 1)

Applies **only** when the document type is a Selection Criteria Response. Otherwise emit exactly one
row: `4.1 | Check 4 scope | Document type is <type>, not a Selection Criteria Response | N-A`.

Verified against the **advertisement's verbatim criteria list**, not against the matrix row, the
draft's own headings, or memory. Full rules: `references/criteria-response-structure.md`.

| # | Check | Evidence required | Blocking? |
|:--|:--|:--|:--|
| 4.1 | Header self-identifies (document type + role + organisation + applicant) | The header lines quoted | Advisory |
| 4.2 | Criterion inventory complete — every criterion in the ad has its own heading | **Count of criteria in the ad vs count of headings in the draft**, plus the per-criterion mapping table (every source criterion listed individually and ticked off). A count alone, with no mapping, is `UNVERIFIED` | **BLOCK** |
| 4.3 | Headings verbatim — word for word, bold, one heading per criterion, no paraphrase, no merged criteria | For each criterion: the ad's wording and the draft's heading side by side, with `verbatim / paraphrased / MISSING` | **BLOCK** |
| 4.4 | Category grouping mirrors the ad's own category headings, in the ad's order | The ad's category headings quoted alongside the draft's `##` headings | Advisory |
| 4.5 | One evidence-dense paragraph per criterion; no bullets, no sub-headings | Per criterion: paragraph count, word count, and the named organisation anchors it carries | Advisory |
| 4.6 | Direct opening — the first sentence answers the criterion | The first sentence of each criterion paragraph, quoted | Advisory |
| 4.7 | Compound criteria — every limb of a multi-part criterion answered | The limbs listed, each mapped to the sentence answering it; `N-A` where no criterion is compound (state that) | Advisory |
| 4.8 | Closing bridge — the last sentence ties back to the criterion or the role | The last sentence of each criterion paragraph, quoted | Advisory |
| 4.9 | Hard-gate qualification criteria answered head-on — what the candidate holds, stated plainly; the gap named in their own words; substantive equivalence argued against the criterion's own wording | The criterion quoted from the ad, plus the draft's leading sentences quoted. Where no hard-gate criterion exists, `N-A` with the reason (**and the essential criteria list must have been read to say so**) | **BLOCK** |
| 4.10 | Desirable criteria proportionate — one consolidated note, not per-criterion treatment | The consolidated note quoted, plus the count of desirable criteria it covers | Advisory |
| 4.11 | Division of labour with the companion letter — no substantive repetition; the letter carries the hand-off line | The companion letter named (file path), the shared proof points listed with how each is framed differently in each document, and the letter's hand-off sentence quoted; `N-A` only where there is genuinely no companion letter | Advisory |

**Blocking semantics for Check 4:** 4.2, 4.3 and 4.9 block. A `paraphrased` or `MISSING` verdict on
any single criterion in 4.3 blocks the whole gate — partial completeness is not completeness, because
the panel scores criterion by criterion.

---

## Anti-patterns — each is a gate failure, not a style preference

1. **Claiming a check passed without running it.** A verdict with no command output, count or quote is `UNVERIFIED`.
2. **Collapsing multiple items into one row.** One screening answer per row; one watch-out ID per row; one traceability check per row. A merged row fails both merged items.
3. **Skipping the table because everything passed.** The clean case is exactly when the table is cheapest to produce and most likely to be faked. Emit it.
4. **Reporting a gate verdict before Check 0.** The voice-audit precondition is reported first, always.
5. **"All watch-outs clear."** Without the full rows of quotes or null results, that is a summary, not a sweep.
6. **Averaging screening answers.** The platform truncates per answer.
7. **Recounting length inside Check 3** instead of citing the Check 1 row — two counts that disagree hide which one is real.
8. **Eleven `N-A` rows for Check 4** on a document that is not a Selection Criteria Response. One row, one reason.
9. **Verifying criterion headings against anything other than the advertisement** — the draft's own contents list, the matrix row, or memory. The advertisement is the scoring instrument; nothing else is.
