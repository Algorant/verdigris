---
id: task-10
uid: df5d6dcb-4c07-4a88-bcac-425669a02d68
type: task
title: "Ship a generated Spotifast theme"
state: "in-progress"
effort: "medium"
relatedFiles: ["apps/spotifast/", "build/generate-spotifast.py", "build/README.md"]
accord:
  status: "claimed"
  acceptance: ["Evidence names the actual Omarchy source/generated file and Spotifast keys/mapping used by the installed app.", "Native Spotifast theme file is generated deterministically from canonical palette; exact Omarchy values match.", "Actual Spotifast loader accepts generated file in isolated state, or inability/absence of format is demonstrated with evidence; no mocked parsing validation.", "README links file and explains use without Omarchy and equivalent Omarchy colors in one line.", "Separate committed result reports generator command, load verification and repo/live reach; no live changes."]
  claimedAt: "2026-11-13T04:43:03Z"
  validation: ["$ python3 build/generate-spotifast.py", "$ git diff --check"]
  constraints: ["No live config changes, no launch affecting Algorant's desktop, no new colors.", "Do not run build/generate.py (unrelated outputs, task-7).", "No changes to additional colors reference branch/task-9.", "No push; owner verifies first.", "American spelling."]
  updatedAt: "2026-11-13T04:43:03Z"
createdAt: "2026-11-13T04:42:48Z"
updatedAt: "2026-11-13T04:43:03Z"
assignee: "pi:spotifast-native-theme"
---

## Description

Algorant via Herdra m31676cba (2026-11-13): "spotifast just uses the omarchy colors, we can either copy how its generated for generic omarchy things (but still physically make the theme in the style spotifast expects, or something similar in the readme"
Herdra selects a real theme file in apps/spotifast, separate commit from 51dfaff.
1. Establish exactly how Omarchy currently supplies Spotifast colors: template/generated file, loaded keys, mappings.
2. Generate a native loadable Spotifast theme from palette/verdigris.json through build/, matching Omarchy's output values. Existing information from Algomarchy: system_theme_cache has accent #8ec07c, danger #c66f70, window #1d2021; custom_theme and ~/.config/spotifast/themes accept JSON. Verify against actual install/source, do not assume.
3. README: one line stating it matches Omarchy-generated colors and how to use without Omarchy.
Only if there is no loadable independent format may documentation-only be used, with source/runtime evidence.
No changes to live settings; validate using actual loader or isolated app state. Owner reports file, loading check and commit to Herdra. Additional colors work (task-9) remains an independent branch and approval gate.
