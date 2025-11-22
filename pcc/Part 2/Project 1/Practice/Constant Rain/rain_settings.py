class Settings:
	"""Initialize settings for falling rain."""

	def __init__(self):
		"""Initialize simulation settings."""
		# Screen settings 
		self.screen_width = 1475
		self.screen_height = 800
		self.bg_color = (255, 255, 255)

		# Rain settings
		self.speed_setting = 1.5