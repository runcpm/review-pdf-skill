---
name: review-pdf-skill
description: "Create a consistent polished review PDF for any task/request using the final template style: visual-first, minimal text, polished overview card, minimal clickable footer, Drive delivery, and full visual QA."
version: 1.0.0
---

# Review PDF Skill

Use this skill whenever a user wants a polished final PDF review, audit, report, handoff, checklist, UX review, product review, website/app test report, campaign review, or task summary that should have the same consistent visual concept as the final template.

The core promise: anyone can say what they want reviewed or turned into a final PDF, and the output should follow the same visual system every time.

## Required Supporting Skills / Capabilities

This skill depends on these workflows:

1. `create-deliver-pdf`
   - ReportLab/PyMuPDF PDF creation.
   - Telegram `MEDIA:/opt/data/file.pdf` delivery.
   - `%PDF` validation.
   - Full visual QA/contact-sheet workflow.

2. `google-workspace`
   - Upload the final PDF/assets to Drive.
   - Set anyone-reader permission.
   - Return a Drive share link.

3. Voice/audio tools
   - Link existing voice notes on Page 1 and every footer.
   - Use page-specific voice-note links when available.
   - Use `text_to_speech` when the user asks for a generated voice note.

4. Web/internet tools
   - Use `web_search` and `web_extract` for current facts, online evidence, sources, market research, docs, and public pages.

5. Browser/vision tools
   - Use browser tools for website/app flows and screenshots.
   - Use `vision_analyze` for screenshots, Page 1 crops, footer crops, and full contact-sheet QA.

6. Telegram delivery
   - Deliver the final PDF natively with `MEDIA:/opt/data/file.pdf`.
   - Send supporting files only when requested.

7. Task-specific input skills as needed:
   - Website/app audit: browser QA / dogfood / screenshots.
   - Code review: GitHub/codebase/code-review skills.
   - Social/video analysis: TikTok/Instagram/YouTube/video skills.
   - Document review: OCR/PDF/document extraction skills.
   - Research: web/research skills.
   - Drive asset management: Google Drive asset library/tracker skills.

See `docs/hermes-integration-map.md` in the public repo for the full skill/tool dependency map.

Always gather the task evidence first, then build the review PDF.

## Visual Style Contract

Match the final template review deck style:

- Warm off-white/cream page background.
- Large bold black titles.
- Short plain-language subtitles.
- Spacious modern layout with strong whitespace.
- White rounded cards with subtle gray border and soft shadow.
- Page 1 overview card includes a small hot-pink accent bar.
- Page 1 overview rows are subtle rounded row cards.
- Numbered pastel circles:
  - pale pink for request/problem rows.
  - pale mint green for solution/fix rows.
- Pink means problem.
- Green means solution.
- Black means normal text.
- Blue means links.
- Clean external-link icons for links.
- Minimal text. No paragraph-heavy pages.
- One idea per page.
- No random decorative assets.
- No internal/process wording such as `converted into template`, `PDF conversion`, or `Quick Overview`.
- No extra blank containers below cards.

## Theme Customization

The output layout must stay the same, but colors and fonts may be changed for different users/brands.

Allowed changes:
- background color.
- ink/text color.
- muted/body text color.
- link color.
- problem color and light problem badge color.
- solution color and light solution badge color.
- card, border, row background, and row border colors.
- regular font and bold font.

Do not change:
- Page 1 structure.
- `What this document says` card.
- row-card structure.
- problem/solution page pattern.
- minimal no-container footer.
- external-link icon concept.
- QA process.

If using the public repo reference renderer, pass a theme file:

```bash
python scripts/render_review_pdf.py examples/example_content.json /tmp/example_review_pdf.pdf --theme examples/example_theme.json
```

After any color/font change, run the same visual QA. Reject the PDF if contrast is weak, fonts clip, or it no longer feels like the same final template.

## Page 1 Required Layout

Page 1 should always be the request + overview page.

Required elements:

1. Small header left: project/review name.
2. Small header right: `REQUEST + OVERVIEW` or a task-specific section label.
3. Small hot-pink eyebrow label: `REQUEST`.
4. Main title from the user's actual request.
5. One- or two-line summary of what was checked, created, or reviewed.
6. Three legend pills:
   - `PINK = PROBLEM`
   - `GREEN = SOLUTION`
   - `BLACK = NORMAL TEXT`
7. Main card titled `What this document says`.
   - white rounded rectangle.
   - subtle border/shadow.
   - short pink accent bar near top-left.
   - 3–5 row cards max.

Preferred overview rows when audio exists:

1. `Audio link` — external-link icon + `Click to review audio`.
2. `Original ask` — compact summary of the user request.
3. `Found blocker` or `Main issue` — most important problem.
4. `Show fixes` or `Final output` — what the solution/final pages show.

Preferred overview rows when no audio exists:

1. `Original ask`.
2. `What I checked`.
3. `Main finding`.
4. `Final output`.

## Interior Page Pattern

Each page after Page 1 should focus on one idea.

Problem pages:
- Pink label/card: `PROBLEM`.
- Big title in plain language.
- One sentence max explaining the issue.
- Screenshot/mockup/diagram/checklist when useful.
- Optional sharp callout arrow, not cluttered.

Solution pages:
- Green label/card: `SOLUTION`.
- Big title in plain language.
- One sentence max explaining what to build/do.
- Mockup, checklist, or action card with minimal copy.

Final/resource pages:
- Simple title such as `Final links` or `Voice note + PDF links are attached`.
- Clean cards or link rows only.

## Footer Rules

Every page must use the final minimal footer:

- No footer card/container/pill.
- No stacked labels like `VOICE LINK` or `TASKS + RESOURCES`.
- Centered compact footer group:
  - small blue external-link icon + `Voice note`
  - thin subtle divider
  - small blue external-link icon + `Resources`
- Keep the two links close together so they feel like one footer.
- Keep every link clickable.
- Use the page-specific voice URL if available; otherwise use the main voice note URL.

## Icon Rules

Use the clean external-link icon, not the bulky chain icon.

Icon style:
- small blue outlined square/corner.
- diagonal arrow pointing up-right.
- lightweight stroke.
- aligned to the text baseline.
- same icon style in Page 1 audio row and footer.

Avoid:
- chunky interlocking chain icon.
- emoji-style icons.
- oversized icons.
- underline unless requested.
- footer pill/container.

## Workflow

1. Understand the user's task.
   - If the task needs evidence, gather it with the right tools first.
   - Do not invent findings.

2. Create a concise page outline.
   - Page 1 overview.
   - Problem pages.
   - Solution/fix pages.
   - Optional final links/resources page.

3. Generate the PDF under `/opt/data/`.
   - Use ReportLab for new decks.
   - Use PyMuPDF for patching existing PDFs.
   - Use clickable links.

4. Render QA files with PyMuPDF.
   - Page 1 full render.
   - Page 1 overview crop.
   - Footer crop.
   - Full contact sheet of every page.

5. Run visual QA with vision.
   - Page 1 overview card polish, row fit, icon alignment, no extra container.
   - Footer crop: no container, icons aligned, links close together.
   - Full contact sheet: serious issues only.

6. Patch and re-render if QA finds issues.
   - Never deliver with clipping, overlap, extra containers, unsafe margins, or bad footer alignment.

7. Verify the PDF.
   - Exists.
   - Non-empty.
   - Starts with `%PDF`.

8. Upload to Drive if available.
   - Use the correct project/client folder.
   - Set anyone-reader permission.
   - Return the Drive link.

9. Final response.
   - Keep it short.
   - Include what changed, QA passed, local PDF path, and Drive link.

## Final Response Format

```text
Done — final review PDF is ready.

What changed:
- [short bullets]

QA passed:
- Page 1 passed
- footer passed
- full contact sheet passed

PDF:
MEDIA:/opt/data/name_FINAL.pdf

Drive link:
https://drive.google.com/file/d/.../view?usp=drivesdk
```

See also:
- `docs/hermes-integration-map.md` for full tool/skill dependencies.
- `docs/theme-customization.md` for color/font changes without changing the layout.
- `docs/quality-gate.md` for the mandatory final-outcome and template-compliance checklist.

## Mandatory QA Checklist

Do not deliver until all pass:

- Page 1 explains the PDF in seconds.
- `What this document says` card looks polished.
- No extra blank container below the overview card.
- Page 1 link icon is the clean external-link icon.
- Footer has no container.
- Footer uses two close text links with icons.
- Every page footer is consistent.
- Links are clickable.
- No clipped text.
- No overlap.
- No unsafe margins.
- No huge dead space above text.
- Extra whitespace sits below content when possible.
- Full contact sheet has no serious regressions.
- PDF starts with `%PDF`.
- Drive link works / file has reader permission.

## Common Fixes Learned From The Final Template Iteration

- If Page 1 heading + audio link feel crowded, put audio in row 1 instead of floating near the heading.
- If footer feels too heavy, remove all labels and containers; keep only `Voice note | Resources` with icons.
- If footer links feel too far apart, reduce the gap and center them as one group.
- If the link/chain icon looks chunky, replace it with the clean external-link icon.
- If a new card creates an accidental blank container below Page 1, erase the duplicate area and re-QA Page 1.
- If rows feel plain, use subtle row cards inside the overview card instead of another outer container.
- If the deck becomes text-heavy, cut copy aggressively and use visual cards/checklists.

## Implementation Notes

Recommended Python stack:
- `/opt/data/pdf-venv/bin/python`
- `reportlab`
- `pymupdf` / `fitz`
- `Pillow`
- `google-api-python-client` for Drive uploads

For existing PDFs, PyMuPDF can patch/overlay small layout fixes quickly:
- erase areas with background-colored rectangles.
- draw new rounded cards/icons/text.
- delete/insert link annotations.
- save with `garbage=4, deflate=True`.

For new PDFs, ReportLab canvas is best for consistent cards, rows, links, and typography.

## Pitfalls

- Do not answer with only a plan; generate and verify the PDF.
- Do not skip full contact-sheet QA.
- Do not use generic default ReportLab styling.
- Do not add a separate listen-first page unless requested.
- Do not add random decorative assets.
- Do not leave old containers/artifacts after patching.
- Do not upload/share Drive files before QA passes.
