#!/usr/bin/env python3
# coding=utf-8
# title          :decorator.py
# description    :An example of decorator
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/11 10:33
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


def decorator(fun):
    def some_fun(a, b):
        print(a, b)
        return fun(a, b)
    return some_fun


# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2


# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))


def decorator(a_class):
    class NewClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = a_class(age)

        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return NewClass


@decorator
class Bird:
    def __init__(self, age):
        self.age = age

    def display(self):
        print("My age is", self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()
