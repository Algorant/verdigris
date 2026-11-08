---
id: task-1
uid: e9e912b4-932a-496a-a7a6-5ae70b3327a2
type: task
kind: "papercut"
title: "Align the push guard with the revised sharing framework"
state: "in-progress"
priority: "low"
effort: "small"
references: ["https://github.com/Algorant/Algorant/blob/main/docs/sharing-framework.md"]
relatedFiles: [".githooks/pre-push", ".gitleaks-privacy.toml"]
accord:
  status: "delivered"
  acceptance: ["The active Verdigris push checks follow the revised sharing framework without rejecting publishable machine, path or network details.", "Credential and personal-record protection remains in place, with hook ownership coordinated with gitguard and the effective checks documented."]
  claimedAt: "2026-11-08T02:35:34Z"
  deliveredAt: "2026-11-08T02:35:42Z"
  summary: "Fixed in 866a369: removed .gitleaks-privacy.toml (home-path, Windows-home, tailnet and private-network rules), so the hook now runs only Gitleaks defaults plus the local untracked identity policy. Also replaced the unapproved gitleaks@8.30.1 pin with @latest and documented the framework in the README."
  evidence: ["Nothing had landed on this card since 2026-10-29 (commits since then were the Herdr theme and oxblood palette); the 2026-10-29 sharing framework makes paths, machine/network names and commit email publishable.", "Real disposable-remote pushes through the edited hook on desktop: a home path and a private IP with a tailnet host both pushed; a GitHub token and the local identity literal were both blocked.", "Real push of 866a369 to origin ran the new hook (default + local policies) with no leaks; origin/main matches.", "Hook ownership coordination stands as agreed with gitguard (m309009d2): Verdigris keeps its tracked hook as sole owner; gitguard uses only a mirror-only log scan, and any later adoption gets a coexistence proposal first. Effective checks documented in README Contributor checks.", "x1nano was offline (tailscale: last seen 1h ago), so its clone picks up 866a369 on its next pull; the hook needs no per-machine change there beyond the existing local literal file."]
  filesChanged: [".githooks/pre-push", ".gitleaks-privacy.toml", "README.md"]
  updatedAt: "2026-11-08T02:35:42Z"
createdAt: "2026-10-29T03:15:55Z"
updatedAt: "2026-11-08T02:35:42Z"
assignee: "pi:verdigris"
---

## Description

The 2026-10-29 sharing framework permits machine names, home paths, network identifiers and commit-author email; only credentials and personal records are private. Verdigris's existing Gitleaks hook still implements the earlier broad path/network/identity blocking policy. This can reject publishable contributions. Coordinate with gitguard's Ceph before changing tool ownership or hook installation; the pilot currently leaves Verdigris's blocking hook untouched.
