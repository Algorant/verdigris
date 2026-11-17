---
id: task-21
uid: 87153281-4823-4127-9c05-6222ff261f95
type: task
kind: "papercut"
title: "Review Neovim README nitpicks"
state: "todo"
priority: "low"
effort: "small"
references: ["task-17"]
accord:
  status: "blocked"
  acceptance: ["When Algorant asks, complete a bounded README/media nitpick review and address the specific issues he accepts."]
  claimedAt: "2026-11-17T21:41:19Z"
  deliveredAt: "2026-11-17T21:48:08Z"
  constraints: ["Deferred until Algorant asks.", "No live config changes or new captures without approval."]
  summary: "Bounded README nitpick pass with before/after Sideshow post; six small wording/consistency fixes proposed, nothing published"
  evidence: ["Sideshow post http://localhost:8228/p/wLBtz3Qz4Io (session zEYoUgewCLE)", "Proposed commit 2a48ecf in temp clone /tmp/vnvim/polish (11 insertions, 12 deletions); patch /tmp/vnvim/polish-post/readme.diff", "Links verified 200 (13 URLs); headless nvim 0.12.6 load check: colors_name=verdigris, lualine table, setup transparent=false bg=#1d2021"]
  note: "Parked pending Algorant's explicit scoping per m443f2ee2. Both manus closed; no public changes."
  updatedAt: "2026-11-17T21:51:03Z"
createdAt: "2026-11-17T19:47:39Z"
updatedAt: "2026-11-17T21:51:03Z"
---

## Description

Algorant (2026-11-17), relayed by Herdra m163bdda7: "verdigris-nvim similar, looks 90% good just needs a quick review pass for some nitpick outsanding things. filed as papercut to review later".
Follow-up after publishing the approved verdigris.nvim Showcase draft and five shots (task-17). Deferred: do not start until Algorant asks. Review remaining README/media nitpicks with him; do not infer new layout or media changes from the broad request.


Activated today by Algorant via Herdra m9e7a6725 (2026-11-17): "I have an ai meetup to go to and I want all my repos in decent shape before I go so I need to do all tehse polish tasks." Supersedes deferral. One bounded mock pass, aim within the hour, GitHub dark Sideshow post, no publishing until Algorant picks. Read published verdigris.nvim README as a stranger; fix wording, consistency, links and image grid nitpicks in one before/after. No new scope or live config changes.

Algorant restriction via Herdra m6e3eca5e: "stop any vhs captures at the moment. I don't want these automated". No automated VHS/headless captures. Task-20 existing images only, retakes parked; task-21 text-only, images unchanged. Stop any in-flight captures; do not restart.

PARKED by Algorant via Herdra m443f2ee2: "who ordered all this stuff to be done? all these polish tasks seem to require at least some sort of scoping by me before you even start". Previous activation was Herdra's direction, not Algorant-approved scope. Child stopped/closed through worker_discard; nothing published. Restart only after Algorant scopes it. Preserved reference: Sideshow wLBtz3Qz4Io v2; /tmp/vnvim/polish-post/readme.diff; /home/algorant/.local/share/verdigris/parked-polish/nvim-readme-polish.bundle (f6eb438).