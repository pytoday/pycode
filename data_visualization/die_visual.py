#!/usr/bin/env python3
# coding=utf-8
# title          :die_visual.py
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
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')
