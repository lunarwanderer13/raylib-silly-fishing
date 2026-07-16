from pyray import *
from config import GameConfig
from rooms.room_types import Room

virtual_width: int = int(GameConfig.virtual_resolution.x)
virtual_height: int = int(GameConfig.virtual_resolution.y)
room_size: Vector2 = Vector2(virtual_width, virtual_height * 2)

def draw_room() -> None:
    draw_circle_v(Vector2(0, 0), 20, RED)

room: Room = Room(room_size, draw_room)