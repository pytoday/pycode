#!/usr/bin/env python3
# coding=utf-8
# title          :scoreboard.py
# description    :a class of scoreboard
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/18 3:34
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import sys
import os

import pygame.font
from pygame.sprite import Group

sys.path.extend(os.getcwd())
from .ship import Ship


class Scoreboard:
    """display score info"""
    def __init__(self, ai_settings, screen, stats):
        """init scoreboard properties"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font and color set
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare score
        self.pre_score()
        self.pre_high_score()
        self.pre_level()
        self.pre_ship()

    def pre_score(self):
        """convert score strings to image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def pre_high_score(self):
        """convert high score to image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # draw high score on screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def pre_level(self):
        """convert level to image"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # draw level on screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def pre_ship(self):
        """show ship left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """display score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
