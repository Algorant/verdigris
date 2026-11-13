# build

Two things live here, both plain scripts with no dependencies beyond python3.

- `generate.py` — reads `palette/verdigris.json` and writes the app files that are pure derivations of it: ghostty, foot, chromium, claude-code and hyprland. Running it twice changes nothing.
- `mask_from_grid.py` and `render_logos.py` — rebuild the omarchy mark raster the fastfetch port uses, in every palette color.
- `generate-spotifast.py` — reads the same palette and writes `apps/spotifast/verdigris.json`, the file Spotifast loads from its themes folder, with the colors Omarchy's own template renders for it. Running it twice changes nothing.
