# Verdigris for lsd

Verdigris is used as a custom `lsd` color theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/lsd/.config/lsd/colors.yaml
```

Enabled from:

```text
~/.dotfiles/lsd/.config/lsd/config.yaml
```

## Shape

```css
:root {
  --lsd-user: #ebdbb2;
  --lsd-group: #928374;

  --lsd-permission-read: #8ec07c;
  --lsd-permission-write: #e6bf86;
  --lsd-permission-exec: #689d6a;
  --lsd-permission-no-access: #665c54;
  --lsd-permission-octal: #83a598;
  --lsd-permission-context: #70764a;

  --lsd-date-hour-old: #689d6a;
  --lsd-date-day-old: #e6bf86;
  --lsd-date-older: #70764a;

  --lsd-size-none: #665c54;
  --lsd-size-small: #ebdbb2;
  --lsd-size-medium: #d4be9a;
  --lsd-size-large: #e6bf86;

  --lsd-tree-edge: #665c54;
}
```

## Notes

- This is a direct custom `lsd` YAML theme, not a terminal ANSI-only port.
- The previous theme was Gruvbox-derived and had very bright green/yellow timestamps.
- Date colors were shifted toward Verdigris roles:
  - recent files use patina `#689d6a`
  - day-old files use ochre `#e6bf86`
  - older files use moss `#70764a`
- Sizes use vellum/soft foregrounds for normal files and reserve ochre for large files.
- Git statuses use fern for new files, ochre for modified/typechange, aqua for renamed, and red for deleted/conflicted.
- `lsd` may quantize configured hex colors to terminal/ANSI approximations depending on output mode, so exact rendered colors can differ slightly from the YAML values.

The lsd port emphasizes metadata legibility while avoiding bright Gruvbox greens/yellows that clash with Verdigris.
