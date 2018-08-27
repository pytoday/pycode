#!/usr/bin/env python3
# coding=utf-8
# title          : bookrankPool.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/30 16:16
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib import request


def get_rank(isbn):
    url = '%s%s' % (AMZN, isbn)
    head = dict()
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
        62.0.3202.94 Safari/537.36"
    req = request.Request(url, headers=head)
    with request.urlopen(req) as page:
        return REGEX.findall(page.read().decode('utf-8'))[0]


def main():
    print("At", ctime(), "on Amazon...")
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(get_rank, ISBNs)):
            print("- %r ranked %s" % (isbn, ranking))
    print("All DONE at:", ctime())


if __name__ == '__main__':
    REGEX = compile('#([\d,]+) in Books')
    AMZN = 'https://www.amazon.com/dp/'
    ISBNs = {
        '0132269937': 'Core Python Programming',
        '0132356139': 'Python Web Development with Django',
        '0137143419': 'Python Fundamentals',
    }
    main()
