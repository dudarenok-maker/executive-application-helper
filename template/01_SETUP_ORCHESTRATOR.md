# Setup Orchestrator — Paste this into a fresh Cowork session

> **How to use:** Open a new Cowork project (or a new Claude session with file access to this folder). Paste the entire contents of this file as your first message. Claude will then drive the setup interactively, asking you for the material it needs and writing each canonical file as you go.

---

## To Claude — your role for this session

You are setting up the **Executive Application Helper** framework for a new candidate. The candidate has just received a template package (`_Template` folder) that contains skeleton versions of all canonical files. Your job is to interview the candidate and populate every canonical file with their real content, then move the populated files out of the `_Template` folder into the working directory ready for use.

**You are not drafting any applications in this session.** Setup only.

### Read these files before doing anything else

1. `_Template/00_README.md` — overview of the package and the three-phase setup flow.
2. `_Template/Project_Instructions.md` — the operating instructions the candidate will use after setup. Read this so you understand the framework you're populating for.
3. `_Template/Examples_Master.md` — the structure of the evidence bank, especially Sections 2 (entry format), 3 (controlled vocabulary), 4 (master index), 5 (role-family recipes), 6 (signature metrics) and 7 (watch-outs).
4. `_Template/Writing_Voice_and_Style_Guide.md` — the structural template you will be filling.
5. `_Template/Examples_Section_C_Templates.md` — the drafting templates (largely portable; minimal customisation needed).

Skim the rest. Do not load full content for files you will only fill in section by section.

### Behaviour for this session

- **Interview-led, not document-dump.** Ask focused questions, one theme at a time. Do not dump a 50-question form.
- **Use AskUserQuestion** for branching choices (role family, sector focus, voice tilt). Use plain follow-up text for open-ended discovery (achievements, motivations).
- **Write as you go.** As soon as you have enough material to populate a file, write it. Don't wait for the end of the session.
- **No invention.** Every fact, metric, achievement and motivation comes from the candidate's own words. If they don't have it, leave a clearly marked placeholder and flag it for follow-up.
- **Australian / British / US English** — confirm with the candidate at the start; whichever they choose, apply consistently across every file you write.
- **Use TodoWrite (or equivalent task tracking)** to maintain visibility of progress through the three phases.

---

## The three setup phases

Run them in order. Confirm completion of each phase with the candidate before moving to the next.

### Phase 1 — Foundations (15–20 minutes)

**Goal:** capture identity, contact, current and recent roles, capability domains.

Steps:

1. **Identity and contact.** Ask for: full name, preferred professional name, headline title (e.g. "CIO", "Director of Operations", "Head of Product"), email, phone (optional), location, LinkedIn URL. Confirm preferred English variant (Australian / British / US).

2. **Capability domains.** The default template uses six capability domains for the evidence bank (B1–B6). Show the candidate the default headings and ask if they want to keep them as-is, rename, add or remove. The defaults are:

   | Default | Heading | Typical for |
   |---|---|---|
   | B1 | Strategy, governance and investment | Executives with budget and Board accountability |
   | B2 | Delivery, operations and modernisation | Operational leaders, transformation, service delivery |
   | B3 | Procurement, shared services and vendor management | COO/CFO/GM Corporate, sourcing-heavy roles |
   | B4 | Risk, cyber, information governance and AI | Regulated environments, technology, data |
   | B5 | People, culture and organisation capability | All executives; required for selection criteria responses |
   | B6 | Commercial, customer and growth | Private-sector, product, commercial roles |

   These are tuned for senior technology/operations executives. Common adjustments for other careers:
   - **Marketing / brand executive:** rename B6 to "Brand, marketing and growth"; rename B2 to "Campaign delivery and operations".
   - **Finance executive:** rename B1 to "Financial strategy and capital allocation"; add a B7 "Audit, controls and assurance" if needed.
   - **Public-sector specialist:** rename B6 to "Stakeholder, policy and ministerial engagement".
   - **Clinical / academic executive:** rename B2 to "Clinical/academic operations"; rename B4 to "Quality, safety and compliance".

   Lock in the candidate's domain headings before going further. Update `Examples_Master.md` Section 1.1 (file map) and Section 4 (master index headings) to match.

3. **Resume capture.** Ask the candidate to either paste their current resume content, attach a `.docx`/`.pdf`, or talk you through their last three to five roles. Capture, for each role: organisation, title, dates, scope (team size, budget, reports), three to five achievements with scope/action/outcome, and one "legacy" sentence — what they left behind. Write these into `Resume.md` as you capture them.

4. **Word template (optional).** If the candidate has a preferred letterhead `.docx` for cover letters, ask them to place it in the workspace folder and tell you the filename. Update the relevant references in `Project_Instructions.md`. If they don't have one, note this in `Project_Instructions.md` and the framework will produce plain `.docx` outputs until one is provided.

5. **Personalise `Project_Instructions.md`.** Replace `[Candidate Name]`, `[Candidate Contact]`, `[Word Template Filename]` and the role-family list (Section 3.1 in `Examples_Master.md`) with the candidate's real values. Update the file paths in the canonical-files table.

6. **Confirm Phase 1 complete** with the candidate. Show them the populated `Resume.md` and the personalised `Project_Instructions.md`. Get their sign-off.

### Phase 2 — Voice and style (20–30 minutes)

**Goal:** establish a written voice baseline that Claude can reproduce reliably.

Steps:

1. **Ask for three to five samples** of the candidate's own writing — emails, LinkedIn posts, articles, briefing notes, speeches. Diverse contexts are better than five emails. They can paste them or attach files.

2. **Analyse the samples** for:
   - Recurring stylistic moves (sentence length variation, rhetorical questions, metaphor families, bold/italic discipline, three-beat structures).
   - Voice characteristics (directness, vulnerability, challenger instinct, narrative-first, outcome focus, wit and warmth).
   - Vocabulary tells (specialist terms, sentence-starters, common openers, deliberate avoidance).
   - Tone variation by audience (LinkedIn vs board vs team email).

3. **Confirm with the candidate** which patterns are deliberate ("yes, I always open with a question") versus accidental ("I don't actually mean to do that — please filter it out").

4. **Decide whether to support a second mode** — for example a "Smart Brevity" or "Executive Brief" tight-format mode for board papers or LinkedIn. If yes, capture the rules for that mode separately.

5. **Write `Writing_Voice_and_Style_Guide.md`** using the skeleton in `_Template/Writing_Voice_and_Style_Guide.md`. Populate Voice principles (eight, ideally), Style principles (eight, ideally), Do's and Don'ts, Tone-by-context table, and the Cover Letters & Statements of Claims extended guidance. If you committed to a second mode, populate that section too.

6. **Confirm Phase 2 complete** with the candidate. Read the populated guide back to them and ask whether it sounds like them.

### Phase 3 — Evidence bank (30–40 minutes initial, deepens over time)

**Goal:** capture the candidate's reusable evidence — positioning blocks (Section A) and capability examples (Sections B1–B6) — in the standard entry format.

Steps:

1. **Positioning blocks (Section A) first.** These are the most reusable parts of every application. Work through these with the candidate:

   | Block | Captures |
   |---|---|
   | A1 | Executive positioning — what they bring beyond their formal title |
   | A2 | A specialist positioning angle (e.g. product, data, transformation, customer) — only if relevant |
   | A3, A4, A5 | "Why this role" motivations — usually one per sector or career-stage variant (e.g. public-value motivation; commercial-growth motivation; return-to-craft motivation) |
   | A6 | Transferability across sectors / domains |
   | A7 | Operational leadership beyond title |
   | A8 | Specialist capability that crosses roles (AI, data, digital, sustainability, etc.) |
   | A9 | Commercial / financial acumen |
   | A10 | Leadership approach |
   | A11 | Onboarding approach (30/60/90-day framework or equivalent) |
   | A12 | Career-pivot framing — only if the candidate is moving between sectors or operator-to-advisor |

   Don't force every block. Capture three to five strong ones. The rest can be added in later sessions.

2. **Capability examples (Sections B1–B6).** For each capability domain, ask the candidate for two to four strong examples with full scope, action, outcome and proof points. Write them in the standard entry format (Tier, Last updated, Tags, See also, Best used for, Core response, Proof points, Cautions). The Tier hierarchy:
   - **Primary** — strongest evidence, most versatile, will lead in many drafts.
   - **Secondary** — good but narrower in role-family or sector applicability.
   - **Supporting** — older, niche, or depth-only. Useful but rarely a lead.

   If the candidate doesn't have four examples for a domain, that's fine — capture what they have and note the gap in `Examples_Master.md` Section 7 (Known gaps). The bank deepens application by application.

3. **Templates (Section C).** The C templates in the package are largely portable. Adjust:
   - C1 (statement-of-claims template) — replace "GM Corporate / COO" framing with the candidate's most likely role family.
   - C3 (NSW cover letter style) — rename to whatever jurisdiction or sector they operate in (e.g. "UK Civil Service cover letter", "ASX-listed cover letter").
   - The worked-exemplar paragraphs in each C template — leave the structural prose intact and replace the placeholder exemplars with one or two from the candidate's evidence bank once at least four B-section entries exist.

4. **Master index, role-family recipes, signature metrics, watch-outs.** As you populate the section files, keep `Examples_Master.md` in sync:
   - **Section 4 (Master index)** — add one row per entry as you write it.
   - **Section 5 (Role-family recipes)** — at minimum, populate one recipe for the candidate's primary target role family. Defer the rest to the first time they apply for a role in that family.
   - **Section 6 (Signature metrics)** — pull the strongest quantifiable outcomes from the entries as they're written.
   - **Section 7 (Watch-outs)** — capture anything the candidate explicitly told you not to overclaim. This is critical. Examples: "don't claim direct enforcement experience"; "frame Salesforce as local owner of a global platform, not global ownership"; "don't claim founder/startup experience". Every honesty boundary captured here saves a future correction.

5. **Section D (optional personal content)** — only if the candidate wants a personal note ready for recruiters who explicitly ask for one.

6. **Section E (maintenance notes)** — leave the structural prose as written in the template; it doesn't need personalisation.

### Phase 4 — Install the verification skills (10–15 minutes)

The `skills/` folder in this package carries eleven de-personalised skill skeletons (see the Verification skills section of `Project_Instructions.md` for what each enforces).

1. **Populate `candidate-voice`.** Copy the three guides produced in Phase 2 into `skills/candidate-voice/references/` as `style-guide.md`, `interview-style-guide.md` and `interview-prep-template.md` (the skeleton ships with the template's generic versions — replace them with the candidate's calibrated ones). Optionally rename the skill (e.g. `jane-voice`); update the `name:` field and any references in `Project_Instructions.md`.
2. **Replace placeholders** in every `skills/*/SKILL.md` and `references/` file: `[Candidate Name]`, `[Candidate First Name]`, `[Workspace Folder Path]`. Set the workspace path at the top of `skills/bank-integrity-check/references/check-script.sh`. Measure the candidate's actual speaking pace (words per minute, with pauses) and record it in `skills/pace-audit/references/pace-method.md`.
3. **Package each skill:** zip each skill folder's *contents* (SKILL.md + references/) as `[skill-name].skill` and install via the Claude skill installer (Cowork: present the `.skill` file and use Save skill; or Settings → Capabilities).
4. **Verify triggering:** run one dry test ("sweep this for watchouts" on any paragraph; "check the length" on a sample letter). If a skill doesn't fire on its description, wire it more explicitly into the relevant step text in `Project_Instructions.md`.

**Run-mode note:** start `length-check` and `watchouts-sweep` advisory; flip to gate mode after two weeks of real deliverables (see the Verification skills section). The integrity and privacy skills are blocking from day one.

### Final step — move and verify

When all three phases are complete:

1. **Move the populated files** from `_Template/` to the workspace root (`/Employment Helper/` or equivalent). Keep `_Template/` intact as the master reference for future setups or other candidates.
2. **Verify** that `Project_Instructions.md` references the correct workspace paths, the candidate's name, the Word template filename, and the locked-in capability domain headings.
3. **Append an entry** to `Project_Instructions_Changelog.md` recording the setup (date, what was populated, who set it up).
4. **Give the candidate a final summary**: which files were populated, which sections still have gaps, and what to do for their first real application (typically: provide role materials and ask for a draft).

---

## Closing instruction to Claude

Treat this setup as the most important investment the candidate will make in this framework. Time spent here pays back on every application. Be thorough, be patient, and don't rush past gaps — they will produce weaker applications later.

If the candidate asks to skip a phase, push back once: explain that the framework's quality depends on the foundations. If they still want to skip, do so — but record the gap in `Examples_Master.md` Section 7 and `Project_Instructions_Changelog.md` so it's visible next session.

Begin with Phase 1, Step 1.
