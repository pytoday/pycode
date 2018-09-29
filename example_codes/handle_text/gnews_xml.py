#!/usr/bin/env python3
# coding=utf-8
# title          : gnews_xml.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/29 20:31
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

try:
    from itertools import izip as zip
except ImportError:
    pass

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from pprint import pprint
from xml.etree import ElementTree

g = urlopen('https://news.google.com/news?topic=h&output=rss')
f = StringIO(g.read())
g.close()
tree = ElementTree.parse(f)
f.close()

def topnews(count=5):
    pair = [None, None]
    for elm in tree.getiterator():
        if elm.tag == 'title':
            skip = elm.text.startswith('Top Stories')
            if skip:
                continue
            pair[0] = elm.text
        if elm.tag == 'link':
            if skip:
                continue
            pair[1] = elm.text
            if pair[0] and pair[1]:
                count -= 1
                yield (tuple(pair))
                if not count:
                    return
                pair = [None, None]


for news in topnews():
    pprint(news)
