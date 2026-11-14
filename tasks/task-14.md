---
id: task-14
uid: f7efe7e0-8f0b-47f1-be7b-c10bb4e7e3e7
type: task
title: "Prepare algOS reference cutover"
state: "in-progress"
effort: "small"
relatedFiles: ["apps/omarchy/README.md", "apps/atuin/screenshot.tape", "apps/lazygit/screenshot.tape", "apps/tandem/screenshot-2.tape", "apps/btop/screenshot.tape", "apps/tandem/screenshot.tape", "apps/eza/screenshot.tape", "apps/starship/screenshot.tape", "apps/fastfetch/screenshot.tape", "apps/yazi/screenshot.tape"]
accord:
  status: "claimed"
  acceptance: ["Full census recorded and naming-only patch prepared with confirmed tape path target.", "Palette and theme identity unchanged; no commit or landing until Herdra signals after folder move."]
  claimedAt: "2026-11-14T22:39:00Z"
  constraints: ["Do not commit until Herdra's explicit signal.", "No live configuration, screenshots, theme or palette changes."]
  updatedAt: "2026-11-14T22:39:00Z"
createdAt: "2026-11-14T22:38:53Z"
updatedAt: "2026-11-14T22:39:19Z"
assignee: "pi:verdigris"
---
Herdra relayed Algorant's 2026-11-14 full algOS cutover (m8c9d9658). Private repo Algorant/.algOS at ~/.algOS; future public showroom Algorant/algOS. Prepare only; do not commit or land until Herdra signals after folder move. Keep palette/theme identity unchanged.
Own census confirmed 10 lines / 10 files: one backlink and nine tape Screenshot output paths.
Herdra clarified/approved exact targets in m67ac8469 (reply to m7793287a): use /home/algorant/.local/state/algOS/verdigris-shots/... to preserve generated-state separation. Algomarchy owns state namespace move. Backlink approved verbatim: [algOS](https://github.com/Algorant/algOS) — a tailored Omarchy/Arch setup, where this theme is used.
Direct Ceph preparation retained because this is a tightly coupled uncommitted hold for coordinated cutover, not a Worker-ready committed delivery. Await explicit landing signal.