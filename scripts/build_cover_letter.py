"""Render the editorial cover letter separately from the anonymous manuscript."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript/submission/cover-letter.txt"
APPENDIX = "Author Information and Declarations"
LABELS = {
    "Manuscript title", "Authors and affiliations", "Correspondence",
    "Author contributions", "Conflicts of interest",
}


def build(destination: Path, font_dir: Path) -> None:
    for name, filename in (
        ("LetterTimes", "times.ttf"),
        ("LetterTimes-Bold", "timesbd.ttf"),
        ("LetterTimes-Italic", "timesi.ttf"),
    ):
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily(
        "LetterTimes", normal="LetterTimes", bold="LetterTimes-Bold",
        italic="LetterTimes-Italic", boldItalic="LetterTimes-Bold",
    )
    body = ParagraphStyle(
        "Body", fontName="LetterTimes", fontSize=11, leading=14,
        spaceAfter=9, alignment=TA_LEFT,
    )
    left = ParagraphStyle("Left", parent=body, alignment=TA_LEFT)
    heading = ParagraphStyle(
        "Heading", parent=left, fontName="LetterTimes-Bold",
        fontSize=14, leading=18, spaceAfter=18, keepWithNext=True,
    )

    text = SOURCE.read_text(encoding="utf-8").strip()
    if text.count(APPENDIX) != 1:
        raise ValueError("Expected one author-information page heading")
    story = []
    for block in text.split("\n\n"):
        if block == APPENDIX:
            story.extend([PageBreak(), Paragraph(APPENDIX, heading)])
            continue
        lines = block.splitlines()
        if lines[0] in LABELS:
            rendered = "<b>" + escape(lines[0]) + "</b><br/>"
            rendered += "<br/>".join(escape(line) for line in lines[1:])
            story.append(Paragraph(rendered, left))
        else:
            rendered = "<br/>".join(escape(line) for line in lines)
            style = left if len(lines) > 1 or len(block) < 90 else body
            story.append(Paragraph(rendered, style))

    def footer(canvas, document):
        canvas.saveState()
        canvas.setFont("LetterTimes", 9)
        canvas.setFillColor(colors.HexColor("#666666"))
        canvas.drawCentredString(A4[0] / 2, 15 * mm, str(document.page))
        canvas.restoreState()

    destination.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(destination), pagesize=A4,
        leftMargin=25 * mm, rightMargin=25 * mm,
        topMargin=23 * mm, bottomMargin=23 * mm,
        title="Cover letter - Blockchains",
        author="Chengnian Long",
        subject="Review submission: Blockchain-Assisted Mission Trust in Air-Surface-Underwater Unmanned Systems",
        pageCompression=1,
    )
    document.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Built cover letter: {destination}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output", nargs="?", type=Path,
        default=ROOT / "output/pdf/cover-letter-blockchains.pdf",
    )
    parser.add_argument(
        "--font-dir", type=Path,
        default=Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts",
        help="Directory containing times.ttf, timesbd.ttf, and timesi.ttf",
    )
    arguments = parser.parse_args()
    build(arguments.output.resolve(), arguments.font_dir)
