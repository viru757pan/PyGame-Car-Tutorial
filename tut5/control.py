import pygame


class Control:
    def move_player(player_car):
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            moved = True
            player_car.move_forward()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            moved = True
            player_car.move_backward()

        if player_car.val != 0:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player_car.rotate(left=True)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player_car.rotate(right=True)

        if not moved:
            player_car.reduce_speed()
