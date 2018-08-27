#!/usr/bin/env python3
# coding=utf-8
# title          :stopWatch.py
# description    :A simple stopwatch
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/7/14 4:04
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import time

print('Press ENTER to start, ENTER to continue,  and Ctrl+C to stop.')
print('Ready to go...')
input()
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s(%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:   # handle the Ctrl-C exception.
    print('\nDone.')
