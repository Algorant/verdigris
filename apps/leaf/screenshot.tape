# leaf - verdigris screen. Regenerate from this folder with: vhs screenshot.tape
# Scratch HOME and every XDG_* live under /tmp; nothing of the real config or notes is read.
Output "/tmp/verdigris-shot/leaf/rec.gif"
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
Type "SRC=$PWD; S=/tmp/verdigris-shot/leaf; rm -rf $S; mkdir -p $S/home/.config/leaf/themes $S/data $S/state $S/cache $S/project"
Enter
Type "export HOME=$S/home XDG_CONFIG_HOME=$S/home/.config XDG_DATA_HOME=$S/data XDG_STATE_HOME=$S/state XDG_CACHE_HOME=$S/cache LANG=C.UTF-8 LC_ALL=C.UTF-8 PS1='demo@workstation:~/project$ '"
Enter
Type `cp $SRC/verdigris.toml $HOME/.config/leaf/themes/ && echo 'theme = "themes/verdigris.toml"' > $HOME/.config/leaf/config.toml && cd $S/project`
Enter
Type `cat > notes.md <<'EOF'`
Enter
Type "# Weathering notes"
Enter
Type ""
Enter
Type "How fresh copper turns green: a short field guide for the workshop."
Enter
Type ""
Enter
Type "## The stages"
Enter
Type ""
Enter
Type "Bare metal darkens first, then the surface oxidizes into a soft **patina**."
Enter
Type ""
Enter
Type "- bright copper, the first week"
Enter
Type "- brown cuprite, a dull _oxide_ layer"
Enter
Type "- green verdigris, the final carbonate"
Enter
Type ""
Enter
Type "| stage | colour | time |"
Enter
Type "| --- | --- | --- |"
Enter
Type "| copper | #b87333 | day 1 |"
Enter
Type "| cuprite | #7a4a2a | month 1 |"
Enter
Type "| verdigris | #689d6a | year 3 |"
Enter
Type ""
Enter
Type "## Speeding it up"
Enter
Type ""
Enter
Type "> Vinegar and salt do in an afternoon what rain does in a decade."
Enter
Type ""
Enter
Type "~~~python"
Enter
Type "def patina(days: int) -> str:"
Enter
Type '    """Rough colour after a number of days."""'
Enter
Type '    return "verdigris" if days > 1000 else "copper"'
Enter
Type "~~~"
Enter
Type ""
Enter
Type "## Sealing"
Enter
Type ""
Enter
Type "- [x] clean the surface"
Enter
Type "- [ ] apply wax"
Enter
Type "EOF"
Enter
Type "clear"
Enter
Show
Type "leaf notes.md"
Enter
Sleep 2s
Type "t"
Sleep 1s
Screenshot "/tmp/verdigris-shot/leaf/screenshot.png"
