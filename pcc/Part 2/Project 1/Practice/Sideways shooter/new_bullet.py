import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""

	def __init__(self, game_settings, screen, ship):
		"""Create bullet object at ship's current position."""
		super().__init__()
		self.screen = screen

		# Create a bullet rect at (0,0) and then set at correct position.
		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, 
			game_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store the position as a decimal
		self.x = float(self.rect.x)


		self.color = game_settings.bullet_color
		self.speed_factor = game_settings.bullet_speed_factor

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.x += self.speed_factor
		# Update the rect position
		self.rect.x = self.x


	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)