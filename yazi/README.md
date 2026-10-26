# Verdigris for Yazi

Verdigris is available as a custom Yazi terminal file-manager theme in the dotfiles.

Source in dotfiles:

```text
~/.dotfiles/yazi/.config/yazi/theme.toml
```

Yazi loads the theme automatically from its config directory:

```text
~/.dotfiles/yazi/.config/yazi/
```

## Shape

Yazi themes map manager chrome, status segments, prompts, help, permissions, filetype rules, and icons to styled colors:

```css
:root {
  --yazi-cwd: #83a598;
  --yazi-hover-bg: #83a598;
  --yazi-hover-fg: #1d2021;
  --yazi-border: #665c54;

  --yazi-find-keyword: #8ec07c;
  --yazi-find-position: #e6bf86;
  --yazi-marker-selected: #8ec07c;
  --yazi-marker-cut: #fb4934;

  --yazi-mode-normal-fg: #ebdbb2;
  --yazi-mode-normal-bg: #665c54;
  --yazi-mode-select-bg: #8ec07c;
  --yazi-mode-unset-bg: #e6bf86;
  --yazi-progress-label: #ebdbb2;
  --yazi-progress-normal: #83a598;

  --yazi-permission-read: #8ec07c;
  --yazi-permission-write: #e6bf86;
  --yazi-permission-exec: #8ec07c;
  --yazi-permission-special: #665c54;

  --yazi-help-key: #e6bf86;
  --yazi-help-exec: #83a598;
  --yazi-help-desc: #928374;

  --yazi-image: #83a598;
  --yazi-media: #8ec07c;
  --yazi-archive: #e6bf86;
  --yazi-directory: #83a598;
  --yazi-fallback: #ebdbb2;
  --yazi-folder-icon: #689d6a;
}
```

## Notes

- This is a direct Yazi `theme.toml` port, not a terminal ANSI-only theme.
- The previous theme was Gruvbox-derived; bright Gruvbox yellow/orange/green roles were shifted into Verdigris fern, ochre, and aqua.
- Patina `#689d6a` is used for folder icons so directories read as Verdigris green instead of Yazi's default bright blue.
- Aqua `#83a598` is used for current-directory, hovered selection, directory names, image files, command names, and other navigational affordances.
- Fern `#8ec07c` is used for selection markers, search hits, media files, and readable/active permission roles.
- Ochre `#e6bf86` is used for positions, archive files, write permissions, mode warnings, and important help/key text.
- Vellum `#ebdbb2` is used for regular filenames, primary status text, and normal-mode status contrast.
- Ashbronze `#665c54` handles borders, inactive separators, low-emphasis structural UI, and the normal-mode status pill.
- Red remains reserved for destructive/cut/error states.

Yazi is a semantic TUI port: it keeps file-manager state legible while replacing Gruvbox's brighter accents with Verdigris identity colors.
