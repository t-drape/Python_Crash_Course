import pygame

from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to represent a single star in a fleet."""
	def __init__(self, screen):
		"""Initialize a star and set its starting position."""
		super().__init__()
		self.screen = screen

		# Load the star image and set its rect attribute
		self.image = pygame.image.load("Desktop/Main/Python Crash Course/Part 2/Practice/Star/star.bmp")
		self.rect = self.image.get_rect()

		# Start each star at the top left corner of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store its exact position
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the star at its current position."""
		self.screen.blit(self.image, self.rect)