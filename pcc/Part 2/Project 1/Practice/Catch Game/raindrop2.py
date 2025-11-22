import pygame

from pygame.sprite import Sprite
from time import sleep
from random import randint
from catch_stats import GameStats

class Raindrop(Sprite):
	"""A class to represent a single raindrop in a rainshower."""
	def __init__(self, settings, stats, screen):
		"""Initialize a raindrop and set its starting position."""
		super().__init__()
		self.screen = screen
		self.settings = settings
		self.stats = stats

		self.image = pygame.image.load("Desktop/raindrop.bmp")
		self.rect = self.image.get_rect()

		new_x = randint(self.rect.width, (settings.screen_width - self.rect.width))

		self.rect.x = new_x
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

		self.y = float(self.rect.y)

	def blitme(self):
		"""Draw the star at its current position."""
		self.screen.blit(self.image, self.rect)


	def update(self, game_settings, rain):
		"""Move the raindrop down."""
		screen_rect = self.screen.get_rect()
		self.y += game_settings.rain_speed_setting
		self.rect.y = self.y
		if self.rect.bottom >= screen_rect.bottom:
			rain.remove(self)
			self.stats.drops_left -= 1
			if self.stats.drops_left == 0:
				self.settings.game_active = False

			sleep(.5)