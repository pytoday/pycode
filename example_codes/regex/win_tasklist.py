#!/usr/bin/env python3
# coding=utf-8
# title          : win_tasklist.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/12 4:38
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import re


with open('./win_task.txt') as f:
    for line in f.readlines():
        print(re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) (?:\w+)\s\s+(?:\d+)\s\s+([\d,]+ K)', line.rstrip()))
