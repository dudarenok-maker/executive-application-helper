---
name: prep-gate
description: "Run the consolidated interview-prep verification gate on any prep document before delivery — STAR construction audit, honest pace audit at the candidate's real measured speaking rate, capability mapping for framework-scored panels, annotation-PDF output conventions, research depth and sourcing, and panel-room calibration and record consistency — in one invocation with one report. Use at prep close, after every reshape, and before any prep PDF is delivered. Also on 'run the prep gate', 'check the STARs', 'time these', 'does this match what I submitted'. Replaces the separate star-audit, pace-audit and capability-mapping-check skills. Blocking: High STAR findings, a pace overrun above 25%, a missing capability component or unpivoted Watch, unlabelled inference, unsourced person-claims, an honest-gap answer with no prohibition list, and any drift from a submitted artefact. Always emit the full checklist table — no row omitted, no unevidenced verdict."
---

# Prep Gate — consolidated interview-prep verification skill

> **Setup note:** This is a template skeleton. Replace `[Candidate Name]` and `[Candidate First Name]`. **Measure the candidate's actual speaking pace before first use** and record it in `references/pace-method.md` — the default published rates are useless here, and an optimistic pace is the single most common reason a prepared answer overruns in the room.

One invocation, six checks, one report. This gate replaces the prep-close trio (`star-audit`, `pace-audit`, `capability-mapping-check`), folds in the annotation-PDF output conventions that used to live in the project instructions (Check 4), and adds the two disciplines that govern the research half and the panel-room half of a prep pack (Checks 5 and 6).

The gate exists because prep failures are invisible on the page. A STAR that reads well silently takes three and a half minutes to say. A capability the panel will score has no story attached, and nobody notices until the question lands. A PDF renders beautifully and cannot be annotated because the right margin is 20 mm. A reformat strips the `(inference)` label off a reasoned guess so it reads back as fact in the room. And a tightened STAR quietly drifts a figure away from the number the candidate already put in writing on their own application — in front of the panel that read it.

## MANDATORY — emit the verification checklist table

This gate is not run until its checklist is **written down**. Load `references/checklist.md` and **emit that table in full**: one row per checklist item, each with an explicit verdict **and the evidence that produced it**. Never summarise. Never omit a row. **A row that cannot be evidenced is `UNVERIFIED`, and `UNVERIFIED` is treated as a FAIL for blocking purposes.**

**Required row count — (6 × S) + R + 6 + W + 9:**

| Block | Rows |
|:--|:--|
| Check 1 — STAR audit | **6 × S** (`S` = number of STARs; six rows each, numbered `1.<star>.<item>`) |
| Check 2 — pace audit | **R** (one row per spoken response) |
| Check 3 — capability mapping | **6 + W** (six component rows + one row per Watch rating) |
| Check 4 — annotation PDF conventions | **9** (rows 4.1–4.9); emitted for every PDF deliverable, and as `N-A` with the reason for a Markdown-only artefact |
| Check 5 — research depth and sourcing | **9** (rows 5.1–5.9); **additional to** the formula above, emitted for every deliverable that names an organisation or an interviewer, and as `N-A` with the reason otherwise |
| Check 6 — panel-room calibration and record consistency | **10** (rows 6.1–6.10); **additional to** the formula above and to Checks 4 and 5, emitted for every deliverable carrying an executive summary or a spoken response, and as `N-A` with the reason otherwise |

Where a check is per-item, **one row per item is mandatory** — a single summary row covering several STARs or several responses is a gate failure.

**Self-audit line — emit it immediately before the gate verdict, every time:**

> `Checklist rows emitted: [X]. Rows required: (6 × S=[s]) + R=[r] + 6 + W=[w] = [Y] · PDF rows: 9 · research rows: 9 · calibration rows: 10. Match: [yes/no].`

### Anti-patterns (each is a gate failure)

- "All STARs are well constructed" without six rows per STAR.
- A pace verdict with no word count and no wpm figure — or one computed at a published average rather than the candidate's measured rate.
- Timing a response without stripping stage directions and pause markers first.
- Collapsing several responses into one pace row. The overrun is always in one specific answer.
- A capability marked Watch with no named pivot story.
- Skipping Check 4 because "the PDF looked fine" — the geometry checks are commands, not impressions.
- Dropping Check 3, 5 or 6's rows when they do not apply instead of emitting them as `N-A` with the reason.
- Marking a research row `PASS` by describing the research that was done rather than quoting the confidence marker or source phrase that appears in the document.
- Marking row 6.9 `PASS` without having opened the submitted artefacts. "Consistent with the application" is `UNVERIFIED` unless the reconciled figures are quoted from **both** sides.

---

## When to invoke

- **Default trigger:** at prep close, before any prep document or its PDF is delivered; **and again after every reshape** (a reshape changes the length of what will be said out loud, so the pace audit is re-run, not carried forward).
- **Explicit triggers:** "run the prep gate", "check the STARs", "how long will this take to say", "check the capability coverage", "is this ready for the panel".

## Inputs the gate needs

1. The prep document (or file path).
2. The interview format — recruiter screen / behavioural panel / executive panel — and the time allowed.
3. The candidate's **measured** words-per-minute, with pauses (`references/pace-method.md`).
4. The capability framework the panel will score against, if any.
5. The matched matrix row — the prep runs off the same row as the application.
6. **The prior rounds' briefs and their Sources sections**, where this is a multi-round pack — Check 5's cross-round hygiene row (5.9) is verified by diffing the earlier round's sensitive intel against the later brief's text.
7. **Every artefact already submitted for this role**, from `Submissions/` — the cover letter or statement of claims, the screening-question responses (**final submitted text**, not drafts), any message to the hiring team, and the resume version sent. Check 6's row 6.9 cannot be run without them, and an unrun 6.9 is `UNVERIFIED`, which blocks.

## Check 1 — STAR audit

Load `references/star-rules.md`. Six checks per STAR: **Why = Situation + Task** (the question behind the question is answered first); **How = Action** (first-person, specific, the candidate's own decisions rather than the team's); **What = Result** (quantified, and attributable); flowing prose with **bolded principle lines** rather than labelled S/T/A/R blocks; a **drop-list runway of at least 20 seconds** (what gets cut if the panel interrupts, marked in the source); and **closing principle lines never cut** — they are the sentence the panel remembers.

High findings block. The common ones: a Result with no number, an Action written in the plural, and a STAR with no drop list, which in the room becomes a STAR delivered at full length while the chair looks at the clock.

## Check 2 — Pace audit (honest timing)

Load `references/pace-method.md`. Strip stage directions and pause markers, count the spoken words, divide by the candidate's **measured** rate — never a published average.

```bash
# Spoken-word count for one response (strip bracketed stage directions first)
sed 's/\[[^]]*\]//g' response.md | wc -w
```

Compare against the format's budget (recruiter screen ~90 seconds per STAR; behavioural panel 2–3 minutes; executive panel per the brief). **An overrun above 25% blocks** until tightened. 10–25% is advisory, and comes with a two-pass tightening plan: first pass removes scene-setting, second removes the second-strongest proof point. Under-runs are worth flagging too — a 45-second answer to a behavioural question reads as thin.

## Check 3 — Capability mapping (framework-scored panels only)

Load `references/mapping-checklist.md`. Required for any panel scored against a formal capability framework; skipped, with the reason stated, otherwise. Every capability group mapped per question; a Strong / Adequate / Watch rating on every cell; **a named pivot story for every Watch**; an overall coverage matrix; a values or behaviours cross-frame; and the cumulative-impression reminder. A missing component blocks. A Watch with no pivot blocks — that is precisely the cell the panel will probe.

Re-run the mapping when the final question list arrives. The coverage that looked complete against the anticipated questions is frequently thin against the real ones.

## Check 4 — Annotation PDF conventions

Load `references/annotation-pdf-rules.md` and verify the output mechanically, not by eye: page geometry including the **wide right margin** for margin notes; the canonical YAML block; `\newpage` and Notes blocks where the candidate needs writing room; footnotes rendering on the page carrying the marker; proportional pipe-table separator dashes; landscape wrapping for wide tables; and the **no-orphaned-near-empty-page** rule around forced breaks. The verification commands are in that file — run them and paste the output into the evidence column.


## Check 5 — Research depth and sourcing discipline

**Applies** to any prep deliverable that asserts facts about the employer or about named individuals — every brief, recruiter-screen pack and fit/working-relationship brief. **Skip only** for a practicalities-only artefact naming no organisation and no interviewer; say so and emit the rows as `N-A`.

Load `references/research-rules.md` (the confidence ladder, the source-authority ranking, the inference-labelling rule and the worked source-conflict cases), and the research half of `candidate-voice/references/interview-prep-template.md` (§R and §§3–6). Verify **against the prep document text**, not against the research that was done.

This check exists because sections 3–6 are the only part of a prep pack that asserts things about other people's companies and other people's careers. A tightening pass strips the confidence marker off a sentence and leaves the claim standing; an inference paragraph loses its `(inference)` label in a reformat and reads as fact. Both fail in the room, not on the page.

| Row | Check | Blocking |
|:--|:--|:--|
| 5.1 | **Company / organisational context present** (§3) — who they are, ownership or legal structure, and at least one **dated** financial or programme-status data point with the release date of its source. A figure with no date fails | No |
| 5.2 | **Entity / business-unit coverage** (§4) where the organisation runs multiple operating businesses — one block per entity, plus the closing "reading this as a set" synthesis. `N-A` for a single-entity employer | No |
| 5.3 | **One profile per confirmed panellist** (§5), each carrying confirmed biography, career history, likely lens and a tailored connection point | No |
| 5.4 | **Every inference labelled as inference** — each speculative claim in its own paragraph under a bolded `(inference)` lead-in; §5 opens with the sourcing-disclaimer blockquote | **Yes** |
| 5.5 | **Every factual claim carries a confidence marker** — confirmed / independently corroborated / reasonably corroborated / reported via secondary sources / not confirmed. An unmarked **person**-claim escalates to 5.6 and blocks | No |
| 5.6 | **No unsourced person-claims** — every claim about a named individual states its source in the same sentence; every unverifiable fact is named as unverified rather than guessed | **Yes** |
| 5.7 | **Sources split internal / web, both dated** — internal block first, then a separately headed **dated** web-research block with full URLs, each annotated with what it confirmed | No |
| 5.8 | **Domain-term explainers where jargon is used** — any term belonging to the employer's world carries a short explainer: what it is, which part matters here, what it means in practice | No |
| 5.9 | **Cross-round information hygiene** (multi-round packs only) — earlier-round intel is not carried into a later round's brief, the boundary is stated as an explicit directive, and the clean generic answer to "what did you discuss last round?" is pre-scripted. `N-A` for a single-round pack | **Yes** |

**Checklist rows.** Emit these as rows `5.1`–`5.9` immediately after the Check 4 rows, each with its quote or count as evidence. They are **additional to** the core count and to Check 4's nine PDF rows — append `· research rows: 9` to the self-audit line. An `UNVERIFIED` research row blocks exactly as any other.

**Blocking semantics.** Rows **5.4, 5.6 and 5.9 block delivery** — an unlabelled inference read back as fact, a person-claim the candidate cannot source when challenged, and intel carried into a room it does not belong in are the three findings that can embarrass them live rather than merely thin the pack. The rest are advisory depth and traceability findings. Fix the **Markdown source** and re-run; never patch the verdict.

## Check 6 — Panel-room calibration and record consistency

**Applies** to any prep deliverable carrying an executive summary or a pre-prepared spoken response. **Skip only** for a practicalities-only artefact with no executive summary and no spoken content; say so and emit the rows as `N-A`. Individual rows scope out on their own terms: 6.1, 6.3 and 6.5 are `N-A` where the interviewer is a single unnamed person; 6.9 is `N-A` only where **nothing** has yet been submitted for the role.

Load the panel-room half of `candidate-voice/references/interview-prep-template.md` — §2 (executive summary as a decision instrument), §X (cross-artefact consistency), §8 (attribution and its caveat), §9 (coaching-note elements, depth calibration, honest-gap doctrine) and §10 (round-dependent salary coaching) — then verify **against the prep document text and against the submitted artefacts**, not against intent.

Checks 1–5 verify that the pack is well built. Check 6 verifies that it is built **for this room**, and that it does not contradict what the candidate has already put in writing to these same people. The two failures it catches are different in kind: a pack that is generically excellent but says nothing about who is asking, and a pack whose spoken figures have drifted from the application the panel is holding.

| Row | Check | Blocking |
|:--|:--|:--|
| 6.1 | **"What this round is for" names every lens in the room** — one clause per named panellist saying what each is testing, closing on the instruction a heterogeneous panel produces. `N-A` for a single unnamed interviewer | No |
| 6.2 | **Decisions and actions are directives, not observations** — imperative voice throughout; where a fit gap exists, one bullet states its **placement** ("plant it early and once, not defensively when pressed"); an executive or final round carries a close directive ("close on forward commitment, not gratitude") | No |
| 6.3 | **Core-risks table present, and every mitigation names the exact section or STAR to deploy** — 3–6 interview-specific rows; where the panel is named, risks attributed to the panellist whose probe produces them. A mitigation that only reassures ("stay calm", "be specific") fails | No |
| 6.4 | **Time-budget arithmetic stated, and Section B reconciles to it** — duration × panellists → expected question count → the delivery directive that follows. "Time will be tight" with no numbers fails | No |
| 6.5 | **Questions and STARs attributed per panellist, with the attribution caveat** — Section B rows and Section C headings tagged with the likely asker or the panellist the answer lands hardest with, plus the standing caveat that attribution is probability, not guarantee. Attribution with no caveat fails | No |
| 6.6 | **Every honest-gap or hard-gap response carries an explicit prohibition list** — the coaching notes name what must **not** be claimed anywhere in that answer, with the reason, and forbid any softening frame that would be untrue. Where a submitted artefact deliberately withheld a claim, that restraint appears here as a prohibition | **Yes** |
| 6.7 | **Coaching notes carry delivery discipline and a don't-invent directive with the substitute line supplied** — how it is said, not only what is said; and for every follow-up that would tempt an invented specific, the replacement sentence is written out. A prohibition with no substitute is a finding | No |
| 6.8 | **Rehearsal priority ranked across the pack** — at least the top two highest-risk responses named in rank order, with a rehearsal directive on each. A pack where every STAR is flagged "practise this" fails; that is not a ranking | No |
| 6.9 | **Cross-artefact consistency reconciled against every submitted artefact** — letter or statement of claims, screening responses (final submitted text), messages to the hiring team, the resume version sent, and every prior-round brief. Same organisation, same figures, same sequence, same admission, same words for the gap. Responses that are the verbal version of something on record say so in their coaching notes, and the drift risk is a standing row in the core-risks table | **Yes** |
| 6.10 | **Salary coaching matches the round type** — recruiter screen: reflect-first plus market research, engagement mechanics where non-standard, and the watch-out that the call must not end without a ballpark; behavioural panel: reflect-first, research table dropped unless the band moved; executive/final panel and fit round: salary is unlikely to arise and the candidate should not raise it | No |

**Checklist rows.** Emit these as rows `6.1`–`6.10` immediately after the Check 5 rows — **additional to** the core count, Check 4's nine PDF rows and Check 5's nine research rows. Append `· calibration rows: 10` to the self-audit line.

**Blocking semantics.** Rows **6.6 and 6.9 block delivery.** 6.9 blocks because contradicting your own submitted application in front of a panel that has read it is unrecoverable in the room — no follow-up answer repairs it, and the hiring manager who wrote the questions from that application is the person who notices. 6.6 blocks because the honest-gap answer is by construction the highest-risk response in the pack, and an unbounded one invites exactly the overclaim the honest framing exists to prevent — one sentence of manufactured experience in front of the person who owns that domain costs more than a thin answer ever does.


---

## Consolidated report format

```
## Prep gate — [Role Title], [Organisation] · [format]
**Measured pace:** [N] wpm · **Time budget:** [per the format] · **Matched row:** [ID]

### 1. STAR audit — [PASS / ADVISORY / BLOCK]
(findings per STAR: which of the six rules, the exact quote, the fix)

### 2. Pace audit — [PASS / ADVISORY / BLOCK]
| Response | Spoken words | At [N] wpm | Budget | Over/under | Verdict |

### 3. Capability mapping — [PASS / ADVISORY / BLOCK / SKIPPED (no formal framework)]
(component coverage, every Watch with its named pivot story)

### 4. Annotation PDF — [PASS / BLOCK / N-A (Markdown-only)]
(command output per geometry check)

### 5. Research depth and sourcing — [PASS / ADVISORY / BLOCK / N-A (practicalities-only)]
(sections 3–6 present / conditional-and-skipped-with-reason / missing; unmarked claims quoted;
unlabelled inferences quoted; unsourced person-claims listed by individual)

### 6. Panel-room calibration and record consistency — [PASS / ADVISORY / BLOCK / N-A]
(executive-summary components present / missing; unattributed risks and pointer-less mitigations named;
time-budget arithmetic quoted or flagged absent; responses missing a prohibition list listed by C-number;
**artefacts reconciled, listed by filename, with every drifted figure quoted from both sides**;
salary posture vs round type)

### Verification checklist (MANDATORY — emit in full)
| # | Check | How verified (command / quote / count) | Result | Verdict |
(rows 1.<star>.1–.6 per STAR, 2.1–2.R, 3.1–3.6 plus one row per Watch, 4.1–4.9, 5.1–5.9, 6.1–6.10 —
see references/checklist.md; no row omitted)

### Self-audit
Checklist rows emitted: [X]. Rows required: (6 × S=[s]) + R=[r] + 6 + W=[w] = [Y] · PDF rows: 9 · research rows: 9 · calibration rows: 10. Match: [yes/no].

### Gate verdict
[DELIVER / AMEND (advisory — the candidate decides) / BLOCKED (name the blocking finding)]
Blocking semantics: High STAR findings, any response >25% over budget, any missing mapping component
or unpivoted Watch, any unlabelled inference, unsourced person-claim or cross-round intel leak, any
honest-gap response with no prohibition list, and any drift between a spoken response and a submitted
artefact block delivery. Any `UNVERIFIED` row blocks until it is evidenced. Re-run the full gate after
every reshape.
```
