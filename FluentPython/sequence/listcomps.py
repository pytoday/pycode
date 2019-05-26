#!/usr/bin/env python3
# coding=utf-8
# title          :listcomps.py
# description    :
# author         :Jackie4Tsui
# organization   :pytoday.org
# date           :2019/5/26 16:29
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
symbols = '2q3r10235235@?!$#'

# listcomps
beyond_ascii = [ord(c) for c in symbols if ord(c)> 100]
print(beyond_ascii)

# filter & map
beyond_ascii = list(filter(lambda c: c>100, map(ord, symbols)))
print(beyond_ascii)

# X * Y
colors = ['red', 'blue', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

tshirts = ((color, size) for color in colors for size in sizes)
for tshirt in tshirts:
    print(tshirt)
