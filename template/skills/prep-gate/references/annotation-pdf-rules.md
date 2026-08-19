# Annotation PDF — operating rules (e-ink tablet)

**What this is.** The complete, self-contained rule set for producing a PDF the candidate will annotate by hand on an e-ink tablet (reMarkable Paper Pro or equivalent). Every prep deliverable, briefing or research document destined for PDF follows these rules by default. If the candidate wants different geometry for a specific deliverable, ask once at kickoff and lock it in for that session.

**Where these come from.** Accumulated prep-output conventions, each added after a real delivery defect: a brief that could not be annotated because the right margin was too narrow, a STAR split across a page break mid-answer, a footnote the candidate could not follow on a device with no second screen, a table that ran off the page. **This file is the operating home for all of them** — the rules are reproduced here in full, including the canonical YAML block, so that a prep PDF can be built from this file alone. If you keep a separate copy of the YAML elsewhere in the workspace for reuse, that copy must stay in sync with Section 3 below.

---

## 1. Paired output — Markdown source, PDF deliverable (Convention 1)

Generate the Markdown source (`.md`) first, then convert to PDF **in the same session**. Both files land in `Interview Prep/` (or the relevant sub-folder for the deliverable category). Same base name; only the extension differs.

- **The PDF is the file the candidate actually uses.** The Markdown is the editable source.
- Naming: `[Candidate Name] - [Format] Prep - [Role] - [Organisation].md` (+ `.pdf`).
- Never deliver the Markdown alone. A prep deliverable without its PDF is incomplete.

## 2. Page geometry (Convention 2)

| Setting | Value | Why |
|:-----------------|:-------------------------------|:------------------------------------------------------------------|
| Paper | A4 portrait, 210 × 297 mm | reMarkable Paper Pro native reading size |
| Top margin | 20 mm | |
| Bottom margin | 20 mm | |
| Left margin | 20 mm | |
| **Right margin** | **40 mm** | **the wide margin is the handwriting gutter — this is the whole point** |
| Body size | 11 pt | legible under stylus annotation |
| Line stretch | 1.35 | leaves room to write between lines |
| Body font | Liberation Serif | or equivalent system serif |
| Heading font | Liberation Sans | or equivalent system sans |
| Running header | short title left, `Page N` right | orientation when flicking through a 20-page pack |

The 40 mm right margin is non-negotiable. If a built PDF's text block runs closer than ~38 mm to the right edge, the geometry did not apply — check the YAML.

## 3. The canonical YAML block

Copy verbatim into the top of the Markdown. Replace the `[REPLACE: ...]` placeholders with role-specific values.

```yaml
---
title: "[REPLACE: Document short title, e.g. Panel Interview Brief — [Role Title], [Organisation]]"
author: "Prepared for [Candidate Name]"
date: "[REPLACE: Interview date and time, e.g. Interview: Tuesday 26 May 2026, 12:00 AEST (Microsoft Teams)]"
documentclass: article
geometry:
  - paperwidth=210mm
  - paperheight=297mm
  - top=20mm
  - bottom=20mm
  - left=20mm
  - right=40mm
fontsize: 11pt
linestretch: 1.35
mainfont: "Liberation Serif"
sansfont: "Liberation Sans"
monofont: "Liberation Mono"
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyhead[L]{\small [REPLACE: Document short title for running header, e.g. Panel Interview Brief — [Organisation]]}
  - \fancyhead[R]{\small Page \thepage}
  - \fancyfoot[C]{}
  - \renewcommand{\headrulewidth}{0pt}
  - \usepackage{pdflscape}
  - \usepackage{titlesec}
  - \titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
  - \titleformat{\subsection}{\large\bfseries}{\thesubsection}{1em}{}
  - \titlespacing*{\section}{0pt}{1.5em}{0.8em}
  - \titlespacing*{\subsection}{0pt}{1em}{0.5em}
---
```

## 4. Page breaks and Notes blocks (Convention 3)

**Every major section starts on a fresh page.** Executive summary, organisational context, each panel member, each STAR response, killer questions, quoted excerpts, panel-member voice samples, inline bank framings, risks and watch-outs, night-before checklist, sources.

- Use an explicit `\newpage` in the Markdown at each section boundary. Do **not** rely on a `---` horizontal rule — that renders as a rule, not a break.
- End each section with a **Notes** placeholder and vertical whitespace so the candidate can annotate under the content rather than only in the margin:

```markdown
**Notes**

\vspace{3.5cm}

\newpage
```

`\vspace{Ncm}` with N usually 3–8. 3.5 cm is the tested value for per-STAR notes strips; go larger (6–8 cm) for a section the candidate will work through slowly.

## 5. Footnote discipline (Convention 4)

Any directly quoted excerpt from an external article, report, audit, inquiry or person's public material carries a Markdown footnote marker (`[^label]`) **at the heading or quote where it appears**.

- Footnote definitions go in a **single block immediately before the `# Sources` heading**.
- xelatex renders footnote text at the bottom of the page where the marker sits — the candidate opens the URL from the page being read, not by flicking to the back.
- The URL still appears in the Sources section for completeness. Both, not either.

## 6. Inline framings and research depth (Conventions 5 and 6)

These are content rules, but they exist *because* of the annotation use case — the candidate reads on a device with no parallel access to the bank, so the document must stand alone.

- **Convention 5 — inline framings.** When the deliverable cites a bank entry by ID ("use A11", "see B1-6"), reproduce that entry's core framing in full in a dedicated section, typically "Inline framings of referenced evidence-bank entries". One quoted paragraph plus a one-line "For [Organisation]:" calibration note.
- **Convention 6 — panel-brief research depth.** Panel briefs (not recruiter screens) additionally require: a direct quoted-excerpts section with per-page footnotes; a panel-member voice section with public material per panellist plus an inference paragraph on likely tone; and the inline-framings section above.

## 7. Paired brief and speaking-notes addendum (Convention 8)

For panel and executive-panel interviews, produce **two separate paired files**, each with its own `.md` + `.pdf`:

| File | Purpose | Contents |
|:-----------------------------|:-------------------------|:--------------------------------------------------------------------------|
| **Panel Interview Brief** | what the candidate studies | panel backgrounds, org context, quoted excerpts with footnotes, inline framings, capability mapping, full STAR catalogue, risks and watch-outs |
| **Speaking Notes Addendum** | what the candidate uses on the day | tailored responses in spoken cadence, `[pause]` / `[short pause]` markers, `[STOP — pass back to panel]` cues, on-the-fly drop lists |

Keep them separate so iteration on one does not disturb the other. Both follow every geometry and page-break rule above.

## 8. Proportional pipe-table separator dashes (Convention 12)

**Vary the dash count in the separator row to match each column's relative content width.** Equal separators (`|---|---|`) collapse every column to the same rendered width — narrow columns squeeze, wide columns waste page real estate. Use a leading colon (`:---`) for left alignment.

The rule is mechanical: count rough content length per column across the table's longest row, then set dashes proportionally — narrow columns ~5–10 dashes, wide columns 40–80.

Worked separators, tested in production packs:

- **2-column Question / Answer (long-form spoken response)**

  ```
  |:------------------------------------------|:----------------------------------------------------------|
  ```

- **2-column Risk / Mitigation**

  ```
  |:----------------------------------------|:----------------------------------------------------------------|
  ```

- **5-column # / Question / Lead with / Evidence / Time**

  ```
  |:--|:----------------------|:--------------------------------------|:----------------|:----------|
  ```

If a regenerated PDF shows column-width imbalance, the fix is almost always in the separator row, not in cell content.

## 9. Landscape rotation for wide tables (Convention 17)

When a table reads cramped in A4 portrait — the canonical case is the Section B "Likely questions" table, five columns with two prose-heavy — rotate **only that section** to landscape while the rest of the document stays portrait. Two mechanics, **both required**:

**(a) `\usepackage{pdflscape}` in `header-includes`.** Already in the canonical YAML above. It rotates the typeset content *and* the page-orientation flag, so the viewer shows it the right way up.

**(b) Wrap the section in explicit raw-LaTeX blocks — NOT a bare `\begin{landscape}` / `\end{landscape}` pair.**

> **The `#`-column build trap.** A bare environment pair on its own lines makes pandoc treat *everything between them* — heading and Markdown table — as a single raw-LaTeX span. The table is passed through verbatim, the literal `#` in the `| # |` header column reaches LaTeX as a macro-parameter character, and the build fails with:
>
> `! You can't use macro parameter character # in vertical mode.`

Emit each landscape command as its **own** raw-LaTeX block so pandoc still parses the Markdown between them:

````markdown
```{=latex}
\begin{landscape}
```

## B. Likely questions — positioning notes

| # | Likely question | Lead with | Evidence anchor | Time |
|:--|:-------------------------|:--------------------------------------------|:----------------|:--------|
| … table rows … |

```{=latex}
\end{landscape}
```
````

**Pair with Convention 12 inside the block.** Landscape gives more width but does not fix *relative* column sizing — pandoc still distributes width by dash count. The five-column separator above is the tested layout: the narrow `#` index collapses to a thin strip and the prose columns take the freed width.

## 10. No orphaned semi-empty pages (Convention 19)

`pdflscape` always starts the landscape environment on a fresh page and returns to portrait on a fresh page afterward. That is unavoidable. What **is** avoidable is stranding a short paragraph — an intro blurb, a "Discipline note", a one-line caveat — alone on the portrait page immediately *after* the landscape block ends, when it could sit on the portrait page immediately *before* the block begins alongside that section's other intro text.

**Rule.** Draft any section-level commentary that is not part of the table itself (framing sentence, discipline note, caveats) so it lands *before* `\begin{landscape}`, never after `\end{landscape}`. Then **verify page-by-page in the built PDF before delivery** — if a short paragraph is sitting alone on its own page right after a landscape section, move it to before the section starts.

Applies to **any** forced-break construct, not just landscape tables — including a `\newpage` placed for section separation that leaves a near-empty trailing page.

Verification command — per-page character counts, flag anything unexpectedly light:

```bash
pdftotext -layout "output.pdf" - | awk 'BEGIN{RS="\f"} {gsub(/[ \t\n]/,"",$0); printf "page %2d: %5d chars\n", NR, length($0)}'
```

A body page normally lands 700–2,800 characters. **Anything under ~500 is a candidate orphan** — open it and check. Intentional exceptions: a title page, or a deliberate Notes-only page in a reMarkable Edition (see below).

This rule exists because of a real delivery: a prep pack shipped with a short "discipline note" stranded alone on the page following a landscape table, producing two near-empty pages where one consolidated page would have done. The reader on an e-ink device pays for every page turn.

---

## 11. reMarkable Edition variant

> **Codified from practice.** This variant was built repeatedly from a verbal request before anyone wrote it down — which is the usual life cycle for a rule in this framework, and the reason the transform kept coming out slightly differently each time. The steps below are the observed build, not an aspiration.

**What it is.** A second, more spacious edition of an existing prep pack, built **alongside — not replacing** the standard edition. The two serve different purposes: the standard edition for a fast pre-call read, the annotation edition for live handwritten notes. Expect the annotation edition to run roughly 20–25% longer in pages.

**Trigger.** The candidate asks for "a reMarkable version", "each STAR on its own page", or "so I can do handwritten notes".

**Build steps** — a scripted transform of the base prep Markdown, not a rewrite:

1. **File naming.** Base name + ` - reMarkable Edition.md` / `.pdf`, in `Interview Prep/`. Leave the standard edition in place untouched.
2. **Title.** Append ` (reMarkable Edition)` to the YAML `title`.
3. **Running header.** Append ` -- reMarkable Edition` to the `\fancyhead[L]` short title (LaTeX en-dash — not a literal em-dash).
4. **Declare the edition.** One line under the executive summary, e.g. *"**reMarkable Edition:** each Section C STAR is on its own page with a blank Notes area at the bottom for handwritten annotation before the call."*
5. **Replace section-boundary `---` rules with `\newpage`.** Every major section (organisational context, bridging table, Sections A/B/C/D/E, Sources) starts on a fresh page.
6. **One STAR per page.** Insert `\newpage` before each STAR from the second onward (C2, C3, …). **The first STAR stays on the page with the Section C intro** — a section opening that strands its own heading reads as an error, not as spacing.
7. **Notes strip after every STAR.** After each STAR's coaching notes, append:

   ```markdown
   **Notes**

   \vspace{3.5cm}

   \newpage
   ```

8. **Amend the Section C intro line** to say the layout out loud — e.g. *"…each on its own page with a Notes strip at the bottom for last-minute handwritten annotation."*
9. **Atomic-save the transform (Convention 10).** Save after each successful edit in the script, not at the end, so a later assertion failure does not roll back earlier good edits.
10. **Verify.** `pdftotext -layout` and confirm each STAR lands as a standalone page and the next section starts cleanly on a page of its own.

The 40 mm right-margin gutter still applies — the Notes strips are **in addition to** the margin, not a replacement for it.

---

## 12. Build and verify

**Build (Convention 7).**

```bash
pandoc "input.md" -o "output.pdf" --pdf-engine=xelatex --validate false
```

Use `--validate false` only where a known-benign validation warning would otherwise mask a real one — and say why in the report.

**Verify — run all four before delivery.**

```bash
# 1. Geometry: A4 portrait, expected page count
pdfinfo "output.pdf" | grep -E "^(Pages|Page size|Page rot)"
#    expect: Page size 595.28 x 841.89 pts (A4), Page rot 0
#    (landscape sections legitimately report rot 90 on those pages)

# 2. Right margin: text block must stop ~40mm short of the right edge
pdftotext -bbox "output.pdf" - | grep -o 'xMax="[0-9.]*"' | tr -cd '0-9.\n' | sort -n | tail -1
#    A4 width 595.28 pts; (210-40)/210 * 595.28 = 481.9 pts.
#    Expect max xMax ~482-490 (a few pts of glyph overshoot is normal).
#    A value near 560 means the 40mm right margin did NOT apply.

# 3. Page-by-page content: section starts, and Convention 19 orphan check
pdftotext -layout "output.pdf" - | awk 'BEGIN{RS="\f"} {gsub(/[ \t\n]/,"",$0); printf "page %2d: %5d chars\n", NR, length($0)}'
#    flag any page under ~500 chars

# 4. Read the light pages and the section boundaries
pdftotext -layout "output.pdf" - | awk 'BEGIN{RS="\f"} {print "===== PAGE " NR " ====="; print}' | less
```

If any check fails, fix the **Markdown source** and rebuild. Never hand-patch the PDF.

---

## 13. Pre-delivery checklist

Run this against every prep deliverable destined for PDF:

- [ ] `.md` and `.pdf` both exist in `Interview Prep/`, same base name (Conv 1)
- [ ] YAML copied from Section 3 of this file, all `[REPLACE: ...]` placeholders filled (Conv 2, 7)
- [ ] Built PDF is A4 portrait; text block stops ~40 mm short of the right edge (Conv 2)
- [ ] Running header shows short title left, `Page N` right, on every page (Conv 2)
- [ ] `\newpage` at **every** major section boundary — no `---` rules doing the job (Conv 3)
- [ ] **Notes** placeholder + `\vspace{Ncm}` at the foot of each section (Conv 3)
- [ ] Every external quote carries a `[^label]` marker; definitions block sits immediately before `# Sources`; URLs also in Sources (Conv 4)
- [ ] Bank entries cited by ID have their framing reproduced inline (Conv 5)
- [ ] Panel briefs only: quoted excerpts, panel-member voice, inline framings all present (Conv 6)
- [ ] Panel interviews only: brief and speaking-notes addendum exist as separate paired files (Conv 8)
- [ ] Every pipe table uses proportional separator dashes, never `|---|---|` (Conv 12)
- [ ] Landscape sections wrapped as **two separate** ` ```{=latex} ` raw blocks, not a bare environment pair (Conv 17)
- [ ] No section commentary stranded after `\end{landscape}`; no page under ~500 chars that is not deliberate (Conv 19)
- [ ] reMarkable Edition only: title and header suffixed, one STAR per page from C2 onward, Notes strip after each STAR, standard edition left in place (Section 11)
