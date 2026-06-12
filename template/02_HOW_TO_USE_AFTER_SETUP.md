# How to use the framework after setup

Once `01_SETUP_ORCHESTRATOR.md` has populated all canonical files and they have been moved to your working directory, this is your operating reference.

---

## Daily / per-application usage

### To draft an application

1. **Open a fresh Cowork session** (or your equivalent Claude project session).
2. **Provide role materials.** At minimum: the position description, advertisement, candidate information pack, or recruiter brief. A role title and organisation alone are not enough — Claude is instructed to refuse drafting without role-specific materials. Paste the text or attach files.
3. **Tell Claude what document type you need:** Cover Letter, Statement of Claims, Targeted Pitch, Selection Criteria Response, or short/long Recruiter Response.
4. **Specify any constraints:** word/character limits, page limits, format requirements, specific sections the panel cares about.
5. **Let Claude run.** It will: gate on materials, run pre-drafting assessment, draft, run coverage analysis, suggest resume tailoring, and update the evidence bank.

### To draft a generic cover letter (no role)

Tell Claude explicitly: *"Draft a generic cover letter for the [category name] application category."* — referencing one of the categories defined in `Writing_Voice_and_Style_Guide.md`. This is the only path that bypasses the role-materials gate.

### Output you'll get back

In this order:

1. **Pre-drafting assessment** — which evidence-bank entries Claude selected, which companion files it loaded, any stale or flagged entries.
2. **Drafted document** — saved as `.docx` in `…/Submissions/` using your Word template.
3. **Coverage analysis** — section-by-section table mapping the draft against the role materials (Addressed / Partially Addressed / Not Addressed).
4. **Resume tailoring recommendations** — side-by-side suggestions, not a full rewrite.
5. **Evidence-bank maintenance report** — what was updated in the bank, what was added to the changelog.

---

## Maintenance disciplines that keep quality high

### After every application

The framework runs Step 4 (post-draft maintenance) automatically, but check the maintenance report. If Claude flagged something it couldn't action — e.g. "this metric is older than 24 months and may need refreshing" — that's your signal to update the underlying entry.

### Periodically (every six months or after a significant role change)

- **Refresh metrics** in `Examples_Master.md` Section 6 (signature metrics quick reference). Numbers age. Replace anything older than 24 months with stronger or more current evidence.
- **Re-tier entries.** A Primary entry from three years ago may now be Secondary; a strong recent example may deserve to be promoted.
- **Update watch-outs** in `Examples_Master.md` Section 7. As your career moves, what you can credibly claim changes.
- **Refresh `Resume.md`** with new role detail and recent achievements.
- **Audit Section A positioning blocks.** These are the most reused content — small refinements compound.

### Whenever you make a structural change

If you change the operating logic in `Project_Instructions.md` — adding a new role family, changing the gating rules, restructuring the evidence bank — append an entry to `Project_Instructions_Changelog.md` in the same session. If you change the evidence bank — adding, retiring or amending an entry — append an entry to `Evidence_Bank_Changelog.md` in the same session. If you change the structure of the framework itself in a way you might want to share with others, also update `_Template/Template_Changelog.md`.

---

## Common operating patterns

### Adding a new role family

1. Add the role family to `Examples_Master.md` Section 3.1 (controlled vocabulary).
2. Add a matching short code to Section 3.5.
3. Add a recipe to Section 5 — at minimum: core pattern, starter set of entry IDs, default template, companion files to load, optional add-ons.
4. Re-tag any existing entries that should now also reference this role family.
5. Append a `Project_Instructions_Changelog.md` entry.

### Adding a new capability domain (B7, B8, etc.)

1. Create a new companion file `Examples_Section_B[n]_[Name].md`.
2. Add it to `Examples_Master.md` Section 1.1 (file map).
3. Add a row in `Project_Instructions.md` canonical-files table.
4. Add capability tags in Section 3.2 and short codes in Section 3.5.
5. Update role-family recipes that should reference the new domain.
6. Append a `Project_Instructions_Changelog.md` entry. Append an `Evidence_Bank_Changelog.md` entry for any new entries created.

### Discovering a watch-out during drafting

When Claude flags or you realise during a draft that you're at risk of overclaiming, add the watch-out to `Examples_Master.md` Section 7 the same session. This is the single highest-leverage maintenance action — every captured watch-out prevents a future overclaim.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Claude refuses to draft, asks for role materials | Mandatory gating step not satisfied | Provide a position description, advertisement, candidate information pack or recruiter brief. Or explicitly request a generic cover letter for a named category. |
| Drafts feel generic, not "you" | Style guide thin or sample base too narrow | Add more writing samples to the Phase 2 setup; reread `Writing_Voice_and_Style_Guide.md` and tighten the principles that aren't landing. |
| Drafts repeat the same examples across roles | Evidence bank too shallow on the relevant domain | Add more entries to the relevant B-section; ensure tags accurately reflect role-family fit. |
| Coverage analysis flags "Partially Addressed" repeatedly | Selection criteria are not well evidenced | Use the gap as a signal to capture new evidence after the draft (Step 4 maintenance). |
| Claude cites IDs in the visible draft | Output instruction not enforced | Remind Claude: IDs are internal-only; reader-facing copy should not show them. |
| Resume tailoring suggestions are too aggressive | Claude has rewritten rather than tailored | Reset and re-prompt: "tailor only — do not rewrite the resume". |

---

## When to come back to the orchestrator

You don't need to re-run the orchestrator for normal use. Only re-run it if:

- Your career changes materially (new sector, new role family, significant scope expansion).
- You want to refresh your style guide from a new sample base.
- You're sharing the framework with someone else and want a clean setup for them.

For incremental tuning, edit the canonical files directly and record changes in the appropriate changelog.
