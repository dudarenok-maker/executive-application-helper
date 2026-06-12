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

When the live framework's Step 5 (template package maintenance) fires, the session mirrors structural changes into the local `_Template/` and this working copy. Then:

```bash
git add -A && git commit -m "v0.x.y — <short descriptor from Template_Changelog>"
git push
```

Tag releases to mirror the instructions version: `git tag v0.5.4 && git push --tags` (template `v0.X.Y` mirrors instructions `VX.Y`).

This file is maintainer-local and harmless to publish; delete it from the repo if preferred.
