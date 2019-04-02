#!/usr/bin/env python3
# coding=utf-8
# title          :vector.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2019/4/2 21:19
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x; self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):
        return hypot(self.x, self.y)    # equal sqrt(x*x + y*y)

    def __mul__(self, num):
        return Vector(self.x*num, self.y*num)

    def __bool__(self):
        return bool(abs(self))

    def __rmul__(self, num):
        return Vector(self.x*num, self.y*num)


v1 = Vector(1, 3)
v2 = Vector(3, 4)
v3 = Vector(2, 6)
print(v1+v2+v3)
print(v1*3,abs(v2))
print(4*v1)
