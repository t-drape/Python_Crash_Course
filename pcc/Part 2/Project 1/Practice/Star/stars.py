import sys

from random import randint

import pygame

from pygame.sprite import Group

from star import Star

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Shining Stars")

	# Set the background color
	bg_color = (255, 255, 255)

	stars = Group()

	screen_rect = screen.get_rect()

	star = Star(screen)
	star_width = star.rect.width
	star_height = star.rect.height
	available_space_x = screen_rect.width - 2 * star_width
	number_stars_x = int(available_space_x / (2 * star_width))
	available_height = screen_rect.height - 2 * star_height
	number_rows = int(available_height / star_height)

	for row in range(number_rows):
		for star_number in range(number_stars_x):
			# Create a star and place it in row
			star = Star(screen)
			star.x = star_width + 2 * star_width * star_number
			star.rect.x = star.x
			star.y = star_height + 2 * star_height * row
			star.rect.y = star.y
			random_number = randint(-10, 10)
			star.rect.x += random_number
			star.rect.y -= random_number
			stars.add(star) 
	# Start the main while loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Redraw the screen each pass through the loop
		screen.fill(bg_color)
		stars.draw(screen)

		# Update the screen
		pygame.display.flip()

run_game()