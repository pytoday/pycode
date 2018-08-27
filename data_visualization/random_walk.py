#!/usr/bin/env python3
# coding=utf-8
# title          :random_walk.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/20 下午5:09
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

from random import choice
import matplotlib.pyplot as plt


class Randomwalk:
    """a class of random walk"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # random start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """walk all point"""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    rw = Randomwalk()
    rw.fill_walk()
    # plt.scatter(rw.x_values, rw.y_values, s=15)
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
    # set start and end point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)
    # hidden label
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # set windows size
    # plt.figure(dpi=128, figsize=(10, 6))
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n' or keep_running == 'N':
        break

rw1 = Randomwalk()
rw1.fill_walk()
point_numbers1 = list(range(rw1.num_points))
plt.plot(rw1.x_values, rw1.y_values, linewidth=8)
plt.show()

