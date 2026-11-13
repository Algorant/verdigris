-- verdigris for hyprland.
local active = "#8ec07c"
local inactive = "rgba(595959aa)"

hl.config({
  general = {
    col = {
      active_border = { colors = { active, active }, angle = 45 },
      inactive_border = inactive,
    },
  },
})
