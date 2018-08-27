#!/usr/bin/env python3
# coding=utf-8
# title          :guessCoin.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/5/20 16:36:01
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

randNum = random.randint(0, 1) # 0 is tails, 1 is heads
if randNum == 1:
    toss = 'heads'
else:
    toss = 'tails'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess=''
    while guess not in('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')