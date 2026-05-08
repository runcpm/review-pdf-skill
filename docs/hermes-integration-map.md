# Hermes Integration Map

This file lists every Hermes skill/tool area needed to fully reproduce the final review PDF workflow.

The `review-pdf-skill` is the visual/output orchestrator. It does not replace every specialized skill; it tells the agent which supporting skill/tool to load based on the user's request.

## Always needed

### `review-pdf-skill`
Purpose:
- Owns the final visual style.
- Creates the consistent review PDF concept.
- Enforces the Page 1 overview card, pink/green pages, minimal footer, clickable links, and QA standard.

### `create-deliver-pdf`
Purpose:
- Generate the PDF with ReportLab/PyMuPDF.
- Save under `/opt/data/`.
- Verify the file starts with `%PDF`.
- Deliver to Telegram with `MEDIA:/absolute/path.pdf`.
- Render QA crops/contact sheets.

### Visual QA tools
Purpose:
- `vision_analyze` checks Page 1, footer crop, and full contact sheet.
- PyMuPDF renders page PNGs/crops/contact sheets.
- This is mandatory before final delivery.

## Usually needed

### `google-workspace`
Purpose:
- Upload final PDF to Google Drive.
- Upload voice/assets if needed.
- Set anyone-reader permission.
- Return Drive links.

### Telegram delivery
Purpose:
- Deliver final PDF natively using `MEDIA:/opt/data/file.pdf`.
- If needed, send follow-up messages/files through the connected Telegram channel.

### Voice / audio tools
Purpose:
- If a voice note exists, link it on Page 1 and in the footer.
- If the user asks for a generated voice note, use `text_to_speech` to create audio.
- Use page-specific voice note URLs if available; otherwise use the main voice note.

## Input-gathering skills/tools by task type

### Internet/web research
Use when the PDF needs current facts, research, market info, docs, or online evidence.

Tools/skills:
- `web_search`
- `web_extract`
- research skills when relevant

### Website/app review
Use when the user gives a URL, app, landing page, login flow, product page, or UI to audit.

Tools/skills:
- browser tools for navigation/screenshots
- `dogfood` for systematic exploratory QA
- `firecrawl` if useful for site extraction

### GitHub/code review
Use when the user gives a repo, PR, branch, codebase, deployment issue, or bug.

Skills:
- `github-auth`
- `github-repo-management`
- `github-code-review`
- `codebase-inspection`
- `systematic-debugging`
- `requesting-code-review`

### Documents/PDF/images
Use when the user gives PDFs, screenshots, scans, docs, or asks to transform written notes.

Skills/tools:
- `ocr-and-documents`
- `nano-pdf` when editing an existing PDF
- `vision_analyze` for screenshots/images
- `create-deliver-pdf` for final generation

### Social/video analysis
Use when the user gives TikTok, Instagram, YouTube, or short-form reference videos.

Skills:
- `tiktok-instagram-viral-strategy-analysis`
- `youtube-content`
- `public-x-post-video-fallback` for X/Twitter posts/videos

### Drive asset library / client folders
Use when the final PDF and assets should be organized in Google Drive.

Skills:
- `google-workspace`
- `google-drive-asset-library-tracker`
- `google-drive-creative-asset-library`

### Creative assets or generated visuals
Use when the PDF needs generated images, ads, mockups, diagrams, or creative pages.

Skills/tools:
- `brand-matched-drive-creative-deliverables`
- `popular-web-designs`
- `architecture-diagram`
- image/video generation tools if the user requests generated media

## Agent decision rule

When a user asks for a final review PDF:

1. Load `review-pdf-skill`.
2. Load `create-deliver-pdf`.
3. Load `google-workspace` if Drive upload/share is expected.
4. Load the task-specific skill based on the input:
   - URL/app/site → browser/dogfood.
   - repo/code → GitHub/code review.
   - video/social → social/video skill.
   - document/image → OCR/vision.
   - current facts → web/research.
5. Gather evidence.
6. Build the PDF using the visual contract.
7. QA with visual crops/contact sheet.
8. Deliver PDF + Drive link.

## Minimum final output

A complete run should produce:

- `/opt/data/...FINAL.pdf`
- rendered Page 1 PNG/crop
- rendered footer crop
- full contact sheet image
- Drive link if Google access is available
- Telegram `MEDIA:/opt/data/...FINAL.pdf`

## If something is unavailable

- No Google access: still deliver `MEDIA:/opt/data/...pdf`, and clearly say Drive upload is unavailable.
- No voice note: omit the `Audio link` overview row or link to resources only.
- No internet access: use only provided files/text and label assumptions.
- No Telegram delivery: save the PDF locally and provide the path.
