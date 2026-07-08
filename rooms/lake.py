from pyray import *
from config import GameConfig
from rooms.room_types import RoomIndex

def draw_room() -> None:
    virtual_width: int = int(GameConfig.virtual_resolution.x)
    virtual_height: int = int(GameConfig.virtual_resolution.y)

    draw_circle_v(Vector2(0, 0), 20, RED)
    draw_rectangle_v(Vector2(virtual_width * 2/3, 0), Vector2(virtual_width * 1/3, virtual_height), DARKBLUE)
    draw_rectangle_v(Vector2(virtual_width * 1/2, virtual_height / 2 - virtual_height / 10), Vector2(virtual_width * 1/3, virtual_height / 5), BROWN)
    draw_rectangle_lines_ex(GameConfig.fishing_spots[RoomIndex.LAKE].rect, 1, YELLOW)