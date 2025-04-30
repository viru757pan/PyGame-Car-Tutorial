import pygame
from utils import blit_text_center
from config import *
from ComputerCar import ComputerCar
from PlayerCar import PlayerCar
from GameInfo import GameInfo
from control import Control

pygame.font.init()


def draw(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)

    level_text = MAIN_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))

    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(
        f"Vel: {round(player_car.val, 1)}px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

    player_car.draw(win)
    player_car.draw_sensor(win)
    computer_car.draw(win)
    pygame.display.update()


def handle_collision(player_car, computer_car, game_info):
    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if computer_finish_poi_collide != None:
        blit_text_center(WIN, MAIN_FONT, "You lost!")
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
                       (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
        self.player_car = PlayerCar()
        self.computer_car = ComputerCar(PATH)
        self.game_info = GameInfo()

    def run(self):
        run = True
        while run:
            self.clock.tick(FPS)

            draw(WIN, self.images, self.player_car,
                 self.computer_car, self.game_info)

            while not self.game_info.started:
                blit_text_center(
                    WIN, MAIN_FONT, f"Press any key to start level {self.game_info.level}!")
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                    if event.type == pygame.KEYDOWN:
                        self.game_info.start_level()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            Control.move_player(self.player_car)
            self.computer_car.move()

            handle_collision(
                self.player_car, self.computer_car, self.game_info)

            if self.game_info.game_finished():
                blit_text_center(WIN, MAIN_FONT, "You won the game!")
                pygame.time.wait(5000)
                self.game_info.reset()
                self.player_car.reset()
                self.computer_car.reset()


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
