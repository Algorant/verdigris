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
  acceptance: ["Restored additional-colors README and SVG swatch are generated from all extended and supporting JSON entries, with name, hex and exact role.", "Homepage additional colors link points to the restored page.", "Two generator runs produce identical tracked outputs and no unrelated app files.", "README rendered in GitHub style is published to Sideshow and visually checked, with the preview sent to Herdra.", "Branch is left unmerged pending Algorant's yes; old examples todo is follow-up only."]
  claimedAt: "2026-11-13T04:41:44Z"
  deliveredAt: "2026-11-13T04:52:24Z"
  validation: ["$ python3 build/generate-additional-colors.py", "$ git diff --check"]
  constraints: ["No live changes, palette edits, app-port regeneration, tags or releases.", "No merge until Algorant accepts visible result.", "American spelling."]
  summary: "Generated reference and 11-color swatch delivered on unmerged branch additional-colors-reference at 333d1ea; GitHub-rendered preview published for Algorant."
  evidence: ["Owner ran generator twice: both up to date and worktree clean; exact 11 JSON name/hex/role table rows and matching SVG groups verified.", "Owner inspected bounded 1024px swatch render: all 11 names/hex/roles visible, no clipping.", "Sideshow post 4caGtaNYbmE in rescope session rsnVsfi6go4: README rendered by GitHub Markdown API, github-markdown dark styling; local and MagicDNS session URLs HTTP 200.", "Manus checked render: Obscura table overlap confirmed absent in one-shot Chromium, known renderer gap; no merge/push/live edits."]
  filesChanged: ["README.md", "additional-colors/README.md", "additional-colors/verdigris-additional-colors-swatch.svg", "build/generate-additional-colors.py", "build/README.md"]
  updatedAt: "2026-11-13T04:52:24Z"
createdAt: "2026-11-13T04:41:25Z"
updatedAt: "2026-11-13T04:52:26Z"
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
