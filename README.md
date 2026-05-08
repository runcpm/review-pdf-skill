# review-pdf-skill

A reusable Hermes skill for producing consistent, polished review PDFs in the same visual style as the final RunCPM / Claw Clips review deck.

The goal is simple: a user can say what they want reviewed, audited, summarized, or handed off, and the agent produces the same clean PDF concept every time.

## What this skill produces

A visual-first review PDF with:

- A clean Page 1 request/overview page
- A `What this document says` overview card
- Pink problem pages
- Green solution pages
- Minimal text
- One idea per page
- Clean external-link icons
- Clickable `Voice note` and `Resources` footer links
- Drive upload/share link
- Telegram-ready PDF delivery
- Full visual QA before delivery

## Visual standard

The deck should look like this concept:

- Warm cream/off-white page background
- Large bold black title
- Short simple subtitle
- White rounded cards with subtle border/shadow
- Small hot-pink accent bar inside the Page 1 overview card
- Subtle rounded row cards in the overview card
- Pastel numbered badges
- Blue clickable links
- Minimal footer: external-link icon + `Voice note` | external-link icon + `Resources`
- No footer container
- No extra blank containers
- No text-heavy pages

## Files

- `SKILL.md` — main Hermes skill instructions
- `requirements.txt` — Python dependencies for local rendering/QA tooling
- `scripts/render_review_pdf.py` — reference generator showing the visual system and output structure
- `examples/example_content.json` — example content payload for the reference generator
- `docs/visual-spec.md` — detailed visual rules
- `docs/how-to-use.md` — usage guide for agents/users

## How to use in Hermes

1. Install/copy this skill into your Hermes skills directory.
2. Ask for a review PDF, for example:

```text
Review this website and make the final PDF in the review-pdf-skill style.
```

or:

```text
Turn these notes into a final review PDF using review-pdf-skill.
```

3. The agent should:
   - load `review-pdf-skill`
   - gather any task-specific evidence
   - create the PDF
   - render QA crops/contact sheet
   - run visual QA
   - upload to Drive if connected
   - return `MEDIA:/opt/data/...pdf` and Drive link

## Local reference generator

The included script is a reference implementation for the visual concept.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/render_review_pdf.py examples/example_content.json /tmp/example_review_pdf.pdf
```

The generated PDF is intentionally generic, but it demonstrates:

- Page 1 request/overview page
- overview card and row cards
- problem/solution page types
- final links page
- minimal footer
- clickable links
- external-link icon style

## Required related skills

Use these alongside `review-pdf-skill` depending on the task:

- `create-deliver-pdf` — PDF generation, validation, Telegram delivery, visual QA
- `google-workspace` — Drive upload/share link
- browser/dogfood skills — website/app QA
- GitHub/code-review skills — code or repo review PDFs
- OCR/document skills — PDF/image/document reviews
- social/video skills — TikTok/Instagram/YouTube/video breakdown PDFs
- research/web skills — fact-grounded research review PDFs

## Delivery format

Final agent response should be short:

```text
Done — final review PDF is ready.

What changed:
- ...

QA passed:
- Page 1 passed
- footer passed
- full contact sheet passed

PDF:
MEDIA:/opt/data/name_FINAL.pdf

Drive link:
https://drive.google.com/file/d/.../view?usp=drivesdk
```

## Quality bar

Never deliver until:

- Page 1 explains the PDF in seconds
- overview card looks polished
- footer has no container
- icons are aligned
- links are clickable
- there is no clipping/overlap
- full contact sheet passes
- PDF validates as `%PDF`
