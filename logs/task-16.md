---
id: task-16
uid: 2c18ac0c-1d08-4f0a-80f7-dd19242c2af2
type: task
kind: "research"
title: "Review omarchy-verdigris-theme README style"
effort: "small"
relatedFiles: ["/home/algorant/Projects/omarchy-verdigris-theme/README.md"]
accord:
  status: "accepted"
  acceptance: ["One Sideshow post shows current and proposed README rendered in GitHub dark, plus a one-line-per-change rationale list.", "Proposed README follows the referenced house style and ends with exactly ## License / [MIT](LICENSE).", "No repository, live theme or published GitHub change is made before Algorant picks."]
  claimedAt: "2026-11-17T15:35:22Z"
  deliveredAt: "2026-11-17T19:44:29Z"
  constraints: ["Suggestions only until Algorant picks.", "Do not change palette, theme identity, wallpapers or live theme installation."]
  summary: "Published approved Showcase variant to omarchy-verdigris-theme at 0017ad1 after Algorant approval relayed in m0aeb1f71."
  evidence: ["Signed-out GitHub page HTTP 200; public README bytes match approved Showcase draft, exact License footer, and all four public image files match local bytes.", "git diff --check passed; commit/push succeeded and main equals origin/main. Only README and approved preview media changed; no theme/live configuration changes.", "Push scan: no findings in one commit, but two PNGs not content-scanned (not a whole-push clean claim). Both are approved existing public images, not new captures."]
  updatedAt: "2026-11-17T19:44:37Z"
createdAt: "2026-11-17T15:35:12Z"
updatedAt: "2026-11-17T19:44:37Z"
assignee: "pi:theme-readme-review"
archivedAt: "2026-11-17T19:44:37Z"
resolution:
  outcome: "completed"
  note: "Merged by worker_finish: main → main at 514491e83581f528a9138e96c9447bcd56107b5d."
---

## Description

Algorant (2026-11-17), relayed by Herdra m63d03e75: "omarchy-verdigris-theme could use a pass for brevity/clarity and assume more of the style/tone we have been setting with my other repos. have a manus review this and make suggestions, with a before/after."

Reference style: his recently approved READMEs — algOS (about 35 lines, banner, plain bullets, collapsed galleries), dotfiles (how it works, one diagram, what it tracks), herdra draft 2, and verdigris itself. Short plain words, lowercase names, no kitchen sink, and the standard final footer: ## License / [MIT](LICENSE).

Deliverable: one Sideshow post with current README and proposed README, both rendered GitHub dark, side by side or sequential, plus a short one-line-each list of what changed and why. Suggestions only: change nothing in the omarchy-verdigris-theme repo until Algorant picks.


Scope addition, Algorant (2026-11-17) relayed by Herdra mf49a5179: "the demo sells it first. algOS and some other repos should also follow this pattern". Standard is Algorant board task-25: stills go in a 2-column "## Screenshots" table with small captions, near the end, before License. Colour schemes need no demo clip. Fold into this mock; push only after he picks.

Planned-extras check (2026-11-17, Herdra mc5958a94): the "Planned extras" list Algorant asked to remove was in verdigris.nvim (added by its bootstrap commit 6ab5e6b, removed in 027c510; see task-17), not in omarchy-verdigris-theme. Neither the current theme README nor this task's proposed draft has any planned / coming soon / roadmap list; keep it that way.

Revision, Algorant (2026-11-17) via Herdra mcbefc713 — revise, not take: "for omarchy-verdigris-theme, it should borrow more from what we've done with algOS and borrow or use similar images. a lot of these were made or done before we created those repos. additionally, the herdr one is just completely outdated now using the old tui style herdr thing and its small and ugly and not meaningful. that one should just be dropped, and the new gallery should have maybe 4-5 images total for how this colorscheme would actually look in day to day omarchy use, not dedicated apps only. again, lost of overlap with what veridgris/algos etc show"
Herdra's brief: model structure/tone on the public Algorant/algOS README (banner, short intro, plain bullets, Screenshots table, License). Gallery 4-5 images of everyday Omarchy in Verdigris (desktop with bar, terminal+editor tiled, launcher/menus, browser or notes window, lock screen), not single-app showcases; reuse/adapt clean public algOS shots, dark only, never the 5 privacy-flagged ones or the pulled clips. Drop the old herdr shot (task-18 verdigris table has no herdr shot). Keep the fixes: false ports list, Super+B, palette link. Re-render before/after GitHub dark in Sideshow session h4KL3kZBrNI.

Heading comparison requested, Algorant via Herdra m0ffe9d9b: "ok for omarchy-verdigris theme. show it to me with 'Gallery' or 'Showcase' as a header vs the current one as well. I want to see it side by side". Revised layout approved in principle only. One bounded render comparison of identical layout/text/media: no heading vs ## Gallery vs ## Showcase immediately before four-shot row, same width/scale/crop, existing supporting post YOHyPr16XYM updated in place. Sole decision via consolidated hub iMTCezlsbAo; no publishing until heading choice.

Algorant heading choice via Herdra mdcf903fc: "Showcase — and 'Showcase' is now the standard heading for every repo". Theme heading decision settled: use ## Showcase before the compact four-image row. Consolidated hub owner must confirm release status before publishing; other repo/media approvals are not inferred.