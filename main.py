import pygame
from settings import *
from slimeEnemy import *
from player import *
from playerBullet import *
import sys
from level import *

# player_walk_images = [pygame.image.load("../Documents/SurvivalPythonGame/assets/player_walk_0.png"), pygame.image.load("../Documents/SurvivalPythonGame/assets/player_walk_1.png"),
#         pygame.image.load("../Documents/SurvivalPythonGame/assets/player_walk_2.png"), pygame.image.load("../Documents/SurvivalPythonGame/assets/player_walk_3.png")]

# player_weapon = pygame.image.load("../Documents/SurvivalPythonGame/assets/shotgun.png").convert()
# player_weapon.set_colorkey((255, 255, 255))

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.display.fill('black')
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)
        # player = Player(400, 300, 32, 32)

        # display_scroll = [0, 0]

        # enemies = [SlimeEnemy(400, 300, player, display_scroll), SlimeEnemy(500, 200, player, display_scroll), SlimeEnemy(100, 300, player, display_scroll), SlimeEnemy(500, 200, player, display_scroll)]

        # player_bullets = []

        # while True:
        #     self.display.fill((24,164,86))

        #     mouse_x, mouse_y = pygame.mouse.get_pos()

        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #             pygame.quit()

        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #                 if event.button == 1: 
        #                     player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

        #     keys = pygame.key.get_pressed()

        #     pygame.draw.rect(self.display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

        #     if keys[pygame.K_a]:
        #         display_scroll[0] -= 5

        #         player.moving_left = True

        #         for bullet in player_bullets:
        #             bullet.x += 5
        #     if keys[pygame.K_d]:
        #         display_scroll[0] += 5

        #         player.moving_right = True

        #         for bullet in player_bullets:
        #             bullet.x -= 5
        #     if keys[pygame.K_w]:
        #         display_scroll[1] -= 5

        #         for bullet in player_bullets:
        #             bullet.y += 5
        #     if keys[pygame.K_s]:
        #         display_scroll[1] += 5

        #         for bullet in player_bullets:
        #             bullet.y -= 5

        #     player.main(self.display)

        #     for bullet in player_bullets:
        #         bullet.main(self.display)

        #     for enemy in enemies:
        #         enemy.main(self.display)


        #     self.clock.tick(60)
        #     pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()


# generating map
# bullets deal damage to enemies
# enemies deal damage to player when touching player
# Gets progressively harder, levels?
# Timer/Score
# Titlescreen, Game Over screen.
# Get better guns when reach a certain amount of kills/score.