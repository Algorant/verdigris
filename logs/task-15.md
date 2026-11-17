---
id: task-15
uid: 93119901-6852-4801-8c37-e0a5cef83a04
type: task
title: "Standardize Verdigris repo license footers"
effort: "small"
references: ["Algorant board task-23"]
accord:
  status: "accepted"
  acceptance: ["Both repository READMEs end with exactly the standard License section and are pushed with checks passing."]
  claimedAt: "2026-11-17T15:29:34Z"
  deliveredAt: "2026-11-17T15:30:01Z"
  summary: "Standard License footer pushed to omarchy-verdigris-theme c9a8c33 and verdigris.nvim 942bf33."
  evidence: ["Both diffs passed git diff --check; omarchy-verdigris-theme adds License after History, verdigris.nvim changes ./LICENSE to LICENSE.", "Signed-out raw GitHub READMEs both end exactly with ## License, blank line, [MIT](LICENSE); both public LICENSE pages return HTTP 200.", "Both pushes passed commit leak scans; local omarchy-verdigris-theme main equals origin/main."]
  filesChanged: ["omarchy-verdigris-theme/README.md", "verdigris.nvim/README.md"]
  reviewer: "Algorant"
  updatedAt: "2026-11-17T15:30:01Z"
createdAt: "2026-11-17T15:29:30Z"
updatedAt: "2026-11-17T15:30:01Z"
assignee: "pi:verdigris"
archivedAt: "2026-11-17T15:30:01Z"
resolution:
  outcome: "completed"
  note: "Completed under Algorant's request relayed in m97289195 (Algorant board task-23), which approved pushing. No live theme/plugin installation changed."
  reviewer: "Algorant"
---

## Description

Herdra relayed Algorant (2026-11-17, Algorant board task-23, m97289195): "I want that standardized across all my repos". Last README section must be exactly ## License followed by [MIT](LICENSE). omarchy-verdigris-theme needs it after History; verdigris.nvim needs [MIT](./LICENSE) normalized. Pushing approved because Algorant asked.
