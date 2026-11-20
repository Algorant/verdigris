# build

Image tools for the repository's images, the fastfetch logo marks and the
Showcase gallery thumbnails. They write PNG, SVG and JPEG images only, never
theme files; each needs ImageMagick 7 (`magick`), and the logo scripts also need
python3 and librsvg (`rsvg-convert`).

- `thumbs.sh` — regenerates every Showcase gallery thumbnail from its full-size screenshot. README.md's `<a href>`/`<img src>` pairs are the input list; each thumbnail is written back to its existing path as one 880x550 frame (the screenshots fitted whole on the palette background colour), 4.4x the 200 CSS px gallery cell, JPEG 4:4:4 q85. It hashes every source before and after and fails if an original changed.
- `mask_from_grid.py` — turns a pixel-grid PNG (Omarchy's `icon.png`, 20px cells) into an exact single-color SVG mask filled with `currentColor`, and checks the mask renders back to the source alpha.
- `render_logos.py` — renders that mask in named palette colors from `palette/verdigris.json`, writing `apps/fastfetch/logos/omarchy-verdigris-COLOR.png` for each color plus the `omarchy-verdigris-preview.png` sheet.
