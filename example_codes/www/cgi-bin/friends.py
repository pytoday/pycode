#!/usr/bin/env python3
# coding=utf-8
# title          : friends.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/12 16:42
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import cgi


reshtml = '''Content-Type: text/html\n
<html>
    <head><title>CGI Demo</title></head>
<body>
<h3>Friend list for: <i>%s</i></h3>
Your name is : <b>%s</b>
You have <b>%s</b> friends
</body>
</html>
'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml % (who, who, howmany))
