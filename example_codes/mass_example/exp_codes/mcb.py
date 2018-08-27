#!/usr/bin/env python3
# coding=utf-8
# title          :mcb.py
# description    :multiple clipboard
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/5/4 22:44:35
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Usage: py.exe mcb.py save <keyword> - save clipboard content to keyword.
#       py.exe mcb.py del <keyword> - del saved keyword.
#       py.exe mcb.py <keyword> - Load saved content to clipboard
#       py.exe mcb.py list - List all keywords
#       py.exe mcb.py del - Del all keywords 

# Import the module needed to run the script
import pyperclip
import sys
import shelve

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
    else:
        print(str(sys.argv[2]) + ' already deleted.')
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(list(mcbShelf.keys()))    # python2中keys()方法返回的是列表，python3中 keys()方法返回的是迭代器:scream:python3中通过list转为列表
    elif sys.argv[1].lower() == 'del':
        mcbShelf.clear()
        if not mcbShelf:
            print('All content cleaned.')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print('Key ' + sys.argv[1] + ' Not Found.')

mcbShelf.close()