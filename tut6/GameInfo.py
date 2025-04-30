import time
from config import FPS


class GameInfo:
    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = time.time()

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def update_level_time(self):
        if self.started:
            self.level_start_time += 1 / FPS

    def get_level_time(self):
        if not self.started:
            return 0
        else:
            return round(time.time() - self.level_start_time)
