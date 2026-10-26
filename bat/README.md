# Verdigris for bat

Verdigris is available as a custom `bat` syntax-highlighting theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/bat/.config/bat/themes/Verdigris.tmTheme
```

Enabled from:

```text
~/.dotfiles/bat/.config/bat/config
```

## Cache and troubleshooting

`bat` does not discover custom themes directly from `~/.config/bat/themes` at runtime. It compiles custom assets into the cache reported by `bat --cache-dir`.

If `bat` prints this warning, even when `Verdigris.tmTheme` exists:

```text
[bat warning]: Unknown theme 'Verdigris', using default.
```

rebuild the cache:

```sh
bat cache --build
```

Then verify the theme is registered:

```sh
bat --list-themes | grep Verdigris
```

Useful diagnostics:

```sh
bat --config-file
bat --config-dir
bat --cache-dir
bat --diagnostic
```

This matters on first install, after editing `Verdigris.tmTheme`, after copying/stowing the dotfiles onto a new machine, and anywhere `cat` is aliased or wrapped to `bat`.

## Shape

`bat` themes use Sublime Text `.tmTheme` XML/plist files. The dotfiles theme defines global editor colors plus TextMate scopes for syntax highlighting:

```css
:root {
  --bat-bg: #1d2021;
  --bat-fg: #ebdbb2;
  --bat-line-highlight: #222526;
  --bat-selection: #3c3836;
  --bat-gutter: #928374;
  --bat-gutter-added: #8ec07c;
  --bat-gutter-modified: #e6bf86;
  --bat-gutter-deleted: #fb4934;

  --bat-comment: #928374;
  --bat-string: #8ec07c;
  --bat-keyword: #689d6a;
  --bat-function: #e6bf86;
  --bat-type: #83a598;
  --bat-operator: #83a598;
  --bat-number: #d8a65c;
  --bat-invalid: #fb4934;
}
```

## Notes

- The active theme is selected in `config` with `--theme="Verdigris"`.
- After installing or changing the theme, rebuild bat's cache with `bat cache --build`; otherwise `--theme="Verdigris"` can warn that the theme is unknown and fall back to default.
- Background uses Verdigris `bg0` `#1d2021` instead of core ashbronze so long code views stay readable and consistent with terminal/editor ports.
- Vellum `#ebdbb2` is the default foreground.
- Fern `#8ec07c` is used for strings and inserted diff markup.
- Patina `#689d6a` is used for keywords/storage.
- Aqua `#83a598` is used for types, operators, links, and escapes.
- Ochre `#e6bf86` is used for functions, warnings, and emphasis.
- Comments and gutter metadata use muted Gruvbox/Verdigris support tones.
- Red is reserved for invalid scopes and deleted diff markup.

The bat port is a syntax-theme expansion of Verdigris: it maps TextMate scopes onto the compact palette and nearby support colors rather than adding new canonical colors.
