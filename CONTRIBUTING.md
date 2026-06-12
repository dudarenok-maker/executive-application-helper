# Contributing

Improvements are welcome — this framework got good by being iterated against real applications, and that's the bar for changes here too.

## What makes a good contribution

- **Structural improvements** that would benefit any user: a new verification discipline, a sharper setup flow, a clearer skeleton, a fix to an ordering or integrity rule.
- **Bug fixes** in the skill skeletons, the setup orchestrator, or the check script.
- **De-personalisation fixes** — if you find a leftover personal reference or a placeholder that doesn't get replaced by the setup flow, flag it.

## What doesn't belong

- Personal evidence content (proof points, metrics, role histories). The framework ships skeletons; content stays with each user.
- Changes that fragment the ordering discipline (duplicate-check → gating → initiation → drafting → verification → maintenance). Skills implement step content; the project instructions own the sequence — proposals that move sequencing into skills will be declined.

## How

1. Open an issue describing the change and, ideally, the real-world failure or friction that motivated it (that's how every rule in this framework was born).
2. PRs: keep changes scoped, update `template/Template_Changelog.md` with a properly formatted entry (see the entry template in that file), and bump the version per its semantic-versioning rules.

## Conduct

Be decent. This is a small project maintained around a day job.
