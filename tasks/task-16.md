---
id: task-16
uid: 2c18ac0c-1d08-4f0a-80f7-dd19242c2af2
type: task
kind: "research"
title: "Review omarchy-verdigris-theme README style"
state: "in-progress"
effort: "small"
relatedFiles: ["/home/algorant/Projects/omarchy-verdigris-theme/README.md"]
accord:
  status: "delivered"
  acceptance: ["One Sideshow post shows current and proposed README rendered in GitHub dark, plus a one-line-per-change rationale list.", "Proposed README follows the referenced house style and ends with exactly ## License / [MIT](LICENSE).", "No repository, live theme or published GitHub change is made before Algorant picks."]
  claimedAt: "2026-11-17T15:35:22Z"
  deliveredAt: "2026-11-17T15:40:32Z"
  constraints: ["Suggestions only until Algorant picks.", "Do not change palette, theme identity, wallpapers or live theme installation."]
  summary: "Proposed README drafted (99→71 lines, 753→311 words); one Sideshow post with GitHub-dark renders of today, proposed (collapsed and open), one-line change list and source. Awaiting Algorant's pick; nothing changed in the theme repo."
  evidence: ["Sideshow session http://localhost:8228/session/h4KL3kZBrNI (also http://desktop.tail1cefc.ts.net:8228/session/h4KL3kZBrNI, both HTTP 200), post F6Qs6-XPqYU", "Draft: /tmp/theme-readme-review/proposed/README.md; ends with ## License / [MIT](LICENSE)", "Theme repo git status clean at c9a8c33 (origin/main same); no edit, commit or push", "Facts checked against repo: 28 backgrounds (2 triptychs + 26), 5 previews, colors.toml slots; verdigris/apps lacks lsd, bat, ncspot, Claude Code; stock omarchy has no Super+B wallpaper binding"]
  updatedAt: "2026-11-17T15:40:32Z"
createdAt: "2026-11-17T15:35:12Z"
updatedAt: "2026-11-17T15:45:46Z"
assignee: "pi:theme-readme-review"
---

## Description

Algorant (2026-11-17), relayed by Herdra m63d03e75: "omarchy-verdigris-theme could use a pass for brevity/clarity and assume more of the style/tone we have been setting with my other repos. have a manus review this and make suggestions, with a before/after."

Reference style: his recently approved READMEs — algOS (about 35 lines, banner, plain bullets, collapsed galleries), dotfiles (how it works, one diagram, what it tracks), herdra draft 2, and verdigris itself. Short plain words, lowercase names, no kitchen sink, and the standard final footer: ## License / [MIT](LICENSE).

Deliverable: one Sideshow post with current README and proposed README, both rendered GitHub dark, side by side or sequential, plus a short one-line-each list of what changed and why. Suggestions only: change nothing in the omarchy-verdigris-theme repo until Algorant picks.


Scope addition, Algorant (2026-11-17) relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip. Fold into this mock; push only after he picks.

Planned-extras check (2026-11-17, Herdra mc5958a94): the "Planned extras" list Algorant asked to remove was in verdigris.nvim (added by its bootstrap commit 6ab5e6b, removed in 027c510; see task-17), not in omarchy-verdigris-theme. Neither the current theme README nor this task's proposed draft has any planned / coming soon / roadmap list; keep it that way.