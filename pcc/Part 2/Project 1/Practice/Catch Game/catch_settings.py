class Settings():
	"""Initialize settings for catch game."""

	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1475
		self.screen_height = 800
		self.bg_color = (0, 0, 0)

		# Initialize the cup settings
		self.cup_speed_setting = 4

		self.rain_speed_setting = 3.5

		# Allowed drops
		self.drops_allowed = 3
		self.game_active = True