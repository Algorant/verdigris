# verdigris for neovim

TUI editor. My editor on every machine.

## install

The colourscheme is its own plugin: [Algorant/verdigris.nvim](https://github.com/Algorant/verdigris.nvim). Install it with your plugin manager and set `colorscheme verdigris`.

```lua
{ "Algorant/verdigris.nvim", lazy = false, priority = 1000, config = function() vim.cmd.colorscheme("verdigris") end }
```

## notes

Dark only. The plugin owns the highlight groups; this folder is the catalogue entry and the palette it follows.

The editor runs the real plugin from Algorant/verdigris.nvim, cloned into the capture sandbox, over a fixture module.
