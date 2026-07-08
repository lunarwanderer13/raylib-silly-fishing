from pyray import get_frame_time

class Timer:
    def __init__(self, time: float) -> None:
        self.time: float = time

    def update(self) -> None:
        self.time -= get_frame_time()