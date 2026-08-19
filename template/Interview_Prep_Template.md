# [Candidate Name] — Interview Prep Template

> **Setup note:** This file is a skeleton. It defines the canonical structure for STAR-style interview preparation documents. The structural guidance is mostly generic and applies to any executive candidate; the only personal content is the candidate's name in the title and the file-naming convention. The Setup Orchestrator (`_Template/01_SETUP_ORCHESTRATOR.md`) handles the basic personalisation.
>
> **How to use this file once populated:** Load alongside `Interview_Voice_and_Style_Guide.md` (for tone and STAR conventions) and the evidence bank (for proof points). Whenever the candidate has an interview to prepare for, follow this structure to assemble the prep document. **Sections 3–6 and §X are verified by `prep-gate` Checks 5 and 6** — a pack built against this file passes those checks by construction, which is the point of reading it before drafting rather than only after.
>
> **Output naming convention:** `[Candidate Name] - [Interview Format] Prep - [Role Title] - [Organisation].md` (e.g. `[Candidate Name] - Recruiter Screen Prep - [Role Title] - [Organisation].md`). Save to `[Workspace Folder Path]/Interview Prep/`. Create the `Interview Prep/` sub-folder on first use if it does not exist.

---

## Canonical structure — all sections in order

```
 1. Front-matter
 2. Executive summary — 1-page brief
 3. Company / organisational context                          [research]
 4. Operating entities and business units                     [research — where the org runs several businesses]
 5. Panel and individual research                             [research — wherever the assessors are named]
 6. Structural-reality analysis                               [research — where the seat carries a structural tension]
 7. Section A — Opening "Tell me about yourself"
 8. Section B — Likely questions and positioning notes
 9. Section C — Pre-prepared STAR responses for highest-risk questions
10. Section D — Practicalities cheat sheet
11. Section E — Questions to ask the panel
12. Sources
```

**Why the research sections sit before the opening script.** Sections 3–6 are the inputs, not an appendix. The candidate reads them first and builds everything downstream from them: beat 3 of the opening, the "why this role" answer, which STAR to lead with for which panellist, the bridges dropped into the close of an answer, and the calibrated questions in Section E. A pack that puts research after the scripts has already written the scripts without it.

Sections 3 and 5 are effectively mandatory for any round with a named interviewer or a named employer. Sections 4 and 6 are conditional — include them when the trigger condition in the section applies, and **say in the document that they were considered and skipped** when it does not.

Sections 3–6 are governed by a shared set of research disciplines, documented as **§R** immediately before section 3. Sections 2 and 7–9 are governed by a second cross-cutting discipline — **§X, cross-artefact consistency** — documented immediately before section 7. Neither is a numbered section; both are letters deliberately, so the twelve-section numbering never moves.

Each section below is documented with: **Purpose**, **Required fields**, **Format**, and an illustrative **Example**.

---

## 1. Front-matter

**Purpose.** Identify the prep at a glance. Lets the candidate pick the right pack from a folder of dozens.

**Required fields.**

- Title in form `# [Interview Format] Prep — [Role Title]`
- **Recruiter** — name and firm (recruiter screens) OR **Panel** — names and roles (panel interviews)
- **Format** — Phone / Video / In-person; duration; location if relevant
- **Reference** — recruiter reference number, role reference, or candidate-pack ID
- **Estimated read time** — both full pack and "executive summary + opening only" for time-poor pre-interview review

**Format.**

```markdown
# [Interview Format] Prep — [Role Title]

**Recruiter:** [Name, Title — Firm]  *(OR)*  **Panel:** [Name, Role; Name, Role; …]
**Format:** [Phone / Video / In-person], [Duration]
**Reference:** [Number or ID]
**Estimated read time:** ~[N] minutes (full pack); ~[N] minutes (executive summary + opening only)
```

---

## 2. Executive summary — 1-page brief

**Purpose.** A pre-interview brief read 30–60 minutes before the interview. Carries decisions, risks, and the key people. Should land in 3 minutes. For a panel or executive round it is not a condensed version of the pack — it is a **decision instrument**. Every line in it is either a choice the candidate has to make in the room, or a risk that will cost them if they make it wrong. Nothing in it is there to remind them what the pack says.

**Required components.**

1. **What this [call / panel / round] is for.** One paragraph naming the interviewer's likely test areas (typically 4–6) and the candidate's job in the conversation. **Where the panel is named, name every lens in the room inside this paragraph** — one clause per person, saying what each of them is actually testing — and close on the instruction a heterogeneous panel produces: *"Your job is not four separate answers; it's one coherent operating model that each of them can see their own stake in."* End by saying what kind of round this is — *"Expect strategic framing over deep behavioural probing — this panel already believes you can do the job from the paper; they're testing how you'd run it inside their institution."*
2. **Decisions and actions.** Bullet list of the deliberate choices the candidate should make in the room. Each bullet is a **directive**, not an observation. The recurring directive types:
   - **Lead with [the single most reusable answer across all the lenses in the room].**
   - **Give [named panellist] the real depth** — the depth-calibration call (see §5 and §9).
   - **Plant the honest gap early and once, not defensively when pressed.** This is a directive about *placement*, not content: the gap is volunteered on the candidate's timing, in one clean sentence, before anyone has to dig for it.
   - **Do not manufacture [the experience they do not have]** — always paired with the honest analogue to pivot to instead, named specifically.
   - **Watch-out: time discipline** — carrying the arithmetic in component 4.
   - **Close on forward commitment, not gratitude.** Executive panels want to hear what the candidate would do with the seat, not thanks for the opportunity.
   - **Confirm [practicality] upfront if asked** — recruiter screens only.
3. **Core risks.** Two-column table — Risk / Mitigation. 3–6 rows. Four binding rules:
   - Risks are **interview-specific**, never generic. "The candidate might get nervous" is not a risk; "[named platform] probed and the answer reads thin" is.
   - Where the panel is named, **attribute the risk to the panellist whose probe produces it** — *"[Panellist] probes with genuine research sophistication (frameworks, organisational-impact literature) and your answer reads as generic executive AI-speak."* An unattributed risk on a named panel is a research gap showing.
   - Every mitigation **names the exact section or STAR to deploy** — *"Use C8's honest framing verbatim"*; *"Lead plain, but have C6 ready with the engineering-gate language as a second layer if she asks a follow-up"*. A mitigation that only reassures ("stay calm", "be specific", "don't over-apologise") is not a mitigation.
   - **One row is standing** wherever written artefacts have already been submitted for the role — the panel references what is on record and the spoken answer drifts from it. See §X.
4. **Time-budget arithmetic.** State the sum, not the feeling: *"45 minutes, four panellists, likely 10–13 questions"* — then the delivery directive that follows from it: *"Lead every answer with the headline result in the first sentence — this panel will not wait for you to build to it."* A different arithmetic produces a different directive: *"45 minutes for two panellists plus your own questions is tight. Expect 5–7 questions asked live, not the full catalogue below. Prioritise landing fewer answers well over rushing through more."* Cross-check the arithmetic against Section B — if the summed time budgets in the question table do not fit it, one of the two is wrong.
5. **Key people involved and worth consulting.** One paragraph naming the executives the role sits under or alongside, and what each is likely to care about. Where §5 panel profiles exist, this paragraph is the two-line version of them and says so — it does not duplicate them.

**Format.**

```markdown
## Executive summary — 1-page brief

**What this [call / panel / round] is for.** [Paragraph naming test areas and the candidate's job.]

**Decisions and actions.**

- **Lead with [X].** [One-sentence directive.]
- **Plant [Y] early.** [One-sentence directive.]
- **[Action verb] [Z].** [One-sentence directive.]
- **Watch-out: [risk].** [One-sentence pivot or framing.]

- **Watch-out: time discipline.** [Duration], [n] panellists, likely [n]–[n] questions. [The delivery directive that follows.]
- **Close on forward commitment, not gratitude.**

**Core risks.**

| Risk | Mitigation |
|---|---|
| [Panellist] probes [specific thing] and [the specific way the answer fails]. | [Exact section / STAR to deploy], [how to deploy it]. |
| Panel references [the submitted artefact] and your spoken answer drifts from what's on record. | [C-numbers] are the spoken versions of exactly those written answers — same facts, same course-correction story. Stay consistent. |

**Key people involved and worth consulting.** [Paragraph naming executives and what each cares about; two-line version of the §5 profiles, not a duplicate.]
```

**Discipline notes.**

- Keep the section to **one printed page** (or ~600–800 words). It is a pre-interview brief, not a strategy paper.
- Decisions and actions should be **directives**, not observations. Use imperative voice.
- Risks should be **specific to the interview**, not generic.
- **A mitigation without a section pointer is a wish.** Every mitigation ends in something the candidate can turn to on the page — a section number, a STAR number, an evidence-bank ID, a named figure.
- **Do the arithmetic explicitly.** "Time will be tight" is not a decision. "45 minutes, four panellists, 10–13 questions, therefore headline first" is.
- **Write this section last, and re-check it after every reshape.** It names sections and STARs by number, so it goes stale the moment one is renumbered, cut or merged. A pack whose executive summary points at a STAR that no longer exists is worse than one with no executive summary.

---

## R. Research disciplines — cross-cutting (applies to sections 3–6 and to Sources)

**Purpose.** Sections 3–6 are the research half of the pack. They are the half that can embarrass the candidate in the room, because they assert things about other people's companies and other people's careers. These disciplines apply to every sentence in them. They are not style preferences — they are the reason the research is usable rather than merely impressive.

**Discipline 1 — every claim carries its epistemic status.** This is the single most transferable habit in the practice. Use the confidence ladder, in words, inline, in the sentence that makes the claim:

| Status | Phrasing to use | When |
|:---|:---|:---|
| First-party confirmed | "confirmed via their own leadership page", "confirmed via the organisation's own current people page (updated [date])" | The organisation's own current site says it |
| Independently corroborated | "confirmed via the company's own leadership page and independently corroborated via [named publication]" | Two independent sources agree, one of them first-party |
| Reasonably corroborated | "confirmed and reasonably corroborated" | Multiple secondary sources agree; no first-party page |
| Secondary only | "reported via professional-network sources, not confirmed on their own site" | One aggregator or professional-network profile only |
| Unconfirmed / refused | "The specific field of the doctorate is not confirmed … don't guess at or repeat a specific field, since none is verified" | The obvious next fact could not be verified — name the gap and forbid the guess |
| Inference | "**Likely voice and tone (inference).**" | Reasoned from evidence, never presented as fact |

**Discipline 2 — source-authority ranking, and what to do when sources conflict.** Rank: (1) the organisation's own current page, (2) dated direct intel from the candidate, the interview invitation or the calendar event, (3) a reputable named publication, (4) a professional-network profile, (5) a data aggregator. When two sources conflict, name the conflict in the document, say which one you are treating as authoritative, and say why. Two illustrative cases: a secondary source names one person as CEO while the company's own current About Us page names another — the current first-party page wins, and the superseded name is flagged as a likely predecessor rather than silently dropped. An organisation's own senior-officers page gives a panellist a different portfolio from the one in the interview invitation — the invitation wins, as the more recent and more direct source, and the discrepancy is written into a **Research caveat** paragraph at the foot of Sources.

**Discipline 3 — no unsourced person-claims, ever.** A claim about a named individual either carries its source in the same sentence or does not go in the document. This includes negative findings: *"No independently confirmed public career history or professional-network profile could be located for her"* is a legitimate, useful entry. An absence honestly reported is worth more than a plausible guess.

**Discipline 4 — inference lives in its own labelled paragraph.** Never let inference share a paragraph with confirmed fact. Give it its own bolded lead-in — **Likely voice and tone (inference).** or **Likely working style (inference from career shape).** — and open the section with a blockquote disclaimer naming what the inference is built from.

**Discipline 5 — handling instructions travel with sensitive facts.** Some facts are worth knowing and wrong to raise. Mark them at the point of use: *"Background awareness only — not a topic to raise unprompted"* (a board-succession announcement); *"a personal detail worth knowing rather than using as a talking point"* (a panellist's family or hobby); *"hold in reserve"* (a technical detail that only helps if the panel goes there first).

**Discipline 6 — per-round information hygiene.** Intel obtained in, or about, one round does not travel into another room. A later round's brief carries this as an explicit directive — *"Do not reference [X]'s personal situation in this room. That context was shared with you in confidence and relates to Round 1 specifically"* — repeated in that round's speaking notes as a one-line **Remember:** anchor. Where a later panel might ask what an earlier round covered, pre-script the clean, generic answer.

**Discipline 7 — date the research.** Every web-research block in Sources carries the date or date range it was performed (`Company and panel research (web, [date])`). Research ages; a reader six weeks later needs to know how stale it is.

---

## 3. Company / organisational context

**Purpose.** The section that turns "qualified candidate" into "candidate who clearly gets what we're building". It is placed before the opening script deliberately: the candidate reads it first and builds everything downstream from it — the opening's beat 3, the "why this role" answer, the calibrated questions in Section E, and the bridges dropped into the close of a STAR.

**Required components.**

1. **Who they are.** One paragraph: legal entity name, headquarters and ownership or listing structure (dual-listed on two exchanges; an independent statutory entity under named legislation; privately held), founding year and growth story, a scale marker, and the segment or division structure with the operating brands named inside each.
2. **Acquisition and growth history** — one bullet per material transaction, each with the **amount and the completion date**, plus what the acquisition was *for* strategically. Flag which entity is hosting the interview.
3. **Most recent published financial results** — the specific figures and the **release date**. Revenue, margin, growth rates, and the segment called out as strongest. For a public-sector body, the equivalent is programme status: funding decision date and amount, current phase, published cost estimate, staged delivery timeline.
4. **The internal technology / shared-services function** — its structure, where it is based, what it is formally responsible for in the organisation's own words, who leads it, and its **certifications** (an ISO certification with the policy document published is "a real, audited governance credential rather than a marketing claim"). Name the confirmed people in it and flag the corroborated-but-unconfirmed ones separately.
5. **Governance / board-change note**, explicitly marked as handling-restricted. This is a fixed convention, not an optional extra.
6. **"Why this matters for the [call / round]"** — one paragraph converting the research into an argument about the role. Never end the section on facts.
7. *(Optional, high value for short calls)* **Quick-reference bridges table** — a two-column map of *"if the conversation touches X"* → *"bridge it to this specific, current fact about them"*. This is the piece that makes research usable live rather than merely known.

**Public-sector / statutory-authority variation.** Where the target is a government entity or programme, break the section into sub-headings rather than running it as one block: *Origin, mandate and legal form* · *Where the programme actually is, right now ([month year])* · *Scale, economics and timeline* · *Technical and delivery complexity* · *Political and governance context* · *International comparator worth knowing* · *Why this matters for the [role] conversation*.

**Format.**

```markdown
## Company context — [Organisation]

**Who they are.** [Entity, HQ, listing/ownership, founding and growth, scale marker, segment structure with brands named.]

**Recent acquisitions.**

- **[Entity]** — [what it does], acquired for [amount] and completed [date]. [Strategic rationale in the group's own framing.]
- **[Entity]** — acquired in [year] for [amount]. Per the [results release] ([date]), [current performance]. **This is the business hosting [the interview].**

**Group financial context ([period], released [date]).** Revenue rose [x]% to [figure]; earnings rose [y]% to [figure], margin improving to [z]%. [Segment called out.]

**[Internal technology function] — structure and team.** [What it is, where based, what it owns in their own words, certifications.]

**Who's in it (confirmed and reasonably corroborated).** [Named people, each with its confidence marker.]

**Governance note.** [Board or leadership change.] Background awareness only — not a topic to raise unprompted.

**Why this matters for the [call / round].** [The argument, not the facts.]

### Linking your answers to the [programme] — quick-reference bridges

| If the conversation touches... | Bridge it to... |
|:---|:---|
| [Your STAR / theme] | "[Spoken bridge sentence naming a specific, current fact about them]" |
```

**Discipline notes.**

- Figures without dates are worthless in the room. Every number carries the release date of the document it came from.
- Do not overclaim familiarity beyond what is public. Reference the completion date, deal size and reported growth factually; do not speculate on integration specifics you do not have.
- Two or three bridges landed naturally will do more work than all six rushed. Build more than the candidate will use; tell them to use fewer.

---

## 4. Operating entities and business units

**Purpose.** Where the organisation runs several distinct operating businesses under one group, this section makes the candidate credible about the *shape of the estate* — which is exactly what a group technology or group operations seat is hired to hold. Include it whenever the target has more than one operating brand, more than one acquired entity, or a panel drawn from different businesses. Skip it — and say so — for a single-entity employer.

**Required components — one block per entity.**

1. **What it actually does** — in operational language, not marketing language.
2. **Who runs it** — named, **with how that was confirmed** ("confirmed via the entity's own current About Us page, updated [date]"). Where no leadership is named publicly, say so and say what that tells you: *"No leadership team is named on [entity]'s own public site — worth knowing that this integration is genuinely fresh, which strengthens rather than weakens the 'help me stitch six IT environments together' narrative."*
3. **Scale markers** — fleet, depots, sites, headcount, geography, founding year, revenue share. These are what let the candidate speak about a business they have never seen.
4. **Systems and vendors, where publicly named** — the core operating system, the backup platform, the certification regime. Name the vendor and what its modules actually do.
5. **Certification / compliance profile** where the business is compliance-led.
6. **Domain-term explainer** wherever the entity's world has jargon the candidate would otherwise parrot (see below).
7. **"Reading this as a set"** — the closing synthesis that turns the list into an argument. Never end on the last entity.

**Domain-term explainers.** When a term belongs to the target's world rather than the candidate's, give it a short explainer box: what the standard or term is, which part of it actually matters here, and what it means in practice on the ground. The test is whether the candidate can *use* the term correctly under follow-up, not merely say it.

> **On "[domain term]."** [What the body or standard is.] The piece that matters here isn't [the meaning a general reader would reach for first] — it's [the specific element that governs this employer's operations], [what it is and how it is carried]. Because the format is a shared standard rather than proprietary to one operator, [what any compliant system can therefore do]. In practice: [the concrete consequence on the ground — what moves between whose systems without custom integration or manual rework] — a good, specific detail to hold in reserve if the panel goes deep on [the entity].

**Format.**

```markdown
## [Region] entities — key people and services

[One-paragraph framing: how many entities, how the role sits across them, and why knowing this is credibility in the room — named to the specific panellist it lands with.]

**[Entity]** — [what it does]. [Scale markers: fleet, depots, sites, founding year, revenue share.] **Leadership (confirmed via [source]):** **[Name — Title]**; [further names].

**[Entity]** — [what it does]. Runs on [named system] — [what the vendor is and what its modules do]. **No leadership team is named on [entity]'s own public site** — [what that tells you].

> **On "[domain term]."** [What it is. Which part matters here. What it means in practice.]

**Reading this as a set.** [The synthesis: what the shape of the estate means for the role, and which of the candidate's stories it maps onto.]
```

**Discipline notes.**

- The synthesis is re-cut for each round; the entity blocks are not. See *Multi-round progression*.
- Where a name is not independently confirmed via the entity's own official page, flag it as such rather than stating it as fact.
- Resist listing entities the candidate will never be asked about at the same depth as the ones a panellist actually runs.

---

## 5. Panel and individual research

**Purpose.** The section that decides how the candidate listens as much as how they speak. Everything else in the pack is about what the candidate says; this is about who is receiving it, what they are testing underneath the question, and which story to reach for first with each of them.

**Required components.**

1. **Sourcing disclaimer, as an opening blockquote.** State what the profiles are built from, state that no direct quotes turned up (or name the ones that did), and state plainly that the "likely voice" paragraphs are reasoned inference — *"a steer, not a script."*
2. **Per person, in this order:**
   - **Confirmed biography, with its source named in the sentence.** Title, remit, what the organisation's own framing says they own.
   - **Career history and tenure.** Where they came from, how long they have been there, and — where it is the most telling fact — how they got the job. A cadet-to-GM path over 20 years is a finding, not trivia.
   - **Why they matter in this room.** Their weight relative to the other panellists, and what they are accountable for that touches this role.
   - **Likely voice and tone (inference)** — its own labelled paragraph, reasoning explicitly from the evidence just given ("a 30-year internal-promotion career, starting as a school-leaver cadet, strongly suggests …"). Where no personal material exists at all, reason from the organisation's own published voice instead, and say that is what you are doing.
   - **Likely lens** — the one question shape they will actually probe.
   - **Tailored connection point** — which STAR or evidence to lead with for this person, and what *not* to over-explain to them.
3. **"The most important fact in this brief"** callout, where one exists. When research turns up a single fact that reframes the whole room — a panellist who has personally been covering the vacant remit for 18 months and is interviewing their own relief — give it its own bolded callout and then spell out what it changes about how they will listen.
4. **Alignment note.** Where two panellists have a shared history, say so and instruct accordingly: treat an aligned pair as **aligned**, not as two independent assessors. Consistency across answers reads as more credible than tailoring a different message to each; per-panellist tailoring is about *which STAR to reach for first*, not about telling two different stories.
5. **"Reading them together"** — the closing synthesis across the panel as a set.

**Format.**

```markdown
## Panel profiles — [Name], [Name] and [Name]

> Built only from what's publicly confirmable — [organisation]'s own leadership page and professional-network sources. No direct quotes or interviews from any panellist turned up, so the "likely voice" paragraphs below are reasoned inference, not documented fact — treat them as a steer, not a script.

### [Name] — [Title]

**History and background (confirmed via [source]).** [Tenure, path, remit, in the organisation's own framing.]

**Additional detail (per [secondary source] — not independently confirmed on an official page).** [Education, earlier roles.] **If accurate, this means [the inference that follows].**

**Why they matter [most] in this room.** [Weight and accountability.]

**Likely voice and tone (inference).** [Reasoned from the career shape just described.]

**Likely lens.** [The question shape they will probe.]

**Tailored connection point.** [Which STAR to lead with; what not to over-explain.]

**The most important fact in this brief.** [Where one exists — the fact, then what it changes.]

**Why this matters for the room.** [Alignment note where panellists share a history.]

**Reading the [n] of them together.** [Synthesis and the single instruction it produces.]
```

**Illustration — what a "most important fact" callout does.** Research establishes that one panellist has personally been covering the vacant remit in a reduced capacity for roughly eighteen months, on top of their substantive role, and has no interest in continuing. **They are, in effect, interviewing their own relief.** That reframes everything about how they will listen: they already know exactly what the job involves day to day — better than the advertisement does — and they will notice immediately if an answer is generic rather than grounded in real operational understanding. The fact is one sentence; the instruction it produces is the reason the section exists.

**Discipline notes.**

- An honest negative finding beats a confident guess. *"No independently confirmed public career history could be located for her"* is a usable line; a borrowed job history from a stale aggregator is a trap.
- Personal colour (family, hobbies) is context for warmth, never an agenda item. Mark it that way in the text.
- Never write a "likely voice" paragraph that could pass for fact on a fast read. The bolded `(inference)` label is load-bearing.

---

## 6. Structural-reality analysis

**Purpose.** Some rounds are not really about capability at all — they are about a structural tension in the role that everyone in the room can feel and nobody has named. This section names it, explains what each panellist is testing underneath their questions, and gives the candidate an honest answer to the tension rather than a way of pretending it does not exist. Include it whenever the role has a matrix or dotted-line structure, a contested scope, a shared-service-to-business-unit relationship, or a reporting line that sits somewhere other than where the day-to-day accountability sits. Skip it — and say so — for a clean single-line role.

**Required components.**

1. **The structure, stated plainly.** Who the formal reporting line is, who the dotted lines are, and what membership of each stakeholder's leadership team actually implies.
2. **The recurring failure mode**, named as a known pattern rather than a personal risk: *"the business-unit GM feels like the technology person is 'Group's person', parachuted in, prioritising head-office agendas over their business's actual needs."*
3. **What each panellist is almost certainly testing underneath their specific questions** — as bullets, in their language, with the concrete detail that proves the point (their busy periods, their P&L pressure, their integration timeline).
4. **How to answer it honestly if raised** — be honest about the tension rather than pretending it does not exist, make the answer specific rather than abstract, and land it on the candidate's own evidence of having made dual accountability work before.

**Format.**

```markdown
## Understanding the matrix — how this role actually sits, and why it's the real subject of this interview

**The structure.** [Formal line, dotted lines, what membership implies.] This is a genuinely common structure for [context], and it has one recurring failure mode: **[the failure mode, in the stakeholder's own words].**

**What each of these panellists is almost certainly testing, underneath their specific questions.**

- **[Test 1, as the question they are really asking]** — [the concrete proof they are listening for, named per panellist].
- **[Test 2]** — [concrete proof].

**How to answer this directly if it's raised (and it likely will be, in some form).** [Honest acknowledgment of the tension; the specific, non-abstract commitments; the evidence anchor from the candidate's own history.]
```

**Discipline note.** This section reframes almost every other section in the pack. Where it exists, say so at the top of the document and tell the candidate to read it before anything else.

---

## X. Cross-artefact consistency — cross-cutting (applies to sections 2, 7–9 and to Sources)

**Purpose.** By the time the candidate sits a panel they have usually already put several thousand words about themselves on the record *for that specific role* — a cover letter or statement of claims in `Submissions/`, screening-question answers, a message to the hiring team, the resume version sent, and the prior rounds' briefs. **The panel has read them.** The hiring manager may have written the interview questions from them. A spoken answer that contradicts a submitted one is not a presentation problem; it is a credibility problem, and it is the one failure in the pack that cannot be recovered in the room.

**The reconciliation — run it before the pack is finalised, not after.**

1. **Inventory every artefact already submitted for this role.** Cover letter or statement of claims, screening-question responses (the **final submitted text**, not the drafting notes), any message to the hiring team, the resume version sent, and every prior-round brief in the same process.
2. **Read each pre-prepared response against them.** Any STAR covering the same ground as a written answer must carry the **same organisation, the same figures, the same sequence of events and the same admission**. Where the written answer named a course correction — a first approach that did not hold — the spoken one names the same course correction, not a tidier one.
3. **Say so in the pack.** Where a response is the verbal version of something already on record, mark it in the coaching notes: *"This is the spoken version of your written screening-question answer — keep the facts identical if the panel cross-references it."* *"This mirrors the close of your written cover letter almost exactly — consistency is a strength here, not repetition to worry about."* The candidate needs to know which answers are being checked against a document, and that repeating themselves there is correct rather than lazy.
4. **Carry forward what the written artefacts deliberately did *not* claim.** This is the half that gets missed. Where a submitted answer withheld a claim on purpose — a named external framework the evidence did not support, a qualification not held, a scope not owned — that restraint becomes a **prohibition** in the spoken pack (§9). A screening-question sourcing note reading *"no claim to a named external framework was made, since the evidence bank does not confirm the programme was formally run under it"* becomes the coaching-note line *"Don't claim a named external framework — you're not confident it formally governed this specific programme. Stick to your own named plan."*
5. **Use the same words for the gap.** Where the submitted letter acknowledged a fit gap, the honest framing in §9 acknowledges it in the same terms — *"I have not held a formal role inside [the sector], and I will not pretend otherwise"* written, *"I have not held a formal role inside [the sector], and I'm not going to pretend otherwise"* spoken. Where the role has a matrix row prescribing a fit-acknowledgment style, that style governs both artefacts.
6. **Log the drift risk as a standing row** in the executive summary's core-risks table (§2), with the mitigation naming the specific responses that carry the reconciled facts.
7. **List every reconciled artefact in Sources**, with its link, so the reconciliation can be re-run when the pack is reshaped or a later round is built.

**Discipline notes.**

- Reconcile against the **final submitted text**. A screening answer trimmed to fit a hard character limit may have lost the very qualifier the spoken answer is leaning on.
- The reconciliation runs **again after every content reshape**. Tightening a STAR is exactly how a figure drifts.
- Consistency is not the same as recital. The panel that has read the application does not want it read back — extend the written answer with the judgement call underneath it (*Multi-round progression* makes the same move across rounds). Same facts, more mechanism.

---

## 7. Section A — Opening "Tell me about yourself"

**Purpose.** The verbatim spoken script for the most predictable opening question. The single most important 2 minutes of any interview — sets the panel's expectation of pace and register.

**Required components.**

1. **Heading** — `## A. Opening — "Tell me about yourself" (2–2.5 minutes spoken)`
2. **Usage note** in blockquote: *"Use this verbatim or close to it. Slow pace. Intentional pauses where indicated. Aim for ~280 words spoken."*
3. **Spoken script** — ~280–400 words, written for spoken delivery (sentence length, pacing per the Interview Voice and Style Guide)
4. **Pause markers** — `*[pause]*` and `*[brief pause]*` embedded in the script at deliberate moments
5. **Closing marker** — `*[stop — pass back to recruiter]*` or `*[stop — pass back to chair]*` at the end
6. **Coaching notes** — 3–5 bullets at the end (per Interview Voice and Style Guide conventions)

**Three-beat structure for the opening.**

- **Beat 1 — Scale (60–80 seconds).** Most recent senior role(s) and the substance of the work. Lead with what the role has been *about*, not where or when.
- **Beat 2 — Sector breadth (40–60 seconds).** Earlier roles that show the transferability and breadth. Compress prior roles into bridge sentences.
- **Beat 3 — Why this role, why now (40–60 seconds).** What draws the candidate to *this* role, *this* organisation, *this* timing. Forward-facing, not retrospective.

Do not add a fourth beat. If a beat runs long, cut from beat 2, not beat 3.

**Format.**

```markdown
## A. Opening — "Tell me about yourself" (2–2.5 minutes spoken)

> Use this verbatim or close to it. Slow pace. Intentional pauses where indicated. Aim for ~[N] words spoken.

[Beat 1 — scale paragraph.]

*[brief pause]*

[Beat 2 — sector breadth paragraph.]

*[pause]*

[Beat 3 — why-this-role paragraph.]

*[stop — pass back to recruiter / chair]*

**Coaching notes.**
- [Directive 1]
- [Directive 2]
- [Directive 3]
- [Directive 4]
```

**Discipline notes.**

- Read the script aloud at least twice before the interview. Time it. Cut if over.
- Resist the urge to list every achievement. The opening tests whether the candidate can be concise.
- Drop optional detail if time pressure is signalled.
- Do not open with "thanks for taking the time" — open with positioning, not pleasantries.

---

## 8. Section B — Likely questions and positioning notes

**Purpose.** A scannable table of the most likely interview questions, each with the lead approach, the evidence-bank anchors that support the answer, and a time budget. Used in the room as a quick-reference.

**Required components.**

1. **Heading** — `## B. Likely questions — positioning notes`
2. **Question table** with five columns: #, Likely question, Lead with, Evidence anchor, Time budget
3. Rows covering 10–25 likely questions depending on interview length
4. **Per-panellist attribution on every question where the panel is named.** Two forms, either acceptable as long as the pack is consistent:
   - **Who is likely to ask it** — prefix the question with the name: `([Name]) "How do you personally work with AI — are you still hands-on, or purely a strategist now?"`
   - **Who it lands hardest with** — annotate the row: `*(from [Name] directly — highest-value question)*`.

   Attribution is what turns a generic question bank into a room-specific one. It pairs directly with each panellist's **likely lens** in §5 — if a question cannot be attributed to a lens in the room, either the lens research is thin or the question does not belong in the table.
5. **The attribution caveat**, as a discipline note immediately under the table. Mandatory wherever attribution is used.

**Question types to cover (calibrate to interview format).**

| Type | Recruiter screen | Behavioural panel | Executive panel |
|---|---|---|---|
| Tell me about yourself | Always | Always | Always |
| Why this role / why now | Always | Always | Always |
| Technical / capability-specific probes | 2–4 (the role's headline capabilities) | 3–6 | 1–2 (strategic only) |
| Behavioural STAR probes | 1–2 (the highest-risk one) | 6–10 | 2–4 (with strategic framing) |
| Stakeholder / leadership style | 1 | 2–3 | 2–3 |
| 30/60/90 / first-X-days | 1 | 1 | Always |
| Why leave current | 1 | 1 | 0–1 (often known by this stage) |
| Practicalities (citizenship / clearance / notice / salary / location) | 4–6 | 1–2 | 0–1 |
| Candidate questions back | 1 (placeholder for Section E) | 1 (placeholder) | 1 (placeholder) |

**Format.**

```markdown
## B. Likely questions — positioning notes

| # | Likely question | Lead with | Evidence anchor | Time budget |
|---|---|---|---|---|
| 1 | "Tell me about yourself / walk me through your background." | The opening above (Section A). | A1, A6 | 2–2.5 min |
| 2 | "Why this role? Why [Organisation]? Why now?" | [Lead sentence summarising the why.] | A3 or A4 (sector-dependent) | 90 sec |
| 3 | "What's your [headline capability] experience?" | [Lead sentence — 1–2 layers of evidence in summary.] | [Entry IDs] | 90 sec |
| … | … | … | … | … |
```

**Discipline notes.**

- **Attribute, then disclaim.** Close the table with the standing caveat: *"Questions 8–10 are attributed to a likely asker based on portfolio fit, not a guarantee of who actually asks them — any panellist may ask any question. Don't assume [Name] won't ask the governance question or [Name] won't ask the student-benefit one."* Attribution that reads as prediction makes the candidate *slower* when the wrong person asks — the caveat is what keeps it a preparation aid rather than a script.
- **Sum the time-budget column and check it against the executive summary's arithmetic (§2).** A 15-row table averaging 2.5 minutes does not fit a 45-minute panel that also has a questions-back slot; say in the table's discipline note which rows are expected to go unasked.
- Order the table by likelihood, not by topic. The most-likely questions first.
- "Lead with" is the **first sentence of the spoken answer**, not a topic summary. Write it the way the candidate would say it.
- Time budget is **strict**. If 30 minutes total and 20 questions, average is 90 seconds per answer. Plan accordingly.
- For questions covered by a pre-prepared STAR in Section C, cross-reference: *"**See Section C[n] — full STAR.**"*
- For practicalities (citizenship, clearance, salary), Lead with = the literal answer.

---

## 9. Section C — Pre-prepared STAR responses for highest-risk questions

**Purpose.** Full STAR scripts for the questions where the candidate most needs to land cleanly. Practised out loud before the interview.

**Selection criteria** — include a full STAR for any question where:

- The question is high-probability AND the answer is non-trivial.
- The question is lower-probability but high-risk if asked (e.g. lived-experience probe; failure question; salary-history probe).
- The question requires careful framing of an honest gap.
- The question is the panel's most likely test of the **single biggest fit risk** for this role.

Typical count: **5–8 pre-prepared STARs** for a 30-min recruiter screen; **8–12** for a 60–90 min panel.

**Required components per STAR.**

1. **Heading** — `### C[n]. "[Question text]"` (use the exact phrasing the panel is likely to use; gives the candidate instant pattern-match)
2. **Attribution and risk flag**, appended to the heading. Where the panel is named, tag the likely asker *and the lens they are probing* — *"([Name] — technical-depth probe)"*, *"([Name] — COO lens)"*, *"([Name] — highest-risk honest-gap probe)"*. Where the pack spans rounds, the tag carries the round instruction instead — *"(hold in reserve — use if asked directly, especially by [Name])"*, *"(extended from the recruiter screen)"*. Where no panel is named, flag risk only — *"(highest-risk lived-experience probe)"*, *"(critical to land)"*. The §8 attribution caveat covers Section C as well; do not repeat it per STAR.
3. **STAR body** in four bold-labelled paragraphs: **Situation.** / **Task.** / **Action.** / **Result.**
4. **Drop list** — a per-response table naming the first and second cuts as *specific sentences* with per-cut savings, closed by the combined runway and the standing line *"Never cut the bolded principle lines above."*
5. **Coaching notes** — 3–5 bullets per STAR, built from the four required elements below.

**STAR word-count targets** (drawn from the Interview Voice and Style Guide):

| Format | Total target | Situation | Task | Action | Result |
|---|---|---|---|---|---|
| Recruiter screen (~90 sec) | 210–240 words | 25–35 w | 20–30 w | 100–140 w | 40–60 w |
| Behavioural panel (~2 min) | 280–320 words | 30–50 w | 25–40 w | 140–180 w | 50–80 w |
| Executive panel (~2–3 min) | 320–480 words | 40–60 w | 30–50 w | 150–220 w | 60–100 w |

**Honest-framing variation.** For lived-experience or hard-gap questions, replace the standard STAR with an **honest framing** block presented as a blockquote (verbatim spoken script with explicit acknowledgment first, evidence anchors second, forward-facing motivation third).

**Coaching notes — required elements.** Three to five bullets per STAR. For any response carrying risk — an honest gap, a claim one sentence away from a more impressive untrue one, a follow-up that invites an invented specific — the block is not complete without all four of these:

1. **Prohibitions — what must not be claimed anywhere in this answer**, named explicitly, with the reason attached. *"Do not claim [governance body] exposure, [domain] governance, or [domain] leadership anywhere in this answer — none of it is true, and this panel would know."* *"Don't claim multi-agent orchestration experience if pushed on architecture specifics — name the multi-model swap design instead, which is what you actually built."* Every honest-gap or hard-gap response carries a prohibition list. So does every answer where the adjacent, more impressive claim is one sentence away from the true one. Prohibitions inherited from what the submitted artefacts deliberately withheld come in via §X.
2. **Delivery discipline — how it is said, not what is said.** *"Acknowledge for the full first sentence before pivoting — cutting it short reads as evasive."* *"Lead with the headline before the course-correction story — don't bury the win under the failure."* *"Numbers first, always."* *"Don't say 'we' in the Action — this was your call."* *"Watch pace — this STAR has a lot of moving parts; don't rush the Result."*
3. **A don't-invent directive, with the substitute line supplied.** For every follow-up that would tempt an invented specific, name the temptation *and hand the candidate the replacement sentence*: *"If asked for a specific headcount or dollar figure for the function, don't invent one — say you'd want thirty days to size it properly against the actual use-case portfolio, and that you'd bring a working range, not a guess, to that conversation."* A prohibition with no substitute leaves the candidate silent; a prohibition with a substitute leaves them fluent.
4. **Rehearsal priority, ranked across the pack.** Not a per-STAR flag — a **ranking**: *"This is your single highest-risk answer in the pack — read it aloud at least three times before Friday"*, then *"This is your second-highest-risk answer after C5 — practise it enough that 'I haven't' doesn't sound rehearsed-defensive."* The ranking is what tells the candidate where to spend the last hour before the interview. Rank at least the top two; never rank everything.

**Depth calibration — register inside a single answer.** Where the panel is heterogeneous, one listener usually owns the subject. §5 identifies them — *"the panel's technical ceiling"*, *"treat her as the panel's sophistication ceiling, not its easiest seat"*. Section C says what to do about it in the moment, and both halves are directives that belong in the coaching notes:

- **Lead plain for the room, hold a second layer for the person who can follow it.** *"This is the one STAR where you can go deeper than the standard executive-safe framing if she follows up — she'll likely appreciate the precision rather than find it excessive. Don't lead with the jargon; have it ready."*
- **Do not spend the room's time explaining that person's own home turf back to them.** *"[Name] will recognise this immediately; if he's the one asking, go straight to the judgement calls rather than re-explaining the platform to him."*
- **Bound the depth.** Real depth is not a lecture back at an expert: *"if she asks a research-literature-style follow-up, the honest answer is a genuine view, not a deflection — but keep it to one tight point, not a lecture back to an actual expert on the subject."*

The failure this prevents is symmetrical — patronising the specialist, or losing the generalists. Calibration happens *within* one answer, not by writing two versions of it.

**Honest-gap doctrine.** The honest framing is a **spoken script**, not a position. It is written as a blockquote with pause markers so the shape of the delivery sits on the page, and it obeys four rules:

1. **Acknowledge for the full first sentence.** *"I should be direct about this: I have not held a formal role inside [the sector], and I'm not going to pretend otherwise."* Hedging the acknowledgment into a subordinate clause on the way to the pivot reads as evasive — and a panel that has read the written application already knows the gap is there.
2. **Do not manufacture the missing experience** — and say in the coaching notes what the manufactured version would sound like, so the candidate can hear themselves starting it. Where a softening frame would be untrue, forbid the frame by name: *"do not soften it with 'adjacent' framing that isn't true here; there is no adjacent experience to point to."*
3. **Pivot to the honest analogue, named and bounded.** The closest real thing, with its evidence — plus an explicit instruction not to oversell it: *"the regulator pivot is the honest analogue — it's a real, defensible connection, not a stretch. Don't oversell it as equivalent to being inside one."*
4. **Close forward, on what they would do rather than what they lack.** *"That's what I'd bring into this room on day one, not [sector]-specific instinct I don't actually have."* *"That's a genuine listening exercise in the first thirty days, not an assumption I'd walk in with."*

**How this interacts with the written fit-acknowledgment discipline.** The honest framing is the *spoken form* of the fit-acknowledgment style the matrix row prescribes for the written application — the same gap, acknowledged in the same order (name it, don't dress it, pivot to the evidenced analogue, close forward), with pause markers and a prohibition list added because it is being said out loud to people who can follow up. Use **the same words for the gap** as the submitted letter used; see §X. Any divergence between the two is a §X finding, not a stylistic choice.

**Honest-framing blocks carry drop lists too.** They are spoken responses under the same time pressure as every other one. Never put the acknowledgment sentence, the bolded pivot line or the forward close in the drop list.

**Format — standard STAR.**

```markdown
### C[n]. "[Question text]"

**Situation.** [1–2 sentences setting the scene.]

**Task.** [1 sentence framing the challenge.]

**Action.** [3–5 sentences naming what the candidate did. Use "I" not "we" unless directly relevant. Include 1–2 specific metrics or moves that anchor the answer.]

**Result.** [1–2 sentences naming the measurable outcome + the lesson or forward link.]

**Coaching notes.**
- [Directive 1]
- [Directive 2]
- [Directive 3]
```

**Format — honest-framing variation (for lived-experience / hard-gap questions).**

```markdown
### C[n]. "[Question text]" *([Panellist name] — highest-risk [type] probe)*

**Honest framing.**

> "[Verbatim spoken script. Acknowledge the gap explicitly and in full in the first sentence. *[brief pause]* Pivot to the closest honest analogue with specific evidence. *[pause]* Close on forward-facing motivation and what they would do. ~150–250 words, with pause markers embedded.]"

**Drop list.**

| Response | First cut if pace is tight | Second cut |
|---|---|---|
| C[n] | "[specific sentence]" (saves ~[n] sec) | "[specific sentence]" (saves ~[n] sec) |

*Combined runway: ~[n] sec. Never cut the acknowledgment sentence, the bolded pivot line or the forward close.*

**Coaching notes.**
- **[Delivery discipline]** — [how it is said; acknowledge for the full first sentence].
- **[Prohibition]** — do not claim [X, Y or Z] anywhere in this answer — [why: none of it is true, and this panel would know].
- **[Don't-invent directive]** — if [follow-up], don't [invent]; say "[the substitute line, supplied]".
- **[Rehearsal priority]** — this is your [highest / second-highest]-risk answer in the pack — [rehearsal directive].
```

---

## 10. Section D — Practicalities cheat sheet

**Purpose.** Quick-reference for the practical questions every recruiter and most panels ask. Answers from this table without burning thinking time.

**Required sub-sections.**

### D1. Salary expectation — coaching

**D1 is round-dependent, not one script.** Calibrate the posture before writing the section — a recruiter screen and a final executive panel want opposite behaviour, and a D1 written for the wrong round is worse than none.

| Round | Posture |
|:---|:---|
| **Recruiter screen** | This is where salary genuinely lives. The recruiter often *needs* a number to progress the process — reflect first, but **don't let the call end without a ballpark exchanged**. Carry the full apparatus: the market research that built the range (published bands, comparator day rates, the read-across for each), the engagement mechanics wherever they are non-standard (payroll vs company structure, superannuation or pension treatment, notice), and an anchored script for "if pushed for a number first". |
| **Behavioural panel** | Lighter — usually cleared at the screen. Keep the reflect-first script; drop the market-research table unless the published band has moved or the scope has changed since the screen. |
| **Executive / final panel** | Say plainly in the section that salary is **unlikely to come up here at all**, and that the candidate should **not raise it themselves** — it reads as premature at a final panel. Keep a one-line reflect-first script and a single anchoring instruction for the case where they are genuinely pressed. Salary is for HR and contract negotiation, not the panel. |
| **Fit and working-relationship round** | Not a salary conversation. Same posture as the executive panel. |

**Required sub-components — scaled to the posture above.**

- **Default reply** (reflect first): one-sentence script that hands the band question back to the recruiter.
- **If they answer**: anchor in the upper half of whatever they say.
- **If pushed for a number first**: anchored answer that names the band, the role's seniority justification, and a working total-remuneration figure (recruiter screen: full; executive panel: one line).
- **Reference points**: 2–4 bullets giving the published or estimated band for the role family / sector / level. **Recruiter screens only** — and where the range was assembled from market research rather than quoted by anyone, say so explicitly, with a comparator table showing how each benchmark was read across.
- **Watch-outs**: 2–4 bullets on what not to do — and make at least one of them round-specific (*"Don't raise salary yourself at this stage — it reads as premature at a final panel"* vs *"Don't let the 15-minute call end without at least a ballpark exchanged — the recruiter needs it to progress the process"*).

### D2. Practicalities — quick confirmations

Two-column table covering:

- [Nationality / citizenship requirement, where relevant — e.g. Australian / UK / US citizenship]
- [Clearance level required, where relevant — e.g. NV1, SC, TS/SCI — with grant date if held]
- Police check / employment screening
- Notice period
- Location preference
- Right to work
- Disability declaration (RecruitAbility / equivalent, where relevant)
- Any other role-specific practicalities (e.g. willingness to travel, hybrid arrangements)

**Format.**

```markdown
## D. Practicalities cheat sheet

### D1. Salary expectation — coaching

**Reflect first.** Don't quote unless pushed.

> "[Default reply script.]"

If the recruiter answers, anchor in the **upper half** of whatever they say.

If pushed for a number first, anchor:

> "[Anchored answer.]"

**Reference points.**
- [Band 1 reference.]
- [Band 2 reference.]
- [Comparator.]

**Watch-outs.**
- [Watch-out 1]
- [Watch-out 2]
- [Watch-out 3]

### D2. Practicalities — quick confirmations

| Question | Answer |
|---|---|
| [Citizenship / nationality]? | **[Answer]** |
| [Clearance] obtainable and maintainable? | **[Answer]** |
| Police check / employment screening — any concerns? | **[Answer]** |
| Notice period? | **[Answer]** |
| Location preference? | **[Answer]** |
| Right to work in [country]? | **[Answer]** |
| [Other role-specific practicality]? | **[Answer]** |
```

**Discipline notes.**

- **Hedge the answers that are not confirmed, in the table itself.** The §R confidence discipline reaches into Section D: *"Standard — confirm current notice period if asked; not flagged as a constraint in prior submissions"* is honest; a confident invented notice period is not.
- **Frame the constraint positively where it is a known concern** — *"Fixed-term (5-year) comfort? **Yes — frame positively: 'a genuine multi-year mandate to build something durable', not a concern to manage.**"*
- **Where the round is unlikely to spend time here, say so under the table** — *"(This panel is unlikely to spend meaningful time on practicalities — Section D is here for completeness, not because it's a likely focus.)"* It stops the candidate over-rehearsing a section that will not be used.

---

## 11. Section E — Questions to ask the panel

**Purpose.** The candidate's prepared questions back to the recruiter or panel. Time permitting (typically 3–5 minutes at end of recruiter screens; sometimes longer in panel formats). Signal preparation and strategic thinking.

**Required components.**

1. **Heading** — `## E. Questions to ask [name] *(time permitting — typically 3–4 minutes at end)*`
2. **Usage note** — *"Pick two or three. Don't ask all five."* (or equivalent — the count varies by format)
3. **Numbered list of 3–6 calibrated questions** — each with a one-line annotation explaining what the question signals
4. **"What not to ask" sub-section** — 3–5 bullets on questions to avoid for this format/round

**Calibrated-question conventions.**

- **Reference something specific** in the role pack or the conversation so far. Naming a specific executive or a specific time horizon signals preparation.
- **Invite the recruiter or panel to share intel** they often want to share. *"What feedback have you been given on what a 'great' [role] would look like 12 months in — beyond the position description?"* opens a door for them.
- **Address named panellists by name**, and make each question one that person is uniquely placed to answer — *"[Name], where do you see the line between [their remit] and this role's — and where do you expect the two to genuinely overlap?"* A question addressed to the person whose expertise it draws on is the clearest signal that the §5 research was real rather than decorative.
- **Do not build a mechanical round-robin.** Prepare one question per panellist if that helps, but put the warning in "What not to ask": *"Don't ask all four panellists a question each mechanically — pick two or three that genuinely interest you; a forced round-robin reads as scripted."*
- **Continue the honest posture from Section C where it applies.** A question that invites the panellist to name the problem the candidate has just refused to invent — *"is there a specific place where you already know [the people you serve] are being let down by a slow or manual process, that you'd want this role to look at early?"* — is the same discipline, carried into the close.
- **Avoid generic culture questions.** *"What's the culture like?"* is the worst possible question — too generic, signals lack of preparation.
- **Avoid salary at first round.** Salary is a Section D question for the recruiter to raise.

**Format.**

```markdown
## E. Questions to ask [Recruiter / Chair / Panel] *(time permitting — typically [N]–[N] minutes at end)*

> Pick [two or three / three or four]. Don't ask all [N].

1. **"[Question text]"** — [one-line annotation on what this signals].
2. **"[Question text]"** — [annotation].
3. **"[Question text]"** — [annotation].
4. **"[Question text]"** — [annotation].
5. **"[Question text]"** — [annotation].

**What not to ask.**
- [Topic 1 to avoid + brief reason]
- [Topic 2 to avoid + brief reason]
- [Topic 3 to avoid + brief reason]
```

---

## 12. Sources

**Purpose.** Citation list of materials used to assemble the prep. Allows quick verification and re-loading if the prep needs an update.

**Required components.**

1. **Heading** — `## Sources`
2. **Materials used**, each as a Markdown link with `computer://` or `file://` where the file is local:
   - Position advertisement / role pack
   - Candidate information pack
   - **Every artefact already submitted for the role** — cover letter or statement of claims, screening-question responses, any message to the hiring team, each linked to its saved file in `Submissions/`. These are the §X reconciliation set, not optional citations; list them even where none of them was quoted.
   - The resume version used
   - The Writing Voice and Style Guide
   - The Interview Voice and Style Guide
3. **Internal sources first, as a single unheaded block** — the advertisement or role pack, the submitted letter or pitch, the resume version used, **the matrix row cited by ID with its file**, **any watch-out register pointer** relevant to the role, **prior-round prep documents** in the same process, and the **dated direct intel** entries: recruiter and executive-assistant emails with their dates and what each confirmed, calendar-event confirmations of date / time / duration / attendees, and any intel the candidate supplied verbally, dated and summarised.
4. **A separately headed, dated web-research block** — `**Company and panel research (web, [date]).**` — with full URLs as Markdown links, each annotated with what it confirmed (`(official; [Name] confirmed as CEO)`, `(independent corroboration of the doctorate; no field named by any source checked)`). Use more than one dated block where research was done in tranches.
5. **Research caveat paragraph**, where any source conflicted or any obvious fact could not be confirmed — name the conflict, name which source was treated as authoritative and why.
6. **Evidence-bank entries used** — comma-separated list of entry IDs so the prep can be cross-referenced with the bank

**Format.**

```markdown
## Sources

- [Position advert — [Role Title] (Recruiter, ref [Number])](file://[path])
- [Candidate Pack — [Role Title] ([Date])](file://[path])
- [[Candidate Name] — [Document Type] (final, in Submissions)](computer://[path])
- [Resume_Master.md](computer://[Workspace Folder Path]/Resume_Master.md)
- [Writing_Voice_and_Style_Guide.md](computer://[Workspace Folder Path]/Writing_Voice_and_Style_Guide.md)
- [Interview_Voice_and_Style_Guide.md](computer://[Workspace Folder Path]/Interview_Voice_and_Style_Guide.md)
- Matrix row: `[row ID]` (`[bank file]`)
- Watch-out: [register reference] pointer (`[register file]`)
- [Recruiter / EA name] email, [date] — [what it confirmed]
- Calendar event "[event title]" — confirms [duration and attendees]
- Direct intel from [Candidate First Name], [date] — [what they said, summarised]

**Company and panel research (web, [date]).**

- [[Page title] (official; [what it confirmed])]([full URL])
- [[Page title] ([what it corroborated]; [what it did not])]([full URL])

**Research caveat.** [Where sources conflicted, which was treated as authoritative, and why; where an obvious fact could not be confirmed at all.]

- Evidence-bank entries used: [comma-separated IDs]
```

---

## Format-specific variations

The canonical structure above stays the same across all four interview formats. The emphasis shifts — and the research sections shift with it, because a research section that is right for one panel is the wrong one for the next.

### Recruiter screen — variation

- **Sections 3–6 (research)**: company context in full, with the acquisitions, the dated results and a **quick-reference bridges table** — on a 10–15 minute call the bridges are what make the research usable. Section 5 covers the single interviewer plus the confirmed reporting line above them. Sections 4 and 6 usually skipped; say so.
- **Executive summary**: heavy on practicalities (citizenship, clearance, salary anchor) — the recruiter is qualifying against a checklist. **No lens paragraph** (one interviewer), but the **time-budget arithmetic still applies and matters more here than anywhere** — 15 minutes is 5–7 exchanges, so the decisions-and-actions bullets carry what to volunteer unprompted rather than what to wait to be asked. Core-risk mitigations still name the section to deploy.
- **Section A opening**: tight 2 minutes maximum. Recruiters reward concise.
- **Section B**: 15–25 likely questions, weighted to practicalities and capability probes.
- **Section C**: 5–8 STARs. Lead with the questions the recruiter has signalled (in the brief or the call setup).
- **Section D**: full practicalities cheat sheet — **D1 is the live event at this round**. Full market-research apparatus, engagement mechanics where non-standard, anchored script, and the watch-out that the call must not end without a ballpark exchanged.
- **Section E**: 3–5 questions, mostly practical (panel composition, timeline, what makes a great hire).

### Behavioural panel — variation

- **Sections 3–6 (research)**: the deepest treatment of the set. Company context plus the internal technology function's structure and certifications; entities where the group runs several; a full profile per panellist with likely lens, tailored connection point and the alignment note. This is where the "most important fact in this brief" callout usually lands.
- **Executive summary**: heavy on the panel's composition (each member's likely lens named in the "what this round is for" paragraph), the role's headline capabilities, and the 1–2 high-risk behavioural probes. Core risks attributed per panellist, every mitigation pointing at a STAR. Time-budget arithmetic stated.
- **Section A opening**: 2.5 minutes. Panels reward measured.
- **Section B**: 10–20 likely questions, weighted to behavioural STAR probes (6–10 of them).
- **Section C**: 8–12 STARs. Most behavioural questions get a pre-prepared STAR. Attribute each to the panellist it lands hardest with; prohibition lists on every honest-gap and near-miss claim.
- **Section D**: lighter — practicalities mostly cleared at the recruiter screen. **D1 keeps the reflect-first script and drops the market-research table** unless the band or scope has moved since the screen.
- **Section E**: 3–4 questions, calibrated to specific panel members.

### Executive panel — variation

- **Sections 3–6 (research)**: company context reframed around the strategic question the panel is actually deciding; per-panellist profiles weighted to **likely lens** and **tailored connection point** over biography, because the panel is heterogeneous by design (an operations executive, an academic and a functional head listen for three different things); structural-reality analysis wherever the role's scope overlaps an existing executive's remit.
- **Executive summary**: the fullest decision-instrument treatment in the set. Required at this format, all five components: a "what this panel is for" paragraph **naming every lens in the room** and closing on the one-coherent-operating-model instruction; decisions-and-actions carrying the depth-calibration call (*"give [the specialist] the real depth"*), the honest-gap placement directive (*"plant it early and once, not defensively when pressed"*), the do-not-manufacture directive with its honest analogue, and *"close on forward commitment, not gratitude"*; a core-risks table with panellist-attributed risks, mitigations naming the exact STAR, **and the standing cross-artefact row** (§X), since by this round the panel has read everything submitted; the time-budget arithmetic; and the key-people paragraph. Also carries the strategic frame the panel is testing, the 30/60/90 hypothesis, and the 1–2 honest gaps acknowledged earlier in the process.
- **Section A opening**: 2.5 minutes, but with a different beat 3 — *forward commitment* rather than *why-this-role-now*. The panel already knows the candidate wants the job; they want to know what the candidate will do with it.
- **Section B**: 10–15 likely questions, weighted to strategic ("how would you approach") and high-level behavioural with strategic framing.
- **Section C**: 6–10 STARs, with explicit governance / risk / 30-60-90 framing layered onto each. Every STAR heading tagged with its likely asker and lens. Coaching notes carry all four required elements (prohibitions, delivery discipline, don't-invent-with-substitute, ranked rehearsal priority) — an executive panel is where the tempting adjacent claim does most damage, because the person best placed to catch it is in the room.
- **Section D**: minimal — practicalities cleared. **D1 says so explicitly**: salary is unlikely to come up at all, the candidate should not raise it, one reflect-first line plus a single anchoring instruction if genuinely pressed. Note under D2 that the section exists for completeness, not because it is a likely focus.
- **Section E**: 2–3 questions, strategic ("what does success look like at 12 months that the position description doesn't already capture?"). Avoid tactical.

### Fit and working-relationship round — variation

A distinct fourth format, not a soft version of the behavioural panel. It appears late in a process — typically round three, after competence has already been demonstrated — and is usually run by the business stakeholders the role will serve rather than the function it reports into. Getting this one wrong by treating it as another behavioural round is the characteristic failure.

**What it is actually testing** — say this at the top of the document, under the heading *"What this interview actually is — read this first"*:

1. **Can we work together?** — day-to-day operating compatibility, communication style, whether the candidate is easy or hard to deal with under normal working conditions.
2. **Do we like each other?** — genuine personal chemistry. Not performative charm — real rapport, curiosity about their businesses, and warmth that reads as authentic.
3. **Can you do what we specifically need, and do you understand how we operate?** — not "can you do the job in the abstract" but "do you get *our* business, *our* pace, *our* way of making decisions" — for each of the businesses represented in the room.

**Structural variations from the canonical order.**

- **Front-matter** gains a **Sequence** line naming what each prior round was and who ran it, and stating plainly that this round is a different kind of conversation.
- **Section 6 — Structural-reality analysis is mandatory and comes first**, immediately after the "read this first" page. It is the real subject of the interview.
- **Section 5 — Panel research is the body of the document**, expanded per person with two extra blocks: *"What's actually on their plate right now"* (current, dated, specific — a live automation programme, a national digitisation project, an integration timeline) and *"Genuinely relevant, specific things to talk about with them (not scripted — real conversation material)"*.
- **Section A — the opening script is replaced by a topics section.** `## Conversation topics likely to come up`, framed as topics and honest talking points, not scripted answers. Keep the "tell me about yourself" entry shorter and more personal than the behavioural round's version, and say explicitly that the conversation should be allowed to go where they take it.
- **Sections B and C collapse into a short reserve at the back** — `## Reserve — behavioural material, if a specific competency question comes up`, five or six one-line pointers to the full STARs in the prior round's brief. Backup, not the main event.
- **Section D — practicalities stay**, condensed to a single table. D1 takes the executive-panel posture: not a salary conversation, do not raise it.
- **Section E — questions to ask are relationship-building by design**, each one anchored to a specific, current thing about that panellist's business, and annotated as genuine curiosity rather than information-gathering.
- **"What not to ask"** carries the cross-round hygiene rule: nothing that assumes this panel knows what earlier rounds covered, and nothing about intel that belongs to another round.
- **§X still applies** — this round is late in the process, so everything submitted plus every prior-round brief is in scope for the reconciliation, and the topics section must not contradict any of it.

**Register.** Business-first, technical-second, all the way down. Every section is built in that order deliberately. Coach warmth explicitly — *"Let warmth show"*, *"Bring genuine curiosity, not rehearsed answers"* — and give the candidate enough real, current material about each business that their responses can be *free* rather than recited.

**Naming.** `[Candidate Name] - Interview [n] Fit and Working Relationship Brief - [Role Title] - [Organisation].md`, with a paired short speaking-notes file where one is wanted.

---

## Multi-round progression

A pack set **grows across rounds; it is not rewritten.** Each round produces its own brief (and, for panel rounds, its own paired speaking-notes addendum), and each new brief carries forward the research investment while re-cutting its relevance for a different audience.

**What carries forward unchanged.** Section 3 (company context) and Section 4 (entities) are built once and reused verbatim in later rounds. The underlying STAR scripts stay the same — say so explicitly in the later round's timing reality-check: *"unchanged from Round 1, since the underlying scripts are the same."*

**What gets re-cut every round.**

- **The section's own heading gains a relevance clause.** `## [Region] entities — key people and services *(directly relevant this round — two of three panellists run these businesses)*`.
- **The framing paragraph is rewritten for the new audience.** *"This section was originally built for Round 1's technical panel; it matters even more here, because [Name] and [Name] are the actual leaders of two of these six."*
- **The "reading this as a set" synthesis is re-argued** against the new panel: the same six entities, re-read as "three people who each own a piece of it directly".
- **Sections that were the focus become context.** *"**For this round, [the shared-services function] is context, not the focus** — this panel is the business side of the house that it serves, not the function itself."*
- **The lead-with / hold-in-reserve assignment flips.** Round 1 led with the architecture and cyber STARs; Round 2 marks the same STARs *"(hold in reserve — use if asked directly)"* and promotes the business-partnership ones. The STAR headings themselves carry the instruction, and the speaking-notes addendum repeats it as a one-line **Quick anchor**.

**What must be added every round.**

- A **Round context** line in the front-matter naming the prior rounds, who ran them, and how this round differs in kind.
- A **do-not-assume-continuity** directive: *"Don't assume this panel knows what was discussed in Round 1 … reintroduce your positioning cleanly rather than assuming continuity."*
- A **cross-round confidentiality boundary** where any round produced sensitive intel, stated as a directive in the executive summary and repeated as a **Remember:** line in the addendum, with the clean generic answer pre-scripted for "what did you discuss last round?"
- A **don't-recite-it-back** instruction where a panellist attended an earlier round: extend each reused STAR with one additional layer of mechanism or a second data point, and say in the brief that those STARs are written as the extended versions, not verbatim repeats.

**Paired brief + addendum convention, across rounds.** Every panel round produces two files, named for the round: `… - Panel Interview Brief - [Round n descriptor] - [Role] - [Organisation].md` and `… - Speaking Notes Addendum - [Round n descriptor] - [Role] - [Organisation].md`. The brief is what the candidate studies; the addendum is what they use on the day. Keep prior rounds' files in place — where a later document supersedes an earlier one, say so in the later document's Sources (*"earlier draft of this interview, superseded by this document"*) rather than deleting the earlier file.

---

## PDF output for annotated prep documents

If the candidate annotates prep documents on an e-ink tablet (or simply prefers a printed PDF), produce a **PDF alongside the Markdown** using `pandoc --pdf-engine=xelatex`. Three reusable disciplines make the output read well:

1. **Paired Markdown + PDF.** Keep the `.md` as the editable source and convert to `.pdf` in the same session. Both live in the `Interview Prep/` folder. Carry the page geometry (A4 portrait, a wide right margin for handwritten notes, a serif body / sans headings, a running header) in the Markdown YAML front-matter so the conversion is reproducible. The canonical YAML block, and the full set of annotation-PDF rules, live in `skills/prep-gate/references/annotation-pdf-rules.md` — copy the block from there into each new prep doc rather than re-deriving it.

2. **Proportional pipe-table separator dashes.** Pandoc sizes table columns by the relative number of dashes in the separator row, **not** by content. Equal separators (`|---|---|`) force every column to the same width — a narrow index column ends up as wide as a prose column. Vary the dash counts to match each column's content (narrow columns ~2–6 dashes, prose columns 30–60), and use a leading colon (`:---`) for left-alignment. Example for a five-column likely-questions table:

   ```
   |:--|:-------------------------|:--------------------------------------------|:----------------|:--------|
   ```

3. **Landscape rotation for wide tables.** When a table is too wide to read in portrait, rotate **only that section** to landscape while the rest of the document stays portrait. Add `\usepackage{pdflscape}` to the YAML `header-includes`, then wrap the section in **raw-LaTeX blocks** — not a bare `\begin{landscape}` / `\end{landscape}` pair. A bare pair makes pandoc treat the heading and the markdown table between them as one raw-LaTeX span, so the table is passed through verbatim and a literal `#` in a `| # |` header column breaks the xelatex build (*"macro parameter character # in vertical mode"*). Emitting each command as its own raw block keeps the markdown table parseable:

   ````
   ```{=latex}
   \begin{landscape}
   ```

   ## B. Likely questions — positioning notes

   | # | Likely question | Lead with | Evidence anchor | Time |
   |:--|:-------------------------|:--------------------------------------------|:----------------|:--------|
   | … rows … |

   ```{=latex}
   \end{landscape}
   ```
   ````

   Apply discipline 2 (proportional dashes) inside the rotated table so the freed landscape width goes to the prose columns, not the index column.

---

## Maintenance and reuse

- **Save every prep document** to `[Workspace Folder Path]/Interview Prep/` so future preps can reference the pattern.
- **After each interview**, capture in the changelog: which STARs landed, which got cut for time, which questions were asked that weren't anticipated, which were anticipated but weren't asked. Use this to calibrate future preps.
- **Reusable STARs** — if a STAR worked well in one interview (the panel responded well, the candidate landed it confidently), tag it as reusable in the evidence-bank changelog. Future preps for similar archetypes can lift it with light tailoring.
- **Question-library accumulation** — over time, the most common interview questions accumulate. Section B can lift from prior preps for similar role families rather than being rebuilt from scratch.

---

*Skeleton written for the Executive Application Helper template package. Codifies the canonical twelve-section structure for STAR-style interview prep documents — the research half (§R disciplines, §3 company context, §4 operating entities, §5 panel and individual research, §6 structural-reality analysis), the panel-room half (§2 executive summary as a decision instrument, §X cross-artefact consistency, per-panellist attribution with its caveat, the four required coaching-note elements, depth calibration, the honest-gap spoken doctrine, round-dependent salary coaching), the four interview formats, and the multi-round progression conventions. Loads alongside `Interview_Voice_and_Style_Guide.md`; verified by `prep-gate` Checks 5 and 6. Last updated: [Setup date].*
