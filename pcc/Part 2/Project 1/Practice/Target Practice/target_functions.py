import sys

import pygame
from time import sleep

from target_bullet import Bullet
from target_rect import Target
from new_button import Button


def check_keydown_events(event, settings, stats, screen, ship, bullets):
	"""Respond the keypresses and user input."""
	if event.key == pygame.K_q:
		sys.exit()

	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_RETURN:
		fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
	"""Respond to the release of keys."""
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(settings, stats, screen, ship, bullets, play_button):
	"""Respond to keypresses and events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, stats, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings, stats, play_button, mouse_x, mouse_y, bullets, ship)


def check_play_button(settings, stats, play_button, mouse_x, mouse_y, bullets, ship):
	"""Start a new game if button pushed."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		bullets.empty()
		ship.center_ship()


def fire_bullet(settings, screen, ship, bullets):
	"""Fire a bullet from the ship, if limit not reached."""
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)


def update_bullets(settings, stats, screen, ship, bullets, target):
	"""Update position of bullets and get rid of old bullets."""
	screen_rect = screen.get_rect()
	bullets.update()

	hits = pygame.sprite.spritecollideany(target, bullets)
	if hits:
		sleep(.2)
		settings.increase_speed()

	for bullet in bullets.copy():
		if bullet.rect.right >= screen_rect.right:
			if not hits:
				stats.misses -= 1
			if stats.misses == 0:
				stats.game_active = False
				pygame.mouse.set_visible(True)
			bullets.remove(bullet)


def update_screen(settings, screen, ship, bullets, target, stats, play_button):
	"""Redraw all game elements and the screen."""
	screen.fill(settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	target.draw_target()

	# Draw the play button if game inactive
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()