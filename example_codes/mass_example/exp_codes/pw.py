#!/usr/bin/env python3
# coding=utf-8
# pw.py -An insecure password locker program
# 测试
import sys
import pyperclip

PASSWORD = {'mail':'asdgawetasdf', 'blog':'asdgasdgasdf'}
if len(sys.argv) < 2:
    print('Usage: python3 pw.py [account] - copy account password.')
    # print(sys.argv)
    sys.exit()

account = sys.argv[1]   # first argv is account name.

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('No account ' + account + ' in password lib.')
