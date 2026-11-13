#!/usr/bin/env python3
"""Generate the app files that are pure palette derivations.

Reads palette/verdigris.json and writes the files under apps/ that Omarchy
otherwise generates on my machine, so the repository owns them. Running it
twice changes nothing.

The ANSI order is the one every terminal port uses: 0-7 normal, 8-15 bright.
Red follows the oxblood role split: fills use oxblood, text uses its tint.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PALETTE = ROOT / "palette" / "verdigris.json"

# Terminal ANSI slots, in order, as palette color names.
ANSI = [
    "base", "oxblood-text", "patina", "ochre", "teal", "ink-violet", "aqua", "vellum",
    "muted", "oxblood-bright", "fern", "ochre", "aqua", "ink-violet", "aqua", "vellum",
]


def load() -> dict[str, str]:
    data = json.loads(PALETTE.read_text())
    colors = {"base": "#1d2021", "soft-light": "#d4be9a", "muted": "#928374"}
    for group in ("colors", "extended", "supporting"):
        for entry in data.get(group, []):
            colors.setdefault(entry["name"], entry["hex"])
    return colors


def lighten(hexcode: str, amount: float) -> str:
    r, g, b = (int(hexcode[i : i + 2], 16) for i in (1, 3, 5))
    mix = lambda c: round(c + (255 - c) * amount)
    return f"#{mix(r):02x}{mix(g):02x}{mix(b):02x}"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != text:
        path.write_text(text)


def ghostty(c: dict[str, str]) -> None:
    lines = [
        "# verdigris for ghostty. Generated from palette/verdigris.json.",
        f"background = {c['base']}",
        f"foreground = {c['vellum']}",
        f"cursor-color = {c['vellum']}",
        f"selection-background = {c['ashbronze']}",
        f"selection-foreground = {c['vellum']}",
        "",
    ]
    lines += [f"palette = {i}={c[name]}" for i, name in enumerate(ANSI)]
    write(ROOT / "apps/ghostty/verdigris", "\n".join(lines) + "\n")


def foot(c: dict[str, str]) -> None:
    lines = [
        "# verdigris for foot. Generated from palette/verdigris.json.",
        "[colors-dark]",
        f"foreground={c['vellum'][1:]}",
        f"background={c['base'][1:]}",
        f"selection-foreground={c['vellum'][1:]}",
        f"selection-background={c['ashbronze'][1:]}",
        "",
        f"cursor={c['base'][1:]} {c['vellum'][1:]}",
        "",
    ]
    for i in range(8):
        lines.append(f"regular{i}={c[ANSI[i]][1:]}")
    for i in range(8):
        lines.append(f"bright{i}={c[ANSI[i + 8]][1:]}")
    write(ROOT / "apps/foot/verdigris.ini", "\n".join(lines) + "\n")


def chromium(c: dict[str, str]) -> None:
    r, g, b = (int(c["base"][i : i + 2], 16) for i in (1, 3, 5))
    write(ROOT / "apps/chromium/verdigris.theme", f"{r},{g},{b}\n")


def claude_code(c: dict[str, str]) -> None:
    accent = c["fern"]
    error = c["oxblood-text"]
    warning = c["ochre"]
    overrides = {
        "claude": accent,
        "claudeShimmer": lighten(accent, 0.18),
        "text": c["vellum"],
        "inverseText": c["base"],
        "inactive": c["soft-light"],
        "inactiveShimmer": lighten(c["soft-light"], 0.12),
        "subtle": c["muted"],
        "suggestion": c["aqua"],
        "permission": c["teal"],
        "permissionShimmer": lighten(c["teal"], 0.22),
        "remember": warning,
        "success": c["patina"],
        "error": error,
        "warning": warning,
        "warningShimmer": lighten(warning, 0.18),
        "merged": c["ink-violet"],
        "promptBorder": accent,
        "promptBorderShimmer": lighten(accent, 0.18),
        "planMode": c["aqua"],
        "autoAccept": warning,
        "bashBorder": warning,
        "ide": c["aqua"],
        "diffAdded": "#28332c",
        "diffRemoved": "#3e2624",
        "diffAddedDimmed": "#232a27",
        "diffRemovedDimmed": "#2f2323",
        "diffAddedWord": "#354838",
        "diffRemovedWord": "#642d27",
        "userMessageBackground": "#292b2a",
        "userMessageBackgroundHover": "#323330",
        "bashMessageBackgroundColor": "#292b2a",
        "memoryBackgroundColor": "#292b2a",
        "selectionBg": c["ashbronze"],
        "rate_limit_fill": accent,
        "rate_limit_empty": "#46453e",
        "briefLabelYou": warning,
    }
    theme = {"name": "verdigris", "base": "dark", "overrides": overrides}
    write(ROOT / "apps/claude-code/verdigris.json", json.dumps(theme, indent=2) + "\n")


def hyprland(c: dict[str, str]) -> None:
    text = f"""-- verdigris for hyprland. Generated from palette/verdigris.json.
local active = "{c['fern']}"
local inactive = "rgba(595959aa)"

hl.config({{
  general = {{
    col = {{
      active_border = {{ colors = {{ active, active }}, angle = 45 }},
      inactive_border = inactive,
    }},
  }},
}})
"""
    write(ROOT / "apps/hyprland/verdigris.lua", text)


def main() -> None:
    c = load()
    ghostty(c)
    foot(c)
    chromium(c)
    claude_code(c)
    hyprland(c)
    print("generated app files from", PALETTE.relative_to(ROOT))


if __name__ == "__main__":
    main()
