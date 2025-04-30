import pygame
from config import *
from Control import Control
from AbstractCar import AbstractCar


class ComputerCar(AbstractCar):
    def __init__(self, pos, img):
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.max_speed = 4
        self.speed = 0
        self.angle = 0
        self.START_POS = pos
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        self.Polygon = ""
        super().__init__(self.x, self.y, self.width, self.height, self.max_speed)

        self.controls = Control()

    def update(self):
        # self.auto_drive()
        super().update()
        self.Polygon = self.createPolygon()

    def auto_drive(self):
        self.speed += self.acceleration
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def draw(self, screen):
        super().draw(screen)

        # if self.Polygon:
        #     draw_polygon(screen, self.Polygon)


def draw_polygon(screen, points):
    if len(points) >= 2:
        pygame.draw.polygon(screen, (255, 0, 0), [
            (point['x'], point['y']) for point in points], 2)
