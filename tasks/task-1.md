---
id: task-1
uid: e9e912b4-932a-496a-a7a6-5ae70b3327a2
type: task
kind: "papercut"
title: "Align the push guard with the revised sharing framework"
state: todo
priority: "low"
effort: "small"
references: ["https://github.com/Algorant/Algorant/blob/main/docs/sharing-framework.md"]
relatedFiles: [".githooks/pre-push", ".gitleaks-privacy.toml"]
accord:
  status: "ready"
  acceptance: ["The active Verdigris push checks follow the revised sharing framework without rejecting publishable machine, path or network details.", "Credential and personal-record protection remains in place, with hook ownership coordinated with gitguard and the effective checks documented."]
  updatedAt: "2026-10-29T03:15:55Z"
createdAt: "2026-10-29T03:15:55Z"
updatedAt: "2026-10-29T03:15:55Z"
---

## Description

The 2026-10-29 sharing framework permits machine names, home paths, network identifiers and commit-author email; only credentials and personal records are private. Verdigris's existing Gitleaks hook still implements the earlier broad path/network/identity blocking policy. This can reject publishable contributions. Coordinate with gitguard's Ceph before changing tool ownership or hook installation; the pilot currently leaves Verdigris's blocking hook untouched.
