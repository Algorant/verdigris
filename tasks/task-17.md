---
id: task-17
uid: bf503f50-5e7c-4a9c-bdd4-5e847c0f074d
type: task
title: "Mock verdigris.nvim README and screenshots"
state: "in-progress"
effort: "medium"
references: ["task-16"]
accord:
  status: "claimed"
  acceptance: ["3-5 same-size headless VHS shots show Verdigris Neovim with README-listed supported plugins/views, using scratch config and demo files with no personal paths or names in frame.", "One Sideshow post shows the shots plus current and proposed README rendered in GitHub dark, with a one-line-per-change rationale.", "Proposed README follows the referenced house style and ends with exactly ## License / [MIT](LICENSE).", "Nothing is committed or pushed to verdigris.nvim and no live Neovim config changes before Algorant picks."]
  claimedAt: "2026-11-17T15:36:08Z"
  constraints: ["Mock only until Algorant picks.", "Headless VHS only; no live screen captures.", "Only plugins/views the README already lists as supported; no palette changes."]
  updatedAt: "2026-11-17T15:36:08Z"
createdAt: "2026-11-17T15:35:56Z"
updatedAt: "2026-11-17T15:40:38Z"
assignee: "pi:nvim-readme-and-shots"
---

## Description

Algorant (2026-11-17), relayed by Herdra mb5ef4810: "similar for verdigris.nvim, it should get some images showing off neovim in particular with some of the listed supported plugins/views"

Herdra's brief: run as a second manus, parallel with the omarchy-verdigris-theme README review (task-16).
1. Screenshots: 3-5 shots of Neovim in Verdigris showing plugins and views the README already lists as supported (e.g. telescope/picker, file tree, git signs/diff, completion menu, statusline, diagnostics). Made headless with VHS tapes in a scratch config with demo files, like verdigris's own terminal shots; check the studio skill. No captures of Algorant's live screen; no personal paths or names in frame. Same size and framing for all.
2. README: before/after brevity pass in the same house style as the theme review (algOS, dotfiles, herdra draft 2, verdigris): short, lowercase, a small gallery, standard final ## License / [MIT](LICENSE) footer.

Deliver one Sideshow post: the shots plus current and proposed README renders, GitHub dark. Mock first: nothing committed or pushed to verdigris.nvim until Algorant picks.


Scope addition, Algorant (2026-11-17) relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip. Fold into this mock; push only after he picks.

Incident (2026-11-17 10:37 EST): scratch `HOME=/tmp/vnvim/home nvim --headless "+Lazy! sync" +qa` loaded Algorant's live ~/.config/nvim and ~/.local/share/nvim because the session exports XDG_CONFIG_HOME/XDG_DATA_HOME/XDG_STATE_HOME/XDG_CACHE_HOME; overriding HOME alone does not isolate Neovim. It moved 9 live plugins (7 mini.*, nvim-treesitter, verdigris) to upstream main and rewrote lazy-lock.json. Herdra decided restore (m8917b9d0): verdigris Ceph ran `mise dot rollback --to 520 ~/.config/nvim/lazy-lock.json` (recorded as checkpoint 522; 521 holds the pre-rollback state) and live `Lazy! restore`; all 9 plugin HEADs match the lock, mise dot shows checkpoint 520 vs 522 and working tree no differences, `:checkhealth lazy` all OK.
Rule for every scratch Neovim run: set HOME and every XDG_* (CONFIG_HOME, DATA_HOME, STATE_HOME, CACHE_HOME) under /tmp (or NVIM_APPNAME with all XDG_* in /tmp), and confirm `:echo stdpath('config')` and stdpath('data') are under /tmp before any Lazy install/sync.