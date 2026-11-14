---
id: task-14
uid: f7efe7e0-8f0b-47f1-be7b-c10bb4e7e3e7
type: task
title: "Prepare algOS reference cutover"
state: todo
effort: "small"
relatedFiles: ["apps/omarchy/README.md", "apps/atuin/screenshot.tape", "apps/lazygit/screenshot.tape", "apps/tandem/screenshot-2.tape", "apps/btop/screenshot.tape", "apps/tandem/screenshot.tape", "apps/eza/screenshot.tape", "apps/starship/screenshot.tape", "apps/fastfetch/screenshot.tape", "apps/yazi/screenshot.tape"]
accord:
  status: "ready"
  acceptance: ["Full census recorded and naming-only patch prepared with confirmed tape path target.", "Palette and theme identity unchanged; no commit or landing until Herdra signals after folder move."]
  constraints: ["Do not commit until Herdra's explicit signal.", "No live configuration, screenshots, theme or palette changes."]
  updatedAt: "2026-11-14T22:38:53Z"
createdAt: "2026-11-14T22:38:53Z"
updatedAt: "2026-11-14T22:38:53Z"
---

## Description

Herdra relayed Algorant's 2026-11-14 decision (m8c9d9658): full cutover from algomarchy to algOS, capitalized; private Algorant/.algOS at ~/.algOS; future public Algorant/algOS, described as "a tailored Omarchy/Arch setup". Request: "Confirm your own full census, then prepare the naming patch: backlink text/URL to the new names, and tape paths to ~/.algOS. Keep palette and theme identity unchanged. Don't commit until I signal, after the folder move. A link to the public Algorant/algOS can't resolve until it goes public, so word it the way your current link to the private showroom is handled."
Census: 10 lines in 10 files: one backlink, nine tape Screenshot paths. Tape paths are actually ~/.local/state/algomarchy/verdigris-shots/... rather than checkout paths. Clarify target before preparing patch. No source commit or live change authorized yet.
