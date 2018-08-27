#!/usr/bin/env python3
# coding=utf-8
# title          : parse_links.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/22 6:19
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import xml
from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup, SoupStrainer
from html5lib import parse


URLs = ('https://python.org', 'https://google.com')


def output(x):
    print('\n'.join(sorted(set(x))))


def simplebs(url, f):
    """simplebs() - use bs4 to parse all tags to get anchors."""
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))


def fasterbs(url, f):
    """fasterbs() - use bs4 to parse only anchor tags"""
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, "html.parser", parse_only=SoupStrainer('a')))


def htmlparser(url, f):
    """htmlparser() - user HTMLParser to parse anchor tags."""
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])

    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)


def html5libparse(url, f):
    """html5parse() - use html5lib to parse anchor tags."""
    output(urljoin(url, x.attributes['href']) for x in parse(f) if isinstance(x, xml.etree.cElementTree.Element) and x.name == 'a')


def process(url, data):
    print('\n*** simple bs')
    simplebs(url, data)
    data.seek(0)    # 文件指针
    print('\n*** faster bs')
    fasterbs(url, data)
    data.seek(0)
    print('\n*** HTMLParse')
    htmlparser(url, data)
    data.seek(0)
    print('\n*** HTML5lib parser')
    html5libparse(url, data)


def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read().decode('utf-8'))
        f.close()
        process(url, data)


if __name__ == '__main__':
    main()
