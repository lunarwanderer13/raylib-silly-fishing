from pyray import *
from typing import TYPE_CHECKING

if TYPE_CHECKING: from player import Player

class Debugger:
    def __init__(self,
                 debug_overlay_keybind: KeyboardKey,
                 command_line_keybind: KeyboardKey):
        self.debug_overlay_keybind = debug_overlay_keybind
        self.command_line_keybind = command_line_keybind

    is_debug_overlay_open: bool = False
    is_command_line_open: bool = False

    def debug_overlay(self, player: Player) -> None:
        if is_key_pressed(self.debug_overlay_keybind):
            self.is_debug_overlay_open = not self.is_debug_overlay_open

        if self.is_debug_overlay_open:
            draw_rectangle_v(Vector2(5, 5), Vector2(50, 100), Color(0, 0, 0, 100))
            draw_text(f"x: {round(player.position.x, 1)}", 10, 10, 10, WHITE)
            draw_text(f"y: {round(player.position.y, 1)}", 10, 25, 10, WHITE)

    def command_line(self) -> None:
        if is_key_pressed(self.command_line_keybind):
            self.is_command_line_open = not self.is_command_line_open
