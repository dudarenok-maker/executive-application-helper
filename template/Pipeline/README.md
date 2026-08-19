# Pipeline — resume and letter build system

Single-source `.md → Jinja2 HTML → WeasyPrint → PDF` production for **both** the resume and
cover letters, under one shared design system (`brand.css`). This folder is a working scaffold, not
a stub: `build.py`, `brand.css` and the two HTML templates run as shipped once the dependencies
are installed and the placeholders are replaced.

> **Setup note.** Two placeholders must be replaced before first use:
> 1. `brand.css` — the running-footer rule renders `[Candidate Name]` literally. Replace it with the
>    candidate's name (search `content: "[Candidate Name]`).
> 2. The accent colour, typeface and page geometry are the shipped defaults. Re-skin freely — the
>    templates and `build.py` do not depend on the colour choices.

---

## Why a pipeline at all

Before this layer existed, the framework carried a resume in two places (a designer-tool PDF and a
divergent Markdown copy) and produced letters from a near-empty Word template with no contact
header. Both drifted. The pipeline replaces that with **one source file per artefact**:

| Artefact | Single source | Output |
|---|---|---|
| Resume | `Resume_Master.md` (workspace root) | `Resume/*.pdf` — master, named variants, `--short` 2-page cut |
| Cover letter | a per-application `.md` in this folder | review `.docx` first, then the final `.pdf` in `Submissions/` |

Variants are **front-matter entries in the single source**, never separate files. A named variant may
override the headline, the profile paragraph, the credentials line and the ordering of career
highlights — nothing else. If you find yourself wanting a second resume file, the answer is a new
variant block.

## Contents

| File | Purpose |
|---|---|
| `brand.css` | The design system: A4 `@page` geometry (resume 18/19/20 mm; letter 23/23/24 mm), running footer with the candidate's name (suppressed on letter page 1), serif stack, heading / role / highlight / letter components, `page-break-inside: avoid` on role blocks and on the letter's closing-paragraph + sign-off group. |
| `resume_template.html` | Jinja2 resume template: header and contact, profile, two-column highlights grid, credentials bar, employment (consecutive roles at the same employer render under one employer heading), education, capability snapshot. Optional sections collapse cleanly when absent. |
| `letter_template.html` | Jinja2 letter template: letterhead (name band + one contact line), date, recipient block, optional salutation, Markdown body, sign-off. |
| `build.py` | CLI entry point. |
| `styles/*.css` | Optional alternate design overrides loaded after `brand.css` via `--style`. Ships empty — add your own if you want more than one look. |

## Where files live (`Pipeline/` is toolchain only)

**`Pipeline/` holds the build system and nothing else.** The entries in the Contents table above —
`brand.css`, `resume_template.html`, `letter_template.html`, `build.py`, `README.md` and `styles/` —
are the complete permitted contents. Anything else in this directory is a stray and belongs
somewhere below.

| Artefact | Lives in | Named |
|---|---|---|
| Letter Markdown source | `Submissions/` | `[Candidate Name] - [Title] - [Company] - Letter Source.md` |
| Selection Criteria Response Markdown source | `Submissions/` | `[Candidate Name] - [Title] - [Company] - Selection Criteria Response Source.md` |
| Stage 1 review copy (`--docx`) | `Submissions/` | `[Candidate Name] - [Title] - [Company] (DRAFT for review).docx` |
| Stage 2 final PDF | `Submissions/` | `[Candidate Name] - [Title] - [Company].pdf` |
| Screening questions / paste text | `Submissions/` | `… - Screening Questions.md`, `… - Paste Version.md` |
| Resume PDFs (all variants) | `Resume/` | `[Candidate Name] - Resume - [Variant or Role].pdf` |
| Superseded drafts, scratch, duplicate builds | an archive folder outside `Pipeline/` | as-is |

**Build from `Submissions/`, write back to `Submissions/`** — never into the working directory:

```sh
cd Pipeline
python3 build.py letter \
  --source "../Submissions/[Candidate Name] - [Title] - [Company] - Letter Source.md" \
  --band short \
  --out "../Submissions/[Candidate Name] - [Title] - [Company].pdf"
```

**Why this rule exists.** A build directory that also holds work product accumulates silently: draft
chains, superseded builds and scratch files pile up next to the toolchain until nobody can tell which
file was actually submitted. Keeping `Pipeline/` to the toolchain means the answer to "what did we
send?" is always a single folder, and a stray in `Pipeline/` is visibly a stray rather than a
candidate for the real thing. Archive strays; never delete them — a superseded draft is cheap to keep
and expensive to reconstruct.

## Dependencies

- Python 3.10+ with `weasyprint`, `jinja2`, `markdown`, `pyyaml`.
- `pandoc` for the letter `--docx` export (Stage 1 review copy).
- A serif font family available to the renderer (the CSS names a primary and a fallback).
- Validation tools: `pdfinfo`, `pdftotext`, `pdffonts` (poppler-utils).
- **No network access is required at build time** — deliberate, so a build never depends on a CDN.

## Usage

```sh
cd Pipeline

# resume
python3 build.py resume --source ../Resume_Master.md \
    [--variant <name>] [--short] [--style <name>] [--out out.pdf]

# letter — --band is REQUIRED; the build prints page count and body word count,
# and warns when the body falls outside the band
python3 build.py letter --source letter.md --band short|long [--out out.pdf] [--docx]
```

- `--variant` — a named entry under `variants:` in the resume front-matter.
- `--short` — 2-page mode. Compresses the **same** source at build time; there is no second source.
- `--band` — `short` = 350–550 body words (private-sector / recruiter / job-board briefs);
  `long` = 900–1,250 (public-sector / criteria-driven). Out-of-band bodies still render, but warn.
- `--docx` — pandoc export for the Stage 1 review copy and for portals that demand Word.

## Resume source format (`Resume_Master.md`)

YAML front-matter (identity, contact, headline, credentials, `variants:`) followed by Markdown
sections: `## Profile`, `## Career highlights`, `## Experience`, `## Education`,
`## Capability snapshot`. A skeleton with every field annotated ships as `Resume_Master.md` at the
template root — populate that rather than authoring from scratch.

Parsing rules worth knowing before you edit:

- Every `### ` role needs `Employer:` and `Dates:` metadata lines (hard errors if missing).
  `Location:`, `Context:` and `About:` are optional.
- Employer grouping is **consecutive-only**. Two spells at the same employer separated by a
  different employer render as two groups — chronology wins; do not interleave to force a group.
- Education bullets: `**Degree** — Institution (Year)`. Capability bullets: `**Label:** detail`.
- A blank line ends a bullet; indent continuation lines instead of starting a new `- `.

### Short mode (`--short`)

Page 1 is never trimmed — header, headline, contact, profile, the full highlights grid and the
credentials bar all survive. What gives way, in order: `Context:` lines (kept only on the most
recent role), `Location:` lines (dropped), bullet counts (most recent role 4, other roles 2, roles
starting more than ~12 years ago 1 — always the **first** N bullets, so author them strongest-first),
and the capability snapshot (one compact paragraph rather than one line per label). Type and
leading tighten as well. If content growth ever pushes short mode to three pages, tighten spacing
further — never trim page-1 content.

## Letter source format

```markdown
---
name: [Candidate Name]
contact:                       # list, or one "a | b | c" string
  - [email]
  - "[phone]"
  - [linkedin]
  - [city, country]
date: [D Month YYYY]           # optional
recipient:                     # optional; list or string
  - [Hiring Manager / Panel]
  - [Organisation, City]
salutation: "Dear [Name],"     # optional
signoff: "Yours sincerely,"    # default if omitted
signature: [Candidate Name]    # defaults to name
---
Body paragraphs, blank-line separated. **Bold lead-in phrases** survive to both PDF and docx.
No heading line — the letterhead carries the name.
```

## Two-stage letter delivery (mandatory)

The pipeline is wired for a two-stage handoff, and the order is not optional:

1. **Stage 1 — review copy.** After the voice audit and the draft gate, build the letter with
   `--docx` and give the candidate the **editable Word file**. Never hand over a PDF first: the
   candidate reads, and usually edits, before anything is final, and a PDF invites them to accept
   what they would otherwise have improved.
2. **Stage 2 — final PDF.** Fold their edits back into the Markdown source **verbatim**, re-check
   length if the edits were material, then build the final PDF into `Submissions/`.

The Markdown source stays authoritative. Edits that live only in the returned `.docx` are lost on
the next rebuild — and, worse, the candidate's own corrections are the highest-quality voice signal
the framework ever receives. Recurring patterns in those edits belong in the voice guide at the
maintenance step.

## Validation

```sh
pdfinfo out.pdf  | grep -E "Pages|Page size"   # expect A4 (595.276 x 841.89 pts)
pdftotext out.pdf - | head                     # clean text layer, correct reading order
pdffonts out.pdf                               # fonts embedded (emb = yes)
```

Targets: resume master ≤3 pages, `--short` exactly 2; long-form letter ≤2 pages with the sign-off
never orphaned; short-form letter 1 page.

## docx caveats

Pandoc renders from the same Markdown, so text, paragraphing and bold lead-ins are faithful. Lost
relative to the PDF: the letterhead band and accent styling, the chosen serif, justification, exact
margins and the running footer. The `.docx` is the review vehicle and the portal fallback. **The PDF
is the submitted artefact.**
