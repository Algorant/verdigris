# Verdigris for Obsidian

The Verdigris Obsidian look is delivered as a **single Minimal-compatible CSS
snippet** that is the authoritative source of truth:

- `verdigris-minimal.css` — canonical snippet. Layered on top of the Minimal
  theme, it sets Minimal's CSS variables directly and unconditionally.

This replaces the previous brittle setup where the look depended on Style
Settings plugin data (`obsidian-style-settings/data.json`). See
`consolidation-options.md` (Option 2 was adopted).

## Why the snippet, not Style Settings

Style Settings only emits CSS for option IDs that the *currently installed*
Minimal version registers, scoped to `body.theme-dark.css-settings-manager`
(high specificity). Consequences observed in the live vault:

- Stored keys whose IDs don't match the installed Minimal become **dead
  config**; the variable silently falls back to Minimal's default.
- Different Minimal versions across machines apply **different subsets** of the
  same `data.json`, so the look drifts per device.
- The plugin's in-memory state and on-disk `data.json` could disagree.

A snippet sets the variables on `body.theme-dark` directly, so the result is
identical on every machine where the file is synced and enabled.

## Current visual direction

Gruvbox-grounded base with Verdigris accents (intentionally warmer/darker than
the early hard-Verdigris background experiment):

```css
:root {
  --obsidian-bg: #282828;        /* gruvbox-grounded base */
  --obsidian-bg-alt: #1e2021;
  --obsidian-fg: #fbf1c7;
  --obsidian-h1: #689d6a;        /* patina */
  --obsidian-h2: #83a598;        /* aqua */
  --obsidian-h3: #d8a65c;        /* deep app-specific brass */
  --obsidian-h4: #70764a;        /* extended moss */
  --obsidian-link-resolved: #8ec07c;   /* fern, solid, no underline */
  --obsidian-link-hover: #83a598;      /* aqua */
  --obsidian-link-unresolved: #689d6a; /* patina @ 80%, solid, no underline */
  --obsidian-link-external: #458588;   /* teal, distinct from internal */
  --obsidian-tag: #d8a65c;
  --obsidian-canonical-ochre: #e6bf86;
}
```

## Link states (resolved the green-on-green ambiguity)

Mapping **B — all-green, missing dimmed + dashed**:

| State | Color | Treatment |
|---|---|---|
| Resolved / existing | fern `#8ec07c` | solid, no underline |
| Hover | aqua `#83a598` | — |
| Unresolved / missing | patina `#689d6a` | 80% opacity, no underline |
| External | teal `#458588` | distinct from internal |

Unresolved links are pinned with explicit selectors for both reading mode and
Live Preview, because the core `--link-unresolved-*` variables alone don't
reliably restyle the editor.

## Notes

- Minimal remains the base theme; the snippet only sets variables.
- `--v-ochre-deep` (`#d8a65c`) drives tags/H3. Set it to `var(--v-ochre)`
  (`#e6bf86`) to use the canonical brass instead.
- Heading sizes are pinned in the snippet (`h1` is currently `1.4em`).
- File-explorer rename text is pinned to the normal foreground. This avoids a
  Minimal `Colorful active states` interaction that otherwise renders dark text
  on the unfilled dark rename field.
- Style Settings is no longer required for Verdigris.
- Drift check/apply helper: `~/.dotfiles/obsidian/sync-verdigris.py`.

## Install on a machine

1. Copy `verdigris-minimal.css` into `<vault>/.obsidian/snippets/`.
2. Appearance → CSS snippets → enable **verdigris-minimal**.
3. Obsidian Sync: enable the **Appearance** sync category (themes, snippets,
   CSS, and the enabled-snippet state) on every device so 1 & 2 propagate.

## Files

- `verdigris-minimal.css` — canonical Minimal-compatible snippet.
- `consolidation-options.md` — packaging approaches (Option 2 adopted).
