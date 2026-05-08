# Theme Customization

The review PDF template is intentionally fixed in structure, but easy to rebrand.

The rule is:

> Change colors and fonts only. Keep the layout, spacing, Page 1 overview card, problem/solution structure, footer, links, and QA process the same.

This lets anyone use the same polished output while matching their own brand.

## What can be changed

You may change:

- background color
- main text color
- muted/body text color
- link color
- problem color
- problem light color
- solution color
- solution light color
- card color
- border color
- row background color
- row border color
- regular font
- bold font

## What should stay the same

Do not change these unless you intentionally want a new template:

- Page 1 structure
- `What this document says` overview card
- row-card layout
- numbered badges
- problem pages
- solution pages
- minimal no-container footer
- external-link icon style
- one idea per page
- full visual QA workflow

## Theme file

Use `examples/example_theme.json` as the starting point.

```json
{
  "fonts": {
    "regular": "Helvetica",
    "bold": "Helvetica-Bold"
  },
  "colors": {
    "background": "#F8F4EF",
    "ink": "#090909",
    "muted": "#6C7480",
    "link": "#1E70CD",
    "problem": "#FF5B92",
    "problem_light": "#FFE7EE",
    "solution": "#14AB67",
    "solution_light": "#E2F8EE",
    "card": "#FFFFFF",
    "border": "#DFE4EB",
    "row_background": "#FCFCFC",
    "row_border": "#EDF0F5"
  }
}
```

## Using a theme with the reference renderer

```bash
python scripts/render_review_pdf.py examples/example_content.json /tmp/example_review_pdf.pdf --theme examples/example_theme.json
```

## Font notes

The reference renderer supports built-in ReportLab fonts by default:

- `Helvetica`
- `Helvetica-Bold`
- `Times-Roman`
- `Times-Bold`
- `Courier`
- `Courier-Bold`

If you want custom brand fonts, register them in the PDF script before rendering, then set the font names in the theme file.

## Good brand-safe changes

Examples:

- Make links purple instead of blue.
- Make problem pages orange instead of pink.
- Make solution pages teal instead of green.
- Use a darker background cream.
- Swap Helvetica for an installed brand font.

## QA reminder

After changing colors or fonts, always re-run visual QA:

- Page 1 overview crop
- footer crop
- full contact sheet

Reject the PDF if:

- text contrast is weak
- footer icons are too hard to see
- problem/solution colors are confusing
- custom fonts cause clipping
- Page 1 no longer feels like the same clean template
