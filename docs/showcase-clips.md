# Showcase clips

The Showcase opens with scrolling above the screenshot gallery. The Omari clip
is kept here, unembedded, for the algOS showcase: it shows Omari features rather
than the palette, so it is not part of this repository's Showcase.

These are the Omari v17 edit and encode commands run on 2026-11-20, recovered
from the editor's resumed context and surviving artifacts. Paths are generalized
to keep inputs and scratch outputs separate. A verification run reproduced the
four overlay PNGs pixel-for-pixel and both MP4s byte-for-byte.

## Published clips

### Scrolling

https://github.com/user-attachments/assets/e7608000-ce65-4e86-b62c-4cca13f0be3a

Approved 6.2-second, 2560 × 1440, 60 fps MP4 (2,213,658 bytes). SHA-256: `93598ddd46ee3b6153f8bba489b191d66ab0389c43e068fa71912ec61eca631c`.

### Omari

Not shown in the README Showcase; kept for the algOS showcase.

https://github.com/user-attachments/assets/01aaa311-7b1a-4a56-9fdc-c0c985d56a97

Approved v17 master: 14.2-second, 2560 × 1440, 60 fps MP4 (8,281,786 bytes). SHA-256: `613378b081b7d88a708919c5a3be2ce58b6af27eec3e3a5c3931fb9f08c6509a`.

The v17 edit emphasizes the overview and landing, then the Alt+Tab action;
overview idle is sped up and landings remain at 1×.

## Variables

Set these before running anything. `SOURCE` is the original 120 fps recording;
`WORK` is a fresh scratch directory; use the same JetBrainsMono Nerd Font for
matching overlays. Requires Python with Pillow and FFmpeg with libx264.

```sh
SOURCE=${SOURCE:?path to 2026-11-20_10.00_screen.mp4}
WORK=$(mktemp -d)
export FONT=${FONT:-/usr/share/fonts/TTF/JetBrainsMonoNerdFont-Regular.ttf}
cd "$WORK"
```

## Overlay artwork (PIL)

The keycap panels and titles are transparent 2560 × 1440 PNGs. They are created
once with Pillow, then composited by ffmpeg. This is the final generation code;
one superseded cue phrase is noted under Gaps.

```python
from PIL import Image, ImageDraw, ImageFont

W, H = 2560, 1440
FONT = __import__("os").environ["FONT"]
VELLUM = (235, 219, 178, 255)
AQUA = (131, 165, 152, 255)
PATINA = (104, 157, 106, 255)
PANEL = (35, 38, 37, 245)

def font(size):
    return ImageFont.truetype(FONT, size)

def panel(keys, cue, out):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    px, py, pw, ph = 60, 1100, 1180, 280
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=24,
                        fill=PANEL, outline=PATINA, width=3)
    x, ky, kh = px + 34, py + 34, 120
    for i, key in enumerate(keys):
        kw = max(170, 52 * len(key) + 90)
        d.rounded_rectangle([x, ky, x + kw, ky + kh], radius=18,
                            fill=(28, 31, 30, 255), outline=PATINA, width=4)
        d.text((x + kw / 2, ky + kh / 2 - 4), key,
               font=font(58), fill=VELLUM, anchor="mm")
        x += kw
        if i < len(keys) - 1:
            d.text((x + 30, ky + kh / 2 - 4), "+",
                   font=font(54), fill=AQUA, anchor="mm")
            x += 70
    d.text((px + 36, py + ph - 56), cue, font=font(42), fill=AQUA, anchor="lm")
    im.save(out)

def title(text, out):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 64, W, 204], fill=(24, 27, 26, 232))
    d.line([0, 204, W, 204], fill=PATINA, width=3)
    d.text((W / 2, 134), text, font=font(66), fill=VELLUM, anchor="mm")
    im.save(out)

panel(["Super", "Tab"], "watch the overview open, then land",
      "panel-super.png")
panel(["Alt", "Tab"], "watch the active window change as it cycles",
      "panel-alt.png")
title("Super + Tab  —  overview of all windows", "title-super.png")
title("Alt + Tab  —  cycle recent windows", "title-alt.png")
```

Run that in `$WORK` with `FONT` exported.

## Omari v17 master

Timing map, all from the original 120 fps source:

- `58.6-60.0` before the overview, 1×
- `60.0-65.0` overview navigation, 2× (idle sped up)
- `65.0-68.8` landing, 1×
- 1.0 s clone of the landed frame as the beat
- `31.0-36.5` Alt+Tab cycling, 1×

The overlays are enabled only on the finished timeline: Super panel `0.6-7.6`,
Super title `0.0-1.8`, Alt panel `9.3-14.2`, Alt title `8.7-10.5`.

```sh
cd "$WORK"
ffmpeg -v error -y -i "$SOURCE" \
  -i panel-super.png -i title-super.png -i panel-alt.png -i title-alt.png \
  -filter_complex "\
[0:v]trim=start=58.6:end=60.0,setpts=PTS-STARTPTS[v0];\
[0:v]trim=start=60.0:end=65.0,setpts=(PTS-STARTPTS)/2[v1];\
[0:v]trim=start=65.0:end=68.8,setpts=PTS-STARTPTS[v2];\
[v0][v1][v2]concat=n=3:v=1:a=0,tpad=stop_mode=clone:stop_duration=1.0[base];\
[0:v]trim=start=31.0:end=36.5,setpts=PTS-STARTPTS[v3];\
[base][v3]concat=n=2:v=1:a=0,fps=60[cat];\
[cat][1:v]overlay=0:0:enable='between(t,0.6,7.6)'[o1];\
[o1][2:v]overlay=0:0:enable='between(t,0.0,1.8)'[o2];\
[o2][3:v]overlay=0:0:enable='between(t,9.3,14.2)'[o3];\
[o3][4:v]overlay=0:0:enable='between(t,8.7,10.5)'[v]" \
  -map "[v]" -an -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p -movflags +faststart \
  "$WORK/highlight-omari.mp4"
```

Check the approved master before treating the recipe as reproduced:

```sh
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,avg_frame_rate \
  -show_entries format=duration -of default=noprint_wrappers=1 \
  "$WORK/highlight-omari.mp4"
sha256sum "$WORK/highlight-omari.mp4"
```

Expected: `2560x1440`, `60/1`, `14.200000`, and SHA-256
`613378b081b7d88a708919c5a3be2ce58b6af27eec3e3a5c3931fb9f08c6509a`
(8,281,786 bytes).

## Omari preview encode

The Sideshow asset path is capped at 5 MiB, so the in-post preview is a second
H.264 encode of the master at CRF 23. It is not the publication master.

```sh
ffmpeg -v error -y -i "$WORK/highlight-omari.mp4" \
  -an -c:v libx264 -preset slow -crf 23 \
  -pix_fmt yuv420p -movflags +faststart \
  "$WORK/highlight-omari-preview.mp4"
```

Expected: 4,799,197 bytes, SHA-256
`633bab4975ae13b67fa8e5abe0776e2806f102e94db1fed5d493b40877e6ee4d`.

## Legibility and cut checks

At least one frame from each function was rendered at 800 px wide and inspected
for the title, keycaps and cue line. A full-cut strip at 1 fps was inspected for
the handoff and landing.

```sh
# one supplied-time frame at review width
ffmpeg -v error -y -ss 0.8 -i "$WORK/highlight-omari.mp4" \
  -frames:v 1 -vf "scale=800:-1" "$WORK/frame-0.8.png"
ffmpeg -v error -y -ss 9.6 -i "$WORK/highlight-omari.mp4" \
  -frames:v 1 -vf "scale=800:-1" "$WORK/frame-9.6.png"
# 1 fps strip of the whole cut (then view the files)
ffmpeg -v error -y -i "$WORK/highlight-omari.mp4" \
  -vf "fps=1,scale=800:-1" "$WORK/strip-%02d.png"
```

The frames were downscaled to 800 px wide for the legibility check; the master
itself is never downscaled.

## Scrolling (approved, unchanged)

The scrolling clip is separate and was not re-encoded for v17. It is a single
continuous 1× trim of the 09.14 recording, `14.4-20.6 s`, encoded at CRF 18 and
60 fps, producing 6.2 s and 2,213,658 bytes. Its SHA-256 is
`93598ddd46ee3b6153f8bba489b191d66ab0389c43e068fa71912ec61eca631c`. The exact scrolling command was not recovered; this paragraph documents the approved artifact.

## Gaps and superseded steps

- No shell history or raw session file was consulted. The commands above come
  from the resumed conversation context plus the surviving `review/clips` files;
  a scratch run with FFmpeg n9.0.2 reproduced both recorded SHA-256 hashes.
- The overlay artwork was iterated. A first pass used smaller keycaps without
  full-width titles and a Super cue of "watch the highlight move between
  windows"; the footage did not show a reliably moving highlight, so the final
  panel-super was regenerated with "watch the overview open, then land". Only
  the final generation is included.
- The actual run used a scratch directory under `/tmp`; `$WORK` replaces it.
  Overlay PNGs and extracted frames are scratch artifacts and are not in the
  repository.
- Publishing and Sideshow-relative asset uploads are not part of this recipe;
  the attachment URLs above are the published result.
- Slower/faster segments are expressed only through `trim` + `setpts` on the
  original; no source frame is cropped or resized.
- The Omari preview is a deliberate lower-bitrate copy for the Sideshow cap.
  The GitHub attachment should use the master, not the preview.
