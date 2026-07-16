from pyray import *
from random import randint, uniform as randfloat
from config import GameConfig
from timer import Timer
from animation import AnimationManager, Animation
from items import ItemManager, Rod, get_rod, Bait, get_bait

class Player:
    def __init__(self, data) -> None:
        self.data = data

        self.animations: AnimationManager = AnimationManager(Vector2(16, 16))
        self.sprite_sheet: Texture = load_texture("assets/sprites/player/player.png")
        self.animations.add("idle", Animation(0, 2, 2))
        self.animations.add("walk", Animation(1, 4, 4))
        self.animations.add("run", Animation(2, 4, 4))
        self.animations.add("sit", Animation(3, 2, 2, False))

        self.inventory: ItemManager = ItemManager()

        self.position: Vector2 = Vector2(self.data["player"]["position"]["x"], self.data["player"]["position"]["y"])

        self.movement: Vector2 = Vector2(0, 0)
        self.speed: float = 75
        self.sprint: float = 1.0
        self.flipped: bool = False
        self.size: Vector2 = Vector2(10, 16)
        self.rect: Rectangle = Rectangle(self.position.x - self.size.x / 2,
                                         self.position.y - 1,
                                         self.size.x,
                                         1)

        self.equipped_rod: Rod | None = get_rod(self.data["player"]["equipped_rod"])
        self.equipped_bait: Bait | None = get_bait(self.data["player"]["equipped_bait"])

        self.cast_timer: Timer | None = None
        self.can_cast: bool = False
        self.is_casting: bool = False
        self.is_cast: bool = False
        self.can_reel: bool = False
        self.can_bait: bool = False
        self.can_move: bool = True
        self.can_interact: bool = True
        self.can_open_inventory: bool = True

        self.bite_timer: Timer | None = None
        self.fish_bit: bool = False
        self.min_bite_time: float = 2.0
        self.max_bite_time: float = 3.0
        self.bite_chance: int = 10

    def move(self) -> None:
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

        self.position.x += round(self.movement.x * self.speed * self.sprint * get_frame_time())
        self.position.y += round(self.movement.y * self.speed * self.sprint * get_frame_time())
        self.rect.x = self.position.x - self.size.x / 2
        self.rect.y = self.position.y - 1

    def draw(self) -> None:
        source: Rectangle = self.animations.source()

        if self.flipped:
            source.x += source.width
            source.width *= -1

        draw_texture_rec(self.sprite_sheet,
                         source,
                         Vector2(self.position.x - self.animations.frame_size.x / 2, self.position.y - self.size.y),
                         WHITE)

        #draw_rectangle_v(Vector2(self.position.x - self.size.x / 2, self.position.y - self.size.y), self.size, BLUE)
        draw_rectangle_rec(self.rect, YELLOW)

    def update(self) -> None:
        self.flipped: bool = self.movement.x < 0

        if self.movement.x != 0 or self.movement.y != 0:
            if self.sprint < 1.25: self.animations.play("walk")
            else: self.animations.play("run")
        else:
            self.animations.play("idle")

        if self.can_move: self.move()

        self.can_cast = bool(any(check_collision_recs(self.rect, fishing_spot.rect) for fishing_spot in GameConfig.fishing_spots.values()) and not self.is_cast and not self.can_reel and self.equipped_rod)

        if self.can_cast and self.equipped_rod and is_key_pressed(self.data["keybinds"]["cast_rod"]):
            self.can_cast = False
            self.is_casting = True
            self.is_cast = False
            self.can_move = False
            self.can_interact = False
            self.can_open_inventory = False
            self.cast_timer = Timer(1.0)

            self.fish_bit = False
            self.min_bite_time: float = 2.0 - self.equipped_rod.item_id / 10
            self.max_bite_time: float = 3.0 - self.equipped_rod.item_id / 10
            self.bite_chance: int = self.equipped_rod.item_id * 10
            self.bite_timer = Timer(randfloat(self.min_bite_time, self.max_bite_time))

        if self.is_casting and self.equipped_rod and self.cast_timer:
            self.cast_timer.update()

            if self.cast_timer.time <= 0:
                self.is_casting = False
                self.is_cast = True
                self.can_reel = True

        if self.is_cast and self.equipped_rod and self.bite_timer:
            if not self.fish_bit: self.bite_timer.update()

            if self.bite_timer.time <= 0:
                if randint(0, 99) < self.bite_chance:
                    self.fish_bit = True
                else:
                    self.bite_timer = Timer(randfloat(self.min_bite_time, self.max_bite_time))
                    print("Bob...")

            if self.fish_bit:
                print("Bite!")

        if self.can_reel and is_key_pressed(self.data["keybinds"]["reel_rod"]):
            self.can_reel = False
            self.is_cast = False
            self.can_reel = False
            self.can_move = True
            self.can_interact = True
            self.can_open_inventory = True
            self.fish_bit = False

        self.animations.update()
