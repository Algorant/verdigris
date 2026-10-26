# Verdigris for Atuin

Verdigris is available as a custom Atuin TUI theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/atuin/.config/atuin/themes/verdigris.toml
```

Enabled from:

```text
~/.dotfiles/atuin/.config/atuin/config.toml
```

## Shape

Atuin themes map semantic UI meanings to colors. The dotfiles theme derives from Atuin's `autumn` theme and overrides the Verdigris-relevant roles:

```css
:root {
  --atuin-base: #ebdbb2;
  --atuin-title: #8ec07c;
  --atuin-important: #e6bf86;
  --atuin-guidance: #83a598;
  --atuin-annotation: #928374;
  --atuin-muted: #665c54;
  --atuin-alert-info: #689d6a;
  --atuin-alert-warn: #e6bf86;
  --atuin-alert-error: #fb4934;
}
```

## Notes

- Atuin custom themes require a TOML file with `[theme]` metadata and a `[colors]` table.
- The active theme is selected in `config.toml` with `[theme] name = "verdigris"`.
- The theme file uses `parent = "autumn"` so unspecified meanings fall back to Atuin's warmer built-in theme.
- Vellum `#ebdbb2` is the base text color.
- Fern `#8ec07c` is used for titles and active labels.
- Ochre `#e6bf86` is used for important and warning text.
- Aqua `#83a598` is used for guidance/prompts/hints.
- Patina `#689d6a` is used for informational alerts.
- Ashbronze `#665c54` is muted/low-emphasis UI.

Atuin is a semantic TUI port: it maps Verdigris colors to Atuin's meaning roles rather than defining a full terminal palette.
