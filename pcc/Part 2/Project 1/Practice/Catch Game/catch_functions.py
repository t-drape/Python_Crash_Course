import sys

import pygame
import pygame.sprite

def check_events(cup):
	"""Respond to keypresses and mouses."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				cup.moving_right = True
			elif event.key == pygame.K_LEFT:
				cup.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				cup.moving_right = False
			elif event.key == pygame.K_LEFT:
				cup.moving_left = False


def check_collisions(rain, cup):
	"""Checks for collisions between drips and cup."""
	# If so get rid of raindrop
	collisions = pygame.sprite.groupcollide(rain, cup, True, False)

def update_screen(settings, screen, cup, raindrop):
	screen.fill(settings.bg_color)
	cup.blitme()
	raindrop.blitme()

	pygame.display.flip()