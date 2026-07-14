from pyray import *
from timer import Timer

class Animation:
    def __init__(self,
                 row: int,
                 frame_count: int,
                 frame_speed: int,
                 loop: bool = True) -> None:
        self.row: int = row
        self.frame_count: int = frame_count
        self.frame_speed: int = frame_speed
        self.loop: bool = loop

        self.frame: int = 0
        self.timer: Timer = Timer(1 / self.frame_speed)
        self.finished: bool = False

    def reset(self) -> None:
        self.frame: int = 0
        self.finished: bool = False
        self.timer.reset()

    def update(self) -> None:
        if self.finished: return

        self.timer.update()

        if self.timer.time <= 0:
            self.timer.reset()

            self.frame += 1

            if self.frame >= self.frame_count:
                if self.loop:
                    self.frame = 0
                else:
                    self.finished = True

class AnimationManager:
    def __init__(self, frame_size: Vector2) -> None:
        self.frame_size: Vector2 = frame_size
        self.animations: dict[str, Animation] = {}
        self.current_animation: str = "idle"

    def add(self, name: str, animation: Animation) -> None:
        self.animations[name] = animation

    def play(self, name: str) -> None:
        if name == self.current_animation: return

        self.current_animation = name
        self.animations[name].reset()

    def update(self) -> None:
        self.animations[self.current_animation].update()

    def source(self) -> Rectangle:
        animation: Animation = self.animations[self.current_animation]

        return Rectangle(
            animation.frame * self.frame_size.x,
            animation.row * self.frame_size.y,
            self.frame_size.x,
            self.frame_size.y
        )
