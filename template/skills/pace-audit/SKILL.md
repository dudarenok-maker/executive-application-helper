---
name: pace-audit
description: "Run an honest timing audit on the spoken responses in the candidate's interview-prep documents, at the candidate's actual measured speaking pace — never at the generic 165 wpm executive baseline. Use this skill whenever a speaking-notes addendum or prep document with spoken responses is about to be delivered, AND after every content reshape or tightening pass (timing drifts with every edit). Also use when [Candidate First Name] asks 'how long does this run', 'time these responses', 'am I over budget', or 'run the pace check'. The audit is mechanical (~10–30 sec): word count ÷ actual wpm vs the format's time budget, with a two-pass tightening plan for any response that runs over."
---

# Pace Audit — interview-prep timing verification skill

Codifies Convention 11 (honest timing audit) and Convention 9 (two-round tightening) of `Project_Instructions.md` (rev 2026-06-12). Wave 2 verification skill of the framework.

A response of 525 words runs ~3:11 at 165 wpm but ~3:37 at the candidate's actual ~145 wpm — and the gap matters when the budget is tight. This skill makes the timing reality-check mechanical so it cannot silently default to the flattering baseline.

---

## When to invoke

- **Default triggers:** before delivering any speaking-notes addendum or prep document containing spoken responses; **after every reshape or tightening pass** (Convention 11: re-audit after every reshape).
- **Explicit triggers:** "time these", "how long does this run", "am I over", "run the pace check".
- **At panel-prep kickoff:** confirm the candidate's current pace once per session if not already stated — use the pace measured at setup.

## Inputs the skill needs

1. **The spoken responses** (text or file path) — typically Section A tailored responses and Section B backup STARs of an addendum.
2. **The time budget per response** — from recruiter/panel intel if available, else format defaults: ~90 sec recruiter screen; 2–3 min behavioural panel; 2–3 min executive panel.
3. **the candidate's confirmed pace** for this session (per the setup measurement; markedly lower effective rate where [pause] markers are dense).

## Method

Load `references/pace-method.md`, then per response:

1. Count words (exclude stage directions: `[pause]`, `[STOP — …]`, drop-list tables, headings).
2. Compute runtime at the confirmed wpm; add ~2–3 sec per `[pause]`, ~1–2 sec per `[short pause]`.
3. Compare to budget. Verdict per response: **Under / On / Over** (Over = >10% past budget).
4. For every Over response, produce the **two-pass tightening plan**: pass 1 = the existing drop-list items (~15–20 sec recovery); pass 2 = structural cuts inside paragraphs (compressed result-block listings, one of two parallel-structure sentences, `[pause]` markers between sub-sections) for ~25–35 sec total. **Never cut closing principle lines.**

## Output format

A timing reality-check table (Response / words / runtime at actual wpm / budget / verdict / recovery needed), then a one-line overall verdict. Gate behaviour: any response >25% over budget blocks delivery until a tightening pass runs; 10–25% over is advisory with the two-pass plan attached.
