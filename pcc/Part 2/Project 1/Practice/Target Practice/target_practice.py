import sys

import pygame

from pygame.sprite import Group

from target_settings import Settings
from new_ship import Ship
import target_functions as tf
from target_bullet import Bullet
from new_button import Button
from target_rect import Target
from target_stats import GameStats
from new_button import Button

def run_game():
	# Initialize the screen and create a screen object
	pygame.init()
	settings = Settings()

	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Target Practice")

	stats = GameStats(settings)
	play_button = Button(settings, screen, "PLAY")

	# Create the ship
	ship = Ship(settings, screen)
	bullets = Group()
	target = Target(settings, screen)

	while True:
		tf.check_events(settings, stats, screen, ship, bullets, play_button)
		if stats.game_active:
			ship.update()
			target.update()
			tf.update_bullets(settings, stats, screen, ship, bullets, target)
		tf.update_screen(settings, screen, ship, bullets, target, stats, play_button)



run_game()