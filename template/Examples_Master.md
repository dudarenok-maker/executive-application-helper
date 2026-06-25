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

This evidence bank supports **two workflows** that draw on the same entries: **application drafting** (cover letters, statements of claims, targeted pitches, etc.) and **interview preparation** (STAR-style prep documents for recruiter screens, behavioural panels and executive panels). The retrieval protocol below applies to both. The workflow-specific style baselines and output structures live in separate files: `Writing_Voice_and_Style_Guide.md` (written) and `Interview_Voice_and_Style_Guide.md` + `Interview_Prep_Template.md` (spoken).

**Before drafting any application OR preparing any interview, Claude follows this sequence:**

1. **Always load this file (`Examples_Master.md`)** as the retrieval entry point. It contains the full master index, role-family recipes, signature metrics, watch-outs and formatting rules — everything needed to select entries.
2. **Read the role materials** (advertisement, position description, candidate information pack, recruiter instructions, any attachments).
3. **Identify the role family** from the list in Section 3 (controlled tag vocabulary).
4. **Open Section 5 (Role-family recipes)** and note the suggested starter set of entry IDs for that role family.
5. **Open Section 4 (Master index)** and filter by relevant capability, sector and tier to extend the starter set with role-specific proof points.
6. **Cross-check Section 7 (Known gaps and watch-outs register)** to confirm no watch-out has been breached by the selected framing.
7. **Load only the companion files containing the selected entries.** Use the **file map in Section 1** below to identify which section files to open. Do not load all section files by default — load only those needed for the specific role.
8. **For interview prep, also load** `Interview_Voice_and_Style_Guide.md` (style baseline for spoken delivery) and `Interview_Prep_Template.md` (canonical prep-document structure).
9. **Report the proposed evidence set to [Candidate First Name]** for confirmation before drafting or finalising prep.
10. **Draft (or prep) using the selected entries**, drawing signature metrics from Section 6 where useful.

After the application is drafted or the prep document is finalised, Claude runs the **post-draft / post-prep maintenance step** (see the `Examples_Section_D_E_Personal_Maintenance.md` file and the project instructions). Both workflows feed back into the same evidence-bank changelog.

---

## 1. How this document is structured

The evidence bank is split into a Master file (this document) and companion section files. The Master file contains the operating layer (retrieval protocol, formatting rules, controlled vocabulary, master index, role-family recipes, signature metrics, watch-outs). The entry bodies sit in the companion section files and are loaded on demand.

### 1.1 File map

> **Setup guidance:** If the candidate adjusts the capability domains during setup (renaming B1, adding B7, removing B3, etc.), update this table to match. The "Load when" column is the trigger for Claude to open that companion file.

| File | Section | Contents | Load when |
|---|---|---|---|
| `Examples_Master.md` (this file) | 0–7 | Retrieval protocol, formatting rules, tag vocabulary, master index, role-family recipes, signature metrics, watch-outs | **Always** |
| `Examples_Section_A_Positioning.md` | A | Core positioning blocks (A1, A2, …) — identity, motivation, leadership approach, onboarding | Almost always — positioning blocks are usually relevant to every draft |
| `Examples_Section_B1.md` | B1 | [Default: Strategy, governance and investment — rename per setup] | When role involves [trigger conditions] |
| `Examples_Section_B2.md` | B2 | [Default: Delivery, operations and modernisation — rename per setup] | When role involves [trigger conditions] |
| `Examples_Section_B3.md` | B3 | [Default: Procurement, shared services and vendor management — rename per setup] | When role involves [trigger conditions] |
| `Examples_Section_B4.md` | B4 | [Default: Risk, cyber, information governance and AI — rename per setup] | When role involves [trigger conditions] |
| `Examples_Section_B5.md` | B5 | [Default: People, culture and organisation capability — rename per setup] | When role involves [trigger conditions] |
| `Examples_Section_B6.md` | B6 | [Default: Commercial, customer and growth — rename per setup] | When role involves [trigger conditions] |
| `Examples_Section_C_Templates.md` | C | Ready-made templates (C1 to C6 or as configured) — SoC, behavioural response, cover letter, pitches, screening answer | When drafting — once the document format is known, load only the template file needed |
| `Examples_Section_D_E_Personal_Maintenance.md` | D, E | Optional personal content (D1) + maintenance notes (E1–E3) | D: only when a recruiter explicitly asks for personal background. E: when maintaining the evidence bank at end of session |

### 1.2 Sections in this Master file

| Section | Purpose |
|---|---|
| **0** | Quick-start retrieval protocol (Claude's working recipe). |
| **1** | Structure overview + file map. |
| **2** | Entry formatting rules (applied inside the companion section files). |
| **3** | Controlled tag vocabulary (four dimensions). |
| **4** | Master index — one-row-per-entry scannable table. |
| **5** | Role-family recipes — recommended starter sets by role family. |
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

The master index in Section 4 uses short codes to keep the scannable rows compact. These codes are used **only in Section 4**. Everywhere else — Section 3.1–3.4 above, Section 5 role-family recipes, and the companion-file entry metadata blocks — the canonical full labels remain in force.

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

## 5. Role-family recipes

Each recipe is a **starter set** to be supplemented from the Master Index based on specific role requirements. All recipes should include the leadership-approach positioning block by default — drop only if not needed.

For each recipe, the **companion files you will typically need** are listed so Claude knows which files to load.

> **Setup guidance:** During setup, populate one recipe in detail — for the candidate's primary target role family. Add stub recipes for the others (just the role-family heading and a placeholder note "to be populated when first applied for"). Recipes deepen with use: every application adds learnings.

### 5.1 [Role family 1]

**Core pattern:** [The recurring frame for this role family — what panels typically look for. One sentence.]

**Starter set:**
- **Positioning:** [List of A-block IDs that should anchor every draft for this role family]
- **Evidence:** [List of B-section IDs that are the workhorses for this role family]
- **Template:** [Default C template ID for this role family]

**Companion files to load:** Section A, [list the B-section files], C.

**Optional add-ons by criterion:**
- If [criterion] → add [entry ID]
- If [criterion] → add [entry ID]
- If [criterion] → add [entry ID]

### 5.2 [Role family 2]

[Stub. Populate when the candidate applies for a role in this family for the first time.]

### 5.3 [Role family 3]

[Stub.]

### 5.4 [Role family 4]

[Stub.]

### 5.5 [Role family 5]

[Stub.]

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
