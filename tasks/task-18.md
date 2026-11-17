---
id: task-18
uid: 3da8e025-91b4-4604-ad72-5ad7fa53eb3a
type: task
title: "Move verdigris gallery to Screenshots table"
state: "in-progress"
effort: "small"
relatedFiles: ["README.md"]
accord:
  status: "delivered"
  acceptance: ["README.md has a 2-column ## Screenshots table with small captions, containing the same images and links as the current gallery, placed immediately before ## License.", "Everything else in README.md is unchanged and the License footer stays exactly ## License / [MIT](LICENSE).", "Nothing reaches main or origin/main until Algorant picks from a GitHub-dark rendered preview."]
  claimedAt: "2026-11-17T15:41:01Z"
  deliveredAt: "2026-11-17T15:41:24Z"
  validation: ["$ git diff --check main...HEAD", "$ git diff --name-only main...HEAD"]
  constraints: ["README-only change.", "Mock on a branch; no push to main until Algorant picks."]
  summary: "Replaced the 3-column gallery with a 2-column \"## Screenshots\" table (440px thumbs, small captions) placed after \"how to use\" and right before \"## License\", committed on the worktree branch only (no push)."
  evidence: ["2-column ## Screenshots table, same images/links, immediately before ## License: All 15 images and links kept; width=440 because every thumb is 480x300 (no upscaling, fits GitHub's ~888px column); order after 'how to use', then License. I kept the visible/collapsed split: 10 visible (5 rows) plus 5 in 'more screenshots' (yazi moved into the visible set to make an even count; last collapsed row has one empty cell because 15 is odd).", "Everything else unchanged; License footer exact: Diff only removes the old gallery block and adds the new section; banner, swatch, bullets, os/terminal/cli/apps and how-to-use untouched; '## License / [MIT](LICENSE)' intact.", "Nothing reaches main/origin until Algorant picks from a GitHub-dark preview: Committed on the worktree branch only, not pushed. I did not render a GitHub-dark preview; the parent must produce it for Algorant's pick. git diff --check clean; changed file list is README.md only."]
  filesChanged: ["README.md"]
  updatedAt: "2026-11-17T15:41:24Z"
createdAt: "2026-11-17T15:40:56Z"
updatedAt: "2026-11-17T15:41:24Z"
assignee: "verdigris-screenshots-table"
---

## Description

Algorant (2026-11-17), relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip.

For verdigris: the current 3-column "## gallery" (9 visible + 6 in a "more screenshots" details block) becomes a "## Screenshots" 2-column table with small captions, placed after "how to use" and right before "## License / [MIT](LICENSE)". Keep the banner, palette swatch, intro bullets, os / terminal/cli / apps link sections and how to use unchanged. Keep the same images and links; no new screenshots. Mock first on a branch with a rendered GitHub-dark preview; merge/push to main only after Algorant picks.
