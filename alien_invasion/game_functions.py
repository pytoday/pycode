#!/usr/bin/env python3
# coding=utf-8
# title          :game_functions.py
# description    :store game functions
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/8 下午3:29
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import os
import sys
from time import sleep

import pygame
sys.path.extend(os.getcwd())
from .bullet import Bullet
from .alien import Alien


def ship_hit(ai_setting, stats, screen, sb, ship, aliens, bullets):
    """alien hit ship?"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.pre_ship()

        # clear aliens and bullets
        aliens.empty()
        bullets.empty()

        # reset ship and create fleet of aliens
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def get_numbers_alien_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_row(ai_setting, ship_height, alien_height):
    """available lines for aliens"""
    available_space_y = ai_setting.screen_height - (3 * alien_height) - ship_height
    numbers_row = int(available_space_y / (2 * alien_height))
    return numbers_row


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)


def create_fleet(ai_setting, screen, ship, aliens):
    """create a lot of aliens"""
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_numbers_alien_x(ai_setting, alien.rect.width)
    number_rows = get_number_row(ai_setting, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_events(ai_setting, screen, stats, play_button, sb, ship, aliens, bullets):
    # monitor mouse and keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats, play_button, sb, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_setting, screen, stats, play_button, sb, ship, aliens, bullets, mouse_x, mouse_y):
    """while click play button , start game"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_setting.initialize_speed()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        # reset score board
        sb.pre_score()
        sb.pre_high_score()
        sb.pre_level()
        sb.pre_ship()

        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # update screen and pic
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_setting, screen, stats, sb, ship, bullets, aliens):
    # fire bullet
    bullets.update()
    # delete disappeared bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))
    check_bullet_alien_collisions(ai_setting, screen, stats, sb, ship, bullets, aliens)


def check_bullet_alien_collisions(ai_setting, screen, stats, sb, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, ai_setting.supper_bullet, True)
    if collisions:
        # stats.score += ai_setting.alien_point
        for alien in collisions.values():
            stats.score += ai_setting.alien_point * len(alien)
            sb.pre_score()
        check_high_score(stats, sb)
    # delete all aliens? create fleet aliens
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        stats.level += 1
        sb.pre_level()
        create_fleet(ai_setting, screen, ship, aliens)


def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def check_fleet_edges(ai_setting, aliens):
    """check alien reach edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def check_alien_bottom(ai_setting, stats, screen, sb, ship, aliens, bullets):
    """check alien reach the screen of bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_setting, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, sb, ship, aliens, bullets)
    check_alien_bottom(ai_setting, stats, screen, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.pre_high_score()
