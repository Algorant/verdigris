![verdigris](docs/banner.png)

verdigris is a dark mode colorscheme built around oxidized copper: weathered bronze, warm vellum, patina green, cool aqua, brass ochre. 

It is what I use on every machine, ported to the software I actually run.

![verdigris core palette](docs/palette-swatch.svg)

Six core colours carry the scheme: ashbronze metal, vellum text, fern and patina greens, aqua, ochre. Everything else in the palette is a supporting role for one app or one state, listed in [`palette/verdigris.json`](palette/verdigris.json).

## gallery

<table>
  <tr>
    <td align="center"><a href="apps/omarchy/screenshot.png"><img src="docs/thumbs/omarchy.jpg" width="260"></a><br><sub>omarchy</sub></td>
    <td align="center"><a href="apps/omarchy/screenshot-2.png"><img src="docs/thumbs/omarchy-keys.jpg" width="260"></a><br><sub>omarchy · keybindings</sub></td>
    <td align="center"><a href="apps/ghostty/screenshot.png"><img src="docs/thumbs/ghostty.jpg" width="260"></a><br><sub>ghostty · fastfetch</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="apps/nvim/screenshot-3.png"><img src="docs/thumbs/neovim-lazy.jpg" width="260"></a><br><sub>neovim · lazy</sub></td>
    <td align="center"><a href="apps/obsidian/screenshot.png"><img src="docs/thumbs/obsidian.jpg" width="260"></a><br><sub>obsidian</sub></td>
    <td align="center"><a href="apps/spotifast/screenshot.png"><img src="docs/thumbs/spotifast.jpg" width="260"></a><br><sub>spotifast</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="apps/leaf/screenshot.png"><img src="docs/thumbs/leaf.jpg" width="260"></a><br><sub>leaf</sub></td>
    <td align="center"><a href="apps/btop/screenshot.png"><img src="docs/thumbs/btop.jpg" width="260"></a><br><sub>btop</sub></td>
    <td align="center"><a href="apps/omarchy/widgets/calendar.png"><img src="docs/thumbs/calendar.jpg" width="260"></a><br><sub>calendar widget</sub></td>
  </tr>
</table>

<details><summary>more screenshots</summary>
<table>
  <tr>
    <td align="center"><a href="apps/yazi/screenshot.png"><img src="docs/thumbs/yazi.jpg" width="260"></a><br><sub>yazi</sub></td>
    <td align="center"><a href="apps/nvim/screenshot.png"><img src="apps/nvim/thumbs/nvim.jpg" width="260"></a><br><sub>neovim</sub></td>
    <td align="center"><a href="apps/omarchy/widgets/system-monitor.png"><img src="docs/thumbs/sysmon.jpg" width="260"></a><br><sub>system monitor</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="apps/atuin/screenshot.png"><img src="docs/thumbs/atuin.jpg" width="260"></a><br><sub>atuin</sub></td>
    <td align="center"><a href="apps/tandem/screenshot-2.png"><img src="docs/thumbs/tandem.jpg" width="260"></a><br><sub>tandem</sub></td>
    <td align="center"><a href="apps/starship/screenshot.png"><img src="docs/thumbs/starship.jpg" width="260"></a><br><sub>starship</sub></td>
  </tr>
</table>
</details>

## apps

### omarchy

[theme](apps/omarchy) · [widgets](apps/omarchy/widgets) · [hyprland](apps/omarchy/hyprland) · [floating terminal](apps/omarchy/floating-terminal) · [omari](apps/omarchy/omari) · [hokum](apps/hokum)

### apps

[herdr](apps/herdr) · [obsidian](apps/obsidian) · [spotifast](apps/spotifast) · [tandem](apps/tandem)

### terminal/cli

[ghostty](apps/ghostty) · [nvim](apps/nvim) · [pi](apps/pi) · [atuin](apps/atuin) · [eza](apps/eza) · [btop](apps/btop) · [yazi](apps/yazi) · [leaf](apps/leaf) · [starship](apps/starship) · [fastfetch](apps/fastfetch) · [zsh](apps/zsh)

## how to use

Don't clone this into your config. Copy the file for the app you want from its folder, or point your agent at the palette and have it build the rest.

Some files are generated from the palette in [`build/generate.py`](build/generate.py); the rest are hand-written and checked against it.

## License

[MIT](LICENSE)
