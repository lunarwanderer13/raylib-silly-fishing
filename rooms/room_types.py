from pyray import Rectangle, Vector2
from enum import Enum

class RoomIndex(Enum):
    TOWN_ENTRANCE = 0
    ROAD = 1
    TOWN = 2
    HOUSE = 3
    FISHERMAN = 4
    LAKE = 5
    RIVER = 6
    SEA = 7

class TravelSpot:
    def __init__(self, room_entrance: Rectangle, room_exit: Vector2) -> None:
        self.room_entrance: Rectangle = room_entrance
        self.room_exit: Vector2 = room_exit

class FishingSpot:
    def __init__(self, rect: Rectangle) -> None:
        self.rect: Rectangle = rect