class GameStats():
	"""Initialize game statistics."""
	def __init__(self, game_settings):
		self.settings = game_settings
		self.reset_stats()
		self.game_active = False


	def reset_stats(self):
		"""Initialize stats each game."""
		self.misses = self.settings.misses

