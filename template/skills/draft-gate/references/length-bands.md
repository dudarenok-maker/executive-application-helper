# Length bands — by channel

Bands are keyed by **channel** and overlay document types. The matched matrix row's `Template / Length` section overrides the channel band; a brief-stated limit overrides everything.

| Channel / format | Band | Blocking? |
|:--|:--|:--|
| **Short form** — private-sector, recruiter-mediated and job-board-lodged letters (**the default channel**) | **350–550 words** | Advisory |
| **Long form** — public-sector and criteria-based briefs | **900–1,250 words** | Advisory |
| Statement of Claims | 1,000–1,250 words | Advisory |
| Targeted Pitch (C4) | 600–1,000 words | Advisory |
| **Platform screening questions** | **The platform's hard per-question character limit — silent truncation** (Seek: 1,000) | **Always blocking** |
| Selection Criteria Response | Per stated limit per criterion; 2 pages default, 1 page for a single criterion; 250–400 words per criterion if unspecified | Stated limits blocking; defaults advisory |
| Short recruiter response (C5/C6) | Strictly per the stated limit — no default | Stated limit blocking |

## Why channel and not document type

The old bands were keyed by document type alone, which produced 900–1,250-word cover letters for private-sector roles where the reader — usually an internal recruiter with forty applications open — reads the first paragraph and skims the rest. The same letter length that reads as thorough against a public-sector selection-criteria brief reads as unedited against a job-board ad. Channel is the better predictor of what the reader will actually do with the document.

## Override hierarchy (highest wins)

1. **The brief's stated limit** — verbatim from the ad, position description, pack or recruiter email.
2. **The matched row's band** — `Matrix_Rows/<ID>.md`, `Template / Length` section. Rows carry tested overrides, and a tested override beats a general rule.
3. **The channel band** above.

Always name which of the three produced the band you applied. If none is available and the format is unusual, ask — one batched question — rather than guessing.

## Counting rules

- **Letters, statements of claims, pitches:** body text only. Exclude the header, greeting, sign-off and signature block. Include section headings.
- **Screening answers:** each answer counted independently. Strip markdown before counting, and separately flag any markdown found — these fields render plain text and will display literal asterisks. Smart quotes, en-dashes and em-dashes are one character each.
- **Selection criteria:** each criterion counted independently. Page limits convert at roughly 850–1,000 words per page; state the conversion as a caveat.
  **A stated page limit beats the per-criterion default.** Eight or nine essential criteria plus a desirables note will not fit two pages at 250 words apiece — a nine-criterion response that fits two pages lands nearer 85–150 words each. Compress the answers; never pad one to reach a word band, and name in the report which limit governed. Structure rules: `criteria-response-structure.md`.

## Tolerance

Bands are inclusive and approximate. A five-to-ten-word overshoot on a 550-word band is not worth interrupting delivery for — say so and move on. A platform character limit has no tolerance at all: it truncates mid-word, silently, and the reader sees the truncation, not the reason for it.
