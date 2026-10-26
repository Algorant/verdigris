# Verdigris for btop

Verdigris is available as a custom btop resource-monitor theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/btop/.config/btop/themes/verdigris.theme
```

Enabled from:

```text
~/.dotfiles/btop/.config/btop/btop.conf
```

## Shape

```css
:root {
  --btop-bg: #1d2021;
  --btop-fg: #ebdbb2;
  --btop-title: #ebdbb2;
  --btop-shortcut-hint: #8ec07c;
  --btop-selected-bg: #665c54;
  --btop-selected-fg: #fbf1c7;
  --btop-inactive: #3c3836;
  --btop-graph-text: #d4be9a;
  --btop-proc-misc: #83a598;
  --btop-box: #665c54;
  --btop-divider: #3c3836;

  --btop-cpu-start: #689d6a;
  --btop-cpu-mid: #e6bf86;
  --btop-cpu-end: #fb4934;

  --btop-free-start: #70764a;
  --btop-free-end: #8ec07c;
  --btop-cached-start: #458588;
  --btop-cached-end: #83a598;
  --btop-available-start: #604b29;
  --btop-available-end: #e6bf86;
  --btop-used-start: #604b29;
  --btop-used-mid: #8b6021;
  --btop-used-end: #cc241d;
}
```

## Notes

- btop themes are `.theme` files under `~/.config/btop/themes/`.
- The dotfiles config sets `color_theme = "verdigris"` and keeps `truecolor = true`.
- Background uses the readable dark base `#1d2021`.
- Main text/title use vellum `#ebdbb2`.
- Box borders and selection background use ashbronze `#665c54`.
- Shortcut hints use fern `#8ec07c` so key hints are distinct from normal vellum text.
- CPU and temperature gradients use patina/aqua through ochre into red.
- Used memory/disk meters avoid beige-to-red and instead move brown-green → dark ochre → red.
- Network download leans patina/aqua; upload leans brown-green/ochre/purple.

btop is a graph-heavy TUI port, so Verdigris is expanded into practical gradients rather than only the core palette.
