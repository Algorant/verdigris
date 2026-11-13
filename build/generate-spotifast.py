#!/usr/bin/env python3
"""Write the native Spotifast theme Omarchy renders for Verdigris.

Reads palette/verdigris.json and writes apps/spotifast/verdigris.json, the
palette file Spotifast lists from its themes folder. The keys and the mix
roundings are Omarchy's own (contrib/omarchy/spotifast.json.tpl in Spotifast),
so a Spotifast without Omarchy shows the colors an Omarchy desktop gives it.
Running it twice changes nothing.

Omarchy's template mixes the current theme's colors.toml. Verdigris's Omarchy
theme takes the five roles it reads from palette entries; the names below are
that mapping, which is the only thing this file adds. Its mode is dark, which
is the base Spotifast is told to start from.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PALETTE = ROOT / "palette" / "verdigris.json"
THEME = ROOT / "apps/spotifast/verdigris.json"

# The colors.toml roles Omarchy's Spotifast template reads, and the palette
# entry each one comes from.
OMARCHY = {
    "background": "base",
    "foreground": "vellum",
    "accent": "fern",
    "red": "oxblood-text",
    "yellow": "ochre",
}


def load() -> dict[str, str]:
    data = json.loads(PALETTE.read_text())
    # The shared dark UI base, as build/generate.py seeds it.
    colors = {"base": "#1d2021"}
    for group in ("colors", "extended", "supporting"):
        for entry in data.get(group, []):
            colors.setdefault(entry["name"], entry["hex"])
    return colors


def mix(start: str, end: str, percent: int) -> str:
    """Omarchy's mix: percent of the way from start to end, rounded half up."""
    channels = zip(
        (int(start[i : i + 2], 16) for i in (1, 3, 5)),
        (int(end[i : i + 2], 16) for i in (1, 3, 5)),
    )
    mixed = ((a * (100 - percent) + b * percent + 50) // 100 for a, b in channels)
    return "#" + "".join(f"{channel:02x}" for channel in mixed)


def spotifast(c: dict[str, str]) -> None:
    omarchy = {role: c[entry] for role, entry in OMARCHY.items()}
    background = omarchy["background"]
    foreground = omarchy["foreground"]
    accent = omarchy["accent"]
    colors = {
        "window": background,
        "panel": mix(background, foreground, 3),
        "surface": mix(background, foreground, 8),
        "surface_hover": mix(background, foreground, 12),
        "surface_active": mix(background, foreground, 18),
        "outline": mix(background, foreground, 20),
        "text": foreground,
        "secondary": mix(background, foreground, 70),
        "dim": mix(background, foreground, 50),
        "accent": accent,
        "accent_hover": mix(accent, foreground, 15),
        "on_accent": background,
        "danger": omarchy["red"],
        "warning": omarchy["yellow"],
    }
    THEME.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps({"base": "dark", "colors": colors}, indent=2) + "\n"
    if not THEME.exists() or THEME.read_text() != text:
        THEME.write_text(text)


def main() -> None:
    spotifast(load())
    print("generated", THEME.relative_to(ROOT))


if __name__ == "__main__":
    main()
