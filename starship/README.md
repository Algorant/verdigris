# Verdigris for Starship

Verdigris is used as a segmented prompt palette in the dotfiles Starship config.

Source in dotfiles:

```text
~/.dotfiles/starship/.config/starship.toml
```

## Shape

Starship uses a fuller terminal palette than the six-color core:

```css
:root {
  --starship-fg0: #fbf1c7;
  --starship-fg1: #ebdbb2;
  --starship-bg0: #141917;
  --starship-bg1: #1d2520;
  --starship-border: #3c3836;
  --starship-border-active: #665c54;
  --starship-aqua: #689d6a;
  --starship-teal: #458588;
  --starship-ochre: #e6bf86;
  --starship-moss: #98971a;
}
```

## Notes

- Prompt segments use darker Verdigris bases than the core swatch to fit terminal contrast.
- Git uses `aqua` / patina green.
- Language/tool runtime segments use teal.
- Docker/visual mode use canonical ochre `#e6bf86`.
- Prompt command mode uses moss.

The Starship palette is a practical terminal expansion of the core palette, not the canonical palette source.
