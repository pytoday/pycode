#!/usr/bin/env python3
# coding=utf-8
# title          :diff_mod.py
# description    :example of difflib
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/21 16:19
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import difflib


text1 = """
text1:
This is the first line.
content things.
version 0.1
some things else
"""

text2 = """
text2:
This is the First line.
content things.
version 0.2
some things else
"""

text_line1 = text1.splitlines()
text_line2 = text2.splitlines()

'''
d = difflib.Differ()
diff = d.compare(text_line1, text_line2)
print('\n'.join(list(diff)))
'''

d = difflib.HtmlDiff()
print(d.make_file(text_line1, text_line2))
