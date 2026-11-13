# lazygit

<table>
  <tr>
    <td align="center"><a href="screenshot.png"><img src="thumbs/1.jpg" width="260"></a><br><sub>a staged change, an untracked one, and the log</sub></td>
  </tr>
</table>

- A terminal UI for git
- [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

## files

- [config.yml](config.yml): the `gui.theme` block, pasted into `~/.config/lazygit/config.yml`

## notes

Fern marks the active panel, ashbronze the idle ones, and the lighter background sits under the selected line. Staged and unstaged changes use oxblood's text tint, which is the only red in the palette that stays readable on `#1d2021`.

Two accents are set but not in frame: cherry-picked commits (teal) and the search prompt's border (goldenrod). Neither can be shot on 0.66.2 as the keys suggest: cherry-pick is bound to an uppercase `C` no automated terminal delivers, and an open search keeps the panel's active border rather than showing goldenrod.
