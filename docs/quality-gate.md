# Quality Gate

This quality gate prevents the agent from delivering a PDF that is technically generated but does not match the final review PDF template.

## Core rule

The PDF is not final until both are true:

1. The user's actual requested outcome is complete.
2. The PDF passes the visual template compliance check.

If the task outcome is blocked, the PDF must say it is blocked and must not call the result final/successful.

## Required template pieces

Every final review PDF must include:

- Page 1 request/overview page.
- A polished `What this document says` overview card.
- Small pink accent bar inside the Page 1 overview card.
- Subtle rounded row cards inside the overview card.
- Numbered pastel circles on Page 1 rows.
- Pink problem pages.
- Green solution pages.
- Minimal no-container footer.
- Footer links:
  - external-link icon + `Voice note`
  - divider
  - external-link icon + `Resources`
- Clickable links.
- Full visual QA before delivery.

## Audio / voice link rule

If a voice note exists, the PDF must include it in two places:

1. Page 1 overview row 1:
   - label: `Audio link`
   - blue external-link icon
   - blue text: `Click to review audio`

2. Every page footer:
   - `Voice note` link

If no voice note exists, either generate one when appropriate or remove the audio row intentionally. Do not leave broken or fake audio links.

## Resource link rule

Every page footer must include a clickable `Resources` link.

The Resources link should point to a Drive folder or equivalent asset folder containing:

- final PDF
- screenshots/evidence
- voice note if present
- supporting files

## Final outcome rule

Do not call the PDF final if the requested task did not actually complete.

Examples:

- If the user asked for a live public campaign, a draft campaign is not final.
- If the user asked for a working public URL, a 404 is not final.
- If the user asked for a successful signup + post, the PDF must show the successful post or clearly state the blocker.

## Required QA renders

Before sending, render:

- Page 1 full image.
- Page 1 overview-card crop.
- Footer crop from Page 1.
- Footer crop from at least one interior page.
- Full contact sheet of every page.

## Required vision QA prompts

Run visual QA with questions like:

1. `Does Page 1 match the review-pdf-skill template exactly: overview card, pink accent, row cards, numbered circles, audio row if audio exists, and no extra container?`

2. `Does the footer show minimal no-container Voice note and Resources links with external-link icons, close together, no clipping or overlap?`

3. `Does the full contact sheet show pink problem pages, green solution pages, all footers present, no clipping, no overlap, no missing links, and no layout regressions?`

4. `Does the final page clearly state the real final outcome and provide links/resources?`

## Auto-fail conditions

Reject and rebuild if any of these are true:

- Missing `Voice note` footer link when audio exists.
- Missing `Resources` footer link.
- Footer has a container/pill/card.
- Page 1 is missing `What this document says`.
- Page 1 overview card has no pink accent bar.
- Page 1 rows are plain text instead of row cards.
- Problem/solution pages do not use pink/green roles.
- PDF is text-heavy.
- Screenshot/card overlaps text.
- Text is clipped.
- Any page has unsafe margins.
- A public/live task is only draft/blocked but described as successful.
- Links are not clickable.
- Full contact sheet was not checked.

## Delivery wording

The final response should never hide a blocker.

If successful:

```text
Done — final review PDF is ready.
```

If blocked:

```text
Blocked — I created the review PDF, but the requested final outcome is not complete because [exact blocker].
```

Only use `final` when the real task outcome and the template QA both pass.
