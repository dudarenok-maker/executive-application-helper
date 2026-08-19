# `Matrix_Rows/` — per-row detail files

One file per matrix row: `Matrix_Rows/<ID>.md`. This folder is the second half of the
**index → row** retrieval split introduced at the V6 restructure of this framework.

## Why the split exists

In the previous architecture each role-family matrix was a single fat file. Matching one row meant
loading every row in the family — hundreds of kilobytes of prescriptions for archetypes irrelevant
to the brief in hand. The split keeps the **whole** family scannable at a glance while loading only
the matched row in full:

| Layer | File | Loaded |
|---|---|---|
| Index | `Examples_Section_5_*.md` | Always, for the matched family — one table row per archetype |
| Detail | `Matrix_Rows/<ID>.md` | Only for the ID(s) the index matched |

A family index should stay around 10 KB. If one grows past that, the `Pattern (distilled)` column
has stopped being distilled — tighten it, don't split the file.

## Index row format

Each family index carries one table row per archetype, and nothing else:

```markdown
| ID | Pattern (distilled) | Tested with | Body stacks | Detail file |
|---|---|---|---|---|
| 5.3-EXAMPLE | Twenty-five words at most: the recurring shape of the brief — sector, seat, mandate, the one screen that decides it. | [Organisation], [Role] [YYYY-MM-DD] | B2-1, B4-3, B1-2 | `Matrix_Rows/5.3-EXAMPLE.md` |
```

**ID convention:** `<family>.<n>-<SHORT-SLUG>` — family and section number, then an uppercase slug
naming the archetype (usually the organisation the row was first tested with, or the pattern where
the organisation is confidential). Each family also carries a `<family>-DEFAULT` row: the fallback
when no archetype matches cleanly.

## Row file format

Every row file carries a header line and the same nine sections, in this order. Use
`_ROW_TEMPLATE.md` in this folder as the starting point — copy it, don't retype it.

| Section | Contents |
|---|---|
| `## Pattern` | The archetype in full — what the brief looks like, what the panel is really testing, where the screen sits. |
| `## Tested with` | Every organisation and date this row has been used against. **The promotion trigger lives here** (see below). |
| `## Positioning` | A-IDs, with the dominant one flagged. The dominant A-ID's framing must be recognisable in the opening third of any draft built on this row. |
| `## Body stacks` | B-IDs grouped by paragraph, each with a one-line note on what it is carrying. |
| `## Template / Length` | The C-template ID and the length band, with any row-specific override and its reason. |
| `## Fit-acknowledgment` | How gaps are handled for this archetype — name-the-gap, transferability-without-naming, confident-close, etc. — and the conditions under which the default should be reconsidered. |
| `## AI register` | Which AI framing applies (hands-on builder / governance-led / not loaded) and why. Register mismatch is a traceability finding, not a watch-out. |
| `## Companion files` | Which A / B / C / D files to load. The retrieval protocol loads these and nothing else. |
| `## Notes / Distinct from` | Tie-breaks against adjacent rows, and any `Section 7.x` watch-out the archetype triggers. |

Header line:

```markdown
# <ID> — Section <n.n> <Family name> matrix row

**Created:** YYYY-MM-DD | **Status:** one-shot | full
```

## Second-occurrence row policy

This replaces the old row-per-application rule, which produced a row for every brief and buried the
patterns that actually recur.

1. **First occurrence of an unmatched pattern.** Same session, create two things: a **slim
   prescription row in the family index** (pattern, positioning lead, body stack, template/length,
   fit-ack, AI register — **1,500 characters maximum**), and a `Matrix_Rows/<ID>.md` file marked
   `Status: one-shot`.
2. **Second occurrence** — meaning a **second distinct organisation** matching the same archetype,
   not a repost or a v2 of the same role — promote the row to full detail: expand the pattern,
   record both engagements under `Tested with`, and write the `Notes / Distinct from` tie-breaks
   properly now that there is something to compare against.
3. **No parking.** Every occurrence remains greppable — index row, row file, changelog line, commit
   message. A pattern that lives only in the changelog does not exist as far as retrieval is
   concerned, and will be rediscovered from scratch next time.

The judgement the policy encodes: one application is an anecdote. Two are a pattern worth the cost
of a full row.

## Maintenance

When a draft improves on its row's prescription, the improvement is folded **back into the row
file** in the same session — with a changelog line and a commit. That loop is the whole point of
the matrix layer. A gate finding of "undocumented drift" that turns out to be an improvement and is
then left unrecorded is a silent loss of calibration.

Keep the index row and the detail file in sync. They are two views of one prescription; when they
disagree, the detail file wins and the index is corrected.
