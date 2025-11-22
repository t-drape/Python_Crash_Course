class Settings():
	"""Initialize the game settings for target practice."""
	def __init__(self):
		"""Initialize settings."""
		self.bg_color = (0, 0, 0)


		# Ship settings
		

		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (50, 255, 50)
		
		self.bullets_allowed = 1
		self.misses = 3

		# Target settings
		self.target_width = 10
		self.target_height = 100
		self.target_color = (255, 0, 255)

		self.speed_up_scale = 1.1

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.target_speed_factor = 1


	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speed_up_scale
		self.target_speed_factor *= self.speed_up_scale