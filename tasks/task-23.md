---
id: task-23
uid: e78f0a74-e80e-4ce1-8396-69bce6725cee
type: task
title: "Sharpen Showcase gallery proposal"
state: "in-progress"
effort: "medium"
relatedFiles: ["README.md", "docs/", "apps/"]
accord:
  status: "delivered"
  acceptance: ["Evidence-backed thumbnail proposal with measured widths, DPR targets, format/proxy support, weight and repeatable generation.", "New PR and rendered branch-page link showing both changes; no merge until Algorant's explicit OK.", "One Sideshow post with decision, before/after, options and undo, routed to Herdra only."]
  claimedAt: "2026-11-20T20:17:21Z"
  deliveredAt: "2026-11-20T20:29:32Z"
  constraints: ["Do not change main or publish an approval request directly to Algorant.", "No new captures, original edits, video uploads, or changes to algOS."]
  summary: "Proposal PR #6 (branch sharp-showcase-proposal, commit 61ec194): Omari clip removed from README Showcase with attachment and recipe preserved in docs/showcase-clips.md; all 14 gallery thumbnails regenerated at 880px wide, native aspect, JPEG q85 4:4:4 via new build/thumbs.sh; originals byte-identical; rendered branch page verified from anonymous HTML; real-browser visual gate unverified (paired Chromium offline). One Sideshow post L8C4f7n0P2U in rsnVsfi6go4 with decide box."
  evidence: ["https://github.com/Algorant/verdigris/pull/6", "https://github.com/Algorant/verdigris/blob/sharp-showcase-proposal/README.md", "http://localhost:8228/p/L8C4f7n0P2U"]
  filesChanged: ["build/thumbs.sh", "README.md", "docs/showcase-clips.md", "build/README.md"]
  updatedAt: "2026-11-20T20:29:32Z"
createdAt: "2026-11-20T20:16:58Z"
updatedAt: "2026-11-20T20:29:32Z"
assignee: "pi:sharp-showcase-proposal"
---

## Description

Algorant via Herdra md1dfcb26: “this repo is supposedto show off colorschemes, so just showing some omari functionality makes sense for my .algOS repo showcase, but not for a colorscheme repo. so I'd like to remove omari completely from this showcase area. show me the proposal from your understanding of what I am asking for. this can be a completely new pull request. Additionally, I noticed that the 'thumbnails' for lack of better word in the gallery view are kind of low res. look, and I mean exhaustively look, into how to make those high quality so they don't look blurry when someone visits the site. its just ugly to have that happen. take these into accoutn and show me the conclusion of the proposal/plan.”
Propose removal of Omari clip and caption only, preserve its attachment for algOS. Recommend keeping scrolling as an example of the palette across apps; note no video at all as alternative. Investigate actual GitHub desktop/mobile cell widths; DPR 1/2/3 requirements; Camo processing, cache, limits; supported PNG/JPEG/WebP/AVIF and screenshot text quality; separate thumbs vs rendering originals; aspect/crop, page weight and current generation tooling. Include homepage visible and collapsed images; census per-app sharing, avoid rewriting separate app galleries. Originals unchanged; no captures. Proposal only: push isolated branch and open new PR, inspect rendered branch page, one Sideshow post in rsnVsfi6go4 with decide box, Omari before/after, two same-crop real-display-size comparisons, rejected options, page weights and undo. Herdra reviews first.
