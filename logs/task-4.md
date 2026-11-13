---
id: task-4
uid: 768c8823-0c22-48db-a14a-c9138d765fcc
type: task
kind: "papercut"
title: "Atuin's red is not verdigris oxblood"
priority: "low"
effort: "small"
relatedFiles: ["apps/atuin/verdigris.toml", "apps/atuin/screenshot.png"]
accord:
  status: "accepted"
  acceptance: ["The atuin port's red matches verdigris oxblood roles: fills use oxblood #74363d and red text uses oxblood-text #c66f70, with no leftover Gruvbox red in apps/atuin/verdigris.toml.", "A fresh atuin screenshot built from the corrected theme replaces the placeholder in apps/atuin/."]
  claimedAt: "2026-11-13T02:48:14Z"
  deliveredAt: "2026-11-13T02:48:22Z"
  summary: "Atuin's error red is now the oxblood text tint in both places: apps/atuin/verdigris.toml and his live config (Algomarchy checkpoint 427, e6d243d). The re-rendered frame shows the UPDATE label sampling #c67273 on #1d1e20, and the same visit fixed the stale Omarchy theme clone that was feeding Gruvbox red into ghostty's ANSI 1/9."
  evidence: ["apps/atuin/verdigris.toml sets AlertError #c66f70; his live ~/.config/atuin/themes/verdigris.toml now matches it exactly (Algomarchy: AlertError #fb4934 -> #c66f70, checkpoint 427 published e6d243d).", "Algomarchy measured the re-rendered frame: UPDATE label glyphs #c67273 (antialias of #c66f70) on #1d1e20; slow durations and the label are both the AlertError key, so one change covered both.", "Owner verification: ~/.local/state/omarchy/current/theme/ghostty.conf now reads palette 1=#c66f70 and 9=#d47b7c, and ~/.config/omarchy/themes/verdigris/colors.toml now reads red #c66f70 / bright_red #d47b7c, matching the theme repo.", "New frame committed as the first atuin tile (1379cac), tape updated, his own history frame second; links and thumbs resolve.", "Legibility note retained: #74363d is 1.8:1 on #1d2021 and stays a fill colour; anything textual uses the tint."]
  filesChanged: ["apps/atuin/verdigris.toml", "apps/atuin/screenshot.png", "apps/atuin/screenshot-2.png", "apps/atuin/screenshot.tape", "apps/atuin/README.md"]
  reviewer: "Algorant"
  updatedAt: "2026-11-13T02:48:30Z"
createdAt: "2026-11-12T22:33:25Z"
updatedAt: "2026-11-13T02:48:30Z"
assignee: "pi:verdigris"
archivedAt: "2026-11-13T02:48:30Z"
resolution:
  outcome: "completed"
  note: "Fixed and verified live: atuin's AlertError is #c66f70 in the repo and on his machine (checkpoint 427), the retaken frame shows the oxblood label, and the stale Omarchy theme clone behind ghostty's ANSI 1/9 was fixed in the same visit. Algorant asked for this change directly."
  reviewer: "Algorant"
---

## Description

Algorant, answering the screenshot review (Herdra mec233ecb): "atuin with my history. also can note that the 'red' in it is not really a verdigris oxblood red so maybe papercut task to have that changed then retake it".

apps/atuin/verdigris.toml still carries a red that is not the oxblood family; the ported theme should use oxblood #74363d for fills and oxblood-text #c66f70 for red text, as every other port now does after palette 0.2.0. Then the placeholder screenshot is retaken.
