---
id: task-9
uid: fd141598-2ad2-4383-8b6c-54c6759d3847
type: task
title: "Restore additional colors reference"
state: "validation"
effort: "medium"
relatedFiles: ["README.md", "additional-colors/", "build/generate-additional-colors.py", "build/README.md"]
accord:
  status: "delivered"
  acceptance: ["additional-colors/README.md equals 09a7639^:additional-colors/README.md except deletion of the ##todo examples line.", "additional-colors/verdigris-additional-colors-swatch.svg equals the historical SVG byte for byte.", "No build/generate-additional-colors.py, generator documentation bullet, trials, added sections or footer remain on branch.", "Homepage additional colors link still targets additional-colors/.", "Same Sideshow post 4caGtaNYbmE updated with GitHub-style rendered revision, sent to Herdra with exact historical diff; no merge before acceptance."]
  claimedAt: "2026-11-13T04:41:44Z"
  deliveredAt: "2026-11-13T04:52:24Z"
  validation: ["$ git diff --check"]
  constraints: ["No live changes, palette edits, unrelated app-port changes, tags or releases.", "Plain historical files; no generation requirement (superseded by Algorant).", "No merge until Algorant accepts visible result.", "American spelling except exact preserved historical content."]
  summary: "Generated reference and 11-color swatch delivered on unmerged branch additional-colors-reference at 333d1ea; GitHub-rendered preview published for Algorant."
  evidence: ["Owner ran generator twice: both up to date and worktree clean; exact 11 JSON name/hex/role table rows and matching SVG groups verified.", "Owner inspected bounded 1024px swatch render: all 11 names/hex/roles visible, no clipping.", "Sideshow post 4caGtaNYbmE in rescope session rsnVsfi6go4: README rendered by GitHub Markdown API, github-markdown dark styling; local and MagicDNS session URLs HTTP 200.", "Manus checked render: Obscura table overlap confirmed absent in one-shot Chromium, known renderer gap; no merge/push/live edits."]
  filesChanged: ["README.md", "additional-colors/README.md", "additional-colors/verdigris-additional-colors-swatch.svg", "build/generate-additional-colors.py", "build/README.md"]
  updatedAt: "2026-11-13T04:54:05Z"
createdAt: "2026-11-13T04:41:25Z"
updatedAt: "2026-11-13T04:54:05Z"
assignee: "pi:additional-colors-reference"
validation.criterion: "README rendered in GitHub style is published to Sideshow and visually checked, with the preview sent to Herdra."
validation.note: "Awaiting Algorant's approval of the rendered restored reference. Preview http://desktop.tail1cefc.ts.net:8228/session/rsnVsfi6go4, post additional colors reference: restored page. Branch additional-colors-reference at 333d1ea remains unmerged and unpushed; review only, no live settings changed."
validation.requestedAt: "2026-11-13T04:52:26Z"
validation.reviewer: "Algorant"
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