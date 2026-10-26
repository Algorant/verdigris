# Consolidating the Verdigris Obsidian setup

> **Status (adopted): Option 2 — single Minimal-compatible CSS snippet.**
> The look now lives in `verdigris-minimal.css`, installed to
> `<vault>/.obsidian/snippets/` and enabled in `appearance.json`. Verdigris
> color and heading-size variables now live in the snippet, so Style Settings is
> no longer required for this port.

Current status: the old vault appearance mechanism was brittle because it mixed Minimal, Minimal Theme Settings, Style Settings color overrides, and Appearance settings. The current consolidation target is:

1. Obsidian active theme: `Minimal`
2. Minimal Theme Settings plugin: selects `minimal-gruvbox-dark` as the base scheme
3. `verdigris-minimal.css`: installed and enabled as `.obsidian/snippets/verdigris-minimal.css`
4. Style Settings plugin: not required; if present, it should not store Minimal appearance overrides in `plugins/obsidian-style-settings/data.json`
5. Obsidian `appearance.json`: stores the app accent color, active theme, and enabled snippet

This file records the options and why the CSS snippet is the practical near-term answer.

## What the documentation suggests

- Obsidian themes are packaged as a theme folder containing `manifest.json` and `theme.css`.
- Style Settings can expose settings from any loaded theme, snippet, or plugin using a `/* @settings ... */` YAML comment.
- Minimal documents custom color schemes in two ways:
  - regular custom schemes through Style Settings
  - advanced schemes through CSS snippets using the same variable structure as Minimal's built-in schemes
- Minimal Theme Settings' preset dropdown is hardcoded in the plugin; adding a named `Verdigris` option there would require patching/forking that plugin.

## Option 1 — Keep current Style Settings profile

Keep using:

```text
Minimal theme
+ Minimal Theme Settings: Gruvbox Dark
+ Style Settings: Verdigris overrides
```

### Pros

- Already working.
- Full UI customization through Style Settings.
- Uses Minimal exactly as intended for custom colors.

### Cons

- The actual palette lives in plugin data JSON, not a clear theme file.
- Sync can be confusing because plugin data/settings must sync correctly on each client.
- Hard to version/review compared to CSS.
- Easy to accidentally change colors through the UI and lose the intended palette shape.

### Verdict

Good for experimentation, not ideal as final durable setup.

## Option 2 — Single Minimal-compatible CSS snippet

Create one canonical snippet, e.g.:

```text
.obsidian/snippets/verdigris-minimal.css
```

The snippet would set Minimal variables directly:

```css
body.theme-dark {
  --bg1: #282828;
  --bg2: #1e2021;
  --tx1: #fbf1c7;
  --ax1: #8ec07c;
  --h1-color: #689d6a;
  --link-color: #8ec07c;
  --link-unresolved-color: #70764a;
  --tag-color: #d8a65c;
  /* etc. */
}
```

It could also include a small `@settings` block for documentation or optional knobs, but the default appearance would not depend on Style Settings data.

### Pros

- One obvious source of truth for the Verdigris palette.
- Sync-friendly: snippets are normal vault files.
- Minimal can still update underneath it.
- No dependence on Style Settings for the base look.
- Easy to version, diff, and generate from `palette.css` later.

### Cons

- Still depends on Minimal being the active theme.
- Still needs the snippet enabled in `appearance.json`.
- If we include optional Style Settings controls, user overrides again live in plugin data.
- Does not appear as a named Minimal Theme Settings preset.

### Verdict

Best practical consolidation if we want to keep Minimal updates and reduce brittleness. This is likely the recommended next step once the palette settles.

## Option 3 — Full local theme: `Verdigris Minimal`

Create:

```text
.obsidian/themes/Verdigris Minimal/manifest.json
.obsidian/themes/Verdigris Minimal/theme.css
```

The `theme.css` would either:

1. vendor/copy Minimal's theme CSS and append Verdigris overrides, or
2. be generated from Minimal's source plus our override layer.

### Pros

- One active theme selection in Obsidian.
- No snippets required.
- No Style Settings required for the base look.
- Most cohesive from Obsidian's point of view.

### Cons

- If we copy Minimal CSS, we stop automatically receiving Minimal updates.
- If we generate from Minimal source, we need a small build/update process.
- More maintenance than a snippet.
- If published/shared, it becomes effectively a Minimal fork/derivative theme.

### Verdict

Best if we want a true standalone theme. More cohesive, but higher maintenance.

## Option 4 — Patch/fork Minimal Theme Settings

Modify Minimal Theme Settings so the dropdown includes `Verdigris`, then add matching CSS scheme selectors such as:

```css
.theme-dark.minimal-verdigris-dark { ... }
```

### Pros

- Verdigris would appear exactly where expected in Minimal Theme Settings.

### Cons

- The plugin dropdown is bundled/hardcoded.
- Local patch would be overwritten by plugin updates.
- Maintaining a fork is not worth it for a palette unless we intend to publish/maintain it.

### Verdict

Not recommended.

## Option 5 — Custom companion plugin

Write a small Obsidian plugin that injects Verdigris CSS and exposes a settings tab.

### Pros

- Custom UI and commands are possible.
- Could avoid Style Settings entirely.

### Cons

- Overkill for color variables.
- More code and maintenance than CSS.
- Another plugin to sync/install.

### Verdict

Not recommended unless the project grows beyond theme variables.

## Recommendation

Short term: use the single **Minimal-compatible CSS snippet** as the source of truth and prune Minimal overrides from Style Settings data. That reduces the live setup to:

```text
Minimal theme
+ one enabled Verdigris Minimal CSS snippet
```

Style Settings is no longer required for the Verdigris look. Use `~/.dotfiles/obsidian/sync-verdigris.py` to catch drift between this repo, the dotfiles File Color snapshot, and live vaults.

Longer term: if the palette stabilizes and we want a truly cohesive install, create a local/full theme called `Verdigris Minimal`. Use a build script to vendor a known Minimal version and append the Verdigris color layer so updates are explicit and reviewable.

## Suggested future source-of-truth layout in this repo

```text
palette.css                 # swatch-friendly palette inventory
palette-notes.md            # human decisions and history
verdigris-minimal.css       # generated/applyable Minimal-compatible snippet
consolidation-options.md    # this document
scripts/build-snippet.py    # optional: generate snippet from palette roles
```

This keeps experimentation in `palette.css` and makes Obsidian installation a generated artifact instead of hand-edited plugin JSON.
