#!/usr/bin/env python3
# coding=utf-8
# title          : linux_who.txt.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/12 4:29
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import re

with open('./linux_who.txt') as fd:
    for line in fd:
        print(re.split(r'\s\s+|\t', line.rstrip()))

