---
id: task-6
uid: 1535b669-8b69-419b-8fc0-68ca13485f8b
type: task
title: "Port verdigris to lazygit and add its page"
state: "in-progress"
priority: "medium"
effort: "small"
relatedFiles: ["apps/lazygit/", "README.md"]
tags: ["port", "app-page", "verify-with-algorant"]
accord:
  status: "delivered"
  acceptance: ["apps/lazygit/config.yml holds a gui.theme block built only from palette/verdigris.json tokens, and every key it sets exists in lazygit's default theme", "apps/lazygit/README.md follows the page rules and is linked from the homepage terminal/cli list", "Algomarchy has applied the block to his live ~/.config/lazygit/config.yml; he has opened lazygit and answered", "His retaken screenshot replaces the pre-port one in the gallery, md5-checked against his file", "Pushed to main only after his OK, with the branch left local until then"]
  claimedAt: "2026-11-13T03:08:49Z"
  deliveredAt: "2026-11-13T03:11:41Z"
  constraints: ["Commit on a local branch; no push until Algorant answers", "Red is oxblood's text tint #c66f70, never a gruvbox red", "Undo for his live file is removing the gui.theme block"]
  summary: "lazygit ported and published: 11-key gui.theme block from palette 0.2.0, apps/lazygit page with his retake, homepage entry; his live config verified identical by parsing both files."
  evidence: ["main 4bc1fcf apps/lazygit/screenshot.png md5 787410b1fe2e = his retake", "live ~/.config/lazygit/config.yml gui.theme == repo block, 11 keys, no extras", "pre-push check: media only, no findings"]
  filesChanged: ["apps/lazygit/config.yml", "apps/lazygit/README.md", "apps/lazygit/screenshot.png", "apps/lazygit/thumbs/1.jpg", "apps/lazygit/screenshot.tape", "README.md"]
  updatedAt: "2026-11-13T03:11:41Z"
createdAt: "2026-11-13T03:05:14Z"
updatedAt: "2026-11-13T03:11:41Z"
assignee: "verdigris-ceph"
---

## Description

Algorant, via Herdra m4cb0bb98: "added a screenshot for lazygit, this one is brand new so we would need to create all the other stuff for it as well in the repo. make a task and figure all that out then verify it iwth me locally before pushing"

lazygit (jesseduffield/lazygit, pacman 0.66.2) has no verdigris theme: his ~/.config/lazygit/config.yml exists with no gui.theme block, so his 22:02 shot shows lazygit's defaults.

Plan: write the gui.theme block from palette/verdigris.json, add apps/lazygit (README, config.yml, gallery) and list it under terminal/cli on the homepage. Algomarchy applies the block to his live config; he opens lazygit, looks, and retakes the screenshot; only then push.
