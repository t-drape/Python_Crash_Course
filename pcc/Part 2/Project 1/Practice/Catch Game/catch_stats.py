class GameStats():
	"""Initialize the game stats for catch."""

	def __init__(self, game_settings):
		"""Initialize stats."""
		self.settings = game_settings
		self.reset_stats()


	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.drops_left = self.settings.drops_allowed