#!/usr/bin/env python3
# coding=utf-8
# title          :signal.py
# description    :A script to test module signal
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/7/28 2:46
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import signal

# Define signal handler function
def myHandles(signum, frame):
    print('I received:', signum)

# Register signal.SIGSTP's handler
# signal.signal(signal.SIGBREAK, myHandles)
signal.signal(signal.SIGSTP, myHandles)
signal.pause()
print('End of Signal Demo')
