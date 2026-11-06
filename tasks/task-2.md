---
id: task-2
uid: cc3ec6d4-3efe-46f9-99e5-70ccad1e96a0
type: task
title: "Adopt oxblood fills and readable red tints across Verdigris ports"
state: "in-progress"
priority: "medium"
effort: "medium"
references: ["https://github.com/Algorant/herdra/blob/c31209e/research/task-73.md", "https://github.com/Algorant/omarchy-verdigris-theme"]
relatedFiles: ["css/palette.json", "css/palette.css", "css/palette-notes.md", "additional-colors/README.md", "additional-colors/verdigris-additional-colors-swatch.svg", "CHANGELOG.md", "herdr-app/verdigris.json", "ghostty/README.md", "bat/README.md", "atuin/README.md", "btop/README.md", "yazi/README.md", "windows-terminal/README.md"]
accord:
  status: "claimed"
  acceptance: ["Canonical palette includes documented oxblood-text #c66f70 and oxblood-bright #d47b7c as supporting tints, with CSS, palette notes, swatches and release/version references consistent.", "Herdr and the six named main-repository ports use the approved role-based red mappings; unrelated ports and live configuration remain untouched.", "Standalone Omarchy theme colors.toml uses red #c66f70 and bright_red #d47b7c, with its palette mapping rationale/version updated and published.", "A real terminal colour test and a Herdr screenshot crop demonstrate the updated red roles; evidence names the artifact paths and deployed/source versions.", "Both owned repositories' approved changes are published, and Herdra/Algomarchy receive the commits for the separately owned live refresh."]
  claimedAt: "2026-11-06T15:05:24Z"
  validation: ["$ git diff --check", "$ python3 -m json.tool css/palette.json > /dev/null", "$ python3 -m json.tool herdr-app/verdigris.json > /dev/null"]
  constraints: ["No deployment or refresh of Algorant's live Herdr/Omarchy settings; Algomarchy owns that step.", "Do not add maintained tests or unrelated abstractions.", "Leave the strict push-guard papercut task-1 out of scope."]
  updatedAt: "2026-11-06T15:05:24Z"
createdAt: "2026-11-06T15:04:57Z"
updatedAt: "2026-11-06T15:05:24Z"
assignee: "pi:oxblood-ports"
---
Algorant approved Herdra task-73's oxblood direction (request md8d55095). Keep canonical oxblood #74363d for red fills/bars; add named supporting colours oxblood-text #c66f70 and oxblood-bright #d47b7c for readable text/ANSI red and bright red. Maintain palette metadata, CSS, notes, swatches and release documentation consistently. Update only the requested owned ports: Herdr desktop theme, Omarchy standalone theme and ghostty/bat/atuin/btop/yazi/windows-terminal port READMEs/configs present in this repository. Do not alter Obsidian, Pi, Hokum, Pele, notification plugin or historical Herdra renders.

Approval wording: "Algorant picked the default oxblood #74363d (already Verdigris's canonical removals / errors) for red fills, bars and blocked states, instead of #fb4934. Where red is TEXT, use the proposal's legible tint #c66f70, and #d47b7c for bright red / ANSI 9. Add both to the palette as named colours, documented as oxblood's text and bright tints."

RESOLVED mapping, Herdra m2fb8b887 replying to me906835e: "Yes: follow the rendered role, exactly as you recommend. Herdr blocked and ANSI 1 (dots, labels, text), and error/deletion/cut markers: #c66f70. ANSI 9 / brightRed: #d47b7c. True fills (btop meter and gradient ends, bars): #74363d. Go ahead." This exact mapping is approved; no ambiguity remains.

Execution split: manus owns main-repository source changes in its worktree, identifies the existing palette release convention, and proposes bounded real-render verification without changing live settings/layouts. Verdigris Ceph handles the small standalone omarchy-verdigris-theme repo update after the main palette version is agreed. Algomarchy owns deployment/mise-dot refresh of the installed Herdr theme after publication. Completion requires a real terminal colour render and Herdr screenshot crop, coordinated with Algomarchy; no live configuration changes by this track without a plan/approval.