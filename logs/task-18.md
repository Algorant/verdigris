---
id: task-18
uid: 3da8e025-91b4-4604-ad72-5ad7fa53eb3a
type: task
title: "Move verdigris gallery to Screenshots table"
effort: "small"
relatedFiles: ["README.md", "docs/thumbs/", "apps/spotifast/", "apps/leaf/", "apps/flea/", "apps/herdr/"]
accord:
  status: "accepted"
  acceptance: ["README.md has a 2-column ## Screenshots table with small captions, containing the same images and links as the current gallery, placed immediately before ## License.", "Everything else in README.md is unchanged and the License footer stays exactly ## License / [MIT](LICENSE).", "Nothing reaches main or origin/main until Algorant picks from a GitHub-dark rendered preview."]
  claimedAt: "2026-11-17T15:41:01Z"
  deliveredAt: "2026-11-17T19:46:47Z"
  validation: ["$ git diff --check main...HEAD", "$ git diff --name-only main...HEAD"]
  constraints: ["README-only change.", "Mock on a branch; no push to main until Algorant picks."]
  summary: "Replaced README.md with the approved draft (## Showcase above ## os/terminal/cli/apps), committed on the branch only; no media changed."
  evidence: ["Apply approved layout only: README.md copied byte-for-byte from /tmp/verdigris-shot-draft/README.md; the commit touches README.md only, so the privacy media edits are untouched.", "Checks: git diff --check main...HEAD clean; every img src and screenshot link in README.md exists in the tree; ## License / [MIT](LICENSE) still last; working tree clean, not pushed."]
  filesChanged: ["README.md"]
  updatedAt: "2026-11-17T19:47:04Z"
createdAt: "2026-11-17T15:40:56Z"
updatedAt: "2026-11-17T19:47:04Z"
assignee: "verdigris-screenshots-table"
archivedAt: "2026-11-17T19:47:04Z"
resolution:
  outcome: "completed"
  note: "Merged by worker_finish: verdigris-screenshots-table → main at 2704e697838f7a0dea382ac28cd1faecb4359c86."
---

## Description

Algorant (2026-11-17), relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip.

For verdigris: the current 3-column "## gallery" (9 visible + 6 in a "more screenshots" details block) becomes a "## Screenshots" 2-column table with small captions, placed after "how to use" and right before "## License / [MIT](LICENSE)". Keep the banner, palette swatch, intro bullets, os / terminal/cli / apps link sections and how to use unchanged. Keep the same images and links; no new screenshots. Mock first on a branch with a rendered GitHub-dark preview; merge/push to main only after Algorant picks.


Scope addition (2026-11-17), Herdra decided (mb00b5e47), reversible by Algorant: apply algOS's privacy exclusions (omarchy-setup 82568b4 dropped spotifast, leaf, flea, herdr-app, yazi, agents captures) to verdigris and drop the old herdr TUI shot (Algorant on that shot: "completely outdated now using the old tui style herdr thing and its small and ugly and not meaningful"). Verified byte-identical: verdigris apps/spotifast/screenshot.png, apps/leaf/screenshot.png, apps/flea/screenshot.png equal the algOS-dropped files.
1. Screenshots table: replace spotifast and leaf with clean shots (reuse clean public algOS images or headless captures with neutral content).
2. App pages apps/spotifast, apps/leaf, apps/flea, apps/herdr: clean replacement captures, headless and neutral; herdr = the current Herdr app or no image. Where a neutral capture is infeasible without his accounts or private data, propose no image instead.
All of it ships only with Algorant's task-18 pick, re-rendered in Sideshow session rsnVsfi6go4. Nothing pushed before.

Latest layout correction, Algorant via Herdra mec940825: "for verdigris itself: the 'showcase' part should be above the os/terminal/app sections. why is this not cohesive/standardized? for every single other repo we put the images and showcase at the top. 'open with the convincing visual'". Supersedes near-end gallery placement: move current ## Showcase block after intro, before ## os; preserve media/privacy bundle. Principle: lead with convincing visuals; flexibility concerns heading/format, not burying images after the catalog. One bounded preview in existing post sFH7OQheWq4; sole hub iMTCezlsbAo, no publishing before review.