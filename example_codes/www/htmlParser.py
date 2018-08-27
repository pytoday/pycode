#!/usr/bin/env python3
# coding=utf-8
# title          :htmlParser.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/27 17:05
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from urllib.request import urlopen
from HTMLParser import HTMLParser


class Scraper(HTMLParser):
    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h3":
            self.in_h3 = True
        if tag == "a" and "href" in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == "h3":
            self.in_h3 = False
        if tag == "a":
            if self.in_h3 and self.in_link:
                print("%s, %s" % (' '.join(self.chunks,), self.url))
            self.in_link = False


text = urlopen(r'https://python.org/community/jobs').read()
parser = Scraper()
parser.feed(text)
parser.close()
