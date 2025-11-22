import sys

import pygame

from new_bullet import Bullet

def check_keydown_events(event, game_settings, screen, ship, bullets):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
	"""Respond to key lifts."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False


def check_events(game_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, game_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)



def update_screen(game_settings, screen, ship, bullets):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen through each pass through the loop
	screen.fill(game_settings.bg_color)

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()

	# Make the most recently drawm screen visible.
	pygame.display.flip()

def update_bullets(bullets, screen):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullets
	bullets.update()
	screen_rect = screen.get_rect()

	# Remove old bullets
	for bullet in bullets.copy():
		if bullet.rect.left >= screen_rect.right:
			bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
	"""Fire a new bullet if limit has not been reached"""
	# Create a new bullet and add it to group
	if len(bullets) < game_settings.bullets_allowed:
		new_bullet = Bullet(game_settings, screen, ship)
		bullets.add(new_bullet)

