import sys

import pygame

from pygame.sprite import Group

from raindrop import Raindrop
from rain_settings import Settings
import rain_functions as rf

def run_game():
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Falling Rain")

	screen_rect = screen.get_rect()

	rain = Group()
	rf.create_shower(rain, screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(game_settings.bg_color)


		rain.draw(screen)
		rf.update_raindrops(rain, game_settings)

		pygame.display.flip()

run_game()