from pyray import *
from config import GameConfig
from rooms.room_types import Room, RoomIndex

virtual_width: int = int(GameConfig.virtual_resolution.x)
virtual_height: int = int(GameConfig.virtual_resolution.y)
room_size: Vector2 = Vector2(virtual_width * 2, virtual_height * 2)

def draw_room() -> None:
    draw_circle_v(Vector2(0, 0), 20, RED)
    draw_rectangle_v(Vector2(room_size.x * 1/3, 0), Vector2(room_size.x * 2/3, room_size.y), DARKBLUE)
    draw_rectangle_v(Vector2(room_size.x / 4, room_size.y / 4 - room_size.y / 20), Vector2(room_size.x / 6, room_size.y / 10), BROWN)
    draw_rectangle_lines_ex(GameConfig.fishing_spots[RoomIndex.LAKE].rect, 1, YELLOW)

room: Room = Room(room_size, draw_room)