#!/usr/bin/env python3
# coding=utf-8
# title          :newsagent1.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :12/18/17 1:47 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from nntplib import NNTP
from datetime import date


servername = 'news.easynews.com'
group = 'gmane.comp.python.committers'
server = NNTP(servername)

# newnews need a date object.
ids = server.newnews(group, date.today())[1]

for i in ids:
    head = server.head(i)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject = line[9:]
            break

    body = server.body(i)[3]

    print(subject)
    print('_'*len(subject))
    print('\n'.join(body))

server.quit()
