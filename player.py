from pyray import *
from debug import Debugger
from items import ItemManager

class Player:
    def __init__(self, data) -> None:
        self.data = data

        self.debugger: Debugger = Debugger(self)

        self.inventory: ItemManager = ItemManager()

    position: Vector2 = Vector2(50, 50)
    movement: Vector2 = Vector2(0, 0)
    speed: float = 100
    sprint: float = 1.0

    can_cast: bool = True
    can_reel: bool = True
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
        draw_rectangle_v(self.position, Vector2(10, 10), BLUE)

    def update(self) -> None:
        self.draw()

        self.debugger.debug_overlay()
        self.debugger.command_line()

        if self.can_move: self.move()
