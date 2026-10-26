#!/usr/bin/env python3
"""Rebuild a pixel-grid icon as an exact single-color SVG mask.

The input must be a PNG whose alpha channel is made of uniform square cells of
UNIT pixels (for example Omarchy's icon.png: 300px, 20px cells). Each opaque row
run becomes one <rect>, filled with currentColor so render.py can recolor it.
The script fails if any cell is not uniform, then verifies that the SVG rendered
back at the original size matches the source alpha exactly.

Requires: ImageMagick 7 (`magick`) and librsvg (`rsvg-convert`).

Usage: mask-from-grid.py SOURCE.png UNIT OUTPUT.svg
"""

import subprocess
import sys
import tempfile
from pathlib import Path


def alpha_bytes(png: Path) -> tuple[int, int, bytes]:
    size = subprocess.run(
        ["magick", "identify", "-format", "%w %h", str(png)],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    width, height = int(size[0]), int(size[1])
    data = subprocess.run(
        ["magick", str(png), "-alpha", "extract", "-depth", "8", "gray:-"],
        capture_output=True, check=True,
    ).stdout
    return width, height, data


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__.strip().splitlines()[-1])
    source, unit, output = Path(sys.argv[1]), int(sys.argv[2]), Path(sys.argv[3])

    width, height, alpha = alpha_bytes(source)
    if width % unit or height % unit:
        sys.exit(f"{source}: {width}x{height} is not a multiple of {unit}px cells")
    cols, rows = width // unit, height // unit

    grid = []
    for gy in range(rows):
        row = []
        for gx in range(cols):
            cell = {
                alpha[y * width + x]
                for y in range(gy * unit, gy * unit + unit)
                for x in range(gx * unit, gx * unit + unit)
            }
            if len(cell) != 1:
                sys.exit(f"{source}: cell ({gx},{gy}) is not uniform; wrong UNIT?")
            row.append(cell.pop() > 127)
        grid.append(row)

    rects = []
    for y, row in enumerate(grid):
        x = 0
        while x < cols:
            if row[x]:
                start = x
                while x < cols and row[x]:
                    x += 1
                rects.append(f'<rect x="{start}" y="{y}" width="{x - start}" height="1"/>')
            else:
                x += 1

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols} {rows}" '
        f'width="{cols}" height="{rows}" shape-rendering="crispEdges">'
        f'<g fill="currentColor">{"".join(rects)}</g></svg>\n'
    )

    with tempfile.TemporaryDirectory() as tmp:
        check = Path(tmp) / "check.png"
        subprocess.run(
            ["rsvg-convert", "-w", str(width), "-h", str(height), str(output), "-o", str(check)],
            check=True,
        )
        _, _, rendered = alpha_bytes(check)
    differing = sum(a != b for a, b in zip(alpha, rendered))
    if differing:
        sys.exit(f"{output}: {differing} pixels differ from {source}")
    print(f"{output}: {cols}x{rows} grid, {len(rects)} rects, 0 differing pixels")


if __name__ == "__main__":
    main()
