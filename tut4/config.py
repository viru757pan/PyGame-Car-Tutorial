import pygame
from utils import scale_image
pygame.font.init()

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

MAIN_FONT = pygame.font.SysFont("comicsans", 44)


FPS = 60
PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]


def create_track_border_polygon(TRACK_BORDER):
    track_border_img = TRACK_BORDER
    track_border_mask = pygame.mask.from_surface(track_border_img)
    polygon_points = []

    for x in range(track_border_img.get_width()):
        for y in range(track_border_img.get_height()):
            if track_border_mask.get_at((x, y)):
                polygon_points.append((x, y))

    return polygon_points


TRACK_BORDER_POLYGON = create_track_border_polygon(TRACK_BORDER)

# print(TRACK_BORDER_POLYGON)
