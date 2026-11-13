---
id: task-8
uid: 02511162-db49-4940-b401-da413d3b7d4b
type: task
title: "Close portfolio documentation gaps"
state: "in-progress"
effort: "small"
references: ["algorant task-4", "mdca7870e"]
relatedFiles: ["README.md", "apps/spotifast/README.md", "CHANGELOG.md"]
accord:
  status: "claimed"
  acceptance: ["README additional colors reference resolves to existing palette documentation.", "Spotifast page says it inherits the Omarchy system theme and needs no separate theme file.", "Changelog describes current coverage and version metadata truthfully, preserving historical palette changes without advertising deleted ports.", "Full-history gitguard result is reported with findings and unverified coverage distinguished.", "Report proposes whether to tag 0.2.0; no tag or release is created."]
  claimedAt: "2026-11-13T04:38:12Z"
  constraints: ["No live configuration changes.", "Do not change Hokum or omarchy-setup links.", "Use American spelling.", "Do not push; owner verifies and pushes after integration."]
  updatedAt: "2026-11-13T04:38:12Z"
createdAt: "2026-11-13T04:38:01Z"
updatedAt: "2026-11-13T04:38:12Z"
assignee: "verdigris"
---

## Description

Herdra request mdca7870e (portfolio review at 55ad1e7; source: algorant task-4):
1. README:8 — the `[additional colors]` reference has no target; point it somewhere or drop it.
2. spotifast — screenshots but no theme file and no note saying why (flea and nvim have one); add the one-line reason.
3. CHANGELOG — still cites the deleted bat and Windows Terminal pages, and claims every theme file names its palette version (2 of 19 do). Make it true.
4. Version story — palette is 0.2.0 with no tag or release. Propose tag-or-not in your report; don't tag yet.
5. After those land, one full-history gitguard pass (the last was at 6aa49f7).
Leave Algorant/hokum and omarchy-setup links unchanged; their publication is Algorant's call.
Owner performs final full-history scan and version recommendation after documentation lands; Worker handles the three documentation fixes only.
