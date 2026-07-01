from items import ItemManager

class Player:
    inventory: ItemManager = ItemManager()

    debug: bool = False
    can_cast: bool = False
    can_reel: bool = False
    can_move: bool = False
    can_interact: bool = False
