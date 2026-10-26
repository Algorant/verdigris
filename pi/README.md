# Verdigris for Pi

Verdigris is available as a Pi coding-agent theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/pi/.pi/agent/themes/verdigris.json
```

## Shape

```css
:root {
  --pi-bg: #1d2021;
  --pi-fg: #ebdbb2;
  --pi-muted: #928374;
  --pi-accent: #8ec07c;
  --pi-accent-dark: #689d6a;
  --pi-secondary: #83a598;
  --pi-ochre: #e6bf86;
}
```

## Notes

- Pi stays closer to Gruvbox dark backgrounds for transcript readability.
- `fern` is the primary accent.
- `patina` is used for code block borders and darker accent roles.
- `aqua` is used for links/user-message style emphasis.
- Canonical ochre `#e6bf86` is used for warnings.
- Red and green remain available for errors/diffs/success states.

Pi is a UI/document-reading port, so it prioritizes muted panels and readable markdown over showing the full palette at once.
