---
# =============================================================================
# Resume_Master.md — THE single source of truth for every resume output.
#
# Replaces the older dual-source arrangement (a designer-tool PDF plus a
# divergent Markdown copy). There is exactly one resume file. Variants live in
# the `variants:` block below and are selected at build time:
#
#     cd Pipeline
#     python3 build.py resume --source ../Resume_Master.md            # master, 3pp
#     python3 build.py resume --source ../Resume_Master.md --short    # 2-page cut
#     python3 build.py resume --source ../Resume_Master.md --variant public_sector
#
# If you ever want to create a second resume file, you want a variant instead.
# =============================================================================
name: [Candidate Name]
headline: "[Primary positioning headline — role frame, then three to four capability anchors]"
contact:
  - "[email]"
  - "[phone]"
  - "[city, country]"
  - "[linkedin.com/in/...]"
credentials: "[Post-nominals | professional memberships | citizenship / work rights]"

# Highlights are authored ONCE under "## Career highlights" below. `highlight_order`
# is a list of 1-based indices into that list — it selects and orders which
# highlights appear. The master usually shows the first six.
highlight_order: [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------------------------
# Variants. Each may override ONLY: headline, profile, credentials,
# highlight_order. Anything else belongs in the body below, not here.
#
# Guidance: create a variant when a role FAMILY recurs, not when a single
# application feels different — that way lies the file sprawl this replaced.
# Sensitive credentials (security clearances, medical registrations) belong on
# a targeted variant, never on the default line of an openly-hosted resume.
# ---------------------------------------------------------------------------
variants:
  [role_family_1]:
    headline: "[Headline recast for this role family]"
    highlight_order: [1, 4, 2, 7, 3, 5]
  [role_family_2]:
    headline: "[Headline recast for this role family]"
    highlight_order: [2, 5, 1, 6, 3, 4]
    credentials: "[Optional per-variant credentials override]"
---

## Profile

[Three to four lines. Lead with the thread that connects the career — sector breadth, capability
mix, signature outcomes — then two or three of the strongest quantified proof points, then the
framing you most want a reader to leave with. Written once; a variant may override it wholesale.]

## Career highlights

> **Setup guidance:** Six to twelve bullets, each a self-contained outcome with scale and result.
> Author them strongest-first — `--short` mode and `highlight_order` both key off position. Every
> number here must reconcile with `Examples_Master.md` Section 6 (signature metrics); a figure that
> appears on the resume but not in the bank is an unverified claim.

- [Outcome with scale and measurable result.]
- [Outcome with scale and measurable result.]
- [Outcome with scale and measurable result.]
- [Outcome with scale and measurable result.]
- [Outcome with scale and measurable result.]
- [Outcome with scale and measurable result.]

## Experience

> **Setup guidance:** Each `### ` heading is a role title. `Employer:` and `Dates:` are mandatory
> (the build fails without them). `Location:`, `Context:` and `About:` are optional. Consecutive
> roles sharing an `Employer:` value render under a single employer heading — order them
> back-to-back and let chronology decide, never interleave to force a grouping. Author bullets
> strongest-first: `--short` keeps the first N.

### [Most recent role title]
Employer: [Organisation]
Dates: [MM/YYYY] – [MM/YYYY or "current"]
Location: [City]
About: [Optional one-line employer descriptor — industry, size, listing status. Renders once per employer.]
Context: [Optional one-line scene-setter — the situation on arrival.]

- [Achievement: scope, action, measurable outcome.]
- [Achievement: scope, action, measurable outcome.]
- [Achievement: scope, action, measurable outcome.]
- [Achievement: scope, action, measurable outcome.]

### [Previous role title]
Employer: [Organisation]
Dates: [MM/YYYY] – [MM/YYYY]
Location: [City]

- [Achievement: scope, action, measurable outcome.]
- [Achievement: scope, action, measurable outcome.]

### [Earlier role title]
Employer: [Organisation]
Dates: [MM/YYYY] – [MM/YYYY]
Location: [City]

- [Achievement: scope, action, measurable outcome.]

## Education

- **[Qualification]** — [Institution] ([Year])
- **[Qualification]** — [Institution]

## Capability snapshot

> **Setup guidance:** Four to six labelled lines. This is the skim surface that replaces a skills
> table — group by capability, not by tool. In `--short` mode these collapse into one compact
> paragraph, so keep each detail string tight.

- **[Capability label]:** [Detail — named systems, scale, jurisdictions, frameworks.]
- **[Capability label]:** [Detail.]
- **[Capability label]:** [Detail.]
- **[Capability label]:** [Detail.]
