import math
import pygame

from utils import blit_rotate_center


class AbstractCar:
    def __init__(self):
        self.img = self.IMG
        self.max_speed = 4
        self.val = 0
        self.rotation_val = 4
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_val
        elif right:
            self.angle -= self.rotation_val

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.val = min(self.val + self.acceleration, self.max_speed)
        self.move()

    def move_backward(self):
        self.val = max(self.val - self.acceleration, -self.max_speed)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.val
        horizontal = math.sin(radians) * self.val

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.val = 0
