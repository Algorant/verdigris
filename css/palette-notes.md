# Verdigris palette notes

These notes track the canonical Verdigris identity palette, the additional colors, and the design intent behind both.

Current palette version: `0.1.2`. See [`../CHANGELOG.md`](../CHANGELOG.md) for release history.

## Canonical core palette

The core palette is the first-class Verdigris identity set. Keep it compact and cohesive.

```css
:root {
  --verdigris-ashbronze: #665c54;
  --verdigris-vellum: #ebdbb2;
  --verdigris-fern: #8ec07c;
  --verdigris-patina: #689d6a;
  --verdigris-aqua: #83a598;
  --verdigris-ochre: #e6bf86;
}
```

| Name | Hex | Role |
|---|---:|---|
| ashbronze | `#665c54` | background / weathered metal |
| vellum | `#ebdbb2` | foreground / warm text |
| fern | `#8ec07c` | bright green accent |
| patina | `#689d6a` | primary green |
| aqua | `#83a598` | cool aqua accent |
| ochre | `#e6bf86` | warm brass accent |

## Additional Colors

These extended colors are available for ports that need specific roles outside the core identity palette: ANSI slots, syntax roles, semantic diagnostics, diffs, warnings, search highlights, or app-specific cases that need more than the six core colors.

```css
:root {
  --verdigris-moss: #70764a;
  --verdigris-teal: #458588;
  --verdigris-oxblood: #74363d;
  --verdigris-goldenrod: #b8863b;
  --verdigris-deep-copper: #b9805f;
  --verdigris-ink-violet: #8989b0;
}
```

| Name | Hex | Role |
|---|---:|---|
| moss | `#70764a` | muted olive / additions / success |
| teal | `#458588` | secondary blue-teal |
| oxblood | `#74363d` | deep red for removals / errors |
| goldenrod | `#b8863b` | muted gold for warnings / search |
| deep-copper | `#b9805f` | muted copper for changes / caution |
| ink-violet | `#8989b0` | readable violet for rare / special accents |

Goldenrod uses `#b8863b` for warning/search roles. Deep copper uses `#b9805f` for caution/change roles, and ink violet uses `#8989b0` for rare/special accents.

Machine-readable source: [`palette.json`](./palette.json)

Visual swatches:

- Core: [`../_images/verdigris-core-swatch.svg`](../_images/verdigris-core-swatch.svg)
- Additional Colors: [`../additional-colors/verdigris-additional-colors-swatch.svg`](../additional-colors/verdigris-additional-colors-swatch.svg)

## Trial colors

```css
:root {
  --verdigris-ochre-alt: #d8a65c;
  --verdigris-brown-green-liked: #604b29;
  --verdigris-dark-ochre-trial: #8b6021;
}
```

- `#d8a65c` was the previous Obsidian ochre and remains useful as a deeper app-specific brass.
- `#604b29` is a liked brownish-green candidate; not part of the canonical 6+6 set.
- `#8b6021` was tested as H3/tag color in Obsidian and felt too dark there, but may be useful as a dark yellow/brown variant.

## Decisions

- The first-class Verdigris identity palette is now six colors: ashbronze, vellum, fern, patina, aqua, and ochre.
- `moss` moved out of the core set into Additional Colors so the base identity stays tighter and more cohesive.
- `ashbronze` and `vellum` provide the weathered-metal / warm-text grounding.
- `fern`, `patina`, and `aqua` are the main identity accents.
- `ochre` is `#e6bf86`: a lighter brass accent used in Starship, Pi, and Herdr.
- `teal` is the alternate blue used by Obsidian, Ghostty, and Neovim-style roles.
- `oxblood` is `#74363d`, a dark mineral red selected for removals/errors and as the palette's primary red shade.
- Oxblood replaces the previous coral-like `diff-red` (`#e36f63`) in palette version `0.1.0`. Existing ports may migrate separately.
- `goldenrod` is `#b8863b`, a darker muted gold selected for warning/search roles while retaining normal-text readability on dark note surfaces.
- Goldenrod replaces the previous `yellow` (`#d29a46`) in palette version `0.1.2`. Existing ports may migrate separately.
- `deep-copper` is `#b9805f`, a muted copper selected for caution/change roles and readable category labels on dark note surfaces.
- Deep copper replaces the previous `orange` (`#c96f3d`) in palette version `0.1.1`. Existing ports may migrate separately.
- `ink-violet` is `#8989b0`, a readable violet selected for special/rare roles.
- Ink violet replaces the previous `purple` (`#ad8294`) in palette version `0.1.2`. Existing ports may migrate separately.

## Earlier exploration notes

Earlier Obsidian experiments used Gruvbox-grounded colors such as `#282828`, `#fbf1c7`, `#bdae93`, `#458588`, `#8c945c`, and `#d79921`. Those colors may still be useful as derived app-specific colors; `#458588` remains directly in Additional Colors, alongside goldenrod `#b8863b`, deep copper `#b9805f`, and ink violet `#8989b0`.
