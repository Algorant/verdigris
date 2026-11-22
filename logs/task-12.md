---
id: task-12
uid: 6acbd287-12aa-498e-8387-7d0ed5fbd112
type: task
kind: "papercut"
title: "Correct logo tool usage filenames"
priority: "low"
effort: "small"
relatedFiles: ["build/mask_from_grid.py", "build/render_logos.py"]
accord:
  status: "accepted"
  acceptance: ["Both image tools' usage/help/docstrings name the actual retained script paths; image behavior is unchanged."]
  claimedAt: "2026-11-22T16:28:25Z"
  deliveredAt: "2026-11-22T16:28:27Z"
  summary: "Corrected stale script names in both retained image-tool usage/help texts via PR #7 (3c21621); no behavior change."
  evidence: ["Published fix 3c21621 changes only the two retained image tools' usage/docstring names; both published files checked via anonymous raw GitHub.", "Both scripts parse and each prints its corrected Usage line when run without arguments; no behavior or image change."]
  filesChanged: ["build/mask_from_grid.py", "build/render_logos.py"]
  reviewer: "Herdra"
  updatedAt: "2026-11-22T16:28:29Z"
createdAt: "2026-11-13T04:58:09Z"
updatedAt: "2026-11-22T16:28:29Z"
assignee: "pi:verdigris"
archivedAt: "2026-11-22T16:28:29Z"
resolution:
  outcome: "completed"
  note: "Papercut fixed in 3c21621 with no functional change; verified published usage names and both scripts parse."
  reviewer: "Herdra"
---

## Description

Retained image tools have stale names in their usage/help text: build/mask_from_grid.py advertises mask-from-grid.py and references render.py; build/render_logos.py advertises render.py and refers to mask-from-grid.py. Actual names use underscores and render_logos.py. Found while removing palette generators; these scripts are intentionally retained as image-only tools, so correct just their usage strings in later work.
