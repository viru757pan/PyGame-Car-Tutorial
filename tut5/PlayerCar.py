import pygame
from AbstractCar import AbstractCar
from config import RED_CAR
from Sensor import Sensor


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.val = max(self.val - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.val = -self.val
        self.move()

    def draw_sensor(self, win):
        sensors = Sensor(self)
        sensors.draw(win)
