---
id: task-12
uid: 6acbd287-12aa-498e-8387-7d0ed5fbd112
type: task
kind: "papercut"
title: "Correct logo tool usage filenames"
state: todo
priority: "low"
effort: "small"
relatedFiles: ["build/mask_from_grid.py", "build/render_logos.py"]
accord:
  status: "ready"
  acceptance: ["Both image tools' usage/help/docstrings name the actual retained script paths; image behavior is unchanged."]
  updatedAt: "2026-11-13T04:58:09Z"
createdAt: "2026-11-13T04:58:09Z"
updatedAt: "2026-11-13T04:58:09Z"
---

## Description

Retained image tools have stale names in their usage/help text: build/mask_from_grid.py advertises mask-from-grid.py and references render.py; build/render_logos.py advertises render.py and refers to mask-from-grid.py. Actual names use underscores and render_logos.py. Found while removing palette generators; these scripts are intentionally retained as image-only tools, so correct just their usage strings in later work.
