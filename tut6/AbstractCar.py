import math
import pygame

from Control import Control
from config import *


class AbstractCar:
    def __init__(self, x, y, width, height, maxSpeed=3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 0
        self.acceleration = 0.2
        self.maxSpeed = maxSpeed
        self.friction = 0.05
        self.angle = 0
        self.angle_degrees = 0
        self.damaged = False

        self.direction = 3  # Initialize the direction as forward

        self.controls = Control()

    def update(self):
        self.move()

    def move(self):
        if self.controls.forward:
            self.speed += self.acceleration
        if self.controls.reverse:
            self.speed -= self.acceleration

        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        if self.speed < -self.maxSpeed / 2:
            self.speed = -self.maxSpeed / 2

        if self.speed > 0:
            self.speed -= self.friction
        if self.speed < 0:
            self.speed += self.friction
        if abs(self.speed) < self.friction:
            self.speed = 0

        if self.speed != 0:
            flip = 1 if self.speed > 0 else -1
            if self.controls.left:
                self.angle += 4 * flip
            if self.controls.right:
                self.angle -= 4 * flip

        radians = math.radians(self.angle)
        self.x -= math.sin(radians) * self.speed
        self.y -= math.cos(radians) * self.speed

    def createPolygon(self):
        points = []
        rad_x = math.hypot(self.width, self.height)/2
        rad_y = math.hypot(self.width, self.height)/2
        p_x = self.x
        p_y = self.y

        points.append({
            'x': p_x - math.sin(math.radians(self.angle - 45)) * rad_x,
            'y': p_y - math.cos(math.radians(self.angle - 45)) * rad_y
        })
        points.append({
            'x': p_x - math.sin(math.radians(self.angle + 45)) * rad_x,
            'y': p_y - math.cos(math.radians(self.angle + 45)) * rad_y
        })
        points.append({
            'x': p_x - math.sin(math.radians(self.angle + 135)) * rad_x,
            'y': p_y - math.cos(math.radians(self.angle + 135)) * rad_y
        })
        points.append({
            'x': p_x - math.sin(math.radians(self.angle - 135)) * rad_x,
            'y': p_y - math.cos(math.radians(self.angle - 135)) * rad_y
        })

        return points

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.img, self.angle)
        rect = rotated_image.get_rect()
        rect.center = (self.x, self.y)
        screen.blit(rotated_image, rect)
