#!/usr/bin/env python3
# coding=utf-8
# title          :numberlines.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/11 15:08
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import fileinput


sw = False  # switch to inplace or not
for line in fileinput.input(inplace=sw):
    line = line.rstrip()
    num = fileinput.lineno()
    print('%-55s # %2i' % (line, num))
