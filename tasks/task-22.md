---
id: task-22
uid: cace500e-e1bd-40f7-8b68-1255dcdebd65
type: task
title: "Complete per-app screenshot coverage"
state: "in-progress"
effort: "medium"
references: ["task-20"]
relatedFiles: ["apps/", "README.md", "review/"]
accord:
  status: "claimed"
  acceptance: ["Complete inventory lists every supported discrete app/config port, including nested app/config folders when appropriate; count reported to Herdra.", "Local review/index.html shows one card per inventoried port with existing images, size/spec status, approvals persisted to a small file, and replacement files picked up from review/<app>/ on refresh.", "Proposed 1600x1000 dark single-window PNG spec is clearly awaiting Algorant confirmation.", "Per-app README drafts use one short screenshot-first template and top-level README links to them.", "No captures by agents and no public changes before Algorant approval."]
  claimedAt: "2026-11-18T14:45:44Z"
  constraints: ["Agents make NO screenshots/captures; Algorant supplies retakes.", "Review page stays local, not published.", "Preserve privacy exclusions; do not resurrect removed private images.", "Showcase selection deferred until full coverage."]
  updatedAt: "2026-11-18T14:45:44Z"
createdAt: "2026-11-18T14:45:15Z"
updatedAt: "2026-11-18T14:45:44Z"
assignee: "pi:per-app-screenshot-review"
---

## Description

Algorant (2026-11-18), relayed by Herdra m50fdc4e8: "for polish 3/6 I want the retakes first. this is a rescope of the initial ask or a new task which supercedes it. I want to get compelete, high res coverage of every single app or colorscheme config I support in the repo. it will be placed in that repo along with the standardized readme and be available there for reference from the parent top level readme."
Earlier words, relayed in the same request: "you create me a quick html document I can scroll through and either approve, or reupload an image for each discrete colorscheme thing ... the minimum is 1 good uniform one. we keep a cohesive style and sizing for all screenshots. high quality that actually display what needs to be shown off."

Supersedes parked task-20; Showcase selection happens only after full coverage.
1. Inventory every supported app/colorscheme config (each port/app folder) and list it.
2. Standardized per-app README in each app folder: same short template, screenshots at top; top-level README links to them.
3. Local review page review/index.html in the repo, NOT published: one card per app, current image(s), size/spec check, Approve, Replace. Replace means Algorant saves a file into review/<app>/ and the card shows it on refresh. Approvals saved to a small file; implement a minimal local persistence path as needed, no external services or new network infrastructure.
4. Spec proposed on page for Algorant to confirm: 1600x1000 (16:10), dark Verdigris, single window, no desktop clutter, PNG.
Algorant takes retakes himself; agents make NO captures. Report review page path/URL and inventory count first. No publication of the page, pending images or README changes until approval.
