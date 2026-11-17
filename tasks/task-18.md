---
id: task-18
uid: 3da8e025-91b4-4604-ad72-5ad7fa53eb3a
type: task
title: "Move verdigris gallery to Screenshots table"
state: "in-progress"
effort: "small"
relatedFiles: ["README.md", "docs/thumbs/", "apps/spotifast/", "apps/leaf/", "apps/flea/", "apps/herdr/"]
accord:
  status: "delivered"
  acceptance: ["README.md has a 2-column ## Screenshots table with small captions, containing the same images and links as the current gallery, placed immediately before ## License.", "Everything else in README.md is unchanged and the License footer stays exactly ## License / [MIT](LICENSE).", "Nothing reaches main or origin/main until Algorant picks from a GitHub-dark rendered preview."]
  claimedAt: "2026-11-17T15:41:01Z"
  deliveredAt: "2026-11-17T16:03:56Z"
  validation: ["$ git diff --check main...HEAD", "$ git diff --name-only main...HEAD"]
  constraints: ["README-only change.", "Mock on a branch; no push to main until Algorant picks."]
  summary: "Removed both obsidian captures (screenshot-2 isn't neutral either: its tabs show \"Movies TBW\" and \"Shows TBW\"), rebalanced the table to 10 visible + 4 collapsed, committed on the branch only, not pushed."
  evidence: ["Remove obsidian.png from table and apps/obsidian; rebalance to even rows: Deleted screenshot.png, thumbs/2.jpg, docs/thumbs/obsidian.jpg (only the table used it), and removed the page's image table; nothing else references them (git grep clean). Table is now 14 entries in 7 even rows: 10 visible (omarchy, omarchy keybindings, ghostty, neovim lazy, workstation, leaf, btop, calendar widget, yazi, neovim) plus 4 collapsed (system monitor, atuin, tandem, starship); I moved neovim up from the collapsed block, so no empty cell remains.", "Keep screenshot-2.png only if neutral apart from the sidebar: Not kept, so apps/obsidian now has no image. Main note 'Theme Testing' is neutral, but the tab bar shows 'Home', 'Movies TBW', 'Shows TBW' (the same watch lists), and the sidebar shows vault 'MasterVault' with folders Agentic, Dashboards, Knowledge Base, Mediafetch, Misc, New Notes, Projects, Publishing, Task Management, Work, plus journal-by-day.png and journal-by-project.png. Restoring it is `git checkout main -- apps/obsidian/screenshot-2.png apps/obsidian/thumbs/1.jpg` plus the page table, if Algorant accepts the tab and sidebar names.", "Branch only, no push: Committed on the worktree branch; git diff --check main...HEAD clean; not pushed. No other screenshots changed."]
  filesChanged: ["README.md", "apps/obsidian/README.md", "apps/obsidian/screenshot.png", "apps/obsidian/screenshot-2.png", "apps/obsidian/thumbs/1.jpg", "apps/obsidian/thumbs/2.jpg", "docs/thumbs/obsidian.jpg"]
  updatedAt: "2026-11-17T16:03:56Z"
createdAt: "2026-11-17T15:40:56Z"
updatedAt: "2026-11-17T16:03:56Z"
assignee: "verdigris-screenshots-table"
---

## Description

Algorant (2026-11-17), relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip.

For verdigris: the current 3-column "## gallery" (9 visible + 6 in a "more screenshots" details block) becomes a "## Screenshots" 2-column table with small captions, placed after "how to use" and right before "## License / [MIT](LICENSE)". Keep the banner, palette swatch, intro bullets, os / terminal/cli / apps link sections and how to use unchanged. Keep the same images and links; no new screenshots. Mock first on a branch with a rendered GitHub-dark preview; merge/push to main only after Algorant picks.


Scope addition (2026-11-17), Herdra decided (mb00b5e47), reversible by Algorant: apply algOS's privacy exclusions (omarchy-setup 82568b4 dropped spotifast, leaf, flea, herdr-app, yazi, agents captures) to verdigris and drop the old herdr TUI shot (Algorant on that shot: "completely outdated now using the old tui style herdr thing and its small and ugly and not meaningful"). Verified byte-identical: verdigris apps/spotifast/screenshot.png, apps/leaf/screenshot.png, apps/flea/screenshot.png equal the algOS-dropped files.
1. Screenshots table: replace spotifast and leaf with clean shots (reuse clean public algOS images or headless captures with neutral content).
2. App pages apps/spotifast, apps/leaf, apps/flea, apps/herdr: clean replacement captures, headless and neutral; herdr = the current Herdr app or no image. Where a neutral capture is infeasible without his accounts or private data, propose no image instead.
All of it ships only with Algorant's task-18 pick, re-rendered in Sideshow session rsnVsfi6go4. Nothing pushed before.