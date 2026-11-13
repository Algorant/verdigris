---
id: task-7
uid: d37d204e-b202-495c-a1cc-6d1d2a2071a9
type: task
kind: "papercut"
title: "build/generate.py writes ports to paths the repo does not track"
state: todo
priority: "medium"
effort: "small"
relatedFiles: ["build/generate.py"]
accord:
  status: "ready"
  acceptance: ["build/generate.py run leaves git status clean", "The four ports it currently drops are either tracked at their real paths or their generators are gone"]
  updatedAt: "2026-11-13T03:47:59Z"
createdAt: "2026-11-13T03:47:59Z"
updatedAt: "2026-11-13T03:47:59Z"
---

## Description

Running `python3 build/generate.py` creates apps/chromium/verdigris.theme, apps/claude-code/verdigris.json, apps/foot/verdigris.ini and apps/hyprland/verdigris.lua. None of those paths is tracked, nor is the hyprland port the repo actually carries (apps/omarchy/hyprland/verdigris.lua), so a regenerate adds four stray directories and updates nothing that ships.

Found while sweeping "colour" to "color": the run also reverted the approved ghostty slot-7 fix (soft-light #d4be9a instead of vellum #ebdbb2), which is fixed at the source in 5d3ed95 by moving slot 7 to vellum — but the print at the end still says which files it generated, and it lists the stray ones.

Wanted: either the generator writes the four missing ports where the repo keeps them (apps/foot, apps/chromium, apps/claude-code, apps/omarchy/hyprland) and they get committed, or those generators are removed because the omarchy theme covers them.
