from pyray import *
from typing import TYPE_CHECKING
from config import GameConfig
from rooms.rooms import RoomIndex

if TYPE_CHECKING: from player import Player

class Debugger:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

    debug_overlay_keybind: KeyboardKey = lambda self: self.player.data["keybinds"]["toggle_debug_overlay"]
    command_line_keybind: KeyboardKey = lambda self: self.player.data["keybinds"]["toggle_command_line"]

    is_debug_overlay_open: bool = False
    is_command_line_open: bool = False

    def toggle_debug_overlay(self) -> None:
        if is_key_pressed(self.debug_overlay_keybind()):
            self.is_debug_overlay_open = not self.is_debug_overlay_open

    def draw_debug_overlay(self) -> None:
        draw_rectangle_v(Vector2(5, 5), Vector2(100, 100), Color(0, 0, 0, 100))

        player_position: Vector2 = self.player.position
        draw_text("Position:", 10, 10, 10, WHITE)
        draw_text(f"x: {round(player_position.x, 1)}", 10, 20, 10, WHITE)
        draw_text(f"y: {round(player_position.y, 1)}", 10, 30, 10, WHITE)

        room_id: int = self.player.data["room_id"]
        draw_text("Room:", 10, 50, 10, WHITE)
        draw_text(f"Id: {room_id}", 10, 60, 10, WHITE)
        draw_text(f"Name: {RoomIndex(room_id).name}", 10, 70, 10, WHITE)

        draw_text(f"FPS: {get_fps()}", 10, 90, 10, WHITE)

    # To be expanded
    def toggle_command_line(self) -> None:
        if is_key_pressed(self.command_line_keybind()):
            self.is_command_line_open = not self.is_command_line_open

    def draw_command_line(self) -> None:
        virtual_resolution: Vector2 = GameConfig.virtual_resolution
        draw_rectangle_v(Vector2(5, virtual_resolution.y - 15), Vector2(virtual_resolution.x - 10, 10), BLACK)
