# Verdigris logos

![Omarchy mark in seven Verdigris colors](./omarchy/omarchy-verdigris-preview.png)

Single-color logo marks recolored with named Verdigris palette colors, plus the
scripts and steps that produce them. Colors always come from
[`../css/palette.json`](../css/palette.json), so a palette release can be
re-rendered instead of hand-edited.

| Set | Source | Colors | Used by |
|---|---|---|---|
| [`omarchy/`](./omarchy/) | Omarchy `icon.png` (MIT, see [`omarchy/LICENSE`](./omarchy/LICENSE)) | aqua, ashbronze, fern, moss, ochre, patina, vellum | Fastfetch on Omarchy machines |

## Requirements

Python 3, ImageMagick 7 (`magick`) and librsvg (`rsvg-convert`). No Python packages.

## Reproduce the Omarchy set

Omarchy's `/usr/share/omarchy/icon.png` (Omarchy 4.0.4) is a 300px pixel-grid
icon: 15×15 cells of 20px, binary alpha. `mask-from-grid.py` rebuilds it as exact
rectangles and verifies the SVG against the source (0 differing pixels);
`render.py` recolors that mask at 2100px (140px per cell, so edges stay perfectly
hard).

```sh
cd logos
./mask-from-grid.py /usr/share/omarchy/icon.png 20 omarchy/omarchy-mark.svg
./render.py omarchy/omarchy-mark.svg omarchy omarchy 2100 \
  aqua,ashbronze,fern,moss,ochre,patina,vellum
```

## Recolor another logo

1. **Get a single-color mask.**
   - A pixel-grid icon: find its cell size and run `mask-from-grid.py`. It fails
     if the cell size is wrong.
   - A vector logo: take the official SVG, merge it to one color and set
     `fill="currentColor"`.
   - Anything else: trace a high-resolution silhouette (for example with
     potrace) and clean it up by hand.
2. **Normalize the mask.** Tight `viewBox` with no padding, transparent
   background, `currentColor` fill. Padding shrinks the visible mark wherever it
   is displayed.
3. **Render.** Choose a square size that is an integer multiple of the grid, if
   there is one (about 2000px is plenty), and name the colors from
   `palette.json`. `render.py` sets transparent pixels to the fill color so
   downscaling never adds dark fringes, and writes a preview sheet.
4. **Check the preview**, then commit the mask, the PNGs and the preview together.

## Displaying in Fastfetch

Verified with Fastfetch 2.68.1 in Ghostty 1.3.1 on Hyprland (output scale 1.25):

```jsonc
"logo": {
  "type": "kitty",
  "source": "$(ls ~/path/to/omarchy-verdigris/*.png | shuf -n 1)",
  "height": 7,
  "padding": { "top": 2, "left": 1, "right": 2 }
}
```

- `kitty` mode resizes the PNG once with ImageMagick and Ghostty draws it 1:1.
  Setting only `height` lets Fastfetch derive the width from the square image,
  so nothing is stretched. `preserveAspectRatio` applies to iTerm only.
- Seven rows with top padding 2 span the seven info rows of a compact config.
  A square mark that fills its box reads heavier than a triangle such as the
  Arch logo, so it wants fewer rows than an 18×8 Arch icon.
- Fastfetch caches resized logos under `~/.cache/fastfetch/images/<path>/<W*H>/`
  and never checks whether the file changed. After re-rendering in place, delete
  that cache (or run once with `--logo-recache true`), or the old pixels stay.
