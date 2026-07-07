from pyray import *
from config import GameConfig
from debug import Debugger
from items import ItemManager, Rod, get_rod, Bait, get_bait

class Player:
    def __init__(self, data) -> None:
        self.data = data
        self.debugger: Debugger = Debugger(self)
        self.inventory: ItemManager = ItemManager()

        self.position: Vector2 = Vector2(self.data["player"]["position"]["x"], self.data["player"]["position"]["y"])

        self.movement: Vector2 = Vector2(0, 0)
        self.speed: float = 100
        self.sprint: float = 1.0
        self.size: Vector2 = Vector2(20, 30)
        self.rect: Rectangle = Rectangle(self.position.x, self.position.y + self.size.y / 2, self.size.x, self.size.y / 2)

        self.equipped_rod: Rod | None = get_rod(self.data["player"]["equipped_rod"])
        self.equipped_bait: Bait | None = get_bait(self.data["player"]["equipped_bait"])

    can_cast: bool = False
    is_cast: bool = False
    can_reel: bool = False
    can_bait: bool = False
    can_move: bool = True
    can_interact: bool = True

    def move(self) -> None:
        delta: float = get_frame_time()

        if is_key_down(self.data["keybinds"]["walk_up"]):
            self.movement.y = -1
        if is_key_down(self.data["keybinds"]["walk_right"]):
            self.movement.x = 1
        if is_key_down(self.data["keybinds"]["walk_down"]):
            self.movement.y = 1
        if is_key_down(self.data["keybinds"]["walk_left"]):
            self.movement.x = -1

        if is_key_down(self.data["keybinds"]["walk_up"]) and is_key_down(self.data["keybinds"]["walk_down"]):
            self.movement.y = 0
        if is_key_down(self.data["keybinds"]["walk_left"]) and is_key_down(self.data["keybinds"]["walk_right"]):
            self.movement.x = 0

        if is_key_up(self.data["keybinds"]["walk_up"]) and is_key_up(self.data["keybinds"]["walk_down"]):
            self.movement.y = 0
        if is_key_up(self.data["keybinds"]["walk_left"]) and is_key_up(self.data["keybinds"]["walk_right"]):
            self.movement.x = 0

        length: float = vector2_length_sqr(self.movement)

        if length > 0:
            self.movement.x /= length
            self.movement.y /= length

        if is_key_down(self.data["keybinds"]["sprint"]):
            self.sprint = 1.25
        else:
            self.sprint = 1.0

        self.position.x += self.movement.x * self.speed * self.sprint * delta
        self.position.y += self.movement.y * self.speed * self.sprint * delta

    def draw(self) -> None:
        draw_rectangle_v(self.position, self.size, BLUE)
        draw_rectangle_rec(self.rect, YELLOW)

    def update(self) -> None:
        self.draw()

        self.debugger.debug_overlay()
        self.debugger.command_line()

        if self.can_move: self.move()

        self.rect.x = self.position.x
        self.rect.y = self.position.y + self.size.y / 2

        self.can_cast = bool(any(check_collision_recs(self.rect, fishing_spot) for fishing_spot in GameConfig.fishing_spots.values()) and not self.can_reel and self.equipped_rod)
