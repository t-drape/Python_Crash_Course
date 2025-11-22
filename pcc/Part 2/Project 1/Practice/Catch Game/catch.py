import sys

import pygame

from pygame.sprite import Group

from catch_settings import Settings
from cup import Cup
import catch_functions as cf
from raindrop2 import Raindrop
from catch_stats import GameStats

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Drop Catch")

	# Create an instance to store game statistics
	stats = GameStats(settings)

	screen_rect = screen.get_rect()

	rain = Group()

	vessel = Group()

	cup = Cup(settings, screen)

	vessel.add(cup)

	while True:
		if len(rain) == 0:
			raindrop = Raindrop(settings, stats, screen)
			rain.add(raindrop)

		cf.check_collisions(rain, vessel)


		cf.check_events(cup)
		if settings.game_active:
			cf.check_events(cup)
			cup.update()
			raindrop.update(settings, rain)
			cf.update_screen(settings, screen, cup, raindrop)
		

run_game()