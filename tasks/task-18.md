---
id: task-18
uid: 3da8e025-91b4-4604-ad72-5ad7fa53eb3a
type: task
title: "Move verdigris gallery to Screenshots table"
state: "in-progress"
effort: "small"
relatedFiles: ["README.md"]
accord:
  status: "claimed"
  acceptance: ["README.md has a 2-column ## Screenshots table with small captions, containing the same images and links as the current gallery, placed immediately before ## License.", "Everything else in README.md is unchanged and the License footer stays exactly ## License / [MIT](LICENSE).", "Nothing reaches main or origin/main until Algorant picks from a GitHub-dark rendered preview."]
  claimedAt: "2026-11-17T15:41:01Z"
  validation: ["$ git diff --check main...HEAD", "$ git diff --name-only main...HEAD"]
  constraints: ["README-only change.", "Mock on a branch; no push to main until Algorant picks."]
  updatedAt: "2026-11-17T15:41:01Z"
createdAt: "2026-11-17T15:40:56Z"
updatedAt: "2026-11-17T15:41:01Z"
assignee: "verdigris-screenshots-table"
---

## Description

Algorant (2026-11-17), relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip.

For verdigris: the current 3-column "## gallery" (9 visible + 6 in a "more screenshots" details block) becomes a "## Screenshots" 2-column table with small captions, placed after "how to use" and right before "## License / [MIT](LICENSE)". Keep the banner, palette swatch, intro bullets, os / terminal/cli / apps link sections and how to use unchanged. Keep the same images and links; no new screenshots. Mock first on a branch with a rendered GitHub-dark preview; merge/push to main only after Algorant picks.
