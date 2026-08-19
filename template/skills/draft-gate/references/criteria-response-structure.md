# Selection Criteria Response — canonical structure

> **How to use this file.** This is both the **drafting** spec and the **gate** spec. Read it
> *before* generating a Selection Criteria Response, not only when verifying one — `draft-gate`
> Check 4 verifies exactly what this file prescribes, so a document generated against it passes the
> gate by construction. Load it alongside `Examples_Section_C_Templates.md` (templates C1–C6), the
> matched `Matrix_Rows/<ID>.md`, and `candidate-voice` `references/style-guide.md` for the prose.
>
> **Setup note:** this is a template skeleton. Replace `[Candidate Name]`, `[Candidate First Name]`
> and `[Workspace Folder Path]`. When you produce your first criteria response, name it here as
> your reference implementation — a worked example of your own beats any generic one.

---

## The governing idea

**A Selection Criteria Response is not a document about the candidate. It is a copy of the panel's
scoring instrument with the evidence filled in.**

Every structural rule here follows from that. A panel member works down their own criteria list,
looking for each criterion in turn, scoring what they find. Anything they cannot find scores zero —
not "partially met", zero — and no other paragraph can recover it. The document's job is to make
each criterion trivially findable and each answer independently scorable.

That is the opposite of the cover letter's job, which is to be read once, in order, as an argument.
Hence the division of labour in Rule 10.

---

## Rule 1 — Header that self-identifies

Three lines, before anything else:

```markdown
**Selection Criteria Response — [Role Title], [Organisation]**

**Applicant: [Candidate Name]**

---
```

The response is routinely detached from the pack, printed, and circulated to panel members who never
see the covering email. It must say what it is, what role it answers, and who wrote it.

## Rule 2 — Every criterion gets a heading. Every one.

Count the criteria in the advertisement, the position description, the candidate pack and the portal
form. Where those sources disagree, resolve in the **advertisement's** favour and flag the
discrepancy to [Candidate First Name]. Then produce **one heading per criterion, no exceptions**:

- Never drop a criterion because the evidence is thin — a thin answer scores something, a missing
  answer scores zero.
- Never merge two criteria under one heading, however similar. The panel has two boxes.
- Never split one criterion into two headings; the compound stays whole (Rule 5).

This is the single highest-value rule in the file, and the reason Check 4.2 blocks.

## Rule 3 — Headings are the criterion, verbatim, in bold

Quote the criterion word for word as its own bold heading. Do not paraphrase it into the candidate's
language, do not shorten it, do not "improve" its grammar, do not turn it into a claim.

```markdown
**Bachelor's degree in [named discipline], [named discipline], or related discipline**
```

Not `**Qualifications**`. Not `**Relevant tertiary background**`. Not
`**My education meets the intent of this criterion**`.

A panel member scanning for their own words must hit them. A paraphrased heading is functionally a
missing criterion, which is why Check 4.3 blocks alongside 4.2.

Bold-as-heading (rather than `###`) keeps the criterion visually subordinate to the advertisement's
category headings while still standing out from body prose.

## Rule 4 — Group under the advertisement's own category headings

Use the ad's categories, in the ad's order, with the ad's Essential/Desirable labels:

```markdown
## [Ad's first category heading] — Essential
## [Ad's second category heading] — Essential
## Desirable criteria — brief note
```

Not a structure of the candidate's invention (`## Leadership`, `## Technical depth`,
`## Why [Organisation]`). The document mirrors the scoring instrument; the panel should be able to
lay their form beside it and read straight down. Where the ad has no categories, one flat list in the
ad's order.

## Rule 5 — One evidence-dense paragraph per criterion

**One paragraph. No bullets, no sub-headings, no lists.**

Bullets look like coverage and read like a résumé fragment; in a criteria response they are padding
that dilutes the evidence. The paragraph carries **two or three named organisation anchors with hard
numbers**, drawn from the matched matrix row's body stack — not freshly improvised evidence selection
(Check 3.1 will catch that anyway).

Within the paragraph: **open direct** (Rule 6), **answer every limb** of a compound criterion, and
**close with a bridge** (Rule 7).

**Compound criteria.** Where a criterion bundles requirements into one sentence — *"Strong knowledge
of X, Y and Z; A, B and C principles; and D, E and F ecosystems"* is three limbs in one heading — the
heading stays whole and verbatim, and the paragraph must touch **every limb**. List the limbs while
drafting and tick each one off. A dropped limb is a partial score on a criterion that *looked*
answered.

## Rule 6 — Open by answering, not by warming up

The first sentence answers the criterion. No restatement of the criterion, no "I have extensive
experience in…", no scene-setting.

> **Criterion:** *Significant experience leading [capability] delivery in a complex organisation*
> **Opens:** "At [Organisation], I led an enterprise technology reform program that secured
> [$ amount] in funding over [N] years…"

The panel may read only the first line of each paragraph on the first pass. Make it the answer.

## Rule 7 — Close with the bridge

The last sentence of each paragraph ties the evidence back to the criterion, or to this role — the
so-what. It does not trail off at the end of the final proof point.

> "…giving me direct experience translating [capability] strategy into funded, delivered outcomes
> rather than pilots that stall."
> "…The governance frameworks I have built have consistently had to be externally defensible, not
> policy on paper."
> "…maps closely to the coordination this position plays across [Organisation]'s business units and
> functions."

## Rule 8 — Hard-gate criteria are answered head-on

A **hard-gate criterion** is one stating a degree, certification, licence, sector tenure or similar
threshold the candidate does not hold literally. It is usually first in the Essential list, and it is
usually where an application quietly dies.

**The sequence, in this order, inside the criterion's own paragraph:**

1. **Lead with what they actually hold** — named specifically and in full. Degrees with titles and
   institution, and the professional qualifications alongside them. Not a gesture at "a strong
   academic background".
2. **Name the gap plainly, in their own words**, and say that you are naming it. For example: *"My
   formal education is in a quantitative, analytical discipline rather than a named [discipline]
   degree, and I want to be direct about that rather than construct an equivalence that isn't
   there."*
3. **Argue substantive equivalence against the criterion's own wording** — quote the criterion's own
   escape hatch where it has one ("or related discipline", "or equivalent experience") and make the
   argument in its terms, with the years and the applied evidence that carry it.
4. **Close on the honest limit**: *"I believe that combination meets the intent of 'or related
   discipline' in substance, even where the degree title does not."*

**Never:** skip the criterion; bury the answer mid-paragraph; pad around it; claim an equivalence the
qualification does not support; or write a heading that pretends the criterion says something softer
than it does. **Evasion on a stated essential is worse than the gap** — a panel that reads a dodge
stops trusting every other claim in the document. That is why Check 4.9 blocks.

**Interaction with the matrix row's fit-acknowledgment discipline.** The row's `Fit-acknowledgment`
section prescribes gap handling for the *package*. Where the package includes a criteria response and
the gap sits inside a stated essential criterion, the criteria response is where the gap gets its
full dedicated treatment — record it in the row as `dedicated-post-evidence for the <name>
criterion` — and the cover letter carries at most a light single-sentence version. **The watch-outs
register's single-mention discipline still applies across the package:** naming the same gap at full
weight in both documents is drift, not thoroughness. Record the split in the matrix row so the next
application in the pattern reproduces it.

Where the gap is a *desirable*, not an essential, it belongs in the consolidated desirable note
(Rule 9) at one sentence, not in a dedicated treatment.

## Rule 9 — Desirable criteria: one consolidated note

Desirables get a **single brief closing note** — one paragraph, roughly 80–130 words — sweeping all
of them, not a heading and paragraph each. Effort proportionate to an instrument that weights them
lightly, and a signal that the candidate can read a scoring rubric.

Structure: the desirables that are held, in a single semicolon-separated run; then any honest gap
named plainly in the same breath, with the closest analogue.

> "I bring [held desirable]; [held desirable] through [organisation]; hands-on experience with
> [named tools]. I have not held a role within [the sector the ad names], and I want to state this
> directly rather than imply otherwise; my closest analogue is leading transformation within other
> [comparable institutions] with comparable governance complexity."

Exception: where the ad states that desirables are separately scored, or asks for them addressed
individually, follow the ad — the instrument always wins over this default.

## Rule 10 — Division of labour with the companion cover letter

The two documents are one package with two jobs. Neither repeats the other.

| | **Selection Criteria Response** | **Companion cover letter** |
|:--|:--|:--|
| Job | Systematic, criterion-by-criterion evidence | Narrative, motivation, argument |
| Read | Scanned, non-linearly, against a form | Read once, in order |
| Structure | The ad's instrument | The matched row's body stack (C1–C6) |
| Opening | Answers criterion 1 | Hook — rhetorical question, tension, scene |
| Carries | Every criterion, in the ad's words; the full hard-gate treatment | Why this organisation, why now, the through-line, the 30/60/90, salary expectation where the ad demands it, the light fit-acknowledgment |
| Voice | Direct, dense, plain; still the candidate's voice, lower on rhetoric | Full `candidate-voice` register — bolded lead-ins, rhythm, wit |
| Bolded lead-ins | No — the bold is the criterion heading | Yes, per the style guide |

**Shared proof points, different framings.** The same evidence appears in both — it is the same
career — but never as reused sentences. The letter tells a governance build as a story about
governance enabling speed; the criteria response states the same work as evidence against
*"establishing governance frameworks, risk controls, and assurance processes"*. If a sentence could
be cut from one and pasted into the other, one of them is doing the wrong job.

**The hand-off line.** The letter carries **one** explicit pointer to the criteria response, placed
where the letter would otherwise be tempted to duplicate it:

> "I address the grounding more fully against the stated selection criteria in the accompanying
> document."

That single line is what licenses the letter to stay narrative — it tells the reader the systematic
answer exists and where to find it.

---

## Length and production

- **Band:** 2 pages default; 1 page where there is a single criterion. Per-criterion stated limits
  always win; absent one, the channel default is 250–400 words per criterion
  (`references/length-bands.md`), and `draft-gate` Check 1 counts each criterion independently.
  **A page limit beats the per-criterion default.** Eight or nine essential criteria plus a
  desirables note will not fit two pages at 250 words apiece — a nine-criterion response that fits
  two pages lands nearer 85–150 words each. Compress the answers; never pad one to reach a word
  band, and say in the gate report which limit governed.
- **Source of truth:** a Markdown source file, saved to `[Workspace Folder Path]/Submissions/` as
  `[Candidate Name] - [Title] - [Company] - Selection Criteria Response Source.md`.
- **Two-stage delivery, as for letters:** Stage 1 `.docx` for the candidate's review, Stage 2 final
  branded PDF to `Submissions/` as
  `[Candidate Name] - [Title] - [Company] - Selection Criteria Response.pdf`.
- Build artefacts and sources live in `Submissions/`, never in `Pipeline/`.

## Pre-flight checklist for drafting

1. Extract the criteria list verbatim from the ad / position description / pack / portal; reconcile
   disagreements in the advertisement's favour; count them.
2. Note the ad's category headings and the Essential/Desirable split.
3. Flag any hard-gate criterion to [Candidate First Name] **before** drafting — it changes the shape
   of the whole package.
4. Map each criterion to B-IDs from the matched row's body stack; note criteria with no strong anchor
   and say so in the pre-drafting assessment.
5. List the limbs of every compound criterion.
6. Draft, then run `draft-gate` — Check 4 verifies rules 1–10 directly.
