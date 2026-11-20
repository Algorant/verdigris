# Screenshots

Every screenshot a page shows is the full-resolution original, inlined at the
display width that page asks for. The click target is that same file, so opening
it only changes the view, not the picture. Pages reference the lossless PNG — or
the animated GIF where the shot moves — never a derived, lossy thumbnail.

- The display size lives in the `width` attribute on the image. The file itself
  is never resized, cropped, padded or re-encoded for a page, so every shot keeps
  its native aspect and its capture resolution.
- Originals are committed byte-for-byte as captured. Nothing in the repository
  replaces them with a smaller copy, and the pages link them directly.
- Inlining originals costs more bytes per page than a thumbnail would. That cost
  is accepted: a colorscheme repository is judged on how its colors actually
  look, so fidelity wins over weight.

## The exception requirement

If a shot has no lossless full-resolution original — a legacy page whose only
source is a JPEG or a resized frame — use the file that exists, inline it at the
display width, and say in the commit message or beside the image that the
original is missing. That keeps the gap visible so a fresh capture can fill it.

Never upscale, recrop or re-encode a lossy-only source to imitate a better one:
that adds bytes and blur without adding information.

## Derived thumbnails

`docs/thumbs/` and the per-app `thumbs/` directories hold thumbnails from before
this convention. No page references them now; they are kept as history rather
than deleted, and no build step regenerates them.
