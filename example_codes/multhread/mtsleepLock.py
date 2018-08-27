#!/usr/bin/env python3
# coding=utf-8
# title          : mtsleepLock.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/30 14:06
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import ctime, sleep


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock()   # create global lock
loops = [randrange(2, 5) for x in range(randrange(3, 7))]
remaining = CleanOutputSet()


def loop(nsec):
    myname = current_thread().name
    lock.acquire()
    remaining.add(myname)
    print("[%s] Started %s" % (ctime(), myname))
    lock.release()
    sleep(nsec)     # thread main code here
    lock.acquire()
    remaining.remove(myname)
    print("[%s] Completed %s (%d secs)" % (ctime(), myname, nsec))
    print(" (remaining: %s)" % (remaining or 'NONE'))
    lock.release()


def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print("ALL DONE at:", ctime())


if __name__ == '__main__':
    main()
