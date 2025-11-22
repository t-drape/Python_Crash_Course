import sys

import pygame

from random import randint

from raindrop import Raindrop

def create_shower(rain, screen):
	"""Create a group of raindrops to simulate a shower."""
	screen_rect = screen.get_rect()
	r = Raindrop(screen)
	r_width = r.rect.width
	r_height = r.rect.height
	available_space_x = screen_rect.width - 2 * r_width
	number_drops = int(available_space_x / r_width)
	available_height = screen_rect.height
	rows = int(available_height / (2 * r_height))

	for row in range(rows):
		for r_number in range(number_drops):
			rd = Raindrop(screen)
			rd.x = r_width + 2 * r_width * r_number
			rn = randint(-10, 10)
			rd.rect.x = rd.x
			rd.rect.x += rn
			rn = randint(-10, 10)
			rd.y = 2 * r_height * row
			rd.rect.y = rd.y
			rd.rect.y += rn
			rain.add(rd)


def update_raindrops(rain, game_settings):
	"""Update the position of each raindrop."""
	rain.update(game_settings)