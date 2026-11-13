---
id: task-9
uid: fd141598-2ad2-4383-8b6c-54c6759d3847
type: task
title: "Restore additional colors reference"
state: "in-progress"
effort: "medium"
relatedFiles: ["README.md", "additional-colors/", "build/generate-additional-colors.py", "build/README.md", "palette/verdigris.json"]
accord:
  status: "delivered"
  acceptance: ["Additional-colors page contains version, six-color-only swatch and one table of the old six short roles; no tints/trials/examples/footer/essay/generator.", "Trial JSON entries ochre-alt/brown-green/dark-ochre-trial removed unless actual shipped-port usage proves retention necessary; no port modified.", "Oxblood-text and oxblood-bright remain in palette JSON but do not appear on the additional-colors page or swatch.", "Homepage link targets additional-colors/ and no generator/docs bullet remains.", "Same Sideshow post 4caGtaNYbmE updated with GitHub-style render, JSON changes reported to Herdra, no merge before approval."]
  claimedAt: "2026-11-13T04:41:44Z"
  deliveredAt: "2026-11-13T04:59:54Z"
  validation: ["$ git diff --check"]
  constraints: ["No live changes, app-port changes, tags or releases.", "Only authorized palette edits are unused trial removals; oxblood text/bright tints retained.", "No palette-to-theme generators.", "No merge until Algorant accepts visible result.", "American spelling."]
  summary: "Six-only historical-style reference ready at 4892e48; same preview post updated, JSON retained by actual shipped-port exception, unmerged for Algorant."
  evidence: ["Owner verified current README contains only title/version/swatch/six short-role rows; six SVG groups, no tint overlays; diff --check clean.", "JSON byte-identical: all three trial hexes have actual shipped-port uses (btop/Leaf/Obsidian/Starship), so explicit exception applies. Oxblood tints retained in JSON only.", "Same Sideshow post 4caGtaNYbmE: GitHub Markdown render, HTTP 200 session; no app configuration changes or merge/push."]
  filesChanged: ["README.md", "additional-colors/README.md", "additional-colors/verdigris-additional-colors-swatch.svg"]
  updatedAt: "2026-11-13T04:59:54Z"
createdAt: "2026-11-13T04:41:25Z"
updatedAt: "2026-11-13T04:59:54Z"
assignee: "pi:additional-colors-reference"
---

## Description

Algorant via Herdra m01044254:
"where in the new repo are we showing what those colors are? we had it in an old commit and nothing replaced it. it should show the additional colors for verdigris. that is vital to the project otherwise how would other people / me / agents know what those are?"

Restore additional-colors/README.md based on 09a7639^:additional-colors/README.md, with a swatch first and name / hex / role for every entry in current palette/verdigris.json extended and supporting (6 + 5 today). Generate both README and SVG from JSON through build/ so values/roles cannot drift. Homepage additional-colors placeholder targets this restored page, not removal or a substitute palette-notes link.
Do not build the old examples todo (nvim, Obsidian, diffs); mention it only as a possible follow-up.
Visible result: branch only, show GitHub-style rendered README in Sideshow and send preview through Herdra for Algorant's acceptance. No merge until he says yes. No push unless separately needed and approved; local preview preferred.
Existing local 51dfaff documentation fixes from task-8 are the base; the additional-colors retarget within that commit is superseded by this task.

## Algorant correction via Herdra m300d7c40 — supersedes generation/all-11 requirements
Algorant: "additional colors is way too verbose. clean it up. also were some of those adlibbed? I feel like that wasn't what the old additional colors page looked like"
Restore additional-colors/README.md and SVG verbatim from 09a7639^, removing ONLY the ##todo examples line. Keep version, swatch, one original intro paragraph, six-row table with original short roles, and original Oxblood tints text/two-row table. No trials, extra prose/sections/footer, or generator. Remove build/generate-additional-colors.py and its build/README bullet from this branch. Keep homepage additional-colors link. Update SAME Sideshow post 4caGtaNYbmE with GitHub-style render. Deliver one-line diff summary against old page, ideally identical except todo line. Still no merge until Algorant accepts.
## Six additional colors only (Algorant via Herdra m31f095b8) — supersedes literal restoration
Algorant: "I only want the additoinal 6 colors, none of the other nonsense"
Page: version line, swatch displaying ONLY moss/teal/oxblood/goldenrod/deep-copper/ink-violet, one table with old short roles. At most one-line description, no tints/intro essay/trials/examples/footer/generator. Keep homepage link. Edit palette/verdigris.json to remove ochre-alt, brown-green, dark-ochre-trial unless a shipped port actually uses the name or hex; retain used entries and report evidence without changing port. Keep oxblood-text/oxblood-bright in JSON (ports use them), absent from this page. Same branch/post, review gate unchanged. Palette edits now expressly authorized.
## Six-only revision ready for Algorant
Branch additional-colors-reference at 4892e48, unpushed/unmerged. Page now only title, palette version, six-only swatch, one six-row table with historical short roles. No prose/tints/trials/examples/footer/generator. Net diff from 51dfaff is three files only: homepage link and reference README/SVG.
JSON is byte-identical, per explicit shipped-port exception: #d8a65c (ochre-alt) in Leaf inline_code_fg/search_match_bg, Obsidian --v-ochre-deep, Starship color_ochre_alt; #604b29 (brown-green) in btop available_start/used_start/upload_start and Starship color_brown_green; #8b6021 (dark-ochre-trial) in btop used_mid and Starship color_dark_ochre. No port changed; oxblood text/bright tints retained in JSON and absent from page/swatch.
Same Sideshow post 4caGtaNYbmE revised using GitHub Markdown API. Owner verified six table rows, six SVG color groups, all non-page supporting names absent, JSON unchanged; inspected bounded six-only swatch. Manus verified real rendered page has only H1, version paragraph, image and six-row table. Session http://desktop.tail1cefc.ts.net:8228/session/rsnVsfi6go4 returns HTTP 200. Waiting on Algorant.