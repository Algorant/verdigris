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
updatedAt: "2026-11-13T02:27:16Z"
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


## Template v2: name, gallery, files, project (Algorant via Herdra me452a093)

Algorant: "I gues the format makes more sense with: <name> <gallery> <files> <project> then a one sentence brief description of what it is as a bullet, followed by a bullet of the parent github project."

Order now: title (literal name), ## gallery, ## files, ## project (one-sentence description bullet, then the upstream repo bullet), notes only if genuinely needed.

Applied on branch app-pages (c87f575) to the three samples:
- btop: upstream aristocratos/btop
- omarchy: titled omarchy-verdigris-theme; project bullet links the theme repo and, after "for", omarchy upstream (omacom/omarchy); notes carry the install one-liner
- neovim: titled verdigris-nvim; project bullet links Algorant/verdigris.nvim, then neovim upstream; no notes

All links 200. Other apps untouched pending his notes on these three.


## Algorant's edits and the codified rules (Herdra mf8a64b49 / m79087503)

Algorant: "I made some initial changes to both btop and veridgris-nvim. neither is quite right but they are closer to what I am imagining. I don't want superfluous stuff. if something doesn't make sense cut it. notes are completely optional or situational. when I link to something like omarchy or my OS, I want a link to algomarchy somewhere, and then a gallery of the stuff, and the simplest way to display what/where everything is, and thats it."

His edits on branch app-pages2: btop lost the gallery heading, lost the whole notes section, gained the two project bullets directly under the table, and renamed the link; nvim was renamed verdigris-nvim.

Applied (c06805e, branch only): all three pages now title → bare table → one sentence + project link → files; omarchy adds the Algomarchy link and a parts line; notes kept only where situational (omarchy's install line).

Rule set proposed in the session post "app pages: rules from your edits" (8 rules: real project name as title, gallery with no heading, two bullets, files only for real files, notes rare, no headings for one-liners, desktop pages link Algomarchy + parts, nothing repeated). Herdra adds them to the global repo-style rules after Algorant OKs.

Open question for Herdra: the public URL for Algomarchy (Algorant/omarchy-setup is currently private).


## Rules applied to every page (Algorant via Herdra m976a7b22)

Algorant: "those rules are fine for now and yes the recommended algomarchy link". Herdra added the 8 rules to his style memory.

- Algomarchy link stays as https://github.com/Algorant/omarchy-setup (live when the guide goes public).
- Branch app-pages2 (059bcec) applies the rules to all 17 pages: bare gallery table with thumbs generated per app, one sentence plus project link, files only where files exist, notes only where situational (omarchy install line, patina's missing picture).
- Omarchy parts pages (widgets, hyprland, floating-terminal, omari) and zsh/patina follow the same shape.
- Pages with no picture: herdr, hokum, pi, zsh, zsh/patina, hyprland, omari.
- Links that could not be verified and are therefore omitted: hokum and spotifast have no resolvable upstream repo; herdr points at https://herdr.dev. Needs Algorant's word if they have GitHub repos worth linking.
