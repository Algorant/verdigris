# Changelog

Palette releases follow [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-11-06

### Added

- Added `oxblood-text` (`#c66f70`) and `oxblood-bright` (`#d47b7c`) as named supporting tints of oxblood for readable red text, ANSI red (1) and ANSI bright red (9).

### Changed

- Documented oxblood (`#74363d`) as the red for fills, bars and meters; red text uses its tints.
- Herdr app theme: ANSI red and `blocked` use `#c66f70`; ANSI bright red uses `#d47b7c`.
- Ghostty and Windows Terminal: red uses `#c66f70`, bright red uses `#d47b7c`.
- bat (deleted gutter, invalid), Atuin (error alerts) and Yazi (cut marker) use `#c66f70`.
- btop CPU and used-meter gradient ends use oxblood `#74363d`.

### Scope

- Other ports (Obsidian, Pi, Omarchy notifications, Hokum, Pele) are unchanged. The standalone Omarchy theme adopts this release in its own repository.

## [0.1.2] - 2026-08-26

### Changed

- Replaced Additional Colors `yellow` (`#d29a46`) with `goldenrod` (`#b8863b`).
- Replaced Additional Colors `purple` (`#ad8294`) with `ink-violet` (`#8989b0`).
- Finalized the complete Additional Colors set: moss, teal, oxblood, goldenrod, deep-copper, and ink-violet.

### Scope

- Application ports are unchanged and may adopt this palette release separately.

## [0.1.1] - 2026-08-26

### Added

- Added a brief record of the deep copper exploration.

### Changed

- Replaced Additional Colors `orange` (`#c96f3d`) with `deep-copper` (`#b9805f`) in the canonical palette and direct palette documentation.

### Scope

- Application ports are unchanged and may adopt this palette release separately.

## [0.1.0] - 2026-08-26

### Added

- Began explicit palette versioning.
- Added `oxblood` (`#74363d`) as the official Additional Colors red.

### Changed

- Replaced `diff-red` (`#e36f63`) with `oxblood` in the canonical palette and direct palette documentation.

### Scope

- Application ports are unchanged and may adopt this palette release separately.
