#!/usr/bin/env python3
# coding=utf-8
# title          :bullet.py
# description    :class of bullet
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/8 下午5:27
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # define a class of shoot bullet
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rect of bullet, and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet y ray position
        self.y = float(self.rect.y)

        # set bullet color and speed
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # fire bullet all the time
        self.fire_bullet = False

    def update(self):
        # update bullet position
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
