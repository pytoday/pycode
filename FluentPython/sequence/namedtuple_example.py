#!/usr/bin/env python3
# coding=utf-8
# title          :namedtuple_example.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2019/6/6 17:27
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from collections import namedtuple

City = namedtuple('City','name country population coordinates')
LatLong = namedtuple('LatLong', 'latitude longitude')

tokyo = City('Tokyo', 'JP', 36.933, LatLong(35.698722, 139.691667))
print('|{:^15}|{:^8}|{:^9.3f}|{:^9.4f}|{:^9.4f}|'.format(tokyo.name, tokyo.country, tokyo.population, tokyo.coordinates.latitude, tokyo.coordinates.longitude))
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)      # same as City(*delhi_data)
for key, value in delhi._asdict().items():
    print(key + " : ", value)