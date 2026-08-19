# Prep gate — mandatory verification checklist

The **emit-in-full** checklist for `prep-gate`. Every invocation reproduces this table with the evidence column filled from the actual document and a verdict on every row.

**Verdict vocabulary:** `PASS` / `FAIL` / `UNVERIFIED` / `N-A`. `UNVERIFIED` counts as a FAIL. `N-A` must state its reason.

**Evidence rules:**
- A STAR row must carry the **exact quote** inspected (or an explicit "absent").
- A pace row must carry the **spoken word count**, the **measured wpm used**, and the resulting time.
- A capability row must name the **capability and the story mapped to it**, or state the gap.
- A PDF row must carry **command output**, not an impression.
- A research row must carry the **quote or count from the prep document itself** — the confidence marker, the `(inference)` label, the source phrase. Describing the research that was done is not evidence that the document says so.
- A calibration row must carry the **directive quoted from the document**, and — for the cross-artefact row — the reconciled figure quoted from **both** sides.

---

## Required row count

| Block | Rows | Notes |
|:--|:--|:--|
| Check 1 — STAR audit | **6 × S** | `S` = number of STARs. Six rows each, numbered `1.<star>.<item>`. |
| Check 2 — pace audit | **R** | One row per spoken response, `2.1 … 2.R`. |
| Check 3 — capability mapping | **6 + W** | Six component rows plus one row per Watch rating. `N-A` for all seven-plus rows where no formal framework applies — state the reason once. |
| Check 4 — annotation PDF | **9** | 4.1–4.9. Emitted for every PDF deliverable, and as `N-A` with the reason for a Markdown-only artefact. |
| Check 5 — research depth and sourcing | **9** | 5.1–5.9. **Additional to** the formula. Emitted for every deliverable naming an organisation or an interviewer; `N-A` with the reason otherwise. |
| Check 6 — panel-room calibration and record consistency | **10** | 6.1–6.10. **Additional to** the formula and to Checks 4 and 5. Emitted for every deliverable carrying an executive summary or a spoken response; `N-A` with the reason otherwise. |

**Required total = (6 × S) + R + 6 + W + 9, plus 9 research rows and 10 calibration rows.**

## Check 1 — STAR audit (six rows per STAR)

| # | Check | Evidence required |
|:--|:--|:--|
| 1.n.1 | Why = Situation + Task — the question behind the question answered first | Quote of the opening two sentences |
| 1.n.2 | How = Action — first person, specific, the candidate's own decisions | Quote; flag any plural ("we decided") |
| 1.n.3 | What = Result — quantified and attributable | The figure quoted, with its attribution |
| 1.n.4 | Flowing prose with bolded principle lines (not labelled S/T/A/R blocks) | The bolded principle line, quoted |
| 1.n.5 | Drop-list runway ≥ 20 seconds, marked in the source | The drop list quoted, with its word count and derived seconds |
| 1.n.6 | Closing principle line present and not marked droppable | The closing line, quoted |

## Check 2 — pace audit (one row per spoken response)

| # | Check | Evidence required |
|:--|:--|:--|
| 2.1 … 2.R | Response `<name>` within its time budget | Spoken word count **after stripping stage directions**, the measured wpm applied, the computed time, the budget, and the delta |

The wpm figure must be the candidate's **measured** rate from `pace-method.md`. A row computed at a published average is `UNVERIFIED`.

## Check 3 — capability mapping (six components + one row per Watch)

| # | Check | Evidence required |
|:--|:--|:--|
| 3.1 | Every capability group mapped per question | The mapping table, or the count of groups mapped vs total |
| 3.2 | Strong / Adequate / Watch rating on every cell | Count of rated cells vs total cells |
| 3.3 | Overall coverage matrix present | Quote or reference to the matrix |
| 3.4 | Values / behaviours cross-frame present | Quote or reference |
| 3.5 | Cumulative-impression reminder present | Quote |
| 3.6 | Mapping re-run against the final question list (where the final list exists) | Date of the re-run, or `N-A` with reason |
| 3.7 … 3.W | Watch `<capability>` has a named pivot story | The story ID or title, and the pivot sentence quoted |

## Check 4 — annotation PDF conventions

| # | Check | Evidence required |
|:--|:--|:--|
| 4.1 | Page size A4, correct rotation | `pdfinfo` output |
| 4.2 | Wide right margin applied (text block stops short of the edge) | The measured max xMax value and the expected value |
| 4.3 | Canonical YAML block used | The front-matter quoted |
| 4.4 | `\newpage` + Notes blocks where writing room is needed | Count of Notes blocks vs sections |
| 4.5 | Footnotes render on the page carrying the marker | Page number of a marker and of its footnote |
| 4.6 | Proportional pipe-table separator dashes | One table's separator row quoted |
| 4.7 | Wide tables wrapped landscape | The section names rendered landscape, or `N-A` |
| 4.8 | No orphaned near-empty pages around forced breaks | Per-page character counts, with any page under ~500 chars named |
| 4.9 | Paired Markdown source and PDF both saved, same base name | Both file paths |

---

## Check 5 — research depth and sourcing (nine rows)

Verified **against the prep document text**, not against the research that was done. Full rules:
`references/research-rules.md`.

| # | Check | Evidence required | Blocking? |
|:--|:--|:--|:--|
| 5.1 | Company / organisational context present (§3) — who they are, ownership or legal structure, and at least one **dated** financial or programme-status data point with the release date of its source | The section heading, plus the figure **and** its date quoted. A figure with no date fails | No |
| 5.2 | Entity / business-unit coverage (§4) where the organisation runs multiple operating businesses — one block per entity, plus the closing "reading this as a set" synthesis | Count of entity blocks against the operating businesses named in §3; the synthesis paragraph quoted. `N-A` with the reason for a single-entity employer | No |
| 5.3 | One profile per confirmed panellist (§5), each carrying confirmed biography, career history, likely lens and a tailored connection point | Front-matter names counted against profile sub-headings; any unprofiled panellist named | No |
| 5.4 | Every inference labelled — each speculative claim in its own paragraph under a bolded `(inference)` lead-in, and §5 opens with the sourcing-disclaimer blockquote | `(inference)` count against the speculative paragraphs (`likely`, `expect`, `strongly suggests`, `reads as`); any speculative sentence sitting inside a confirmed-fact paragraph quoted | **Yes** |
| 5.5 | Every factual claim carries a confidence marker | Claims in §§3–5 naming a person, figure, certification or system counted against markers; the unmarked ones quoted. An unmarked **person**-claim escalates to 5.6 | No |
| 5.6 | No unsourced person-claims — every claim about a named individual states its source in the same sentence | Each named individual listed with the source phrase attached to each claim about them | **Yes** |
| 5.7 | Sources split internal / web, both dated — internal block first, then a separately headed **dated** web-research block with full annotated URLs | The Sources section inspected; the web block's date quoted; bare unannotated URLs counted | No |
| 5.8 | Domain-term explainers where jargon from the employer's world is used | Domain terms in §§3–4 listed, each with its explainer or a note that it is common enough not to need one | No |
| 5.9 | Cross-round information hygiene (multi-round packs only) — earlier-round intel not carried forward, the boundary stated as a directive, and the clean generic "what did you discuss last round?" answer pre-scripted | The prior round's sensitive intel diffed against this brief's text; the directive and the pre-scripted answer both quoted. `N-A` with the reason for a single-round pack | **Yes** |

**Blocking semantics:** 5.4, 5.6 and 5.9 block — an unlabelled inference read back as fact, a
person-claim the candidate cannot source when challenged, and intel carried into a room it does not
belong in are the three findings that can embarrass them live. The rest are depth and traceability
findings; the candidate decides whether the gap matters for the round in front of them.

## Check 6 — panel-room calibration and record consistency (ten rows)

Verified against the prep document text **and against the artefacts already submitted for the role**,
not against intent. Checks 1–5 verify that the pack is well built; Check 6 verifies that it is built
**for this room**, and that it does not contradict what is already on the record.

| # | Check | Evidence required | Blocking? |
|:--|:--|:--|:--|
| 6.1 | "What this round is for" names every lens in the room — one clause per named panellist saying what each is testing, closing on the instruction a heterogeneous panel produces | Named panellists counted against lens clauses; the closing instruction quoted. `N-A` for a single unnamed interviewer | No |
| 6.2 | Decisions and actions are directives, not observations — imperative voice; where a fit gap exists, one bullet states its **placement**; an executive or final round carries a close directive | Each bullet's opening verb quoted; any observation named. The gap-placement and close directives quoted, or "no gap applies" stated | No |
| 6.3 | Core-risks table present, and every mitigation names the exact section or STAR to deploy — 3–6 interview-specific rows, risks attributed to the panellist whose probe produces them | Rows counted; per row, the section/STAR identifier quoted from the mitigation cell. A mitigation that only reassures ("stay calm", "be specific") fails | No |
| 6.4 | Time-budget arithmetic stated, and Section B reconciles to it — duration × panellists → expected question count → the delivery directive | The arithmetic sentence and the directive quoted; Section B's time-budget column summed against the stated duration. "Time will be tight" with no numbers fails | No |
| 6.5 | Questions and STARs attributed per panellist, **with the attribution caveat** | Attributed Section B rows and Section C headings counted against named panellists; the caveat **quoted**. Attribution with no caveat fails. `N-A` where the panel is not named | No |
| 6.6 | Every honest-gap or hard-gap response carries an explicit prohibition list — what must **not** be claimed anywhere in that answer, with the reason | Every honest-framing block and highest-risk STAR listed; the prohibition sentence **quoted** per response. Where a submitted artefact deliberately withheld a claim, that restraint appears here as a prohibition | **Yes** |
| 6.7 | Coaching notes carry delivery discipline **and** a don't-invent directive with the substitute line supplied | Per STAR, one delivery-discipline bullet quoted; for every follow-up that invites an invented number, name or use case, the substitute line quoted. A prohibition with no substitute is a finding | No |
| 6.8 | Rehearsal priority ranked across the pack — at least the top two highest-risk responses named in rank order | The ranking lines quoted. A pack where every STAR is flagged "practise this" fails — that is not a ranking | No |
| 6.9 | Cross-artefact consistency reconciled against every submitted artefact — letter or statement of claims, screening responses (final submitted text), messages to the hiring team, resume version sent, prior-round briefs | The artefacts opened, listed **by filename**. For every response covering ground a written artefact covers, the figure or claim **quoted from both sides side by side**. The "this is the spoken version of…" coaching note and the core-risks drift row quoted. `N-A` only where nothing has been submitted | **Yes** |
| 6.10 | Salary coaching (D1) matches the round type — recruiter screen: reflect-first plus market research and the no-ballpark watch-out; behavioural panel: reflect-first, research table dropped unless the band moved; executive/final and fit rounds: salary unlikely to arise, do not raise it | The round named, then the D1 posture sentence quoted. A full market-research apparatus at a final executive panel fails; a "don't raise it" posture at a recruiter screen fails harder | No |

**Blocking semantics:** 6.6 and 6.9 block. 6.9 blocks because contradicting a submitted application
in front of a panel that has read it is unrecoverable in the room. 6.6 blocks because the honest-gap
answer is by construction the highest-risk response in the pack, and an unbounded one invites exactly
the overclaim the honest framing exists to prevent.

---

## Anti-patterns — each is a gate failure

1. One summary row for several STARs or several responses. The problem is always in one specific item.
2. A pace figure at a published wpm rather than the measured rate.
3. Timing without stripping stage directions — pause markers are not spoken.
4. A Watch rating with no pivot story. That is the cell the panel will probe.
5. Check 4 verdicts based on looking at the PDF instead of running the commands.
6. Carrying a pace verdict forward across a reshape. A reshape changes the length; re-run it.
7. Marking a research row `PASS` by describing the research that was done rather than quoting the confidence marker or source phrase that appears in the document.
8. Marking row 6.9 `PASS` without having opened the submitted artefacts. "Consistent with the application" is `UNVERIFIED` unless the reconciled figures are quoted from both sides.
9. Dropping Checks 5 and 6 because they do not apply, instead of emitting their rows as `N-A` with the reason.
