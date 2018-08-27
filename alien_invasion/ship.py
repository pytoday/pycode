#!/usr/bin/env python3
# coding=utf-8
# title          :ship.py
# description    :create and init a ship
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/8 上午10:48
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_setting, screen):
        super(Ship, self).__init__()
        # init ship and set startup position.
        self.screen = screen
        self.ai_setting = ai_setting

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set ship to screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # set move flag
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_setting.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        # set position draw ship
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # set ship to the center of bottom
        self.center = self.screen_rect.centerx
