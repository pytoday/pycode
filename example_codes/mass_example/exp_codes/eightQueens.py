#!/usr/bin/env python3
# coding=utf-8
# title          :eightQueens.py
# description    :eightQueens
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/10 20:51
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import random


def conflict(state, next_x):
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i]-next_x) in (0, next_y-i):
            # state[i]-next_x=0为同一列(x坐标相同)，abs(state[i])-next_x)=next_y-i为对角线(x,y坐标差值相同)
            return True
    return False


'''
def queens(num=8, state=()):
    if len(state) == num-1:   # check is last queen?
        for pos in range(num):
            if not conflict(state, pos):
                yield (pos,)
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result
'''


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. '*pos + 'X ' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))


prettyprint(random.choice(list(queens(8))))
