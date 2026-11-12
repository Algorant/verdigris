![verdigris](docs/banner.png)

verdigris is a dark mode colorscheme built around oxidized copper: weathered bronze, warm vellum, patina green, cool aqua, brass ochre. 

It is what I use on every machine, ported to the software I actually run.

![verdigris core palette](docs/palette-swatch.svg)

Six core colours carry the scheme: ashbronze metal, vellum text, fern and patina greens, aqua, ochre. Everything else in the palette is a supporting role for one app or one state, listed in [`palette/verdigris.json`](palette/verdigris.json).

## apps

Every app has a folder with its theme file, an install line and screenshots.

| app | type | folder |
| --- | --- | --- |
| omarchy | desktop shell | [apps/omarchy](apps/omarchy) |
| herdr app | GUI | [apps/herdr-app](apps/herdr-app) |
| ghostty | GUI terminal | [apps/ghostty](apps/ghostty) |
| foot | GUI terminal | [apps/foot](apps/foot) |
| chromium | GUI browser | [apps/chromium](apps/chromium) |
| obsidian | GUI notes | [apps/obsidian](apps/obsidian) |
| hokum | GUI notifications | [apps/hokum](apps/hokum) |
| hyprland | compositor | [apps/hyprland](apps/hyprland) |
| neovim | TUI editor | [apps/neovim](apps/neovim) |
| pi | TUI agent harness | [apps/pi](apps/pi) |
| claude code | TUI agent | [apps/claude-code](apps/claude-code) |
| btop | TUI monitor | [apps/btop](apps/btop) |
| atuin | TUI history | [apps/atuin](apps/atuin) |
| yazi | TUI file manager | [apps/yazi](apps/yazi) |
| leaf | TUI markdown reader | [apps/leaf](apps/leaf) |
| tandem | TUI board | [apps/tandem](apps/tandem) |
| spotifast | GUI music | [apps/spotifast](apps/spotifast) |
| quickshell | GUI widgets | [apps/quickshell](apps/quickshell) |
| starship | shell prompt | [apps/starship](apps/starship) |
| zsh-patina | shell highlighting | [apps/zsh-patina](apps/zsh-patina) |
| eza | CLI listing | [apps/eza](apps/eza) |
| fastfetch | CLI summary | [apps/fastfetch](apps/fastfetch) |


## how to use

Don't clone this into your config. Copy the file for the app you want from its folder, or point your agent at the palette and have it build the rest.

Some files are generated from the palette in [`build/generate.py`](build/generate.py); the rest are hand-written and checked against it.

## License

[MIT](LICENSE)
