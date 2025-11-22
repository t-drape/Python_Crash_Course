import pygame
from pygame.sprite import Sprite

class Target(Sprite):
	"""Initialize target attributes."""
	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings

		# Create a bullet rect at (0, 0) then set at correct position.
		self.rect = pygame.Rect(0, 0, self.settings.target_width,
		 self.settings.target_height)

		self.rect.centery = self.screen_rect.centery
		self.rect.right = self.screen_rect.right

		self.top = float(self.rect.top)
		self.rect.top = self.top
		self.bottom = float(self.rect.bottom)
		self.rect.bottom = self.bottom

		self.color = settings.target_color
		self.speed_factor = float(settings.target_speed_factor)

		self.moving_up = True
		self.moving_down = False


	def update(self):
		"""Adjust the position of the target."""

		if self.moving_up and self.rect.top > 0:
			self.rect.top -= self.speed_factor
		if self.rect.top == 0:
			self.moving_up = False
			self.moving_down = True
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.bottom += self.speed_factor
		if self.rect.bottom == self.screen_rect.bottom:
			self.moving_up = True
			self.moving_down = False


	def draw_target(self):
		"""Draw the target to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)