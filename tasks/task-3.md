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
updatedAt: "2026-11-13T01:16:12Z"
assignee: "pi:verdigris"
---
\n## Description\n\nAlgorant (via Herdra, m5fdbcd6b), verbatim:\n\n\"for verdigris, seems like we need a full refactor of sorts. open a ceph up for that project and bring down latest. My goal for that repo would for it to be like similar colorscheme repos which have a color palette and config/scheme for every supported project, good things to model after are like flexoki by kepano. Not that is the goal, so telling me 'a ton of these are private now' is not helpful and doesn't seem to capture or understand waht the goal of this repo is. its meant to be a public colorscheme repo where people can see waht I use for config, with pictures/demos of what they look like for every given thing piece of software etc. we will need to rescope this completely it seems due to my personal config getting so many changes and things being anchored on the wrong idea\"\n\nThis supersedes the earlier \"polish, then share\" framing. The Algorant Ceph's port-table critique was anchored on that wrong idea; treat it as superseded rather than as work to finish.\n\nPlan first, change nothing:\n1. Study flexoki (github.com/kepano/flexoki, latest, plus its site) and one or two similar scheme repos: how the palette is laid out, per-app folders, install notes, and screenshots.\n2. Propose verdigris's shape the same way: palette as source of truth (names, hex, roles, light/dark if any), one folder per supported app with a real installable theme file generated or kept from the palette, and a screenshot of each app wearing it. Draw the app list from what Algorant actually uses; Algomarchy's Ceph knows the machine setup. Mark which exist today and which need making.\n3. Follow the repo style rules (global memory note repo-style-rules.md): banner, lowercase names, first-person voice, short showroom README, `## License` -> `[MIT](LICENSE)` last.\n\nPublish the plan in a new Sideshow session \"verdigris rescope\" (Decide box first with only Algorant's calls, then the proposed layout, then the app list as a short table) and reply to Herdra with the link. Algorant iterates there before any implementation is dispatched.\n\n## Approved so far\n\nSideshow session \"verdigris rescope\": http://desktop.tail1cefc.ts.net:8228/session/rsnVsfi6go4\n\n- Structure: apps nested under one `apps/<app>/` folder, small top level. Algorant on the first plan post: \"I think maybe at top level every individual 'program' or palette for a given pieces of software should be nested so that when you click on the repo in github its not just a giant stack of directories.\"\n- Banner: **variant 3**, all four highlight tiles tall (ochre, vellum, aqua, then fern). Algorant via Herdra md1ec80dc: \"for banner: option 3\". Mockups: post \"banner A: four highlights and quiet fill\".\n- **Dark variants only. No light variant, no `-light` names or placeholders.** Algorant via Herdra md7d11819: \"verdigris should basically only have dark variants. Light variants are nice to have only, and I don't really know where or how I would support them anyway. its a dark theme\".\n\n## Still open (Algorant's call)\n\n- omarchy and neovim placement: recommend keeping them as their own installable repos and linking them, because `omarchy theme install` clones a repository root. The build plan is drafted assuming that; implementation waits for the answer.\n\n## Next step\n\nBuild-order plan posted in the same session, pending the omarchy/neovim call: palette source, `apps/` skeleton and banner, the existing herdr-app and obsidian files, then the dotfiles themes moved in, then screenshots and the README, then the Algomarchy cutover.\n

## Structure: every app is apps/<app> (Algorant, via Herdra m97322a53)

Algorant, verbatim: "neovim should have scaffolding and proper linking but link to its own repo as well. similar for omarchy related projects. there is no hard and fast line, for example I use many things on omarchy such as starship, ghostty, etc but they don't 'belong' to omarchy. similarly things like quickshell and widgets I make for it, even thoug hthey are omarchy cnetric, could easily be used on other linux distros. its just the wrong wya to go about structuring or anchoring on. the fact that they are used in things like omarchy should be descriptive, not prescriptive"

So:
- apps/neovim/ exists like any other app: theme file or stub, install note, screenshot, and a link to Algorant/verdigris.nvim for the full plugin
- apps/omarchy/ exists too: colours file or stub, desktop screenshot, link to Algorant/omarchy-verdigris-theme
- starship, ghostty and any quickshell or desktop widgets are ordinary apps/ entries; "used on omarchy" lives in their note or README row, never in the tree
- no folder is named after a desktop or groups another app
- step 10 of the build plan is the consumer switch: my dotfiles keep only the enable lines

Build-order plan revised accordingly in the same Sideshow session (post "build order"), awaiting Algorant's go.


## README policy (Algorant via Herdra m261d45c0)

Algorant: "This is not a utilitiarian repo, and you shouldn't have added an ugly 'screenshot' section. We need to rethink and propose pushes better for this. From now on README changes go to a branch and come to him as a rendered preview first; nothing README-facing lands on main without his OK."

- Do not touch README.md on main; propose README changes on a branch and show a rendered preview through Herdra before any merge.
- App folders, theme files and screenshots continue; the README shape is being rethought by Algorant with Herdra, brief to follow.
- Current main README already follows his GitHub edit: his intro, the restored swatch plus a short description, the apps table, how to use, License. The gallery and palette table he removed are not present.


## Progress (2026-11-12)

- 20 app folders under apps/, each with a theme file in the app's own format and a README from one template
- terminal screenshots complete: omarchy, atuin, btop, eza, fastfetch, leaf, neovim (plus split), starship, tandem (plus seeded board), yazi; every frame has its tape except omarchy, which is a compositor capture
- no picture, with the reason in the folder: herdr app, hokum, hyprland, pi, claude code
- deferred until Algorant is away: ghostty, foot, chromium, obsidian at native window size, and zsh-patina from inside ghostty
- palette 0.2.0 hues applied to every moved theme; generator idempotent; foot, ghostty and hyprland config checks pass
- README frozen on main pending Algorant's showroom brief; proposals go on a branch with a rendered preview
- still open: step-10 dotfiles switch (Algorant's OK), pi theme handover to the .pi Ceph, final full-history gitguard scan, the showroom README


## Stop the automation (Algorant via Herdra mb44db0d6)

Algorant: "for verdigris please stop all complicated automation things. lets assess where we are and don't overdo the classificaiton automatically, I can help and make ti go by much faster so that we can get the ball rolling, and figure out whats outstanding. lets just get something working and understood first"

- The screenshot classification helper was killed and removed; no contact sheet was published.
- No capture harness, no further capture plumbing, no automated classification.
- Algorant sorts his 20 hand-taken screenshots with Herdra himself.
- README stays frozen on main; nothing README-facing lands without his OK.
- Next step is his direction: assess what exists and get one working, understood state first.


## Algorant's screenshot review (all 20 answered, mec233ecb)

Answers: 19 yes, 1 unsure (#7, eza via my ls alias, kept as a candidate, not featured). Privacy: "Personal lists are ok" and the spotifast frames are fine, so no fixture reshoots; #1 needs a higher-resolution retake and stays a placeholder.

Corrections to my guesses:
- #3, #4: omarchy menu and keybinding menu, also showing the background and my layout
- #5: a floating ghostty running the omarchy fastfetch
- #6: atuin with my history; its red is not verdigris oxblood → papercut task-4 filed, retake after the fix
- #8: leaf with a generic readme open
- #9–#12: neovim plain, file picker, lazy, mason
- #13–#15: spotifast, which is verdigris-themed and now has its own folder
- #16–#20: omarchy widgets — calendar, flux, ethernet (placeholder to retake as just the widget), system monitor, ai coding plans; flux is a widget, not an app, and all five live under apps/quickshell/

Placement: 8faae24 on main. VHS frames kept where they are better (atuin, eza, btop, yazi, fastfetch, tandem, starship, omarchy replaced, neovim and leaf replaced by his). The :8771 review page is stopped. README showroom proposed on branch readme-showroom (dd6b3b2), preview posted in the session.


## Front-page README merged (Algorant, ma3520ba1)

Algorant: "bring verdigris back. I like the proposed change we pushed up. how do I merge it? can you do it through gh cli?"

- PR #1 opened from readme-showroom and merged with the merge commit cf9076d; branch deleted after merge.
- Main now carries the showroom README with the three-column gallery, nine tiles plus six folded, and 15 thumbnails in docs/thumbs/.
- Verified on the public front page: the gallery and palette swatch render, 15 thumb references present.
