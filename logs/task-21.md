---
id: task-21
uid: 87153281-4823-4127-9c05-6222ff261f95
type: task
kind: "papercut"
title: "Review Neovim README nitpicks"
priority: "low"
effort: "small"
references: ["task-17"]
accord:
  status: "accepted"
  acceptance: ["When Algorant asks, complete a bounded README/media nitpick review and address the specific issues he accepts."]
  claimedAt: "2026-11-18T14:23:45Z"
  deliveredAt: "2026-11-18T14:37:40Z"
  constraints: ["Deferred until Algorant asks.", "No live config changes or new captures without approval."]
  summary: "Published exact approved v5 scoped Neovim README at e60ccb2 under Algorant approval mb20ad8d2."
  evidence: ["Signed-out GitHub returns HTTP 200, README bytes match /tmp/vnvim/scoped-polish/README.md; five existing screenshot URLs return 200.", "Only README changed; git diff --check passed, push succeeded, clean main equals origin/main.", "One-sentence intro, full-width editor + captioned 2x2, separate diagnostics line and consistent headings verified; no media/code/live configuration changes."]
  updatedAt: "2026-11-18T14:37:44Z"
createdAt: "2026-11-17T19:47:39Z"
updatedAt: "2026-11-18T14:37:44Z"
assignee: "pi:scoped-neovim-polish"
archivedAt: "2026-11-18T14:37:44Z"
resolution:
  outcome: "completed"
  note: "Merged by worker_finish: main → main at 2704e697838f7a0dea382ac28cd1faecb4359c86."
---

## Description

Algorant (2026-11-17), relayed by Herdra m163bdda7: "verdigris-nvim similar, looks 90% good just needs a quick review pass for some nitpick outsanding things. filed as papercut to review later".
Follow-up after publishing the approved verdigris.nvim Showcase draft and five shots (task-17). Deferred: do not start until Algorant asks. Review remaining README/media nitpicks with him; do not infer new layout or media changes from the broad request.


Activated today by Algorant via Herdra m9e7a6725 (2026-11-17): "I have an ai meetup to go to and I want all my repos in decent shape before I go so I need to do all tehse polish tasks." Supersedes deferral. One bounded mock pass, aim within the hour, GitHub dark Sideshow post, no publishing until Algorant picks. Read published verdigris.nvim README as a stranger; fix wording, consistency, links and image grid nitpicks in one before/after. No new scope or live config changes.

Algorant restriction via Herdra m6e3eca5e: "stop any vhs captures at the moment. I don't want these automated". No automated VHS/headless captures. Task-20 existing images only, retakes parked; task-21 text-only, images unchanged. Stop any in-flight captures; do not restart.

PARKED by Algorant via Herdra m443f2ee2: "who ordered all this stuff to be done? all these polish tasks seem to require at least some sort of scoping by me before you even start". Previous activation was Herdra's direction, not Algorant-approved scope. Child stopped/closed through worker_discard; nothing published. Restart only after Algorant scopes it. Preserved reference: Sideshow wLBtz3Qz4Io v2; /tmp/vnvim/polish-post/readme.diff; /home/algorant/.local/share/verdigris/parked-polish/nvim-readme-polish.bundle (f6eb438).

EXPLICIT SCOPE APPROVED by Algorant via Herdra m2408378b (2026-11-17): intro bullets "are just not cohesive and don't go well, they just look crappy"; "why is built-in-lsp diagnostics in that list of supported plugins. why is which-key separated and not highlighted, then there is the random text with editor telescope blink and mini.files and I can't tell what I'm looking at. its not a nice looking showcase." Then "Ok go I await the before/after".
Exact changes only: (1) Replace two bullets with one plain sentence, e.g. "A warm, copper-toned colorscheme for Neovim, part of verdigris." linking verdigris; drop gruvbox/everforest comparison. (2) Showcase editor full width, then 2x2 table telescope, blink.cmp, mini.files, which-key, own small caption under each, no toggle or loose caption. (3) Remove built-in lsp diagnostics from plugin list; add line "Also styles Neovim's built-in LSP diagnostics." below. (4) Consistent heading case matching other repos (Showcase/License are standard capitalized; use sentence case Install/Options/Supported plugins). No other nitpicks, code/media changes or captures. One current-published vs proposed GitHub-dark before/after, publish only after Algorant's OK. Supersedes previous parked scope and unapproved general nitpick draft.