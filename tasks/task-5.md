---
id: task-5
uid: 4d16535c-659c-4889-aea2-9e3ce0f99a6f
type: task
title: "Give every app README the homepage gallery format"
state: todo
priority: "medium"
effort: "medium"
relatedFiles: ["apps/neovim/README.md", "README.md", "docs/thumbs/"]
accord:
  status: "ready"
  acceptance: ["Every app README opens with a gallery table in the approved format: three columns where there is room, a small caption under each tile, each tile linking to the full screenshot.", "Each app's thumbnails are small copies beside the app (thumbs/) generated from its own screenshots, and a README with more than about nine shots folds the extras under more screenshots.", "The pattern is proven on one app as a mockup before it is applied everywhere; the installed layout still shows the install steps and notes below the gallery."]
  updatedAt: "2026-11-12T23:13:52Z"
createdAt: "2026-11-12T23:13:52Z"
updatedAt: "2026-11-12T23:13:52Z"
---

## Description

Algorant (via Herdra mda564664), verbatim:

"for latest gallery mockup: YES. that is what I am looking for. not just for the homepage, but honestly that should be the format in every single readme for every single app/project/section. not to be done now, just planned out in a task and mocked up as well."

Plan (not applied yet):
- Same gallery block as the homepage: an HTML table, three columns, one tile per screenshot the app has, a <sub> caption under each, every tile linking to the full screenshot.
- Thumbnails live beside the app: apps/<app>/thumbs/<name>.jpg, 480x300, padded on #1d2021, generated from that app's own screenshots.
- More than about nine shots fold the extras under <details><summary>more screenshots</summary>.
- Order in each app README: title, one line, gallery, install, notes. Apps with a single screenshot get one tile, not a table.
- The homepage gallery stays as the model; this Task is for the per-app standard.

Proof before rollout: mockup of apps/neovim/README.md (four shots) published in the verdigris rescope Sideshow session, post "app README gallery: neovim mockup".

Herdra is recording this as Algorant's README format for his public repos.
