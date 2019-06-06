#!/usr/bin/env python3
# coding=utf-8
# title          :loop_tuple.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2019/6/6 17:11
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.20889))
]

print('|{:^15}|{:^9}|{:^9}|'.format('name', 'lat.', 'long'))
fmt='|{:^15}|{:^9.3f}|{:^9.3f}|'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude > 50:
        print(fmt.format(name, latitude, longitude))
