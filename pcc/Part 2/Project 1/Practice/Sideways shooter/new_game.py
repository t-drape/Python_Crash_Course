import pygame
from pygame.sprite import Group

from new_game_settings import Settings
from new_ship import Ship
import new_game_functions as gf

def run_game():
	# Initialize screen and create a screen object
	pygame.init()
	# Initialize settings
	game_settings = Settings()

	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make a ship
	ship = Ship(game_settings, screen)

	# Make a group to store bullets
	bullets = Group()

	# Start the main loop for the game
	while True:
		# Watch for keyboard and mouse events
		gf.check_events(game_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets, screen)
		gf.update_screen(game_settings, screen, ship, bullets)

run_game()