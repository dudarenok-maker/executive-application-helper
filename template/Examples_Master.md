# Examples, Responses and Positioning Statements — Master Retrieval File

**Owner:** [Candidate Name]
**Document type:** Reusable evidence bank and drafting reference (operating layer)
**Last full review:** [YYYY-MM-DD]
**Structure:** Split into one Master file (this document) plus the companion section files listed in the file map below.
**Changelog:** See `Evidence_Bank_Changelog.md` in this project.

---

## Purpose and audience

| | |
|---|---|
| **Purpose** | Provide reusable positioning blocks, evidence-led examples, and draft templates that can be quickly adapted for different roles. |
| **Primary audience** | Claude, when drafting applications, briefing notes, recruiter responses and interview prep. [Candidate First Name], when editing and reviewing. |
| **Best use** | First reference point when drafting cover letters, statements of claims, targeted pitches, recruiter responses, interview responses, and resume tailoring. |
| **Design principle** | Keep each example short, evidence-rich, and easy to tailor. Separate reusable examples from role-specific templates and optional personal content. Structure is optimised for Claude retrieval, while remaining readable and editable for a human author. |

---

## 0. Quick-start retrieval protocol (for Claude)

This evidence bank supports **two workflows** that draw on the same entries: **application drafting** (cover letters, statements of claims, targeted pitches) and **interview preparation** (STAR-style prep documents for recruiter screens, behavioural panels and executive panels). The protocol below applies to both. Workflow-specific voice baselines and output structures live in the `candidate-voice` skill.

**Retrieval is index → row.** The family matrices in Section 5 are slim **indexes**; the full prescription for a matched archetype lives in its own file under `Matrix_Rows/`. Match on the index, then open only the row(s) you matched. This exists because loading a whole family matrix to use one row is how a session's context budget disappears before the drafting starts.

**Before drafting any application OR preparing any interview, Claude follows this sequence:**

1. **Always load this file (`Examples_Master.md`)** — Sections 0, 1.1, 3, and the Section 5 preamble and family-pointer table. This is the operating layer: protocol, entry format, controlled vocabulary, master index, family pointers.
2. **Read the role materials** (advertisement, position description, candidate pack, recruiter instructions, attachments).
3. **Identify the role family** from Section 3.1. If the brief blends two families in equal weight, go to the **cross-family hybrid index first**, before either family's own default.
4. **Open the matched family's index file** and pattern-match the brief against the `Pattern (distilled)` column. Use `Notes` for tie-breaks between adjacent rows.
5. **Open only `Matrix_Rows/<ID>.md` for the matched ID(s).** That file carries the full prescription — pattern, positioning (A-IDs with the dominant flagged), body stacks (B-IDs by paragraph), template and length band, fit-acknowledgment style, AI register, companion files, notes. It is the drafting or prep plan; follow it rather than re-deriving one.
6. **Extend with Section 4 (master index)** — filter by capability, sector and tier for role-specific proof points beyond the row's stack.
7. **Cross-check Section 7 (watch-outs)** for framing constraints on the chosen entries, and Section 6 for metric consistency.
8. **Load only the companion files the matched row names.** Never load all section files by default.
9. **Report the proposed evidence set** to [Candidate First Name] in the pre-drafting assessment before drafting.

No row matches cleanly → check the cross-family index, then the family's `-DEFAULT` row. If neither fits, say so in the assessment, propose the closest analogue, and create a new row per the second-occurrence policy in Section 5.

After the deliverable is finalised, run the **maintenance step** (Step 4 in `Project_Instructions.md`). Both workflows feed the same evidence-bank changelog and the same commit.

---

## 1. How this document is structured

The evidence bank is split into a Master file (this document) and companion section files. The Master file contains the operating layer (retrieval protocol, formatting rules, controlled vocabulary, master index, the family-pointer table, signature metrics, watch-outs). The role-family matrices themselves live outside it — a slim index per family, and one detail file per archetype under `Matrix_Rows/`. The entry bodies sit in the companion section files and are loaded on demand.

### 1.1 File map

> **Setup guidance:** If the capability domains are renamed, added to or removed during setup (renaming B1, adding B7, removing B3), update this table to match. The "Load when" column is the trigger for Claude to open that file.

| File | Section | Contents | Load when |
|---|---|---|---|
| `Examples_Master.md` (this file) | 0–7 | Retrieval protocol, formatting rules, tag vocabulary, master index, family-pointer table, signature metrics, watch-outs | **Always** |
| `Resume_Master.md` | — | Single source of truth for career history and metrics; drives every resume build | **Always** |
| `Examples_Section_5_*.md` | 5 | Slim role-family **indexes** — one table row per archetype | The matched family only |
| `Matrix_Rows/<ID>.md` | 5 | The full prescription for one archetype | The matched ID(s) only — never the folder |
| `Examples_Section_A_Positioning.md` | A | Core positioning blocks (A1, A2, …) — identity, motivation, leadership approach, onboarding | Almost always — positioning is relevant to nearly every draft |
| `Examples_Section_B1.md` | B1 | [Default: Strategy, governance and investment — rename per setup] | When the matched row names it |
| `Examples_Section_B2.md` | B2 | [Default: Delivery, operations and modernisation — rename per setup] | When the matched row names it |
| `Examples_Section_B3.md` | B3 | [Default: Procurement, shared services and vendor management — rename per setup] | When the matched row names it |
| `Examples_Section_B4.md` | B4 | [Default: Risk, cyber, information governance and AI — rename per setup] | When the matched row names it |
| `Examples_Section_B5.md` | B5 | [Default: People, culture and organisation capability — rename per setup] | When the matched row names it |
| `Examples_Section_B6.md` | B6 | [Default: Commercial, customer and growth — rename per setup] | When the matched row names it |
| `Examples_Section_C_Templates.md` | C | Ready-made templates (C1–C6 or as configured) | Once the document format is known |
| `Examples_Section_D_E_Personal_Maintenance.md` | D, E | Optional personal content (D1) + maintenance notes (E1–E3) | D: only on an explicit recruiter request. E: at the maintenance step |
| `Pipeline/` | — | Resume and letter production (`build.py`, `brand.css`, templates) | Any output build |

### 1.2 Sections in this Master file

| Section | Purpose |
|---|---|
| **0** | Quick-start retrieval protocol (index → row). |
| **1** | Structure overview + file map. |
| **2** | Entry formatting rules (applied inside the companion section files). |
| **3** | Controlled tag vocabulary (four dimensions). |
| **4** | Master index — one-row-per-entry scannable table. |
| **5** | Family-pointer table, matrix index format, and the second-occurrence row policy. |
| **6** | Signature metrics quick reference — top quantifiable outcomes. |
| **7** | Known gaps and watch-outs register — honesty boundaries. |

---

## 2. Entry formatting rules

Every entry in the Section A and Section B companion files uses the following structure. Entries in the Section C file may condense some fields where a template is format-only.

| Field | Rule |
|---|---|
| **Heading** | Capability-based title, not role-specific (e.g. "Budget ownership at scale", not "[Specific organisation] budget example"). |
| **Tier** | Primary, Secondary or Supporting. Primary = strongest evidence and most versatile; Secondary = good but narrower; Supporting = niche, older or depth-only. |
| **Last updated** | ISO date (YYYY-MM-DD). Claude flags entries older than 12 months for review on next use. |
| **Tags** | Four controlled dimensions (see Section 3): Role families, Capability, Sector, Anchor organisation. |
| **Primary / Secondary example** | Name the strongest anchor organisation first. Add a secondary only where it adds breadth or contrast. |
| **See also** | Cross-references to related entries (by ID). |
| **Best used for** | List the role families or criteria the example supports. |
| **Core response** | 120–180 words. Reads cleanly as a direct answer; suitable for cover letters or statements of claims. |
| **Proof points** | 3–5 bullets with quantifiable facts, delivery metrics, governance forums, scale, budgets, or outcomes. Entries may carry more where the added detail preserves reusability and quality — do not compress for its own sake. |
| **Cautions** | Framing limits so the example is used honestly and credibly. |

**Formatting notes:**
- Write one polished answer first, then add proof points, tags and cautions.
- Avoid storing raw prompts or half-finished notes inside the main evidence bank.
- For high-scrutiny roles (regulators, integrity bodies, public-trust environments), use compliance-facing, legally sensitive, public-trust and governance examples where they are the strongest honest fit. Do not imply specialist regulatory expertise unless it is clearly evidenced. Rely on transferability, judgement, governance, and public-value outcomes rather than constructed adjacency.

---

## 3. Controlled tag vocabulary

Tags are drawn from four closed dimensions. New tags are added only by agreement (see maintenance protocol in the project instructions).

> **Setup guidance:** Populate each dimension with the candidate's actual list. The lists below show structural shape only — replace with the candidate's real role families, capabilities, sectors and anchor organisations.

### 3.1 Role families

> **Setup guidance:** List the role families the candidate is targeting or could credibly apply for. Three to seven families is typical. Examples for an executive: "CIO / CTO / CDO", "COO / GM Corporate", "SES / equivalent senior public-sector tier", "Product Director / CPO", "Consulting Director", "[Sector-specific senior tier]".

- **[Role family 1]**
- **[Role family 2]**
- **[Role family 3]**
- **[Role family 4]**
- **[Role family 5]**

### 3.2 Capability

> **Setup guidance:** Capability is the most important tag dimension — it drives retrieval. Mirror the capability domains the candidate locked in during setup (B1–B6). Use the canonical full label here; the master index in Section 4 uses shorter scannable forms.

The canonical capability vocabulary used in entry tags is the consolidated list below.

- **[Capability 1 canonical label]** (short form: [short form])
- **[Capability 2 canonical label]** (short form: [short form])
- **[Capability 3 canonical label]** (short form: [short form])
- **[Capability 4 canonical label]** (short form: [short form])
- **[Capability 5 canonical label]** (short form: [short form])
- **[Capability 6 canonical label]** (short form: [short form])

When a new entry is created, use the canonical label in the entry's tag block, and the short form in the master-index row.

### 3.3 Sector

> **Setup guidance:** List the sectors / jurisdictions the candidate has worked in or targets. Examples: "Public sector — Federal", "Public sector — State", "Private — corporate", "Private — SMB", "NFP", "Cross-sector".

- [Sector 1]
- [Sector 2]
- [Sector 3]
- [Sector 4]
- Cross-sector

### 3.4 Anchor organisation

> **Setup guidance:** List the organisations the candidate's strongest evidence is anchored to. Use the names that will appear in the entry tags. Include "Multi-role" as a valid anchor for blended cross-role summaries (positioning blocks, leadership approach, etc.).

- [Anchor org 1]
- [Anchor org 2]
- [Anchor org 3]
- [Anchor org 4]
- [Anchor org 5]
- Multi-role (for blended cross-role summaries)

### 3.5 Master-index short codes

The master index in Section 4 uses short codes to keep the scannable rows compact. These codes are used **only in Section 4**. Everywhere else — Section 3.1–3.4 above, the family indexes and `Matrix_Rows/` files, and the companion-file entry metadata blocks — the canonical full labels remain in force.

> **Setup guidance:** Add a short code for every role family, capability and sector defined above. Anchor organisations are usually short enough to leave in full form.

**Role families**

| Short code | Full label |
|---|---|
| [Code] | [Full label] |
| [Code] | [Full label] |
| [Code] | [Full label] |
| All | All role families |

**Capability**

| Short code | Canonical capability |
|---|---|
| [Code] | [Canonical label] |
| [Code] | [Canonical label] |
| [Code] | [Canonical label] |

**Sector**

| Short code | Full label |
|---|---|
| [Code] | [Full label] |
| [Code] | [Full label] |
| All | Cross-sector |

**Anchor organisations** are left in full form because they are already short and stay readable at a glance.

**Maintenance rule:** if a new role family, capability or sector is added to Sections 3.1–3.3, a matching short code must be added to Section 3.5 in the same session. Do not use a short code in Section 4 that is not listed here.

---

## 4. Master index

Scannable one-row-per-entry index. Use to filter by Tier, Capability, Sector or Role family when selecting entries. The **File** column tells you which companion file to open for the full entry.

> **Setup guidance:** This index is empty until the section files are populated. Add one row per entry as you create it. The minimum information needed for retrieval is: ID, Title, Tier, Capability, Sector, Role families, Anchor org. Add a "File" column if it helps Claude navigate, or rely on the predictable mapping (B1-* → Examples_Section_B1.md, etc.).

### Section A — Core positioning blocks (file: `Examples_Section_A_Positioning.md`)

| ID | Title | Tier | Capability | Sector | Role families | Anchor org |
|---|---|---|---|---|---|---|
| A1 | [Title] | [Tier] | [Cap] | [Sector] | [Role families] | [Anchor] |
| A2 | [Title] | | | | | |
| A3 | [Title] | | | | | |
| A4 | [Title] | | | | | |
| A5 | [Title] | | | | | |
| A6 | [Title] | | | | | |
| A7 | [Title] | | | | | |
| A8 | [Title] | | | | | |
| A9 | [Title] | | | | | |
| A10 | [Title] | | | | | |
| A11 | [Title] | | | | | |
| A12 | [Title] | | | | | |

### Section B — Reusable evidence bank

Each B-subsection sits in its own companion file.

| ID | Title | Tier | Capability | Sector | Role families | Anchor org |
|---|---|---|---|---|---|---|
| B1-1 | [Title] | [Tier] | [Cap] | [Sector] | [Role families] | [Anchor] |
| B1-2 | [Title] | | | | | |
| B2-1 | [Title] | | | | | |
| B2-2 | [Title] | | | | | |
| B3-1 | [Title] | | | | | |
| B4-1 | [Title] | | | | | |
| B5-1 | [Title] | | | | | |
| B6-1 | [Title] | | | | | |

### Section C — Ready-made templates (file: `Examples_Section_C_Templates.md`)

| ID | Title | Length | Best used for |
|---|---|---|---|
| C1 | [Title — e.g. 400-word statement of claims] | 400 words | [Best used for] |
| C2 | [Title] | [Length] | [Best used for] |
| C3 | [Title] | [Length] | [Best used for] |
| C4 | [Title] | [Length] | [Best used for] |
| C5 | [Title] | [Length] | [Best used for] |
| C6 | [Title] | [Length] | [Best used for] |

### Section D — Optional personal content (file: `Examples_Section_D_E_Personal_Maintenance.md`)

| ID | Title | Use |
|---|---|---|
| D1 | Optional personal note | Only where a recruiter explicitly asks for personal background. |

---

## 5. Role-family matrices — index and row files

Section 5 is a **pointer layer**, not a content layer. The archetype prescriptions live in two places:

| Layer | File | Loaded |
|---|---|---|
| **Index** | `Examples_Section_5_<n>_<Family>.md` — one table row per archetype | The matched family only |
| **Detail** | `Matrix_Rows/<ID>.md` — the full prescription for one archetype | The matched ID(s) only |

The full format spec for both layers, and the row-file template, are in **`Matrix_Rows/README.md`**. Do not duplicate that guidance into the index files — the indexes carry a two-line preamble pointing here and then the table.

### 5.0 Family-pointer table

> **Setup guidance:** Name the role families the candidate actually targets. Five to eight is typical. Add a cross-family hybrid family for briefs that blend two families in equal weight — it earns its place faster than expected, because senior briefs blend more often than they don't.

| Family | Covers | Index file |
|---|---|---|
| 5.1 [Role family 1] | [One line on the seats this family covers] | `Examples_Section_5_1_[Name].md` |
| 5.2 [Role family 2] | [One line] | `Examples_Section_5_2_[Name].md` |
| 5.3 [Role family 3] | [One line] | `Examples_Section_5_3_[Name].md` |
| 5.4 [Role family 4] | [One line] | `Examples_Section_5_4_[Name].md` |
| 5.5 [Role family 5] | [One line] | `Examples_Section_5_5_[Name].md` |
| 5.8 Cross-family hybrids | Briefs blending two families in equal weight — **checked FIRST when that is the case**, before either family's own default | `Examples_Section_5_8_Hybrids.md` |

### 5.1 Index file format

Each index file opens with a short preamble pointing at `Matrix_Rows/README.md`, then one table:

```markdown
| ID | Pattern (distilled) | Tested with | Body stacks | Detail file |
|---|---|---|---|---|
| 5.3-EXAMPLE | Twenty-five words at most — sector, seat, mandate, and the one screen that decides it. | [Organisation], [Role] [YYYY-MM-DD] | B2-1, B4-3, B1-2 | `Matrix_Rows/5.3-EXAMPLE.md` |
| 5.3-DEFAULT | The family fallback when no archetype matches cleanly. | [Organisations] | B2-1, B1-2, B5-1 | `Matrix_Rows/5.3-DEFAULT.md` |
```

Target: **10 KB or less per index.** An index growing past that means the `Pattern (distilled)` column has stopped being distilled — tighten the entries rather than splitting the file. Every family carries a `-DEFAULT` row.

### 5.2 Second-occurrence row policy

This replaces the earlier row-per-application rule, which produced a row for every brief and buried the archetypes that actually recur under the ones that never did.

1. **First occurrence of an unmatched pattern.** In the same session, create two things:
   - a **slim prescription row in the family index** — **1,500 characters maximum**: pattern, positioning lead, body stack, template and length, fit-acknowledgment, AI register;
   - a `Matrix_Rows/<ID>.md` file marked `Status: one-shot`.
2. **Second occurrence** — a **second distinct organisation** matching the same archetype, not a repost or a v2 of the same role — promote the row to full detail: expand the pattern, record both engagements under `Tested with`, and write the tie-breaks properly now that there is something to compare against.
3. **No parking.** Every occurrence stays greppable: index row, row file, changelog line, commit message. A pattern recorded only in the changelog does not exist as far as retrieval is concerned, and will be rediscovered from scratch next time.

The judgement this encodes: one application is an anecdote; two are a pattern worth the cost of a full row.

### 5.3 Maintenance

When a draft improves on its row's prescription, fold the improvement **back into the row file** in the same session, with a changelog line and a commit — and keep the index row in sync. That loop is the entire point of the matrix layer. A traceability finding of "undocumented drift" that turns out to be an improvement, and is then left unrecorded, is a silent loss of calibration.

---

## 6. Signature metrics quick reference

Hardest-hitting quantifiable outcomes for drop-in use. Always preserve the source-entry framing; do not isolate a metric from its context.

> **Setup guidance:** Populated as section files are written. Every B-section entry that contains a strong number should contribute its top one or two metrics here. Group the metrics by category (Investment and finance / Scale and reach / Delivery and performance / Cyber, risk and compliance / Customer, commercial and people, or whatever categories fit the candidate's career). Each row: metric, context, source entry IDs.

### [Metric category 1 — e.g. Investment and finance]

| Metric | Context | Source entry |
|---|---|---|
| **[Metric with units]** | [Context — what it's a metric of] | [Entry ID(s)] |

### [Metric category 2 — e.g. Scale and reach]

| Metric | Context | Source entry |
|---|---|---|

### [Metric category 3 — e.g. Delivery and performance]

| Metric | Context | Source entry |
|---|---|---|

### [Metric category 4 — e.g. People, culture, customer]

| Metric | Context | Source entry |
|---|---|---|

---

## 7. Known gaps and watch-outs register

Consolidated honesty boundaries. Claude must check this register before finalising any draft and must not assert anything that breaches a watch-out unless new evidence explicitly supports it.

> **Setup guidance:** Capture every honesty boundary the candidate names during setup, and every additional one that surfaces during application drafting. This is the single highest-leverage maintenance section — every captured watch-out prevents a future overclaim. Three categories help organise the register.

### 7.1 Experience limits — do not overclaim

| Area | Watch-out |
|---|---|
| **[Specific area where overclaim risk exists]** | [Specific boundary — what to avoid asserting; what to assert instead.] |
| **[Area]** | [Boundary.] |
| **[Area]** | [Boundary.] |

### 7.2 Framing discipline — lead with substance, not labels

> **Setup guidance:** Capture the candidate's preferred substantive framings. These are reminders to Claude about what to lead with for this candidate's career. Examples might include: "Lead with outcomes, not tooling"; "Lead with stakeholder engagement and risk-managed delivery, not architecture"; "Lead with practical enablement on AI; keep guardrails as supporting logic".

- Lead with [substance], not [label].
- Lead with [substance], not [label].
- Lead with [substance], not [label].
- Lead with [substance], not [label].
- Lead with [substance], not [label].

### 7.3 Evidence-recency flags

> **Setup guidance:** Capture any time-sensitive proof points that need revalidation before reuse. Examples: "Confirm latest [annual cycle outcome] before asserting [strongest claim about it]"; "Refresh [specific metric] annually before quoting"; "[Specific employer] metrics may have eroded comparability — revalidate before reuse".

- [Recency flag — what needs to be revalidated, when, and why.]
- [Recency flag.]
- [Recency flag.]

---
