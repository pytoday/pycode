#!/usr/bin/env python3
# coding=utf-8
# title          :die.py
# description    :a class of die
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/21 下午9:57
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
