#!/usr/bin/env python3
# coding=utf-8
# title          : bookrank.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/30 11:07
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib import request


REGEX = compile('#([\d,]+) in Books')
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}


def get_rank(isbn):
    url = '%s%s' % (AMZN, isbn)
    head = dict()
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
        62.0.3202.94 Safari/537.36"
    req = request.Request(url, headers=head)
    page = request.urlopen(req)
    data = page.read().decode('utf-8')
    page.close()
    return REGEX.findall(data)[0]


def show_rang(isbn):
    print('- %r ranked %s' % (ISBNs[isbn], get_rank(isbn)))     # %r repr method


def main():
    print("AT", ctime(), "on Amazon...")
    """ single thread
        show_rang(isbn)
    """
    for isbn in ISBNs:
        Thread(target=show_rang, args=(isbn,)).start()


@register
def _atexit():
    print("All DONE at: ", ctime())


if __name__ == '__main__':
    main()
