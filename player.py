import pygame
import math

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load("./assets/player.png").convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0, -26)

		self.direction = pygame.math.Vector2()
		self.speed = 20

		self.obstacle_sprites = obstacle_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right
		
		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def update(self):
		self.input()
		self.move(self.speed)

# class Player:
#     def __init__(self, x, y, width, height, player):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.player = player
#         self.animation_count = 0
#         self.moving_right = False
#         self.moving_left = False
#     def handle_weapons(self, display):
#         mouse_x, mouse_y = pygame.mouse.get_pos()

#         rel_x, rel_y = mouse_x - self.player.x, mouse_y - self.player.y
#         angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

#         # player_weapon_copy = pygame.transform.rotate(player_weapon, angle)

#         # display.blit(player_weapon_copy, (self.x +15-int(player_weapon_copy.get_width()/2), self.y+25-int(player_weapon_copy.get_height()/2)))

#     def main(self, display):
#         if self.animation_count + 1 >= 16:
#             self.animation_count = 0

#         self.animation_count += 1

#         # if self.moving_right:
#             # display.blit(pygame.transform.scale(player_walk_images[self.animation_count // 4], (32, 42)), (self.x, self.y))
#         # elif self.moving_left:
#             # display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count // 4], True, False), (32, 42)), (self.x, self.y)) 
#         # else:
#             # display.blit(pygame.transform.scale(player_walk_images[0], (32, 42)), (self.x, self.y))
        
#         self.handle_weapons(display)
       
#         self.moving_right = False
#         self.moving_left = False