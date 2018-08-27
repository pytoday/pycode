#!/usr/bin/env python3
# coding=utf-8
# title          :settings.py
# description    :settings for project alien invasion
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/7 下午11:20
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


class Settings:
    # store all settings for alien invasion

    def __init__(self):
        # init settings for game
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # set ship speed
        self.ship_limit = 2

        # bullet setting
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000

        # alien down to bottom speed
        self.fleet_drop_speed = 3
        # -1: move to left. 1:move to right
        self.fleet_direction = 1

        # set speedup scale percent
        self.speedup_scale = 50

        # True:NOT super bullet (delete bullet), False: super bullet (not delete bullet)
        self.supper_bullet = True

        # set base alien point
        self.alien_point = 50

        # init speed
        self.initialize_speed()

    def initialize_speed(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        # set alien speed
        self.alien_speed_factor = 1

    def increase_speed(self):
        self.ship_speed_factor *= (1 + self.speedup_scale/100)
        self.bullet_speed_factor *= (1 + self.speedup_scale/100)
        self.alien_speed_factor *= (1 + self.speedup_scale/100)
        # set alien points
        self.alien_point = int(self.alien_point * (1 + self.speedup_scale/100))
