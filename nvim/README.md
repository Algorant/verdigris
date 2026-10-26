# Verdigris for Neovim

The Neovim colorscheme lives in its own standalone public repository:

<https://github.com/Algorant/verdigris.nvim>

Local development checkout:

```text
~/dev/projects/verdigris.nvim
```

Dotfiles currently load it directly:

```text
~/.dotfiles/nvim/.config/nvim/lua/plugins/colorscheme.lua
```

## Shape

The current Neovim palette is more complete than the core swatch and includes editor-specific neutrals, overlays, diagnostics, and syntax roles.

```css
:root {
  --nvim-bg0: #1d2021;
  --nvim-bg1: #282828;
  --nvim-bg5: #665c54;
  --nvim-fg1: #ebdbb2;
  --nvim-fern: #8ec07c;
  --nvim-aqua: #689d6a;
  --nvim-cyan: #83a598;
  --nvim-teal: #458588;
  --nvim-moss: #70764a;
  --nvim-ochre-current-upstream: #d8a65c;
  --nvim-ochre-lighter: #e6bf86;
}
```

## Notes

- Neovim keeps a neutral Gruvbox-dark base rather than the earlier green-tinted background.
- Fern/aqua are green identity colors.
- Cyan/teal handle cool code/UI accents.
- Moss is rare support.
- The umbrella Verdigris palette now treats `#e6bf86` as canonical ochre; `verdigris.nvim` currently keeps it as `ochre_lighter` while using `#d8a65c` as `ochre`.

This repository links to the Neovim port rather than vendoring it.
