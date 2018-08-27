#!/usr/bin/env python3
# coding=utf-8
# title          : crawl.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/21 11:14
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os
import sys
from html.parser import HTMLParser
from urllib import request
from urllib.parse import urlparse
from http import client


class Retriever:
    __slots__ = ('url', 'file')

    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        """Create usable local filename from url"""
        parsed = urlparse(url)
        host = parsed.netloc.split('@')[-1].split(":")[0]   # netlocl get host(www.aaa.com).
        filepath = '%s%s' % (host, parsed.path)     # parsed.path get url path

        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath, default)
        linkdir = os.path.dirname(filepath)

        if not os.path.isdir(linkdir):
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        """Download url to specific named file"""
        try:
            retval = request.urlretrieve(self.url, self.file)
        except (IOError, client.InvalidURL) as e:
            retval = (('***Error: bad url "%s":%s' % (self.url, e)), )
        return retval

    def parse_links(self):
        """Parse links found in downloaded html file"""
        with open(self.file) as f:
            data = f.read()
        # p = parser.HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(StringIO())))
        p = HTMLParser()
        parse = p.feed(data)
        p.close()
        return parse


class Crawler:
    count = 0

    def __init__(self, url):
        self.q = [url]
        self.seen = set()
        parsed = request.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])

    def get_page(self, url, media=False):
        """Download page & parse links, add to queue"""
        r = Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            print(fname, '... skip parse.')
            return
        Crawler.count += 1
        print('\n(', Crawler.count, ')')
        print('URL:', url)
        print('FILE:', fname)
        self.seen.add(url)
        ftype = os.path.splitext(fname)[1]
        if ftype not in ('.htm', '.html'):
            return

        for link in r.parse_links():
            if link.startwith('mailto:'):
                print('... discarded, mail link.')
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3', '.mp4', '.m4v', '.wav'):
                    print('...discarded, media file.')
                    continue
            if not link.startwith('http://'):
                link = request.urljoin(url, link)
            print('*', link)
            if link not in self.seen:
                if self.dom not in link:
                    print('... discarded. not in domain')
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print('... new. added to Q')
                    else:
                        print('... discarded. already in Q')
            else:
                print('... discarded. processed.')

    def go(self, media=False):
        """Process next page in queue"""
        while self.q:
            url = self.q.pop()
            self.get_page(url, media)


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = input("Enter URL:")
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url:
        return
    if not url.startswith('http://') and not url.startswith('ftp://'):
        url = 'http://%s/' % url
    robot = Crawler(url)
    robot.go()


if __name__ == '__main__':
    main()
