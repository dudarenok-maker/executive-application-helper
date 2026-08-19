# `styles/` — optional design overrides

Empty by design. `brand.css` carries the default design system; a file here is loaded **after** it
when `--style <name>` is passed, and only needs to reset the rules it wants to change.

```sh
python3 build.py resume --source ../Resume_Master.md --style understated
# loads brand.css, then styles/understated.css
```

Add one only if the candidate genuinely needs a second look — a stricter public-sector rendering,
say, or a monochrome variant for a portal that mangles colour. A separate style is not the answer to
"this role needs a different emphasis"; that is what resume variants are for.
