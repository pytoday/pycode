#!/usr/bin/env python3
# coding=utf-8
# title          :scatter_squares.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/20 下午4:53
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import matplotlib.pyplot as plt

# plt.scatter(2, 5, s=200)
x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

# plt.scatter(x_value, y_value, s=40)
# plt.scatter(x_value, y_value, c='red', edgecolor='none', s=5)
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolor='none', s=5)

plt.title('This is title', fontsize=14)
plt.xlabel('xlabel', fontsize=10)
plt.ylabel('ylabel', fontsize=10)

# plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()

# plt.savefig('squares_plot.png', bbox_inches='tight')
