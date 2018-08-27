#!/usr/bin/env python3
# coding=utf-8
# title          :threadDemo.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/7/14 5:34
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import threading
import time

print('Start of program...')
def takeANap():
    time.sleep(6)
    print('Wake Up!!!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of program.')