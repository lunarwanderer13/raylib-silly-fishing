from pyray import *
from config import GameConfig

def draw_room() -> None:
    virtual_width: int = int(GameConfig.virtual_resolution.x)
    virtual_height: int = int(GameConfig.virtual_resolution.y)
