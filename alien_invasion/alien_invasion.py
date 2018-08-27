#!/usr/bin/env python3
# coding=utf-8
# title          :alien_invasion.py
# description    :alien invasion main program.
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/7 下午10:59
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import pygame
from pygame.sprite import Group
from .settings import Settings
from .ship import Ship
from . import game_functions as gf
from .game_stats import GameStats
from .button import Button
from .scoreboard import Scoreboard


def run_game():
    # init a game screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion[外星飞船]')

    # create start button
    play_button = Button(ai_settings, screen, 'Play')

    # set game status
    stats = GameStats(ai_settings)

    # create score board
    sb = Scoreboard(ai_settings, screen, stats)

    # create a ship
    ship = Ship(ai_settings, screen)
    # create a set of bullet
    bullets = Group()
    # create a lot of aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start main loop
    while True:

        # monitor mouse and keyboard
        gf.check_events(ai_settings, screen, stats, play_button, sb, ship, aliens, bullets)
        if stats.game_active:
            # move ship
            ship.update()
            # update and draw bullets
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            # update aliens
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        # set background color and draw ship
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
