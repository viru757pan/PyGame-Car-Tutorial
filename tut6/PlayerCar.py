import pygame
import math
from config import GREEN_CAR
from Sensor import Sensor
from Control import Control
from utils import polysIntersect
from AbstractCar import AbstractCar
from Network import NeuralNetwork


class PlayerCar(AbstractCar):
    def __init__(self, pos):
        self.img = GREEN_CAR
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.max_speed = 3
        self.speed = 0
        self.angle = 0
        self.START_POS = pos
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        super().__init__(self.x, self.y, self.width, self.height, self.max_speed)

        self.damaged = False

        self.sensors = Sensor(self)

        self.controls = Control()

        # self.brain = NeuralNetwork([self.sensors.rayCount, 4])
        # Update the neural network to the specified structure
        self.brain = NeuralNetwork([self.sensors.rayCount, 4])

    def update(self, roadBorders, computerCars):
        if not self.damaged:
            self.move()
            self.Polygon = self.createPolygon()
            self.damaged = self.assessDamage(roadBorders, computerCars)
        else:
            self.bounce()

        if self.sensors:
            super().update()
            self.sensors.update(roadBorders, computerCars)

            offsets = [0 if s is None else s['offset']
                       for s in self.sensors.readings]

            outputs = NeuralNetwork.feedForward(offsets, self.brain)
            # print(outputs)

            if self.brain:
                self.controls.forward = outputs[0]
                self.controls.left = outputs[1]
                self.controls.right = outputs[2]
                self.controls.reverse = outputs[3]

    def assessDamage(self, roadBorders, computerCars):
        for road_border in roadBorders:
            if polysIntersect(self.Polygon, road_border):
                return True

        for traffic in computerCars:
            if polysIntersect(self.Polygon, traffic.Polygon):
                return True

        return False

    def bounce(self):
        self.speed = 0
        self.controls.forward = False
        self.controls.reverse = False
        self.controls.left = False
        self.controls.right = False

    def draw(self, screen):

        super().draw(screen)

        # if self.Polygon:
        #     draw_polygon(screen, self.Polygon)

        self.sensors.draw(screen)


def draw_polygon(screen, points):
    if len(points) >= 2:
        pygame.draw.polygon(screen, (0, 0, 0), [
            (point['x'], point['y']) for point in points], 2)
