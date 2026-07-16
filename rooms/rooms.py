from .room_types import Room, RoomIndex
from .town_entrance import room as room_town_entrance
from .road import room as room_road
from .town import room as room_town
from .house import room as room_house
from .fisherman import room as room_fisherman
from .lake import room as room_lake
from .river import room as room_river
from .sea import room as room_sea

class RoomManager:
    def __init__(self, current_room: RoomIndex = RoomIndex.TOWN_ENTRANCE) -> None:
        self.current_room: RoomIndex = current_room
        self.rooms: dict[RoomIndex, Room] = {
            RoomIndex.TOWN_ENTRANCE: room_town_entrance,
            RoomIndex.ROAD: room_road,
            RoomIndex.TOWN: room_town,
            RoomIndex.HOUSE: room_house,
            RoomIndex.FISHERMAN: room_fisherman,
            RoomIndex.LAKE: room_lake,
            RoomIndex.RIVER: room_river,
            RoomIndex.SEA: room_sea,
        }

    def select_room(self, room_id: RoomIndex | None = None) -> Room:
        if not room_id: room_id = RoomIndex(self.current_room)

        self.current_room = room_id
        return self.rooms[room_id]
