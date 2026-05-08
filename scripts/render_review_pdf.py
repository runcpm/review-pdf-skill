#!/usr/bin/env python3
"""Reference renderer for review-pdf-skill.

Usage:
    python scripts/render_review_pdf.py examples/example_content.json /tmp/review.pdf

This is a reusable starting point for the final RunCPM review PDF concept.
It intentionally keeps copy minimal and uses the standard Page 1 overview card,
pink problem pages, green solution pages, and minimal clickable footer.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

W, H = LETTER

BG = colors.Color(248 / 255, 244 / 255, 239 / 255)
INK = colors.Color(9 / 255, 9 / 255, 9 / 255)
MUTED = colors.Color(108 / 255, 116 / 255, 128 / 255)
BLUE = colors.Color(30 / 255, 112 / 255, 205 / 255)
PINK = colors.Color(1, 91 / 255, 146 / 255)
PINK_LIGHT = colors.Color(1, 231 / 255, 238 / 255)
GREEN = colors.Color(20 / 255, 171 / 255, 103 / 255)
MINT_LIGHT = colors.Color(226 / 255, 248 / 255, 238 / 255)
BORDER = colors.Color(223 / 255, 228 / 255, 235 / 255)
ROW_BG = colors.Color(252 / 255, 252 / 255, 252 / 255)
ROW_BORDER = colors.Color(237 / 255, 240 / 255, 245 / 255)


def tw(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def draw_round_rect(c: canvas.Canvas, x, y, w, h, r=18, fill=colors.white, stroke=BORDER, sw=0.7):
    c.setStrokeColor(stroke)
    c.setLineWidth(sw)
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)


def draw_external_link_icon(c: canvas.Canvas, x, y, size=10, color=BLUE, bg=None, lw=1.05):
    """Draw small external-link icon. x/y is lower-left."""
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.roundRect(x, y, size, size, 1.6, stroke=1, fill=0)
    if bg is not None:
        c.setFillColor(bg)
        c.setStrokeColor(bg)
        c.rect(x + size * 0.56, y + size * 0.58, size * 0.52, size * 0.52, stroke=0, fill=1)
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x + size * 0.42, y + size * 0.42, x + size * 0.91, y + size * 0.91)
    c.line(x + size * 0.66, y + size * 0.91, x + size * 0.91, y + size * 0.91)
    c.line(x + size * 0.91, y + size * 0.91, x + size * 0.91, y + size * 0.66)


def draw_footer(c: canvas.Canvas, page_num: int, voice_url: str | None, resources_url: str | None):
    # Page number
    c.setFillColor(INK)
    c.setFont("Helvetica", 9)
    c.drawString(54, 35, str(page_num))

    # Minimal centered footer links, no container.
    fs = 9
    label1 = "Voice note"
    label2 = "Resources"
    icon = 9.5
    gap = 4.2
    item_gap = 16
    sep = 8
    total = icon + gap + tw(label1, "Helvetica", fs) + item_gap + sep + item_gap + icon + gap + tw(label2, "Helvetica", fs)
    x = (W - total) / 2
    y = 35

    def item(ix, label, url):
        draw_external_link_icon(c, ix, y - 1, size=icon, bg=BG, lw=0.95)
        tx = ix + icon + gap
        c.setFillColor(BLUE)
        c.setFont("Helvetica", fs)
        c.drawString(tx, y, label)
        end = tx + tw(label, "Helvetica", fs)
        if url:
            c.linkURL(url, (ix - 2, y - 4, end + 3, y + 11), relative=0)
        return end

    end1 = item(x, label1, voice_url)
    sx = end1 + item_gap
    c.setStrokeColor(colors.Color(172 / 255, 180 / 255, 190 / 255))
    c.setLineWidth(0.45)
    c.line(sx + 3, y - 2, sx + 3, y + 10)
    item(sx + sep + item_gap, label2, resources_url)


def draw_header(c: canvas.Canvas, left: str, right: str):
    c.setFillColor(colors.Color(110 / 255, 116 / 255, 128 / 255))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(54, H - 32, left.upper())
    c.drawRightString(W - 54, H - 32, right.upper())


def draw_pill(c, x, y, w, text, fill, text_color=INK):
    c.setFillColor(fill)
    c.setStrokeColor(fill)
    c.roundRect(x, y, w, 27, 13.5, stroke=0, fill=1)
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", 8.3)
    c.drawCentredString(x + w / 2, y + 9.2, text)


def draw_page_one(c: canvas.Canvas, data: dict):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    draw_header(c, data.get("project_label", "RUNCPM REVIEW"), "REQUEST + OVERVIEW")

    c.setFillColor(PINK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(54, H - 68, "REQUEST")

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 31)
    c.drawString(54, H - 113, data.get("title", "Review PDF"))

    c.setFont("Helvetica", 12.5)
    summary = data.get("summary", "Review the request, show the main issue, and provide dev-ready fixes.")
    c.drawString(54, H - 154, summary[:92])

    draw_pill(c, 82, H - 224, 118, "PINK = PROBLEM", PINK_LIGHT, PINK)
    draw_pill(c, 246, H - 224, 128, "GREEN = SOLUTION", MINT_LIGHT, INK)
    draw_pill(c, 416, H - 224, 130, "BLACK = NORMAL TEXT", INK, colors.white)

    # Main overview card.
    x, y, w, h = 60, 268, 492, 266
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.045))
    c.roundRect(x + 2, y - 3, w, h, 18, stroke=0, fill=1)
    draw_round_rect(c, x, y, w, h, r=18, fill=colors.white, stroke=BORDER, sw=0.65)

    c.setFillColor(PINK)
    c.roundRect(x + 18, y + h - 22, 40, 4, 2, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(x + 18, y + h - 53, "What this document says")

    rows = data.get("overview_rows") or []
    row_x = x + 18
    row_w = w - 36
    row_h = 35
    row_gap = 9
    start_y = y + h - 78 - row_h
    label_x = row_x + 46
    value_x = row_x + 196

    for i, row in enumerate(rows[:5]):
        ry = start_y - i * (row_h + row_gap)
        tone = row.get("tone", "problem")
        circle = MINT_LIGHT if tone == "solution" else PINK_LIGHT
        draw_round_rect(c, row_x, ry, row_w, row_h, r=11, fill=ROW_BG, stroke=ROW_BORDER, sw=0.45)
        c.setFillColor(circle)
        c.circle(row_x + 18, ry + row_h / 2, 12.5, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawCentredString(row_x + 18, ry + row_h / 2 - 3.2, str(i + 1))
        c.setFont("Helvetica-Bold", 11.5)
        c.drawString(label_x, ry + 12.4, row.get("label", "Item"))
        if row.get("type") == "link":
            draw_external_link_icon(c, value_x, ry + 12.2, size=11, bg=ROW_BG, lw=1.05)
            c.setFillColor(BLUE)
            c.setFont("Helvetica", 9.2)
            label = row.get("value", "Click to review")
            c.drawString(value_x + 16.5, ry + 12.6, label)
            url = data.get("voice_url") or data.get("resources_url")
            if url:
                c.linkURL(url, (value_x - 3, ry + 6, value_x + 16.5 + tw(label, "Helvetica", 9.2) + 4, ry + 29), relative=0)
        else:
            c.setFillColor(MUTED)
            c.setFont("Helvetica", 9.2)
            c.drawString(value_x, ry + 12.7, row.get("value", ""))

    draw_footer(c, 1, data.get("voice_url"), data.get("resources_url"))
    c.showPage()


def draw_content_page(c: canvas.Canvas, page_num: int, data: dict, item: dict):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    kind = item.get("kind", "problem").lower()
    is_solution = kind == "solution"
    accent = GREEN if is_solution else PINK
    light = MINT_LIGHT if is_solution else PINK_LIGHT
    label = "SOLUTION" if is_solution else "PROBLEM"
    draw_header(c, data.get("project_label", "RUNCPM REVIEW"), label)

    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(54, H - 68, label)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(54, H - 113, item.get("title", "Page title"))

    c.setFillColor(INK)
    c.setFont("Helvetica", 12.5)
    c.drawString(54, H - 154, item.get("body", "One clear sentence explains this page."))

    # Main action card.
    x, y, w, h = 70, 238, 472, 310
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.04))
    c.roundRect(x + 2, y - 3, w, h, 22, stroke=0, fill=1)
    draw_round_rect(c, x, y, w, h, r=22, fill=colors.white, stroke=BORDER, sw=0.65)
    c.setFillColor(light)
    c.roundRect(x + 24, y + h - 76, 110, 34, 17, stroke=0, fill=1)
    c.setFillColor(accent if not is_solution else INK)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(x + 79, y + h - 64, label)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(x + 24, y + h - 114, "What matters")

    bullets = item.get("bullets") or []
    by = y + h - 156
    for idx, bullet in enumerate(bullets[:5], 1):
        cy = by - idx * 38
        c.setFillColor(light)
        c.circle(x + 34, cy + 4, 11, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x + 34, cy + 1, str(idx))
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(x + 58, cy, bullet)

    draw_footer(c, page_num, data.get("voice_url"), data.get("resources_url"))
    c.showPage()


def draw_final_page(c: canvas.Canvas, page_num: int, data: dict):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    draw_header(c, data.get("project_label", "RUNCPM REVIEW"), "FINAL LINKS")
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(54, H - 112, "Final links")
    c.setFont("Helvetica", 12.5)
    c.drawString(54, H - 152, "Voice note and resources are attached for review.")

    cards = [("Voice note", data.get("voice_url")), ("Resources", data.get("resources_url"))]
    y = 450
    for title, url in cards:
        draw_round_rect(c, 88, y, 436, 72, r=18, fill=colors.white, stroke=BORDER, sw=0.65)
        draw_external_link_icon(c, 112, y + 31, size=13, bg=colors.white)
        c.setFillColor(BLUE)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(134, y + 31, title)
        if url:
            c.linkURL(url, (88, y, 524, y + 72), relative=0)
        y -= 92

    draw_footer(c, page_num, data.get("voice_url"), data.get("resources_url"))
    c.showPage()


def render(data: dict, out_path: str):
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out), pagesize=LETTER)
    c.setTitle(data.get("title", "Review PDF"))
    draw_page_one(c, data)
    page_num = 2
    for item in data.get("pages", []):
        draw_content_page(c, page_num, data, item)
        page_num += 1
    draw_final_page(c, page_num, data)
    c.save()
    if not out.read_bytes().startswith(b"%PDF"):
        raise RuntimeError(f"Output is not a PDF: {out}")
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: render_review_pdf.py content.json output.pdf", file=sys.stderr)
        return 2
    data = json.loads(Path(argv[1]).read_text())
    out = render(data, argv[2])
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
