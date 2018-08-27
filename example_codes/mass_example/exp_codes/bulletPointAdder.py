#!/usr/bin/env python3
# coding=utf-8

# 测试
import pyperclip
import pprint

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '*==* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
print('Formated text copied in clip board. copied text is:')
pprint.pprint(text)