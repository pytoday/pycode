#!/usr/bin/env python3
# coding=utf-8
# title          :alien.py
# description    :create class of alien
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/9 下午6:14
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class of alien"""
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.ai_setting = ai_setting
        self.screen = screen

        # load alien image.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien positon
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien in some position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move to left or right"""
        self.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction
        self.rect.x = self.x
