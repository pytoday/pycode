#!/usr/bin/env python3
# coding=utf-8
# title          :diffrent_dice.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/21 下午9:59
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


import sys
import os
import pygal

sys.path.extend(os.getcwd())
from die import Die


die = Die()
die1 = Die(10)
results = []

for roll_num in range(1000):
    result = die.roll() + die1.roll()
    results.append(result)

frequencies = []
max_results = die.num_sides + die1.num_sides
for value in range(1, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Result of rolling  D6+D10 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6+D10", frequencies)
hist.render_to_file('different_dice.svg')
