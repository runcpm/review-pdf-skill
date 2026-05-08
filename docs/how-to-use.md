# How to Use review-pdf-skill

## User prompts that should trigger this skill

Use this skill when a user says things like:

- `Make this into a final PDF.`
- `Review this site and send me the final PDF.`
- `Turn these notes into the same review PDF style.`
- `Make a visual handoff PDF.`
- `Audit this app and give me the polished PDF.`
- `Use review-pdf-skill.`

## Agent workflow

1. Load `review-pdf-skill`.
2. Load any task-specific supporting skill:
   - website/app review → browser QA / dogfood
   - code/repo review → GitHub/code review
   - document review → OCR/document extraction
   - video/social review → TikTok/Instagram/YouTube skills
   - Drive output → google-workspace
   - PDF generation → create-deliver-pdf
3. Gather evidence.
4. Build a short outline.
5. Generate the PDF with the standard visual system.
6. Render QA crops/contact sheet.
7. Run visual QA.
8. Patch if needed.
9. Verify `%PDF`.
10. Upload to Drive.
11. Return Telegram media path and Drive link.

## Content mapping

For any user request, map the content into this deck structure:

Page 1:
- What the request was.
- What was checked.
- Main issue/finding.
- What the final pages show.

Problem pages:
- What is broken, confusing, risky, or unclear.

Solution pages:
- What to build, fix, change, write, ship, or hand off.

Final page:
- Voice note / resources / files / links.

## Example prompt

```text
Review this landing page and make the final review PDF using review-pdf-skill:
https://example.com
```

Expected behavior:

- Agent browses the site.
- Takes screenshots.
- Identifies key problems and fixes.
- Builds a visual review deck.
- Runs visual QA.
- Uploads and sends the PDF.

## Example final response

```text
Done — final review PDF is ready.

What changed:
- reviewed the page
- turned findings into pink problem pages
- added green fix pages
- added minimal clickable footer links

QA passed:
- Page 1 passed
- footer passed
- full contact sheet passed

PDF:
MEDIA:/opt/data/example_FINAL.pdf

Drive link:
https://drive.google.com/file/d/.../view?usp=drivesdk
```
