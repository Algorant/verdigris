---
id: task-3
uid: 5f36ad2d-a8c5-4005-ab9e-7262c4cfa302
type: task
title: "Rescope verdigris as a public colour-scheme repo with a theme and screenshot per app"
state: "in-progress"
priority: "high"
effort: "medium"
references: ["https://github.com/kepano/flexoki", "https://stephango.com/flexoki"]
relatedFiles: ["README.md", "css/palette.json", "herdr-app/verdigris.json"]
accord:
  status: "claimed"
  acceptance: ["A plan post is published in a new Sideshow session \"verdigris rescope\" with the Decide box first (only Algorant's calls), the proposed repo layout, and a short app table covering today versus missing.", "The proposal is modelled on flexoki and at least one similar scheme repo: palette as source of truth, one folder per supported app with a real installable theme file, and a screenshot per app.", "The app list reflects what Algorant actually uses (Omarchy desktop, terminals, herdr app, pi, Obsidian, editors, browser, etc.), each marked as existing or to be made, with Algomarchy's machine inventory as evidence.", "The proposed README follows the repo style rules: banner, lowercase names, first-person voice, showroom tone, and a final \"## License\" linking MIT.", "Nothing in the repository is changed or refactored in this Task; Algorant iterates on the plan in Sideshow before implementation is dispatched."]
  claimedAt: "2026-11-12T14:44:35Z"
  updatedAt: "2026-11-12T14:44:35Z"
createdAt: "2026-11-12T14:41:20Z"
updatedAt: "2026-11-12T14:44:35Z"
assignee: "pi:verdigris"
---

## Description

Algorant (via Herdra, m5fdbcd6b), verbatim:

"for verdigris, seems like we need a full refactor of sorts. open a ceph up for that project and bring down latest. My goal for that repo would for it to be like similar colorscheme repos which have a color palette and config/scheme for every supported project, good things to model after are like flexoki by kepano. Not that is the goal, so telling me 'a ton of these are private now' is not helpful and doesn't seem to capture or understand waht the goal of this repo is. its meant to be a public colorscheme repo where people can see waht I use for config, with pictures/demos of what they look like for every given thing piece of software etc. we will need to rescope this completely it seems due to my personal config getting so many changes and things being anchored on the wrong idea"

This supersedes the earlier "polish, then share" framing. The Algorant Ceph's port-table critique was anchored on that wrong idea; treat it as superseded rather than as work to finish.

Plan first, change nothing:
1. Study flexoki (github.com/kepano/flexoki, latest, plus its site) and one or two similar scheme repos: how the palette is laid out, per-app folders, install notes, and screenshots.
2. Propose verdigris's shape the same way: palette as source of truth (names, hex, roles, light/dark if any), one folder per supported app with a real installable theme file generated or kept from the palette, and a screenshot of each app wearing it. Draw the app list from what Algorant actually uses; Algomarchy's Ceph knows the machine setup. Mark which exist today and which need making.
3. Follow the repo style rules (global memory note repo-style-rules.md): banner, lowercase names, first-person voice, short showroom README, `## License` -> `[MIT](LICENSE)` last.

Publish the plan in a new Sideshow session "verdigris rescope" (Decide box first with only Algorant's calls, then the proposed layout, then the app list as a short table) and reply to Herdra with the link. Algorant iterates there before any implementation is dispatched.
