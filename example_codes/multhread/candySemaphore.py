#!/usr/bin/env python3
# coding=utf-8
# title          : candySemaphore.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/30 15:02
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep


def refill():
    lock.acquire()
    print("Refilling candy ...")
    try:
        candytray.release()
    except ValueError:
        print("Full, skipping...")
    else:
        print("Refilling ok.")
    lock.release()


def buy():
    lock.acquire()
    print("Buying candy...")
    if candytray.acquire(False):    # if candytray is empty return False.   candy_count - 1
        print("OK")
    else:
        print("empty, skipping...")
    lock.release()


def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def main():
    print("starting at:", ctime())
    nloops = randrange(2, 6)
    print("THE CANDY MACHINE (full with %d bars)!" % MAX)
    Thread(target=producer, args=(nloops,)).start()     # V()
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+5),)).start()    # P()


@register
def _atexit():
    print("ALL DONE at:", ctime())


if __name__ == '__main__':
    lock = Lock()
    MAX = 5
    candytray = BoundedSemaphore(MAX)

    main()
