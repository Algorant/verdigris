---
id: task-9
uid: fd141598-2ad2-4383-8b6c-54c6759d3847
type: task
title: "Restore additional colors reference"
state: "in-progress"
effort: "medium"
relatedFiles: ["README.md", "additional-colors/", "build/generate-additional-colors.py", "build/README.md", "palette/verdigris.json"]
accord:
  status: "rework"
  acceptance: ["Additional-colors page contains version, six-color-only swatch and one table of the old six short roles; no tints/trials/examples/footer/essay/generator.", "Trial JSON entries ochre-alt/brown-green/dark-ochre-trial removed unless actual shipped-port usage proves retention necessary; no port modified.", "Oxblood-text and oxblood-bright remain in palette JSON but do not appear on the additional-colors page or swatch.", "Homepage link targets additional-colors/ and no generator/docs bullet remains.", "Same Sideshow post 4caGtaNYbmE updated with GitHub-style render, JSON changes reported to Herdra, no merge before approval."]
  claimedAt: "2026-11-13T04:41:44Z"
  deliveredAt: "2026-11-13T04:52:24Z"
  validation: ["$ git diff --check"]
  constraints: ["No live changes, app-port changes, tags or releases.", "Only authorized palette edits are unused trial removals; oxblood text/bright tints retained.", "No palette-to-theme generators.", "No merge until Algorant accepts visible result.", "American spelling."]
  summary: "Generated reference and 11-color swatch delivered on unmerged branch additional-colors-reference at 333d1ea; GitHub-rendered preview published for Algorant."
  evidence: ["Owner ran generator twice: both up to date and worktree clean; exact 11 JSON name/hex/role table rows and matching SVG groups verified.", "Owner inspected bounded 1024px swatch render: all 11 names/hex/roles visible, no clipping.", "Sideshow post 4caGtaNYbmE in rescope session rsnVsfi6go4: README rendered by GitHub Markdown API, github-markdown dark styling; local and MagicDNS session URLs HTTP 200.", "Manus checked render: Obscura table overlap confirmed absent in one-shot Chromium, known renderer gap; no merge/push/live edits."]
  filesChanged: ["README.md", "additional-colors/README.md", "additional-colors/verdigris-additional-colors-swatch.svg", "build/generate-additional-colors.py", "build/README.md"]
  note: "Algorant rejected verbose/ad-libbed restoration. Return to old page/SVG verbatim, remove only todo line, drop generator and its docs, keep homepage link. Same branch and preview post; needs his re-review."
  updatedAt: "2026-11-13T04:55:59Z"
createdAt: "2026-11-13T04:41:25Z"
updatedAt: "2026-11-13T04:55:59Z"
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