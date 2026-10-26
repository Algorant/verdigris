# Verdigris for Ghostty

Verdigris is available as a custom Ghostty terminal theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/ghostty/.config/ghostty/themes/Verdigris
```

Enabled from:

```text
~/.dotfiles/ghostty/.config/ghostty/config
```

## Shape

```css
:root {
  --ghostty-bg: #1d2021;
  --ghostty-fg: #ebdbb2;
  --ghostty-selection-bg: #665c54;
  --ghostty-selection-fg: #ebdbb2;
  --ghostty-cursor: #ebdbb2;
  --ghostty-cursor-text: #1d2021;

  --ghostty-black: #1d2021;
  --ghostty-red: #cc241d;
  --ghostty-green: #689d6a;
  --ghostty-yellow: #e6bf86;
  --ghostty-blue: #458588;
  --ghostty-magenta: #b16286;
  --ghostty-cyan: #83a598;
  --ghostty-white: #d4be9a;
  --ghostty-bright-black: #928374;
  --ghostty-bright-red: #fb4934;
  --ghostty-bright-green: #8ec07c;
  --ghostty-bright-yellow: #e6bf86;
  --ghostty-bright-blue: #83a598;
  --ghostty-bright-magenta: #d3869b;
  --ghostty-bright-cyan: #8ec07c;
  --ghostty-bright-white: #ebdbb2;
}
```

## Notes

- This started as a conservative port from Ghostty's built-in `Gruvbox Dark Hard` theme.
- Background stays at `#1d2021` for terminal readability and to match the Pi Verdigris UI base.
- Vellum `#ebdbb2` is the main foreground and cursor color.
- Ashbronze `#665c54` is used for selection background.
- ANSI green/yellow/cyan slots are shifted toward Verdigris identity colors: patina, fern, ochre, and aqua.
- This terminal ANSI palette affects tools that render ANSI colors in Ghostty, including Fastfetch palette dots.

Ghostty is a practical terminal palette expansion of the core Verdigris palette, not the canonical palette source.
