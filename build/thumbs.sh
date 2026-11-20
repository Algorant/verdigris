#!/usr/bin/env bash
# Regenerate the Showcase gallery thumbnails from the full-size screenshots.
#
# README.md's gallery is the input list: every row links an original
# (<a href="...png">) and displays a thumbnail (<img src="...jpg" width="440">).
# The thumbnails are written back to exactly those paths, so the gallery markup
# never changes. Screenshots are never edited: each source is hashed before and
# after, and the run fails if a byte changed.
#
# Thumbnails are 880x550, one frame for the whole gallery, four across in the
# README: each cell asks for 200 CSS px, so the file carries 4.4x the pixels of
# its nominal box and stays sharp at any display density. The frame is the same
# 16:10 shape the gallery has always had, so the four-column rows keep even
# heights. Each screenshot is fitted whole and centred (no crop, no stretch);
# the leftover bars are filled with the palette's background colour, matching the
# screenshots' own surround.
#
# Needs ImageMagick 7 (`magick`). Writes images only; no theme files.
set -euo pipefail
cd "$(dirname "$0")/.."

WIDTH=880      # 4.4x the 200 CSS px gallery cell in README.md
HEIGHT=550     # 16:10, the gallery's original frame
MATTE='#1d2021'  # verdigris background, matches the screenshots
QUALITY=85

command -v magick >/dev/null || { echo "needs ImageMagick 7 (magick)" >&2; exit 1; }

# "original|thumbnail" for each gallery row, in README order.
mapfile -t pairs < <(
  grep -o '<a href="[^"]*"><img src="[^"]*"' README.md \
    | sed -E 's#<a href="([^"]*)"><img src="([^"]*)"#\1|\2#'
)
[ "${#pairs[@]}" -gt 0 ] || { echo "no gallery entries found in README.md" >&2; exit 1; }

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

before="$tmp/before.sha"
after="$tmp/after.sha"
: >"$before"

total=0
for pair in "${pairs[@]}"; do
  src=${pair%%|*}
  out=${pair#*|}
  [[ -f $src ]] || { echo "missing original: $src" >&2; exit 1; }
  sha256sum "$src" >>"$before"

  # Lanczos downscale into the 880x550 frame, JPEG with 4:4:4 chroma (coloured
  # terminal text keeps its edges), no metadata.
  magick "$src" \
    -filter Lanczos -resize "${WIDTH}x${HEIGHT}" \
    -background "$MATTE" -gravity center -extent "${WIDTH}x${HEIGHT}" \
    -strip -sampling-factor 4:4:4 -interlace JPEG -quality "$QUALITY" \
    "$tmp/${out##*/}"

  mkdir -p "$(dirname "$out")"
  mv "$tmp/${out##*/}" "$out"

  size=$(stat -c%s "$out")
  dims=$(magick identify -format '%wx%h' "$out")
  total=$((total + size))
  printf '%-34s <- %-38s %s %6d B\n' "$out" "$src" "$dims" "$size"
done

: >"$after"
for pair in "${pairs[@]}"; do sha256sum "${pair%%|*}" >>"$after"; done
if ! diff -q "$before" "$after" >/dev/null; then
  echo "originals changed during the run:" >&2
  diff "$before" "$after" >&2
  exit 1
fi

printf '%d thumbnails, %d B total\n' "${#pairs[@]}" "$total"
