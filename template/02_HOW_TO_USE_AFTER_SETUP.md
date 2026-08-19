# How to use the framework after setup

Once `01_SETUP_ORCHESTRATOR.md` has populated the canonical files and they have been moved to your working directory, this is your operating reference.

---

## Daily / per-application usage

### To draft an application

1. **Open a fresh session** in your Claude project.
2. **Provide role materials.** At minimum: the position description, advertisement, candidate information pack, or recruiter brief. A role title and organisation alone are not enough — Claude is instructed to refuse without role-specific materials. Paste the text, attach files, or drop a URL.
3. **Optionally name the document type** — `SoC`, `pitch`, `criteria`, `recruiter reply`. With nothing named, you get a Cover Letter.
4. **Specify any constraints:** word, character or page limits, format requirements, sections the panel cares about.
5. **Let Claude run.** It gates on materials, checks for a duplicate submission, runs the pre-drafting assessment, drafts, audits the voice, runs the draft gate, hands you a review copy, folds your edits in, produces the final PDF, analyses coverage, suggests resume tailoring, maintains the bank, and commits.

### To draft a generic cover letter (no role)

Say explicitly: *"Draft a generic cover letter for the [category name] application category"* — one of the categories in your writing style guide. This is the only path that bypasses the role-materials gate.

### What you get back, in order

1. **Pre-drafting assessment** — the duplicate-check outcome, the matched matrix row and its body stack, the entries and companion files selected, any stale or flagged entries, and every default applied.
2. **The draft**, plus the **voice-audit summary** and the **draft-gate report** with its full verification checklist.
3. **A review `.docx`** — the editable copy. Mark it up.
4. **The final PDF** in `Submissions/`, built after your edits are folded back into the source.
5. **Coverage analysis** — section by section against the role materials (Addressed / Partially / Not).
6. **Resume tailoring recommendations** — targeted at `Resume_Master.md`, one mini-table each.
7. **Maintenance report** — what was updated where, the changelog entry, the bank-gate verdict, and the commit hash.

### Why the review copy comes first

The `.docx` before the PDF is not a formality. You read the letter and you almost always change something — a phrase that isn't how you'd say it, a claim pitched half a degree too high, a paragraph that could lose its first sentence. A PDF invites you to accept what you would otherwise have improved.

Those edits are also the single best input the framework ever receives. When the same correction shows up twice, it stops being a preference and becomes a rule — and it belongs in your style guide, not just in that one letter.

---

## Maintenance disciplines that keep quality high

### After every application

Step 4 runs automatically, but read the maintenance report. If Claude flagged something it could not action — a metric older than 24 months, a capability with thin evidence — that is your signal to fill the gap while the role is still fresh in your mind.

Check that the session ended in a **commit**. A clean `git status` at close is the bank gate's first check, and it is what makes everything else recoverable.

### The matrix layer

New archetypes follow the **second-occurrence policy**: a slim index row plus a `Status: one-shot` row file the first time a pattern appears, promoted to full detail on a second distinct organisation. Two things to watch for:

- **Row files that never get promoted.** If a `one-shot` row has three organisations under `Tested with`, someone skipped the promotion. Promote it — that is where the calibration lives.
- **Improvements that don't get folded back.** When the draft gate reports "undocumented drift" and you decide the drift was an improvement, the row file must be updated in the same session. An improvement you don't record is one you'll rediscover from scratch.

### Periodically (every six months, or after a significant role change)

- **Refresh signature metrics** in `Examples_Master.md` Section 6, and reconcile them against `Resume_Master.md`. A number on the resume that isn't in the bank is an unverified claim.
- **Re-tier entries.** A Primary from three years ago may now be Secondary; a strong recent example may deserve promotion.
- **Update watch-outs.** As a career moves, what can credibly be claimed changes — in both directions.
- **Audit Section A positioning blocks.** These are the most-reused content in the framework; small refinements compound across every future application.
- **Rebuild the resume** and read the PDF. Sources drift from their output more quietly than you would expect.

### Whenever you make a structural change

Append to the appropriate changelog **in the same session** — `Evidence_Bank_Changelog.md` for bank changes, `Project_Instructions_Changelog.md` for operating-logic changes. Entries are **2–4 lines**: what changed and why. The narrative goes in the commit message, which is why the commit message matters more than it used to.

If the change would benefit anyone else using this framework, mirror it into `_Template/` and add a `Template_Changelog.md` entry.

---

## Common operating patterns

### Adding a new role family

1. Add the family to `Examples_Master.md` Section 3.1 (controlled vocabulary) and Section 3.5 (short codes).
2. Add a row to the family-pointer table in Section 5.0.
3. Copy `Examples_Section_5_INDEX_TEMPLATE.md` to `Examples_Section_5_[n]_[Family].md` and write its `-DEFAULT` row.
4. Create `Matrix_Rows/5.[n]-DEFAULT.md` from `_ROW_TEMPLATE.md`.
5. Re-tag any existing entries that should now reference the family.
6. Changelog entry, then commit.

### Adding a new capability domain (B7, B8, …)

1. Create `Examples_Section_B[n]_[Name].md`.
2. Add it to `Examples_Master.md` Section 1.1 (file map), Section 3.2 (capability tags) and Section 3.5 (short codes).
3. Update any matrix rows that should now name it as a companion file.
4. Changelog entries for both the instructions change and any new entries, then commit.

### Discovering a watch-out during drafting

Add it to Section 7 **the same session**, and add its search patterns to `skills/draft-gate/references/sweep-checklist.md` so the sweep can actually find it next time. This is the single highest-leverage maintenance action in the framework: every captured watch-out prevents a future overclaim, and the register is only as good as the discipline of adding to it the moment something is caught.

### Recovering from a bad edit

Git replaced the old snapshot discipline entirely:

```sh
git diff                          # what changed since the last commit
git checkout -- <file>            # discard uncommitted damage to one file
git log --oneline -- <file>       # every state that file has had
git checkout <commit> -- <file>   # restore one file from any past commit
```

There is no separate backup folder to maintain, and no snapshot to remember to take.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Claude refuses to draft, asks for role materials | The gate is not satisfied | Provide a position description, advertisement, pack or recruiter brief — or explicitly request a generic cover letter for a named category. |
| Drafts feel generic, not "you" | Style guide thin, or the voice audit is being skipped | Check that the draft-gate report opens with `Voice audit: run + folded`. If it doesn't, the gate should have blocked. Then deepen the style guide from your own edits. |
| Every letter opens the same way | Opener rotation not enforced | The voice audit compares against the previous letter — make sure prior letters are where they can be found, and that the sanctioned-opener list in the style guide has more than one entry. |
| Drafts repeat the same examples across roles | The evidence bank is shallow in the relevant domain, or the matched row's stack is doing all the work | Add entries to the relevant B-section; check whether the row's body stack needs widening. |
| A screening answer was truncated on submission | Character limit exceeded | This should be impossible — it is an always-blocking gate check. Verify the gate emitted **one checklist row per answer** with an actual character count. A single summary row for several answers is a gate failure. |
| Coverage analysis keeps flagging "Partially Addressed" | Criteria are genuinely not well evidenced | Treat the gap as the session's real output: capture new evidence at Step 4. |
| Claude cites entry IDs in the visible draft | Output rule not enforced | IDs are internal-only. Remind and re-run. |
| Resume suggestions are too aggressive | Rewriting rather than tailoring | Re-prompt: "tailor only — do not rewrite". Full rewrites happen only on request. |
| The gate reports "all pass" with no table | The checklist requirement is being skipped | Reject the gate result and re-run. There is no short-form report — the table *is* the gate. |
| The resume build comes out a page too long | Content growth, not CSS | Tighten the source. `--short` trims mechanically; never trim page-1 content to make a build fit. |

---

## When to come back to the orchestrator

Not for normal use. Only if:

- Your career changes materially (new sector, new role family, significant scope expansion).
- You want to refresh your style guide from a new sample base.
- You are handing the framework to someone else and want a clean setup for them.

For incremental tuning, edit the canonical files directly, log the change, and commit.
