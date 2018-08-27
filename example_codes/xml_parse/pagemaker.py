#!/usr/bin/env python3
# coding=utf-8
# title          :pagemaker.py
# description    :parse xml file to html
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/11 下午3:54
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from xml.sax.handler import ContentHandler
from xml.sax import parse


class HeadlineHandler(ContentHandler):
    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'title':
            self.in_headline = True

    def endElement(self, name):
        if name == 'title':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)


class PageMaker(ContentHandler):
    passthrough = False

    def startElement(self, name, attrs):
        if name == 'entry':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>%s</title>\n' % attrs['title'])
            self.out.write('</head><body>')
        elif self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write('%s="%s"' % (key, val))
                self.out.write('>')

    def endElement(self, name):
        if name == 'entry':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</%s>' % name)

    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)


# get headlines
# headlines = []
# parse('atom.xml', HeadlineHandler(headlines))
parse('atom.xml', PageMaker())
