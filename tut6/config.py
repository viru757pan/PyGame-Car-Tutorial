import pygame
from utils import scale_image
pygame.font.init()

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

# IMAGES
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)

FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (70, 50)

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREY_CAR = scale_image(pygame.image.load("imgs/grey-car.png"), 0.55)
PURPLE_CAR = scale_image(pygame.image.load("imgs/purple-car.png"), 0.55)
WHITE_CAR = scale_image(pygame.image.load("imgs/white-car.png"), 0.55)

# RED_CAR_MASK = pygame.mask.from_surface(RED_CAR)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

WIDTH = HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
screen_width = 200
screen_height = HEIGHT
neuralscreen_width = 480
neuralscreen_height = 650

MAIN_FONT = pygame.font.SysFont("comicsans", 40)

FPS = 60
# PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
#         (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]

PATH = [(160, 600), (160, 500), (100, 400), (160, 300), (160, 200)]
