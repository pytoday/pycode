#!/usr/bin/env python3
# coding=utf-8
# title          : uni_cgi.py
# description    : unicode cgi
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/14 22:18
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
code = 'UTF-8'
unicode_hello = u'''
Hello!
\u00A1Hola!
\u4F60\u597D
'''

print('Content-Type: text/html; charset=%s\n\n' % code)
print('<html><head><title>Unicode Demo</title></head>')
print('<body>')
print(unicode_hello)
print('</body></html>')
