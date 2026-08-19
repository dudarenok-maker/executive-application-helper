# Publishing this repo (maintainer notes)

One-time setup — the repo is already initialised and committed locally.

1. Create the repository on GitHub: https://github.com/new — name `executive-application-helper`, public, **no** README/licence/gitignore (they exist locally).
2. From this folder, run:

```bash
git remote add origin https://github.com/<your-username>/executive-application-helper.git
git push -u origin main
```

3. On the repo page, set the description — *"Run executive job applications and interview prep as a Claude project: evidence bank, matrix retrieval, verification-skill gates"* — and add topics: `claude`, `claude-ai`, `cowork`, `prompt-engineering`, `job-applications`, `interview-preparation`, `ai-agents`.

## Ongoing releases

When the live framework's Step 5 (template package maintenance) fires, the session mirrors structural changes into the local `_Template/` and into this working copy, then **commits here but never pushes** — that boundary is deliberate, so nothing reaches the public remote without a maintainer read-through. The mirroring session runs no git command in the parent workspace repository at all. To release:

```bash
git log -1 --stat               # what the mirroring session committed
git show HEAD                   # read it before pushing
git push
```

If the mirror needs correcting first, amend or add a follow-up commit locally — the unpushed commit is the review checkpoint, not a fait accompli.

Tag releases to mirror the instructions version (template `v0.X.Y` mirrors instructions `VX.Y`). Use an **annotated** tag whose message is the release notes, so the GitHub Release can be created from it without retyping:

```
git tag -a v0.X.Y -F <notes-file>     # or -a v0.X.Y and write the message in the editor
git push origin v0.X.Y
gh release create v0.X.Y --notes-from-tag --verify-tag
```

Without the `gh` CLI, create the release in the web UI (Releases → Draft a new release → choose the existing tag) and paste the same notes. Release notes are written for someone deciding whether to adopt: what changed structurally, what is new, what blocks that did not block before, and what migration costs. The changelog carries the full detail; the release notes carry the decision.

**Before a major release**, check three things beyond the diff:

1. **De-personalisation.** Grep the tree for real names, employers, metrics and absolute paths. The one deliberate exception is the maintainer attribution in `README.md` and the historical entries in `template/Template_Changelog.md`, which record who made each change.
2. **Internal coherence.** No file should reference a retired mechanism as if it were live, and no two files should state the same rule differently. Retirements are the easy thing to half-finish.
3. **The pipeline runs.** `python3 template/Pipeline/build.py resume --source <a filled-in Resume_Master.md>` should produce a PDF from a populated source. Shipping a build system that doesn't build is worse than shipping no build system.

This file is maintainer-local and harmless to publish; delete it from the repo if preferred.
