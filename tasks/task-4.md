---
id: task-4
uid: 768c8823-0c22-48db-a14a-c9138d765fcc
type: task
kind: "papercut"
title: "Atuin's red is not verdigris oxblood"
state: todo
priority: "low"
effort: "small"
relatedFiles: ["apps/atuin/verdigris.toml", "apps/atuin/screenshot.png"]
accord:
  status: "ready"
  acceptance: ["The atuin port's red matches verdigris oxblood roles: fills use oxblood #74363d and red text uses oxblood-text #c66f70, with no leftover Gruvbox red in apps/atuin/verdigris.toml.", "A fresh atuin screenshot built from the corrected theme replaces the placeholder in apps/atuin/."]
  updatedAt: "2026-11-12T22:33:25Z"
createdAt: "2026-11-12T22:33:25Z"
updatedAt: "2026-11-12T22:33:25Z"
---

## Description

Algorant, answering the screenshot review (Herdra mec233ecb): "atuin with my history. also can note that the 'red' in it is not really a verdigris oxblood red so maybe papercut task to have that changed then retake it".

apps/atuin/verdigris.toml still carries a red that is not the oxblood family; the ported theme should use oxblood #74363d for fills and oxblood-text #c66f70 for red text, as every other port now does after palette 0.2.0. Then the placeholder screenshot is retaken.
