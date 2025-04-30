import pygame
from pygame.locals import *
import json
from pathlib import Path
import os
import random

from config import *
from ComputerCar import ComputerCar
from PlayerCar import PlayerCar
from GameInfo import GameInfo
from Road import Road
from Network import NeuralNetwork
from Visualizer import Visualizer

pygame.font.init()


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.Surface((screen_width, screen_height))
        self.neuralScreen = pygame.Surface(
            (neuralscreen_width, neuralscreen_height))
        self.screen_x = (WIDTH - screen_width) // 6
        self.images = [(GRASS, (0, 0)), (FINISH, FINISH_POSITION)]
        self.road = Road(screen_width / 2, screen_width * 0.9)
        self.player_car = PlayerCar((100, 700))
        self.computer_car = self.generateCars()
        self.game_info = GameInfo()
        self.game_info.start_level()

    def draw(self):
        self.read_data()

        self.screen.fill(GRAY)
        self.neuralScreen.fill(BLACK)
        WINDOW.fill(WHITE)
        self.road.draw(self.screen, self.player_car)

        for i in range(len(self.computer_car)):
            self.computer_car[i].draw(self.screen)
        self.player_car.draw(self.screen)

        Visualizer.draw_network(self.neuralScreen, self.player_car.brain)

        time_text = MAIN_FONT.render(
            f"Time: {self.game_info.get_level_time()}s", 1, RED)
        WINDOW.blit(time_text, (570, 5))

        vel_text = MAIN_FONT.render(
            f"Vel: {round(self.player_car.speed, 1)}px/s", 1, RED)
        WINDOW.blit(vel_text, (570, 42))

        WINDOW.blit(self.screen, (self.screen_x, 0))
        WINDOW.blit(self.neuralScreen, (self.screen_x + 210, 110))

    def run(self):
        self.clock.tick(FPS)

        self.draw()

        pygame.display.flip()

    def generateCars(self):
        cars = []
        # pos = [(40, 550), (160, 550), (40, 400),
        #        (100, 400), (100, 250), (160, 250)]
        pos = [(100, 550)]
        c = [RED_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR]
        for i in range(len(pos)):
            random_value = random.randint(0, 3)
            cars.append(ComputerCar(pos[i], c[random_value]))
        return cars

    def save_button_click(self):
        print("Save")

        data = {'BestBrain': self.player_car.brain}
        file_path = './tut6/data/data.json'
        with open(file_path, 'w') as file:
            json.dump(self.player_car.brain.to_json(), file)
        file.close()

    def read_data(self):
        file_path = Path('./tut6/data/data.json')
        file_path.touch(exist_ok=True)

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.player_car.brain = NeuralNetwork.from_json(data)
                NeuralNetwork.mutate(self.player_car.brain, 0.5)

        except json.JSONDecodeError:
            if json.JSONDecodeError:
                self.save_button_click()
                # print(json.JSONDecodeError)

        file.close()

    def delete_button_click(self):
        # Specify the file path of the JSON file
        file_path = './tut6/data/data.json'

        # Check if the JSON file exists
        if os.path.exists(file_path):
            # Delete the JSON file
            os.remove(file_path)
            print("Deleted")
        else:
            print("Data file does not exist.")


if __name__ == "__main__":
    game = Game()
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    exit()
                if event.key == K_s:
                    game.save_button_click()
                if event.key == K_d:
                    game.delete_button_click()
            if event.type == pygame.QUIT:
                running = False
            else:
                game.player_car.controls.handle_event(event)
                # for i in range(len(game.computer_car)):
                #     game.computer_car[i].controls.handle_event2(event)

        game.player_car.update(game.road.borders, game.computer_car)
        for i in range(len(game.computer_car)):
            game.computer_car[i].update()
        # game.computer_car.update()

        if game.player_car.damaged:
            game.game_info.reset()

        game.run()

    pygame.quit()
