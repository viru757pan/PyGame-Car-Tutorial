from config import YELLOW, BLACK
from utils import *
import pygame
import math


class Sensor:
    def __init__(self, car):
        self.color = YELLOW
        self.car = car
        self.rayCount = 5
        self.rayLength = 150
        self.raySpread = math.pi / 2

        self.readings = []
        self.rays = []

    def update(self, roadborders, computerCars):
        self.castRays()
        self.readings = []
        for i in range(len(self.rays)):
            self.readings.append(self.getTotalReading(
                self.rays[i], roadborders, computerCars))

    def lerp(self, start, end, t):
        return start + (end - start) * t

    def calculateRayAngle(self, i):
        return -(self.lerp(
            -self.raySpread / 2,
            self.raySpread / 2,
            0.5 if self.rayCount == 1 else i / (self.rayCount - 1)
        ) + math.radians(self.car.angle))

    def calculateRayPoints(self, angle):
        start = {'x': self.car.x, 'y': self.car.y}
        end = {
            'x': self.car.x + math.sin(angle) * self.rayLength,
            'y': self.car.y - math.cos(angle) * self.rayLength
        }
        return [start, end]

    def getRoadBorderReading(self, ray, roadBorders):
        touches = []

        for i in range(len(roadBorders)):
            touch = getIntersection(
                ray[0],
                ray[1],
                roadBorders[i][0],
                roadBorders[i][1]
            )
            if touch:
                touches.append(touch)

        if not touches:
            return None
        else:
            offsets = [e['offset'] for e in touches]
            minOffset = min(offsets)
            return next(e for e in touches if e['offset'] == minOffset)

    def getComputerCarReading(self, ray, computerCars):
        touches = []

        for traffic in computerCars:
            poly = traffic.Polygon
            for point in poly:
                touch = getIntersection(
                    ray[0],
                    ray[1],
                    point,
                    poly[(poly.index(point)+1) % len(poly)])

                if touch:
                    touches.append(touch)

        if not touches:
            return None
        else:
            offsets = [e['offset'] for e in touches]
            minOffset = min(offsets)
            return next(e for e in touches if e['offset'] == minOffset)

    def getTotalReading(self, ray, roadBorders, computerCars):
        roadBordersTouch = self.getRoadBorderReading(ray, roadBorders)
        computerCarsTouch = self.getComputerCarReading(ray, computerCars)

        if not roadBordersTouch and not computerCarsTouch:
            return None
        elif not roadBordersTouch:
            return computerCarsTouch
        elif not computerCarsTouch:
            return roadBordersTouch
        else:
            allIntersections = [roadBordersTouch, computerCarsTouch]
            offsets = [e['offset'] for e in allIntersections]
            return next((e for e in allIntersections if e['offset'] == min(offsets)), None)

    def castRays(self):
        self.rays = []
        for i in range(self.rayCount):
            rayAngle = self.calculateRayAngle(i)
            rayPoints = self.calculateRayPoints(rayAngle)
            self.rays.append(rayPoints)

    def draw(self, screen):
        for i in range(self.rayCount):
            start_x = self.rays[i][0]['x']
            start_y = self.rays[i][0]['y']

            end = self.rays[i][1]

            if self.readings[i]:
                end = self.readings[i]

            pygame.draw.line(screen, YELLOW, (start_x, start_y),
                             (end['x'], end['y']), 2)

            pygame.draw.line(
                screen, BLACK, (self.rays[i][1]['x'], self.rays[i][1]['y']), (end['x'], end['y']), 2)
