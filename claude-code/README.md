# Verdigris for Claude Code

Verdigris is available as a Claude Code custom TUI theme.

Source:

```text
~/.claude/themes/verdigris.json
```

Enabled from `~/.claude/settings.json` via `"theme": "custom:verdigris"` (or interactively with `/theme`).

## Shape

```css
:root {
  --cc-text: #ebdbb2;
  --cc-claude: #8ec07c;
  --cc-permission: #83a598;
  --cc-plan-mode: #458588;
  --cc-success: #70764a;
  --cc-warning: #d29a46;
  --cc-error: #e36f63;
  --cc-selection-bg: #665c54;
  --cc-border: #928374;
  --cc-panel: #2c2f30;
}
```

## Notes

- The theme is a set of overrides on the built-in `dark-ansi` base: anything not overridden falls back to the terminal's ANSI palette, which is already Verdigris in Ghostty.
- `fern` is the brand accent: spinner, Claude highlights, and the Clawd mascot.
- `aqua` covers the "blue" UI roles: permission prompts, suggestions, IDE, and the rate-limit bar.
- Semantic roles follow the [additional colors](../additional-colors/) set: `moss` for success and diff additions, `diff-red` for errors and removals, `yellow` for warnings, `teal` for plan mode, `orange` for fast mode, and `purple` for merged/ultra-effort accents.
- Canonical ochre `#e6bf86` stays on the bash border as brass emphasis.
- Diff line backgrounds are dark tints of moss and diff-red.
- Panel backgrounds (user message, bash, memory) reuse the Pi port's dark panel values.

Claude Code is a UI port in the same spirit as Pi: muted panels and readable transcript first, full palette second.
