from pyray import *

class GameConfig:
    virtual_resolution: Vector2 = Vector2(320, 180)

class DefaultConfig:
    keybinds: dict[str, KeyboardKey] = {
        "walk_up": KeyboardKey.KEY_W,
        "walk_right": KeyboardKey.KEY_D,
        "walk_down": KeyboardKey.KEY_S,
        "walk_left": KeyboardKey.KEY_A,
        "sprint": KeyboardKey.KEY_LEFT_SHIFT,
        "use_rod": KeyboardKey.KEY_SPACE,
        "use_bait": KeyboardKey.KEY_LEFT_CONTROL,
        "toggle_debug_mode": KeyboardKey.KEY_TAB,
        "toggle_command_line": KeyboardKey.KEY_GRAVE
    }

    fps: int = 60
    fullscreen: bool = False
    room_id: int = 5
