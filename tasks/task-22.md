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
updatedAt: "2026-11-20T20:04:10Z"
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

## Clip source findings and privacy blocker (agent, 2026-11-18)

Original recordings (full-resolution sources; local copies of the x1nano files):
- scrolling: `/home/algorant/Pictures/algOS-showroom/x1-videos-20261115/2026-11-15_22.53_screen.mp4` — 28.13 s, 2160x1350, 120 fps.
- omari: `/home/algorant/Pictures/algOS-showroom/x1-videos-20261115/2026-11-15_22.55_zen.mp4` — 26.13 s, 2124x1278, 120 fps.
- Excluded after content check: `2026-11-15_22.47_screen.mp4` (static desktop, one window), `2026-11-15_22.52_screen.mp4` (editor only), `2026-11-15_23.48_screen.mp4` and `2026-11-15_23.47_hex.mp4` (Hex dictation).

Privacy scan (bounded; timestamps only, sensitive strings omitted):
- omari: private windows are visible throughout, and the overview/alt-tab actions show them as thumbnails, so the important alt+tab and super+tab cannot be shown without exposure. Approximate exposed spans: 0.0-1.5, 4.0-4.5, 5.0-7.0, 7.5-9.5, 9.5-10.5, 11.0-12.5, 13.0-14.0, 15.0-16.5, 18.0-19.5, 20.0-22.5, 23.0-23.5 s; the overview frames between them expose the same windows.
- scrolling: private project-name listings at 5.0-10.0, 16.0-19.5 and 25.5-28.0 s; private source code in the editor at 10.5-12.5 and 23.5-25.5 s. The left-to-right transitions land on those windows around 16.5-17.0, 22.7-23.3 and 25.0-25.7 s. Clean spans are desktop/plain-terminal only: 0.0-4.8, 12.6-15.9 and 19.6-21.5 s.

Status: no capture, encode, post or repo change made. Blocker escalated for direction: neutral re-records, or an explicit allowance for scrolling directory names only, with private source and omari exposure still cut. Do not treat any private material above as approved.


Scrolling-specific privacy exception, Algorant via Herdra m57170612: "I will allow folder names in the clip. I need to see the clips though. are they recreated?" Encode scrolling only from original x1 22.53_screen recording; Projects/Yazi folder names permitted, near-real-speed left/right transitions, full source resolution, high quality ≤10MB WebP or report MP4 need. Cut all Herdra-source frames around 10.5–12.5s and 23.5–25.5s with safe boundaries. One PLAYING Sideshow preview + cut note, no commits. Omari remains blocked pending neutral human re-record. No new captures.

New demo scope supersedes the old clip drafts for Showcase, Algorant via Herdra mbf6960e7 (2026-11-20): "I recorded two new clips. I don't want any 'personal' information guard blocking anything. that should be informational only (for this specific use case). First clip should show the clean, high quality transition between windows of terminal, browser, OBS studio. omari will be teh same, except highlight the super+tab and alt+tab functions so that its clear what is going on. quality is of highest importance. it needs to be clear what is going one, regardless of end format/size. I want this to be the demo we put on github, right 'start with the obvious' or whatever the wording was"
Identify ~/Videos/2026-11-20_09.14_screen.mp4 and 09.16_screen.mp4 by content. Full source 2560×1440 frame, no crop/downscale. Quality and clarity first, no WebP cap. Verify shortcut timing for Verdigris-styled labels on Omari only. Privacy observations informational for these two clips only. Plan and one playable draft of each in existing Sideshow session, with recommended GitHub format/placement. No commit or public upload before review.

Quality priority clarified by Algorant via Herdra mf8d98a8f: "focus on what my end goal is, to have a clip that shows very clearly in high quality what I want to show, and not some arbitrary size or format constraint". Judge editing, fps, encoding, overlays and delivery by viewer clarity. If a host or upload cap would cost clarity, use a suitable approved preview route or recommend another publication route; no degradation to fit a cap. Keep public changes gated.

Trim and speed direction from Algorant via Herdra mbd92eedd (2026-11-20): "good start but here are some nits 1)they are too long and don't show the basic function in a simple way. they can be trimmed down and sped up. likely being no longer than 10 seconds each. this is not rocket surgery. I just need to show switching between windows and what happens when someone wants to use omari style switchers. thats it"

Applied in the same Sideshow post (vdSAK32VdQk):
- Scrolling preview trimmed to 6.2 s: one continuous 14.4-20.6 s span from 2026-11-20_09.14_screen.mp4, 1x; five clean browser/terminal/OBS switches; waits removed by trimming.
- Omari preview trimmed to 8.5 s: 0.0-2.5 s overview, 19.0-22.0 s switcher, 41.0-44.0 s overview from 2026-11-20_09.16_screen.mp4, 1x; Super + Tab labels, Alt + Tab still a draft label.
Both full 2560x1440, 60 fps, H.264 CRF 18; 2,213,658 and 746,121 bytes. No commit or public upload.


Showcase clip review, Algorant via Herdra mbac58037 (2026-11-20): "for verdigris: first one is approved, for just scrolling view. second one, omari, needs work. doesn't clearly show how alt+tab and super+tab work in an easy to digest way for a human."

- Scrolling clip APPROVED as-is (6.2 s, 2560x1440, 60 fps, current post version). Keep unchanged.
- Omari rework blocked by source clarity in 2026-11-20_09.16_screen.mp4: the Super+Tab overview appears only as three empty window outlines, with no window content/thumbnails captured, so a keycap + "overview of all windows" caption would overclaim what the recording shows. The Alt+Tab portion does show a populated switcher and a landing window (19.0-22.0 s), but the press itself is not recorded (no keycast).
- Proposed exact re-record sequence instead of forcing the overlay: (1) start on a full browser window, press Super+Tab once, hold until the overview shows visible window thumbnails, pause 1 s, select OBS Studio, release, hold the landed OBS window 1 s. (2) beat on the landed window 1 s. (3) press Alt+Tab once, cycle one step to the browser, release, hold the landed browser 1 s. Full 2560x1440/120 fps, no menus or app launcher in frame; ~9-11 s raw.
- No forced Omari update published; post vdSAK32VdQk keeps the approved scrolling clip and the existing Omari draft until a clear re-record exists. No commit.


Omari re-record delivered, Algorant via Herdra md3894027 (2026-11-20): "Ok I re-recorded something you can definitely clip out some simple things from for omari. please help me just finish this. it should show 5-10 seconds of the basic functionality. its ok if sometimes they are empty when selected or previews are broken, thats fine."

- New source: /home/algorant/Videos/2026-11-20_10.00_screen.mp4 (77.2 s, 2560x1440/120 fps).
- Finished Omari basics clip: 7.0 s, 2560x1440, 60 fps, H.264 CRF 18, 2,596,363 bytes. Spans 58.0-62.5 s (Super+Tab overview, empty placeholders expected) + 0.3 s beat + 32.4-34.6 s (Alt+Tab cycling recent windows), all 1x.
- Keycap + one-line caption per action: "Super + Tab — overview of all windows" at 0.2-4.4 s; "Alt + Tab — cycle recent windows" at 4.9-6.9 s.
- Replaced in post vdSAK32VdQk; scrolling clip stays approved and unchanged. No commit or public upload.


Showcase playback diagnosis and Omari recut (2026-11-20, agent):
- Playback failure proven from the pasted screenshot: both players show "No video with supported format and MIME type found." Root cause: Sideshow serves uploaded files as application/octet-stream with Content-Disposition: attachment and X-Content-Type-Options: nosniff, and the embeds used absolute localhost URLs, which fail in a non-local viewer. Sideshow's own server code confirms only raster images are served inline; video cannot be a same-origin Sideshow asset.
- Fix applied: both players now use the Sideshow-relative /a/<id> path so they resolve against whichever host serves the session, and the loopback fallbacks were removed. Verified in the actual sandboxed surfaces at the MagicDNS session URL with a temporary readiness probe: both videos reached readyState 4 and playing. Probe removed afterwards; sources unchanged.
- Omari recut, 11.9 s at 2560x1440/60 fps: 56.5-63.0 s (before -> Super+Tab overview -> landed NEOVIM), 0.4 s beat, 31.0-36.0 s (Alt+Tab cycling between browser and adjacent editor). Separate Super/Tab and Alt/Tab keycaps plus captions "overview of all windows" and "cycle recent windows".
- Master quality 7,656,500 bytes; in-post preview 4,311,344 bytes to fit the 5 MiB Sideshow asset cap. Scrolling stays the approved 2,213,658-byte clip, unchanged.
- What the footage cannot show: the Alt+Tab switcher overlay itself is not captured; only the focus/landing changes are visible, so the caption describes what happens rather than claiming a visible list. Empty overview placeholders are shown as recorded.


Omari v15 revision per Herdra m15f652be (2026-11-20): 14.2 s, 2560x1440/60 fps. Added full-width function titles at each cut, large filled rounded Super/Tab and Alt/Tab keycaps with visible patina borders on a solid dark panel, one cue line each ("watch the overview open, then land"; "watch the active window change as it cycles" - no claim of an Alt+Tab overlay). Overview idle sped 2x, landing at 1x, 1 s landed beat before Alt+Tab. Master 8,281,786 bytes; preview 4,799,197 bytes for the Sideshow cap. Post vdSAK32VdQk version 17; scrolling asset unchanged. 800px legibility and full-cut contact sheet checked. Playback limit: supported browser (Obscura) unavailable this round, so the revised asset was not re-proven in-browser; no alternate browser used.


Publication approval via Herdra m3abcd7a3: Algorant: "who these are a million times better. finally approved omari. I would also like to use them for their coutnerparts in my actual algOS showcase as well. propose what I mean there while approving verdigris readme for adding these in the appropriate place. both delegated". Publish approved unchanged scrolling and full-quality 8.28 MB Omari v17 master. Scrolling opens Showcase; Omari goes second beside the Omarchy entry; no unrelated moves. GitHub attachment upload approved via existing gh login; if unavailable via gh, stop at the browser-only upload step and relay it rather than working around it. Verify both actual players signed out. Commit a short reusable reproduction recipe from commands actually run. algOS proposal only, no algOS changes.

Showcase videos live at 38c0cc5 (integration 0676e60), attached via native gh on PR #5. Anonymous GitHub homepage renders two video controls; fetched both actual rendered sources signed out as video/mp4 and verified approved SHA-256 (2,213,658 and 8,281,786 bytes). Existing image order, two-column gallery and catalog unchanged. Actual in-browser playback remains unverified: paired Chromium offline. docs/showcase-clips.md records provenance and hashes, but exact executed v17 recipe not recovered from available artifacts and is not claimed complete. Review checkout retained, no algOS changes. Task remains open.