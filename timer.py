from pyray import get_frame_time

class Timer:
    def __init__(self, time: float) -> None:
        self.start_time = time
        self.time: float = time

    def update(self) -> None:
        self.time -= get_frame_time()

    def reset(self) -> None:
        self.time = self.start_time
