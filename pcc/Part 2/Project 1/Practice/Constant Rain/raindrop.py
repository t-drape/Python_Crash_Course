import pygame

from pygame.sprite import Sprite

class Raindrop(Sprite):
	"""A class to represent a single raindrop in a rainshower."""
	def __init__(self, screen):
		"""Initialize a raindrop and set its starting position."""
		super().__init__()
		self.screen = screen

		self.image = pygame.image.load("Desktop/raindrop.bmp")
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the star at its current position."""
		self.screen.blit(self.image, self.rect)


	def update(self, game_settings):
		"""Move the raindrop down."""
		screen_rect = self.screen.get_rect()
		self.y += game_settings.speed_setting
		self.rect.y = self.y
		if self.rect.y >= screen_rect.bottom:
			self.y = screen_rect.top - 1