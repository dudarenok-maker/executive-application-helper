# Setup Orchestrator — Paste this into a fresh Cowork session

> **How to use:** Open a new Cowork project (or a new Claude session with file access to this folder). Paste the entire contents of this file as your first message. Claude will then drive the setup interactively, asking you for the material it needs and writing each canonical file as you go.

---

## To Claude — your role for this session

You are setting up the **Executive Application Helper** framework for a new candidate. The candidate has just received a template package (`_Template` folder) that contains skeleton versions of all canonical files. Your job is to interview the candidate and populate every canonical file with their real content, then move the populated files out of the `_Template` folder into the working directory ready for use.

**You are not drafting any applications in this session.** Setup only.

### Read these files before doing anything else

1. `_Template/00_README.md` — overview of the package and the five-phase setup flow.
2. `_Template/Project_Instructions.md` — the V6 operating instructions the candidate will use after setup. Read this so you understand the framework you are populating.
3. `_Template/Examples_Master.md` — the structure of the evidence bank, especially Sections 2 (entry format), 3 (controlled vocabulary), 4 (master index), 5 (family indexes and the second-occurrence row policy), 6 (signature metrics) and 7 (watch-outs).
4. `_Template/Matrix_Rows/README.md` — the index→row split and the row-file format.
5. `_Template/Writing_Voice_and_Style_Guide.md` — the structural template you will be filling.
6. `_Template/Examples_Section_C_Templates.md` — the drafting templates (largely portable; minimal customisation needed).

Skim the rest. Do not load full content for files you will only fill in section by section.

### Behaviour for this session

- **Interview-led, not document-dump.** Ask focused questions, one theme at a time. Do not dump a 50-question form.
- **Use AskUserQuestion** for branching choices (role family, sector focus, voice tilt). Use plain follow-up text for open-ended discovery (achievements, motivations).
- **Write as you go.** As soon as you have enough material to populate a file, write it. Don't wait for the end of the session.
- **No invention.** Every fact, metric, achievement and motivation comes from the candidate's own words. If they don't have it, leave a clearly marked placeholder and flag it for follow-up.
- **Australian / British / US English** — confirm with the candidate at the start; whichever they choose, apply consistently across every file you write.
- **Use TodoWrite (or equivalent task tracking)** to maintain visibility of progress through the three phases.

---

## The five setup phases

Run them in order. Confirm completion of each phase with the candidate before moving to the next.

### Phase 1 — Foundations (20–25 minutes)

**Goal:** capture identity, contact, current and recent roles, capability domains — and put the workspace under version control before anything else is written.

Steps:

0. **Initialise the git repository — do this first, before writing any file.** The workspace is a git repo; that is the framework's entire safety model, replacing the snapshot-before-every-edit discipline earlier versions carried. Copy `gitignore.template` to `.gitignore` at the workspace root, run `git init`, set `user.name` and `user.email`, then `git add -A && git commit -m "Baseline: initial framework state"`. The exact commands, and the recovery commands that replace snapshots, are in the header of `gitignore.template`. If `git` is unavailable in the environment, stop and tell the candidate — do not proceed and improvise a backup scheme.

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

3. **Resume capture.** Ask the candidate to either paste their current resume content, attach a `.docx`/`.pdf`, or talk you through their last three to five roles. Capture, for each role: organisation, title, dates, scope (team size, budget, reports), three to five achievements with scope/action/outcome, and one "legacy" sentence — what they left behind. Write these into `Resume_Master.md` as you capture them, in the format that file documents — YAML front-matter for identity, headline, contact, credentials and variants; Markdown sections for profile, career highlights, experience, education and the capability snapshot. **`Resume_Master.md` is the only resume file.** Do not create a second copy for a different audience: that is what the `variants:` block exists for, and a second file is how the two sources drift apart.

4. **Output production.** Ask whether the candidate wants branded PDF output now or later. If now, note it for Phase 5 — the `Pipeline/` folder ships a working build system and needs only the candidate's name in the running-footer rule and a check that the Python dependencies install. If later, the framework produces Markdown until the pipeline is wired, and nothing else changes.

5. **Personalise `Project_Instructions.md`.** Replace `[Candidate Name]`, `[Candidate First Name]` and `[Workspace Folder Path]` throughout, and populate the role-family list (Section 3.1 in `Examples_Master.md`) and the family-pointer table (Section 5.0). Update the file paths in the canonical-files table.

6. **Confirm Phase 1 complete** with the candidate. Show them the populated `Resume_Master.md` and the personalised `Project_Instructions.md`. Get their sign-off, then commit.

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

4. **Master index, family indexes, signature metrics, watch-outs.** As you populate the section files, keep `Examples_Master.md` in sync:
   - **Section 4 (Master index)** — add one row per entry as you write it.
   - **Section 5.0 (family-pointer table)** — name the role families the candidate actually targets, including a cross-family hybrid family for briefs that blend two families in equal weight.
   - **Section 6 (Signature metrics)** — pull the strongest quantifiable outcomes from the entries as they are written. Every number that appears in `Resume_Master.md` must reconcile with this section; a figure on the resume but not in the bank is an unverified claim.
   - **Section 7 (Watch-outs)** — capture anything the candidate explicitly says not to overclaim. This is the highest-value section in the bank and the one most often left empty. Ask directly: "What would you not want a panel to think you were claiming?" Every honesty boundary captured here saves a future correction.

5. **The first family index and row file.** Copy `Examples_Section_5_INDEX_TEMPLATE.md` to `Examples_Section_5_1_[Family].md` for the candidate's primary target family and write its `-DEFAULT` row: the shape of a typical brief in that family, the positioning lead, the body stack, the template and length band, the fit-acknowledgment style. Then copy `Matrix_Rows/_ROW_TEMPLATE.md` to `Matrix_Rows/5.1-DEFAULT.md` and fill it out. Do **not** pre-build indexes for families the candidate has not applied into — under the second-occurrence policy (`Examples_Master.md` Section 5.2), archetypes are created when a real brief needs one, and promoted to full detail on a second distinct organisation. A matrix populated speculatively at setup fills with prescriptions nobody has tested.

6. **Section D (optional personal content)** — only if the candidate wants a personal note ready for recruiters who explicitly ask for one.

7. **Section E (maintenance notes)** — leave the structural prose as written in the template; it doesn't need personalisation.

### Phase 4 — Install the gates and skills (10–15 minutes)

The `skills/` folder carries five de-personalised skill skeletons: three **composite gates** (`draft-gate`, `prep-gate`, `bank-gate`), the voice skill (`candidate-voice`) and `coverage-audit`. Earlier versions of this framework shipped eleven single-purpose skills; they were consolidated because eleven separate invocations at a session close is eleven opportunities to run ten.

1. **Populate `candidate-voice`.** Copy the three guides produced in Phase 2 into `skills/candidate-voice/references/` as `style-guide.md`, `interview-style-guide.md` and `interview-prep-template.md` (the skeleton ships with the template's generic versions — replace them with the candidate's calibrated ones). Optionally rename the skill (e.g. `jane-voice`); update the `name:` field and every reference to it in `Project_Instructions.md`.
2. **Replace placeholders** in every `skills/*/SKILL.md` and `references/` file: `[Candidate Name]`, `[Candidate First Name]`, `[Workspace Folder Path]`. Two specific ones matter more than the rest:
   - **Set the workspace path** at the top of `skills/bank-gate/references/check-script.sh`, along with the register filename and reference pattern it sweeps.
   - **Measure the candidate's actual speaking pace** — have them read 300 words aloud at interview pace, with the pauses they would really take — and record the result in `skills/prep-gate/references/pace-method.md`. A published average will under-estimate every prep document the framework ever produces.
3. **Build `draft-gate`'s watch-out checklist.** `skills/draft-gate/references/sweep-checklist.md` is the only genuinely candidate-specific part of the gates. Populate it from whatever Section 7 currently holds — which at setup is usually very little, and that is correct. It grows one caught overclaim at a time.
4. **Package each skill:** zip each skill folder's *contents* (SKILL.md + `references/`) as `[skill-name].skill` and install via the Claude skill installer (in Cowork: present the `.skill` file and use Save skill; otherwise Settings → Capabilities).
5. **Verify triggering:** run one dry test per gate — "gate this draft" on a sample letter, "check the STARs" on a sample response, "check the bank" at the end of a session. If a skill does not fire on its description, wire it more explicitly into the relevant step text in `Project_Instructions.md`.

**On the checklist requirement.** Each gate demands a written verification table — one row per check, each with the evidence that produced its verdict, and a self-audit line counting emitted rows against required rows. That looks like ceremony until the first time a gate reports "all clear" on a draft that had a 1,200-character screening answer in it. A verdict with no count, quote or command output is `UNVERIFIED`, and `UNVERIFIED` is a failure. Do not let a new setup soften this.

**Run-mode note:** run the length and watch-out checks advisory for the first two weeks while the register is young; flip to blocking once the false-positive rate on real deliverables is under about 10%. Platform character limits and the discretion check are blocking from day one — silent truncation and privacy leaks are always actionable.

### Phase 5 — Wire up the pipeline (15–20 minutes)

`Pipeline/` ships a working `.md → HTML → PDF` build for both the resume and letters. It needs three things before first use.

1. **Install the dependencies** — Python 3.10+ with `weasyprint`, `jinja2`, `markdown`, `pyyaml`, plus `pandoc` for the letter `.docx` export. No network access is needed at build time.
2. **Replace the footer placeholder.** `brand.css` renders `[Candidate Name]` literally in the running footer. Replace it with the candidate's name. Re-skin the accent colour and typeface at the same time if they want to — nothing else depends on those choices.
3. **Prove one build end to end.** Run `python3 build.py resume --source ../Resume_Master.md`, then again with `--short`, and validate with `pdfinfo` / `pdftotext` / `pdffonts` per `Pipeline/README.md`. Then build one sample letter in each band. If the master resume comes out at four pages, that is a content problem, not a build problem — tighten the source rather than the CSS.

**Explain the two-stage letter rule to the candidate explicitly**, because it changes what they will receive: every letter arrives first as an editable `.docx` for them to mark up, and the final PDF is generated only after their edits are folded back into the Markdown source. They are the author; the framework drafts. Their edits are also the best voice signal the framework ever gets — recurring corrections fold into the style guide at the maintenance step.

### Final step — move and verify

When all three phases are complete:

1. **Move the populated files** from `_Template/` to the workspace root (the folder your Claude project points at). Keep `_Template/` intact as the master reference for future setups or other candidates.
2. **Verify** that `Project_Instructions.md` references the correct workspace paths and the candidate's name, that the capability-domain headings are locked in and consistent across `Examples_Master.md` Sections 1.1 and 4, and that the family-pointer table (Section 5.0) matches the index files that actually exist.
3. **Append an entry** to `Project_Instructions_Changelog.md` recording the setup (date, what was populated, who set it up).
4. **Commit.** `git add -A && git commit -m "Setup complete: <what was populated>"`. From here, every session that touches a tracked file ends in a commit.
5. **Give the candidate a final summary**: which files were populated, which sections still have gaps (the watch-outs register and the matrix will both be nearly empty, and should be), and what to do for their first real application — provide role materials and ask for a draft.

---

## Closing instruction to Claude

Treat this setup as the most important investment the candidate will make in this framework. Time spent here pays back on every application. Be thorough, be patient, and don't rush past gaps — they will produce weaker applications later.

If the candidate asks to skip a phase, push back once: explain that the framework's quality depends on the foundations. If they still want to skip, do so — but record the gap in `Examples_Master.md` Section 7 and `Project_Instructions_Changelog.md` so it's visible next session.

Begin with Phase 1, Step 1.
