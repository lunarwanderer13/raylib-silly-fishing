from pyray import *
from config import DefaultConfig
from items import ItemManager

class Player:
    inventory: ItemManager = ItemManager()

    position: Vector2 = Vector2(50, 50)
    movement: Vector2 = Vector2(0, 0)
    speed: float = 100
    sprint: float = 1.0

    debug: bool = False
    can_cast: bool = False
    can_reel: bool = False
    can_move: bool = False
    can_interact: bool = False

    def draw(self) -> None:
        draw_rectangle_v(self.position, Vector2(20, 20), BLUE)

    def move(self) -> None:
        if self.can_move:
            delta: float = get_frame_time()

            if is_key_down(DefaultConfig.keybinds["walk_up"]):
                self.movement.y = -1
            if is_key_down(DefaultConfig.keybinds["walk_right"]):
                self.movement.x = 1
            if is_key_down(DefaultConfig.keybinds["walk_down"]):
                self.movement.y = 1
            if is_key_down(DefaultConfig.keybinds["walk_left"]):
                self.movement.x = -1

            if is_key_up(DefaultConfig.keybinds["walk_up"]) and is_key_up(DefaultConfig.keybinds["walk_down"]):
                self.movement.y = 0
            if is_key_up(DefaultConfig.keybinds["walk_left"]) and is_key_up(DefaultConfig.keybinds["walk_right"]):
                self.movement.x = 0

            length: float = vector2_length_sqr(self.movement)

            if length > 0:
                self.movement.x /= length
                self.movement.y /= length

            if is_key_down(DefaultConfig.keybinds["sprint"]):
                self.sprint = 1.25
            else:
                self.sprint = 1.0

            self.position.x += self.movement.x * self.speed * self.sprint * delta
            self.position.y += self.movement.y * self.speed * self.sprint * delta

        self.draw()
