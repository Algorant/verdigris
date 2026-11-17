# flea (terminal mode) - verdigris screen. Regenerate from this folder with: vhs screenshot.tape
# Scratch HOME and every XDG_* live under /tmp; flea reads the omarchy theme from the scratch state dir, never the real one.
Output "/tmp/verdigris-shot/flea/rec.gif"
Set Width 1600
Set Height 1000
Set Padding 0
Set Margin 0
Set FontFamily "JetBrainsMono Nerd Font"
Set FontSize 22
Set LineHeight 1.2
Set LetterSpacing 1
Set TypingSpeed 0s
Set Shell "bash"
Set Theme {
  "background": "#1d2021",
  "foreground": "#ebdbb2",
  "cursor": "#ebdbb2",
  "selection": "#665c54",
  "black": "#1d2021",
  "red": "#c66f70",
  "green": "#689d6a",
  "yellow": "#e6bf86",
  "blue": "#458588",
  "magenta": "#8989b0",
  "cyan": "#83a598",
  "white": "#d4be9a",
  "brightBlack": "#928374",
  "brightRed": "#d47b7c",
  "brightGreen": "#8ec07c",
  "brightYellow": "#e6bf86",
  "brightBlue": "#83a598",
  "brightMagenta": "#8989b0",
  "brightCyan": "#83a598",
  "brightWhite": "#ebdbb2"
}
Hide
Type "S=/tmp/verdigris-shot/flea; rm -rf $S; T=$S/home/.local/state/omarchy/current/theme; mkdir -p $T $S/data $S/cache $S/home/.config"
Enter
Type "export HOME=$S/home XDG_CONFIG_HOME=$S/home/.config XDG_DATA_HOME=$S/data XDG_STATE_HOME=$S/home/.local/state XDG_CACHE_HOME=$S/cache LANG=C.UTF-8 LC_ALL=C.UTF-8 PS1='demo@workstation:~$ '"
Enter
Type "cat > $T/colors.toml <<'EOF'"
Enter
Type `mode = "dark"`
Enter
Type `accent = "#8ec07c"`
Enter
Type `selection = "#665c54"`
Enter
Type `muted = "#928374"`
Enter
Type `background = "#1d2021"`
Enter
Type `dark_background = "#171a1a"`
Enter
Type `darker_background = "#121515"`
Enter
Type `lighter_background = "#292d2a"`
Enter
Type `foreground = "#ebdbb2"`
Enter
Type `dark_foreground = "#928374"`
Enter
Type `light_foreground = "#d4be9a"`
Enter
Type `bright_foreground = "#ebdbb2"`
Enter
Type `red = "#c66f70"`
Enter
Type `yellow = "#e6bf86"`
Enter
Type `orange = "#b9805f"`
Enter
Type `green = "#689d6a"`
Enter
Type `cyan = "#83a598"`
Enter
Type `blue = "#458588"`
Enter
Type `magenta = "#8989b0"`
Enter
Type `brown = "#665c54"`
Enter
Type `bright_red = "#d47b7c"`
Enter
Type `bright_yellow = "#e6bf86"`
Enter
Type `bright_green = "#8ec07c"`
Enter
Type `bright_cyan = "#83a598"`
Enter
Type `bright_blue = "#83a598"`
Enter
Type `bright_magenta = "#8989b0"`
Enter
Type "EOF"
Enter
Type `cd $HOME && mkdir -p Documents Downloads Music Pictures Videos && printf "x\n" > todo.txt && mkdir -p Projects && cd Projects`
Enter
Type `mkdir -p copper-guide/images garden-planner/data harbor-notes/src lighthouse-demo mosaic-tiles paper-boats sketchbook tide-tables && printf "MIT\n" > copper-guide/LICENSE && printf "name,colour\ncopper,#b87333\n" > garden-planner/data/palette.csv && printf "fn main() {}\n" > harbor-notes/src/main.rs && printf "# Harbor notes\n" > harbor-notes/README.md && printf "[package]\nname = \"harbor\"\n" > harbor-notes/Cargo.toml && printf "# Recipes\n" > recipes.md && printf "ideas\n" > notes.txt`
Enter
Type "clear"
Enter
Show
Type "cd ~/Projects && flea --tui"
Enter
Sleep 2s
Down
Down
Sleep 3s
Screenshot "/tmp/verdigris-shot/flea/screenshot.png"
