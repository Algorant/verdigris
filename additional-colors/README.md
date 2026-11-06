# Additional Colors

Palette version: `0.2.0`

![Verdigris additional colors](./verdigris-additional-colors-swatch.svg)

The core Verdigris palette is intentionally small. These additional colors are the extended set for ports that need specific roles outside the core identity palette: diffs, warnings, search highlights, diagnostics, ANSI slots, or syntax accents.


| Name | Hex | Role |
|---|---:|---|
| moss | `#70764a` | additions / success |
| teal | `#458588` | secondary blue-teal |
| oxblood | `#74363d` | removals / errors |
| goldenrod | `#b8863b` | warnings / search |
| deep-copper | `#b9805f` | changes / caution |
| ink-violet | `#8989b0` | rare / special accent |

### Oxblood tints

Oxblood `#74363d` is a fill color: bars, meters, removed-line bands and badge backgrounds under vellum text. It is too dark to read as text on Verdigris backgrounds, so red text uses its supporting tints:

| Name | Hex | Role |
|---|---:|---|
| oxblood-text | `#c66f70` | red text, labels, status dots, error/deletion/cut markers, ANSI red (1) |
| oxblood-bright | `#d47b7c` | ANSI bright red (9) |

## Examples

##todo add examples from nvim, obsidian, diffs showing the additional colors.

