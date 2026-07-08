from.room_types import RoomIndex
from .town_entrance import draw_room as draw_town_entrance
from .road import draw_room as draw_road
from .town import draw_room as draw_town
from .house import draw_room as draw_house
from .fisherman import draw_room as draw_fisherman
from .lake import draw_room as draw_lake
from .river import draw_room as draw_river
from .sea import draw_room as draw_sea

class RoomManager:
    def __init__(self, current_room: RoomIndex = RoomIndex.TOWN_ENTRANCE) -> None:
        self.current_room: RoomIndex = current_room

    def load_room(self, room_id: RoomIndex | None = None) -> None:
        if not room_id: room_id = RoomIndex(self.current_room)

        match room_id:
            case RoomIndex.TOWN_ENTRANCE:
                draw_town_entrance()
            case RoomIndex.ROAD:
                draw_road()
            case RoomIndex.TOWN:
                draw_town()
            case RoomIndex.HOUSE:
                draw_house()
            case RoomIndex.FISHERMAN:
                draw_fisherman()
            case RoomIndex.LAKE:
                draw_lake()
            case RoomIndex.RIVER:
                draw_river()
            case RoomIndex.SEA:
                draw_sea()

        self.current_room = room_id
