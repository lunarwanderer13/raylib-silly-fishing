from pyray import *
from rooms.room_types import RoomIndex, TravelSpot, FishingSpot

class GameConfig:
    virtual_resolution: Vector2 = Vector2(320, 180)

    travel_spots: dict[str, dict[RoomIndex, TravelSpot]] = {
        RoomIndex.TOWN_ENTRANCE: {
            RoomIndex.TOWN: TravelSpot(Rectangle(),
                                       Vector2()),
        },
        RoomIndex.ROAD: {
            RoomIndex.TOWN_ENTRANCE: TravelSpot(Rectangle(),
                                                Vector2()),
            RoomIndex.ROAD: TravelSpot(Rectangle(),
                                       Vector2()),
        },
        RoomIndex.TOWN: {
            RoomIndex.TOWN_ENTRANCE: TravelSpot(Rectangle(),
                                                Vector2()),
            RoomIndex.HOUSE: TravelSpot(Rectangle(),
                                        Vector2()),
            RoomIndex.FISHERMAN: TravelSpot(Rectangle(),
                                            Vector2()),
            RoomIndex.LAKE: TravelSpot(Rectangle(),
                                       Vector2()),
        },
        RoomIndex.HOUSE: {
            RoomIndex.TOWN: TravelSpot(Rectangle(),
                                       Vector2()),
        },
        RoomIndex.FISHERMAN: {
            RoomIndex.TOWN: TravelSpot(Rectangle(),
                                       Vector2()),
        },
        RoomIndex.LAKE: {
            RoomIndex.TOWN: TravelSpot(Rectangle(),
                                       Vector2()),
        },
        RoomIndex.RIVER: {},
        RoomIndex.SEA: {},
    }

    fishing_spots: dict[RoomIndex, FishingSpot] = {
        RoomIndex.LAKE: FishingSpot(Rectangle(virtual_resolution.x * 3/4,
                                              virtual_resolution.y / 2 - virtual_resolution.y / 10,
                                              virtual_resolution.x * 1/12,
                                              virtual_resolution.y / 5)),
        RoomIndex.RIVER: FishingSpot(Rectangle()),
        RoomIndex.SEA: FishingSpot(Rectangle()),
    }

class DefaultConfig:
    keybinds: dict[str, KeyboardKey] = {
        "walk_up": KeyboardKey.KEY_W,
        "walk_right": KeyboardKey.KEY_D,
        "walk_down": KeyboardKey.KEY_S,
        "walk_left": KeyboardKey.KEY_A,
        "sprint": KeyboardKey.KEY_LEFT_SHIFT,
        "cast_rod": KeyboardKey.KEY_SPACE,
        "reel_rod": KeyboardKey.KEY_R,
        "use_bait": KeyboardKey.KEY_E,
        "toggle_debug_overlay": KeyboardKey.KEY_TAB,
        "toggle_command_line": KeyboardKey.KEY_GRAVE
    }

    fps: int = 60
    fullscreen: bool = False
    room_id: int = 5
