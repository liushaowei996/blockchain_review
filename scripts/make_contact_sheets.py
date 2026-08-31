"""Build legible PDF page contact sheets for visual QA."""

from pathlib import Path
from PIL import Image, ImageDraw


root = Path("tmp/pdfs/render-final")
pages = sorted(root.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
per_sheet = 6
thumb_w = 410
thumb_h = 580
margin = 24
label_h = 28
for start in range(0, len(pages), per_sheet):
    subset = pages[start:start + per_sheet]
    sheet = Image.new("RGB", (margin * 4 + thumb_w * 3, margin * 3 + (thumb_h + label_h) * 2), "white")
    draw = ImageDraw.Draw(sheet)
    for offset, path in enumerate(subset):
        with Image.open(path) as page:
            page = page.convert("RGB")
            page.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            col, row = offset % 3, offset // 3
            x = margin + col * (thumb_w + margin)
            y = margin + row * (thumb_h + label_h + margin)
            sheet.paste(page, (x + (thumb_w - page.width) // 2, y + label_h))
            number = int(path.stem.split("-")[-1])
            draw.text((x, y), f"Page {number}", fill="black")
    out = root / f"contact-{start // per_sheet + 1:02d}.png"
    sheet.save(out, optimize=True)
print(f"Created {(len(pages) + per_sheet - 1) // per_sheet} contact sheets for {len(pages)} pages")
