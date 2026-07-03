from pyray import *

class Debugger:
    def __init__(self,
                 debug_overlay_keybind: KeyboardKey,
                 command_line_keybind: KeyboardKey):
        self.debug_overlay_keybind = debug_overlay_keybind
        self.command_line_keybind = command_line_keybind

    is_debug_overlay_open: bool = False
    is_command_line_open: bool = False

    def debug_overlay(self) -> None:
        if is_key_pressed(self.debug_overlay_keybind):
            self.is_debug_overlay_open = not self.is_debug_overlay_open

    def command_line(self) -> None:
        if is_key_pressed(self.command_line_keybind):
            self.is_command_line_open = not self.is_command_line_open