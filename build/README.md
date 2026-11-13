# build

Image tools for the fastfetch logo marks. They write PNG and SVG images only, never theme files; each needs python3 plus ImageMagick 7 (`magick`) and librsvg (`rsvg-convert`).

- `mask_from_grid.py` — turns a pixel-grid PNG (Omarchy's `icon.png`, 20px cells) into an exact single-color SVG mask filled with `currentColor`, and checks the mask renders back to the source alpha.
- `render_logos.py` — renders that mask in named palette colors from `palette/verdigris.json`, writing `apps/fastfetch/logos/omarchy-verdigris-COLOR.png` for each color plus the `omarchy-verdigris-preview.png` sheet.
