---
id: task-9
uid: fd141598-2ad2-4383-8b6c-54c6759d3847
type: task
title: "Restore additional colors reference"
state: "in-progress"
effort: "medium"
relatedFiles: ["README.md", "additional-colors/", "build/generate-additional-colors.py", "build/README.md"]
accord:
  status: "claimed"
  acceptance: ["Restored additional-colors README and SVG swatch are generated from all extended and supporting JSON entries, with name, hex and exact role.", "Homepage additional colors link points to the restored page.", "Two generator runs produce identical tracked outputs and no unrelated app files.", "README rendered in GitHub style is published to Sideshow and visually checked, with the preview sent to Herdra.", "Branch is left unmerged pending Algorant's yes; old examples todo is follow-up only."]
  claimedAt: "2026-11-13T04:41:44Z"
  validation: ["$ python3 build/generate-additional-colors.py", "$ git diff --check"]
  constraints: ["No live changes, palette edits, app-port regeneration, tags or releases.", "No merge until Algorant accepts visible result.", "American spelling."]
  updatedAt: "2026-11-13T04:41:44Z"
createdAt: "2026-11-13T04:41:25Z"
updatedAt: "2026-11-13T04:41:44Z"
assignee: "pi:additional-colors-reference"
---

## Description

Algorant via Herdra m01044254:
"where in the new repo are we showing what those colors are? we had it in an old commit and nothing replaced it. it should show the additional colors for verdigris. that is vital to the project otherwise how would other people / me / agents know what those are?"

Restore additional-colors/README.md based on 09a7639^:additional-colors/README.md, with a swatch first and name / hex / role for every entry in current palette/verdigris.json extended and supporting (6 + 5 today). Generate both README and SVG from JSON through build/ so values/roles cannot drift. Homepage additional-colors placeholder targets this restored page, not removal or a substitute palette-notes link.
Do not build the old examples todo (nvim, Obsidian, diffs); mention it only as a possible follow-up.
Visible result: branch only, show GitHub-style rendered README in Sideshow and send preview through Herdra for Algorant's acceptance. No merge until he says yes. No push unless separately needed and approved; local preview preferred.
Existing local 51dfaff documentation fixes from task-8 are the base; the additional-colors retarget within that commit is superseded by this task.
