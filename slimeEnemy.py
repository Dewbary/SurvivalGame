import pygame
import math
import random

class SlimeEnemy:
    def __init__(self, x, y, player, display_scroll):
        self.x = x
        self.y = y
        self.player = player
        self.display_scroll = display_scroll
        self.animation_images = [pygame.image.load("./assets/slime_animation_0.png"), pygame.image.load("./assets/slime_animation_1.png"),
        pygame.image.load("./assets/slime_animation_2.png"), pygame.image.load("./assets/slime_animation_0.png")]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-300, 300)
        self.offset_y = random.randrange(-300, 300)
    
    def main(self, display):
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-300, 300)
            self.offset_y = random.randrange(-300, 300)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1

        if self.player.x + self.offset_x > self.x - self.display_scroll[0]:
            self.x += 1
        elif self.player.x + self.offset_x < self.x - self.display_scroll[0]:
            self.x -= 1

        if self.player.y + self.offset_y > self.y - self.display_scroll[1]:
            self.y += 1
        elif self.player.y + self.offset_y < self.y - self.display_scroll[1]:
            self.y -= 1 

        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//4], (32, 30)), (self.x-self.display_scroll[0], self.y-self.display_scroll[1]))
