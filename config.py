from pyray import *

class GameConfig:
    virtual_resolution: Vector2 = Vector2(320, 180)

    fishing_spots: dict[str, Rectangle] = {
        "lake": Rectangle(virtual_resolution.x / 2 + 5, virtual_resolution.y / 2 - virtual_resolution.y / 10 + 5, virtual_resolution.x * 1/3 - 10, virtual_resolution.y / 5 - 10),
    }

class DefaultConfig:
    keybinds: dict[str, KeyboardKey] = {
        "walk_up": KeyboardKey.KEY_W,
        "walk_right": KeyboardKey.KEY_D,
        "walk_down": KeyboardKey.KEY_S,
        "walk_left": KeyboardKey.KEY_A,
        "sprint": KeyboardKey.KEY_LEFT_SHIFT,
        "use_rod": KeyboardKey.KEY_SPACE,
        "use_bait": KeyboardKey.KEY_LEFT_CONTROL,
        "toggle_debug_overlay": KeyboardKey.KEY_TAB,
        "toggle_command_line": KeyboardKey.KEY_GRAVE
    }

    fps: int = 60
    fullscreen: bool = False
    room_id: int = 5
