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
updatedAt: "2026-11-13T01:17:23Z"
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


## Template correction (Algorant via Herdra mefd04f41)

Algorant: "for neovim mockup, maybe bad example because that one has its entire own repo which we can draw from or change to match this. but why 'verdigris for neovim' instead of the literal name of the project already which is 'verdigris-nvim' ? additionally, the sections are not named for clarity or brevity really. I want the title, a file list (maybe) the gallery, and any notes, thats about it"

Final shape, in this order and nothing else:
1. Title: the thing's literal name — verdigris-nvim for neovim; for an app with no repo of its own, the app's name (btop, yazi). Never "verdigris for X".
2. files: a short list of the files in the folder, each linked, with a few words only if needed. Optional when there is one obvious file.
3. gallery: the approved table (three columns, captions, tiles linking to the full screenshot; extras folded).
4. notes: only if there is something worth saying (non-obvious install steps belong here).

Neovim: link to Algorant/verdigris.nvim and note that its own README can later be changed to match; do not touch that repo now.
Proof: corrected mockup using an app with no repo of its own (btop), published in the verdigris rescope session.


## Trial branch (Algorant via Herdra m2ac7ca2e)

Algorant: "we definitely need to iron out the individual pages a bit, but hte homepage basically looks pretty great"

- Branch app-pages (de8a8e5, pushed, no PR) rewrites three READMEs in the corrected template: btop (one shot), omarchy (two shots, titled omarchy-verdigris-theme, files link its theme repo), neovim (titled verdigris-nvim, four shots, files link Algorant/verdigris.nvim).
- Thumbs committed beside each app in apps/<app>/thumbs/ (480x300).
- Draft PR #2 closed and the earlier branch deleted, so he reads the rendered pages on the branch.
- The other 17 apps wait for his notes on these three before any rollout.
