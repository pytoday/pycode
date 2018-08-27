#!/usr/bin/env python3
# coding=utf-8
# title          :simple_markup.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/30 下午5:46
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys
import re
from util import *


print('<html><head><title>....</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
        print('</body></html>')
