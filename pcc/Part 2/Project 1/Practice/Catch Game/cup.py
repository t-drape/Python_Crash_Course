import pygame

from pygame.sprite import Sprite

class Cup(Sprite):
	"""A class to represent a cup to catch drops."""
	def __init__(self, catch_settings, screen):
		"""Initialize a cup and set its starting position."""
		super().__init__()
		self.screen = screen
		self.settings = catch_settings

		self.image = pygame.image.load("Desktop/cup.bmp")
		self.rect = self.image.get_rect()

		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.x = float(self.rect.x)

		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""Update the cup's position based on the movement flag."""
		# Update the center of the cup
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.settings.cup_speed_setting
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.settings.cup_speed_setting


	def blitme(self):
		"Draw the cup at its starting position."
		self.screen.blit(self.image, self.rect)