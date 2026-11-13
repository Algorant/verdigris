---
id: task-8
uid: 02511162-db49-4940-b401-da413d3b7d4b
type: task
title: "Close portfolio documentation gaps"
state: "in-progress"
effort: "small"
references: ["algorant task-4", "mdca7870e"]
relatedFiles: ["README.md", "apps/spotifast/README.md", "CHANGELOG.md", "apps/hokum/README.md"]
accord:
  status: "delivered"
  acceptance: ["Additional colors restoration and final README target are handed to the separate restoration Task rather than treated as a removed/retargeted gap.", "Spotifast page says it inherits the Omarchy system theme and needs no separate theme file.", "Changelog describes current coverage and version metadata truthfully, preserving historical palette changes without advertising deleted ports.", "Full-history gitguard result is reported with findings and unverified coverage distinguished.", "Report proposes whether to tag 0.2.0; no tag or release is created.", "Hokum project line points to https://github.com/anomalyco/hokum in the same documentation commit."]
  claimedAt: "2026-11-13T04:38:12Z"
  deliveredAt: "2026-11-13T04:42:19Z"
  constraints: ["No live configuration changes.", "Correct Hokum upstream to anomalyco/hokum; do not change omarchy-setup links.", "Use American spelling.", "Do not push; owner verifies and pushes after integration."]
  summary: "Documentation fixes pushed at 51dfaff; full-history scan reports no findings in 140 commits but 121 unverified media; palette-tag proposal recorded, no tag created. Restored additional colors belongs to task-9."
  evidence: ["51dfaff on origin/main: README link, Spotifast note, changelog corrected, Hokum upstream fixed; omarchy-setup untouched.", "git diff --check passed; additional-colors notes heading/link and palette version independently checked.", "gitguard 0.5.1 scan --all-refs --history: exit 0, 140 commits, no findings; 121 media not verified (1 GIF, 62 JPG, 58 PNG), explicitly not clean.", "Proposal only: annotated palette v0.2.0 tag after task-9 approval and media coverage accounted for; no tag/release created."]
  filesChanged: ["README.md", "CHANGELOG.md", "apps/spotifast/README.md", "apps/hokum/README.md"]
  updatedAt: "2026-11-13T04:42:19Z"
createdAt: "2026-11-13T04:38:01Z"
updatedAt: "2026-11-13T04:42:19Z"
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

## Scope correction from Algorant via Herdra (m65c58576)
Algorant: "hokum is an opencode project with its own github. I only have a specific colorscheme for it". The actual upstream is https://github.com/anomalyco/hokum, not Algorant/hokum. Supersedes the earlier prohibition on editing that link: correct apps/hokum/README.md in the same documentation commit. omarchy-setup stays unchanged.
## Additional colors scope correction (m01044254)
Algorant says the homepage placeholder is for the deleted additional-colors reference, not a link to remove or substitute. Restoration is a separate Task; that Task owns the final README target and visible swatch. task-8's already-integrated palette-notes link is interim and superseded by the restored page. Continue other documentation gaps, version proposal and scan without treating the interim link as fulfilling restoration.
## Delivered
Documentation changes integrated and pushed as 51dfaff42536dcff862162af7b372e070d77255e (README intermediate palette-notes link, Spotifast inheritance note, accurate changelog coverage/version claim, corrected anomalyco/hokum upstream). Additional colors restoration/final homepage target now owned by task-9; no replacement of that requested visible reference is claimed here. omarchy-setup link unchanged.

Full-history command: `gitguard scan --all-refs --history` using gitguard 0.5.1 after integration at 51dfaff. Exit 0. Result: `no findings in 140 commit(s), but 121 item(s) not verified: not clean`; 121 media files unscanned (1 GIF, 62 JPG, 58 PNG). Log: /tmp/verdigris-history-scan-51dfaff.log. No whole-history clean claim; these media remain outside gitguard coverage. Normal push gitleaks checks found no leaks.

Version proposal (not executed): one annotated v0.2.0 tag for the palette/reference baseline, after Algorant accepts task-9's restored visible reference and media review coverage is accounted for. No tag or release now; no automated release machinery. State explicitly that app ports adopt independently and this is the palette version, not a claim of synchronized version headers across ports.