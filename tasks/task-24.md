---
id: task-24
uid: cbc93cc9-508f-42c0-868b-746a9578f88e
type: task
title: "Add Pi recap teal"
state: todo
effort: "small"
relatedFiles: ["apps/pi/verdigris.json"]
accord:
  status: "ready"
  acceptance: ["Only vars.recapTeal is added with exact value #5c9fa1; all existing roles, theme values and palette files stay unchanged.", "Source commit reported without editing live configuration."]
  validation: ["$ git diff --check main...HEAD"]
  constraints: ["No live reload or config edits; no push requested."]
  updatedAt: "2026-11-20T20:32:13Z"
createdAt: "2026-11-20T20:32:13Z"
updatedAt: "2026-11-20T20:32:13Z"
---

## Description

Herdra m23727505 relays Algorant’s option C from http://desktop.tail1cefc.ts.net:8228/p/7qbaYD52LII: add only vars.recapTeal = #5c9fa1 in apps/pi/verdigris.json for the new TLDR reply pill. Not canonical palette teal (#458588) or aqua (#83a598); do not substitute or change canonical palette. Source-only commit, notify .pi Ceph and Herdra with commit.
