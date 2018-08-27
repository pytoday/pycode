#!/usr/bin/env python3
# coding=utf-8
# title          :bs4Eaxmple.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/27 17:23
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from urllib.request import urlopen
from bs4 import BeautifulSoup


text = urlopen(r'https://www.python.org/jobs').read()
soup = BeautifulSoup(text, "lxml")

jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links:
        continue
    link = links[0]
    jobs.add("%s (%s)" % (link.string, link['href']))

print("\n".join(sorted(jobs, key=lambda s: s.lower())))
