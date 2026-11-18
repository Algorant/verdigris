---
id: task-22
uid: cace500e-e1bd-40f7-8b68-1255dcdebd65
type: task
title: "Complete per-app screenshot coverage"
state: "in-progress"
effort: "medium"
references: ["task-20"]
relatedFiles: ["apps/", "README.md", "review/"]
accord:
  status: "claimed"
  acceptance: ["Complete inventory lists every supported discrete app/config port, including nested ones; count reported to Herdra.", "Local review/index.html shows one card per port, persisted per-image selections/approvals, and add-image workflow; dimensions informational only, no fixed-size gating.", "Algorant's selected approved media retained byte-for-byte, no crop/resize or captures by agents.", "Per-app README drafts for the 24 approved sets use one short screenshot-first template; top-level README links to them; drafts shown before publishing.", "Unapproved/missing ports remain explicit: hyprland/omari clips, floating terminal, ai-coding-plans and yazi approvals."]
  claimedAt: "2026-11-18T14:45:44Z"
  constraints: ["Agents make NO screenshots/captures; Algorant supplies retakes.", "Review page stays local, not published.", "Preserve privacy exclusions; do not resurrect removed private images.", "Showcase selection deferred until full coverage."]
  updatedAt: "2026-11-18T15:33:59Z"
createdAt: "2026-11-18T14:45:15Z"
updatedAt: "2026-11-18T16:05:44Z"
assignee: "pi:per-app-screenshot-review"
---

## Description

Algorant (2026-11-18), relayed by Herdra m50fdc4e8: "for polish 3/6 I want the retakes first. this is a rescope of the initial ask or a new task which supercedes it. I want to get compelete, high res coverage of every single app or colorscheme config I support in the repo. it will be placed in that repo along with the standardized readme and be available there for reference from the parent top level readme."
Earlier words, relayed in the same request: "you create me a quick html document I can scroll through and either approve, or reupload an image for each discrete colorscheme thing ... the minimum is 1 good uniform one. we keep a cohesive style and sizing for all screenshots. high quality that actually display what needs to be shown off."

Supersedes parked task-20; Showcase selection happens only after full coverage.
1. Inventory every supported app/colorscheme config (each port/app folder) and list it.
2. Standardized per-app README in each app folder: same short template, screenshots at top; top-level README links to them.
3. Local review page review/index.html in the repo, NOT published: one card per app, current image(s), size/spec check, Approve, Replace. Replace means Algorant saves a file into review/<app>/ and the card shows it on refresh. Approvals saved to a small file; implement a minimal local persistence path as needed, no external services or new network infrastructure.
4. Spec proposed on page for Algorant to confirm: [superseded agent-proposed size] (16:10), dark Verdigris, single window, no desktop clutter, PNG.
Algorant takes retakes himself; agents make NO captures. Report review page path/URL and inventory count first. No publication of the page, pending images or README changes until approval.


Review UX revision approved by Algorant via Herdra mecd7291c: "the screenshot review tool is not that useful for me. I want to be able to look at one card at a time and then hit a button to go to the next one. while on a card, I want the ability to pick and choose which images to use, if there are multiple, and add new ones to pick from. if that is not easily achievable in a simple html file, then we do a pass of the approved ones and then a second pass of the ones that need new images, one at a time, and I capture them."
Use existing serve.py: one port per screen; Prev/Next plus arrow keys; spec status per image; use/skip toggle per image; Add image button/drop zone saves uploads into review/<app>/; persist selections. Keep one small page. If not simple, stop and report for two-pass alternative. Algorant views desktop; loopback sufficient. No captures by agents, no publication, README drafts still held.

Media-type exception, Algorant via Herdra m2432f3ea while reviewing: "things like hyprland and omari will have to be videos we turn into webp's. not useful to show screenshots vs a quick video or gif." Mark hyprland and omari cards video: Algorant records; agents later encode short sped-up looping animated WebP, approximately 2–3 MB, displayed full width. No capture or encoding now; review in progress and more directions may follow. This overrides PNG/still spec only for these two ports.

AUTHORITATIVE CORRECTION from Algorant via Herdra m0ae33465: "I never said 1600x1000 was the approved standard, you just picked that. the other format is how I take screenshots on my computer. I don't need that to be changed or anchored to anything else. if I approved one with the previous resolution then that is ok."
No fixed resolution requirement. Algorant's own capture sizes (mostly 2560×1440) are normal; approved shots at any prior sizes stand as-is. Remove resolution/spec gating from review page; actual dimensions can remain informational only. No crop/resize/transformation. Prior proposed size and any recorded spec checkbox are superseded, not authority for size restrictions.
Proceed with standardized per-app README DRAFTS for the 24 currently approved sets using exact selected original media. Show drafts to Herdra before publication. Leftovers: hyprland/omari clips, floating terminal, approve clicks on ai-coding-plans/yazi. No new captures/encoding or public changes.

Publication approved by Algorant via Herdra m5c8d781c (2026-11-18): "high res screenshots approved make the changes and merge". Apply reviewed drafts at 929a614: 24 sets, 43 exact originals, no transforms; existing parent widgets content and pending ai-coding-plans preserved, top-level navigation intact. Only app READMEs/media ship; local review tool/runtime is not published. Task stays OPEN for hyprland/omari clips, floating-terminal, ai-coding-plans/yazi approvals. Owner verifies signed-out GitHub after merge/push.

Additional explicit media/publication approval, Algorant via Herdra mb9c1a698: "oh, then yes approved I don't need to click on it I'm telling you they are approved". yazi and ai-coding-plans selected images approved verbally; no page click needed. Include both with same README template in current publication: 26 sets / 49 originals (43 + 3 + 3), no transforms. Leftovers now ONLY hyprland/omari clips and floating terminal. Preserve source selection evidence; no need to fabricate page interaction.

LANDED milestone: 7936c90 merged via Worktrunk and pushed to origin/main. 26 approved sets / 49 original files hash-verified byte-for-byte by owner; all publication changes under apps/, local review tool/runtime excluded. Signed-out GitHub index + leaf/tandem/yazi/widget parent/ai-coding-plans pages return 200 and raw README bytes match, their images load; review/index.html returns 404 upstream. Push scan: no text findings, 32 PNG files unverified by content scanner (not fully clean). Publication worktree removed after integration; review worktree/server/selections/uploads preserved. Task remains OPEN only for hyprland/omari clips and floating terminal. No new captures/transforms/live config changes.

Clip editing scope approved by Algorant via Herdra mffe6bf35: "they are too crappy quality. these should be high res renders of what the recording showed, high as possible, within github limits. second. for scrolling: the important part to show is the 'transition' between terminals or different windows going left to right. if the video is sped up too much, it doesn't really highlight those well. for omari: the important parts are the alt+tab and the super+tab sections. those can be slowed down and emphasized. re-do them with this in mind."
Use ORIGINAL source recordings from ~/Videos (resolve via algOS/omarchy-setup history), NOT low-res recovered WebPs in ~/Videos/recovered-demos (from b81aab9). Scrolling near-real-time transitions, dead time trimmed; omari alt+tab/super+tab focused and slightly slowed. Full source resolution/high quality, recommend animated WebP <=10MB or MP4 <=100MB if necessary. Old clips were pulled for privacy (Slack/address/private repos/herdra source): remove unsafe sections, report exact cuts. No new captures; show both playing in ONE Sideshow post for approval before commits/publication.