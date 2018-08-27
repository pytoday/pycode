#!/usr/bin/env python3
# coding=utf-8
# title          :game_stats.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/10 下午11:18
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


class GameStats:
    def __init__(self, ai_settings):
        """init information of stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """init changed stats"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0