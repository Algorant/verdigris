#!/usr/bin/env python3
"""Render a single-color SVG mask in named Verdigris palette colors.

The mask must use fill="currentColor" (see mask-from-grid.py). Colors are looked
up by name in ../css/palette.json (core and extended), never hard-coded. Each
PNG is square, SIZE pixels, with transparent pixels set to the fill color so
resampling can never introduce dark fringes. A preview sheet is written too.

Requires: ImageMagick 7 (`magick`) and librsvg (`rsvg-convert`).

Usage: render.py MASK.svg OUTDIR NAME SIZE COLOR[,COLOR...]
Writes OUTDIR/NAME-verdigris-COLOR.png and OUTDIR/NAME-verdigris-preview.png.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

PALETTE = Path(__file__).resolve().parent.parent / "css" / "palette.json"


def palette() -> dict[str, str]:
    data = json.loads(PALETTE.read_text())
    return {c["name"]: c["hex"] for c in data["colors"] + data["extended"]}


def main() -> None:
    if len(sys.argv) != 6:
        sys.exit(__doc__.strip().splitlines()[-2])
    mask, outdir, name, size = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    names = sys.argv[5].split(",")

    colors = palette()
    unknown = [n for n in names if n not in colors]
    if unknown:
        sys.exit(f"not in {PALETTE}: {', '.join(unknown)}")

    svg = mask.read_text()
    if "currentColor" not in svg:
        sys.exit(f"{mask}: expected fill=\"currentColor\"")

    outdir.mkdir(parents=True, exist_ok=True)
    outputs = []
    with tempfile.TemporaryDirectory() as tmp:
        for color in names:
            hexcode = colors[color]
            colored = Path(tmp) / f"{color}.svg"
            colored.write_text(svg.replace("currentColor", hexcode))
            png = outdir / f"{name}-verdigris-{color}.png"
            subprocess.run(
                ["rsvg-convert", "-w", str(size), "-h", str(size), str(colored), "-o", str(png)],
                check=True,
            )
            subprocess.run(
                ["magick", str(png), "-background", hexcode, "-alpha", "background",
                 "-define", "png:color-type=6", str(png)],
                check=True,
            )
            outputs.append(png)
            print(png)

    preview = outdir / f"{name}-verdigris-preview.png"
    subprocess.run(
        ["magick", "montage", *map(str, outputs), "-background", "#1d2021",
         "-geometry", "256x256+32+32", "-tile", f"{len(outputs)}x1", "-depth", "8", str(preview)],
        check=True,
    )
    print(preview)


if __name__ == "__main__":
    main()
