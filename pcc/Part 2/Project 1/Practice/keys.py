import sys

import pygame

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption(("Keys"))

	# Start with the loop
	while True:

		# Watch for keyboard events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				print(event.key)


		pygame.display.flip()

run_game()
