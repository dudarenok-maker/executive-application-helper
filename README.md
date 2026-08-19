# Executive Application Helper

A complete, battle-tested framework for running senior-executive job applications and interview preparation as a Claude project — with an evidence bank, index→row retrieval, composite verification gates that check mechanically rather than by assurance, a real document-production pipeline, and an integrity model earned the hard way.

Built and iterated across months of real executive applications (CIO / CTO / COO / CDO / SES and equivalent roles). Every rule in this framework exists because something went wrong without it.

**Current version: v0.6.5.** See `template/Template_Changelog.md` for what changed and what was retired.

## What this is — and what it deliberately is not

**This is not an AI application generator. It will never apply for you, and it is not designed to.**

The point of this framework is not to mass-produce applications at the push of a button — that path produces generic, AI-slop submissions that say nothing true about you and that any experienced panel can spot in seconds. This framework is the opposite of that. Its job is to help you **build a rigorous, structured bank of your own real evidence** — your actual proof points, metrics, scope, and outcomes — and then assemble the strongest possible application *from your own material*, tailored to a specific role.

Three principles are non-negotiable and built into how it works:

1. **Your evidence, not invented evidence.** Nothing goes into a draft that your evidence bank can't support. The framework cannot — and must not — fabricate achievements, inflate scope, or claim outcomes that weren't yours. The watch-outs register exists specifically to catch overclaim before it reaches a page.
2. **You review every word.** There is a clear and intentional expectation that **you read the final document end to end** before it goes anywhere — checking that it is consistent, accurate, and truthful, and that it genuinely sounds like you. The framework drafts and verifies; **you are the author and the accountable signatory.** It is a co-pilot, never an autopilot.
3. **The real value is the loop, not the document.** When you review a draft and find something off — a weak framing, a stale metric, a claim that doesn't quite hold — you don't just fix the document. **You fix the evidence bank.** That correction makes the next application better, and the one after that. The compounding asset is the bank: a sharper, truer, better-organised account of your career that improves every time you use it. Document production is the by-product; **continuous iteration on your evidence is the product.**

If you want a button that fires off applications without your judgement in the loop, this is the wrong tool. If you want to get systematically better at representing your real, hard-won experience — application after application — this is built for exactly that.

## What it does

**Two workflows, one evidence base:**

- **Application drafting** — drop a job URL or attachment into a Claude project and get a tailored cover letter, statement of claims, pitch, or selection-criteria response in the candidate's own voice, built from a structured evidence bank, gated by length and overclaim checks before delivery.
- **Interview preparation** — recruiter screens, behavioural panels, and executive panels: twelve-section prep documents — company and panel research with an explicit confidence ladder, structural-reality analysis, STAR responses written for spoken delivery, honest timing audits at the candidate's real speaking pace, capability mapping for framework-scored panels, and a reconciliation of every spoken answer against everything already submitted for the role.

**The machinery underneath:**

- **Evidence bank** — a structured, tagged library of proof points, positioning blocks and ready-made templates, with a master index and per-role-family decision matrices that prescribe exactly which evidence stack fits which role archetype.
- **Index→row retrieval** — each role family is a slim index file (one line per archetype); the full prescription for a matched archetype lives in its own `Matrix_Rows/<ID>.md`. A session loads the one row it matched, not the whole family. In the live framework this cut matrix selection load from ~338 KB to ~22 KB and typical session reference load by around 56%.
- **Second-occurrence row policy** — a new pattern gets a slim one-shot row; it is promoted to full detail only when a second distinct organisation matches the same archetype. One application is an anecdote; two are a pattern worth the cost of a full row.
- **Three composite gates** (`template/skills/`) — `draft-gate` (length bands, overclaim sweep, matrix-row traceability, selection-criteria structure), `prep-gate` (STAR construction, honest pace at the candidate's measured speaking rate, capability mapping, annotation-PDF conventions, research depth and sourcing, panel-room calibration and record consistency), `bank-gate` (git commit discipline, mount-cache coherence, cross-reference resolution, personal-context boundaries). They replaced eleven single-purpose skills, because eleven invocations at a session close is eleven opportunities to run ten.
- **Checklists with teeth** — each gate must emit a verification table with a fixed required row count, one row per item, and the evidence that produced every verdict. A verdict with no count, quote or command output is `UNVERIFIED`, and `UNVERIFIED` counts as a failure. There is no "all pass" shortcut.
- **Selection criteria answered as an instrument, not an essay** — a criteria response mirrors the advertisement's own scoring form: every criterion gets its own heading, quoted verbatim, under the ad's own categories; one evidence-dense paragraph each; hard-gate criteria (a degree or licence not held) answered head-on rather than dodged. A criterion a panel cannot find scores zero, not "partially met", so a missing or paraphrased heading blocks delivery.
- **Research disciplines with an explicit confidence ladder** — everything a prep pack asserts about the employer or about a named interviewer carries its epistemic status in words, in the sentence that makes the claim: first-party confirmed, independently corroborated, secondary only, not confirmed. Inference lives in its own labelled paragraph and never shares one with fact. An unsourced claim about a named person blocks; so does intel from one interview round leaking into another.
- **Panel-room calibration and cross-artefact consistency** — the executive summary is a decision instrument, not a summary: every mitigation names the exact section or STAR to deploy, the time budget is arithmetic rather than a feeling, and honest-gap answers carry an explicit list of what must *not* be claimed, each prohibition paired with the substitute line to say instead. Before delivery, every spoken answer is reconciled against everything already submitted for that role — contradicting your own application in front of a panel that has read it is the one failure no follow-up answer repairs.
- **A mandatory voice audit** before the draft gate, covering opener rotation, em-dash discipline (capped *and* not zero), word-echo, sentence rhythm and the tells that make a document read as machine-made. The gate blocks if it hasn't run.
- **Document pipeline** — a working `.md → HTML → PDF` build for the resume and letters under one design system. One `Resume_Master.md` with named variants in front-matter and a 2-page mode; letters delivered as an **editable review `.docx` first**, with the final PDF produced only after the candidate's edits are folded back into the source.
- **Git as the integrity model** — the workspace is a repository; a commit at every session close makes every state recoverable. This replaced a snapshot-before-every-edit discipline, a three-axis file-integrity check and a weekly changelog-splitting scheme. Two rules survived because they *prevent* damage rather than recover from it: rebuild long files whole rather than editing in place, and — on mounted or synced workspaces — read with the file tool, write from the shell, and cross-check before any rewrite.

## Quick start

1. **Clone or download** this repository.
2. **Copy the `template/` folder** into a fresh folder on your machine — this becomes your workspace.
3. **Open a Cowork session** (Claude desktop) pointed at that folder and paste the contents of `template/01_SETUP_ORCHESTRATOR.md` into the chat. Claude walks you through five setup phases: foundations (including `git init` — step zero, before anything is written), voice and style, evidence bank, gates and skills, and the document pipeline.
4. **Paste the populated `template/Project_Instructions.md`** into your Claude project's instructions field.
5. Drop a job ad URL into the project. The default action is a tailored cover letter, drawn from your evidence bank.
6. **Read it end to end.** Check it's accurate, consistent, and sounds like you. You'll get it as an editable `.docx` precisely so that you will edit it. Push every correction back into the evidence bank and the voice guide so the next application starts stronger. This review step is not optional; it is the framework working as intended.

## Repository layout

| Path | What it is |
|---|---|
| `template/` | The de-personalised framework: V6 project instructions, setup orchestrator, evidence-bank skeletons, voice guides, single-source resume, changelog scaffolds |
| `template/Matrix_Rows/` | Row-file format spec, the second-occurrence policy, and a copy-me row skeleton |
| `template/Pipeline/` | Working build system — `build.py`, `brand.css`, Jinja2 HTML templates, README |
| `template/skills/` | Five skill skeletons: three composite gates plus the voice and coverage skills. Populate, package as `.skill`, install per Setup Phase 4 |
| `template/gitignore.template` | Starter `.gitignore` with the git setup and recovery commands |
| `template/Template_Changelog.md` | Version history of the framework package (current: v0.6.5) |
| `LICENSE` | MIT |
| `CONTRIBUTING.md` | How to propose improvements |

## Requirements

- Claude desktop app with Cowork mode (for setup and file-producing sessions), or any Claude project for drafting-only use.
- **`git`** — the workspace becomes a repository at setup. This is the safety model; there is no fallback.
- For the document pipeline: Python 3.10+ with `weasyprint`, `jinja2`, `markdown`, `pyyaml`, plus `pandoc`. Optional at first — the framework produces Markdown until you wire it up.
- For annotated interview-prep PDFs: `pandoc` with `xelatex`.

## Design principles

1. **Evidence before prose.** Nothing is claimed that the bank can't support; the watch-outs register records every framing that once went too far, and it grows one caught overclaim at a time.
2. **Ordering is sacred.** Duplicate-check → gating → initiation → drafting → voice audit → gates → maintenance → commit. Skills implement content; the project instructions own the sequence.
3. **Gates, not vibes.** The checks most often skipped under pressure are the ones made mechanical — and a gate that can't show its evidence hasn't run.
4. **Load what you matched.** Slim indexes, per-row detail files, companion files named by the matched row. Context spent on prescriptions you didn't match is context unavailable for the draft.
5. **Everything leaves a trail.** Changelogs for the bank, the instructions and the template; a commit at every session close; every past state one `git checkout` away.
6. **Human in the loop, always.** The framework drafts and verifies; you review, correct, and sign. Your edits are the highest-quality signal it ever receives — the loop that turns them into rules is the point. The checklist discipline exists to serve that review rather than to replace it: a gate that must show its counts, quotes and command output hands you a document whose weak points are already named, so your reading time goes to judgement instead of proofreading. And the disciplines that block — no unsourced claim about a named person, no unlabelled inference, no spoken answer that contradicts what you already signed — all protect the same thing, which is that everything the framework produces stays true and stays yours.

## Provenance and licence

Extracted and de-personalised from a live framework maintained by Mikhail Dudarenok. MIT licence — use it, adapt it, ship your own version. Attribution appreciated, not required.
