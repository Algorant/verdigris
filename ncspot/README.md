# Verdigris for ncspot

Verdigris is available as a custom ncspot terminal Spotify-client theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/ncspot/.config/ncspot/config.toml
```

Loaded at runtime via the symlinked live config:

```text
~/.config/ncspot/config.toml
```

## Shape

ncspot exposes a compact set of semantic TUI theme roles. The current port keeps terminal transparency enabled while grounding the UI in Verdigris colors:

```css
:root {
  --ncspot-background: default;
  --ncspot-primary: #ebdbb2;
  --ncspot-secondary: #d4be9a;
  --ncspot-title: #e6bf86;
  --ncspot-playing: #83a598;
  --ncspot-playing-bg: #1d2021;
  --ncspot-highlight: #689d6a;
  --ncspot-highlight-bg: #1d2021;
  --ncspot-statusbar: #ebdbb2;
  --ncspot-statusbar-progress: #8ec07c;
  --ncspot-statusbar-bg: #3c3836;
  --ncspot-cmdline: #1d2021;
  --ncspot-cmdline-bg: #e6bf86;
  --ncspot-search-match: #e6bf86;
}
```

## Notes

- This is a complete ncspot `[theme]` port, replacing the earlier Gruvbox-derived colors.
- Background remains `default` for terminal transparency; the intended solid fallback is `#1d2021`.
- Vellum `#ebdbb2` is the primary foreground.
- Ochre `#e6bf86` is used for block titles such as `Library`, command-line background, and search matches.
- Aqua `#83a598` marks the currently playing track.
- Patina `#689d6a` handles selection/highlight emphasis.
- Fern `#8ec07c` is reserved for progress to keep playback state distinct from title/search emphasis.
- Red remains reserved for error backgrounds.

ncspot is a compact semantic TUI port: it keeps the original layout readable while moving titles and interactive accents into Verdigris ochre, aqua, fern, and patina roles.
