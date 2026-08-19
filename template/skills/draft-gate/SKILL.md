---
name: draft-gate
description: "Run the consolidated Step-1-close verification gate on any drafted application document — length compliance against the channel bands, watch-outs sweep against the candidate's overclaim register, matrix-row traceability, and Selection Criteria Response structure — in one invocation with one report. Use before saving any output to Submissions/, before any platform screening-question response, and before any cover letter, statement of claims, pitch, criteria response or recruiter response is presented to the candidate. Also on 'run the gate', 'gate this draft', 'is this ready to deliver'. Replaces length-check, watchouts-sweep and matrix-row-traceability. PRECONDITION (Check 0, blocking): the voice audit must have run with its findings folded first. Blocking: platform character-limit breaches, High watch-out findings, missing or paraphrased criterion headings, and dodged hard-gate criteria; band and matrix drift are advisory. Always emit the full checklist table — no row omitted, no unevidenced verdict."
---

# Draft Gate — consolidated Step-1-close verification skill

> **Setup note:** This is a template skeleton. Replace `[Candidate Name]`, `[Candidate First Name]` and `[Workspace Folder Path]`. Build `references/sweep-checklist.md` from your own Section 7 register as it grows — that file is the only part of this gate that is candidate-specific.

One invocation, four checks, one report. This gate replaces the Step-1-close trio (`length-check`, `watchouts-sweep`, `matrix-row-traceability`) under the V6 structure: matrix rows now live at `Matrix_Rows/<ID>.md`, and length bands are keyed by **channel**, overlaying document types.

The gate exists because each check catches a real, recurring pre-delivery failure. Job boards truncate screening answers at their character limit **silently**. The watch-outs register carries the framework's hardest-earned overclaim discipline — every entry was added after a real overclaim was caught. And a draft that quietly swaps the matched row's tested body stack for ad-hoc evidence selection throws away the calibration the row encodes. The fourth is newer and the most brutal: a Selection Criteria Response that drops, merges or paraphrases one of the advertisement's criteria scores **zero** against that criterion no matter how good the prose is, because the panel scores the instrument, not the document.

## MANDATORY — emit the verification checklist table

This gate is not run until its checklist is **written down**. Load `references/checklist.md` and **emit that table in full** in the report: one row per checklist item, each with an explicit verdict **and the evidence that produced it**. Never summarise. Never omit a row. Never write "all pass" without the table. **If a row cannot be evidenced, its verdict is `UNVERIFIED` — and `UNVERIFIED` is treated as a FAIL for blocking purposes.**

| # | Check | How verified (command / quote / count) | Result | Verdict |
|:--|:--|:--|:--|:--|
| 0.3 | Em-dashes within cap AND not zero | Counted `—` in body text | 4 em-dashes, cap 6 | PASS |
| 1.2 | Screening answer Q2 within limit | `awk … \| wc -c` after markdown strip | 1,043 chars (limit: 1,000 hard) | FAIL |

Verdicts are `PASS` / `FAIL` / `UNVERIFIED` / `N-A`. `N-A` must state its reason in the evidence cell.

**Required row count — 29 fixed + L + C:**

| Block | Rows |
|:--|:--|
| Check 0 — voice-audit precondition | 10 (rows 0.1–0.10) |
| Check 1 — length | **L = one row per document section or per screening answer** (`L ≥ 1`) |
| Check 2 — watch-outs | 13 (rows 2.1–2.13, per your register's structure) |
| Check 3 — traceability | 6 (rows 3.1–3.6) |
| Check 4 — criteria-response structure | **C = 11 (rows 4.1–4.11) when the document type is a Selection Criteria Response; otherwise C = 1** — a single `N-A` row naming the actual document type |

**Total required = 29 + L + C. Minimum 31.** Check 4 is **additional to** the 29 + L formula, not a re-slice of it. Where a check is per-item, **one row per item is mandatory — a single summary row covering several items is a gate failure.** Where Check 4 is out of scope, emit **one** `N-A` row — never eleven.

**Self-audit line — emit it immediately before the gate verdict, every time:**

> `Checklist rows emitted: [X]. Rows required: 29 + L + C = [Y]. Match: [yes/no]. · criteria rows: [N]`

If they differ, the gate did not run — restart it.

### Anti-patterns (each is a gate failure)

- Claiming a check passed without running it — a verdict with no count, quote or command output is `UNVERIFIED`.
- Collapsing multiple items into one row (two screening answers, two watch-out IDs, two traceability checks in one row).
- Skipping the table because everything passed. There is **no** "one line per check" shortcut in this gate.
- Reporting any gate verdict before Check 0 has been reported.
- "All watch-outs clear" without the 13 rows of quotes or null results.
- A length verdict without the actual number; a watch-out verdict without the exact quote or `no match found for pattern "…"`; a traceability verdict without the B-ID and where it appears in the draft.
- Emitting eleven `N-A` Check 4 rows on a document that is not a Selection Criteria Response — one row, one reason.
- Verifying criterion headings against the draft's own table of contents or against the matrix row instead of against the advertisement's verbatim criteria list.

---

## When to invoke

- **Default trigger:** before saving any drafted output to `[Workspace Folder Path]/Submissions/`; before saving any screening-question `.md`; before any final application draft is presented to [Candidate First Name] — including re-drafts of prior submissions.
- **Explicit triggers:** "run the gate", "gate this draft", "check the length", "count words", "sweep this for watchouts", "check for overclaim", "did we follow the row", "is this on-prescription".
- **Skip when:** the draft is a working sketch or an intermediate iteration under review. Gate at the end, not at every revision.

## Inputs the gate needs

1. **The final draft text** (or the file path just written).
2. **Channel and document type** — channel: private-sector / recruiter-mediated / job-board vs public-sector / criteria-based. Document type: Cover Letter / Statement of Claims / Targeted Pitch / Recruiter Response / Screening Questions / Selection Criteria Response. If unknown, infer from the matched row and the brief.
3. **The matched matrix row** — read `Matrix_Rows/<ID>.md` in full. If the session ran on a documented no-clean-match basis, trace against the closest-analogue row and note the documented deviations.
4. **The pre-drafting assessment** (for deviations agreed before drafting).
5. **The brief's stated limits** (these always override defaults and row bands).
6. The watch-outs register — read in full for Check 2.
7. **For a Selection Criteria Response only — the advertisement's own criteria list, verbatim** (ad, position description, candidate pack or portal form), with its category headings and its Essential/Desirable split intact. Check 4 cannot run without it: the check is a comparison against the scoring instrument, and a remembered or paraphrased criteria list is not the instrument. Also load `references/criteria-response-structure.md`.

---

## Check 0 — Voice-audit precondition (blocking)

Before any other check, confirm the `candidate-voice` audit has run on **this** draft in **this** session and every finding was folded in: opener pattern rotated (never the previous letter's opener); em-dashes within cap **and not zero** (colons carrying every rhythmic beat is the same machine tell); no word-echo (a distinctive word repeated across paragraphs); sentence-rhythm spikes present with no flat multi-sentence runs; at least one low-probability phrase; one wit or warmth moment; no banned filler; bolded lead-ins intact; the configured English variant throughout. If the audit has not run, STOP — invoke `candidate-voice`, fold the findings, then restart this gate. The report's first line states `Voice audit: run + folded (date)` or `BLOCKED — voice audit missing`.

## Check 1 — Length (channel bands)

Bands are in `references/length-bands.md`.

**Override hierarchy (highest wins):** 1. the brief-stated limit (verbatim from the ad, position description, pack or recruiter) → 2. the matched row's `Template / Length` section in `Matrix_Rows/<ID>.md` → 3. the channel band. Name the source of the band in the report. If the band is genuinely ambiguous, ask [Candidate First Name] — one batched question — before applying a default.

### Counting rules

- **Letters / Statements of Claims / pitches:** count **body text only** — exclude the header, greeting, sign-off and signature block; include section headings.
- **Screening answers:** count **each answer independently** — passing on average is not passing per question. These fields render **plain text**: strip markdown syntax before counting AND flag any markdown as its own finding, because the platform will display literal asterisks. Smart quotes and dashes count as one character each.
- **Selection criteria:** count each criterion independently. Two-page limits convert at roughly 850–1,000 words, with a one-line caveat in the report.

```bash
# Body word count (strip YAML front-matter if present)
awk '/^---$/{f++; next} f!=1' draft.md | wc -w
# Per-answer character counts for H2-separated screening answers, markdown stripped
awk '/^## /{if(b)print b; b=""; next}{b=b $0 " "}END{print b}' draft.md \
  | sed 's/\*\*//g; s/\*//g' | awk '{printf "Q%d: %d chars\n", NR, length($0)-1}'
```

### Verdicts

Pass / Under by X / Over by X per section, with the gap named. On a platform-limit breach, never advise "trim a little": recommend the priority discipline — lead with the strongest one or two anchor proof points, abbreviate or drop the rest, never truncate mid-sentence. Don't enforce false precision: bands are inclusive, and a five-to-ten-word overshoot is rarely worth interrupting delivery for.

## Check 2 — Watch-outs sweep

Read the watch-outs register in full, then load `references/sweep-checklist.md` (the flat checklist of every named watch-out and sub-variant) as the working-memory aid.

1. **Filter to applicable watch-outs:** the always-applicable honesty boundaries, plus framing discipline and evidence recency; plus family-applicable sub-variants matching the role family or sector; plus any sub-variant the matched row's `Notes / Distinct from` section names. No matched row → run every named sub-variant; false positives are cheaper than missed overclaims.
2. **Cross-check the draft** for direct breaches (exact forbidden phrasing), indirect breaches (a paraphrase achieving the same overclaim), framing breaches (a required positioning or framing not used), missing-mandatory-discipline breaches (e.g. a required fit-acknowledgment absent), and recency flags.
3. **Score:** **High** = a direct or indirect breach of a named overclaim boundary — **blocks delivery**; **Medium** = a framing or missing-discipline breach — advisory, advise a rewrite; **Low** = a recency flag or contextual near-miss — surface for awareness.

Rules: cite register references by exact ID; quote the draft exactly; always recommend the compliant alternative; don't invent watch-outs (raise anything the register doesn't name as a "Watch-out candidate"); version-stamp the sweep with the register's revision date.

## Check 3 — Matrix-row traceability

Load `references/traceability-method.md`, then run all six checks against `Matrix_Rows/<ID>.md`:

1. **Body-stack reflection** — every B-ID in the row's stack shapes a draft paragraph (a one-clause allusion doesn't count). Record B-ID → paragraph → reflected / thin / absent; list substitutions.
2. **A-ID dominance** — the dominant A-ID's framing is recognisable in the opening third; secondary A-IDs support rather than compete.
3. **Template and length band** — the row's template was used and the draft sits in the row's band (cross-reference Check 1's count; do not recount).
4. **Fit-acknowledgment style** — gap handling follows the row's prescribed style; absence where the row prescribes one is drift.
5. **AI register** — AI claims match the row's register (hands-on builder vs governance-led). A register mismatch belongs here; framing overclaims belong in Check 2.
6. **Deviation accounting** — every deviation from 1–5 is either documented in the pre-drafting assessment or flagged as undocumented drift.

Verdicts: **On-prescription** / **Documented deviations only** / **Undocumented drift — review** (advisory: [Candidate First Name] decides regression vs improvement; an improvement must be folded back into the row file — with a changelog entry and a commit — in the same session. That is the row-calibration loop).


## Check 4 — Selection Criteria Response structure

**Applies only when the document type is a Selection Criteria Response.** For every other document type the whole check is a single `N-A` row naming the actual document type — do not emit an `N-A` row per sub-item.

Load `references/criteria-response-structure.md` — the canonical structure spec. That file is also the **drafting** spec: read it before generating the document, not only when gating it.

The check exists because a criteria response is scored mechanically against the advertisement's own instrument. A panel member works down their criteria list looking for each one. Anything they cannot find scores zero — not "partially met", zero — and the strongest paragraph in the document cannot recover it. So the structural failures matter more here than in any other document type the framework produces.

**Rows 4.1–4.11:**

| # | Rule | Blocking? |
|:--|:--|:--|
| 4.1 | **Header self-identifies.** Title line names the document type, the role and the organisation; an applicant line names the candidate. The response is read detached from the pack. | Advisory |
| 4.2 | **Criterion inventory complete.** Every criterion in the advertisement has its own heading in the response. Count criteria in the source; count headings in the draft; the numbers match, and each source criterion is ticked off individually. | **BLOCK** |
| 4.3 | **Headings verbatim.** Each heading quotes its criterion word for word, in bold, as its own heading. Never paraphrase a criterion into a heading, never compress two criteria into one heading, never re-title a criterion in the candidate's language. A paraphrased heading is a missed criterion to a panel scanning for its own words. | **BLOCK** |
| 4.4 | **Category grouping mirrors the advertisement.** Criteria sit under the ad's own category headings, in the ad's own order — not under a structure of the candidate's invention. The document mirrors the scoring instrument. | Advisory |
| 4.5 | **One evidence-dense paragraph per criterion.** No bullet lists, no sub-headings, no bullet padding. One paragraph carrying two or three named organisation anchors with hard numbers drawn from the matched row's body stack. Length is Check 1's business — cite it, don't recount, and don't pad to reach a word band. | Advisory |
| 4.6 | **Direct opening.** The first sentence answers the criterion. No warm-up, no restatement of the criterion, no "I have extensive experience in…" throat-clearing. | Advisory |
| 4.7 | **Compound criteria answered in full.** Where a criterion bundles several requirements into one sentence, the heading still stays verbatim as one heading, and the paragraph touches **every limb**. List the limbs; map each to the sentence that answers it. | Advisory |
| 4.8 | **Closing bridge.** The last sentence of each criterion paragraph ties the evidence back to the criterion or to this role — the so-what — rather than trailing off at the end of the last proof point. | Advisory |
| 4.9 | **Hard-gate qualification criteria answered head-on.** Where a criterion states a degree, certification or licence requirement the candidate does not hold literally, the paragraph leads with what they actually hold, plainly and specifically; states the gap in their own words; then argues substantive equivalence against the criterion's own wording. No dodging, no padding, no constructed false equivalence, no burying it mid-paragraph. Evasion on a stated essential is worse than the gap. | **BLOCK** |
| 4.10 | **Desirable criteria proportionate.** Handled as one brief consolidated closing note, not full per-criterion treatment — effort proportionate to an instrument that weights them lightly. Any honest gap among the desirables is named plainly inside that same note. | Advisory |
| 4.11 | **Division of labour with the companion letter.** No substantive repetition between the two: the criteria response carries the systematic, criterion-by-criterion evidence; the letter carries narrative, motivation, opening hook, salary and 30/60/90. Shared proof points appear in different framings, never as reused sentences. The letter carries one explicit hand-off line pointing the reader to the criteria response. | Advisory |

**How to verify 4.2 and 4.3 (the two blocking rows).** Build the comparison explicitly — do not eyeball it:

```bash
# Headings actually present in the draft (bold criterion lines, not category headings)
grep -n '^\*\*.*\*\*$' criteria-response.md
```

Then, in the report, list every criterion from the advertisement in the ad's order, each with the draft heading that answers it and a `verbatim / paraphrased / MISSING` verdict. `paraphrased` and `MISSING` both block. A criterion the ad states but the panel's own form omits (or vice versa) is resolved in the ad's favour and flagged.

**How 4.9 interacts with the rest of the system.** The matrix row's `Fit-acknowledgment` section prescribes the gap-handling style for the *package*, and Check 3.4 verifies it. Where the package includes a criteria response and the gap sits inside a stated essential criterion, the criteria response is where the gap gets its full, dedicated treatment, and the letter carries at most a light single-sentence version — see the watch-outs register's single-mention discipline: naming the same gap twice at full weight across the two documents is drift, not thoroughness. Register sub-variants still apply to the criteria response in full; Check 2 sweeps both documents.

**Verdicts:** **STRUCTURE PASS** / **STRUCTURE ADVISORY** (advisory rows failing — the candidate decides) / **STRUCTURE BLOCK** (any of 4.2, 4.3, 4.9 failing) / **N-A** (not a Selection Criteria Response).


---

## Consolidated report format

```
## Draft gate — [Role Title], [Organisation]
**Channel:** [short/long form] · **Doc type:** [type] · **Matched row:** [ID] · **Register rev:** [date]

### 1. Length — [PASS / ADVISORY / BLOCK]
| Section | Count | Band | Source of band | Verdict |
(one row per document section / screening answer)

### 2. Watch-outs — [PASS / ADVISORY / BLOCK] · [H/M/L counts]
(findings grouped High → Medium → Low: watch-out ID, exact draft quote, breach, recommended fix;
then two to four bullets of watch-outs that were relevant and correctly observed)

### 3. Traceability — [ON-PRESCRIPTION / DOCUMENTED DEVIATIONS / UNDOCUMENTED DRIFT]
| Check | On-prescription? | Deviation | Documented? |
(six rows)

### 4. Criteria-response structure — [STRUCTURE PASS / ADVISORY / BLOCK / N-A]
| Criterion (verbatim, in the ad's order) | Draft heading | verbatim / paraphrased / MISSING |
(one row per criterion in the advertisement — omit this table entirely when the check is N-A)

### Verification checklist (MANDATORY — emit in full, 29 + L + C rows)
| # | Check | How verified (command / quote / count) | Result | Verdict |
(rows 0.1–0.10, 1.1–1.L, 2.1–2.13, 3.1–3.6, 4.1–4.11 or a single 4.1 N-A row —
see references/checklist.md; no row omitted)

### Self-audit
Checklist rows emitted: [X]. Rows required: 29 + L + C = [Y]. Match: [yes/no]. · criteria rows: [N]

### Gate verdict
[DELIVER / AMEND (advisory findings — the candidate decides) / BLOCKED (name the blocking finding)]
Blocking semantics: a platform character-limit breach, High watch-out findings, a missing or
paraphrased criterion heading (4.2 / 4.3) and a dodged hard-gate criterion (4.9) block; band drift,
undocumented matrix drift and Check 4's advisory rows are advisory. Any `UNVERIFIED` row blocks
until it is evidenced.
```

The narrative sections summarise; **the checklist table is the gate**. Emit it in full every time, including when everything passes — there is no short-form report.
