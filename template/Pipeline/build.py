#!/usr/bin/env python3
"""build.py — Executive Application Helper document pipeline.

Renders resume and cover-letter content (markdown with YAML front-matter,
or plain YAML for the resume) through Jinja2 HTML templates and WeasyPrint
into A4 PDFs under the shared design system (brand.css — the "Navy
Statement" system, locked at setup — see README).

Usage:
    python3 build.py resume --source Resume_Master.md [--variant nsw] [--short]
    python3 build.py letter --source letter.md --band short|long [--docx]

The exact Resume_Master.md and letter source formats are documented in
README.md (with a complete miniature example).

Engine: WeasyPrint (no network at build time). Fallback engine if output
ever disappoints: headless Chromium (a deliberate choice, not a silent fallback) — do not
switch silently; that is a lead decision.
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup, escape
from weasyprint import HTML, CSS

PIPELINE_DIR = Path(__file__).resolve().parent
STYLES_DIR = PIPELINE_DIR / "styles"
BRAND_CSS = PIPELINE_DIR / "brand.css"
RESUME_TEMPLATE = "resume_template.html"
LETTER_TEMPLATE = "letter_template.html"

# Length bands (words, body only — header/date/recipient/sign-off
# excluded). Keyed by channel: short = private-sector/recruiter/Seek
# briefs; long = public-sector/criteria letters.
LENGTH_BANDS = {"short": (350, 550), "long": (900, 1250)}


# --------------------------------------------------------------- helpers

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")


def md_inline(text):
    """Jinja filter `md`: escape, then render **bold** / *italic*."""
    if text is None:
        return ""
    s = str(escape(str(text)))
    s = _BOLD.sub(r"<strong>\1</strong>", s)
    s = _ITALIC.sub(r"<em>\1</em>", s)
    return Markup(s)


def jinja_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(PIPELINE_DIR)),
        undefined=StrictUndefined,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["md"] = md_inline
    return env


def split_front_matter(text: str, name: str):
    """Return (meta_dict, body_str) from a '---' YAML front-matter file."""
    if not text.startswith("---"):
        sys.exit(f"error: {name} has no YAML front-matter block; "
                 "it must open with '---'.")
    end = text.find("\n---", 3)
    if end == -1:
        sys.exit(f"error: unterminated front-matter in {name}.")
    meta = yaml.safe_load(text[3:end]) or {}
    if not isinstance(meta, dict):
        sys.exit(f"error: front-matter in {name} is not a mapping.")
    body = text[end + 4:]
    body = body.split("\n", 1)[1] if "\n" in body else ""
    return meta, body


def resolve(path_str: str) -> Path:
    p = Path(path_str)
    return p if p.is_absolute() else (Path.cwd() / p).resolve()


def word_count(paragraphs) -> int:
    return sum(
        len(p.replace("**", " ").replace("*", " ").split())
        for p in paragraphs
    )


# ------------------------------------------- resume: markdown body parse

SECTION_ALIASES = {
    "profile": "profile",
    "career highlights": "highlights",
    "highlights": "highlights",
    "experience": "employment",
    "education": "education",
    "capability snapshot": "capabilities",
}

_H2 = re.compile(r"^##(?!#)\s*(.+?)\s*$")
_H3 = re.compile(r"^###(?!#)\s*(.+?)\s*$")
_BULLET = re.compile(r"^-\s+(.*)$")
_ROLE_KEY = re.compile(r"^(Employer|Dates|Location|Context|About)\s*:\s*(.*)$", re.I)


def _split_sections(body: str, src: str):
    """Split markdown body into [(canonical_key, [lines])]."""
    sections, key, buf = [], None, []
    for line in body.splitlines():
        m = _H2.match(line)
        if m:
            if key is not None:
                sections.append((key, buf))
            heading = m.group(1).strip().lower()
            if heading not in SECTION_ALIASES:
                allowed = ", ".join(sorted(set(SECTION_ALIASES)))
                sys.exit(f"error: unknown section '## {m.group(1)}' in {src}. "
                         f"Allowed headings: {allowed}")
            key, buf = SECTION_ALIASES[heading], []
        elif key is not None:
            buf.append(line)
        elif line.strip():
            sys.exit(f"error: content before the first '## ' heading in "
                     f"{src}: {line.strip()!r}")
    if key is not None:
        sections.append((key, buf))
    return sections


def _parse_paragraphs(lines):
    """Blank-line-separated paragraphs, internal newlines collapsed."""
    text = "\n".join(lines)
    return [" ".join(p.split()) for p in re.split(r"\n\s*\n", text) if p.strip()]


def _parse_bullets(lines, src, where):
    items = []
    for line in lines:
        if not line.strip():
            continue
        m = _BULLET.match(line)
        if m:
            items.append(m.group(1).strip())
        elif items:                       # wrapped continuation line
            items[-1] += " " + line.strip()
        else:
            sys.exit(f"error: expected '- ' bullet in {where} of {src}, "
                     f"got: {line.strip()!r}")
    return items


def _parse_experience(lines, src):
    roles = []
    for line in lines:
        m = _H3.match(line)
        if m:
            roles.append({"title": m.group(1).strip(), "meta": {}, "bullets": []})
            continue
        if not line.strip():
            continue
        if not roles:
            sys.exit(f"error: content in ## Experience of {src} before the "
                     f"first '### ' role heading: {line.strip()!r}")
        cur = roles[-1]
        mk = _ROLE_KEY.match(line)
        if mk:
            cur["meta"][mk.group(1).lower()] = mk.group(2).strip()
            continue
        mb = _BULLET.match(line)
        if mb:
            cur["bullets"].append(mb.group(1).strip())
            continue
        if cur["bullets"]:                # wrapped continuation line
            cur["bullets"][-1] += " " + line.strip()
            continue
        sys.exit(f"error: unrecognised line under role '{cur['title']}' in "
                 f"{src}: {line.strip()!r} (expected 'Employer:/Dates:/"
                 f"Location:/Context:' or '- ' bullets)")

    employment = []
    for r in roles:
        employer = r["meta"].get("employer")
        if not employer:
            sys.exit(f"error: role '{r['title']}' in {src} is missing its "
                     f"'Employer:' line.")
        if not r["meta"].get("dates"):
            sys.exit(f"error: role '{r['title']}' in {src} is missing its "
                     f"'Dates:' line.")
        entry = {
            "title": r["title"],
            "dates": r["meta"]["dates"],
            "location": r["meta"].get("location"),
            "context": r["meta"].get("context"),
            "bullets": r["bullets"],
        }
        # Employer grouping: CONSECUTIVE roles under one employer render
        # under a single employer heading (a long-tenure employer may have several consecutive roles).
        about = r["meta"].get("about")
        if employment and employment[-1]["employer"] == employer:
            employment[-1]["roles"].append(entry)
            if about and not employment[-1].get("about"):
                employment[-1]["about"] = about
        else:
            employment.append({"employer": employer, "roles": [entry],
                               "about": about})
    # employer About renders once per employer across the whole resume,
    # even when a group is split by an interlude (e.g. FCTG / Aquatic / FCTG)
    seen = set()
    for emp in employment:
        if emp["employer"] in seen:
            emp["about"] = None
        elif emp.get("about"):
            seen.add(emp["employer"])
    return employment


_EDU_SPLIT = re.compile(r"^\*\*(.+?)\*\*\s*(?:[—–-]{1,2}\s*)?(.*)$")
_EDU_YEAR = re.compile(r"\s*\(([^()]*\d{4}[^()]*)\)\s*$")


def _parse_education(lines, src):
    items = []
    for raw in _parse_bullets(lines, src, "## Education"):
        m = _EDU_SPLIT.match(raw)
        if m:
            degree, rest = m.group(1).strip(), m.group(2).strip()
            year = None
            my = _EDU_YEAR.search(rest)
            if my:
                year = my.group(1).strip()
                rest = rest[:my.start()].strip()
            items.append({"degree": degree, "institution": rest or None,
                          "year": year})
        else:
            items.append({"degree": raw, "institution": None, "year": None})
    return items


_CAP_SPLIT = re.compile(r"^\*\*(.+?):?\*\*\s*:?\s*(.*)$")


def _parse_capabilities(lines, src):
    items = []
    for raw in _parse_bullets(lines, src, "## Capability snapshot"):
        m = _CAP_SPLIT.match(raw)
        if m:
            items.append({"label": m.group(1).rstrip(":").strip(),
                          "detail": m.group(2).strip()})
        else:
            items.append({"label": None, "detail": raw})
    return items


def parse_resume_markdown(body: str, src: str) -> dict:
    parsed = {}
    for key, lines in _split_sections(body, src):
        if key in parsed:
            sys.exit(f"error: duplicate '## {key}' section in {src}.")
        if key == "profile":
            parsed[key] = _parse_paragraphs(lines)
        elif key == "highlights":
            parsed[key] = _parse_bullets(lines, src, "## Career highlights")
        elif key == "employment":
            parsed[key] = _parse_experience(lines, src)
        elif key == "education":
            parsed[key] = _parse_education(lines, src)
        elif key == "capabilities":
            parsed[key] = _parse_capabilities(lines, src)
    return parsed


# ------------------------------------------------------- resume: build

OPTIONAL_KEYS = ("headline", "contact", "profile", "highlights", "credentials",
                 "employment", "education", "capabilities", "variants")


def load_source(path: Path) -> dict:
    """Load resume content from a YAML file, or from Resume_Master.md
    (YAML front-matter + conventional markdown body sections — see
    README.md). Body sections override same-named front-matter keys."""
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        data = yaml.safe_load(text)
    elif path.suffix == ".md":
        data, body = split_front_matter(text, path.name)
        data.update(parse_resume_markdown(body, path.name))
    else:
        sys.exit(f"error: unsupported source type: {path.suffix}")
    if not isinstance(data, dict) or "name" not in data:
        sys.exit(f"error: {path.name} did not yield a resume dict with 'name'.")
    return data


def normalise(data: dict) -> dict:
    for key in OPTIONAL_KEYS:
        data.setdefault(key, None)
    for emp in data.get("employment") or ():
        for role in emp.get("roles") or ():
            for k in ("location", "context", "bullets"):
                role.setdefault(k, None)
    return data


def apply_highlight_order(data: dict, order, label: str):
    """Subset/reorder highlights by 1-based indices."""
    n = len(data["highlights"] or ())
    bad = [i for i in order if not 1 <= i <= n]
    if bad:
        sys.exit(f"error: {label} highlight_order indices {bad} out of range 1..{n}.")
    data["highlights"] = [data["highlights"][i - 1] for i in order]


def apply_variant(data: dict, variant: str) -> dict:
    """Apply a named variant: per-family headline parenthetical and
    highlight ordering, defined under data['variants'][variant]."""
    variants = data.get("variants") or {}
    if variant not in variants:
        available = ", ".join(sorted(variants)) or "(none defined)"
        sys.exit(f"error: variant '{variant}' not found. Available: {available}")
    v = variants[variant] or {}
    if "headline" in v:
        data["headline"] = v["headline"]
    if "highlight_order" in v:  # 1-based indices into the master highlight list
        apply_highlight_order(data, v["highlight_order"], f"variant '{variant}'")
    for key in ("profile", "credentials"):
        if key in v:
            data[key] = v[key]
    return data


_YEAR = re.compile(r"\d{4}")

SHORT_BULLET_CAP_RECENT = 4    # most recent role
SHORT_BULLET_CAP_DEFAULT = 2   # every other role
SHORT_BULLET_CAP_EARLY = 1     # roles starting before SHORT_EARLY_YEAR
SHORT_EARLY_YEAR = 2013


def compress_for_short(data: dict) -> dict:
    """--short 2-page content compression (rules documented in README.md).

    Page 1 stays intact: header band, headline, profile, highlights (with
    whatever highlight_order applied), credentials bar. Compression:
      - drop every role's Context line EXCEPT the most recent role;
      - drop Location lines everywhere;
      - cap bullets: most recent role 4, other roles 2, roles whose start
        year is before 2013 just 1 — always the FIRST N in authored order
        (bullets are authored strongest-first);
      - Education untouched;
      - Capability snapshot renders as one compact "Label: detail" run
        separated by " \u00b7 " (template short-branch + brand.css).
    """
    most_recent = True
    for emp in data.get("employment") or ():
        for role in emp.get("roles") or ():
            role["location"] = None
            if most_recent:
                cap = SHORT_BULLET_CAP_RECENT
                most_recent = False
            else:
                m = _YEAR.search(role.get("dates") or "")
                early = bool(m) and int(m.group(0)) < SHORT_EARLY_YEAR
                cap = SHORT_BULLET_CAP_EARLY if early else SHORT_BULLET_CAP_DEFAULT
            if role.get("bullets"):
                role["bullets"] = role["bullets"][:cap]
    return data


def render_pdf(template_name: str, context: dict, out: Path,
               extra_css: Path | None = None):
    html_str = jinja_env().get_template(template_name).render(**context)
    stylesheets = [CSS(filename=str(BRAND_CSS))]
    if extra_css:
        stylesheets.append(CSS(filename=str(extra_css)))
    doc = HTML(string=html_str, base_url=str(PIPELINE_DIR)).render(
        stylesheets=stylesheets)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.write_pdf(str(out))
    return doc


def build_resume(args: argparse.Namespace) -> None:
    source = resolve(args.source)
    data = normalise(load_source(source))
    if args.variant:
        data = apply_variant(data, args.variant)
    elif isinstance(data.get("highlight_order"), list):
        apply_highlight_order(data, data["highlight_order"], "top-level")
    if args.short:
        data = compress_for_short(data)

    style_css = None
    if getattr(args, "short", False) and not args.style:
        style_css = STYLES_DIR / "_short_page.css"
    if args.style:
        style_css = STYLES_DIR / f"{args.style}.css"
        if not style_css.exists():
            available = ", ".join(p.stem for p in sorted(STYLES_DIR.glob("*.css")))
            sys.exit(f"error: unknown style '{args.style}'. Available: {available}")

    if args.out:
        out = resolve(args.out)
    else:
        suffix = (f"_{args.variant}" if args.variant else "") + \
                 ("_2page" if args.short else "")
        out = source.with_name(f"{source.stem}{suffix}.pdf")

    doc = render_pdf(RESUME_TEMPLATE,
                     dict(r=data, style=args.style or "default",
                          short=bool(args.short)),
                     out, style_css)
    print(f"wrote {out}  ({out.stat().st_size} bytes, {len(doc.pages)} page(s), "
          f"style={args.style or 'default'}, "
          f"variant={args.variant or 'master'}"
          f"{', short' if args.short else ''})")


# -------------------------------------------------------- letter: build

def load_letter_source(path: Path) -> dict:
    meta, body = split_front_matter(path.read_text(encoding="utf-8"), path.name)
    if "name" not in meta:
        sys.exit(f"error: letter front-matter in {path.name} needs 'name'.")
    contact = meta.get("contact") or []
    if isinstance(contact, str):
        contact = [c.strip() for c in contact.split("|") if c.strip()]
    recipient = meta.get("recipient") or []
    if isinstance(recipient, str):
        recipient = [recipient]
    paragraphs = [" ".join(p.split())
                  for p in re.split(r"\n\s*\n", body) if p.strip()]
    if not paragraphs:
        sys.exit(f"error: letter {path.name} has an empty body.")
    return {
        "name": meta["name"],
        "contact": contact,
        "date": meta.get("date"),
        "recipient": recipient,
        "salutation": meta.get("salutation"),
        "signoff": meta.get("signoff", "Yours sincerely,"),
        "signature": meta.get("signature", meta["name"]),
        "body_paragraphs": paragraphs,
    }


def export_letter_docx(letter: dict, out_docx: Path) -> None:
    """Portal-upload path: pandoc renders the same markdown source to
    .docx. Styling is approximate (no navy band; Word default styles) —
    the PDF remains canonical."""
    lines = [f"**{letter['name']}**"]
    if letter["contact"]:
        lines[-1] += "  "                       # markdown hard break
        lines.append(" | ".join(letter["contact"]))
    lines.append("")
    if letter["date"]:
        lines += [letter["date"], ""]
    if letter["recipient"]:
        lines += [r + "  " for r in letter["recipient"]] + [""]
    if letter["salutation"]:
        lines += [letter["salutation"], ""]
    for p in letter["body_paragraphs"]:
        lines += [p, ""]
    lines += [letter["signoff"] + "  ", f"**{letter['signature']}**"]
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write("\n".join(lines))
        tmp_path = tmp.name
    try:
        subprocess.run(["pandoc", "-f", "markdown", "-t", "docx",
                        "-o", str(out_docx), tmp_path], check=True)
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    print(f"wrote {out_docx}  ({out_docx.stat().st_size} bytes, pandoc docx "
          f"— approximate styling; PDF is canonical)")


def build_letter(args: argparse.Namespace) -> None:
    source = resolve(args.source)
    letter = load_letter_source(source)

    out = resolve(args.out) if args.out else source.with_suffix(".pdf")
    doc = render_pdf(LETTER_TEMPLATE, dict(l=letter), out)

    words = word_count(letter["body_paragraphs"])
    lo, hi = LENGTH_BANDS[args.band]
    pages = len(doc.pages)
    print(f"wrote {out}  ({out.stat().st_size} bytes)")
    print(f"pages: {pages}")
    print(f"body words: {words} (band '{args.band}' = {lo}–{hi})")
    if not lo <= words <= hi:
        direction = "under" if words < lo else "over"
        print(f"WARNING: body is {words} words — {direction} the "
              f"'{args.band}' band of {lo}–{hi} words.", file=sys.stderr)

    if args.docx:
        export_letter_docx(letter, out.with_suffix(".docx"))


# ----------------------------------------------------------------- main

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    p_resume = sub.add_parser("resume", help="render a resume PDF")
    p_resume.add_argument("--source", required=True,
                          help="content source: .yaml, or .md with YAML "
                               "front-matter + markdown body (Resume_Master.md)")
    p_resume.add_argument("--variant", default=None,
                          help="named variant from the source's 'variants' map")
    p_resume.add_argument("--short", action="store_true",
                          help="2-page mode (tighter type; content trimming "
                               "driven by the source)")
    p_resume.add_argument("--style", default=None,
                          help="optional design override from styles/<name>.css; "
                               "the built-in system in brand.css is the default")
    p_resume.add_argument("--out", default=None, help="output PDF path")
    p_resume.set_defaults(func=build_resume)

    p_letter = sub.add_parser("letter", help="render a cover-letter PDF")
    p_letter.add_argument("--source", required=True,
                          help=".md letter source: YAML front-matter (name, "
                               "contact, date, recipient, signoff) + body")
    p_letter.add_argument("--band", required=True, choices=sorted(LENGTH_BANDS),
                          help="length band: short = 350–550 words "
                               "(private-sector/recruiter/Seek), long = "
                               "900–1,250 (public-sector/criteria)")
    p_letter.add_argument("--out", default=None, help="output PDF path")
    p_letter.add_argument("--docx", action="store_true",
                          help="also export .docx via pandoc (portal uploads; "
                               "PDF remains canonical)")
    p_letter.set_defaults(func=build_letter)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
