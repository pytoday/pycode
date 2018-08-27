#!/usr/bin/env python3
# coding=utf-8
# title          :mpl_squares.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/20 下午4:39
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]

plt.plot(input_values, squares, linewidth=5)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

