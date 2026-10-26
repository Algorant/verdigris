# Verdigris for Herdr

Herdr currently uses Verdigris overrides on top of its built-in Gruvbox theme.

Source in dotfiles:

```text
~/.dotfiles/herdr/.config/herdr/config.toml
```

## Shape

```css
:root {
  --herdr-accent: #e6bf86;
  --herdr-yellow: #e6bf86;
  --herdr-green: #8ec07c;
  --herdr-teal: #8ec07c;
  --herdr-blue: #83a598;
  --herdr-mauve: #83a598;
  --herdr-peach: #e6bf86;
  --herdr-text: #ebdbb2;
}
```

## Notes

- Herdr is not a full standalone palette yet; it is a small override layer using gruvbox as a default.
- Canonical ochre `#e6bf86` drives active borders, working/running, warning, and interrupted states.
- Fern `#8ec07c` is used for done/idle/positive states.
- Aqua `#83a598` carries git-change/cool notification/special label roles.
- Vellum `#ebdbb2` is the main text color.
