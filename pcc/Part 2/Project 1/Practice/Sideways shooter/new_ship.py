import pygame

class Ship():

	def __init__(self, game_settings, screen):
		"""Initialize the ship and its starting position"""
		# Make the self.screen the screen
		self.screen = screen
		self.game_settings = game_settings

		# Load the ship image and get its rect.
		self. image = pygame.image.load("Desktop/Main/Python Crash Course/Part 2/Alien Invasion/images/new_ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.center = float(self.rect.centerx)
		self.top = float(self.rect.top)

		# Movement flags
		self.moving_up = False
		self.moving_down = False

		# Start each ship at the left middle of the screen
		self.top = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		# Movement right flag
		self.moving_right = False
		# Movement left flag
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		# Update the center of the ship
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.game_settings.ship_speed_factor

		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.top -= self.game_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.top += self.game_settings.ship_speed_factor

		# Update rect from center
		self.rect.centerx = self.center
		self.rect.top = self.top



	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)