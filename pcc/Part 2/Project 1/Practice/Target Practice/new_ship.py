import pygame

class Ship():
	"""Attributes for a ship in a game, target practice."""
	def __init__(self, game_settings, screen):
		"""Initialize the ship and its starting position."""
		self.screen = screen
		self.settings = game_settings
		self.image = pygame.image.load("Desktop/new_ship.bmp")
		self.image = pygame.transform.rotate(self.image, -90)
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery


		self.center = float(self.rect.centerx)

		self.moving_up = False
		self.moving_down = False


	def update(self):
		"""Move the ship in response to input."""
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.top -= self.settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.top += self.settings.ship_speed_factor


	def blitme(self):
		"""Draw the ship to the screen."""
		self.screen.blit(self.image, self.rect)


	def center_ship(self):
		"""Recenter the ship."""
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery